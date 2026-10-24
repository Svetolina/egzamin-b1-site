import re, json, glob
C='/home/claude/corpus/'
out=[]
def ff_last_number(fn, src):
    for pg in open(C+fn).read().split('\f'):
        lines=[l.strip() for l in pg.split('\n') if l.strip()]
        if not lines: continue
        num=None
        for l in reversed(lines[-3:]):
            m=re.fullmatch(r'(\d{1,3})',l)
            if m: num=int(m.group(1)); break
        if num is None:
            for l in lines[:3]:
                m=re.match(r'^(\d{1,3})\s{3,}',l) or re.search(r'\s{3,}(\d{1,3})$',l)
                if m: num=int(m.group(1)); break
        out.append({'src':src,'page':num,'text':pg})
for fn in ['Gramatyka-z-kultura.-Przez-osoby.-Logo-1-123-1-61.txt','Gramatyka-z-kultura.-Przez-osoby.-Logo-1-123-62-123.txt']:
    ff_last_number(fn,'PO')
for fn in sorted(glob.glob(C+'Podr_cznik*.txt')):
    ff_last_number(fn.split('/')[-1],'ZJP')
ff_last_number('_wiczenia_Z_j_zykiem_polskim_ka_dego_dnia___B1.txt','ZJP Ćw')
ff_last_number('Poradnik_metodyczny_Z_j_zykiem_polskim_ka_dego_dnia___B1.txt','ZJP Por')
# header-then-number style (PO 124+, PP)
for fn,src in [('PO_124.txt','PO'),('PP.txt','PP')]:
    t=open(C+fn).read()
    parts=re.split(r'\n?„Gramatyka z kulturą”[^\n]*\n(\d{1,3})\n',t)
    # parts: [pre, num, text, num, text...]
    if parts[0].strip(): out.append({'src':src,'page':None,'text':parts[0]})
    for i in range(1,len(parts),2):
        out.append({'src':src,'page':int(parts[i]),'text':parts[i+1]})
for fn in ['JPBG_XI_1.txt','JPBG_XI_2.txt']:
    t=open(C+fn).read()
    parts=re.split(r'\n\n(\d{1,3})\n(?=LEKCJA|Lekcja|KLUCZ|Klucz|TRANSKRYP)',t)
    if parts[0].strip(): out.append({'src':'JPBG XI','page':None,'text':parts[0]})
    for i in range(1,len(parts),2):
        out.append({'src':'JPBG XI','page':int(parts[i]),'text':parts[i+1]})
json.dump(out,open('/home/claude/conv/pages.json','w'),ensure_ascii=False)
import collections
c=collections.Counter(p['src'] for p in out); n=collections.Counter(p['src'] for p in out if p['page'] is None)
print(c, 'no page:', n)
for s in c: 
    ps=[p['page'] for p in out if p['src']==s and p['page']]; print(s, min(ps), max(ps))
