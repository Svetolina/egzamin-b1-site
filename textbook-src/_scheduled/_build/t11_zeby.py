import sys; sys.path.insert(0, '/home/claude/build')
from lib import S, item, ex, save

ELON_Z = "https://elon.io/grammar/polish/verbs/conditional/zeby-purpose-and-wishes"
ELON_ZE = "https://elon.io/grammar/polish/conjunctions/subordinating-ze"
ELON_RS = "https://elon.io/grammar/polish/syntax/reported-speech"
ELON_K = "https://elon.io/grammar/polish/verbs-reference/wolac-prosic-kazac"
ELON_X = "https://elon.io/learn-polish/lesson/clauses-of-excess-(zbyt...-%C5%BCeby)"
DZ = "https://faculty.washington.edu/dziwirek/grammar/miscellaneous/polish-ze-zeby.pdf"
WIKI = "https://en.wikipedia.org/wiki/Polish_grammar"
WIKT = "https://www.wiktionary.com/wiki/%C5%BCeby"
ZPE = "https://zpe.gov.pl/watek/LP1AC9VRws/6/a/tryby-czasownika/D18kXuVcM"
VAIA = "https://www.vaia.com/en-us/explanations/polish/polish-syntax/polish-adverbial-clauses"
TR = "https://blogs.transparent.com/polish/?p=5133"
LANG = "https://en.langenscheidt.com/polish-german/kaza%C4%87"
LV = "https://journals.akademicka.pl/lv/article/view/5077"

dz = lambda loc: S("K. Dziwirek (University of Washington), «Polish że / żeby» — раздаточный материал", DZ, loc)
el = lambda loc: S("elon.io — «żeby: Purpose, Wishes, and Subordinate Mood»", ELON_Z, loc)
elze = lambda loc: S("elon.io — «że and żeby: That, So That»", ELON_ZE, loc)
wiki = lambda loc: S("Wikipedia (en) — «Polish grammar»", WIKI, loc)
wikt = lambda loc: S("Wiktionary — «żeby» (Polish, Conjunction)", WIKT, loc)
zpe = lambda loc: S("ZPE (Zintegrowana Platforma Edukacyjna, MEN) — «Tryby czasownika»", ZPE, loc)

