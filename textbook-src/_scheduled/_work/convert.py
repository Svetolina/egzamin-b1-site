#!/usr/bin/env python3
"""Переводит черновики запланированной задачи (textbook-src/_scheduled) в формат
textbook-src/<тема>/{extract,topic}.json, как у czas-przyszly / biernik.

python3 convert.py <папка черновика> <папка вывода>
"""
import json, os, re, sys
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from meta import M, STD, KEY, exname
import models

GRAM = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gram_all.json')))
CYR = re.compile(r'[А-Яа-яЁё]')
TODAY = '2026-10-24'

HOSTS = {'elon.io': 'EL', 'en.wikipedia.org': 'WE', 'pl.wikipedia.org': 'WP', 'zpe.gov.pl': 'ZP',
         'polski.info': 'PI', 'faculty.washington.edu': 'DZ', 'grzegorj.smallhost.pl': 'GJ',
         'courseofpolish.com': 'CP', 'www.polskidaily.eu': 'PD', 'polskidaily.eu': 'PD',
         'www.clozemaster.com': 'CM', 'internal.varsitytutors.com': 'VT', 'wfpik.amu.edu.pl': 'AM',
         'pressto.amu.edu.pl': 'AP', 'preply.com': 'PR', 'blogs.transparent.com': 'TL',
         'www.lingq.com': 'LQ', 'ojs.ung.si': 'UN'}


import morfeusz2
_MORF = morfeusz2.Morfeusz()
WORD = re.compile(r"[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż]+")


def unknown(w):
    return len(w) > 2 and all(t.split(':')[0] == 'ign' for *_x, (_o, _l, t, _q, _s) in _MORF.analyse(w))


def bold_bad(s):
    """Слова, которых нет в Morfeusz, — это заведомо неверные формы из черновика: выделяем **…**."""
    return WORD.sub(lambda m: f'**{m.group(0)}**' if unknown(m.group(0)) else m.group(0), s)


def it_text(s):
    """*польский* → [[польский]] (или **…**, если внутри неверная форма), **выделение** сохраняется."""
    s = s.replace('**', '\x00')
    def pl(m):
        x = m.group(1)
        return f'**{x}**' if any(unknown(w) for w in WORD.findall(x)) else f'[[{x}]]'
    s = re.sub(r'\*([^*\n]+?)\*', pl, s)
    return s.replace('\x00', '**')


def first_sentence(t, n=120):
    t = re.sub(r'\*+', '', t).strip()
    m = re.match(r'(.+?[.!?])(\s|$)', t)
    s = m.group(1) if m else t
    if len(s) > n:
        s = s[:n].rsplit(' ', 1)[0].rstrip(',;:') + '…'
    return s


def dedupe(xs):
    out, seen = [], set()
    for x in xs:
        x = x.strip()
        k = re.sub(r'\s+', ' ', x.lower())
        if x and k not in seen:
            seen.add(k); out.append(x)
    return out


# ---------- источники и факты ----------

def build_extract(src, slug, meta):
    e = json.load(open(os.path.join(src, 'extract.json'), encoding='utf-8'))
    url_id, sources, cnt = {}, {'STD': STD}, {}
    def sid(title, url):
        if url in url_id:
            return url_id[url]
        h = HOSTS.get(urlparse(url).netloc, 'XX')
        cnt[h] = cnt.get(h, 0) + 1
        i = h + chr(64 + cnt[h])          # ELA, ELB … — одной длины, не префиксы друг друга
        url_id[url] = i
        sources[i] = f'{title}: {url}'
        return i
    for s in e.get('sources', []):        # первый формат: общий список
        sid(s['title'], s['url'])
    facts = []
    for f in e['facts']:
        refs = []
        for s in f['sources']:
            i = sid(s['title'], s['url'])
            where = s.get('where') or s.get('loc') or ''
            refs.append(f'{i} ({where})' if where else i)
        text = f.get('text') or f.get('rule')
        fact = {'id': f['id'], 'ru': text, 'pl': [], 'refs': refs, 'status': 'ok'}
        one = len(f['sources']) < 2 or f.get('single_source_note')
        if one:
            fact['status'] = 'marked'
            fact['decision'] = ('правило из одного источника — публикуется одной строкой с пометкой '
                                '(как решено для czas przyszły и вида)' +
                                (f": {f['single_source_note']}" if isinstance(f.get('single_source_note'), str) else ''))
        if f.get('note'):
            fact['note'] = f['note']
        facts.append(fact)
    # официальные ключи — источник раздела «На экзамене»
    if meta['exam_refs']:
        sources['KEY'] = KEY
    sources['MORF'] = 'Morfeusz 2 (SGJP) — проверка польских слов скриптом tools/morfeusz_check.py'
    return {
        'topic': slug,
        'title': f"{meta['title_pl']} — {meta['title_ru'].lower()}",
        'stage': 'перенесено из черновика запланированной задачи (24.10.2026): факты по веб-источникам; сверка с учебниками проекта (PO, PP, JPBG, ZJP) со страницами — не сделана',
        'updated': TODAY,
        'passport': {
            'standard': meta['standard'], 'level': meta['lvl'],
            'katalog_b': [], 'katalog_a': [],
            'exam': meta['exam_text'].replace('[[', '').replace(']]', ''),
            'depends_on': meta['depends'], 'feeds': meta['feeds'],
        },
        'sources': sources,
        'noticed': ['Тема перенесена из textbook-src/_scheduled/: источники — сайты (ссылки с разделом), страниц учебников проекта пока нет; Katalog A/B не подобраны.'],
        'facts': facts,
        'forms': [],
    }


