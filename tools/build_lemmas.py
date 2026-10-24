# Сборка assets/js/lemmas.js: pip install morfeusz2; список слов /tmp/words.txt собирается из tests/*.js (см. README)
import morfeusz2,json,re,collections
m=morfeusz2.Morfeusz(expand_tags=False)
words=open('/tmp/words.txt').read().split()
gen_cache={}
def gen_form(verb,kind,neg='aff'):
    # именительный ед.ч. муж. рода причастия / отглагольного существительного
    key=(verb,kind)
    if key in gen_cache:return gen_cache[key]
    res=None
    try:
        for f in m.generate(verb):
            form,lem,tag=f[0],f[1],f[2]
            p=tag.split(':')
            if p[0]!=kind:continue
            if kind in('ppas','pact') and 'sg' in p and 'nom' in p[2].split('.') and 'm1' in p[3] and p[-1]=='aff':res=form;break
            if kind=='ger' and 'sg' in p and 'nom' in p[2].split('.') and p[-1]=='aff':res=form;break
    except Exception:pass
    gen_cache[key]=res;return res
out={}
for w in words:
    lw=w.lower()
    if lw in out:continue
    an=[a[2] for a in m.analyse(lw)]
    an=[a for a in an if not a[2].startswith(('ign','interp','brev'))]
    if not an:continue
    lems=[(a[1].split(':')[0],a[2]) for a in an]
    if any(l==lw for l,_ in lems):continue   # уже начальная форма в каком-то значении
    cnt=collections.Counter(l for l,_ in lems)
    # приоритет: существительные/прилагательные/глаголы, потом остальное
    best=None
    for l,t in lems:
        k=t.split(':')[0]
        if k in('ppas','pact','ger'):
            g=gen_form(l,k)
            if g and g!=lw: best=g+'|'+l; break
            if g==lw: best=None; break
    if best is None:
        l=cnt.most_common(1)[0][0]
        if l!=lw: best=l
    if best: out[lw]=best
print(len(out))
for k in ['podanym','tego','ta','mamie','wypowiedzi','słuchać','nagrania','zgodnie','przykładem','robię','były','dzieci','ludźmi']:
    print(k,out.get(k))
js='/* Начальные формы для слов из текстов тестов (собрано Morfeusz 2, словарь SGJP).\n   Формат: форма → начальная форма; для причастий «podany|podać» (причастие|глагол). */\nwindow.B1=window.B1||{};B1.lemmas='+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';\n'
open('/home/claude/site/assets/js/lemmas.js','w').write(js)
import os;print(os.path.getsize('/home/claude/site/assets/js/lemmas.js'))
