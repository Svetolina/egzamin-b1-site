"""Общие помощники для сборки textbook-src/<topic>/{extract,topic}.json."""
import json, os, re

ROOT = '/home/claude/textbook-src'


def S(title, url, loc):
    return {"title": title, "url": url, "loc": loc}


def variants(ans, aby=False):
    """ans: str | list[str]; '/'-separated alternatives inside one string allowed.
    aby=True additionally accepts the same answer with aby instead of żeby."""
    if isinstance(ans, str):
        ans = [a.strip() for a in ans.split('|')]
    out = []
    for a in ans:
        out.append(a)
        if aby and a.startswith('żeby'):
            out.append('aby' + a[4:])
    seen = []
    for a in out:
        if a not in seen:
            seen.append(a)
    return seen


def item(q, *answers, hint=None, aby=False, note=None):
    """one positional answer per gap {1},{2}...; each 'a|b' string or list."""
    gaps = [variants(a, aby) for a in answers]
    d = {"q": q, "a": gaps}
    if hint:
        d["hint"] = hint
    if note:
        d["note"] = note
    return d


def ex(eid, title, kind, instr, items, facts, example=None, fmt=None):
    d = {"id": eid, "title": title, "kind": kind, "instr": instr,
         "facts": facts, "items": items}
    if example:
        d["example"] = example
    if fmt:
        d["format"] = fmt
    return d


def validate(topic, extract):
    ids = {f["id"] for f in extract["facts"]}
    errs = []
    for f in extract["facts"]:
        if len(f["sources"]) < 2 and not f.get("single_source_note"):
            errs.append(f"{f['id']}: <2 sources without note")
    for s in topic["sections"]:
        for r in s.get("facts", []):
            if r not in ids:
                errs.append(f"section {s['id']}: unknown fact {r}")
    total = 0
    for e in topic["exercises"]:
        for r in e.get("facts", []):
            if r not in ids and not r.startswith('T'):
                errs.append(f"{e['id']}: unknown fact {r}")
        if e["kind"] == "writing":
            continue
        for i, it in enumerate(e["items"], 1):
            n = len(re.findall(r'\{\d+\}', it["q"]))
            if n != len(it["a"]):
                errs.append(f"{e['id']}#{i}: {n} gaps vs {len(it['a'])} answers: {it['q']}")
            for g in it["a"]:
                if not g or any(not x for x in g):
                    errs.append(f"{e['id']}#{i}: empty answer")
            total += n
    return errs, total


def save(slug, extract, topic):
    errs, total = validate(topic, extract)
    if errs:
        raise SystemExit("\n".join(errs))
    topic["stats"] = {"gaps": total,
                      "exercises": len([e for e in topic["exercises"] if e["kind"] != "writing"]),
                      "writing": len([e for e in topic["exercises"] if e["kind"] == "writing"]),
                      "sections": len(topic["sections"]),
                      "facts": len(extract["facts"])}
    d = os.path.join(ROOT, slug)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'extract.json'), 'w', encoding='utf-8') as f:
        json.dump(extract, f, ensure_ascii=False, indent=1)
    with open(os.path.join(d, 'topic.json'), 'w', encoding='utf-8') as f:
        json.dump(topic, f, ensure_ascii=False, indent=1)
    print(slug, topic["stats"])
    return d
