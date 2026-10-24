U = ['Chociaż', 'Choć', 'Mimo że', 'Pomimo że']
F = {
'e5': {'items': {
 2: {'q': 'Zostałem w domu, **ponieważ że** padało. → Zostałem w domu, ___ padało.', 'a': ['ponieważ', 'bo', 'gdyż']},
 4: {'q': 'Nie poszedłem, **bo deszcz**. → Nie poszedłem, bo ___ deszcz.', 'a': ['padał']},
}},
'e6': {'instr': 'Соедините два предложения подходящим союзом (в скобках — что он выражает). Впишите союз.', 'items': {
 1: {'q': 'Jest zimno. Włożę kurtkę. (следствие) → Jest zimno, ___ włożę kurtkę.', 'a': ['więc', 'dlatego', 'toteż', 'zatem']},
 2: {'q': 'Nie przyszedł. Był chory. (причина) → Nie przyszedł, ___ był chory.', 'a': ['bo', 'ponieważ', 'gdyż']},
 3: {'q': 'Było późno. Pracowaliśmy dalej. (уступка) → ___ było późno, pracowaliśmy dalej.', 'a': U},
 4: {'q': 'Mam egzamin. Uczę się całą noc. (следствие) → Mam egzamin, ___ uczę się całą noc.', 'a': ['dlatego', 'więc', 'toteż', 'zatem']},
 5: {'q': 'Padał deszcz. Graliśmy w piłkę. (уступка) → ___ padał deszcz, graliśmy w piłkę.', 'a': U},
 6: {'q': 'Autobus się spóźnił. Wzięłam taksówkę. (причина, начало предложения) → ___ autobus się spóźnił, wzięłam taksówkę.', 'a': ['Ponieważ']},
 7: {'q': 'Lubię go. Często się kłócimy. (противопоставление) → Lubię go, ___ często się kłócimy.', 'a': ['ale', 'lecz', 'choć', 'chociaż', 'mimo że']},
 8: {'q': 'Zaspał. Spóźnił się. (следствие) → Zaspał, ___ się spóźnił.', 'a': ['więc', 'toteż', 'dlatego']},
}},
'e8': {'items': {
 3: {'q': 'Mimo choroby poszła do pracy. → Mimo że była ___, poszła do pracy.', 'a': ['chora']},
 4: {'q': 'Zdałem egzamin, bo mi pomogłeś. → Zdałem egzamin dzięki twojej ___.', 'a': ['pomocy']},
}},
}
EX = {'e5': [([2], 'Причина: ponieważ / bo / gdyż — без że.', 't1'), ([4], 'После bo — целое предложение с глаголом: bo padał deszcz.', 't1')],
      'e6': [([1,4,8], 'Следствие: więc, dlatego, toteż (zatem).', 't3'), ([2], 'Причина во второй части: bo, ponieważ, gdyż.', 't1'),
             ([3,5], 'Уступка: chociaż, choć, mimo że.', 't5'), ([6], 'В начале предложения — ponieważ, не bo.', 't1'),
             ([7], 'Противопоставление: ale / lecz или уступка chociaż.', 't7')],
      'e8': [([3], 'Mimo że + целое предложение: mimo że była chora.', 't5'), ([4], 'dzięki + celownik: twojej pomocy.', 't4')]}
