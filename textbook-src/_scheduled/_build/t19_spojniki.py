import sys; sys.path.insert(0, '/home/claude/build')
from lib import S, item, ex, save

ECR = "https://elon.io/grammar/polish/conjunctions/cause-result"
ECI = "https://elon.io/grammar/polish/expressions/connecting-ideas"
ECC = "https://elon.io/grammar/polish/conjunctions/contrast-condition"
EL1 = "https://elon.io/learn-hardcore-polish/lexicon/500813/mimo-że-pada-deszcz-idę-na-spacer."
EL2 = "https://elon.io/learn-hardcore-polish/lexicon/500867/idę-na-spacer-mimo-deszczu."
VA = "https://vaia.com/en-us/explanations/polish/polish-syntax/polish-sentence-connectors"
BK = "https://journals.us.edu.pl/index.php/TPDJP/article/download/12879/9990"
NCK = "https://nck.pl/projekty-kulturalne/projekty/ojczysty-dodaj-do-ulubionych/ciekawostki-jezykowe/mimo-ze-pomimo-ze-.ajax"
LM = "https://en.langenscheidt.com/polish-german/mimo"

ecr = lambda l: S("elon.io — «Cause and result: bo, ponieważ, więc, dlatego»", ECR, l)
eci = lambda l: S("elon.io — «Connecting ideas»", ECI, l)
ecc = lambda l: S("elon.io — «Contrast and Condition: ale, jednak, chociaż…»", ECC, l)
va = lambda l: S("Vaia — «Polish Sentence Connectors»", VA, l)
bk = lambda l: S("K. Bakuła, «Bo v. ponieważ i inne spójniki w mówionym i pisanym», Z Teorii i Praktyki Dydaktycznej Języka Polskiego t. 30, 2021", BK, l)
lm = lambda l: S("Langenscheidt Polish–German — «mimo»", LM, l)
nck = lambda l: S("NCK / Ojczysty — dodaj do ulubionych: «Mimo że, pomimo że»", NCK, l)

F = [
 ("R1", "Причина: bo, ponieważ, gdyż («потому что»); перед ними — запятая. Ponieważ может стоять в начале предложения (Ponieważ było zimno, wzięłam kurtkę), bo — нет: не *Bo był zmęczony, poszedł spać*.",
  [ecr("раздел Cause Conjunctions, Punctuation, Common Mistakes"), eci("«bo cannot start a sentence»; ponieważ «can open the sentence»")]),
 ("R2", "Стиль: gdyż — официальный, письменный; ponieważ — нейтральный, уместен в официальном письме; bo — очень частый, обычно считается разговорным (хотя исследования показывают, что он широко встречается и в письменных текстах).",
  [ecr("описания bo / ponieważ / gdyż"), va("«ponieważ … formal contexts», «bo … casual speech»"), bk("с. 150–152, 163–164: противопоставление bo (устн.) / ponieważ (письм.) — «złudzenie poznawcze»")]),
 ("R3", "dlatego że (или dlatego…, że) — «потому что» с упором на причину: Wyjechała dlatego, że chciała odpocząć.",
  [ecr("разделы dlatego że и dlatego … że"), eci("«dlatego że is an alternative for fronting the reason»")]),
 ("R4", "Следствие: więc, dlatego, zatem (офиц.), toteż — «поэтому, так что»; стоят после причины, перед ними запятая: Padało, więc wzięliśmy parasol. Ошибка: *Zostaliśmy w domu, dlatego padało*.",
  [ecr("раздел Result Conjunctions, Common Mistakes"), eci("dlatego и więc — «bo points back, dlatego points forward»"), va("więc, dlatego, zatem в таблице связок")]),
 ("R5", "Причина-существительное — через предлог: z powodu + dopełniacz (нейтр.), przez + biernik (часто с упрёком), dzięki + celownik (положительная причина).",
  [ecr("раздел Causes With Nouns")]),
 ("R6", "Уступка: chociaż, choć, mimo że, pomimo że («хотя») + придаточное; в главной части ale/jednak НЕ добавляется: Chociaż padało, wyszliśmy na spacer (не *…, ale wyszliśmy*).",
  [ecc("раздел о chociaż / mimo że; ошибка «Chociaż padało, ale…»"), lm("mimo że — spójnik, «obwohl»"), S("elon.io — пример «Mimo że pada deszcz, idę na spacer»", EL1, "пример")]),
 ("R7", "Запятая ставится перед всем союзом mimo że / pomimo że, а не внутри: …, mimo że… (не *mimo, że*).",
  [nck("правило о przecinku przed całym wyrażeniem")]),
 ("R8", "mimo / pomimo + dopełniacz — «несмотря на»: mimo deszczu, pomimo problemów. Устойчиво: mimo wszystko.",
  [lm("mimo — przyimek + dopełniacz; mimo wszystko"), S("elon.io — пример «Idę na spacer mimo deszczu»", EL2, "пример")]),
 ("R9", "mimo to, jednak — «тем не менее, однако»: Był chory. Mimo to poszedł do pracy. jednak может стоять в начале или внутри предложения.",
  [lm("mimo to — «trotzdem»"), ecc("jednak — «can open the clause or sit inside it»"), va("jednak «often starts a sentence»")]),
 ("R10", "Противопоставление: ale (нейтр.), lecz (книжн.) — с запятой перед ними: Chciałem przyjść, ale nie miałem czasu.",
  [ecc("ale, lecz; ошибка без запятой"), va("ale «between clauses»")]),
]
extract = {"topic": "spojniki-przyczyna-przyzwolenie", "title": "Spójniki: przyczyna, skutek, przyzwolenie", "facts": [
    {"id": i, "rule": r, "sources": s} for i, r, s in F]}