F = [
 ("R1", "żeby = że + by. Личное окончание присоединяется к самому союзу и пишется слитно: żebym, żebyś, żeby, żebyśmy, żebyście, żeby (3-е лицо без окончания). Так же aby: abym, abyś, abyśmy, abyście.",
  [el("раздел «żeby = że + by, and it takes the clitic»"), wiki("раздел Conjunctions / Subjunctive clauses: «the by of the conjunction … takes personal endings»"), zpe("часть о частице by: «Pisownia» — łącznie ze spójnikami (gdybym…); пример «Żebyś wiedział!»")]),
 ("R2", "Цель при одном и том же субъекте: żeby + инфинитив. Uczę się, żeby zdać egzamin.",
  [dz("раздел Purpose clauses: «purpose clauses are introduced by żeby followed by an infinitive»"), el("раздел «Purpose: the same-subject vs different-subject split»"), S("Transparent Language Polish Blog — «So what's the trick with Polish clauses?» (30.05.2014)", TR, "пункт aby/żeby + bezokolicznik: «Odwiedziłam ją, aby/żeby jej pogratulować»")]),
 ("R3", "Если субъекты разные, после żeby стоит форма прошедшего времени на -ł (без личного окончания — оно уже на żeby): Mówię głośno, żebyś słyszał. Настоящее и будущее время после żeby не употребляются (не *żeby on przyjdzie, а żeby przyszedł).",
  [el("разделы «Purpose: the same-subject vs different-subject split» и «Common Mistakes»"), wiki("Conjunctions: aby/żeby «can take an infinitive phrase or a past-tense sentence»"), wikt("значения 1, 2: «with past tense»")]),
 ("R4", "В придаточном цели żeby обязателен — его нельзя опустить, как английское to: Pan Orłowski jest w biurze, żeby pracować.",
  [dz("раздел Purpose clauses: «żeby is NOT optional»"), el("раздел «Purpose …»: смешение конструкций названо «the classic error»")]),
 ("R5", "После глаголов хотения, просьбы, приказа (chcieć, prosić, powiedzieć, mówić в значении «велеть») при другом исполнителе — żeby + форма на -ł: Chcę, żebyś przyszedł. Конструкции «хотеть + кого-то + инфинитив» нет: не *chcę ciebie przyjść. Если исполнитель тот же — просто инфинитив: Chcę przyjść.",
  [el("раздел «Indirect commands and requests: ‘I want you to…’»"), wiki("Subjunctive clauses: «used with verbs meaning ‘want’, ‘expect’», пример chce, żeby(m) śpiewał"), S("elon.io — «reported speech»", ELON_RS, "пункт Commands and requests: «Powiedział, żebym poszedł do domu»")]),
 ("R6", "Пожелания: Chciałbym/Chciałabym, żeby…; Marzę o tym, żeby…; восклицание Żebyś wiedział! («Ещё бы!», разг.).",
  [el("раздел «Wishes: Chciałbym, żeby…»"), wikt("значение «desire or wish, with past tense»; пример «Żebyś wiedział!»"), zpe("пример «Żebyś wiedział!»")]),
 ("R7", "że сообщает факт (глагол в обычном времени), żeby — цель, желание, просьбу. Один и тот же глагол меняет смысл: Powiedz mu, że zadzwonił (сообщи факт) — Powiedz mu, żeby zadzwonił (передай просьбу). Перед że и żeby всегда ставится запятая.",
  [elze("разделы «że vs żeby»; пример с powiedz mu"), dz("раздел Complement clauses: «finite complement clauses are introduced by że»"), S("elon.io — «reported speech»", ELON_RS, "пункты Statements (że) и Commands and requests (żeby); «A comma always precedes że, czy, żeby»")]),
 ("R8", "Сомнение и отрицаемое мнение (nie sądzę, nie wydaje mi się, wątpię) часто вводятся через żeby + форма на -ł: Nie sądzę, żeby to był dobry pomysł.",
  [elze("пример «Nie sądzę, żeby to był dobry pomysł» — отрицание переводит в ирреальность"), wikt("значение «doubt, chiefly in negated sentences: that, if (past tense)»")]),
 ("R9", "Отрицательная цель: żeby nie + инфинитив / форма на -ł: Śpieszę się, żeby nie być spóźniona. Idź na palcach, żeby nie obudzić dziecka. Прямое дополнение при отрицании — в dopełniacz (см. тему 8).",
  [dz("примеры «Studiuję, żeby się nie nudzić», «Śpieszę się, żeby nie być spóźniona»"), el("пример «Idź na palcach, żeby nie obudzić dziecka»")]),
 ("R10", "«Слишком … чтобы»: za/zbyt + прилагательное/наречие, żeby + инфинитив: Jestem zbyt zajęta, żeby robić zakupy. Kawa jest za gorąca, żeby ją pić.",
  [dz("пример «Jestem zbyt zajęta, żeby robić zakupy»"), S("elon.io — урок «clauses of excess (zbyt… żeby)»", ELON_X, "весь урок")]),
 ("R11", "aby значит то же, что żeby, но звучит официальнее/книжнее; by и ażeby — ещё книжнее. Окончания те же: abym, byś…",
  [el("раздел «aby and the formal register»"), S("Vaia — «Polish Adverbial Clauses»", VAIA, "раздел о purpose: aby — «more formal», żeby — «spoken language», пример «Piszę, by pamiętać»"), wiki("Subjunctive clauses: перечень żeby, iżby, ażeby, aby, coby; пример chce, by(m) śpiewał")]),
 ("R12", "Придаточное с żeby может стоять в начале предложения: Żeby być dobrym studentem, trzeba dużo się uczyć.",
  [dz("пример «Żeby być dobrym studentem, trzeba dużo się uczyć»"), S("Vaia — «Polish Adverbial Clauses»", VAIA, "примеры цели с aby/żeby")]),
 ("R13", "kazać («велеть») обычно управляет дательным лицом + инфинитивом, без żeby: Kazał mi czekać. Kazał nam kupić chleb.",
  [S("elon.io — «wołać, prosić, kazać»", ELON_K, "раздел kazać: «kazać + [DATIVE] + [INFINITIVE]»"), S("Langenscheidt Polish–German — «kazać»", LANG, "конструкция «kazać [komuś] + bezokolicznik», примеры kazał nam milczeć / kupić chleb")]),
 ("R14", "tak, żeby — «так, чтобы»: Piotr kupił samochód tak, żeby móc pojechać do Francji.",
  [S("Transparent Language Polish Blog — «So what's the trick with Polish clauses?»", TR, "пункт «tak, aby / tak, żeby»"), el("раздел «Purpose …» (żeby = so that)")]),
 ("R15", "После глаголов движения цель часто выражается просто инфинитивом: Idę spać. Pobiegł otworzyć drzwi. (Можно и с żeby: Idę tam, żeby robić zakupy.)",
  [S("M. Danielewiczowa, I. Duraj-Nowosielska, «Polski bezokolicznik celu przy czasownikach ruchu», LingVaria 18(1)(35), 2023", LV, "с. 41–61, аннотация"), dz("пример с żeby после глагола движения: «Idę tam, żeby robić zakupy»")]),
]
extract = {"topic": "zeby-aby", "title": "Żeby / aby", "facts": [
    {"id": i, "rule": r, "sources": s} for i, r, s in F]}
