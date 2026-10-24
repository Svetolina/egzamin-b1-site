import json,sys,re
t=json.load(open(f'out/{sys.argv[1]}/topic.json'))
for s in t['theory']:
    print('##',s['id'],s['title'])
    for b in s['blocks']:
        ty=b['type']
        if ty=='ex':
            for i in b['items']: print('  ex:',i['pl'])
        elif ty=='table':
            for r in b['rows']: print('  tr:',' | '.join(r[c] for c in b.get('pl_cols',[]) if c<len(r)))
        elif ty=='fix':
            for i in b.get('items',[b]): print('  fix:',i.get('bad'),'→',i.get('good'))
        elif ty=='chips': print('  chips:',b.get('items'))
        else:
            txt=b.get('text','') if isinstance(b.get('text'),str) else json.dumps(b,ensure_ascii=False)
            pl=re.findall(r'\[\[(.+?)\]\]',txt)
            if pl: print(f'  {ty}:',' / '.join(pl))
