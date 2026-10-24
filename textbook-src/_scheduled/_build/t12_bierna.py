import sys; sys.path.insert(0, '/home/claude/build')
from lib import S, item, ex, save

EP = "https://elon.io/grammar/polish/verbs/voice/passive-byc-zostac"
EPP = "https://elon.io/grammar/polish/verbs/participles/passive-participle"
EC = "https://elon.io/grammar/polish/complex/se-passive-vs-no-to-vs-zostac"
ZS = "https://zpe.gov.pl/a/strona-czynna-i-bierna/Dbi8lrKg0"
ZR = "https://zpe.gov.pl/watek/LPCgxyBw7p/255/a/rodzaje-imieslowow-imieslow-przymiotnikowy/DgfX2F5qy"
ZI = "https://zpe.gov.pl/a/imieslowy-i-ich-rodzaje/DN28lvu36"
PD = "https://polskidaily.eu/wp-content/uploads/2025/06/Klub-Gramatyczny-Strona-bierna-2.pdf"
GJ = "https://grzegorj.smallhost.pl/gram/en/gram07.html"
WIKI = "https://en.wikipedia.org/wiki/Polish_grammar"

ep = lambda l: S("elon.io — «The Passive Voice: być and zostać + Participle»", EP, l)
epp = lambda l: S("elon.io — «The Passive Participle (-ny / -ty)»", EPP, l)
ec = lambda l: S("elon.io — «The Full Impersonal/Passive System Compared»", EC, l)
zs = lambda l: S("ZPE (MEN) — «Strona czynna i bierna»", ZS, l)
zr = lambda l: S("ZPE (MEN) — «Rodzaje imiesłowów. Imiesłów przymiotnikowy»", ZR, l)
zi = lambda l: S("ZPE (MEN) — «Imiesłowy i ich rodzaje»", ZI, l)
pd = lambda l: S("Polski Daily — «Klub Gramatyczny: Strona bierna 2» (PDF, 2025)", PD, l)
gj = lambda l: S("G. Jagodziński, «A Grammar of the Polish Language», ч. 7 (Conjugation 2)", GJ, l)
wiki = lambda l: S("Wikipedia (en) — «Polish grammar»", WIKI, l)

