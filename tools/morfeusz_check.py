#!/usr/bin/env python3
"""Проверка польских форм в файле темы учебника через Morfeusz 2.

Запуск:  python tools/morfeusz_check.py textbook-src/czas-przyszly/extract.json
Нужно:   pip install morfeusz2

Что проверяет:
  1. Каждое польское слово в примерах фактов (поле "pl") есть в словаре
     Morfeusz (иначе — в список на ручную проверку).
  2. Каждая форма из списка "forms" — именно то, что заявлено:
       prosty  — fin:...:perf нужного лица и числа, лемма совпадает;
       byc     — будущее być (класс bedzie) нужного лица и числа;
       zlozony — będę/będziesz/... + инфинитив или форма на -ł
                 несовершенного вида; род/число формы на -ł совпадают с "g".
       teraz   — fin:imperf нужного лица и числа;
       przesz  — praet нужного числа и рода (+ вид, если задан "aspect"),
                 для 1-го и 2-го лица ещё aglt того же лица.
     Формы с "expect_error": true — заведомо неверные примеры; скрипт
     должен найти в них ошибку, иначе это сбой проверки.
  3. У каждого факта есть хотя бы 2 ссылки (refs). Факты со статусом
     conflict / one-rule-source выводятся как нерешённые (не публикуем),
     со статусом marked — как решённые, но публикуемые с пометкой.
Код возврата 1, если есть ошибки.
"""
import json
import os
import re
import sys

import morfeusz2

PERSON = {1: "pri", 2: "sec", 3: "ter"}
GENDER = {  # что допустимо в теге praet для кода рода из файла
    "m": {"m1", "m2", "m3"},
    "f": {"f"},
    "n": {"n"},
    "mo": {"m1"},
    "nmo": {"m2", "m3", "f", "n"},
}
BYC = {"będę", "będziesz", "będzie", "będziemy", "będziecie", "będą"}

morf = morfeusz2.Morfeusz()


def analyses(word):
    """[(lemma, [tag parts])] без служебных меток леммы (np. 'czytać:v')."""
    out = []
    for _s, _e, (_orth, lemma, tag, _q, _st) in morf.analyse(word):
        out.append((lemma.split(":")[0], tag.split(":")))
    return out


def has_parts(tag, *needed):
    return all(any(n in p.split(".") or n == p for p in tag) for n in needed)


def known(word):
    return any(t[0] != "ign" for _l, t in analyses(word))


def check_prosty(f):
    want_p, want_n = PERSON[f["p"]], f["n"]
    for lemma, tag in analyses(f["form"]):
        if tag[0] == "fin" and lemma == f["lemma"] and has_parts(tag, want_n, want_p, "perf"):
            return None
    return f"не найдено fin:{want_n}:{want_p}:perf от «{f['lemma']}»"


def check_byc(f):
    want_p, want_n = PERSON[f["p"]], f["n"]
    for lemma, tag in analyses(f["form"]):
        if lemma == "być" and tag[0] == "bedzie" and has_parts(tag, want_n, want_p):
            return None
    return f"не найдено будущее być {want_n}:{want_p}"


def check_zlozony(f):
    words = f["form"].split()
    if words[0] not in BYC:
        return "первое слово — не будущее być"
    aux = [t for l, t in analyses(words[0]) if l == "być" and t[0] == "bedzie"][0]
    aux_n = aux[1]
    main = [w for w in words[1:] if w != "się"]
    if len(main) != 1:
        return "ожидалось одно основное слово после będę (кроме się)"
    problems = []
    readings = [(l, t) for l, t in analyses(main[0]) if l == f["lemma"]]
    # Омонимы SGJP: «kupić:Vp» (купить) и редкое «kupić:Vi» (скапливать).
    # Если у слова есть и совершенное прочтение, будущее с będę сомнительно.
    both = (any("perf" in t for _l, t in readings) and any("imperf" in t for _l, t in readings))
    for lemma, tag in readings:
        if tag[0] == "inf":
            if "imperf" in tag:
                if both:
                    return "REVIEW: у слова есть и совершенное прочтение (омоним в SGJP) — проверьте вручную"
                return None
            problems.append("инфинитив совершенного вида")
        elif tag[0] == "praet":
            if "imperf" not in tag:
                problems.append("форма на -ł совершенного вида")
                continue
            if both:
                return "REVIEW: у слова есть и совершенное прочтение (омоним в SGJP) — проверьте вручную"
            if tag[1] != aux_n:
                problems.append(f"число: będę… {aux_n}, форма на -ł {tag[1]}")
                continue
            g = f.get("g")
            genders = set(tag[2].split("."))
            if g and not (genders & GENDER[g]):
                problems.append(f"род {tag[2]} не подходит к «{g}»")
                continue
            return None
    return "; ".join(problems) or f"нет инфинитива/формы на -ł от «{f['lemma']}»"


