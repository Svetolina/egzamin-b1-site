F = {
'e1': {'items': {10: {'q': 'sprzedać → ___', 'a': ['sprzedany']}}},
'e5': {'instr': 'Перестройте в страдательный залог: впишите недостающее слово (причастие или форму być/zostać).', 'items': {
 1: {'q': 'Poeta napisał wiersz. → Wiersz został ___ przez poetę.', 'a': ['napisany']},
 2: {'q': 'Policja zatrzymała złodzieja. → Złodziej został ___ przez policję.', 'a': ['zatrzymany']},
 3: {'q': 'Firma zbuduje nowy most. → Nowy most ___ zbudowany przez firmę.', 'a': ['zostanie', 'będzie']},
 4: {'q': 'Mama ugotowała obiad. → Obiad został ___ przez mamę.', 'a': ['ugotowany']},
 5: {'q': 'Dyrektor zaprosił gości. → Goście zostali ___ przez dyrektora.', 'a': ['zaproszeni']},
 6: {'q': 'Studenci przeczytali książkę. → Książka ___ przeczytana przez studentów.', 'a': ['została']},
 7: {'q': 'Ktoś otworzył okno. → Okno zostało ___.', 'a': ['otwarte']},
 8: {'q': 'Sejm przyjmie ustawę. → Ustawa ___ przyjęta przez Sejm.', 'a': ['zostanie', 'będzie']},
 9: {'q': 'Lekarz zbadał pacjentkę. → Pacjentka została ___ przez lekarza.', 'a': ['zbadana']},
 10: {'q': 'Komisja sprawdza testy. → Testy są ___ przez komisję.', 'a': ['sprawdzane']},
 11: {'q': 'Firma zatrudniła nowych pracowników. → Nowi pracownicy ___ zatrudnieni przez firmę.', 'a': ['zostali']},
 12: {'q': 'Turyści odwiedzają to muzeum. → To muzeum jest ___ przez turystów.', 'a': ['odwiedzane']},
}},
'e6': {'items': {4: {'q': 'Nowa szkoła została otwarta. → Otwarto nową ___.', 'a': ['szkołę']}}},
'e8': {'instr': 'Перестройте предложение, как в задании VI экзамена. Впишите одно слово.', 'items': {
 1: {'q': 'Znany architekt zaprojektował ten dom. → Ten dom został ___ przez znanego architekta.', 'a': ['zaprojektowany']},
 2: {'q': 'Policja zatrzymała dwóch mężczyzn. → Dwaj mężczyźni ___ zatrzymani przez policję.', 'a': ['zostali']},
 3: {'q': 'Organizatorzy odwołali koncert. → Koncert został ___ przez organizatorów.', 'a': ['odwołany']},
 4: {'q': 'Ten wiersz został napisany przez Szymborską. → Szymborska ___ ten wiersz.', 'a': ['napisała']},
 5: {'q': 'Wczoraj podpisano umowę. → Wczoraj umowa została ___.', 'a': ['podpisana']},
 6: {'q': 'Turyści często fotografują ten zamek. → Ten zamek jest często ___ przez turystów.', 'a': ['fotografowany']},
 7: {'q': 'Sejm przyjmie nową ustawę. → Nowa ustawa ___ przyjęta przez Sejm.', 'a': ['zostanie', 'będzie']},
 8: {'q': 'Mój dziadek zbudował ten dom. → Ten dom został zbudowany przez mojego ___.', 'a': ['dziadka']},
}},
}
P = 'Причастие согласуется с подлежащим в роде и числе (мужско-личное мн. ч. — -i / -eni).'
EX = {
'e1': [([10], 'sprzedać → sprzedany (-ać → -any).', 't2')],
'e5': [([1,2,4,5,7,9,10,12], P, 't3'), ([3,8], 'Будущее событие: zostanie (или będzie) + причастие.', 't5'),
       ([6,11], 'Законченное событие в прошлом: zostać в прошедшем времени, согласуется с подлежащим.', 't4')],
'e6': [([4], 'После формы на -no/-to дополнение — в bierniku: nowa szkoła → nową szkołę.', 't8')],
'e8': [([1,3,5,6], P, 't3'), ([2], 'Мужско-личное мн. ч.: dwaj mężczyźni zostali.', 't3'),
       ([4], 'Обратно в действительный залог: исполнитель становится подлежащим — Szymborska napisała.', 't7'),
       ([7], 'Будущее событие: zostanie (или będzie) + причастие.', 't5'), ([8], 'przez + biernik: mój dziadek → mojego dziadka.', 't6')],
}