F = [
 ("R1", "Strona bierna: подлежащее — тот, над кем совершается действие. Образуется: być / zostać + imiesłów przymiotnikowy bierny. Wiersz został napisany przez poetę.",
  [zs("разделы «Strona czynna / bierna», «Budowa»"), pd("раздел «Czym jest strona bierna?»: «Ten pałac został zbudowany przez króla…»"), ep("вводная часть")]),
 ("R2", "Пассив образуют только переходные глаголы (czasowniki przechodnie); подлежащим становится прямое дополнение в bierniku. От myśleć o czymś пассива нет.",
  [zs("разделы «Przekształcanie» и «Które czasowniki»"), gj("passive voice: «created almost exclusively by transitive verbs»"), zi("«tylko od czasowników przechodnich»")]),
 ("R3", "Imiesłów bierny оканчивается на -ny или -ty и склоняется как прилагательное; образуется и от несовершенных (robiony), и от совершенных (zrobiony) глаголов.",
  [zi("раздел о imiesłów przymiotnikowy bierny: «-ny lub -ty», odmiana jak ładny / bogaty"), zr("таблица склонения namalowany; пример robiony / zrobiony"), wiki("раздел Participles: «passive participle … in -ny or -ty (conjugated as an adjective)»")]),
 ("R4", "Глаголы на -ać → -any, на -ować → -owany: napisać → napisany, zaprojektować → zaprojektowany.",
  [epp("раздел -any (-ać) и -owany"), pd("пример zaprojektować → zaprojektowany"), zi("примеры napisany, karany")]),
 ("R5", "Глаголы на -ić, -yć, -eć → -ony, часто с чередованием: zrobić → zrobiony, kupić → kupiony, zaprosić → zaproszony, (za)płacić → (za)płacony, skończyć → skończony.",
  [epp("раздел -ony: zrobiony, kupiony, zobaczony, zaproszony, płacony; чередования ś→sz, ć→c"), pd("пример skończyć → skończony"), zr("пример robiony / zrobiony")]),
 ("R6", "-ty: глаголы на -nąć/-ąć (ą → ę: zamknąć → zamknięty, zacząć → zaczęty, wziąć → wzięty) и ряд коротких основ (umyć → umyty, użyć → użyty, zepsuć → zepsuty); otworzyć → otwarty — особая форма.",
  [epp("раздел -ty"), pd("пример użyć → użyty"), gj("пример on jest myty")]),
 ("R7", "Причастие согласуется с подлежащим в роде и числе. Мужско-личное мн. ч.: -ny → -ni, -ony → -eni, -ty → -ci: wybrani, zaproszeni, aresztowani, myci; для остальных — -ne/-te: zamknięte, wybrane.",
  [ep("раздел Agreement: studenci zostali wybrani"), epp("раздел Masculine-personal plural: aresztowani / aresztowane, zaproszeni"), zr("таблица: rodzaj męskoosobowy — namalowani"), gj("пример oni są myci")]),
 ("R8", "zostać + причастие (обычно сов. вида) — событие, которое произошло (можно указать дату): Most został zbudowany w 1990 roku. być + причастие — состояние, результат: Sklep jest zamknięty w niedziele. Ошибка: *Prezydent był wybrany w niedzielę* → został wybrany.",
  [ep("разделы «być vs zostać», «Common mistakes»"), zs("раздел «Budowa»: być — stan, zostać — czynność dokonana"), gj("passive: perfective verbs form past and future passives with zostać; resultative forms with być")]),
 ("R9", "być + причастие несовершенного вида — процесс: Muzeum jest/było budowane (строится / строилось). Testy są sprawdzane.",
  [gj("imperfective verbs: być + participle — on jest myty, ona jest myta"), pd("примеры był budowany, jest monitorowany, są śpiewane")]),
 ("R10", "Будущее: zostanie / zostaną + причастие сов. вида (у zostać нет настоящего, его формы значат будущее): Wystawa zostanie otwarta. Встречается и będzie + причастие (будущее состояние/процесс): będzie odwiedzane.",
  [ep("раздел Tenses: «zostać has no present tense … present-shaped forms carry future meaning»"), gj("resultative forms byłem / jestem / będę umyty; future passive with zostać")]),
 ("R11", "Исполнитель действия — przez + biernik, не творительный падеж, как в русском («написано Пушкиным»): Wiersz został napisany przez Szymborską. List został wysłany przez sekretarkę.",
  [ep("раздел Agent: «przez + accusative, not the instrumental»"), zs("раздел «Przekształcanie»: podmiot → przez + biernik, «przez poetę»"), gj("пример Jan jest bity przez Pawła")]),
 ("R12", "Пассив — скорее письменный стиль (новости, история, официальные тексты); в разговоре чаще действительный залог или конструкции с się и -no/-to.",
  [gj("«characteristic for the written language rather»"), ep("раздел «Polish alternatives»")]),
 ("R13", "Безличная форма на -no/-to (zbudowano, otwarto, zamknięto): без подлежащего и без исполнителя (przez нельзя), прямое дополнение остаётся в bierniku: Otwarto wystawę. Это не причастие.",
  [ec("раздел -no/-to impersonal past: «keeps the object in the accusative», przez — ungrammatical"), wiki("раздел Verbs: «subjectless past tense … with the ending -o (e.g. śpiewano)»"), zr("примечание: формы na -no, -to (zamknięto, zbudowano) — nieosobowe, не imiesłowy")]),
 ("R14", "Конструкция с się (3 л. ед. ч.) — общее, безличное действие: W Polsce dużo się czyta. Tutaj sprzedaje się świeży chleb.",
  [ec("раздел się-construction"), wiki("раздел Impersonal sentences: «się but no subject, the verb being third-person singular»"), ep("пример Sprzedaje się mieszkanie")]),
]
extract = {"topic": "strona-bierna", "title": "Strona bierna", "facts": [
    {"id": i, "rule": r, "sources": s} for i, r, s in F]}