# R15: инфинитив без żeby прямо описан только в одном источнике (LingVaria) — помечаем
extract["facts"][-1]["single_source_note"] = "Инфинитив без żeby после глаголов движения прямо описан в одном источнике; второй подтверждает только вариант с żeby. Даётся одной строкой с пометкой."

sections = [
 {"id": "s1", "title": "Что такое żeby и aby", "facts": ["R1", "R2", "R3"],
  "body": "**Żeby** (книжн. **aby**) вводит придаточное цели («чтобы»), желания и просьбы. Главное правило всей темы:\n\n- **один и тот же человек** → żeby + **инфинитив**: *Uczę się, żeby zdać egzamin.*\n- **разные люди** → żeb**y + окончание** + форма **на -ł**: *Mówię głośno, żebyś słyszał.*\n\n💡 Подсказка для русскоговорящих: как и в русском «чтобы ты пришёл», после żeby стоит форма прошедшего времени.",
  "examples": [["Uczę się, żeby zdać egzamin.", "Учусь, чтобы сдать экзамен."], ["Mówię głośno, żebyś słyszał.", "Говорю громко, чтобы ты слышал."]]},
 {"id": "s2", "title": "Окончания: żebym, żebyś…", "facts": ["R1", "R3"],
  "body": "Личное окончание «уезжает» на союз, а глагол стоит в форме на -ł **без** окончания.",
  "table": {"head": ["Лицо", "żeby + …", "пример (iść → poszedł/poszła)"], "rows": [
     ["ja", "żebym", "żebym poszedł / poszła"], ["ty", "żebyś", "żebyś poszedł / poszła"],
     ["on / ona / ono", "żeby", "żeby poszedł / poszła / poszło"], ["my", "żebyśmy", "żebyśmy poszli / poszły"],
     ["wy", "żebyście", "żebyście poszli / poszły"], ["oni / one", "żeby", "żeby poszli / poszły"]]},
  "note": "Неверно: *żeby poszedłem*, *żebym poszłem*. Окончание -m/-ś/-śmy/-ście — только одно и только на żeby."},
 {"id": "s3", "title": "Один субъект → инфинитив", "facts": ["R2", "R4", "R12"],
  "body": "Если «чтобы» относится к тому же человеку, что и главный глагол, — инфинитив. Żeby **обязателен**, его нельзя пропустить. Придаточное может стоять и в начале.",
  "examples": [["Anna oszczędza, żeby kupić mieszkanie.", "Анна копит, чтобы купить квартиру."], ["Żeby być dobrym studentem, trzeba dużo się uczyć.", "Чтобы быть хорошим студентом, надо много учиться."]]},
 {"id": "s4", "title": "Разные субъекты → форма на -ł", "facts": ["R3"],
  "body": "Если действие выполняет другой человек, после żeby — форма на -ł, согласованная с ним по роду и числу. Настоящее и будущее время **не** ставятся.",
  "examples": [["Zostawiłem ci klucz, żebyś mogła wejść.", "Я оставил тебе ключ, чтобы ты могла войти."], ["Otwórz okno, żeby weszło świeże powietrze.", "Открой окно, чтобы вошёл свежий воздух."]],
  "note": "Ошибка: *żeby on przyjdzie* → правильно *żeby przyszedł*."},
 {"id": "s5", "title": "Хочу, чтобы ты… / Прошу, чтобы…", "facts": ["R5"],
  "body": "chcieć, prosić, powiedzieć, mówić (в значении «велеть») + **żeby** при другом исполнителе. Так же передаётся приказ в косвенной речи: «Kup chleb!» → *Powiedziała, żebym kupił chleb.*",
  "table": {"head": ["Тот же человек", "Другой человек"], "rows": [["Chcę przyjść.", "Chcę, żebyś przyszedł."], ["Proszę o pomoc.", "Proszę, żebyś mi pomógł."]]},
  "note": "Не бывает: *chcę ciebie przyjść*, *chcę, żebym przyszedł* (если это я сам)."},
 {"id": "s6", "title": "kazać — без żeby", "facts": ["R13"],
  "body": "Глагол **kazać** («велеть») обычно сочетается с дательным падежом лица и инфинитивом.",
  "examples": [["Kazał mi czekać.", "Он велел мне ждать."], ["Szefowa kazała nam kupić chleb.", "Начальница велела нам купить хлеб."]],
  "note": "Не *Kazał mnie czekać* (лицо — в celowniku)."},
 {"id": "s7", "title": "Пожелания", "facts": ["R6"],
  "body": "*Chciałbym / Chciałabym, żeby…*, *Marzę o tym, żeby…*. Разговорное восклицание *Żebyś wiedział!* — «Ещё бы! / Если бы ты знал!».",
  "examples": [["Chciałabym, żeby ten rok był spokojniejszy.", "Я бы хотела, чтобы этот год был спокойнее."], ["Marzę o tym, żebyśmy pojechali nad morze.", "Мечтаю о том, чтобы мы поехали на море."]]},
 {"id": "s8", "title": "że или żeby?", "facts": ["R7"],
  "body": "**że** — факт (обычное время): *Wiem, że masz rację.* **żeby** — цель, желание, просьба (форма на -ł / инфинитив). Перед обоими — **запятая**.",
  "table": {"head": ["że (факт)", "żeby (просьба)"], "rows": [["Powiedz mu, że dzwoniła mama.", "Powiedz mu, żeby zadzwonił do mamy."], ["Napisała, że wróci w niedzielę.", "Napisała, żebyśmy na nią nie czekali."]]}},
 {"id": "s9", "title": "Сомнение: nie sądzę, żeby…", "facts": ["R8"],
  "body": "После *nie sądzę, nie wydaje mi się, wątpię* обычно żeby + форма на -ł (сравните: *Myślę, że to dobry pomysł* — *Nie sądzę, żeby to był dobry pomysł*).",
  "examples": [["Wątpię, żeby zdążył na pociąg.", "Сомневаюсь, что он успел/успеет на поезд."]]},
 {"id": "s10", "title": "Чтобы не…", "facts": ["R9"],
  "body": "**żeby nie** + инфинитив или форма на -ł. Прямое дополнение при отрицании — в dopełniacz (тема 8): *żeby nie zgubić kluczy*.",
  "examples": [["Idź na palcach, żeby nie obudzić dziecka.", "Иди на цыпочках, чтобы не разбудить ребёнка."], ["Powiedz mu, żeby nie palił papierosów.", "Скажи ему, чтобы не курил."]]},
 {"id": "s11", "title": "Слишком… чтобы; так, чтобы", "facts": ["R10", "R14"],
  "body": "**za / zbyt** + прилагательное, **żeby** + инфинитив. **tak, żeby** — «так, чтобы».",
  "examples": [["Jest za późno, żeby zaczynać nowy temat.", "Слишком поздно, чтобы начинать новую тему."], ["Mów tak, żeby wszyscy słyszeli.", "Говори так, чтобы все слышали."]]},
 {"id": "s12", "title": "aby, by, ażeby — стиль", "facts": ["R11"],
  "body": "Смысл одинаковый. **żeby** — нейтрально и в разговоре; **aby** — официально (письма в учреждения, объявления); **by, ażeby** — книжно. В официальном письме на экзамене уместно *aby*.",
  "examples": [["Uprzejmie proszę, aby Pan odpowiedział do piątku.", "Убедительно прошу Вас ответить до пятницы."]]},
 {"id": "s13", "title": "Глаголы движения: иногда без żeby", "facts": ["R15"],
  "body": "После iść, pójść, pobiec и т. п. цель часто выражается просто инфинитивом: *Idę spać. Pobiegł otworzyć drzwi.* Вариант с żeby тоже правилен: *Idę tam, żeby zrobić zakupy.*",
  "note": "Правило подтверждено одним источником напрямую — дано одной строкой."},
]

