G = 'Соедините два предложения с помощью żeby. Впишите одно слово.'
F = {
'e3': {'instr': G, 'items': {
 1: {'q': 'Jadę do Krakowa. Chcę zwiedzić Wawel. → Jadę do Krakowa, żeby ___ Wawel.', 'a': ['zwiedzić']},
 2: {'q': 'Uczę się polskiego. Chcę pracować w Polsce. → Uczę się polskiego, żeby ___ w Polsce.', 'a': ['pracować']},
 3: {'q': 'Mówię głośno. Wszyscy mają mnie słyszeć. → Mówię głośno, żeby wszyscy mnie ___.', 'a': ['słyszeli']},
 4: {'q': 'Kupiłam słownik. Chcę szybciej czytać. → Kupiłam słownik, żeby szybciej ___.', 'a': ['czytać']},
 5: {'q': 'Daję ci mój numer. Możesz do mnie zadzwonić. → Daję ci mój numer, ___ mógł do mnie zadzwonić.', 'a': ['żebyś', 'abyś']},
 6: {'q': 'Wychodzimy wcześniej. Nie chcemy stać w korku. → Wychodzimy wcześniej, żeby nie ___ w korku.', 'a': ['stać']},
 7: {'q': 'Mama gotuje zupę. Dzieci mają zjeść coś ciepłego. → Mama gotuje zupę, żeby dzieci ___ coś ciepłego.', 'a': ['zjadły']},
 8: {'q': 'Oszczędzam. Chcę pojechać na wakacje. → Oszczędzam, żeby ___ na wakacje.', 'a': ['pojechać']},
 9: {'q': 'Tłumaczę ci to jeszcze raz. Masz wszystko zrozumieć. → Tłumaczę ci to jeszcze raz, ___ wszystko zrozumiała.', 'a': ['żebyś', 'abyś']},
 10: {'q': 'Włączyłem światło. Chciałem coś zobaczyć. → Włączyłem światło, żeby coś ___.', 'a': ['zobaczyć']},
 11: {'q': 'Zapisałam adres. Nie chciałam go zapomnieć. → Zapisałam adres, żeby go nie ___.', 'a': ['zapomnieć']},
 12: {'q': 'Piszę do was. Macie przyjść w sobotę. → Piszę do was, ___ przyszli w sobotę.', 'a': ['żebyście', 'abyście']},
}},
'e4': {'instr': 'Передайте просьбу с помощью żeby: впишите одно слово — форму на -ł. Если говорит «я», засчитываются обе формы рода.', 'items': {
 1: {'q': 'Mama do mnie: «Posprzątaj pokój!» → Mama chce, żebym ___ pokój.', 'a': ['posprzątał', 'posprzątała']},
 2: {'q': 'Szef do nas: «Skończcie projekt do piątku!» → Szef chce, żebyśmy ___ projekt do piątku.', 'a': ['skończyli', 'skończyły']},
 3: {'q': 'Lekarz do pacjenta: «Proszę nie palić!» → Lekarz prosi pacjenta, żeby nie ___.', 'a': ['palił']},
 4: {'q': 'Ja do ciebie: «Zadzwoń wieczorem!» → Proszę cię, żebyś ___ wieczorem.', 'a': ['zadzwonił', 'zadzwoniła']},
 5: {'q': 'Nauczyciel do uczniów: «Otwórzcie książki!» → Nauczyciel mówi, żeby uczniowie ___ książki.', 'a': ['otworzyli']},
 6: {'q': 'Anna do Marka: «Kup chleb!» → Anna powiedziała Markowi, żeby ___ chleb.', 'a': ['kupił']},
 7: {'q': 'Policjant do kierowcy: «Proszę pokazać dokumenty.» → Policjant poprosił kierowcę, żeby ___ dokumenty.', 'a': ['pokazał']},
 8: {'q': 'Babcia do wnuczki: «Ubierz się ciepło!» → Babcia mówi wnuczce, żeby się ___ ciepło.', 'a': ['ubrała']},
 9: {'q': 'Koleżanka do mnie: «Pomóż mi!» → Koleżanka prosi, żebym jej ___.', 'a': ['pomógł', 'pomogła']},
 10: {'q': 'Rodzice do nas: «Nie wracajcie późno!» → Rodzice proszą, żebyśmy nie ___ późno.', 'a': ['wracali', 'wracały']},
 11: {'q': 'Urzędniczka do mnie: «Proszę wypełnić formularz.» → Urzędniczka prosi, żebym ___ formularz.', 'a': ['wypełnił', 'wypełniła']},
 12: {'q': 'Ty do Ewy: «Przyjdź jutro!» → Powiedz Ewie, żeby ___ jutro.', 'a': ['przyszła']},
}},
'e9': {'instr': 'Перестройте предложение, как в задании VI экзамена. Впишите одно слово.', 'items': {
 1: {'q': '«Zamknij okno!» — powiedziała mi mama (я — ж.). → Mama powiedziała, ___ zamknęła okno.', 'a': ['żebym', 'abym']},
 2: {'q': 'Uczę się polskiego w celu znalezienia pracy. → Uczę się polskiego, żeby ___ pracę.', 'a': ['znaleźć']},
 3: {'q': 'Szef do mnie: «Proszę przygotować raport.» (я — м.) → Szef poprosił mnie, ___ przygotował raport.', 'a': ['żebym', 'abym']},
 4: {'q': 'Ta walizka jest bardzo ciężka. Nie da się jej podnieść. → Ta walizka jest za ciężka, żeby ją ___.', 'a': ['podnieść']},
 5: {'q': 'Myślę, że to nie jest prawda. → Nie sądzę, żeby to ___ prawda.', 'a': ['była']},
 6: {'q': 'Mówię wolno, bo chcę, żebyście mnie zrozumieli. → Mówię wolno, ___ mnie zrozumieli.', 'a': ['żebyście', 'abyście']},
 7: {'q': 'Powiedział, żebym czekał. → Kazał mi ___.', 'a': ['czekać']},
 8: {'q': 'Исправьте ошибку: Chcę, **żebym pojechał** do Gdańska. → Chcę ___ do Gdańska.', 'a': ['pojechać']},
}},
}
F['e6'] = {'items': {10: {'q': 'Weź parasol, żeby nie zmoknąć. Sprawdź pogodę, żeby nie zapomnieć ___ (parasol).', 'a': ['parasola']}}}
REPL = [('Szefowa kazała nam kupić chleb.', 'Szefowa kazała nam zostać dłużej.'),
        ('trzeba dużo się uczyć', 'trzeba się dużo uczyć'),
        ('Начальница велела нам купить хлеб.', 'Начальница велела нам задержаться.')]
S3 = 'Субъект тот же — żeby + инфинитив.'
EX = {
'e3': [([1,2,4,6,8,10,11], S3, 't3'), ([3,7], 'Субъекты разные — żeby + форма на -ł (wszyscy → słyszeli, dzieci → zjadły).', 't4'),
       ([5,9,12], 'Субъекты разные: окончание лица присоединяется к żeby (ty → żebyś, wy → żebyście).', 't2')],
'e4': [(list(range(1,13)), 'Просьба к другому лицу: żeby (+ окончание) + форма на -ł в нужном роде.', 't5')],
'e6': [([10], 'После отрицания дополнение — в dopełniaczu: parasol → parasola.', 't10')],
'e9': [([1,3,6], 'Просьба или желание о другом лице: żeby + окончание лица (ja → żebym, wy → żebyście).', 't5'),
       ([2], S3, 't3'), ([4], 'za + прилагательное, żeby + инфинитив.', 't11'),
       ([5], 'После nie sądzę — żeby + форма на -ł: żeby to była prawda.', 't9'),
       ([7], 'kazać + кому (celownik) + инфинитив, без żeby.', 't6'),
       ([8], 'Субъект тот же — не żeby, а инфинитив: Chcę pojechać.', 't3')],
}