sections = [
 {"id": "s1", "title": "Что такое strona bierna", "facts": ["R1", "R2", "R12"],
  "body": "В действительном залоге подлежащее делает действие: *Poeta napisał wiersz.* В страдательном (strona bierna) подлежащее — то, над чем действие совершается: *Wiersz został napisany przez poetę.*\n\nФормула: **być / zostać + imiesłów bierny**. Работает только с переходными глаголами (у которых есть дополнение в bierniku). Пассив — в основном письменный стиль: новости, история, официальные тексты.",
  "examples": [["Ten pałac został zbudowany przez króla.", "Этот дворец был построен королём."]]},
 {"id": "s2", "title": "Как образовать причастие", "facts": ["R3", "R4", "R5", "R6"],
  "body": "Причастие оканчивается на **-ny** или **-ty** и склоняется как прилагательное.",
  "table": {"head": ["Инфинитив", "Суффикс", "Примеры"], "rows": [
     ["-ać, -ować", "-any, -owany", "napisać → napisany, zbudować → zbudowany"],
     ["-ić, -yć, -eć", "-ony (+ чередование)", "zrobić → zrobiony, kupić → kupiony, zaprosić → zaproszony, zapłacić → zapłacony, skończyć → skończony"],
     ["-nąć, -ąć", "-ęty", "zamknąć → zamknięty, zacząć → zaczęty, wziąć → wzięty"],
     ["короткие основы", "-ty", "umyć → umyty, użyć → użyty, zepsuć → zepsuty"],
     ["особая форма", "", "otworzyć → otwarty"]]},
  "note": "Надёжнее всего ориентироваться на основу настоящего/будущего времени: zaproszę → zaproszony."},
 {"id": "s3", "title": "Согласование и мужско-личная форма", "facts": ["R7"],
  "body": "И глагол (został/została…), и причастие согласуются с подлежащим.",
  "table": {"head": ["Подлежащее", "Пример"], "rows": [
     ["он (м.)", "list został napisany"], ["она (ж.)", "książka została napisana"], ["оно (ср.)", "zadanie zostało napisane"],
     ["мужчины / смешанная группа", "studenci zostali wybrani / zaproszeni / umyci"], ["остальные мн. ч.", "listy zostały napisane, drzwi są zamknięte"]]},
  "note": "Мужско-личное мн. ч.: -ny → -ni (wybrani), -ony → -eni (zaproszeni), -ty → -ci (umyci)."},
 {"id": "s4", "title": "być или zostać?", "facts": ["R8", "R9"],
  "body": "Вопрос-проверка: **был ли момент, когда это случилось?** Да (можно добавить дату) → **zostać**. Описываем, как обстоят дела сейчас → **być**.\n\n**być** + причастие несовершенного вида — процесс: *Muzeum było budowane przez trzy lata.*",
  "table": {"head": ["zostać — событие", "być — состояние / процесс"], "rows": [
     ["Drzwi zostały zamknięte o ósmej.", "Drzwi są zamknięte."], ["Most został zbudowany w 1990 roku.", "Ten dom jest zbudowany z drewna."], ["Prezydent został wybrany w niedzielę.", "Testy są sprawdzane przez komisję."]]},
  "note": "Ошибка: *Prezydent był wybrany w niedzielę* — правильно został wybrany."},
 {"id": "s5", "title": "Времена", "facts": ["R8", "R9", "R10"],
  "table": {"head": ["Время", "być", "zostać"], "rows": [
     ["настоящее", "jest zamknięty / jest budowany", "— (нет)"],
     ["прошедшее", "był zamknięty / był budowany", "został zamknięty"],
     ["будущее", "będzie zamknięty / będzie odwiedzany", "zostanie zamknięty"]]},
  "body": "У zostać нет настоящего времени: *zostanie* — это будущее («будет закрыт»)."},
 {"id": "s6", "title": "Кем? — przez + biernik", "facts": ["R11"],
  "body": "Исполнитель — **przez + biernik**. Внимание: не творительный падеж, как в русском «написано Пушкиным».",
  "examples": [["List został wysłany przez sekretarkę.", "Письмо было отправлено секретарём."], ["Obraz został namalowany przez Jana Matejkę.", "Картина была написана Яном Матейко."]],
  "note": "Неверно: *List został wysłany sekretarką*."},
 {"id": "s7", "title": "Как перестроить предложение", "facts": ["R1", "R2", "R11"],
  "body": "1. Дополнение в bierniku → подлежащее (в mianowniku).\n2. Время и вид исходного глагола → być/zostać в том же времени + причастие.\n3. Подлежащее исходного предложения → przez + biernik (можно опустить).\n\n*Policja zatrzymała złodzieja.* → *Złodziej został zatrzymany przez policję.*"},
 {"id": "s8", "title": "Без исполнителя: -no/-to и się", "facts": ["R13", "R14"],
  "body": "**-no/-to** (*zbudowano, otwarto, zamknięto, podpisano*) — «построили, открыли»: нет подлежащего, исполнителя назвать нельзя, дополнение остаётся в **bierniku**: *Otwarto nową wystawę.* Типично для новостей.\n\n**się** — общее действие «у нас так делают»: *W Polsce dużo się czyta. Tutaj sprzedaje się świeży chleb.*",
  "table": {"head": ["Пассив", "-no/-to"], "rows": [["Wystawa została otwarta.", "Otwarto wystawę."], ["Umowa została podpisana.", "Podpisano umowę."]]}},
]

