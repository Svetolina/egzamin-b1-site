F = {
'e6': {'items': {4: {'q': 'Miejsce w samochodzie albo w pociągu, na którym siedzisz: ___', 'a': ['siedzenie']}}},
'e8': {'instr': 'Перестройте, используя отглагольное существительное. Впишите одно слово.', 'items': {
 1: {'q': 'Po tym, jak zjedliśmy kolację, poszliśmy na spacer. → Po ___ kolacji poszliśmy na spacer.', 'a': ['zjedzeniu']},
 2: {'q': 'Kiedy czekam na autobus, słucham muzyki. → Podczas ___ na autobus słucham muzyki.', 'a': ['czekania']},
 6: {'q': 'Zebraliśmy się, żeby omówić plan. → Zebraliśmy się w celu ___ planu.', 'a': ['omówienia']},
 8: {'q': 'Przyjemnie jest uczyć się języków. → ___ się języków jest przyjemne.', 'a': ['Uczenie']},
}},
}
REPL = [('pracować → pracowanie', 'pływać → pływanie'), ('czuć → czucie', 'szyć → szycie')]
EX = {'e6': [([4], 'siedzieć → siedzenie (стало обычным словом).', 't7')],
      'e8': [([1], 'po + miejscownik: po zjedzeniu.', 't6'), ([2], 'podczas + dopełniacz: podczas czekania.', 't6'),
             ([6], 'w celu + dopełniacz: omówienia.', 't6'), ([8], 'uczyć się → uczenie się.', 't2')]}
