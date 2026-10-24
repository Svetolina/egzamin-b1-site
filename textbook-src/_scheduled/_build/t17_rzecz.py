import sys; sys.path.insert(0, '/home/claude/build')
from lib import S, item, ex, save

DF = "https://faculty.washington.edu/dziwirek/grammar/miscellaneous/polish-verbal-nouns-format.pdf"
DU = "https://faculty.washington.edu/dziwirek/grammar/miscellaneous/polish-verbalnounsdecluse.pdf"
EG = "https://elon.io/grammar/polish/nouns/types/verbal-nouns-gerunds"
EN = "https://elon.io/grammar/polish/complex/nominalization"
TR = "https://blogs.transparent.com/polish/?p=1652"

df = lambda l: S("K. Dziwirek (University of Washington), «Verbal nouns: formation»", DF, l)
du = lambda l: S("K. Dziwirek (University of Washington), «Verbal nouns: declension and use»", DU, l)
eg = lambda l: S("elon.io — «Verbal Nouns (-anie, -enie, -cie)»", EG, l)
en = lambda l: S("elon.io — «Nominalization and Verbal-Noun Constructions»", EN, l)
tr = lambda l: S("Transparent Language Polish Blog — «Verbal nouns»", TR, l)

F = [
 ("R1", "Rzeczownik odczasownikowy называет действие (czytanie — чтение) и оканчивается на -nie / -enie / -cie; он среднего рода и склоняется как существительные на -e: czytanie, czytania, czytaniu, czytaniem.",
  [df("определение"), du("таблица склонения"), eg("раздел Neuter declension"), tr("«decline like neuter nouns»")]),
 ("R2", "Глаголы на -ać: -ć → -nie: czytać → czytanie, pytać → pytanie, czekać → czekanie, oglądać → oglądanie, pracować → pracowanie.",
  [df("п. 1"), eg("раздел Formation: «-ać → -anie»")]),
 ("R3", "Глаголы на -ić, -yć, -eć II спряжения: основа 1-го л. ед. ч. + -enie (с тем же чередованием): robię → robienie, myślę → myślenie, siedzę → siedzenie, noszę → noszenie.",
  [df("п. 2"), eg("раздел Formation: nosić → noszenie")]),
 ("R4", "Короткие основы на -ić, -yć, -uć: -ć → -cie: pić → picie, myć → mycie, żyć → życie, czuć → czucie.",
  [df("п. 3"), eg("раздел Formation: pić → picie")]),
 ("R5", "się сохраняется: uczyć się → uczenie się, nudzić się → nudzenie się.",
  [df("п. 2: uczenie się, nudzenie się, dziwienie się")]),
 ("R6", "Вид глагола сохраняется: czytanie (процесс) — przeczytanie (результат), robienie — zrobienie, kończenie — zakończenie.",
  [eg("раздел Aspect pairs"), tr("czytanie vs przeczytanie"), en("kończenie / zakończenie")]),
 ("R7", "Прямое дополнение после отглагольного существительного — в dopełniaczu: czytać książkę → czytanie książki; mówienie prawdy, ukończenie szkoły. Ошибка: *czytanie książkę*.",
  [eg("раздел Object in the genitive, Common mistakes"), en("«czytanie książek … not the accusative»"), du("п. b: pisanie książki, mówienie prawdy")]),
 ("R8", "do + dopełniacz — «для того, чтобы…» / назначение: Nie mam nic do powiedzenia. Co jest do jedzenia? proszek do prania, maszyna do pisania.",
  [du("п. a"), tr("«do + Gen»: Nie mam nic do powiedzenia")]),
 ("R9", "С предлогами вместо придаточного: po + miejscownik (обычно сов. вид) — «после»: po przeczytaniu listu; podczas + dopełniacz (несов.) — «во время»: podczas czytania; bez + dopełniacz; w celu + dopełniacz (офиц.): w celu omówienia budżetu.",
  [eg("раздел Uses: po + Ms., podczas + D."), en("po, w celu, bez + verbal noun"), du("пример «Pływanie po jedzeniu jest niezdrowe»")]),
 ("R10", "Многие стали обычными существительными: mieszkanie (квартира), pytanie (вопрос), jedzenie (еда), picie (питьё), życie (жизнь), uczucie (чувство), otwarcie / zamknięcie (открытие / закрытие).",
  [du("п. d"), eg("раздел Lexicalized meanings")]),
 ("R11", "После lubić естественнее инфинитив: Lubię gotować (Lubię gotowanie звучит книжно, но встречается: Lubię czytanie).",
  [eg("Common mistakes: «Lubię gotowanie sounds stilted»"), du("пример «Lubię czytanie»")]),
 ("R12", "Отглагольные существительные типичны для официального стиля; злоупотреблять ими в своих текстах не стоит — получается канцелярит.",
  [en("раздел Caution")]),
]
extract = {"topic": "rzeczowniki-odczasownikowe", "title": "Rzeczowniki odczasownikowe", "facts": [
    {"id": i, "rule": r, "sources": s} for i, r, s in F]}
