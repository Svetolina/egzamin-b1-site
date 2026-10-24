import sys; sys.path.insert(0, '/home/claude/build')
from lib import S, item, ex, save

EK = "https://elon.io/grammar/polish/pronouns/indefinite/ktos-cos"
EN = "https://elon.io/grammar/polish/pronouns/negative/nikt-nic"
ED = "https://elon.io/grammar/polish/negation/double-negation"
DZ = "https://faculty.washington.edu/dziwirek/grammar/nouns/polish-indef-prons.pdf"
CZ = "https://www.clozemaster.com/blog/polish-negative-pronouns/"
WM = "https://en.wikipedia.org/wiki/Polish_morphology"
PD = "https://www.polskidaily.eu/wp-content/uploads/2021/01/Subject-expressed-with-Genitive.pdf"

ek = lambda l: S("elon.io — «Indefinite Pronouns: ktoś, coś, gdzieś, jakiś»", EK, l)
en = lambda l: S("elon.io — «Negative Pronouns and Double Negation: nikt, nic, nigdy»", EN, l)
ed = lambda l: S("elon.io — «Double and Multiple Negation»", ED, l)
dz = lambda l: S("K. Dziwirek (University of Washington), «Indefinite pronouns» (по Z. Kalecie)", DZ, l)
cz = lambda l: S("Clozemaster Blog — «The Polish Negative Pronouns “nikt” and “nic”»", CZ, l)
wm = lambda l: S("Wikipedia (en) — «Polish morphology»", WM, l)

F = [
 ("R1", "Вопросительное слово + -ś = «-то»: ktoś (кто-то), coś, gdzieś, kiedyś, jakoś, jakiś, czyjś — существует, но не названо.",
  [ek("таблица -ś"), dz("таблица пар -ś / -kolwiek")]),
 ("R2", "ktoś и coś склоняются как kto и co, окончание стоит перед -ś: kogoś, komuś, kimś, o kimś; czegoś, czemuś, czymś, o czymś. Падеж задаёт глагол или предлог: Szukam kogoś. Rozmawiałam z kimś.",
  [ek("раздел Declension; Common mistakes: «z kimś», «Szukam kogoś»"), wm("таблица kto / co; «derived pronouns … declined similarly to kto and co»")]),
 ("R3", "jakiś согласуется как прилагательное: jakiś pan, jakaś pani, jakieś pytanie.",
  [ek("раздел jakiś agreement; ошибка «Dzwonił jakiś pani»"), dz("jakiś — «some kind of», jakikolwiek")]),
 ("R4", "-kolwiek = «любой, неважно кто/что; -угодно, -бы ни»: ktokolwiek, cokolwiek, gdziekolwiek, kiedykolwiek, jakikolwiek.",
  [dz("правило Z. Kalety: -kolwiek — «identity doesn't matter»; совет переводить как -ever"), ek("раздел -ś vs -kolwiek")]),
 ("R5", "kiedyś может значить и «когда-то (в прошлом)», и «когда-нибудь (в будущем)».",
  [dz("примечание к kiedyś")]),
 ("R6", "Отрицательные слова nikt, nic, nigdy, nigdzie, żaden всегда требуют nie при глаголе (двойное отрицание), и их можно ставить несколько: Nikt nic nie powiedział. Ошибка: *Nikt przyszedł*.",
  [en("Core rule, Common mistakes"), ed("«Verbal nie is mandatory», «Multiple negatives add emphasis»"), cz("«Nikt nic nie wie», triple negation is normal")]),
 ("R7", "Склонение: nikt — nikogo, nikomu, nikogo, nikim, o nikim; nic — niczego, niczemu, nic, niczym, o niczym.",
  [en("раздел Declension"), cz("таблица nikt / nic"), wm("«declined similarly to kto and co»")]),
 ("R8", "Как дополнение при отрицании возможны и nic, и niczego: Nie mam nic / Nie mam niczego (niczego — выразительнее/официальнее). Niczego nie żałuję.",
  [en("раздел Nic after negated verbs"), ed("«Nie mam nic» и «Nie mam niczego»"), wm("«nic has the unaltered (accusative) form instead of niczego»")]),
 ("R9", "В отрицательном предложении «any-» передаётся словами на ni-, а не -ś / -kolwiek: Nic nie widzę (не *Nie widzę cokolwiek*), Nie mam nic (не *Nie mam coś*).",
  [ek("Common mistakes: «Nie widzę cokolwiek → Nic nie widzę»"), ed("Common mistakes: «Nie mam coś → Nie mam nic»"), cz("«nikt and nic can also mean anybody and anything»")]),
 ("R10", "żaden («никакой, ни один») склоняется как прилагательное; как дополнение при отрицании — в dopełniaczu: Nie znam żadnego z tych ludzi.",
  [en("раздел Żaden agreement"), ed("«żaden declines like an adjective»")]),
 ("R11", "coś / nic + прилагательное в dopełniaczu: coś ciekawego, nic nowego, niczego podejrzanego.",
  [S("Polski Daily — «Subject expressed with Genitive» (PDF)", PD, "пункт coś / nic / co + przymiotnik: «Nic ciekawego się nie stało»"), cz("пример «Nie zauważyłem niczego podejrzanego»")]),
 ("R12", "С nikt глагол прошедшего времени — в м. р. ед. ч.: Nikt nie przyszedł. Также ani razu («ни разу»), wcale («совсем не»): Ani razu nie zadzwonił. Wcale mi to nie przeszkadza.",
  [en("nikt «defaults to masculine singular in the past tense»"), ed("wcale, ani")]),
]
extract = {"topic": "zaimki-nieokreslone", "title": "Zaimki nieokreślone i przeczące", "facts": [
    {"id": i, "rule": r, "sources": s} for i, r, s in F]}
