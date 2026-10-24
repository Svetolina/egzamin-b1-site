# Тест на пересказ: 4 слова подряд из наших польских текстов, совпадающие с корпусом учебников.
import json, glob, re, sys
W = re.compile(r"[a-ząćęłńóśźż]+")
def words(s): return W.findall(s.lower())
grams = set()
for f in glob.glob('/home/claude/corpus/*.txt'):
    w = words(open(f, errors='ignore').read())
    grams.update(tuple(w[i:i+4]) for i in range(len(w)-3))
def texts(t):
    out = []
    for s in t['theory']:
        for b in s['blocks']:
            raw = json.dumps(b, ensure_ascii=False)
            out += re.findall(r'\[\[(.+?)\]\]', raw)
            if b['type'] == 'ex': out += [i['pl'] for i in b['items']]
    for e in t['exercises']:
        if e.get('passage'): out.append(re.sub(r'\{\d+\}', '|', e['passage']))
        for k in ('model', 'model_future'):
            v = e.get(k)
            if v: out += v if isinstance(v, list) else [v]
        for it in e.get('items', []):
            q = it['q']
            for part in re.split(r'→', q):
                a = it['a'][0] if it['a'] else ''
                out.append(part.replace('___', a))
    return out
slugs = sys.argv[1:] or [p.split('/')[1] for p in sorted(glob.glob('out/*/topic.json'))]
for s in slugs:
    t = json.load(open(f'out/{s}/topic.json')); hits = []
    for x in texts(t):
        for seg in re.split(r'[|.!?;:«»„”"()\[\]—–]', x):
            w = words(seg)
            for i in range(len(w)-3):
                g = tuple(w[i:i+4])
                if g in grams: hits.append(' '.join(g))
    print(s, len(set(hits)), sorted(set(hits)))