for f in extract["facts"]:
    if len(f["sources"]) < 2:
        f["single_source_note"] = "Подтверждено одним источником — дано одной строкой с пометкой."

sections = [
 {"id": "s1", "title": "Что это такое", "facts": ["R1", "R12"],
  "body": "Rzeczownik odczasownikowy — существительное-действие, как русское «чтение», «плавание». Оканчивается на **-nie / -enie / -cie**, всегда **среднего рода**.",
  "examples": [["Czytanie przed snem pomaga mi się zrelaksować.", "Чтение перед сном помогает мне расслабиться."], ["Takie myślenie jest błędne.", "Такое мышление ошибочно."]],
  "note": "Типично для официальных текстов (правила, объявления). В своей речи — в меру."},
 {"id": "s2", "title": "Как образовать", "facts": ["R2", "R3", "R4", "R5"],
  "table": {"head": ["Глагол", "Как", "Примеры"], "rows": [
     ["-ać (-ować)", "-ć → -nie", "czytać → czytanie, pracować → pracowanie, spać → spanie"],
     ["-ić / -yć / -eć (II спр.)", "основа «ja» + -enie", "robię → robienie, myślę → myślenie, noszę → noszenie"],
     ["короткие -ić / -yć / -uć", "-ć → -cie", "pić → picie, myć → mycie, żyć → życie, czuć → czucie"]]},
  "note": "się остаётся: uczenie się, nudzenie się (одним источником)."},
 {"id": "s3", "title": "Склонение", "facts": ["R1"],
  "table": {"head": ["Падеж", "Окончание", "Пример"], "rows": [
     ["M. / B.", "-nie / -cie", "Lubię czytanie."], ["D.", "-nia / -cia", "Nie ma nic do jedzenia."],
     ["C. / Ms.", "-niu / -ciu", "po jedzeniu"], ["N.", "-niem / -ciem", "Interesuję się czytaniem."]]}},
 {"id": "s4", "title": "Вид сохраняется", "facts": ["R6"],
  "body": "**czytanie** — процесс, **przeczytanie** — результат. После *po* обычно совершенный вид, после *podczas* — несовершенный.",
  "table": {"head": ["Несов. (процесс)", "Сов. (результат)"], "rows": [["czytanie", "przeczytanie"], ["robienie", "zrobienie"], ["kończenie", "zakończenie / skończenie"]]}},
 {"id": "s5", "title": "Дополнение — в dopełniaczu", "facts": ["R7"],
  "body": "*czytać książkę* → *czytanie **książki***; *myć samochód* → *mycie **samochodu***. Как в русском: «читать книгу» → «чтение книги».",
  "note": "Ошибка: *czytanie książkę*."},
 {"id": "s6", "title": "С предлогами", "facts": ["R8", "R9"],
  "table": {"head": ["Конструкция", "Значение", "Пример"], "rows": [
     ["do + D.", "для, чтобы", "Nie mam nic do powiedzenia. maszyna do pisania"],
     ["po + Ms.", "после", "Po przeczytaniu listu zadzwoniła do brata."],
     ["podczas + D.", "во время", "Podczas czytania nie słucham muzyki."],
     ["bez + D.", "без", "Bez zrozumienia kontekstu trudno ocenić decyzję."],
     ["w celu + D.", "с целью (офиц.)", "Zebranie zwołano w celu omówienia budżetu."]]}},
 {"id": "s7", "title": "Ставшие обычными словами", "facts": ["R10", "R11"],
  "body": "*mieszkanie* — квартира, *pytanie* — вопрос, *jedzenie* — еда, *picie* — питьё, *życie* — жизнь, *uczucie* — чувство, *otwarcie wystawy* — открытие выставки, *godzina zamknięcia* — время закрытия.\n\nПосле *lubić* лучше инфинитив: *Lubię gotować* (форма *Lubię czytanie* тоже встречается)."},
]

