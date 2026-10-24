# Метаданные тем для перевода черновиков запланированной задачи в формат textbook-src.
# Страницы — Dz.U. 2025 poz. 217 (номер в колонтитуле «Dziennik Ustaw – N –»).

STD = "Dz.U. 2025 poz. 217 (файл проекта D20250217.pdf)"
KEY = "Официальные ключи комиссии: сборник B1 2017 (tests/b1-sbornik.js) и экзамены 2017–2024 (tests/b1-*.js) — найдено поиском по заданиям раздела Gramatyka"
EX = {
 'b1-sbornik': 'сборник 2017', 'b1-2017': 'образец 2017', 'b1-2019': 'образец 2019', 'b1-2020-03': 'образец 2020',
}
def exname(tid):
    if tid in EX: return EX[tid]
    y, m = tid[3:].split('-')
    return f'экзамен {m}.{y}'

M = {}

def T(slug, **kw): M[slug] = kw

T('tryb-rozkazujacy', group='Глагол', level='B1', title_pl='Tryb rozkazujący', title_ru='Повелительное наклонение',
  lead='Zrób! Nie rób! Niech zrobi! Как просить, советовать и запрещать — и какой вид для этого нужен.',
  standard='Dz.U. 2025 poz. 217, Zał. 1, Część II, E (B1): 2.2.1 Fleksja, pkt 2 lit. a «tryb rozkazujący (np.: bierzcie, napiszmy, przeczytaj, uczcie się, niech słuchają)», s. 77; 2.2.3 Składnia, pkt 2 lit. d «zdania rozkazujące (np.: Posłuchajcie go! Nie słuchajcie go! Niech oni kupią chleb! Niech oni nie kupują chleba!)», s. 78. На B2 (s. 89) — та же строка с более трудными формами (weź, włóż, wynieśmy, niech upiecze).',
  lvl='B1 — формы ty / my / wy и niech, вежливые proszę + инфинитив, выбор вида в просьбе и запрете.',
  depends=['czas-terazniejszy', 'czas-przyszly', 'aspekt'], feeds=['zeby-aby (просьбы в косвенной речи)', 'mowa-zalezna'],
  exam_text='Повелительное наклонение проверяют отдельные задания сборника (блок 8, зад. XII–XIII; блок 12, зад. VIII — «замените глагол формой повелительного наклонения») и задание VII реальных экзаменов «вид и наклонение» (там встречаются niech + 3 лицо). В письме — инструкции, просьбы и советы.',
  exam_refs=['k8-12', 'k8-13', 'k12-8', ('b1-2023-06', 'g7'), ('b1-2022-11', 'g7')],
  steps=['Кому вы говорите: ty, wy, my или pan/pani?', 'Просьба сделать один раз — обычно совершенный вид: [[Zamknij okno!]]', 'Запрет — nie + несовершенный: [[Nie zamykaj okna!]]', 'Для третьего лица и вежливо — [[niech]] + форма 3 лица.'])

T('tryb-przypuszczajacy', group='Глагол', level='B1', title_pl='Tryb przypuszczający', title_ru='Условное наклонение',
  lead='Chciałbym, mogłabyś, gdybyśmy… Вежливые просьбы, мечты и нереальные условия.',
  standard='Dz.U. 2025 poz. 217, Zał. 1, Część II, E (B1): 2.2.1 Fleksja, pkt 2 lit. a «tryb przypuszczający (np.: napisalibyście, przeczytałbyś)», s. 77; 2.2.3 Składnia, pkt 3 lit. b «podrzędnie ze spójnikami: … jeśli, jeżeli ..., to ..., gdyby ..., to ...», s. 78. На B2 (s. 89) — та же строка (przyniósłbym, zaczęlibyśmy, wzięłabym).',
  lvl='B1 — образование форм на -łby-, вежливые просьбы, gdyby и разница jeśli / gdyby.',
  depends=['czas-przeszly'], feeds=['zeby-aby (żeby + форма на -ł)', 'zdania warunkowe'],
  exam_text='Условному наклонению в сборнике посвящён целый блок 9 (зад. I–V: формы, gdyby, перефразирование) и задание IX блока 12. В реальных экзаменах оно встречается в задании VII «вид и наклонение» (например, 06.2022: spróbowalibyśmy, byłoby).',
  exam_refs=['k9-1', 'k9-2', 'k9-3', 'k9-4', 'k9-5', 'k12-9', ('b1-2022-06', 'g7')],
  steps=['Возьмите форму прошедшего времени нужного рода: [[mógł, mogła, mogli]].', 'Добавьте [[by]] и окончание лица: [[mógłbym, mogłabyś, moglibyśmy]].', 'Нереальное условие — [[gdyby]], реальное — [[jeśli / jeżeli]] с обычным временем.'])