for f in extract["facts"]:
    if len(f["sources"]) < 2:
        f["single_source_note"] = "Подтверждено одним источником — дано одной строкой с пометкой."
extract["facts"][0]["note"] = "Оба источника — разные страницы одного сайта (elon.io); правило «bo не в начале» — норма письменной речи."

sections = [
 {"id": "s1", "title": "Причина: bo, ponieważ, gdyż", "facts": ["R1", "R2"],
  "table": {"head": ["Союз", "Стиль", "В начале предложения?"], "rows": [
     ["bo", "очень частый, разговорный оттенок", "нет"], ["ponieważ", "нейтральный, годится для официального письма", "да"],
     ["gdyż", "официальный, письменный", "—"]]},
  "examples": [["Zostałem w domu, bo byłem zmęczony.", "Я остался дома, потому что устал."], ["Ponieważ było zimno, wzięłam kurtkę.", "Поскольку было холодно, я взяла куртку."], ["Plan wstrzymano, gdyż brakowało funduszy.", "План приостановили, так как не хватало средств."]],
  "note": "Ошибки: *Bo był zmęczony, poszedł spać → Ponieważ…; *Nie poszedłem, bo deszcz → bo padał deszcz (после bo — целое предложение)."},
 {"id": "s2", "title": "dlatego że", "facts": ["R3"],
  "body": "*dlatego że* — «потому что» с упором: *Uczę się polskiego, dlatego że lubię języki.* С выделением: *Wyjechała dlatego, że chciała odpocząć.*"},
 {"id": "s3", "title": "Следствие: więc, dlatego, zatem", "facts": ["R4"],
  "body": "**bo** смотрит назад, на причину; **więc / dlatego** — вперёд, на результат.",
  "table": {"head": ["Причина → следствие", "Следствие ← причина"], "rows": [
     ["Padało, więc wzięliśmy parasol.", "Wzięliśmy parasol, bo padało."], ["Był zmęczony, dlatego poszedł spać.", "Poszedł spać, ponieważ był zmęczony."], ["Zaspał, toteż spóźnił się.", "Spóźnił się, bo zaspał."]]},
  "note": "zatem — официальный; toteż — книжный."},
 {"id": "s4", "title": "Причина-существительное", "facts": ["R5"],
  "table": {"head": ["Предлог", "Падеж", "Пример"], "rows": [
     ["z powodu", "D.", "Zamknięto drogę z powodu remontu."], ["przez", "B.", "Spóźniłem się przez awarię."], ["dzięki", "C.", "Udało się dzięki pomocy kolegi."]]},
  "note": "przez — часто с упрёком, dzięki — «благодаря» (хорошее). Правило — одним источником."},
 {"id": "s5", "title": "Уступка: chociaż, mimo że", "facts": ["R6", "R7"],
  "body": "**chociaż / choć / mimo że / pomimo że** + предложение — «хотя». В главной части **без ale**: *Chociaż padało, wyszliśmy na spacer.*\n\nЗапятая — перед всем союзом: *…, mimo że…* (не *mimo, że*).",
  "note": "Ошибка по русской модели «хотя…, но…»: *Chociaż padało, ale wyszliśmy*."},
 {"id": "s6", "title": "mimo + dopełniacz; mimo to", "facts": ["R8", "R9"],
  "table": {"head": ["С предложением", "С существительным", "Отдельное слово"], "rows": [
     ["Mimo że padał deszcz, poszliśmy.", "Mimo deszczu poszliśmy.", "Padał deszcz. Mimo to poszliśmy."]]},
  "body": "*mimo wszystko* — «несмотря ни на что». *jednak* — «однако»: в начале или внутри: *Postanowiłem jednak spróbować.*"},
 {"id": "s7", "title": "ale, lecz", "facts": ["R10"],
  "body": "*ale* — обычное «но», *lecz* — книжное. Перед ними — запятая: *Chciałem przyjść, ale nie miałem czasu.*"},
]