for f in extract["facts"]:
    if len(f["sources"]) < 2:
        f["single_source_note"] = "Подтверждено одним источником — дано одной строкой с пометкой."
extract["facts"][11]["note"] = "Два источника — разные страницы одного сайта (elon.io)."

sections = [
 {"id": "s1", "title": "Три ряда местоимений", "facts": ["R1", "R4", "R6"],
  "table": {"head": ["Вопрос", "-ś (-то)", "-kolwiek (-угодно)", "ni- (никто)"], "rows": [
     ["kto?", "ktoś", "ktokolwiek", "nikt"], ["co?", "coś", "cokolwiek", "nic"], ["gdzie?", "gdzieś", "gdziekolwiek", "nigdzie"],
     ["kiedy?", "kiedyś", "kiedykolwiek", "nigdy"], ["jaki?", "jakiś", "jakikolwiek", "żaden"], ["jak?", "jakoś", "jakkolwiek", "—"]]},
  "note": "kiedyś — и «когда-то», и «когда-нибудь» (одним источником)."},
 {"id": "s2", "title": "ktoś, coś — склонение", "facts": ["R2", "R3"],
  "body": "Склоняются как *kto, co*; окончание — **перед -ś**.",
  "table": {"head": ["Падеж", "ktoś", "coś"], "rows": [
     ["M.", "ktoś", "coś"], ["D.", "kogoś", "czegoś"], ["C.", "komuś", "czemuś"], ["B.", "kogoś", "coś"], ["N.", "kimś", "czymś"], ["Ms.", "o kimś", "o czymś"]]},
  "note": "jakiś согласуется: jakiś pan, jakaś pani, jakieś pytanie. Ошибки: *z ktoś → z kimś; *Szukam ktoś → Szukam kogoś."},
 {"id": "s3", "title": "-kolwiek: любой, неважно какой", "facts": ["R4"],
  "examples": [["Możesz zapytać kogokolwiek.", "Можешь спросить кого угодно."], ["Cokolwiek zrobisz, będę z tobą.", "Что бы ты ни сделал, я буду с тобой."], ["Dzwoń kiedykolwiek.", "Звони когда угодно."]]},
 {"id": "s4", "title": "Двойное отрицание", "facts": ["R6", "R9", "R12"],
  "body": "Как в русском: **nikt nie**, **nic nie**, **nigdy nie** — nie обязательно. Можно ставить несколько отрицаний: *Nikt nigdy nigdzie nic nie powiedział.*\n\nВ отрицании не используются -ś / -kolwiek: *Nic nie widzę* (не *Nie widzę cokolwiek*).",
  "note": "С nikt глагол в м. р.: Nikt nie przyszedł. Ani razu — «ни разу», wcale — «совсем не»."},
 {"id": "s5", "title": "nikt, nic — склонение", "facts": ["R7", "R8"],
  "table": {"head": ["Падеж", "nikt", "nic"], "rows": [
     ["M.", "nikt", "nic"], ["D.", "nikogo", "niczego"], ["C.", "nikomu", "niczemu"], ["B.", "nikogo", "nic"], ["N.", "nikim", "niczym"], ["Ms.", "o nikim", "o niczym"]]},
  "note": "Дополнение при отрицании: nic или niczego — оба верны (niczego выразительнее): Nie mam nic / Nie mam niczego."},
 {"id": "s6", "title": "żaden", "facts": ["R10"],
  "body": "*żaden, żadna, żadne* — «никакой, ни один»; склоняется как прилагательное; при отрицании дополнение — в dopełniaczu: *Nie mam żadnego pytania. Nie znam żadnego z tych ludzi.*"},
 {"id": "s7", "title": "coś ciekawego, nic nowego", "facts": ["R11"],
  "body": "После coś / nic прилагательное стоит в **dopełniaczu**: *coś ciekawego, nic nowego, coś słodkiego, niczego podejrzanego*. Как в русском «что-то интересное» — но в польском родительный падеж."},
]