M = 'żebym poszedł'
exs = []
exs.append(ex("e1", "Окончание на żeby", "gaps",
  "Впишите żeby с нужным окончанием (в 12 — aby).", [
  item("Mama prosi, {1} (ja) wrócił przed dziesiątą.", "żebym"),
  item("Chcę, {1} (ty) zadzwonił do mnie jutro.", "żebyś"),
  item("Szef chce, {1} (my) skończyli raport do piątku.", "żebyśmy"),
  item("Proszę, {1} (wy) nie rozmawiali w czasie egzaminu.", "żebyście"),
  item("Nauczycielka chce, {1} (oni) przeczytali ten tekst.", "żeby"),
  item("Lekarz powiedział, {1} (ona) dużo piła.", "żeby"),
  item("Powiedz mu, {1} (on) zaczekał.", "żeby"),
  item("Rodzice chcą, {1} (ja) studiowała medycynę.", "żebym"),
  item("Prosiliśmy, {1} (ty) się nie spóźniała.", "żebyś"),
  item("Chciałbym, {1} (wy) przyjechali do nas w lipcu.", "żebyście"),
  item("Koledzy proszą, {1} (my) zrobili przerwę.", "żebyśmy"),
  item("Dyrektor prosi, {1} (wy) przyszli o ósmej.", "abyście", hint="aby + окончание"),
 ], ["R1"], example={"q": "Chcę, ___ (ty) przyszedł.", "a": "żebyś"}))