exs = []
vn = [("czytać", "czytanie"), ("pisać", "pisanie"), ("pływać", "pływanie"), ("gotować", "gotowanie"), ("czekać", "czekanie"),
      ("oglądać", "oglądanie"), ("spać", "spanie"), ("robić", "robienie"), ("mówić", "mówienie"), ("nosić", "noszenie"),
      ("myśleć", "myślenie"), ("siedzieć", "siedzenie"), ("uczyć się", "uczenie się"), ("palić", "palenie"), ("płacić", "płacenie"),
      ("pić", "picie"), ("myć", "mycie"), ("żyć", "życie"), ("przeczytać", "przeczytanie"), ("zrobić", "zrobienie"), ("napisać", "napisanie")]
exs.append(ex("e1", "Образуйте существительное", "gaps", "Напечатайте rzeczownik odczasownikowy.",
  [item(f"{a} → {{1}}", b) for a, b in vn], ["R2", "R3", "R4", "R5", "R6"]))

exs.append(ex("e2", "Дополнение в dopełniaczu", "gaps", "Поставьте дополнение в нужную форму.", [
  item("czytać książki → czytanie {1}", "książek"), item("myć samochód → mycie {1}", "samochodu"),
  item("pisać list → pisanie {1}", "listu"), item("mówić prawdę → mówienie {1}", "prawdy"),
  item("oglądać telewizję → oglądanie {1}", "telewizji"), item("gotować obiad → gotowanie {1}", "obiadu"),
  item("kupić mieszkanie → kupienie {1}", "mieszkania"), item("palić papierosy → palenie {1}", "papierosów"),
  item("ukończyć szkołę → ukończenie {1}", "szkoły"), item("organizować konferencję → organizowanie {1}", "konferencji"),
  item("pić kawę → picie {1}", "kawy"), item("zrobić zakupy → zrobienie {1}", "zakupów"),
 ], ["R7"]))

exs.append(ex("e3", "Нужный падеж", "gaps", "Поставьте отглагольное существительное в нужный падеж.", [
  item("Myj ręce przed {1} (jedzenie).", "jedzeniem"),
  item("Po {1} (przeczytanie) listu zadzwoniła do brata.", "przeczytaniu"),
  item("Nie mam nic do {1} (powiedzenie).", "powiedzenia"),
  item("Podczas {1} (jedzenie) nie rozmawiamy przez telefon.", "jedzenia"),
  item("Interesuję się {1} (czytanie).", "czytaniem"),
  item("Pływanie po {1} (jedzenie) jest niezdrowe.", "jedzeniu"),
  item("Bez {1} (zrozumienie) kontekstu trudno ocenić tę decyzję.", "zrozumienia"),
  item("Kupiłam proszek do {1} (pranie).", "prania"),
  item("To jest stara maszyna do {1} (pisanie).", "pisania"),
  item("Zebranie zwołano w celu {1} (omówienie) budżetu.", "omówienia"),
  item("Zajmuję się {1} (gotowanie).", "gotowaniem"),
  item("Polecisz mi coś do {1} (czytanie)?", "czytania"),
 ], ["R1", "R8", "R9"]))