exs = []
exs.append(ex("e1", "ktoś, coś, jakiś… в нужной форме", "gaps", "Впишите местоимение на -ś в нужной форме (подсказка по-русски).", [
  item("{1} dzwonił, kiedy byłeś pod prysznicem. (кто-то)", "Ktoś"),
  item("Muszę ci o {1} powiedzieć. (что-то)", "czymś"),
  item("Rozmawiałam z {1} o tobie. (кем-то)", "kimś"),
  item("Szukam {1}, kto mi pomoże. (кого-то)", "kogoś"),
  item("Dzwonił {1} pan. (какой-то)", "jakiś"),
  item("Dzwoniła {1} pani. (какая-то)", "jakaś"),
  item("Mam {1} pytanie. (какой-то)", "jakieś"),
  item("Zostawiłam {1} klucze. (где-то)", "gdzieś"),
  item("{1} byłam w Paryżu. (когда-то)", "Kiedyś"),
  item("Daj mi {1} do picia. (что-нибудь)", "coś"),
  item("Dam to {1} z rodziny. (кому-нибудь)", "komuś"),
  item("To {1} parasol? (чей-то)", "czyjś"),
  item("Interesuję się {1} nowym. (чем-то)", "czymś"),
  item("{1} sobie poradzimy. (как-нибудь)", "Jakoś"),
 ], ["R1", "R2", "R3"]))

exs.append(ex("e2", "-ś или -kolwiek?", "gaps", "Впишите местоимение на -ś или -kolwiek в нужной форме.", [
  item("Możesz zapytać {1} — wszyscy znają drogę. (кого угодно)", "kogokolwiek"),
  item("Zjem {1}, jestem bardzo głodny. (что угодно)", "cokolwiek"),
  item("Usiądź {1}. (где угодно)", "gdziekolwiek"),
  item("Dzwoń {1}, nawet w nocy. (когда угодно)", "kiedykolwiek"),
  item("{1} zapukał do drzwi. (кто-то)", "Ktoś"),
  item("Czy byłeś {1} w Polsce? (когда-нибудь)", "kiedykolwiek|kiedyś"),
  item("{1} zrobisz, będę z tobą. (что бы ни)", "Cokolwiek"),
  item("Kupiłam {1} prezent dla mamy. (какой-то)", "jakiś"),
  item("Weź {1} książkę, wszystkie są ciekawe. (любую)", "jakąkolwiek"),
  item("{1} pojedziesz, pisz do mnie. (куда бы ни)", "Gdziekolwiek"),
 ], ["R4", "R1", "R5"]))

