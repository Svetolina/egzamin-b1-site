#!/usr/bin/env python3
"""Собирает список тем учебника для сайта: textbook-src/index.js.

Запуск из папки сайта:  python tools/build_textbook_index.py
Запускать после добавления новой темы или переименования разделов/упражнений.
Сайт сам берёт теорию и упражнения из textbook-src/<тема>/topic.json,
а index.js нужен для списка тем и счётчиков (чтобы не грузить все темы сразу).
"""
import json
import os

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(here, "..", "textbook-src")

# порядок тем в разделе «Грамматика»; новые папки, которых тут нет, встают в конец
ORDER = [
    "czas-przyszly", "czas-terazniejszy", "czas-przeszly", "aspekt",
    "biernik", "dopelniacz", "przyimki",
    "narzednik", "miejscownik", "celownik", "wolacz", "mianownik-lm", "dopelniacz-lm", "przypadki-lm", "zaimki-osobowe",
    "tryb-rozkazujacy", "tryb-przypuszczajacy", "czasowniki-ruchu",
    "dopelniacz-po-negacji", "liczebniki-z-rzeczownikami",
    "zdania-ktory", "zeby-aby", "spojniki-przyczyna-przyzwolenie",
    "zaimki-nieokreslone", "swoj-siebie", "stopniowanie",
    "strona-bierna", "mowa-zalezna", "imieslowy-przyslowkowe", "rzeczowniki-odczasownikowe",
]

folders = [d for d in os.listdir(root)
           if not d.startswith(("_", ".")) and os.path.isfile(os.path.join(root, d, "topic.json"))]
folders.sort(key=lambda d: (ORDER.index(d) if d in ORDER else len(ORDER), d))

out = []
for d in folders:
    t = json.load(open(os.path.join(root, d, "topic.json"), encoding="utf-8"))
    ex = t.get("exercises") or []
    out.append({
        "id": d,
        "title_pl": t.get("title_pl", d),
        "title_ru": t.get("title_ru", ""),
        "group": t.get("group", "Грамматика"),
        "level": t.get("level", "B1"),
        "theory": [{"id": s["id"], "title": s.get("title", "")} for s in t.get("theory", [])],
        "exercises": [{"id": e["id"], "title": e.get("title", ""), "level": e.get("level"),
                       "kind": e.get("kind"), "n": len(e.get("items") or []) or 1} for e in ex],
    })

js = ("/* Список тем учебника. Файл собирается скриптом tools/build_textbook_index.py — руками не править. */\n"
      "window.B1_TEXTBOOK=" + json.dumps(out, ensure_ascii=False, indent=1) + ";\n")
open(os.path.join(root, "index.js"), "w", encoding="utf-8").write(js)
print("тем:", len(out), "→ textbook-src/index.js")
for t in out:
    print(" ", t["id"], "·", len(t["theory"]), "разделов,", len(t["exercises"]), "упражнений")
