import json, re, glob, morfeusz2, sys
m = morfeusz2.Morfeusz()
D = '/home/claude/zo/zaimki-osobowe'
T = json.load(open(f'{D}/topic.json')); X = json.load(open(f'{D}/extract.json'))
errs, warn = [], []
NAMES = {'Marek','Marka','Ewa','Ewo','Ania','Ani','Anną','Tomka','Tomek','Kasiu','Kasia','Ola','Oli','Oly','Magdo','Paweł','Japonii','Adam','Olga'}
def an(w): return m.analyse(w)
def known(w):
    a = an(w)
    return any(x[2][2] != 'ign' for x in a)
def words(s):
    s = re.sub(r'\*\*.*?\*\*', ' ', s)
    return re.findall(r"[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż]+", s)

# 1. формы
for f in X['forms']:
    ok = False
    for _,_,(orth,lem,tag,*r) in an(f['form']):
        lem = lem.split(':')[0]
        if lem == f['lemma'] and f':{f["case"]}' in tag and f':{f["n"]}:' in tag+':' :
            ok = True
    if not ok: errs.append(f"form {f}")
# 2. известные слова
pl_texts = []
for t in T['theory']:
    for b in t['blocks']:
        js = json.dumps(b, ensure_ascii=False)
        pl_texts += re.findall(r'\[\[(.+?)\]\]', js)
        if b['type']=='table':
            for row in b['rows']:
                for i in b['pl_cols']: pl_texts.append(row[i])
        if b['type']=='ex': pl_texts += [i['pl'] for i in b['items']]
        if b['type']=='fix': pl_texts += [i['good'] for i in b['items']]
        if b['type']=='chips': pl_texts += b['items']
tids = {t['id'] for t in T['theory']}
fids = {f['id'] for f in X['facts']} | {'EXAM'}
for t in T['theory']:
    for f in t['facts']:
        if f not in fids: errs.append(f'theory {t["id"]} fact {f}')
for e in T['exercises']:
    if e['kind']=='write':
        pl_texts.append(e['model'])
        n = len(words(e['model']))
        if not (e['words'][0] <= n <= e['words'][1]): errs.append(f'model length {n}')
        for f in e['model_future']:
            if f not in e['model']: errs.append(f'model lacks {f}')
        continue
    if e['kind']=='text': pl_texts.append(re.sub(r'\{\d+\}',' ',e['passage']))
    for it in e['items']:
        if it['t'] not in tids: errs.append(f'{e["id"]} t {it["t"]}')
        pl_texts.append(it['q']); pl_texts += it['a']
        if 'opts' in it and it['a'][0] not in it['opts']: errs.append(f'{e["id"]} answer not in opts {it["q"]}')
unk = set()
for s in pl_texts:
    for w in words(s):
        if w in NAMES or len(w)<=2: continue
        if not known(w) and not known(w.lower()): unk.add(w)
if unk: warn.append(f'unknown: {sorted(unk)}')

# 3. грамматика ответов
PREP = {'do','dla','z','ze','o','na','u','bez','obok','w','za','przed','przede','od','po','przez','dzięki'}
CASE = {'родительн':'gen','дательн':'dat','винительн':'acc','творительн':'inst','предложн':'loc'}
for e in T['exercises']:
    if e['kind'] in ('write',): continue
    for k,it in enumerate(e['items']):
        q = it['q']
        if e['kind']=='text':
            idx = k+1; q = e['passage'].replace('{%d}'%idx,'___')
        before = q.split('___')[0] if '___' in q else q.split('**')[0]
        prev = (words(before) or [''])[-1].lower()
        initial = before.strip()=='' or before.rstrip().endswith(('.','!','?','→','–'))
        for a in it['a']:
            tags = [x[2][2] for x in an(a.lower()) if x[2][1].split(':')[0] in ('ja','ty','on','my','wy')]
            if not tags: errs.append(f'{e["id"]}#{k+1} {a}: не местоимение'); continue
            if prev in PREP and not any('praep' in t and 'npraep' not in t.replace('praep.npraep','') or ('ppron12' in t and ':nakc' not in t) for t in tags):
                errs.append(f'{e["id"]}#{k+1} {a}: после предлога {prev} нужна praep/длинная')
            if prev not in PREP and any(t.endswith(':praep') for t in tags) and not any('npraep' in t for t in tags):
                errs.append(f'{e["id"]}#{k+1} {a}: форма с n- без предлога')
            al=a.lower()
            if prev not in PREP and (al in ('niego','niemu','niej','nich','nie') or (al=='nią' and 'творительн' not in it['expl'])):
                errs.append(f'{e["id"]}#{k+1} {a}: форма с n- без предлога')
            if initial and all(':nakc' in t and 'akc.nakc' not in t for t in tags):
                errs.append(f'{e["id"]}#{k+1} {a}: краткая форма в начале фразы')
            for ru,c in CASE.items():
                if ru in it['expl'] and not any(f':{c}:' in t for t in tags):
                    errs.append(f'{e["id"]}#{k+1} {a}: ожидался {c}, теги {tags}')
print('ERRORS', len(errs)); [print(' ',x) for x in errs]
print('WARN'); [print(' ',x) for x in warn]
print('polish fragments', len(pl_texts))