exs.append(ex("e2", "Инфинитив или форма на -ł?", "gaps",
  "Поставьте глагол в скобках в нужную форму: инфинитив (тот же субъект) или форму на -ł (другой субъект).", [
  item("Uczę się wieczorami, żeby {1} (zdać) egzamin B1.", "zdać"),
  item("Mówię wolno, żebyś mnie dobrze {1} (zrozumieć; ty — м.).", "zrozumiał"),
  item("Anna oszczędza pieniądze, żeby {1} (kupić) mieszkanie.", "kupić"),
  item("Otwórz okno, żeby {1} (wejść) świeże powietrze.", "weszło"),
  item("Zostawiłem ci klucz, żebyś {1} (móc; ty — ж.) wejść.", "mogła"),
  item("Wstałam wcześnie, żeby się nie {1} (spóźnić) na pociąg.", "spóźnić"),
  item("Dzwonię, żebyś {1} (wiedzieć; ty — м.), co się stało.", "wiedział"),
  item("Pracujemy dużo, żeby nasze dzieci {1} (mieć) lepsze życie.", "miały"),
  item("Piotr poszedł do apteki, żeby {1} (kupić) leki.", "kupić"),
  item("Napiszę do Ewy, żeby {1} (przyjść) na urodziny.", "przyszła"),
  item("Ćwiczę codziennie, żeby {1} (być) zdrowym.", "być"),
  item("Zamknij drzwi, żeby kot nie {1} (uciec).", "uciekł"),
  item("Kupiłem mapę, żebyśmy się nie {1} (zgubić).", "zgubili"),
  item("Przyjechali wcześniej, żeby nam {1} (pomóc).", "pomóc"),
 ], ["R2", "R3"]))