exs.append(ex("e3", "Ответьте отрицательно", "gaps", "Ответьте «нет», используя nikt, nic, nigdy, nigdzie, żaden в нужной форме.", [
  item("Ktoś dzwonił? — Nie, {1} nie dzwonił.", "nikt"),
  item("Widzisz coś? — Nie, {1} nie widzę.", "nic|niczego"),
  item("Byłeś kiedyś w Japonii? — Nie, {1} nie byłem.", "nigdy"),
  item("Idziesz gdzieś wieczorem? — Nie, {1} nie idę.", "nigdzie"),
  item("Czekasz na kogoś? — Nie, na {1} nie czekam.", "nikogo"),
  item("Rozmawiałeś z kimś? — Nie, z {1} nie rozmawiałem.", "nikim"),
  item("Myślisz o czymś? — Nie, o {1} nie myślę.", "niczym"),
  item("Dałeś to komuś? — Nie, {1} tego nie dałem.", "nikomu"),
  item("Masz jakieś pytanie? — Nie, nie mam {1} pytania.", "żadnego"),
  item("Interesujesz się czymś? — Nie, {1} się nie interesuję.", "niczym"),
  item("Kogoś szukasz? — Nie, {1} nie szukam.", "nikogo"),
  item("Boisz się czegoś? — Nie, {1} się nie boję.", "niczego|nic"),
 ], ["R6", "R7", "R8", "R10"]))

exs.append(ex("e4", "Исправьте ошибку", "gaps", "Напечатайте правильную форму вместо пропуска.", [
  item("Nikt przyszedł. → Nikt {1} przyszedł.", "nie"),
  item("Nigdy byłem w Hiszpanii. → Nigdy {1} w Hiszpanii.", "nie byłem"),
  item("Nie mam coś do picia. → Nie mam {1} do picia.", "nic|niczego"),
  item("Nie znam żaden z tych ludzi. → Nie znam {1} z tych ludzi.", "żadnego"),
  item("Rozmawiałem z ktoś. → Rozmawiałem z {1}.", "kimś"),
  item("Nie widzę cokolwiek. → {1} nie widzę.", "Nic|Niczego"),
  item("Nigdy nie powiem to nikomu. → Nigdy nikomu {1} nie powiem.", "tego"),
  item("Dzwonił jakiś pani. → Dzwoniła {1} pani.", "jakaś"),
 ], ["R2", "R3", "R6", "R8", "R9", "R10"]))

exs.append(ex("e5", "coś ciekawego, nic nowego", "gaps", "Поставьте прилагательное в dopełniacz.", [
  item("Opowiedz mi coś {1} (ciekawy).", "ciekawego"),
  item("Nic {1} (nowy) się nie stało.", "nowego"),
  item("Zjadłabym coś {1} (słodki).", "słodkiego"),
  item("Nie zauważyłem niczego {1} (podejrzany).", "podejrzanego"),
  item("Coś {1} (inny) mi się przypomniało.", "innego"),
  item("Nie mam nic {1} (ważny) do powiedzenia.", "ważnego"),
  item("Kup coś {1} (dobry) na kolację.", "dobrego"),
  item("Nic {1} (zły) się nie stanie.", "złego"),
 ], ["R11"]))

exs.append(ex("e6", "Несколько отрицаний", "gaps", "Переведите, заполнив пропуски.", [
  item("Никто ничего не сказал. → {1} {2} nie powiedział.", "Nikt", "nic|niczego"),
  item("Я никогда никому не говорю. → {1} {2} nie mówię.", "Nigdy", "nikomu"),
  item("Никто нигде не был. → {1} {2} nie był.", "Nikt", "nigdzie"),
  item("Мы ни с кем ни о чём не говорили. → Z {1} o {2} nie rozmawialiśmy.", "nikim", "niczym"),
  item("Он ни разу не позвонил. → {1} razu nie zadzwonił.", "Ani"),
  item("Мне это совсем не мешает. → {1} mi to nie przeszkadza.", "Wcale"),
  item("Там никого нет. → {1} tam nie ma.", "Nikogo"),
  item("В коробке ничего не было. → W pudełku {1} nie było.", "nic|niczego"),
 ], ["R6", "R7", "R12"]))