C = "bo|ponieważ|gdyż"
CD = C + "|dlatego że"
R = "więc|dlatego"
Z = "Chociaż|Choć|Mimo że|Pomimo że"
exs = []
exs.append(ex("e1", "bo или ponieważ?", "gaps", "Впишите союз причины. В начале предложения bo нельзя. Где помечено «офиц.» — только официальный союз.", [
  item("Zostałem w domu, {1} byłem zmęczony.", CD),
  item("{1} było zimno, wzięłam kurtkę.", "Ponieważ"),
  item("Nie przyszła, {1} była chora.", CD),
  item("{1} nie mam czasu, nie pójdę z wami.", "Ponieważ"),
  item("Uczę się polskiego, {1} lubię języki.", C + "|dlatego że"),
  item("Uprzejmie informuję, że nie będę obecny na zebraniu, {1} jestem w delegacji. (офиц.)", "gdyż|ponieważ"),
  item("{1} autobus się spóźnił, wzięłam taksówkę.", "Ponieważ"),
  item("Nie zadzwoniłem, {1} nie miałem twojego numeru.", CD),
  item("Wyjechała {1}, że chciała odpocząć.", "dlatego"),
  item("Nie kupię tego, {1} jest za drogie.", CD),
  item("{1} pada deszcz, zostaniemy w domu.", "Ponieważ"),
  item("Szkolenie odwołano, {1} zachorował trener. (офиц.)", "gdyż|ponieważ"),
 ], ["R1", "R2", "R3"]))

exs.append(ex("e2", "Причина или следствие?", "gaps", "Впишите bo/ponieważ (причина) или więc/dlatego (следствие).", [
  item("Padało, {1} wzięliśmy parasol.", R + "|toteż"),
  item("Wzięliśmy parasol, {1} padało.", C),
  item("Był zmęczony, {1} poszedł wcześnie spać.", R + "|toteż"),
  item("Poszedł wcześnie spać, {1} był zmęczony.", C),
  item("Zaspał, {1} spóźnił się do pracy.", R + "|toteż"),
  item("Spóźnił się do pracy, {1} zaspał.", C),
  item("Nie mam samochodu, {1} jeżdżę autobusem.", R + "|toteż"),
  item("Jeżdżę autobusem, {1} nie mam samochodu.", C),
  item("Wyniki są jasne, {1} decyzja jest prosta.", R + "|zatem"),
  item("Lubię to miasto, {1} jest spokojne.", C),
 ], ["R1", "R4"]))

exs.append(ex("e3", "z powodu, przez, dzięki", "gaps", "Поставьте слово в скобках в нужный падеж.", [
  item("Zamknięto drogę z powodu {1} (remont).", "remontu"),
  item("Spóźniłem się przez {1} (awaria).", "awarię"),
  item("Udało się dzięki {1} (pomoc) kolegi.", "pomocy"),
  item("Lot odwołano z powodu {1} (mgła).", "mgły"),
  item("Przez {1} (ty) spóźniłam się na pociąg!", "ciebie"),
  item("Dzięki {1} (wy) wszystko się udało.", "wam"),
  item("Szkoła była zamknięta z powodu {1} (choroba) nauczycieli.", "choroby"),
  item("Zdałam egzamin dzięki {1} (twoje notatki).", "twoim notatkom"),
  item("Przez {1} (korek) nie zdążyliśmy na film.", "korek"),
  item("Mecz przełożono z powodu {1} (deszcz).", "deszczu"),
 ], ["R5"]))