T('czasowniki-ruchu', group='Глагол', level='B1', title_pl='Czasowniki ruchu', title_ru='Глаголы движения',
  lead='Iść или chodzić, jechać или jeździć — и что меняют приставки przy-, wy-, do-, prze-.',
  standard='Dz.U. 2025 poz. 217, Zał. 1, Część II, E (B1): отдельной строки о глаголах движения нет; они входят в 2.2.1 Fleksja, pkt 2 lit. a «czas teraźniejszy (np.: … chodzę, jadę …)» и «czas przeszły … (np.: … poszłam …)», и в pkt 2 lit. b «aspekt», s. 77.',
  lvl='B1 — iść/chodzić, jechać/jeździć, pójść/pojechać, приставочные глаголы и предлоги «куда / откуда».',
  depends=['czas-terazniejszy', 'czas-przeszly', 'aspekt'], feeds=['przyimki miejsca i kierunku'],
  exam_text='Отдельного задания на глаголы движения в экзамене нет, но их формы постоянно встречаются в заданиях на времена и вопросы: сборник, блок 6, зад. III (poszedłeś, przyszła) и блок 12, зад. IV (przyjechać / wyszedł); экзамены 04.2023 и 03.2022, задание V (chodzi, przyszła, poszedł, pojechała).',
  exam_refs=['k6-3', 'k12-4', ('b1-2023-04', 'g5'), ('b1-2022-03', 'g5')],
  steps=['Пешком — [[iść / chodzić]], на транспорте — [[jechać / jeździć]].', 'Сейчас, в одну сторону — [[iść, jechać]]; регулярно, туда-обратно — [[chodzić, jeździć]].', 'Приставка даёт совершенный вид и направление: [[wyjść, przyjechać, dojść]].'])

T('dopelniacz-po-negacji', group='Падежи', level='B1', title_pl='Dopełniacz po negacji', title_ru='Родительный падеж при отрицании',
  lead='Mam czas — nie mam czasu. Почему после nie меняется падеж и когда он не меняется.',
  standard='Dz.U. 2025 poz. 217, Zał. 1, Część II, E (B1): 2.2.3 Składnia, pkt 1 lit. b «dopełniacz: … jako określenie czasownika zaprzeczonego (np.: Studentki nie przeczytały tych artykułów na dzisiaj.)» и «jako podmiot (np.: Studentów nie było na tym spotkaniu.)», s. 77; pkt 2 lit. c «zaprzeczone (np.: Niczym się nie interesujesz. Nikt nie przyszedł. Nigdy nie byłem w Polsce.)», s. 78.',
  lvl='B1 — nie + глагол + родительный, nie ma / nie było / nie będzie, исключения (być, падежи кроме винительного).',
  depends=['biernik', 'dopełniacz (окончания)'], feeds=['zaimki-nieokreslone (nikt, nic, żaden)'],
  exam_text='В сборнике есть отдельное задание на отрицание: блок 11, зад. X «przekształć zdania (negacja)». Родительный после nie нужен и в заданиях «поставьте слово в нужную форму», и в письме (nie było…, nie dostałam…).',
  exam_refs=['k11-10', 'k3-6'],
  steps=['Есть ли перед глаголом [[nie]]?', 'Если глагол без nie требует винительного — ставьте родительный: [[mam czas → nie mam czasu]].', 'Другие падежи не меняются: [[nie pomagam bratu, nie interesuję się sportem]].'])