exs.append(ex("e3", "Соедините предложения", "gaps",
  "Соедините два предложения с помощью żeby. Напечатайте только часть с żeby (aby тоже засчитывается).", [
  item("Jadę do Krakowa. Chcę zwiedzić Wawel. → Jadę do Krakowa, {1}.", "żeby zwiedzić Wawel", aby=True),
  item("Uczę się polskiego. Chcę pracować w Polsce. → Uczę się polskiego, {1}.", "żeby pracować w Polsce", aby=True),
  item("Mówię głośno. Wszyscy mają mnie słyszeć. → Mówię głośno, {1}.", "żeby wszyscy mnie słyszeli", aby=True),
  item("Kupiłam słownik. Chcę szybciej czytać. → Kupiłam słownik, {1}.", "żeby szybciej czytać", aby=True),
  item("Daję ci mój numer. Możesz do mnie zadzwonić. → Daję ci mój numer, {1}.", "żebyś mógł do mnie zadzwonić|żebyś mogła do mnie zadzwonić", aby=True),
  item("Wychodzimy wcześniej. Nie chcemy stać w korku. → Wychodzimy wcześniej, {1}.", "żeby nie stać w korku", aby=True),
  item("Mama gotuje zupę. Dzieci mają zjeść coś ciepłego. → Mama gotuje zupę, {1}.", "żeby dzieci zjadły coś ciepłego", aby=True),
  item("Oszczędzam. Chcę pojechać na wakacje. → Oszczędzam, {1}.", "żeby pojechać na wakacje", aby=True),
  item("Tłumaczę ci to jeszcze raz. Masz wszystko zrozumieć. → Tłumaczę ci to jeszcze raz, {1}.", "żebyś wszystko zrozumiał|żebyś wszystko zrozumiała", aby=True),
  item("Włączyłem światło. Chciałem coś zobaczyć. → Włączyłem światło, {1}.", "żeby coś zobaczyć", aby=True),
  item("Zapisałam adres. Nie chciałam go zapomnieć. → Zapisałam adres, {1}.", "żeby go nie zapomnieć", aby=True),
  item("Piszę do was. Macie przyjść w sobotę. → Piszę do was, {1}.", "żebyście przyszli w sobotę", aby=True),
 ], ["R2", "R3", "R9"]))

exs.append(ex("e4", "Передайте просьбу", "gaps",
  "Передайте просьбу/приказ с помощью żeby. Если говорит «я», засчитываются обе формы рода.", [
  item("Mama do mnie: «Posprzątaj pokój!» → Mama chce, {1} pokój.", "żebym posprzątał|żebym posprzątała"),
  item("Szef do nas: «Skończcie projekt do piątku!» → Szef chce, {1} projekt do piątku.", "żebyśmy skończyli|żebyśmy skończyły"),
  item("Lekarz do pacjenta: «Proszę nie palić!» → Lekarz prosi pacjenta, {1}.", "żeby nie palił"),
  item("Ja do ciebie: «Zadzwoń wieczorem!» → Proszę cię, {1} wieczorem.", "żebyś zadzwonił|żebyś zadzwoniła"),
  item("Nauczyciel do uczniów: «Otwórzcie książki!» → Nauczyciel mówi, {1} książki.", "żeby otworzyli"),
  item("Anna do Marka: «Kup chleb!» → Anna powiedziała Markowi, {1} chleb.", "żeby kupił"),
  item("Policjant do kierowcy: «Proszę pokazać dokumenty.» → Policjant poprosił kierowcę, {1} dokumenty.", "żeby pokazał"),
  item("Babcia do wnuczki: «Ubierz się ciepło!» → Babcia mówi wnuczce, {1} ciepło.", "żeby się ubrała|żeby ubrała się"),
  item("Koleżanka do mnie: «Pomóż mi!» → Koleżanka prosi, {1}.", "żebym jej pomógł|żebym jej pomogła|żebym pomógł jej|żebym pomogła jej"),
  item("Rodzice do nas: «Nie wracajcie późno!» → Rodzice proszą, {1} późno.", "żebyśmy nie wracali|żebyśmy nie wracały"),
  item("Urzędniczka do mnie: «Proszę wypełnić formularz.» → Urzędniczka prosi, {1} formularz.", "żebym wypełnił|żebym wypełniła"),
  item("Ty do Ewy: «Przyjdź jutro!» → Powiedz Ewie, {1} jutro.", "żeby przyszła"),
 ], ["R5", "R1", "R3"]))

