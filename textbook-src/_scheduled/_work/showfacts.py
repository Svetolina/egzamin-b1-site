import json,sys
e=json.load(open(f'out/{sys.argv[1]}/extract.json'))
for f in e['facts']:
    print(f"{f['id']} [{f['status']}] {f['ru'][:230]}  || {', '.join(r.split(' ')[0] for r in f['refs'])}")