exs = []
exs.append(ex("e1", "Образуйте причастие", "gaps",
  "Напечатайте imiesłów bierny в форме м. р. ед. ч.", [
  item("napisać → {1}", "napisany"), item("przeczytać → {1}", "przeczytany"),
  item("zbudować → {1}", "zbudowany"), item("zaprojektować → {1}", "zaprojektowany"),
  item("zrobić → {1}", "zrobiony"), item("kupić → {1}", "kupiony"),
  item("zaprosić → {1}", "zaproszony"), item("zapłacić → {1}", "zapłacony"),
  item("skończyć → {1}", "skończony"), item("zobaczyć → {1}", "zobaczony"),
  item("zamknąć → {1}", "zamknięty"), item("otworzyć → {1}", "otwarty"),
  item("umyć → {1}", "umyty"), item("wziąć → {1}", "wzięty"),
  item("zacząć → {1}", "zaczęty"), item("zepsuć → {1}", "zepsuty"),
  item("użyć → {1}", "użyty"),
 ], ["R3", "R4", "R5", "R6"]))

exs.append(ex("e2", "Согласуйте причастие", "gaps",
  "Поставьте причастие от глагола в скобках в нужную форму.", [
  item("Książka została {1} (napisać) w 1990 roku.", "napisana"),
  item("Okna są {1} (zamknąć).", "zamknięte"),
  item("Studenci zostali {1} (zaprosić) na konferencję.", "zaproszeni"),
  item("Dziecko zostało {1} (umyć).", "umyte"),
  item("Sprawcy zostali {1} (aresztować).", "aresztowani"),
  item("List został {1} (wysłać) wczoraj.", "wysłany"),
  item("Drzwi zostały {1} (otworzyć) o ósmej.", "otwarte"),
  item("Rachunki są już {1} (zapłacić).", "zapłacone"),
  item("Nowi pracownicy zostali {1} (wybrać) w maju.", "wybrani"),
  item("Zadanie zostało {1} (skończyć).", "skończone"),
  item("Kobiety zostały {1} (wybrać) do zarządu.", "wybrane"),
  item("Piłkarze zostali {1} (ukarać) przez sędziego.", "ukarani"),
  item("Ten film został {1} (nagrodzić) na festiwalu.", "nagrodzony"),
  item("Goście zostali {1} (zaprosić) na siódmą.", "zaproszeni"),
 ], ["R7", "R4", "R5", "R6"]))

exs.append(ex("e3", "być или zostać?", "gaps",
  "Впишите нужную форму być или zostać (событие или состояние?).", [
  item("Most {1} zbudowany w 1990 roku.", "został"),
  item("Sklep {1} zamknięty w niedziele.", "jest"),
  item("Prezydent {1} wybrany w niedzielę.", "został"),
  item("Ten dom {1} zbudowany z drewna.", "jest"),
  item("Jutro wystawa {1} oficjalnie otwarta przez prezydenta miasta.", "zostanie|będzie"),
  item("Muzeum {1} otwarte od wtorku do niedzieli.", "jest"),
  item("Wczoraj złodziej {1} zatrzymany przez policję.", "został"),
  item("Ten wiersz {1} napisany przez Szymborską w 1957 roku.", "został"),
  item("Stół {1} już nakryty, możemy jeść.", "jest"),
  item("W zeszłym tygodniu nowa ustawa {1} przyjęta przez Sejm.", "została"),
  item("Wyniki {1} ogłoszone w przyszły piątek.", "zostaną|będą"),
  item("Nasze mieszkanie {1} ubezpieczone.", "jest"),
 ], ["R8", "R10"]))