exs.append(ex("e4", "Хотя, несмотря на, но", "gaps", "Впишите союз или поставьте слово в нужную форму.", [
  item("{1} padał deszcz, poszliśmy na spacer. (хотя)", Z),
  item("Poszliśmy na spacer mimo {1} (deszcz).", "deszczu"),
  item("Mimo {1} (zmęczenie) skończył pracę.", "zmęczenia"),
  item("{1} jest starsza od narzeczonego, dobrze się rozumieją. (хотя)", Z),
  item("Pomimo {1} (problemy) firma się rozwija.", "problemów"),
  item("Był chory. {1} poszedł do pracy. (тем не менее)", "Mimo to|Jednak|Mimo wszystko"),
  item("Mimo {1} (późna godzina) wszyscy jeszcze pracowali.", "późnej godziny"),
  item("Lubię go, {1} czasem mnie denerwuje. (хотя)", "chociaż|choć|mimo że|pomimo że"),
  item("Chciałem przyjść, {1} nie miałem czasu. (но)", "ale|lecz"),
  item("Nie mówię dobrze po polsku, {1} rozumiem prawie wszystko. (но / однако)", "ale|lecz|jednak"),
  item("Mimo {1} jestem optymistką. (всё)", "wszystko"),
 ], ["R6", "R8", "R9", "R10"]))

exs.append(ex("e5", "Исправьте ошибку", "gaps", "Напечатайте правильный вариант вместо пропуска.", [
  item("Bo był zmęczony, poszedł spać. → {1} był zmęczony, poszedł spać.", "Ponieważ"),
  item("Zostałem w domu bo padało. → Напишите с правильной пунктуацией: {1}", "Zostałem w domu, bo padało"),
  item("Chociaż padało, ale wyszliśmy na spacer. → Chociaż padało, {1} na spacer.", "wyszliśmy"),
  item("Nie poszedłem, bo deszcz. → Nie poszedłem, bo {1}.", "padał deszcz|padało"),
  item("Zostaliśmy w domu, dlatego padało. → Padało, {1} zostaliśmy w domu.", R),
  item("Mimo deszcz poszliśmy na spacer. → Mimo {1} poszliśmy na spacer.", "deszczu"),
  item("Był zmęczony, bo poszedł spać. → Był zmęczony, {1} poszedł spać.", R),
  item("Album mimo, że został nagrany dawno, jest popularny. → Album, {1} został nagrany dawno, jest popularny.", "mimo że|choć|chociaż"),
 ], ["R1", "R4", "R6", "R7", "R8"]))

exs.append(ex("e6", "Соедините предложения", "gaps", "Соедините два предложения данным союзом. Напечатайте пропущенную часть.", [
  item("Jest zimno. Włożę kurtkę. (więc) → Jest zimno, {1}.", "więc włożę kurtkę"),
  item("Nie przyszedł. Był chory. (bo) → Nie przyszedł, {1}.", "bo był chory"),
  item("Było późno. Pracowaliśmy dalej. (chociaż) → {1}, pracowaliśmy dalej.", "Chociaż było późno"),
  item("Mam egzamin. Uczę się całą noc. (dlatego) → Mam egzamin, {1}.", "dlatego uczę się całą noc|dlatego całą noc się uczę"),
  item("Padał deszcz. Graliśmy w piłkę. (mimo że) → {1}, graliśmy w piłkę.", "Mimo że padał deszcz|Mimo że padało"),
  item("Autobus się spóźnił. Wzięłam taksówkę. (ponieważ) → {1}, wzięłam taksówkę.", "Ponieważ autobus się spóźnił"),
  item("Lubię go. Często się kłócimy. (ale) → Lubię go, {1}.", "ale często się kłócimy"),
  item("Zaspał. Spóźnił się. (toteż) → Zaspał, {1}.", "toteż się spóźnił|toteż spóźnił się"),
 ], ["R1", "R4", "R6", "R10"]))

