F = {
'e2': {'items': {9: {'q': 'Ten film jest ___ interesujący ze wszystkich. (bardzo → превосходная)', 'a': ['najbardziej']}}},
'e5': {'items': {1: {'q': 'Mój brat jest wyższy ode ___ (ja).', 'a': ['mnie']}}},
'e8': {'instr': 'Перестройте предложение, сохранив смысл. Впишите одно слово.', 'items': {
 1: {'q': 'Marek jest wyższy niż Piotr. → Piotr jest ___ niż Marek.', 'a': ['niższy']},
 2: {'q': 'Anna jest starsza od Ewy. → Ewa jest ___ od Anny.', 'a': ['młodsza']},
 3: {'q': 'Nikt w klasie nie pisze lepiej niż Kasia. → Kasia pisze ___ w klasie.', 'a': ['najlepiej']},
 5: {'q': 'Ten hotel jest tańszy od tamtego. → Tamten hotel jest ___ od tego.', 'a': ['droższy']},
 6: {'q': 'Żadna rzeka w Polsce nie jest dłuższa od Wisły. → Wisła jest ___ rzeką w Polsce.', 'a': ['najdłuższą']},
 8: {'q': 'Ten serial jest mniej ciekawy niż powieść. → Powieść jest ___ niż serial.', 'a': ['ciekawsza', 'bardziej ciekawa']},
 7: {'q': 'Z roku na rok mam więcej pracy. → Mam ___ więcej pracy.', 'a': ['coraz']},
}},
}
O = 'Противоположное прилагательное в сравнительной степени: wysoki ↔ niski, stary ↔ młody, tani ↔ drogi.'
EX = {'e2': [([9], 'Прилагательные на -ący — описательная степень: najbardziej interesujący.', 't5')],
      'e5': [([1], 'od + ja → ode mnie.', 't8')],
      'e8': [([1,2,5], O, 't3'), ([3], 'Никто не пишет лучше = пишет лучше всех: najlepiej.', 't9'),
             ([6], 'Wisła jest + narzędnik: najdłuższą rzeką.', 't9'), ([7], 'coraz + сравнительная степень: coraz więcej.', 't10'),
             ([8], 'ciekawy → ciekawszy (ciekawsza).', 't3')]}
