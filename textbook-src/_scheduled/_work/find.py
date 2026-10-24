import json,re,sys
P=json.load(open('/home/claude/conv/pages.json'))
def find(pat, srcs=None, ctx=90, maxn=8, flags=re.I):
    r=re.compile(pat,flags); n=0
    for p in P:
        if srcs and p['src'] not in srcs: continue
        for m in r.finditer(p['text']):
            s=p['text'][max(0,m.start()-ctx):m.end()+ctx].replace('\n',' ⏎ ')
            print(f"  [{p['src']} s.{p['page']}] …{re.sub(r'\s+',' ',s)}…"); n+=1
            if n>=maxn: return
            break
if __name__=='__main__':
    srcs=sys.argv[2].split(',') if len(sys.argv)>2 and sys.argv[2] else None
    find(sys.argv[1], srcs, maxn=int(sys.argv[3]) if len(sys.argv)>3 else 8)