def exam_ref(meta):
    refs = []
    for r in meta['exam_refs']:
        if isinstance(r, tuple):
            tid, gid = r
            t = next(t for t in GRAM[tid]['tasks'] if t['id'] == gid)
            refs.append(f"KEY: {exname(tid)}, Gramatyka {t['rn']} «{t['name']}» (tests/{tid}.js, {gid})")
        else:
            t = next(t for t in GRAM['b1-sbornik']['tasks'] if t['id'] == r)
            refs.append(f"KEY: сборник 2017, Gramatyka {t['rn']} «{t['name']}» (tests/b1-sbornik.js, {r})")
    refs.insert(0, 'STD: ' + meta['standard'])
    if not meta['exam_refs']:
        refs.append('KEY: поиск по разделу Gramatyka сборника 2017 и 18 экзаменов (tests/b1-*.js) — заданий на эту тему нет')
    return {'id': 'EXAM', 'refs': refs}


# ---------- теория ----------

def body_blocks(body):
    out = []
    for para in re.split(r'\n\s*\n', body.strip()):
        lines = [l for l in para.split('\n') if l.strip()]
        if lines and all(re.match(r'\s*[-•]\s', l) for l in lines):
            out.append({'type': 'steps', 'items': [it_text(re.sub(r'^\s*[-•]\s*', '', l)) for l in lines]})
            continue
        buf = []
        for l in lines:
            if re.match(r'\s*[-•]\s', l):
                if buf: out.append({'type': 'p', 'text': it_text(' '.join(buf))}); buf = []
                out.append({'type': 'steps', 'items': [it_text(re.sub(r'^\s*[-•]\s*', '', l))]})
            elif l.strip().startswith('💡'):
                if buf: out.append({'type': 'p', 'text': it_text(' '.join(buf))}); buf = []
                out.append({'type': 'note', 'kind': 'tip', 'text': it_text(l.strip().lstrip('💡').strip())})
            else:
                buf.append(l.strip())
        if buf: out.append({'type': 'p', 'text': it_text(' '.join(buf))})
    # слить соседние steps
    merged = []
    for b in out:
        if merged and b['type'] == 'steps' and merged[-1]['type'] == 'steps':
            merged[-1]['items'] += b['items']
        else:
            merged.append(b)
    return merged


def table_block(t):
    head = [it_text(h) for h in t['head']]
    rows = [[re.sub(r'\*+', '', c) if False else c for c in r] for r in t['rows']]
    ncol = max(len(r) for r in rows)
    pl_cols = []
    for i in range(ncol):
        cells = [r[i] for r in rows if i < len(r) and r[i].strip()]
        if cells and not any(CYR.search(c) for c in cells) and not (i == 0 and CYR.search(head[0] or '') and len(cells[0]) < 3):
            pl_cols.append(i)
    rows = [[(re.sub(r'\*+', '', c) if i in pl_cols else it_text(c)) for i, c in enumerate(r)] for r in rows]
    return {'type': 'table', 'head': head, 'rows': rows, 'pl_cols': pl_cols}