T('liczebniki-z-rzeczownikami', group='Числительные', level='B1', title_pl='Liczebniki z rzeczownikami', title_ru='Числительные с существительными',
  lead='Dwa koty, pięć kotów, dwóch braci, dwoje dzieci. Какой падеж и какой глагол после числа.',
  standard='Dz.U. 2025 poz. 217, Zał. 1, Część II, E (B1): 2.2.1 Fleksja, pkt 1 lit. d «odmiana liczebników głównych (np.: jeden, dwa, dwie; cztery, czterej, czterech; pięć, pięciu; siedem, siedmiu)» и lit. a «męskoosobowych i niemęskoosobowych (np.: … czterech panów, czterej studenci ≠ cztery stoły, cztery studentki)», s. 76.',
  lvl='B1 — 2–4 и 5+ с существительным, dwa / dwie / dwaj / dwóch, собирательные dwoje, troje, согласование глагола, возраст и цены.',
  depends=['dopełniacz (мн. ч.)', 'męskoosobowe (мн. ч.)'], feeds=['склонение числительных (z pięcioma…) — отдельная тема'],
  exam_text='В сборнике числительным посвящено задание III блока 11 («поставьте числительные в нужную форму»). В письме числа нужны почти всегда: цены, возраст, количество людей и вещей.',
  exam_refs=['k11-3'],
  steps=['Посмотрите на последнюю цифру: 2, 3, 4 (кроме 12–14) — именительный мн. ч.', '5 и больше, 12–14 — родительный мн. ч.: [[pięć kotów]].', 'Мужчины: [[dwóch / trzech / pięciu panów]] + глагол в ед. ч. ср. р.: [[przyszło]].'])

T('zdania-ktory', group='Синтаксис', level='B1', title_pl='Zdania z „który”', title_ru='Придаточные со словом «który»',
  lead='Człowiek, który…, książka, którą…, dom, w którym… Który склоняется, как прилагательное.',
  standard='Dz.U. 2025 poz. 217, Zał. 1, Część II, E (B1): 2.2.1 Fleksja, pkt 1 lit. c «odmiana zaimków pytających: kto, co, jaki, który, czyj, ile», s. 76; 2.2.3 Składnia, pkt 3 lit. b «podrzędnie ze spójnikami: … który, jaki …», s. 78. На B2 (s. 91) — то же с предлогом перед który (Chłopak, na którego czekałaś…).',
  lvl='B1 — род и число który по существительному, падеж — по придаточному, предлог перед który, запятые.',
  depends=['biernik', 'dopełniacz', 'miejscownik', 'narzędnik'], feeds=['strona-bierna (rachunek, który został zapłacony)'],
  exam_text='Który — частый ответ в задании II реальных экзаменов «союзы» (например, 06.2024, 02.2024, 11.2023, 04.2023). В сборнике его формы проверяются в блоке 3 (зад. V — перефразирование, зад. VI — выбор формы).',
  exam_refs=[('b1-2024-06', 'g2'), ('b1-2024-02', 'g2'), ('b1-2023-11', 'g2'), 'k3-5', 'k3-6'],
  steps=['Род и число — как у слова, к которому относится: [[książka, która…]].', 'Падеж — по роли в придаточном: [[książka, którą czytam]].', 'Предлог — перед który: [[dom, w którym mieszkam]].', 'Придаточное выделяется запятыми.'])

T('zeby-aby', group='Синтаксис', level='B1', title_pl='Żeby / aby', title_ru='Цель, желание, просьба: «чтобы»',
  lead='Uczę się, żeby zdać. Chcę, żebyś przyszedł. Когда инфинитив, а когда форма на -ł.',
  standard='Dz.U. 2025 poz. 217, Zał. 1, Część II, E (B1): 2.2.3 Składnia, pkt 3 lit. b «zdania złożone podrzędnie ze spójnikami: że, żeby, …», s. 78. На B2 (s. 91) добавлены aby и by.',
  lvl='B1 — żeby + инфинитив и żeby + окончание + форма на -ł, просьбы и желания, że или żeby; aby — официальный вариант.',
  depends=['czas-przeszly', 'tryb-przypuszczajacy'], feeds=['mowa-zalezna (просьбы)'],
  exam_text='Żeby — частый ответ в задании II реальных экзаменов «союзы» (например, 06.2023, 04.2023, 02.2023, 03.2022). В сборнике — блок 11, зад. VIII и блок 12, зад. VI (союзы из рамки).',
  exam_refs=[('b1-2023-06', 'g2'), ('b1-2023-04', 'g2'), ('b1-2022-03', 'g2'), 'k11-8', 'k12-6'],
  steps=['Один и тот же человек — [[żeby]] + инфинитив.', 'Разные люди — [[żebym, żebyś, żeby…]] + форма на -ł.', 'Факт — [[że]], просьба или цель — [[żeby]].'])

