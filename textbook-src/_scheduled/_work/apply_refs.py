# Промежуточный шаг доводки: вписать сверку с учебниками (tb_refs.R) в extract.json, обновить статусы и плашку.
import json, re, tb_refs
SRC = {
 'PO': 'Gramatyka z kulturą. Przez osoby (файлы проекта Gramatyka-z-kultura.-Przez-osoby.-Logo-*.pdf)',
 'PP': 'Gramatyka z kulturą. Przez przypadki (файл проекта 142944-gramatyka-z-kultura.pdf)',
 'JPBG XI': 'Język polski bez granic, kl. XI (B2) (файлы проекта kl.-XI-*.pdf)',
 'ZJP': 'Z językiem polskim każdego dnia – B1, podręcznik (файлы проекта Podręcznik_…B1-*.pdf)',
 'ZJP Ćw': 'Z językiem polskim każdego dnia – B1, ćwiczenia (файл проекта Ćwiczenia_…B1.pdf)',
 'ZJP Por': 'Z językiem polskim każdego dnia – B1, poradnik metodyczny (файл проекта Poradnik_…B1.pdf)',
 'KEY': 'официальные ключи комиссии в tests/b1-*.js сайта',
}
OK = {'tryb-przypuszczajacy': ['R7','R13','R16','R17'], 'zaimki-nieokreslone': ['R5'], 'swoj-siebie': ['R11'],
      'spojniki-przyczyna-przyzwolenie': ['R5'], 'stopniowanie': ['R11'], 'imieslowy-przyslowkowe': ['R3']}
for slug, refs in tb_refs.R.items():
    d = f'out/{slug}'; ex = json.load(open(f'{d}/extract.json')); tp = json.load(open(f'{d}/topic.json'))
    used = set()
    for f in ex['facts']:
        add = refs.get(f['id'], [])
        for r in add:
            if r not in f['refs']: f['refs'].append(r)
            m = re.match(r'(ZJP Ćw|ZJP Por|JPBG XI|ZJP|PO|PP|KEY)\b', r)
            if m: used.add(m.group(1))
        if f['id'] in OK.get(slug, []) and f['status'] != 'ok':
            f['status'] = 'ok'; f['decision'] = 'подтверждено учебником проекта при сверке 24.10.2026'
    for k in sorted(used): ex['sources'].setdefault(k, SRC[k])
    n_tb = sum(1 for f in ex['facts'] if refs.get(f['id']))
    still = [f['id'] for f in ex['facts'] if f['status'] != 'ok']
    stage = (f'доводка (24.10.2026): {n_tb} из {len(ex["facts"])} фактов сверены с учебниками проекта со страницами; '
             f'с пометкой: {", ".join(still) or "нет"}. Ещё не сделано: Katalog A/B, проверка естественности, ответы-слова в перефразированиях, тест на пересказ')
    ex['stage'] = stage; tp['stage'] = stage
    marked = set(still)
    for s in tp['theory']:
        if s.get('marked') and not (set(s.get('facts', [])) & marked):
            s.pop('marked'); s['blocks'] = [b for b in s['blocks'] if not (b.get('type') == 'note' and b.get('kind') == 'mark')]
    json.dump(ex, open(f'{d}/extract.json', 'w'), ensure_ascii=False, indent=1)
    json.dump(tp, open(f'{d}/topic.json', 'w'), ensure_ascii=False, indent=1)
    print(slug, n_tb, len(ex['facts']), still)
