# Ручная доводка пунктов: fixes/<slug>.py содержит F = {ex_id: {'instr':..., 'items': {номер(1..): {'q':..,'a':[..],'expl':..} | None(удалить)}, 'passage':..}}
import json, sys, importlib.util
slug = sys.argv[1]
spec = importlib.util.spec_from_file_location('f', f'fixes/{slug}.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
p = f'out/{slug}/topic.json'; t = json.load(open(p))
ex = {e['id']: e for e in t['exercises']}
for eid, ch in m.F.items():
    e = ex[eid]
    for k in ('instr', 'title', 'passage'):
        if k in ch: e[k] = ch[k]
    items = ch.get('items', {})
    for n in sorted(items, reverse=True):
        v = items[n]
        if v is None: del e['items'][n-1]; continue
        if n > len(e['items']): e['items'].append(dict(v)); continue
        e['items'][n-1].update(v)
for eid, groups in getattr(m, 'EX', {}).items():
    for nums, expl, tid in groups:
        for n in nums:
            it = ex[eid]['items'][n-1]; it['expl'] = expl; it['t'] = tid
for fn in getattr(m, 'THEORY', []): fn(t)
raw = json.dumps(t, ensure_ascii=False)
for old, new in getattr(m, 'REPL', []):
    if old not in raw: assert new in raw, ('REPL not found', old); continue
    raw = raw.replace(old, new)
t = json.loads(raw)
json.dump(t, open(p, 'w'), ensure_ascii=False, indent=1)
multi = [(e['id'], i+1) for e in t['exercises'] if e['kind'] in ('type','choice') for i, it in enumerate(e['items']) if any(len(a.split()) > 1 for a in it['a'])]
print(slug, 'multi-word left:', multi)