T('strona-bierna', group='Глагол', level='B2', title_pl='Strona bierna', title_ru='Страдательный залог',
  lead='Dom został zbudowany w 1900 roku. Kto? Przez kogo? Слой B2 поверх B1.',
  standard='По стандарту это тема B2, не B1: Dz.U. 2025 poz. 217, Zał. 1, Część II, F (B2): 2.2.1 Fleksja, pkt 2 lit. d «strona bierna – w ograniczonym zakresie (np.: Dziecko jest myte przez matkę. Pokój zostanie uporządkowany przez Pawła.)», s. 89; 2.2.3 Składnia, lit. g «synonimia syntaktyczna (… Rachunek, który został zapłacony przez ojca…)», s. 92. В списке B1 (s. 75–78) страдательного залога нет.',
  lvl='B2 (слой поверх B1) — być / zostać + причастие на -any, -ony, -ty, przez + винительный, безличные -no / -to.',
  depends=['czas-przeszly', 'aspekt', 'biernik'], feeds=['imiesłowy przymiotnikowe (B2)'],
  exam_text='На экзамене B1 страдательный залог не проверяется: поиск по сборнику 2017 и всем 18 экзаменам на сайте не нашёл ни одного такого задания. Его полезно узнавать в текстах для чтения (новости, объявления), а на B2 он входит в список грамматики.',
  exam_refs=[],
  steps=['Событие — [[zostać]] + причастие: [[Most został otwarty.]]', 'Состояние — [[być]] + причастие: [[Sklep jest zamknięty.]]', 'Исполнитель — [[przez]] + винительный: [[przez prezydenta]].'])

T('mowa-zalezna', group='Синтаксис', level='B2', title_pl='Mowa zależna', title_ru='Косвенная речь',
  lead='Powiedział, że…, zapytała, czy…, prosił, żebym… Время не сдвигается. Слой B2 поверх B1.',
  standard='По стандарту это тема B2: Dz.U. 2025 poz. 217, Zał. 1, Część II, F (B2): 2.2.3 Składnia, lit. f «mowa niezależna i mowa zależna: wykładniki formalne…; zamiana mowy niezależnej na mowę zależną (np.: Mama powiedziała: Idź po zakupy! / Mama powiedziała, żebym poszedł po zakupy.)», s. 92. На B1 нужны только союзы że, żeby (2.2.3 pkt 3 lit. b, s. 78).',
  lvl='B2 (слой поверх B1) — że, czy, вопросительные слова, żeby в пересказе; время не меняется, меняются лицо и местоимения.',
  depends=['zeby-aby', 'tryb-rozkazujacy'], feeds=[],
  exam_text='Отдельного задания на косвенную речь в экзамене B1 нет (поиск по сборнику и 18 экзаменам на сайте). Но союзы [[że, czy, żeby]] из этой темы — частые ответы в задании II «союзы» (например, 05.2021: że, czy; образец 2019: że, czy, żeby), а пересказ нужен в письме и в устной части.',
  exam_refs=[('b1-2021-05', 'g2'), ('b1-2019', 'g2')],
  steps=['Утверждение — [[że]], вопрос «да / нет» — [[czy]], другие вопросы — то же слово ([[gdzie, kiedy]]).', 'Просьба и приказ — [[żeby]] + форма на -ł.', 'Время не сдвигается; меняются «я / ты» и местоимения.'])

T('stopniowanie', group='Прилагательное', level='B1', title_pl='Stopniowanie', title_ru='Степени сравнения',
  lead='Tani — tańszy — najtańszy, dobry — lepszy. Как сравнивать прилагательные и наречия.',
  standard='Dz.U. 2025 poz. 217, Zał. 1, Część II, E (B1): 2.2.2 Słowotwórstwo, pkt 1 «stopniowanie przymiotników: a) proste: regularnych (np.: pilny – pilniejszy, długi – dłuższy), supletywnych (np.: duży – większy), b) opisowe (np. bardziej chory)» и pkt 2 «stopniowanie przysłówków (np. szybko – szybciej; źle – gorzej; dużo – więcej; bardziej gorąco)», s. 77.',
  lvl='B1 — -szy / -ejszy, чередования, неправильные формы, bardziej / najbardziej, наречия, niż / od, coraz, im… tym.',
  depends=['przymiotnik (склонение)'], feeds=[],
  exam_text='Степени сравнения — постоянное задание III реальных экзаменов (например, 06.2024, 04.2024, 02.2024, 11.2023, 06.2023, 04.2023) и задание V блока 12 сборника. В письме — сравнения в отзывах и сообщениях на форуме.',
  exam_refs=[('b1-2024-06', 'g3'), ('b1-2024-04', 'g3'), ('b1-2023-11', 'g3'), 'k12-5'],
  steps=['Короткое прилагательное — [[-szy]], с трудной основой — [[-ejszy]].', 'Проверьте неправильные: [[dobry – lepszy, zły – gorszy, duży – większy, mały – mniejszy]].', 'Сравнение — [[niż]] + именительный или [[od]] + родительный.'])