def build_theory(secs, facts):
    marked = {f['id'] for f in facts if f['status'] == 'marked'}
    theory = []
    for n, s in enumerate(secs, 1):
        blocks = []
        if s.get('body'):
            blocks += body_blocks(s['body'])
        if s.get('list'):
            blocks.append({'type': 'steps', 'items': [it_text(x) for x in s['list']]})
        if s.get('table'):
            blocks.append(table_block(s['table']))
        if s.get('examples'):
            blocks.append({'type': 'ex', 'items': [{'pl': re.sub(r'\*+', '', a), 'ru': b} for a, b in s['examples']]})
        for k in ('tip', 'note', 'warn'):
            if s.get(k):
                txt = s[k] if isinstance(s[k], str) else ' '.join(s[k])
                if k == 'warn':
                    txt = 'Внимание: ' + txt
                blocks.append({'type': 'note', 'kind': 'tip', 'text': it_text(txt)})
        sec = {'id': f't{n}', 'title': it_text(s['title']), 'facts': list(s.get('facts', [])), 'blocks': blocks}
        mk = [f for f in sec['facts'] if f in marked]
        if mk or s.get('sourceNote'):
            sec['marked'] = True
            txt = s.get('sourceNote') or ('Правило подтверждено одним источником — дано одной строкой с пометкой.')
            blocks.append({'type': 'note', 'kind': 'mark', 'text': it_text(txt)})
        theory.append(sec)
    return theory


# ---------- упражнения ----------

def gaps_of(it):
    """Список ответов по пропускам [[..], [..]] для любого из двух форматов."""
    a = it['a']
    if isinstance(a, dict):
        return [a[k] if isinstance(a[k], list) else [a[k]] for k in sorted(a, key=int)]
    if a and isinstance(a[0], list):
        return a
    return [a]


def item_facts(it, ex):
    f = it.get('fact') or ''
    ids = re.findall(r'R\d+', f) if isinstance(f, str) else list(f)
    return ids or [x for x in ex.get('facts', []) if x.startswith('R')]


def make_t(ids, theory):
    for i in ids:
        for s in theory:
            if i in s['facts']:
                return s['id']
    return theory[0]['id']


def expl_for(ids, facts):
    for i in ids:
        if i in facts:
            return first_sentence(facts[i]['ru'])
    return 'См. правило в теории.'


ALT = re.compile(r'\(([^()]*?/[^()]*?)\)')


def try_choice(items):
    """Если в каждом пункте есть «(A / B)» с ответом среди вариантов — делаем выбор."""
    out = []
    for q, ans, extra in items:
        m = None
        for mm in ALT.finditer(q):
            opts = [o.strip() for o in mm.group(1).split('/')]
            if any(a.lower() in [o.lower() for o in opts] for a in ans):
                m = (mm, opts)
        if not m:
            return None
        mm, opts = m
        a = [o for o in opts if o.lower() in [x.lower() for x in ans]]
        out.append((q[:mm.start()].rstrip() + q[mm.end():], a, opts, extra))
    return out


def convert_ex(ex, theory, facts, n):
    kind, fmt = ex['kind'], ex.get('format')
    title, instr = ex['title'], ex.get('instr', '')
    base = {'id': f'e{n}', 'title': title}
    if instr:
        base['instr'] = instr
    if fmt in ('exam', 'exam-text', 'rewrite'):
        base['format'] = 'exam'

    # 1) связный текст
    if kind == 'text-gaps' or fmt == 'exam-text':
        if kind == 'text-gaps':
            text, a = ex['text'], ex['a']
            nums = [int(x) for x in re.findall(r'\{(\d+)\}', text)]
            ans = {k: (v if isinstance(v, list) else [v]) for k, v in a.items()}
            fids = item_facts(ex, ex)
        else:   # предложения подряд → один текст
            parts, ans, k = [], {}, 0
            for it in ex['items']:
                q = it['q']
                gs = gaps_of(it)
                # подсказка в скобках не сразу после пропуска (в конце фразы) — перенести к пропуску
                if len(gs) == 1 and not re.search(r'\{\d+\}\s*\(', q):
                    m = re.search(r'\s*\(([^()]*)\)\s*([.!?…]?)\s*$', q)
                    if m:
                        q = q[:m.start()] + m.group(2)
                        q = re.sub(r'(\{\d+\})', lambda mm: mm.group(1) + ' (' + m.group(1) + ')', q, count=1)
                for g in gs:
                    k += 1
                    ans[str(k)] = g
                parts.append(q)
            # перенумеровать
            k = 0
            def ren(m):
                nonlocal k; k += 1; return '{%d}' % k
            text = re.sub(r'\{\d+\}', ren, ' '.join(parts))
            fids = [x for x in ex.get('facts', []) if x.startswith('R')]
        items, passage, idx = [], text, 0
        def repl(m):
            nonlocal idx
            idx += 1
            hint = (m.group(2) or '').strip()
            items.append({'q': hint or '…', 'a': dedupe(ans[m.group(1)]),
                          'expl': expl_for(fids, facts), 't': make_t(fids, theory)})
            return '{%d}' % idx
        passage = re.sub(r'\{(\d+)\}(?:\s*\(([^()]*)\))?', repl, text)
        base.update({'level': 3, 'kind': 'text', 'format': 'exam', 'passage': passage, 'items': items})
        return [base]

    # 2) пункты: развернуть многопропусковые
    flat = []
    for it in ex['items']:
        gs = gaps_of(it)
        q = it['q']
        fids = item_facts(it, ex)
        hint = it.get('hint')
        if '{' not in q:          # typed без маркера: поле ввода — под заданием
            flat.append((bold_bad(q), dedupe(gs[0]), (fids, hint)))
            continue
        nums = re.findall(r'\{(\d+)\}', q)
        for j, num in enumerate(nums):
            qq = q
            for k2 in nums:
                qq = qq.replace('{%s}' % k2, '___' if k2 == num else '…')
            flat.append((bold_bad(qq), dedupe(gs[j]), (fids, hint)))

    ch = try_choice(flat) if kind != 'typed' else None
    items = []
    if ch:
        for q, a, opts, (fids, hint) in ch:
            items.append({'q': q + (f' (подсказка: {hint})' if hint else ''), 'opts': opts, 'a': a,
                          'expl': expl_for(fids, facts), 't': make_t(fids, theory)})
        base.update({'level': 1, 'kind': 'choice', 'items': items})
        return [base]
    for q, a, (fids, hint) in flat:
        items.append({'q': q + (f' (подсказка: {hint})' if hint else ''), 'a': a,
                      'expl': expl_for(fids, facts), 't': make_t(fids, theory)})
    level = 3 if base.get('format') == 'exam' else 2
    base.update({'level': level, 'kind': 'type', 'items': items})
    return [base]