exs.append(ex("e7", "Тест в формате экзамена: рекламация", "gaps",
  "Uzupełnij list (styl oficjalny). Wpisz spójnik albo wyraz w nawiasie w odpowiedniej formie. W nawiasie — podpowiedź po rosyjsku.", [
  item("Szanowni Państwo, piszę do Państwa, {1} chciałabym złożyć reklamację. (потому что)", "ponieważ|gdyż"),
  item("Dwa tygodnie temu kupiłam w Państwa sklepie pralkę. {1} była nowa, po tygodniu przestała działać. (хотя)", Z),
  item("Dzwoniłam do serwisu, {1} nikt nie odbierał. (но)", "ale|lecz"),
  item("Mimo {1} (wiele prób) nie udało mi się z nikim porozmawiać.", "wielu prób"),
  item("{1} nie mam pralki, muszę prać u sąsiadki. (поскольку)", "Ponieważ"),
  item("Z powodu {1} (awaria) musiałam przełożyć urlop,", "awarii"),
  item("{1} cały tydzień czekałam na technika. (так как)", "ponieważ|gdyż"),
  item("Technik w końcu przyszedł, {1} nie naprawił pralki, (однако)", "jednak|ale|lecz"),
  item("{1} nie miał potrzebnej części. (так как)", "ponieważ|gdyż"),
  item("{1} proszę o wymianę pralki na nową. (поэтому)", "Dlatego|Zatem"),
  item("Mam nadzieję, że dzięki {1} (Państwa szybka reakcja) sprawa zostanie szybko załatwiona.", "Państwa szybkiej reakcji"),
  item("{1} wszystko jestem zadowolona z wcześniejszych zakupów w Państwa sklepie. Z poważaniem, Anna Nowak (несмотря на)", "Mimo|Pomimo"),
 ], ["R1", "R2", "R4", "R5", "R6", "R8", "R9", "R10"], fmt="exam-text"))

exs.append(ex("e8", "Przekształcenia", "gaps", "Перестройте предложение, сохранив смысл. Напечатайте пропущенную часть.", [
  item("Ponieważ padał deszcz, mecz odwołano. → Mecz odwołano z powodu {1}.", "deszczu"),
  item("Chociaż był zmęczony, skończył pracę. → Mimo {1} skończył pracę.", "zmęczenia"),
  item("Mimo choroby poszła do pracy. → Mimo że {1}, poszła do pracy.", "była chora|chorowała"),
  item("Zdałem egzamin, bo mi pomogłeś. → Zdałem egzamin dzięki {1}.", "twojej pomocy|tobie"),
  item("Ponieważ był korek, spóźniliśmy się. → Spóźniliśmy się przez {1}.", "korek"),
  item("Mimo złej pogody pojechaliśmy nad morze. → {1} pogoda była zła, pojechaliśmy nad morze.", Z),
  item("Był zmęczony, więc poszedł spać. → Poszedł spać, {1} był zmęczony.", C),
  item("Nie mam czasu, dlatego nie przyjdę. → {1} nie mam czasu, nie przyjdę.", "Ponieważ"),
 ], ["R1", "R4", "R5", "R6", "R8"], fmt="rewrite"))

exs.append({"id": "w1", "kind": "writing", "title": "Рекламация", "facts": ["R1", "R2", "R4", "R5", "R6"],
  "instr": "Napisz list z reklamacją (100–120 słów) do biura podróży: wycieczka nie była taka, jak w ofercie. Opisz problemy, ich przyczyny i skutki, napisz, czego oczekujesz.",
  "checklist": ["официальные союзы: ponieważ, gdyż, zatem", "1 конструкция z powodu + D.", "1 уступка: chociaż / mimo że / mimo + D.", "dlatego / więc для следствия", "без bo в начале предложения"]})
exs.append({"id": "w2", "kind": "writing", "title": "Работа из дома: за и против", "facts": ["R1", "R6", "R8", "R9", "R10"],
  "instr": "Napisz wpis na forum (80–100 słów): czy praca zdalna jest lepsza od pracy w biurze? Podaj argumenty za i przeciw, napisz swoje zdanie.",
  "checklist": ["2 причины (bo, ponieważ)", "2 уступки (chociaż, mimo + D.)", "1 mimo to / jednak", "1 dzięki + C.", "вывод с więc / dlatego"]})

topic = {"id": "spojniki-przyczyna-przyzwolenie", "num": 19, "title": "Bo, ponieważ, więc, chociaż, mimo: причина, следствие, уступка", "level": "B1",
  "lang": "ru", "prev": "zaimki-nieokreslone", "next": None,
  "summary": "Союзы причины (bo, ponieważ, gdyż, dlatego że), следствия (więc, dlatego, zatem), уступки (chociaż, mimo że, mimo + D., mimo to) и противопоставления (ale, lecz, jednak); стиль и пунктуация.",
  "sections": sections, "exercises": exs}
save("spojniki-przyczyna-przyzwolenie", extract, topic)
