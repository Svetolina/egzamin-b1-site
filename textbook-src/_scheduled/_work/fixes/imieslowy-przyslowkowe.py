F = {
'e4': {'instr': 'В предложении разные подлежащие — деепричастие тут нельзя. Замените его на kiedy + глагол прошедшего времени: впишите глагол (говорит «я»; засчитываются обе формы рода).', 'items': {
 1: {'q': '**Idąc do szkoły**, padał deszcz. → Kiedy ___ do szkoły, padał deszcz.', 'a': ['szedłem', 'szłam']},
 2: {'q': '**Jadąc autobusem**, zepsuł się silnik. → Kiedy ___ autobusem, zepsuł się silnik.', 'a': ['jechałem', 'jechałam']},
 3: {'q': '**Czytając książkę**, zadzwonił telefon. → Kiedy ___ książkę, zadzwonił telefon.', 'a': ['czytałem', 'czytałam']},
 4: {'q': '**Wchodząc do sklepu**, zaczęła się burza. → Kiedy ___ do sklepu, zaczęła się burza.', 'a': ['wchodziłem', 'wchodziłam']},
 5: {'q': '**Będąc dzieckiem**, mama czytała mi bajki. → Kiedy ___ dzieckiem, mama czytała mi bajki.', 'a': ['byłem', 'byłam']},
 6: {'q': '**Wróciwszy do domu**, pies na mnie czekał. → Kiedy ___ do domu, pies na mnie czekał.', 'a': ['wróciłem', 'wróciłam']},
}},
'e5': {'instr': 'Подлежащее одно — замените придаточное деепричастием (-ąc или -wszy/-łszy). Впишите одно слово.', 'items': {
 1: {'q': 'Kiedy czekała na tramwaj, czytała książkę. → ___ na tramwaj, czytała książkę.', 'a': ['Czekając']},
 2: {'q': 'Kiedy zjadł śniadanie, wyszedł z domu. → ___ śniadanie, wyszedł z domu.', 'a': ['Zjadłszy']},
 3: {'q': 'Gdy prowadzę samochód, nie rozmawiam przez telefon. → ___ samochód, nie rozmawiam przez telefon.', 'a': ['Prowadząc']},
 4: {'q': 'Kiedy skończyła studia, wyjechała do Anglii. → ___ studia, wyjechała do Anglii.', 'a': ['Skończywszy']},
 5: {'q': 'Kiedy wracaliśmy z kina, rozmawialiśmy o filmie. → ___ z kina, rozmawialiśmy o filmie.', 'a': ['Wracając']},
 6: {'q': 'Kiedy przeczytał wiadomość, uśmiechnął się. → ___ wiadomość, uśmiechnął się.', 'a': ['Przeczytawszy']},
 7: {'q': 'Gdy mieszkałem w Polsce, nauczyłem się polskiego. → ___ w Polsce, nauczyłem się polskiego.', 'a': ['Mieszkając']},
 8: {'q': 'Kiedy otworzyła drzwi, zobaczyła kwiaty. → ___ drzwi, zobaczyła kwiaty.', 'a': ['Otworzywszy']},
 9: {'q': 'Ponieważ nie wiedział, co robić, zadzwonił do brata. → Nie ___, co robić, zadzwonił do brata.', 'a': ['wiedząc']},
 10: {'q': 'Kiedy weszła do domu, zdjęła buty. → ___ do domu, zdjęła buty.', 'a': ['Wszedłszy']},
}},
'e8': {'instr': 'Перестройте на разговорный вариант (kiedy/gdy, ponieważ, który). Впишите глагол (одно слово).', 'items': {
 1: {'q': 'Zjadłszy obiad, wyszedł na spacer. → Kiedy ___ obiad, wyszedł na spacer.', 'a': ['zjadł']},
 2: {'q': 'Czytając gazetę, pił kawę. → Kiedy ___ gazetę, pił kawę.', 'a': ['czytał']},
 3: {'q': 'Nie mając czasu, nie przyszła na spotkanie. → Ponieważ nie ___ czasu, nie przyszła na spotkanie.', 'a': ['miała']},
 4: {'q': 'Będąc w Krakowie, odwiedziliśmy Wawel. → Kiedy ___ w Krakowie, odwiedziliśmy Wawel.', 'a': ['byliśmy']},
 5: {'q': 'Przeczytawszy list, zadzwoniła do matki. → Kiedy ___ list, zadzwoniła do matki.', 'a': ['przeczytała']},
 6: {'q': 'Mieszkając blisko, chodzę do pracy pieszo. → Ponieważ ___ blisko, chodzę do pracy pieszo.', 'a': ['mieszkam']},
 7: {'q': 'Kobieta czytająca książkę to moja siostra. → Kobieta, która ___ książkę, to moja siostra.', 'a': ['czyta']},
 8: {'q': 'Ludzie mieszkający w centrum narzekają na hałas. → Ludzie, którzy ___ w centrum, narzekają na hałas.', 'a': ['mieszkają']},
}},
}
REPL = [('{7} psa, i {8} go,', '{7} psa i {8} go,')]
EX = {
'e4': [(list(range(1,7)), 'Подлежащие разные — деепричастие нельзя; kiedy + прошедшее время в нужном роде.', 't4')],
'e5': [([1,3,5,7,9], 'Действия одновременные, подлежащее одно → форма на -ąc.', 't2'),
       ([2,4,6,8,10], 'Сначала одно действие, потом другое (совершенный вид) → форма на -wszy / -łszy.', 't3')],
'e8': [([1,2,3,4,5,6], 'Деепричастие заменяем придаточным: kiedy / ponieważ + глагол в лице и времени подлежащего.', 't6'),
       ([7,8], 'Причастие на -ący заменяем на który + глагол в настоящем времени.', 't7')],
}