def check_teraz(f):
    """Настоящее время: fin нужного лица и числа от несовершенного глагола."""
    want_p, want_n = PERSON[f["p"]], f["n"]
    for lemma, tag in analyses(f["form"]):
        if tag[0] == "fin" and lemma == f["lemma"] and has_parts(tag, want_n, want_p, "imperf"):
            return None
    return f"не найдено fin:{want_n}:{want_p}:imperf от «{f['lemma']}»"


def check_przesz(f):
    """Прошедшее время: praet нужного числа, рода (и вида, если задан) от нужной
    леммы; для 1-го и 2-го лица — ещё aglt (-m, -ś, -śmy, -ście) того же лица."""
    want_p, want_n = PERSON[f["p"]], f["n"]
    segs = morf.analyse(f["form"])
    praet = [(s, e, l.split(":")[0], t.split(":")) for s, e, (_o, l, t, _q, _st) in segs
             if t.startswith("praet")]
    aglt = [t.split(":") for s, e, (_o, l, t, _q, _st) in segs if t.startswith("aglt")]
    problems = []
    for s, e, lemma, tag in praet:
        if lemma != f["lemma"]:
            continue
        if tag[1] != want_n:
            problems.append(f"число {tag[1]}")
            continue
        if f.get("g") and not (set(tag[2].split(".")) & GENDER[f["g"]]):
            problems.append(f"род {tag[2]} не подходит к «{f['g']}»")
            continue
        if f.get("aspect") and tag[3] != f["aspect"]:
            problems.append(f"вид {tag[3]}")
            continue
        if f["p"] == 3:
            if aglt:
                problems.append("лишнее окончание лица")
                continue
            return None
        if any(a[1] == want_n and a[2] == want_p for a in aglt):
            return None
        problems.append("окончание лица не совпадает")
    return "; ".join(problems) or f"не найдено praet от «{f['lemma']}»"


def check_aspekt(f):
    """Вид глагола: инфинитив с нужным видом (perf / imperf)."""
    tags = [t for l, t in analyses(f["form"]) if t[0] == "inf" and l == f["form"]]
    if not tags:
        return "инфинитив не найден"
    if any(f["aspect"] in t for t in tags):
        if any(("perf" if f["aspect"] == "imperf" else "imperf") in t for t in tags):
            return "REVIEW: Morfeusz знает и второй вид (омоним)"
        return None
    return f"вид не {f['aspect']}"


def check_przyp(f):
    """Падеж: форма от нужной леммы в нужном падеже и числе (subst / adj / ppron / ten)."""
    for lemma, tag in analyses(f["form"]):
        if lemma == f["lemma"] and has_parts(tag, f["n"], f["case"]):
            return None
    return f"не найдено {f['case']}:{f['n']} от «{f['lemma']}»"


CHECKS = {"przesz": check_przesz, "teraz": check_teraz, "prosty": check_prosty, "byc": check_byc, "zlozony": check_zlozony, "aspekt": check_aspekt, "przyp": check_przyp}


WORD = r"(?<![-A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż])[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż]+"


def polish_strings(theory):
    """Все польские фрагменты теории: [[…]], примеры, польские колонки таблиц,
    чипы, верные варианты в «fix». Неверные (bad) не проверяются как слова."""
    out = []
    def marked(s):
        out.extend(re.findall(r"\[\[(.+?)\]\]", s))
    for sec in theory:
        marked(sec.get("title", ""))
        for b in sec["blocks"]:
            t = b["type"]
            if t in ("p", "note"):
                marked(b["text"])
            elif t == "ex":
                out.extend(i["pl"] for i in b["items"])
            elif t == "chips":
                out.extend(b["items"])
            elif t == "fix":
                out.extend(i["good"] for i in b["items"])
            elif t == "steps":
                for i in b["items"]:
                    marked(i)
            elif t == "table":
                for h in b["head"]:
                    marked(h)
                cols = set(b.get("pl_cols", []))
                for row in b["rows"]:
                    for i, cell in enumerate(row):
                        if i in cols:
                            out.append(cell)
                        else:
                            marked(cell)
    return out


