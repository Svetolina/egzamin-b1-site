import sys; sys.path.insert(0, '/home/claude/build')
from lib import S, item, ex, save

RS = "https://elon.io/grammar/polish/syntax/reported-speech"
AK = "https://aleklasa.pl/gimnazjum/gramatyka/c185-slowotworstwo/15-mowa-zalezna-i-niezalezna"
KO = "http://agnieszkakochan.pl/mowa-zalezna-i-niezalezna/"
EK = "https://elon.io/grammar/polish/verbs-reference/wolac-prosic-kazac"
GOV = "https://www.gov.pl/zdalnelekcje/jezyk-polski-luty-2021-r7"

rs = lambda l: S("elon.io — «Polish reported speech»", RS, l)
ak = lambda l: S("Aleklasa.pl — «Mowa zależna i niezależna» (материал, рекомендованный в уроке gov.pl «Zdalne lekcje», Temat 51)", AK, l)
ko = lambda l: S("Agnieszka Kochan — «Mowa zależna i niezależna»", KO, l)

F = [
 ("R1", "Четыре типа: утверждение → że; вопрос «да/нет» → czy; вопрос с вопросительным словом → то же слово (gdzie, kiedy, co…); приказ/просьба → żeby (aby, ażeby, by).",
  [ak("разделы о zdaniach oznajmujących, pytających i rozkazujących"), ko("пункты 1–4"), rs("«Polish reported speech at a glance»")]),
 ("R2", "Время глагола не «сдвигается», как в английском: сохраняется время исходной фразы. Jan powiedział wczoraj: «Jestem chory» → Jan powiedział, że jest chory.",
  [rs("пункт Statements: «keep the original tense»; «The most common error is backshifting»"), ak("пример «Nauczyciel powiedział nam, że dzisiaj idziemy na wycieczkę»"), ko("пример «Ola zapytała mnie, kiedy wyjeżdżam»")]),
 ("R3", "Лицо глагола и местоимения меняются с точки зрения того, кто пересказывает: «Czy spotkałaś się z Robertem?» → zapytał, czy spotkałam się z Robertem; mój → jego / jej.",
  [ko("пункт 7, примеры spotkałaś → spotkałam, posprzątaj → żebym posprzątała"), ak("примеры в таблице"), rs("«Pronouns and time/place words shift to the reporter's viewpoint»")]),
 ("R4", "Вопрос без вопросительного слова вводится czy, и его нельзя пропустить: Bartek spytał mnie, czy napisałem wypracowanie.",
  [ak("пример «Bartek spytał mnie, czy napisałem…»"), ko("пункт 3"), rs("пункт Yes/no questions")]),
 ("R5", "Вопросительное слово сохраняется, порядок слов — как в утверждении: Spytała, gdzie mieszkam.",
  [ak("пример «Marek spytał mnie, kiedy spotkałem się z Anką»"), ko("пункт 2"), rs("пункт Wh-questions: «with statement word order»")]),
 ("R6", "Приказ/просьба → żeby (+ окончание) + форма на -ł: «Posprzątaj pokój» → Matka powiedziała mi, żebym posprzątała pokój. (Подробно — тема 11.)",
  [ak("пример «Matka powiedziała Marcie, żeby pozmywała naczynia»"), ko("пункт 4: «Mama poprosiła mnie, żebym wyniosła śmieci»"), rs("пункт Commands and requests")]),
 ("R7", "Пунктуация: кавычки, двоеточие и тире исчезают; перед że, czy, żeby и вопросительным словом — запятая.",
  [ko("пункт 8"), ak("примеры в таблице"), rs("«A comma always precedes że, czy, żeby, and wh-words»")]),
 ("R8", "Эмоциональные элементы (восклицания, междометия, разговорные словечки) при пересказе опускаются.",
  [ko("пункты 5–6"), ak("о восклицательных знаках и эмоциональных элементах")]),
 ("R9", "Управление глаголов речи: powiedzieć komuś (celownik), zapytać / spytać kogoś (biernik), poprosić kogoś (biernik): powiedział nam, zapytała mnie, poprosiła mnie.",
  [ak("примеры «powiedział nam», «powiedziała Marcie», «spytał mnie»"), ko("примеры «zapytała mnie», «poprosiła mnie»"), S("elon.io — «wołać, prosić, kazać»", EK, "раздел prosić: «prosić kogoś» (accusative)")]),
 ("R10", "Слова времени и места тоже пересчитываются с точки зрения пересказчика (tu → tam, jutro → następnego dnia), если пересказ идёт в другом месте или в другой день.",
  [rs("«Pronouns and time/place words shift … (ciebie → mnie, tu → tam)»")]),
]
extract = {"topic": "mowa-zalezna", "title": "Mowa zależna", "facts": [
    {"id": i, "rule": r, "sources": s} for i, r, s in F]}
