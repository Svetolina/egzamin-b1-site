import json,re,sys
D=json.load(open('/home/claude/conv/gram_all.json'))
K={
'tryb-rozkazujacy':(r'rozkazując',r'\bniech\b'),
'tryb-przypuszczajacy':(r'przypuszczając',r'\b\w+(łbym|łabym|łbyś|łby|łaby|łoby|libyśmy|łybyśmy|liby|łyby|libyście)\b|\bgdyby\w*'),
'czasowniki-ruchu':(None,r'\b(idę|idzie|idą|chodzę|chodzi|chodzą|jadę|jedzie|jadą|jeżdżę|jeździ|jeżdżą|poszed\w*|poszł\w*|pojecha\w*|przyjecha\w*|wyjecha\w*|przyszed\w*|przyszł\w*|wyszed\w*|wyszł\w*|chodził\w*|jeździł\w*)\b'),
'dopelniacz-po-negacji':(r'negacj|zaprzecz',None),
'liczebniki-z-rzeczownikami':(r'liczebnik',None),
'zdania-ktory':(None,r'\bktór\w+'),
'zeby-aby':(None,r'\b(żeby|aby)(m|ś|śmy|ście)?\b'),
'strona-bierna':(r'stron\w+ biern',r'\b(został|została|zostało|zostali|zostały|zostanie|zostaną)\s+\w+'),
'mowa-zalezna':(r'mow\w+ zależn',None),
'stopniowanie':(r'stopniowan',None),
'swoj-siebie':(None,r'\b(swój|swoj\w+|swoim|swoją|swoich|swoje|swego|siebie|sobie|sobą)\b'),
'imieslowy-przyslowkowe':(r'imiesł',r'\b\w{3,}ąc\b'),
'rzeczowniki-odczasownikowe':(r'odczasown',None),
'zaimki-nieokreslone':(None,r'\b(ktoś|kogoś|komuś|kimś|coś|czegoś|czymś|nikt|nikogo|nikomu|nic|niczego|nikim|niczym|nigdy|nigdzie|gdzieś|kiedyś|jakiś|jakieś|jakiegoś|żaden|żadnego|żadnej)\b'),
'spojniki-przyczyna-przyzwolenie':(r'spójnik',r'\b(ponieważ|chociaż|choć|mimo że|dlatego że)\b'),
}
def answers(txt):
    # crude: values of "a" / "key" / "ans" fields
    return ' '.join(re.findall(r'"(?:a|key|ans|answer|k|opts|text|t)":\s*("(?:[^"\\]|\\.)*"|\[[^\]]*\])',txt))
for top,(ri,rt) in K.items():
    res=[]
    for tid,v in D.items():
        for t in v['tasks']:
            n=0; ex=set()
            if ri and re.search(ri,t['instr'],re.I): n+=100
            if rt:
                m=[x.group(0) for x in re.finditer(rt,t['txt'],re.I)]
                n+=len(m); ex.update(m)
            if n>=2: res.append((n,tid,t['id'],t['rn'],t['name'],sorted(ex)[:5]))
    res.sort(reverse=True)
    print('##',top)
    for r in res[:7]: print('  ',r)