exs.append(ex("e7", "Тест в формате экзамена: рассказ", "gaps",
  "Uzupełnij tekst. Wpisz zaimek (ktoś, nikt, jakiś, nic…) w odpowiedniej formie. W nawiasie — podpowiedź po rosyjsku.", [
  item("Wczoraj wieczorem {1} zadzwonił do drzwi. (кто-то)", "ktoś"),
  item("Otworzyłam, ale {1} nie było. (никого)", "nikogo"),
  item("Myślałam, że to {1} dzieci z sąsiedztwa. (какие-то)", "jakieś"),
  item("Po godzinie znowu {1} zadzwonił. (кто-то)", "ktoś"),
  item("Zapytałam sąsiadów, ale {1} nic nie widział. (никто)", "nikt"),
  item("Pani Nowak powiedziała, że {1} nie słyszała takiej historii. (никогда)", "nigdy"),
  item("Potem {1} w domu zaczął dzwonić telefon, (где-то)", "gdzieś"),
  item("ale w słuchawce {1} nie było słychać. (ничего)", "nic|niczego"),
  item("Następnego dnia znalazłam pod drzwiami {1} list. (какое-то)", "jakiś"),
  item("Nie było w nim {1}: (ничего интересного)", "nic ciekawego|niczego ciekawego|nic interesującego|niczego interesującego"),
  item("tylko {1} reklama. (какая-то)", "jakaś"),
  item("Teraz wieczorem {1} nie otwieram drzwi! (никому)", "nikomu"),
 ], ["R1", "R2", "R3", "R6", "R7", "R8", "R11"], fmt="exam-text"))

exs.append(ex("e8", "Przekształcenia", "gaps", "Сделайте предложение отрицательным. Напечатайте продолжение.", [
  item("Ktoś przyszedł. → {1}.", "Nikt nie przyszedł|Nie przyszedł nikt"),
  item("Coś widzę. → {1}.", "Nic nie widzę|Niczego nie widzę|Nie widzę nic|Nie widzę niczego"),
  item("Zawsze tu jem. → {1} tu nie jem.", "Nigdy"),
  item("Wszędzie byłam. → {1}.", "Nigdzie nie byłam|Nie byłam nigdzie"),
  item("Mam jakiś pomysł. → Nie mam {1}.", "żadnego pomysłu"),
  item("Wszyscy wiedzą wszystko. → {1}.", "Nikt nic nie wie|Nikt niczego nie wie"),
  item("Rozmawiam z kimś. → {1}.", "Z nikim nie rozmawiam|Nie rozmawiam z nikim"),
  item("Znam kogoś w tym mieście. → {1} w tym mieście.", "Nikogo nie znam|Nie znam nikogo"),
 ], ["R6", "R7", "R8", "R10"], fmt="rewrite"))

exs.append({"id": "w1", "kind": "writing", "title": "Жалоба на гостиницу", "facts": ["R6", "R7", "R8", "R10"],
  "instr": "Napisz e-mail z reklamacją do hotelu (80–100 słów). Nic nie działało tak, jak obiecano: nikt nie odbierał telefonu, w pokoju nie było żadnych ręczników, nigdzie nie można było zaparkować…",
  "checklist": ["не меньше 5 отрицательных слов (nikt, nic, nigdy, nigdzie, żaden)", "везде nie при глаголе", "żaden в dopełniaczu", "официальное обращение и подпись"]})
exs.append({"id": "w2", "kind": "writing", "title": "Объявление: ищу кого-то", "facts": ["R1", "R2", "R4", "R11"],
  "instr": "Napisz ogłoszenie (50–70 słów): szukasz kogoś, kto pomoże Ci w nauce polskiego / zaopiekuje się kotem / pomoże przy przeprowadzce. Napisz, czego oczekujesz i kiedy można się kontaktować.",
  "checklist": ["szukam kogoś, kto…", "1 форма jakiś в нужном роде", "1 форма -kolwiek (kiedykolwiek, gdziekolwiek)", "coś + прилагательное в dopełniaczu"]})

topic = {"id": "zaimki-nieokreslone", "num": 18, "title": "Ktoś, ktokolwiek, nikt: неопределённые и отрицательные местоимения", "level": "B1",
  "lang": "ru", "prev": "rzeczowniki-odczasownikowe", "next": "spojniki-przyczyna-przyzwolenie",
  "summary": "Ряды ktoś / ktokolwiek / nikt: склонение, jakiś и żaden, двойное отрицание, nic или niczego, coś ciekawego.",
  "sections": sections, "exercises": exs}
save("zaimki-nieokreslone", extract, topic)