extract["facts"][-1]["single_source_note"] = "Сдвиг слов времени/места прямо описан одним источником; дано одной строкой с пометкой и в упражнениях не проверяется."

sections = [
 {"id": "s1", "title": "Что такое mowa zależna", "facts": ["R1"],
  "body": "Mowa niezależna — цитата: *Ewa powiedziała: „Jestem zmęczona”.* Mowa zależna — пересказ: *Ewa powiedziała, że jest zmęczona.* Связка зависит от типа фразы:",
  "table": {"head": ["Исходная фраза", "Связка", "Пересказ"], "rows": [
     ["утверждение: «Jestem zmęczona.»", "że", "Powiedziała, że jest zmęczona."],
     ["вопрос да/нет: «Masz czas?»", "czy", "Zapytała, czy mam czas."],
     ["вопрос со словом: «Gdzie mieszkasz?»", "gdzie, kiedy, co…", "Zapytała, gdzie mieszkam."],
     ["просьба/приказ: «Zadzwoń!»", "żeby + окончание", "Poprosiła, żebym zadzwonił."]]}},
 {"id": "s2", "title": "Время не сдвигается", "facts": ["R2"],
  "body": "В отличие от английского, время остаётся тем же, что в исходной фразе — как и в русском («он сказал, что болеет»).",
  "examples": [["Jan (wczoraj): „Jestem chory.” → Jan powiedział, że jest chory.", "Ян сказал, что болеет."], ["Ola: „Kiedy wyjeżdżasz?” → Ola zapytała mnie, kiedy wyjeżdżam.", "Ола спросила, когда я уезжаю."]],
  "note": "Ошибка по образцу английского: *Jan powiedział, że był chory* (так можно, только если он сказал «Byłem chory»)."},
 {"id": "s3", "title": "Меняются лицо и местоимения", "facts": ["R3", "R10"],
  "body": "Пересказываем со своей точки зрения: кто «я», кто «ты».",
  "table": {"head": ["Сказали", "Пересказ"], "rows": [
     ["Ewa do mnie: „Widziałam cię w kinie.”", "Ewa powiedziała, że widziała mnie w kinie."],
     ["Marek: „Mój brat jest lekarzem.”", "Marek powiedział, że jego brat jest lekarzem."],
     ["Kasjerka do mnie: „Ma pani monetę?”", "Kasjerka zapytała, czy mam monetę."]]},
  "note": "Слова времени и места (jutro, tu) тоже пересчитываются, если пересказ идёт в другой день или в другом месте: tu → tam, jutro → następnego dnia (правило из одного источника)."},
 {"id": "s4", "title": "Вопросы: czy и вопросительные слова", "facts": ["R4", "R5"],
  "body": "Вопрос «да/нет» — всегда с **czy** (его нельзя опустить). Вопрос со словом — это слово остаётся, порядок слов обычный.",
  "examples": [["„Napisałeś wypracowanie?” → Spytał mnie, czy napisałem wypracowanie.", "Спросил, написал ли я сочинение."], ["„Gdzie mieszkasz?” → Spytała, gdzie mieszkam.", "Спросила, где я живу."]]},
 {"id": "s5", "title": "Просьбы и приказы: żeby", "facts": ["R6"],
  "body": "Повелительное наклонение → **żeby + окончание + форма на -ł** (тема 11). В официальной речи — aby.",
  "examples": [["„Posprzątaj pokój!” → Mama powiedziała mi, żebym posprzątała pokój.", "Мама сказала, чтобы я убрала комнату."], ["„Proszę nie palić.” → Lekarz powiedział, żeby nie palił.", "Врач сказал ему не курить."]]},
 {"id": "s6", "title": "Глаголы речи и их падежи", "facts": ["R9"],
  "table": {"head": ["Глагол", "Падеж лица", "Пример"], "rows": [
     ["powiedzieć / mówić", "komu? — celownik", "Powiedział nam, że…"],
     ["zapytać / spytać", "kogo? — biernik", "Zapytała mnie, czy…"],
     ["poprosić / prosić", "kogo? — biernik", "Poprosiła mnie, żebym…"]]},
  "note": "Как в русском: «спросил меня», «попросил меня», но «сказал мне»."},
 {"id": "s7", "title": "Пунктуация и что пропадает", "facts": ["R7", "R8"],
  "body": "Кавычки, двоеточие и тире исчезают; перед связкой — **запятая**. Восклицания и междометия (*Ojej! No wiesz!*) при пересказе опускаются."},
]

