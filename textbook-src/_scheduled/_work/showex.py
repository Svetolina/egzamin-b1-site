import json,sys
t=json.load(open(f'out/{sys.argv[1]}/topic.json'))
for e in t['exercises']:
    if e['kind']=='write': continue
    print(f"## {e['id']} [{e['kind']} L{e['level']}] {e['title']} — {e.get('instr','')[:120]}")
    if e['kind']=='text': print('   P:', e['passage'])
    for i,it in enumerate(e['items'],1):
        o=f" opts={it['opts']}" if it.get('opts') else ''
        print(f"  {i}. {it['q']}  => {' | '.join(it['a'])}{o}")