exs.append(ex("e5", "że или żeby?", "gaps",
  "Впишите że или żeby (aby тоже засчитывается).", [
  item("Wiem, {1} masz rację.", "że"),
  item("Chcę, {1} przyszedł wcześniej.", "żeby", aby=True),
  item("Powiedz mu, {1} dzwoniła mama.", "że"),
  item("Powiedz mu, {1} zadzwonił do mamy.", "żeby", aby=True),
  item("Myślę, {1} to dobry pomysł.", "że"),
  item("Nie sądzę, {1} to był dobry pomysł.", "żeby", aby=True),
  item("Cieszę się, {1} przyjechałeś.", "że"),
  item("Marzę o tym, {1} mieć własny dom.", "żeby", aby=True),
  item("Napisała, {1} wróci w niedzielę.", "że"),
  item("Napisała, {1} na nią nie czekać.", "żeby", aby=True),
  item("Słyszałem, {1} szukasz pracy.", "że"),
  item("Wątpię, {1} zdążył na pociąg.", "żeby", aby=True),
  item("Szef uważa, {1} projekt jest gotowy.", "że"),
  item("Zależy mi na tym, {1} wszyscy byli zadowoleni.", "żeby", aby=True),
 ], ["R7", "R8"]))

exs.append(ex("e6", "Чтобы не… (+ dopełniacz)", "gaps",
  "Поставьте слово в скобках в нужную форму (после отрицания — dopełniacz; глагол — форма на -ł).", [
  item("Schowaj portfel, żeby nie zgubić {1} (pieniądze).", "pieniędzy"),
  item("Mów cicho, żeby nie obudzić {1} (dziecko).", "dziecka"),
  item("Jedź wolno, żeby nie mieć {1} (wypadek).", "wypadku"),
  item("Uczę się codziennie, żeby nie stracić {1} (motywacja).", "motywacji"),
  item("Wyłączyłem telefon, żeby nie słyszeć {1} (powiadomienia).", "powiadomień"),
  item("Zrób listę, żeby nie zapomnieć {1} (nic).", "niczego"),
  item("Wyszliśmy wcześniej, żeby nie przegapić {1} (początek) filmu.", "początku"),
  item("Piję dużo wody, żeby nie mieć {1} (ból) głowy.", "bólu"),
  item("Zapisz hasło, żeby nie zablokować {1} (konto).", "konta"),
  item("Przeczytaj umowę, żeby nie podpisać {1} (zły dokument).", "złego dokumentu"),
  item("Poproś go, żeby nie {1} (palić) w domu.", "palił"),
  item("Prosiłam was, żebyście nie {1} (jeść; вы — м.) słodyczy przed obiadem.", "jedli"),
 ], ["R9", "R3"]))

exs.append(ex("e7", "Слишком…, чтобы; сомнение", "gaps",
  "Поставьте глагол в нужную форму.", [
  item("Jestem zbyt zmęczona, żeby {1} (iść) na imprezę.", "iść"),
  item("Kawa jest za gorąca, żeby ją {1} (pić) od razu.", "pić"),
  item("Jest za późno, żeby {1} (zaczynać) nowy temat.", "zaczynać"),
  item("Ten plecak jest za ciężki, żeby go {1} (nieść) jedną ręką.", "nieść"),
  item("On jest za młody, żeby {1} (prowadzić) samochód.", "prowadzić"),
  item("Nie sądzę, żeby to {1} (być) prawda.", "była"),
  item("Wątpię, żeby Marek {1} (zdążyć) na czas.", "zdążył"),
  item("Nie wydaje mi się, żeby oni {1} (chcieć) przyjść.", "chcieli"),
  item("Wątpię, żebyś {1} (znaleźć; ty — м.) tani bilet w sierpniu.", "znalazł"),
  item("Mów tak, żeby wszyscy cię {1} (słyszeć).", "słyszeli"),
 ], ["R10", "R8", "R14"]))