exs = []
exs.append(ex("e1", "Какая связка?", "gaps",
  "Впишите że, czy, żeby (с окончанием) или вопросительное слово.", [
  item("Ewa: «Jestem zmęczona.» → Ewa powiedziała, {1} jest zmęczona.", "że"),
  item("Marek do mnie: «Pójdziesz ze mną do kina?» → Marek zapytał mnie, {1} pójdę z nim do kina.", "czy"),
  item("Mama do mnie: «Wynieś śmieci!» → Mama poprosiła mnie, {1} wyniosła śmieci.", "żebym", aby=True),
  item("Turysta: «Gdzie jest dworzec?» → Turysta zapytał, {1} jest dworzec.", "gdzie"),
  item("Szef do nas: «Kiedy skończycie raport?» → Szef zapytał, {1} skończymy raport.", "kiedy"),
  item("Lekarz do pacjenta: «Proszę dużo pić.» → Lekarz powiedział pacjentowi, {1} dużo pił.", "żeby", aby=True),
  item("Ania do mnie: «Masz czas?» → Ania zapytała, {1} mam czas.", "czy"),
  item("Piotr: «Wrócę o szóstej.» → Piotr powiedział, {1} wróci o szóstej.", "że"),
  item("Sąsiad do mnie: «Dlaczego nie odpowiadasz?» → Sąsiad zapytał, {1} nie odpowiadam.", "dlaczego|czemu"),
  item("Nauczycielka do nas: «Otwórzcie okna!» → Nauczycielka powiedziała, {1} otworzyli okna.", "żebyśmy", aby=True),
  item("Kasjerka do mnie: «Ma pani monetę?» → Kasjerka zapytała, {1} mam monetę.", "czy"),
  item("Kolega do mnie: «Co robisz w sobotę?» → Kolega zapytał, {1} robię w sobotę.", "co"),
  item("Babcia: «Ile kosztuje chleb?» → Babcia zapytała, {1} kosztuje chleb.", "ile"),
  item("Ola do Kuby: «Zadzwoń do mnie!» → Ola poprosiła Kubę, {1} do niej zadzwonił.", "żeby", aby=True),
 ], ["R1", "R4", "R5", "R6"]))

exs.append(ex("e2", "Утверждения: że", "gaps",
  "Перескажите: впишите глагол или местоимение в нужной форме (время не меняется!).", [
  item("Anna: «Mieszkam w Gdańsku.» → Anna powiedziała, że {1} w Gdańsku.", "mieszka"),
  item("Marek: «Jestem głodny.» → Marek powiedział, że {1} głodny.", "jest"),
  item("Ty do mnie: «Lubię jazz.» → Powiedziałeś mi, że {1} jazz.", "lubisz"),
  item("Rodzice: «Przyjedziemy w niedzielę.» → Rodzice napisali, że {1} w niedzielę.", "przyjadą"),
  item("Ja do Ewy: «Nie mam czasu.» → Powiedziałem Ewie, że nie {1} czasu.", "mam"),
  item("Ewa do mnie: «Widziałam cię wczoraj w kinie.» → Ewa powiedziała, że {1} mnie wczoraj w kinie.", "widziała"),
  item("Koledzy do nas: «Pomożemy wam.» → Koledzy obiecali, że nam {1}.", "pomogą"),
  item("Szef do mnie: «Pan dostanie podwyżkę.» → Szef powiedział, że {1} podwyżkę.", "dostanę"),
  item("Kasia: «Mój brat pracuje w banku.» → Kasia powiedziała, że {1} brat pracuje w banku.", "jej"),
  item("Ty do mnie: «Byłam chora.» → Powiedziałaś mi, że {1} chora.", "byłaś"),
  item("Pan Nowak: «Moje dzieci chodzą do szkoły.» → Pan Nowak powiedział, że {1} dzieci chodzą do szkoły.", "jego"),
  item("Jan (wczoraj): «Jestem chory.» → Jan powiedział wczoraj, że {1} chory.", "jest"),
 ], ["R2", "R3"]))