exs.append(ex("e4", "Процесс или результат?", "gaps", "Выберите и напечатайте подходящую форму (несов. или сов. вид) в нужном падеже.", [
  item("Po {1} (czytanie / przeczytanie) książki obejrzałam film.", "przeczytaniu"),
  item("{1} (czytanie / przeczytanie) przed snem pomaga mi się zrelaksować.", "Czytanie"),
  item("Podczas {1} (pisanie / napisanie) listu zadzwonił telefon.", "pisania"),
  item("Po {1} (kończenie / skończenie) pracy idę na siłownię.", "skończeniu"),
  item("{1} (robienie / zrobienie) zakupów zajmuje mi godzinę.", "Robienie"),
  item("Gratuluję {1} (kończenie / ukończenie) studiów!", "ukończenia"),
  item("Po {1} (jedzenie / zjedzenie) obiadu wyszli na spacer.", "zjedzeniu"),
  item("{1} (pływanie / przepłynięcie) jest dobre dla zdrowia.", "Pływanie"),
 ], ["R6", "R9"]))

exs.append(ex("e5", "Замените придаточное", "gaps", "Замените придаточное или инфинитив существительным. Напечатайте пропущенное слово.", [
  item("Kiedy przeczytała list, zadzwoniła do brata. → Po {1} listu zadzwoniła do brata.", "przeczytaniu"),
  item("Kiedy jem, nie oglądam telewizji. → Podczas {1} nie oglądam telewizji.", "jedzenia"),
  item("Nie mam nic, co mógłbym powiedzieć. → Nie mam nic do {1}.", "powiedzenia"),
  item("Gdy skończył szkołę, wyjechał za granicę. → Po {1} szkoły wyjechał za granicę.", "skończeniu|ukończeniu"),
  item("Myj ręce, zanim zjesz. → Myj ręce przed {1}.", "jedzeniem"),
  item("Trudno jest pisać po polsku. → {1} po polsku jest trudne.", "Pisanie"),
  item("Spotkaliśmy się, żeby omówić budżet. → Spotkaliśmy się w celu {1} budżetu.", "omówienia"),
  item("Nie zrozumiesz tego, jeśli nie znasz kontekstu. → Bez {1} kontekstu tego nie zrozumiesz.", "znajomości|zrozumienia"),
 ], ["R7", "R8", "R9"]))

exs.append(ex("e6", "Обычные существительные", "gaps", "Напечатайте существительное по определению.", [
  item("Miejsce, w którym mieszkasz: {1}", "mieszkanie"),
  item("To, o co pytasz: {1}", "pytanie"),
  item("To, co jesz: {1}", "jedzenie"),
  item("To, co pijesz: {1}", "picie"),
  item("Czas od urodzenia do śmierci: {1}", "życie"),
  item("Miłość to piękne {1}.", "uczucie"),
  item("Uroczystość na początku wystawy: {1} wystawy", "otwarcie"),
  item("Godzina, od której sklep jest nieczynny: godzina {1}", "zamknięcia"),
 ], ["R10"]))