exs.append(ex("e8", "Тест в формате экзамена: письмо", "gaps",
  "Uzupełnij tekst. Wpisz że/żeby (z końcówką) i czasownik w odpowiedniej formie. W nawiasie: podmiot i bezokolicznik. Ola — kobieta, Kasia — kobieta.", [
  item("Cześć Kasiu! Piszę, {1} (zapytać) cię o radę.", "żeby zapytać", aby=True),
  item("Moja szefowa chce, {1} (ja: pojechać) w przyszłym miesiącu na szkolenie do Gdańska.", "żebym pojechała", aby=True),
  item("Chciałabym, {1} (ty: pojechać) ze mną, bo sama trochę się boję.", "żebyś pojechała", aby=True),
  item("Szefowa powiedziała, {1} (ja: zarezerwować) hotel jak najszybciej,", "żebym zarezerwowała", aby=True),
  item("{1} (nie płacić) za dużo.", "żeby nie płacić", aby=True),
  item("Mój mąż prosi, {1} (my: wziąć) też dzieci,", "żebyśmy wzięli", aby=True),
  item("ale nie sądzę, {1} (to: być) dobry pomysł — szkolenie trwa cały dzień.", "żeby to był", aby=True),
  item("Poza tym jest za daleko, {1} (jechać) z małymi dziećmi samochodem.", "żeby jechać", aby=True),
  item("Mama obiecała, {1} (ona: przyjść) do nas i zajmie się dziećmi.", "że przyjdzie"),
  item("Napisz mi, proszę, czy masz czas, {1} (ja: wiedzieć) wcześniej.", "żebym wiedziała", aby=True),
  item("Kupię bilety wcześniej, {1} (one: być) tańsze.", "żeby były", aby=True),
  item("Zależy mi na tym, {1} (wszystko: być) gotowe do piątku. Ściskam, Ola", "żeby wszystko było", aby=True),
 ], ["R1", "R2", "R3", "R5", "R7", "R8", "R10"], fmt="exam-text"))

exs.append(ex("e9", "Przekształcenia", "gaps",
  "Перестройте предложение, начиная с данного начала (как в задании VI экзамена). Напечатайте продолжение.", [
  item("«Zamknij okno!» — powiedziała mi mama. → Mama powiedziała, {1}.", "żebym zamknął okno|żebym zamknęła okno", aby=True),
  item("Uczę się polskiego w celu znalezienia pracy. → Uczę się polskiego, {1}.", "żeby znaleźć pracę", aby=True),
  item("Szef do mnie: «Proszę przygotować raport.» → Szef poprosił mnie, {1}.", "żebym przygotował raport|żebym przygotowała raport", aby=True),
  item("Ta walizka jest bardzo ciężka. Nie da się jej podnieść. → Ta walizka jest za ciężka, {1}.", "żeby ją podnieść", aby=True),
  item("Myślę, że to nie jest prawda. → Nie sądzę, {1}.", "żeby to była prawda", aby=True),
  item("Mówię wolno, bo chcę, żebyście mnie zrozumieli. → Mówię wolno, {1}.", "żebyście mnie zrozumieli", aby=True),
  item("Powiedział, żebym czekał. → Kazał {1}.", "mi czekać"),
  item("Исправьте ошибку: Chcę, żebym pojechał do Gdańska. → Chcę {1}.", "pojechać do Gdańska"),
 ], ["R2", "R3", "R5", "R8", "R10", "R13"], fmt="rewrite"))

exs.append({"id": "w1", "kind": "writing", "title": "Письмо подруге (неофициальное)", "facts": ["R2", "R3", "R5"],
  "instr": "Napisz e-mail do koleżanki (80–100 słów). Przeprowadzasz się i potrzebujesz pomocy. Napisz: kiedy i dlaczego się przeprowadzasz; o co ją prosisz; co chcesz zrobić, żeby przeprowadzka poszła szybko; jak jej podziękujesz.",
  "checklist": ["не меньше 4 конструкций с żeby", "хотя бы 2 — с другим субъектом (żebyś…, żebyśmy…)", "хотя бы 1 — żeby nie …", "обращение и подпись"]})
exs.append({"id": "w2", "kind": "writing", "title": "Официальное письмо администрации", "facts": ["R11", "R3"],
  "instr": "Napisz list do administracji budynku (80–100 słów). W Twoim mieszkaniu od tygodnia nie działa ogrzewanie. Opisz problem, poproś o naprawę i termin wizyty, zaproponuj, jak się z Tobą skontaktować.",
  "checklist": ["официальное обращение (Szanowni Państwo)", "не меньше 3 конструкций с aby (abym, aby Państwo…)", "просьба через «Uprzejmie proszę, aby…»", "официальная подпись (Z poważaniem)"]})

topic = {"id": "zeby-aby", "num": 11, "title": "Żeby / aby: цель, желание, просьба", "level": "B1",
  "lang": "ru", "prev": "zdania-ktory", "next": "strona-bierna",
  "summary": "Как сказать «чтобы»: żeby + инфинитив (тот же человек) или żeby + окончание + форма на -ł (другой человек); просьбы, пожелания, że/żeby, aby в официальном стиле.",
  "sections": sections, "exercises": exs}

save("zeby-aby", extract, topic)