exs.append(ex("e3", "Вопросы «да/нет»: czy", "gaps",
  "Перескажите вопрос: напечатайте czy + глагол в нужном лице.", [
  item("Ania do mnie: «Masz samochód?» → Ania zapytała mnie, {1} samochód.", "czy mam"),
  item("Ja do Ani: «Znasz Marka?» → Zapytałem Anię, {1} Marka.", "czy zna"),
  item("Szef do nas: «Skończyliście?» → Szef zapytał nas, {1}.", "czy skończyliśmy|czy skończyłyśmy"),
  item("Kelner do nas: «Zamawiają państwo deser?» → Kelner zapytał, {1} deser.", "czy zamawiamy"),
  item("Mama do mnie: «Zjadłaś obiad?» → Mama zapytała mnie, {1} obiad.", "czy zjadłam"),
  item("Ja do mamy: «Będziesz w domu wieczorem?» → Zapytałam mamę, {1} w domu wieczorem.", "czy będzie"),
  item("Kolega do mnie: «Pójdziesz z nami?» → Kolega zapytał mnie, {1} z nimi.", "czy pójdę"),
  item("Lekarz do pacjentki: «Boli panią głowa?» → Lekarz zapytał pacjentkę, {1} ją głowa.", "czy boli"),
  item("Ewa do Piotra: «Kupiłeś bilety?» → Ewa zapytała Piotra, {1} bilety.", "czy kupił"),
  item("Turyści do mnie: «Mówi pan po angielsku?» → Turyści zapytali mnie, {1} po angielsku.", "czy mówię"),
  item("Ja do was: «Widzieliście ten film?» → Zapytałem was, {1} ten film.", "czy widzieliście|czy widziałyście"),
  item("Babcia do nas: «Przyjedziecie na święta?» → Babcia zapytała nas, {1} na święta.", "czy przyjedziemy"),
 ], ["R4", "R3", "R2"]))

exs.append(ex("e4", "Вопросы с вопросительным словом", "gaps",
  "Перескажите вопрос: напечатайте вопросительное слово + глагол (обычный порядок слов).", [
  item("Turysta do mnie: «Gdzie jest muzeum?» → Turysta zapytał mnie, {1} muzeum.", "gdzie jest"),
  item("Ja do Ewy: «Kiedy wracasz?» → Zapytałem Ewę, {1}.", "kiedy wraca"),
  item("Szef do mnie: «Dlaczego się pan spóźnił?» → Szef zapytał mnie, {1}.", "dlaczego się spóźniłem|czemu się spóźniłem"),
  item("Mama do nas: «Co chcecie na obiad?» → Mama zapytała nas, {1} na obiad.", "co chcemy"),
  item("Kolega do mnie: «Ile płacisz za mieszkanie?» → Kolega zapytał mnie, {1} za mieszkanie.", "ile płacę"),
  item("Ja do kelnera: «Ile kosztuje kawa?» → Zapytałam kelnera, {1} kawa.", "ile kosztuje"),
  item("Urzędniczka do mnie: «Jak się pani nazywa?» → Urzędniczka zapytała mnie, {1}.", "jak się nazywam"),
  item("Dziecko do mamy: «Gdzie jest tata?» → Dziecko zapytało mamę, {1} tata.", "gdzie jest"),
  item("Sąsiadka do nas: «Kiedy się przeprowadzacie?» → Sąsiadka zapytała nas, {1}.", "kiedy się przeprowadzamy"),
  item("Ja do lekarza: «Jak długo mam brać leki?» → Zapytałem lekarza, {1} brać leki.", "jak długo mam"),
 ], ["R5", "R3"]))