T('swoj-siebie', group='Местоимения', level='B1', title_pl='Swój, jego; siebie, się', title_ru='Притяжательное «свой» и возвратное «себя»',
  lead='Kocha swoją żonę — а не jego żonę. Siebie, sobie, sobą, się.',
  standard='Dz.U. 2025 poz. 217, Zał. 1, Część II, E (B1): 2.2.1 Fleksja, pkt 1 lit. c «odmiana zaimków dzierżawczych: mój, twój, nasz, wasz, swój» и «odmiana zaimka zwrotnego: siebie, się», s. 76.',
  lvl='B1 — swój или jego / jej / ich, где swój невозможен, склонение swój, siebie / sobie / sobą / się, друг друга.',
  depends=['biernik', 'dopełniacz', 'celownik'], feeds=[],
  exam_text='Формы swój и siebie проверяются в сборнике: блок 3, зад. IV (местоимения: swojego, swojej, swoich) и зад. VI (siebie, sobie, sobą). В реальных экзаменах они встречаются в заданиях IV и V (например, 04.2024, 06.2024).',
  exam_refs=['k3-4', 'k3-6', ('b1-2024-04', 'g4'), ('b1-2024-06', 'g5')],
  steps=['Владелец — подлежащее этого же предложения? Тогда [[swój]].', 'В подлежащем [[swój]] не бывает: [[Jego brat…]], не «Swój brat…».', 'Действие на себя — [[się / siebie]]; падеж — по глаголу или предлогу.'])

T('imieslowy-przyslowkowe', group='Глагол', level='B2', title_pl='Imiesłowy przysłówkowe', title_ru='Деепричастия на -ąc и -wszy',
  lead='Idąc do pracy… Zjadłszy śniadanie… Одно подлежащее на всё предложение. Слой B2 поверх B1.',
  standard='По стандарту это тема B2: Dz.U. 2025 poz. 217, Zał. 1, Część II, F (B2): 2.2.1 Fleksja, pkt 2 lit. f «imiesłowy przysłówkowe (w ograniczonym zakresie): tworzenie i użycie imiesłowów współczesnych (np.: słuchając, pisząc), rozpoznawanie imiesłowów uprzednich (np.: wysłuchawszy, zjadłszy)», s. 89. В списке B1 (s. 75–78) деепричастий нет. На B2 формы на -wszy нужно только узнавать.',
  lvl='B2 (слой поверх B1) — образовать и употребить -ąc, узнать -wszy / -łszy; одно подлежащее, запятые, nie раздельно, отличие от -ący.',
  depends=['czas-terazniejszy', 'czas-przeszly', 'aspekt'], feeds=['imiesłowy przymiotnikowe (B2)'],
  exam_text='На экзамене B1 деепричастия не проверяются: поиск по сборнику 2017 и всем 18 экзаменам на сайте не нашёл таких заданий. Их стоит узнавать в текстах для чтения; на B2 образование форм на -ąc входит в список грамматики.',
  exam_refs=[],
  steps=['Одно ли подлежащее у оборота и главной части?', 'Одновременно — [[-ąc]] от несовершенного: [[czytając]].', 'Раньше — [[-wszy / -łszy]] от совершенного: [[przeczytawszy]].'])

T('rzeczowniki-odczasownikowe', group='Существительное', level='B2', title_pl='Rzeczowniki odczasownikowe', title_ru='Отглагольные существительные',
  lead='Czytanie, pływanie, palenie wzbronione. Существительные-действия. Слой B2 поверх B1.',
  standard='По стандарту образование отглагольных существительных — тема B2: Dz.U. 2025 poz. 217, Zał. 1, Część II, F (B2): 2.2.2 Słowotwórstwo, pkt 2 lit. a «derywacja rzeczowników odczasownikowych (np.: pisać – pisanie, rozumieć – rozumienie, liczyć – liczenie, szyć – szycie)», s. 90. В списке B1 (s. 75–78) этого пункта нет; частые слова (czytanie, gotowanie, zwiedzanie) встречаются на B1 как лексика.',
  lvl='B2 (слой поверх B1) — образование на -nie / -enie / -cie, склонение, сохранение вида, дополнение в родительном, предлоги и официальный стиль.',
  depends=['czas-przeszly', 'aspekt', 'dopełniacz'], feeds=[],
  exam_text='Отдельного задания на отглагольные существительные в экзамене B1 нет (поиск по сборнику и 18 экзаменам на сайте). Они часты в объявлениях и правилах (Palenie wzbronione) и в письме об увлечениях (Interesuję się gotowaniem).',
  exam_refs=[],
  steps=['Возьмите форму прошедшего времени: [[czytał → czyta-]].', 'Добавьте [[-nie / -enie / -cie]]: [[czytanie, robienie, picie]].', 'Дополнение — в родительном: [[czytanie książek]].'])