def main(path):
    data = json.load(open(path, encoding="utf-8"))
    errors, review, flagged, marked = [], [], [], []

    # 1. все польские слова: примеры фактов и текст теории
    texts = [ex for fact in data.get("facts", []) for ex in fact.get("pl", [])]
    if "theory" in data:
        texts += polish_strings(data["theory"])
    # упражнения: все польские слова заданий, вариантов и ответов
    for e in data.get("exercises", []):
        if e["kind"] == "write":
            texts.append(e["model"])
            for fut in e.get("model_future", []):
                if fut.lower() not in e["model"].lower():
                    errors.append(f"{e['id']}: в образце нет формы «{fut}»")
            n = len(re.findall(WORD, e["model"]))
            lo, hi = e["words"]
            if not lo <= n <= hi:
                errors.append(f"{e['id']}: в образце {n} слов, нужно {lo}–{hi}")
            continue
        if e["kind"] == "text":
            gaps = re.findall(r"\{(\d+)\}", e["passage"])
            if gaps != [str(i + 1) for i in range(len(e["items"]))]:
                errors.append(f"{e['id']}: пропуски в тексте не совпадают с пунктами")
            texts.append(re.sub(r"\{\d+\}", "", e["passage"]))
        for it in e["items"]:
            # **…** — заведомо неверная форма в заданиях «исправьте ошибку»
            texts.append(re.sub(r"\*\*.+?\*\*", "", it["q"]))
            texts += it["a"]  # неверные варианты (opts) — заведомо ошибки, не проверяем
            if it.get("opts") and not set(it["a"]) <= set(it["opts"]):
                errors.append(f"{e['id']}: ответ не среди вариантов: {it['q']}")
            if it.get("t") not in {s["id"] for s in data.get("theory", [])}:
                errors.append(f"{e['id']}: ссылка на несуществующий раздел теории {it.get('t')}")
            if e["kind"] in ("type", "text"):
                for ans in it["a"]:
                    w = [x for x in ans.split() if x != "się"]
                    exp = e.get("expect")
                    if len(w) == 1 and w[0] not in BYC and exp:
                        rd = [t for _l, t in analyses(w[0]) if t[0] == "fin"]
                        if exp == "future" and not any("perf" in t for t in rd):
                            errors.append(f"{e['id']}: ответ «{ans}» — не совершенный глагол (не будущее)")
                        if exp == "present" and not any("imperf" in t for t in rd):
                            errors.append(f"{e['id']}: ответ «{ans}» — не настоящее время")
                        if exp == "past" and not any(t[0] == "praet" for _l, t in analyses(w[0])):
                            errors.append(f"{e['id']}: ответ «{ans}» — не прошедшее время")
                    if w and w[0] in BYC and len(w) == 2:
                        # только инфинитив / форма на -ł; причастие (będzie zbudowany) — это страдательный залог, не ошибка
                        rd = [t for _l, t in analyses(w[1]) if t[0] in ("inf", "praet")]
                        if rd and all("perf" in t and "imperf" not in t for t in rd):
                            errors.append(f"{e['id']}: в ключе będę + совершенный глагол: {ans}")
    unknown = set()
    for ex in texts:
        for w in re.findall(WORD, ex):
            if len(w) > 2 and not known(w):  # буквы и окончания (cz, -y) не слова
                unknown.add(w)
    print(f"Польских фрагментов: {len(texts)}")
    for w in sorted(unknown):
        review.append(f"слово не найдено в Morfeusz: {w}")

    # 2. формы
    ok = 0
    for f in data["forms"]:
        res = CHECKS[f["kind"]](f)
        if f.get("expect_error"):
            if res is None:
                errors.append(f"«{f['form']}»: ожидалась ошибка, но форма прошла проверку")
            else:
                ok += 1
                print(f"  ✓ «{f['form']}» отклонена, как и должно: {res}")
        elif res and res.startswith("REVIEW:"):
            review.append(f"«{f['form']}»: {res[8:]}")
        elif res:
            errors.append(f"«{f['form']}»: {res}")
        else:
            ok += 1

    # 3a. теория ссылается на существующие и решённые факты
    if "theory" in data:
        ff = os.path.join(os.path.dirname(path), data["facts_file"])
        facts = {f["id"]: f for f in json.load(open(ff, encoding="utf-8"))["facts"]}
        extra = {data["exam_ref"]["id"]} if "exam_ref" in data else set()
        for sec in data["theory"]:
            if not sec.get("facts"):
                errors.append(f"{sec['id']}: раздел без ссылок на факты")
            for fid in sec.get("facts", []):
                if fid in extra:
                    continue
                f = facts.get(fid)
                if not f:
                    errors.append(f"{sec['id']}: нет факта {fid} в {data['facts_file']}")
                elif f.get("status", "ok") not in ("ok", "marked"):
                    errors.append(f"{sec['id']}: факт {fid} не решён ({f['status']}) — публиковать нельзя")
                elif f.get("status") == "marked":
                    has_note = any(b["type"] == "note" and b.get("kind") == "mark" for b in sec["blocks"])
                    if not (sec.get("marked") and has_note):
                        errors.append(f"{sec['id']}: факт {fid} публикуется только с пометкой — её нет")
        if "exam_ref" in data and len(data["exam_ref"]["refs"]) < 2:
            errors.append("exam_ref: меньше двух источников")

    # 3. источники
    for fact in data.get("facts", []):
        st = fact.get("status", "ok")
        if st == "marked":
            marked.append(f"{fact['id']}: {fact.get('decision', '')}")
        elif st != "ok":
            flagged.append(f"{fact['id']} [{st}]: {fact.get('proposal', '')}")
        elif len(fact.get("refs", [])) < 2:
            errors.append(f"{fact['id']}: меньше двух источников")

    print(f"\nФорм проверено: {len(data['forms'])}, без замечаний: {ok}")
    for title, items in (("ОШИБКИ", errors), ("НА РУЧНУЮ ПРОВЕРКУ", review),
                         ("НЕРЕШЁННЫЕ ФАКТЫ (не публикуем до решения)", flagged),
                         ("ПУБЛИКУЕМ С ПОМЕТКОЙ", marked)):
        print(f"\n{title}: {len(items)}")
        for i in items:
            print("  -", i)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