exs.append(ex("e5", "Просьбы и приказы: żeby", "gaps",
  "Перескажите: напечатайте żeby (+ окончание) и глагол в форме на -ł.", [
  item("Mama do mnie (я — ж.): «Posprzątaj pokój!» → Mama powiedziała mi, {1} pokój.", "żebym posprzątała", aby=True),
  item("Nauczyciel do uczniów: «Przeczytajcie tekst!» → Nauczyciel powiedział uczniom, {1} tekst.", "żeby przeczytali", aby=True),
  item("Szef do mnie (я — м.): «Proszę zadzwonić do klienta.» → Szef poprosił mnie, {1} do klienta.", "żebym zadzwonił", aby=True),
  item("Ja do ciebie (ты — м.): «Nie spóźnij się!» → Prosiłam cię, {1}.", "żebyś się nie spóźnił", aby=True),
  item("Lekarz do pacjentki: «Proszę nie pić kawy.» → Lekarz powiedział pacjentce, {1} kawy.", "żeby nie piła", aby=True),
  item("Rodzice do nas: «Wróćcie przed północą!» → Rodzice poprosili nas, {1} przed północą.", "żebyśmy wrócili|żebyśmy wróciły", aby=True),
  item("Policjant do kierowcy: «Proszę zwolnić.» → Policjant powiedział kierowcy, {1}.", "żeby zwolnił", aby=True),
  item("Ewa do Marka: «Kup mleko!» → Ewa poprosiła Marka, {1} mleko.", "żeby kupił", aby=True),
  item("Ja do was: «Nie róbcie hałasu!» → Poprosiłem was, {1} hałasu.", "żebyście nie robili|żebyście nie robiły", aby=True),
  item("Babcia do mnie (я — ж.): «Ubierz się ciepło!» → Babcia powiedziała mi, {1} ciepło.", "żebym się ubrała|żebym ubrała się", aby=True),
  item("Trener do zawodników: «Biegajcie codziennie!» → Trener powiedział zawodnikom, {1} codziennie.", "żeby biegali", aby=True),
  item("Koleżanka do mnie (я — м.): «Pomóż mi z przeprowadzką!» → Koleżanka poprosiła mnie, {1} z przeprowadzką.", "żebym jej pomógł|żebym pomógł jej", aby=True),
 ], ["R6", "R3"]))

exs.append(ex("e6", "Местоимения и падежи", "gaps",
  "Впишите местоимение/слово в нужной форме.", [
  item("Ewa zapytała {1} (ja), czy mam czas.", "mnie"),
  item("Szef powiedział {1} (my), że jutro nie pracujemy.", "nam"),
  item("Zapytałem {1} (ona), czy przyjdzie.", "ją"),
  item("Powiedz {1} (on), że czekam.", "mu|jemu"),
  item("Anna: «Mój pies jest chory.» → Anna powiedziała, że {1} pies jest chory.", "jej"),
  item("Marek do mnie: «Twój samochód stoi na moim miejscu.» → Marek powiedział, że {1} samochód stoi na {2} miejscu.", "mój", "jego"),
  item("Ja do Ewy: «Czy mogę wziąć twój rower?» → Zapytałem Ewę, czy mogę wziąć {1} rower.", "jej"),
  item("Mama zapytała {1} (wy), co chcecie na obiad.", "was"),
  item("Zapytaliśmy {1} (pani Nowak), gdzie mieszka.", "panią Nowak"),
  item("Napisz {1} (rodzice), że wszystko w porządku.", "rodzicom"),
  item("Poprosiłam {1} (sąsiad), żeby podlał kwiaty.", "sąsiada"),
 ], ["R9", "R3"]))