exs.append(ex("e4", "przez + biernik", "gaps",
  "Поставьте слова в скобках после przez в нужную форму.", [
  item("List został napisany przez {1} (sekretarka).", "sekretarkę"),
  item("Obraz został namalowany przez {1} (Jan Matejko).", "Jana Matejkę"),
  item("Film został wyreżyserowany przez {1} (Agnieszka Holland).", "Agnieszkę Holland"),
  item("Dom został zaprojektowany przez {1} (znany architekt).", "znanego architekta"),
  item("Ustawa została przyjęta przez {1} (Sejm).", "Sejm"),
  item("Złodziej został zatrzymany przez {1} (policja).", "policję"),
  item("Drzwi zostały zamknięte przez {1} (dozorca).", "dozorcę"),
  item("Ten wiersz został napisany przez {1} (Wisława Szymborska).", "Wisławę Szymborską"),
  item("Pacjent został zbadany przez {1} (lekarze).", "lekarzy"),
  item("Projekt został oceniony przez {1} (komisja).", "komisję"),
 ], ["R11"]))

exs.append(ex("e5", "Из действительного — в страдательный", "gaps",
  "Перестройте в страдательный залог: напечатайте сказуемое (być/zostać + причастие).", [
  item("Poeta napisał wiersz. → Wiersz {1} przez poetę.", "został napisany"),
  item("Policja zatrzymała złodzieja. → Złodziej {1} przez policję.", "został zatrzymany"),
  item("Firma zbuduje nowy most. → Nowy most {1} przez firmę.", "zostanie zbudowany|będzie zbudowany"),
  item("Mama ugotowała obiad. → Obiad {1} przez mamę.", "został ugotowany"),
  item("Dyrektor zaprosił gości. → Goście {1} przez dyrektora.", "zostali zaproszeni"),
  item("Studenci przeczytali książkę. → Książka {1} przez studentów.", "została przeczytana"),
  item("Ktoś otworzył okno. → Okno {1}.", "zostało otwarte"),
  item("Sejm przyjmie ustawę. → Ustawa {1} przez Sejm.", "zostanie przyjęta|będzie przyjęta"),
  item("Lekarz zbadał pacjentkę. → Pacjentka {1} przez lekarza.", "została zbadana"),
  item("Komisja sprawdza testy. → Testy {1} przez komisję.", "są sprawdzane"),
  item("Firma zatrudniła nowych pracowników. → Nowi pracownicy {1} przez firmę.", "zostali zatrudnieni"),
  item("Turyści odwiedzają to muzeum. → To muzeum {1} przez turystów.", "jest odwiedzane"),
 ], ["R1", "R7", "R8", "R9", "R10"]))

exs.append(ex("e6", "Форма на -no/-to", "gaps",
  "Перестройте с формой на -no/-to (без исполнителя). Помните: дополнение — в bierniku.", [
  item("Most został zbudowany w 1990 roku. → {1} most w 1990 roku.", "Zbudowano"),
  item("Wystawa została otwarta w piątek. → Otwarto {1} w piątek.", "wystawę"),
  item("Sklep został zamknięty. → {1} sklep.", "Zamknięto"),
  item("Nowa szkoła została otwarta. → Otwarto {1}.", "nową szkołę"),
  item("Decyzja została podjęta. → Podjęto {1}.", "decyzję"),
  item("Umowa została podpisana wczoraj. → Wczoraj podpisano {1}.", "umowę"),
  item("Złodziej został zatrzymany. → {1} złodzieja.", "Zatrzymano"),
  item("Ustawa została przyjęta. → Przyjęto {1}.", "ustawę"),
  item("Wyniki zostały ogłoszone. → {1} wyniki.", "Ogłoszono"),
  item("Książka została wydana w 2020 roku. → W 2020 roku {1} książkę.", "wydano"),
 ], ["R13"]))

