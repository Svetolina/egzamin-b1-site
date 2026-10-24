F = {
'e7': {'items': {12: {'q': 'к себе'}}},
'e8': {'instr': 'Перестройте предложение, используя swój или siebie/sobie/sobą. Впишите одно слово.', 'items': {
 1: {'q': 'Marek myje samochód. Samochód należy do Marka. → Marek myje ___ samochód.', 'a': ['swój']},
 2: {'q': 'Anna rozmawia z mamą Anny. → Anna rozmawia ze ___ mamą.', 'a': ['swoją']},
 4: {'q': 'Oni pomagają jeden drugiemu. → Oni pomagają ___ nawzajem.', 'a': ['sobie']},
 5: {'q': 'Przyjechał mój brat i żona mojego brata. → Przyjechał mój brat i ___ żona.', 'a': ['jego']},
 6: {'q': 'Piotr odwiedza babcię Piotra. → Piotr odwiedza ___ babcię.', 'a': ['swoją']},
 7: {'q': 'Tomek rozmawiał z Olą, a Ola z Tomkiem. → Tomek i Ola rozmawiali ze ___.', 'a': ['sobą']},
}},
}
REPL = [('do {12}. (к себе)', 'do {12}.')]
REPL += [('**[[Mój** brat mieszka w Krakowie. **Jego** dom jest duży.]] Не [[Swój brat…]].', '[[Mój brat mieszka w Krakowie. Jego dom jest duży.]] Не **Swój brat…**')]
EX = {'e8': [([1,2,6], 'Вещь или человек принадлежит подлежащему → swój в нужной форме.', 't1'),
             ([4], 'Друг другу → sobie nawzajem.', 't8'), ([5], 'Жена брата, а брат — не подлежащее этой части → jego.', 't2'),
             ([7], 'Друг с другом → ze sobą.', 't8')]}