exs.append(ex("e7", "Тест в формате экзамена: записка", "gaps",
  "Odebrałaś telefon do współlokatorki Kasi. Uzupełnij wiadomość dla niej: wpisz że / czy / żeby (z końcówką) / zaimek pytający i czasownik w odpowiedniej formie. W nawiasie — co powiedziała pani Kowalska z biura podróży.", [
  item("(«Bilety pani Kasi są już gotowe.») Kasiu, dzwoniła pani Kowalska. Powiedziała, {1} Twoje bilety do Rzymu {2} już gotowe.", "że", "są"),
  item("(«Czy może pani odebrać je w piątek?») Zapytała, {1} {2} je odebrać w piątek.", "czy", "możesz"),
  item("(«Proszę do mnie zadzwonić przed południem.») Prosiła, {1} do niej {2} przed południem.", "żebyś|abyś", "zadzwoniła"),
  item("(«Kiedy pani wraca z Rzymu?») Zapytała też, {1} {2} z Rzymu.", "kiedy", "wracasz"),
  item("(«Hotel ma bardzo dobre opinie.») Powiedziała, {1} hotel {2} bardzo dobre opinie.", "że", "ma"),
  item("(«Niech pani nie zapomni paszportu!») Prosiła, {1} nie {2} paszportu.", "żebyś|abyś", "zapomniała"),
  item("(«Będę w biurze do osiemnastej.») Dodała, {1} {2} w biurze do osiemnastej.", "że", "będzie"),
  item("(«Czy chce pani ubezpieczenie?») Zapytała jeszcze, {1} {2} ubezpieczenie. Ola", "czy", "chcesz"),
 ], ["R1", "R2", "R3", "R4", "R5", "R6"], fmt="exam-text"))

exs.append(ex("e8", "Przekształcenia", "gaps",
  "Перескажите фразу, начиная с данного начала. Напечатайте продолжение.", [
  item("Marek: «Jutro jadę do Krakowa.» → Marek powiedział, {1}.", "że jutro jedzie do Krakowa|że jedzie jutro do Krakowa"),
  item("Ewa do mnie: «Czy lubisz pływać?» → Ewa zapytała mnie, {1}.", "czy lubię pływać"),
  item("Szef do nas: «Przyjdźcie jutro o ósmej!» → Szef powiedział nam, {1}.", "żebyśmy przyszli jutro o ósmej|żebyśmy jutro przyszli o ósmej", aby=True),
  item("Turystka do mnie: «Gdzie mogę kupić bilet?» → Turystka zapytała mnie, {1}.", "gdzie może kupić bilet"),
  item("Mama do mnie (я — ж.): «Nie wracaj późno!» → Mama poprosiła mnie, {1}.", "żebym nie wracała późno", aby=True),
  item("Anna do Piotra: «Kiedy się spotkamy?» → Anna zapytała Piotra, {1}.", "kiedy się spotkają"),
  item("Kolega do mnie: «Pożyczysz mi samochód?» → Kolega zapytał mnie, {1}.", "czy pożyczę mu samochód|czy mu pożyczę samochód"),
  item("Lekarz: «Pacjent musi zostać w szpitalu.» → Lekarz powiedział, {1}.", "że pacjent musi zostać w szpitalu"),
 ], ["R1", "R2", "R3", "R4", "R5", "R6"], fmt="rewrite"))

exs.append({"id": "w1", "kind": "writing", "title": "Пересказ разговора (письмо другу)", "facts": ["R1", "R2", "R3"],
  "instr": "Napisz e-mail do przyjaciela (80–100 słów). Wczoraj rozmawiałeś/rozmawiałaś z nowym sąsiadem. Opowiedz: co sąsiad powiedział o sobie, o co Cię zapytał, o co Cię poprosił i co mu odpowiedziałeś/odpowiedziałaś.",
  "checklist": ["не меньше 2 утверждений с że", "1 вопрос с czy и 1 — с вопросительным словом", "1 просьба с żeby", "время в пересказе не сдвинуто", "без кавычек"]})
exs.append({"id": "w2", "kind": "writing", "title": "Сообщение коллеге о звонке клиента", "facts": ["R1", "R6", "R9"],
  "instr": "Napisz wiadomość do kolegi z pracy (50–70 słów). Dzwonił do niego klient, pan Nowak. Przekaż: kim jest i co powiedział, o co pytał, o co prosił, kiedy można do niego oddzwonić.",
  "checklist": ["Dzwonił pan Nowak. Powiedział, że…", "Pytał, czy / kiedy…", "Prosił, żebyś…", "правильные падежи: powiedział mi, pytał mnie"]})

topic = {"id": "mowa-zalezna", "num": 13, "title": "Mowa zależna: косвенная речь", "level": "B1",
  "lang": "ru", "prev": "strona-bierna", "next": "stopniowanie",
  "summary": "Как пересказать чужие слова: że, czy, вопросительные слова, żeby; время не сдвигается; меняются лицо и местоимения; падежи после powiedzieć / zapytać / poprosić.",
  "sections": sections, "exercises": exs}
save("mowa-zalezna", extract, topic)