def convert_write(w, slug, theory, n):
    instr = w.get('prompt') or w.get('instr')
    m = re.search(r'(\d+)\s*[–-]\s*(\d+)\s*sł', instr)
    words = [int(m.group(1)), int(m.group(2))] if m else [60, 80]
    mo = models.MODELS.get((slug, w['id']), {})
    model = mo.get('model') or w.get('model') or ''
    fids = [x for x in w.get('facts', []) if x.startswith('R')]
    return {'id': f'e{n}', 'level': 4, 'kind': 'write', 'title': w['title'], 'instr': instr,
            'words': words, 'need': mo.get('need') or ('; '.join(w['checklist'][:2]) + '.').replace('..', '.'),
            'model': model, 'model_future': mo.get('forms', []),
            'checklist': w['checklist'] + ([f'{words[0]}–{words[1]} слов'] if not any('слов' in c for c in w['checklist']) else []),
            't': make_t(fids, theory), 'items': []}


def main(src, out):
    slug = os.path.basename(src.rstrip('/'))
    meta = M[slug]
    ext = build_extract(src, slug, meta)
    facts = {f['id']: f for f in ext['facts']}
    t = json.load(open(os.path.join(src, 'topic.json'), encoding='utf-8'))
    secs = t.get('theory') or t.get('sections')
    theory = build_theory(secs, ext['facts'])
    theory.append({'id': f't{len(theory) + 1}', 'title': 'На экзамене', 'facts': ['EXAM'],
                   'blocks': [{'type': 'p', 'text': meta['exam_text']}, {'type': 'steps', 'items': meta['steps']}]})
    exs, n = [], 0
    writes = [x for x in t['exercises'] if x['kind'] == 'writing'] + t.get('writing', [])
    for ex in [x for x in t['exercises'] if x['kind'] != 'writing']:
        for e in convert_ex(ex, theory, facts, n + 1):
            n += 1; e['id'] = f'e{n}'; exs.append(e)
    # ступени по порядку: 1 → 2 → 3
    exs.sort(key=lambda e: e['level'])
    for w in writes:
        exs.append(convert_write(w, slug, theory, 0))
    for i, e in enumerate(exs, 1):
        e['id'] = f'e{i}'
    topic = {
        'topic': slug, 'level': meta['level'], 'group': meta['group'],
        'title_pl': meta['title_pl'], 'title_ru': meta['title_ru'], 'lead': meta['lead'],
        'facts_file': 'extract.json',
        'stage': 'перенесено из черновика запланированной задачи; источники — сайты, сверка с учебниками проекта не сделана' +
                 ('; по стандарту — слой B2' if meta['level'] == 'B2' else ''),
        'markup': '[[…]] — польский текст',
        'exam_ref': exam_ref(meta), 'forms': [], 'theory': theory, 'exercises': exs,
    }
    os.makedirs(out, exist_ok=True)
    json.dump(ext, open(os.path.join(out, 'extract.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(topic, open(os.path.join(out, 'topic.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(slug, 'теория', len(theory), 'упражнений', len(exs), 'пунктов', sum(len(e['items']) for e in exs))


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