exs.append(ex("e7", "Тест в формате экзамена: правила бассейна", "gaps",
  "Uzupełnij regulamin. Wpisz rzeczownik odczasownikowy od czasownika w nawiasie w odpowiedniej formie.", [
  item("REGULAMIN BASENU. 1. {1} (wchodzić) do wody bez czepka jest zabronione.", "Wchodzenie"),
  item("2. Przed {1} (pływać) należy wziąć prysznic.", "pływaniem"),
  item("3. {1} (jeść)", "Jedzenie"),
  item("i {1} (pić) na terenie basenu jest zabronione.", "picie"),
  item("4. Po {1} (skończyć) zajęć należy opuścić halę basenu.", "skończeniu"),
  item("5. Podczas {1} (pływać) prosimy nie korzystać z telefonów.", "pływania"),
  item("6. Rzeczy do {1} (przechować) można zostawić w szafce.", "przechowania"),
  item("7. {1} (palić) papierosów jest zabronione.", "Palenie"),
  item("8. Za {1} (zgubić) kluczyka do szafki płaci się 20 zł.", "zgubienie"),
  item("9. W celu {1} (zarezerwować) toru prosimy dzwonić do recepcji.", "zarezerwowania"),
  item("10. Bez {1} (pokazać) biletu nie można wejść na basen.", "pokazania"),
  item("Dziękujemy za {1} (przestrzegać) regulaminu!", "przestrzeganie"),
 ], ["R1", "R2", "R3", "R4", "R7", "R8", "R9"], fmt="exam-text"))

exs.append(ex("e8", "Przekształcenia", "gaps", "Перестройте, используя отглагольное существительное. Напечатайте вставку.", [
  item("Po tym, jak zjedliśmy kolację, poszliśmy na spacer. → Po {1} poszliśmy na spacer.", "zjedzeniu kolacji|skończeniu kolacji"),
  item("Kiedy czekam na autobus, słucham muzyki. → Podczas {1} słucham muzyki.", "czekania na autobus"),
  item("Nie wolno tu palić. → {1} jest tu zabronione.", "Palenie"),
  item("Lubię gotować. → Moje hobby to {1}.", "gotowanie"),
  item("Zanim pójdziesz spać, wyłącz komputer. → Przed {1} wyłącz komputer.", "spaniem|snem"),
  item("Zebraliśmy się, żeby omówić plan. → Zebraliśmy się w celu {1}.", "omówienia planu"),
  item("Nie wiem, co powiedzieć. → Nie mam nic do {1}.", "powiedzenia"),
  item("Przyjemnie jest uczyć się języków. → {1} jest przyjemne.", "Uczenie się języków"),
 ], ["R6", "R7", "R8", "R9"], fmt="rewrite"))

exs.append({"id": "w1", "kind": "writing", "title": "Правила общежития", "facts": ["R1", "R7", "R9", "R12"],
  "instr": "Napisz regulamin akademika lub hostelu (8–10 punktów, 60–80 słów): co jest zabronione, co trzeba zrobić przed wyjazdem, w jakich godzinach jest cisza nocna.",
  "checklist": ["не меньше 6 отглагольных существительных", "дополнения в dopełniaczu (palenie papierosów)", "po / przed / podczas / w celu — хотя бы 3 разных", "официальный стиль"]})
exs.append({"id": "w2", "kind": "writing", "title": "Мои увлечения", "facts": ["R1", "R10", "R11"],
  "instr": "Napisz tekst o swoich zainteresowaniach (80–100 słów): czym się interesujesz, co robisz w wolnym czasie, czego nie lubisz robić.",
  "checklist": ["interesuję się …-niem (творительный)", "moje hobby to …", "2 формы с po / podczas", "хотя бы 1 lubię + инфинитив"]})

topic = {"id": "rzeczowniki-odczasownikowe", "num": 17, "title": "Rzeczowniki odczasownikowe: czytanie, picie", "level": "B1",
  "lang": "ru", "prev": "imieslowy-przyslowkowe", "next": "zaimki-nieokreslone",
  "summary": "Существительные-действия на -nie/-enie/-cie: образование, склонение, вид, дополнение в dopełniaczu, предлоги po/podczas/do/bez/w celu и официальный стиль.",
  "sections": sections, "exercises": exs}
save("rzeczowniki-odczasownikowe", extract, topic)