T('zaimki-nieokreslone', group='Местоимения', level='B1', title_pl='Ktoś, coś, nikt, nic', title_ru='Неопределённые и отрицательные местоимения',
  lead='Ktoś dzwonił. Nikt nie dzwonił. Двойное отрицание — норма.',
  standard='Dz.U. 2025 poz. 217, Zał. 1, Część II, E (B1): 2.2.1 Fleksja, pkt 1 lit. c «odmiana zaimków nieokreślonych: ktoś, coś» и «odmiana zaimków przeczących: nikt, nic», s. 76; 2.2.3 Składnia, pkt 2 lit. c «zaprzeczone (np.: Niczym się nie interesujesz. Nikt nie przyszedł. Nigdy nie byłem w Polsce.)», s. 78. Формы на -kolwiek и jakiś, któryś, żaden — в списке B2 (s. 88).',
  lvl='B1 — ktoś / coś, nikt / nic и их склонение, двойное отрицание, coś + родительный (coś ciekawego); -kolwiek и żaden — слой B2.',
  depends=['dopelniacz-po-negacji'], feeds=[],
  exam_text='В сборнике: блок 11, зад. X (отрицание: nikt, nikogo, nic, nigdy) и блок 3, зад. VI (nikogo, nikomu). В реальных экзаменах — задание I (например, 02.2022: nikogo, nikim; образец 2019: coś, czegoś, czymś).',
  exam_refs=['k11-10', 'k3-6', ('b1-2022-02', 'g1'), ('b1-2019', 'g1')],
  steps=['Есть отрицательное слово ([[nikt, nic, nigdy, nigdzie]])? Тогда при глаголе тоже [[nie]].', 'Падеж nikt / nic — по глаголу: [[nikogo nie widzę, niczym się nie interesuję]].', 'После [[coś, nic]] прилагательное в родительном: [[coś ciekawego]].'])

T('spojniki-przyczyna-przyzwolenie', group='Синтаксис', level='B1', title_pl='Bo, ponieważ, więc, chociaż', title_ru='Причина, следствие, уступка',
  lead='Bo, ponieważ, dlatego że — почему; więc, dlatego — поэтому; chociaż, mimo że — хотя.',
  standard='Dz.U. 2025 poz. 217, Zał. 1, Część II, E (B1): 2.2.3 Składnia, pkt 3 lit. a «współrzędnie ze spójnikami: oraz, a także, lub, albo, czy, dlatego, ale» и lit. b «podrzędnie ze spójnikami: że, żeby, ponieważ, bo, dlatego że, kiedy, gdy …», s. 78. Chociaż / choć, mimo / pomimo że, gdyż, lecz, zatem, toteż — в списке B2 (s. 91).',
  lvl='B1 — bo, ponieważ, dlatego że, więc, dlatego, ale; уступка (chociaż, mimo że, mimo + родительный) и официальные gdyż, zatem — слой B2.',
  depends=['dopełniacz (mimo + D.)'], feeds=[],
  exam_text='Эти союзы — постоянные ответы в задании II реальных экзаменов «союзы» (например, 11.2021: chociaż, ponieważ; 02.2022: bo, chociaż; 06.2023, 11.2022, 03.2022: ponieważ; 02.2023, 11.2023, 04.2024: bo, więc) и в задании VI блока 12 сборника.',
  exam_refs=[('b1-2021-11', 'g2'), ('b1-2022-02', 'g2'), ('b1-2023-06', 'g2'), ('b1-2024-04', 'g2'), 'k12-6'],
  steps=['Почему? — [[bo, ponieważ, dlatego że]].', 'И что из этого? — [[więc, dlatego]].', 'Вопреки чему? — [[chociaż, mimo że]] или [[mimo]] + родительный.'])
