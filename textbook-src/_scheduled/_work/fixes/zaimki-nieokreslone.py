F = {
'e4': {'items': {2: {'q': 'Nigdy **byłem** w Hiszpanii. → Nigdy ___ byłem w Hiszpanii.', 'a': ['nie']}}},
'e8': {'instr': 'Сделайте предложение отрицательным. Впишите одно слово.', 'items': {
 1: {'q': 'Ktoś przyszedł. → ___ nie przyszedł.', 'a': ['Nikt']},
 2: {'q': 'Coś widzę. → ___ nie widzę.', 'a': ['Nic', 'Niczego']},
 4: {'q': 'Wieczorem gdzieś idę. → Wieczorem ___ nie idę.', 'a': ['nigdzie']},
 5: {'q': 'Mam jakiś pomysł. → Nie mam ___ pomysłu.', 'a': ['żadnego']},
 6: {'q': 'Ktoś coś wie. → Nikt ___ nie wie.', 'a': ['nic', 'niczego']},
 7: {'q': 'Rozmawiam z kimś. → Z ___ nie rozmawiam.', 'a': ['nikim']},
 8: {'q': 'Znam kogoś w tym mieście. → ___ nie znam w tym mieście.', 'a': ['Nikogo']},
}},
}
REPL = [('(не [[Nie widzę cokolwiek]])', '(не **Nie widzę cokolwiek**)')]
EX = {'e4': [([2], 'При nigdy глагол всегда с nie (двойное отрицание).', 't4')],
      'e8': [([1], 'ktoś → nikt + nie.', 't4'), ([2], 'coś → nic / niczego + nie.', 't4'), ([4], 'gdzieś → nigdzie + nie.', 't4'),
             ([5], 'jakiś → żaden; после nie mam — dopełniacz: żadnego.', 't6'), ([6], 'Двойное отрицание: nikt nic nie wie.', 't4'),
             ([7], 'z + narzędnik: z nikim.', 't5'), ([8], 'kogoś → nikogo + nie.', 't5')]}