exs.append(ex("e7", "Тест в формате экзамена: новость", "gaps",
  "Uzupełnij tekst. Wpisz formę strony biernej (być/zostać + imiesłów) albo formę na -no/-to — zgodnie z podpowiedzią w nawiasie.", [
  item("W sobotę w Gdańsku {1} nowe Muzeum Morza. (otworzyć → forma na -no/-to)", "otwarto"),
  item("Budynek {1} przez młodą architektkę z Krakowa. (zaprojektować → zostać, przeszły)", "został zaprojektowany"),
  item("Muzeum {1} przez trzy lata. (budować → być, przeszły)", "było budowane"),
  item("Pieniądze na budowę {1} przez miasto. (przekazać → zostać, przeszły)", "zostały przekazane"),
  item("Na otwarcie {1} ponad dwustu gości. (zaprosić → forma na -no/-to)", "zaproszono"),
  item("Najstarsi marynarze {1} medalami. (nagrodzić → zostać, przeszły)", "zostali nagrodzeni"),
  item("Wstęga {1} przez najstarszego kapitana w mieście. (przeciąć → zostać, przeszły)", "została przecięta"),
  item("Od wtorku do niedzieli muzeum {1} dla zwiedzających. (otworzyć → być, teraźniejszy)", "jest otwarte"),
  item("W poniedziałki muzeum {1}. (zamknąć → być, teraźniejszy)", "jest zamknięte"),
  item("Bilety mogą {1} przez internet. (kupować → być + imiesłów)", "być kupowane|być kupione"),
  item("Najcenniejsze eksponaty {1} w przyszłym roku. (pokazać → zostać, przyszły)", "zostaną pokazane|będą pokazane"),
  item("Według organizatorów muzeum {1} przez sto tysięcy osób rocznie. (odwiedzać → być, przyszły)", "będzie odwiedzane"),
 ], ["R1", "R7", "R8", "R9", "R10", "R13"], fmt="exam-text"))

exs.append(ex("e8", "Przekształcenia", "gaps",
  "Перестройте предложение, начиная с данного начала (как в задании VI экзамена). Напечатайте продолжение.", [
  item("Znany architekt zaprojektował ten dom. → Ten dom {1}.", "został zaprojektowany przez znanego architekta"),
  item("Policja zatrzymała dwóch mężczyzn. → Dwaj mężczyźni {1}.", "zostali zatrzymani przez policję"),
  item("Organizatorzy odwołali koncert. → Koncert {1}.", "został odwołany przez organizatorów"),
  item("Ten wiersz został napisany przez Szymborską. → Szymborska {1}.", "napisała ten wiersz"),
  item("Wczoraj podpisano umowę. → Wczoraj umowa {1}.", "została podpisana"),
  item("Turyści często fotografują ten zamek. → Ten zamek {1}.", "jest często fotografowany przez turystów|jest fotografowany przez turystów często|często jest fotografowany przez turystów"),
  item("Sejm przyjmie nową ustawę. → Nowa ustawa {1}.", "zostanie przyjęta przez Sejm|będzie przyjęta przez Sejm"),
  item("Mój dziadek zbudował ten dom. → Ten dom {1}.", "został zbudowany przez mojego dziadka"),
 ], ["R1", "R8", "R9", "R10", "R11", "R13"], fmt="rewrite"))

exs.append({"id": "w1", "kind": "writing", "title": "Заметка в местную газету", "facts": ["R1", "R8", "R11", "R13"],
  "instr": "Napisz krótką notatkę do lokalnej gazety (80–100 słów) o wydarzeniu w Twoim mieście (otwarcie parku, festyn, remont dworca). Napisz: co i kiedy zostało otwarte/zorganizowane, przez kogo, kto został zaproszony, co jeszcze zostanie zrobione.",
  "checklist": ["не меньше 4 форм страдательного залога (został/zostanie …)", "хотя бы 1 исполнитель с przez + biernik", "хотя бы 2 формы на -no/-to (otwarto, zorganizowano)", "газетный стиль: без «ja»"]})
exs.append({"id": "w2", "kind": "writing", "title": "История здания", "facts": ["R8", "R9", "R10"],
  "instr": "Opisz historię ważnego budynku w Twoim mieście lub kraju (80–100 słów): kiedy i przez kogo został zbudowany, co było w nim robione, co zostało zmienione, jak jest używany dziś.",
  "checklist": ["даты с zostać (został zbudowany w … roku)", "хотя бы 1 процесс с być (był budowany przez … lat)", "хотя бы 1 состояние сегодня (jest otwarty / jest używany)", "хотя бы 1 форма будущего (zostanie odnowiony)"]})

topic = {"id": "strona-bierna", "num": 12, "title": "Strona bierna: страдательный залог", "level": "B1",
  "lang": "ru", "prev": "zeby-aby", "next": "mowa-zalezna",
  "summary": "być / zostać + imiesłów bierny: образование причастий (-any, -ony, -ty), согласование, событие или состояние, przez + biernik, безличные формы на -no/-to и się.",
  "sections": sections, "exercises": exs}
save("strona-bierna", extract, topic)
