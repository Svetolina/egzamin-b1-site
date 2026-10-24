import json,re,sys
P=json.load(open('/home/claude/conv/pages.json'))
src=sys.argv[1]; a,b=map(int,sys.argv[2].split('-')); kw=sys.argv[3] if len(sys.argv)>3 else None; lim=int(sys.argv[4]) if len(sys.argv)>4 else 1500
for p in P:
    if p['src']==src and p['page'] and a<=p['page']<=b:
        t=re.sub(r'[.…]{4,}','…',p['text']); t=re.sub(r'[ \t ]+',' ',t); t=re.sub(r'\n\s*\n+','\n',t)
        lines=t.split('\n')
        if kw: lines=[l for l in lines if re.search(kw,l,re.I)]
        out='\n'.join(lines).strip()
        if out: print(f'=== {src} s.{p["page"]}'); print(out[:lim])
