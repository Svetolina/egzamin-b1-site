import sys; sys.path.insert(0, '/home/claude/build')
from lib import S, item, ex, save

EC = "https://elon.io/grammar/polish/adjectives/comparison/comparative"
ES = "https://elon.io/grammar/polish/adjectives/comparison/superlative"
EA = "https://elon.io/grammar/polish/adverbs/comparison"
EN = "https://elon.io/grammar/polish/choosing/niz-vs-od-comparison"
ECC = "https://elon.io/grammar/polish/syntax/comparative-clauses"
PIA = "https://polski.info/grammar/adjectives"
PIV = "https://polski.info/grammar/adverbs"
PD = "https://polskidaily.eu/wp-content/uploads/2021/02/stopniowanie-przymiotnikow.pdf"
WM = "https://en.wikipedia.org/wiki/Polish_morphology"
DZA = "https://faculty.washington.edu/dziwirek/grammar/verbs/polish-adverb-form.pdf"
DZM = "https://faculty.washington.edu/dziwirek/grammar/nouns/polish-MPplural.pdf"
VA = "https://vaia.com/en-us/explanations/polish/polish-grammar/polish-comparatives-and-superlatives"

ec = lambda l: S("elon.io — «The Comparative: -szy / bardziej»", EC, l)
pia = lambda l: S("polski.info — «Adjectives» (раздел Comparison of adjectives)", PIA, l)
piv = lambda l: S("polski.info — «Adverbs» (раздел о stopniowaniu)", PIV, l)
pd = lambda l: S("Polski Daily — «Stopniowanie przymiotników» (PDF)", PD, l)
wm = lambda l: S("Wikipedia (en) — «Polish morphology»", WM, l)
ea = lambda l: S("elon.io — «Comparative and Superlative Adverbs»", EA, l)

F = [
 ("R1", "Простая сравнительная степень: одна согласная перед -y/-i → -szy (stary → starszy, młody → młodszy, nowy → nowszy); две согласные → -ejszy (nudny → nudniejszy, ładny → ładniejszy, trudny → trudniejszy). Превосходная = naj- + сравнительная: najstarszy, najładniejszy.",
  [pia("подраздел regular comparison: «one consonant + -szy», «two consonants + -ejszy»"), ec("разделы «-szy after a single consonant», «-ejszy after consonant clusters»"), pd("раздел Regular forms: młodszy, ładniejszy"), wm("adjective comparison: «-szy or -iejszy»")]),
 ("R2", "Чередования: ł → l (miły → milszy, ciepły → cieplejszy, wesoły → weselszy), n → ń (tani → tańszy), g → ż (drogi → droższy, długi → dłuższy); суффикс -k-/-ok-/-ek- выпадает: szybki → szybszy, niski → niższy, wysoki → wyższy, bliski → bliższy, daleki → dalszy, głęboki → głębszy; ciężki → cięższy, lekki → lżejszy.",
  [pd("разделы «Consonant alternations», «Ending reduction»"), ec("раздел «Stem alternations»"), pia("подразделы «Alternations in single-/two-consonant stems»: wysoki → wyższy")]),
 ("R3", "Неправильные: dobry → lepszy → najlepszy; zły → gorszy → najgorszy; duży → większy → największy; mały → mniejszy → najmniejszy.",
  [ec("раздел «Irregular forms»"), pd("раздел Irregular"), pia("подраздел «Irregular comparison of adjectives»"), S("Vaia — «Polish Comparatives and Superlatives»", VA, "раздел irregular: lepszy, większy, mniejszy, gorszy")]),
 ("R4", "Описательная степень bardziej / najbardziej (и mniej / najmniej) — для длинных прилагательных (4+ слога), прилагательных от глаголов и причастий, ряда заимствований: bardziej interesujący, najbardziej zmęczony, mniej irytujący.",
  [pia("подраздел analytical comparison: 4+ слога → bardziej / najbardziej"), ec("раздел «bardziej (analytic comparative)»"), pd("раздел Descriptive: bardziej interesujący, mniej irytujący"), wm("«bardziej and najbardziej are used before the adjective»")]),
 ("R5", "Не сравниваются прилагательные материала, происхождения, постоянных признаков: drewniany, polski, krakowski, martwy.",
  [pd("раздел «Not compared»")]),
 ("R6", "Мужско-личное мн. ч. сравнительной степени: -szy → -si: starsi, młodsi, lepsi, więksi, mniejsi, wyżsi; najlepsi, najmłodsi.",
  [S("K. Dziwirek (University of Washington), «Masculine personal plural»", DZM, "п. 3: «-szy → -si: starszy brat → starsi bracia»"), wm("раздел о чередованиях: «starszy → starsi»")]),
 ("R7", "«Чем»: niż + тот же падеж, что у первого члена (Ewa jest młodsza niż Marek; Lubię herbatę bardziej niż kawę); od + dopełniacz (wyższy od brata, starszy ode mnie). Только niż — перед придаточным (trudniejsze, niż myślałem), наречием (lepiej niż wczoraj) и количеством (dłużej niż godzinę).",
  [S("elon.io — «niż vs od: Two Ways to Say ‘Than’»", EN, "весь раздел"), piv("примеры «Latem jest cieplej niż zimą», «Magda mówi po polsku lepiej od Nazara»"), ec("примеры wyższy od brata, starszy ode mnie")]),
 ("R8", "Превосходная степень с группой: z + dopełniacz (najlepszy z całej klasy), с местом: w + miejscownik (najwyższa góra w Polsce).",
  [S("elon.io — «The Superlative: naj- + Comparative»", ES, "примеры «najlepszy z całej klasy», «najwyższa góra w Polsce»"), S("Vaia — «Polish Comparatives and Superlatives»", VA, "пример «najszybszą biegaczką w szkole»")]),
 ("R9", "Наречия: сравнительная на -ej, часто с чередованием; превосходная naj- + сравнительная: szybko → szybciej, wolno → wolniej, tanio → taniej, ciepło → cieplej, drogo → drożej, wysoko → wyżej, daleko → dalej, krótko → krócej, jasno → jaśniej, późno → później, trudno → trudniej.",
  [piv("подразделы regular comparison и alternations"), ea("раздел «Comparative with -ej»"), wm("adverb comparison: «-iej», naj-"), S("K. Dziwirek, «Adverb formation»", DZA, "пример inteligentnie → inteligentniej")]),
 ("R10", "Неправильные наречия: dobrze → lepiej → najlepiej; źle → gorzej → najgorzej; dużo → więcej → najwięcej; mało → mniej → najmniej. После więcej/mniej существительное — в dopełniaczu (więcej czasu).",
  [piv("подраздел irregular comparison"), ea("раздел «Irregular comparatives»: «Potrzebuję więcej czasu»"), S("K. Dziwirek, «Adverb formation»", DZA, "irregular: lepiej, gorzej, więcej, mniej")]),
 ("R11", "coraz + сравнительная — «всё более»: Mam coraz więcej pracy.",
  [piv("Comparison expressions: «Mam coraz więcej pracy»")]),
 ("R12", "im + сравнительная …, tym + сравнительная — «чем…, тем…»: Im szybciej skończymy, tym wcześniej wyjdziemy.",
  [S("elon.io — «Comparative and Result Clauses: tak… jak, taki… jak, im… tym»", ECC, "раздел im … tym")]),
]
extract = {"topic": "stopniowanie", "title": "Stopniowanie przymiotników i przysłówków", "facts": [
    {"id": i, "rule": r, "sources": s} for i, r, s in F]}
for f in extract["facts"]:
    if len(f["sources"]) < 2:
        f["single_source_note"] = "Подтверждено одним источником — дано одной строкой с пометкой."

sections = [
 {"id": "s1", "title": "Три степени", "facts": ["R1"],
  "body": "Stopień równy (stary) → wyższy (starszy) → najwyższy (najstarszy). Превосходная всегда = **naj- + сравнительная**.",
  "table": {"head": ["Równy", "Wyższy", "Najwyższy"], "rows": [["stary", "starszy", "najstarszy"], ["nowy", "nowszy", "najnowszy"], ["ładny", "ładniejszy", "najładniejszy"], ["trudny", "trudniejszy", "najtrudniejszy"]]}},
 {"id": "s2", "title": "-szy или -ejszy?", "facts": ["R1"],
  "body": "Смотрим на согласные перед окончанием: **одна** → -szy (sta**r**y → starszy, mło**d**y → młodszy); **две** → -ejszy (nu**dn**y → nudniejszy, ła**dn**y → ładniejszy). Есть исключения: ciekawy → ciekawszy."},
 {"id": "s3", "title": "Чередования", "facts": ["R2"],
  "table": {"head": ["Изменение", "Примеры"], "rows": [
     ["ł → l", "miły → milszy, ciepły → cieplejszy, wesoły → weselszy"],
     ["n → ń", "tani → tańszy"], ["g → ż", "drogi → droższy, długi → dłuższy"],
     ["-k- выпадает", "szybki → szybszy, daleki → dalszy, głęboki → głębszy"],
     ["-sk- → -ż-", "niski → niższy, wysoki → wyższy, bliski → bliższy"],
     ["особые", "ciężki → cięższy, lekki → lżejszy"]]},
  "note": "Такие формы лучше запоминать как слова."},
 {"id": "s4", "title": "Неправильные формы", "facts": ["R3", "R10"],
  "table": {"head": ["Прилагательное", "Наречие"], "rows": [
     ["dobry → lepszy → najlepszy", "dobrze → lepiej → najlepiej"], ["zły → gorszy → najgorszy", "źle → gorzej → najgorzej"],
     ["duży → większy → największy", "dużo → więcej → najwięcej"], ["mały → mniejszy → najmniejszy", "mało → mniej → najmniej"]]},
  "note": "После więcej / mniej — dopełniacz: więcej czasu, mniej pieniędzy."},
 {"id": "s5", "title": "bardziej / najbardziej", "facts": ["R4", "R5"],
  "body": "Для длинных слов (4+ слога), прилагательных от глаголов и причастий: *bardziej interesujący, najbardziej zmęczony*. Меньшая степень: *mniej / najmniej*. Изобретать формы вроде *zmęczeńszy* нельзя.\n\nНе сравниваются: *drewniany, polski, krakowski, martwy* (материал, происхождение; правило из одного источника)."},
 {"id": "s6", "title": "Мужско-личное мн. ч.: -si", "facts": ["R6"],
  "body": "О мужчинах и смешанных группах: **-szy → -si**.",
  "examples": [["Moi bracia są młodsi ode mnie.", "Мои братья младше меня."], ["Ci studenci są lepsi od tamtych.", "Эти студенты лучше тех."], ["Zawodnicy są wyżsi od nas.", "Спортсмены выше нас."]],
  "note": "Сравните: siostry są młodsze, książki są lepsze."},
 {"id": "s7", "title": "Наречия: -ej", "facts": ["R9", "R10"],
  "table": {"head": ["Równy", "Wyższy", "Najwyższy"], "rows": [
     ["szybko", "szybciej", "najszybciej"], ["wolno", "wolniej", "najwolniej"], ["tanio", "taniej", "najtaniej"],
     ["ciepło", "cieplej", "najcieplej"], ["drogo", "drożej", "najdrożej"], ["wysoko", "wyżej", "najwyżej"],
     ["daleko", "dalej", "najdalej"], ["krótko", "krócej", "najkrócej"], ["późno", "później", "najpóźniej"]]}},
 {"id": "s8", "title": "niż или od?", "facts": ["R7"],
  "body": "**niż** — после него тот же падеж, что у первого сравниваемого: *Ewa jest młodsza niż Marek. Lubię herbatę bardziej niż kawę.*\n**od + dopełniacz** — коротко и разговорно: *Ewa jest młodsza od Marka. Brat jest wyższy ode mnie.*\nТолько **niż**: перед придаточным (*trudniejsze, niż myślałem*), наречием (*lepiej niż wczoraj*), количеством (*dłużej niż godzinę*).",
  "note": "Как в русском «старше Марека» — od + dopełniacz; «старше, чем Марек» — niż + mianownik."},
 {"id": "s9", "title": "Самый… из / в", "facts": ["R8"],
  "examples": [["Jest najlepszy z całej klasy.", "Он лучший во всём классе (из всего класса)."], ["To najwyższa góra w Polsce.", "Это самая высокая гора в Польше."]]},
 {"id": "s10", "title": "coraz…; im…, tym…", "facts": ["R11", "R12"],
  "body": "*coraz* + сравнительная — «всё более»: *Mam coraz więcej pracy.* *im* …, *tym* … — «чем…, тем…»: *Im szybciej skończymy, tym wcześniej wyjdziemy.* (Каждое из этих правил подтверждено одним источником.)"},
]

exs = []
comp = [("stary", "starszy"), ("młody", "młodszy"), ("nowy", "nowszy"), ("ładny", "ładniejszy"), ("trudny", "trudniejszy"),
        ("ważny", "ważniejszy"), ("ciepły", "cieplejszy"), ("miły", "milszy"), ("tani", "tańszy"), ("drogi", "droższy"),
        ("długi", "dłuższy"), ("wysoki", "wyższy"), ("niski", "niższy"), ("szybki", "szybszy"), ("bliski", "bliższy"),
        ("daleki", "dalszy"), ("dobry", "lepszy"), ("zły", "gorszy"), ("duży", "większy"), ("mały", "mniejszy"),
        ("ciekawy", "ciekawszy"), ("lekki", "lżejszy"), ("ciężki", "cięższy"), ("głęboki", "głębszy")]
exs.append(ex("e1", "Сравнительная степень", "gaps", "Напечатайте сравнительную степень (м. р. ед. ч.).",
  [item(f"{a} → {{1}}", b) for a, b in comp], ["R1", "R2", "R3"]))

exs.append(ex("e2", "Превосходная степень", "gaps", "Поставьте прилагательное в превосходную степень в нужной форме.", [
  item("To jest {1} (dobry) restauracja w mieście.", "najlepsza"),
  item("Wisła to {1} (długi) rzeka w Polsce.", "najdłuższa"),
  item("Rysy to {1} (wysoki) szczyt w Polsce.", "najwyższy"),
  item("Marek jest {1} (młody) z nas.", "najmłodszy"),
  item("To był {1} (zły) dzień w moim życiu.", "najgorszy"),
  item("Kup {1} (tani) bilet.", "najtańszy"),
  item("Warszawa to {1} (duży) miasto w Polsce.", "największe"),
  item("To {1} (ciekawy) książka, jaką czytałam.", "najciekawsza"),
  item("Ten film jest {1} (interesujący) ze wszystkich.", "najbardziej interesujący"),
  item("Ci chłopcy to {1} (mały) uczniowie w szkole.", "najmniejsi"),
  item("Moi {1} (dobry) przyjaciele mieszkają w Gdańsku.", "najlepsi"),
  item("To jest {1} (stary) kościół w mieście.", "najstarszy"),
 ], ["R1", "R3", "R4", "R6", "R8"]))

exs.append(ex("e3", "Сравнение в предложении", "gaps", "Поставьте прилагательное в сравнительную степень и согласуйте его.", [
  item("Moja siostra jest {1} (stary) ode mnie.", "starsza"),
  item("Moi bracia są {1} (młody) ode mnie.", "młodsi"),
  item("Ten pokój jest {1} (ładny) niż tamten.", "ładniejszy"),
  item("Dzisiejszy dzień jest {1} (ciepły) niż wczorajszy.", "cieplejszy"),
  item("Nowe mieszkanie jest {1} (duży) od starego.", "większe"),
  item("Ci studenci są {1} (dobry) od tamtych.", "lepsi"),
  item("Te buty są {1} (drogi) niż tamte.", "droższe"),
  item("Nasi nowi sąsiedzi są {1} (miły) niż poprzedni.", "milsi"),
  item("Pociąg jest {1} (szybki) od autobusu.", "szybszy"),
  item("Ta walizka jest {1} (lekki) od mojej.", "lżejsza"),
  item("Ci koszykarze są {1} (wysoki) od nas.", "wyżsi"),
  item("To zadanie jest {1} (trudny), niż myślałem.", "trudniejsze"),
 ], ["R1", "R2", "R3", "R6"]))

exs.append(ex("e4", "Наречия", "gaps", "Поставьте наречие в сравнительную (или, где сказано, превосходную) степень.", [
  item("Mów {1} (wolno), proszę.", "wolniej"),
  item("Pociągiem jedzie się {1} (szybko) niż autobusem.", "szybciej"),
  item("Dzisiaj czuję się {1} (dobrze) niż wczoraj.", "lepiej"),
  item("W nocy było jeszcze {1} (źle).", "gorzej"),
  item("Latem jest {1} (ciepło) niż zimą.", "cieplej"),
  item("W tym sklepie jest {1} (tanio).", "taniej"),
  item("W centrum mieszka się {1} (drogo).", "drożej"),
  item("Wróciłem {1} (późno), niż planowałem.", "później"),
  item("Mam {1} (dużo) pracy niż w zeszłym roku.", "więcej"),
  item("Jem teraz {1} (mało) słodyczy.", "mniej"),
  item("Kto z was biega {1} (szybko)? — превосходная", "najszybciej"),
  item("Która kawa smakuje ci {1} (dobrze)? — превосходная", "najlepiej"),
  item("Samolot leci {1} (wysoko) niż ptak.", "wyżej"),
  item("Mieszkam {1} (daleko) od pracy niż ty.", "dalej"),
  item("Coraz {1} (krótko) śpię.", "krócej"),
 ], ["R9", "R10", "R11"]))

exs.append(ex("e5", "niż или od?", "gaps", "Впишите слово в нужной форме или niż / od.", [
  item("Mój brat jest wyższy {1} (od + ja).", "ode mnie"),
  item("Anna jest starsza od {1} (Marek).", "Marka"),
  item("Ewa jest młodsza niż {1} (Marek).", "Marek"),
  item("Lubię herbatę bardziej niż {1} (kawa).", "kawę"),
  item("Pociąg jest szybszy od {1} (autobus).", "autobusu"),
  item("Kraków jest mniejszy od {1} (Warszawa).", "Warszawy"),
  item("Kraków jest mniejszy niż {1} (Warszawa).", "Warszawa"),
  item("Dzisiaj czuję się lepiej {1} wczoraj. (niż / od)", "niż"),
  item("To było trudniejsze, {1} myślałem. (niż / od)", "niż"),
  item("Czekaliśmy dłużej {1} godzinę. (niż / od)", "niż"),
  item("Moja córka jest wyższa od {1} (syn).", "syna"),
  item("Lepiej późno {1} wcale. (niż / od)", "niż"),
 ], ["R7"]))

exs.append(ex("e6", "Простая или описательная?", "gaps",
  "Напечатайте сравнительную степень: простую (-szy/-ejszy) или с bardziej. Где в живой речи возможны обе — засчитываются обе.", [
  item("interesujący → {1}", "bardziej interesujący"),
  item("zmęczony → {1}", "bardziej zmęczony"),
  item("romantyczny → {1}", "bardziej romantyczny"),
  item("ładny → {1}", "ładniejszy"),
  item("zadowolony → {1}", "bardziej zadowolony"),
  item("irytujący → {1}", "bardziej irytujący"),
  item("spokojny → {1}", "spokojniejszy|bardziej spokojny"),
  item("nowoczesny → {1}", "nowocześniejszy|bardziej nowoczesny"),
  item("stary → {1}", "starszy"),
  item("zmęczony → (меньше) {1}", "mniej zmęczony"),
 ], ["R4", "R1"]))

exs.append(ex("e7", "Тест в формате экзамена: письмо", "gaps",
  "Uzupełnij e-mail. Wpisz przymiotnik lub przysłówek w odpowiednim stopniu i formie.", [
  item("Cześć Basiu! Od miesiąca mieszkamy w nowym mieszkaniu. Jest {1} (duży) od starego", "większe"),
  item("i dużo {1} (jasny),", "jaśniejsze"),
  item("bo ma {1} (dużo) okien.", "więcej"),
  item("Niestety jest też {1} (drogi),", "droższe"),
  item("ale czynsz jest {1} (niski), niż się baliśmy.", "niższy"),
  item("Do pracy mam teraz {1} (daleko),", "dalej"),
  item("ale autobus jeździ {1} (szybko).", "szybciej"),
  item("Dzieci mówią, że to {1} (dobry) mieszkanie, w jakim mieszkały.", "najlepsze"),
  item("Ich nowa szkoła jest {1} (mały) od poprzedniej,", "mniejsza"),
  item("ale nauczyciele są {1} (miły).", "milsi"),
  item("Sąsiedzi też są {1} (spokojny) od poprzednich.", "spokojniejsi|bardziej spokojni"),
  item("Czujemy się tu coraz {1} (dobrze). Ściskam, Ewa", "lepiej"),
 ], ["R1", "R2", "R3", "R6", "R9", "R10", "R11"], fmt="exam-text"))

exs.append(ex("e8", "Przekształcenia", "gaps", "Перестройте предложение, сохранив смысл. Напечатайте продолжение.", [
  item("Marek jest wyższy niż Piotr. → Piotr jest {1}.", "niższy niż Marek|niższy od Marka"),
  item("Anna jest starsza od Ewy. → Ewa jest {1}.", "młodsza od Anny|młodsza niż Anna"),
  item("Nikt w klasie nie pisze lepiej niż Kasia. → Kasia pisze {1}.", "najlepiej w klasie|najlepiej z całej klasy|najlepiej z klasy"),
  item("Pociąg jedzie dwie godziny, a autobus trzy. → Pociąg jedzie {1} niż autobus.", "krócej|szybciej"),
  item("Ten hotel jest tańszy od tamtego. → Tamten hotel jest {1}.", "droższy od tego|droższy niż ten"),
  item("Żadna rzeka w Polsce nie jest dłuższa od Wisły. → Wisła jest {1}.", "najdłuższą rzeką w Polsce|najdłuższa w Polsce"),
  item("Z roku na rok mam więcej pracy. → Mam {1} pracy.", "coraz więcej"),
  item("Ten film jest mniej ciekawy niż książka. → Książka jest {1} niż film.", "ciekawsza|bardziej ciekawa"),
 ], ["R1", "R3", "R7", "R8", "R9", "R11"], fmt="rewrite"))

exs.append({"id": "w1", "kind": "writing", "title": "Город или деревня?", "facts": ["R1", "R3", "R7", "R9"],
  "instr": "Napisz tekst na forum (80–100 słów): gdzie lepiej mieszkać — w dużym mieście czy na wsi? Porównaj ceny, transport, pracę, spokój i przyrodę. Napisz, co wybierasz i dlaczego.",
  "checklist": ["не меньше 5 форм сравнительной степени", "хотя бы 1 неправильная (lepszy, więcej, gorzej)", "хотя бы 1 сравнение с niż и 1 с od", "1 превосходная степень", "coraz или im…tym"]})
exs.append({"id": "w2", "kind": "writing", "title": "Какой отель выбрать", "facts": ["R1", "R4", "R8", "R6"],
  "instr": "Napisz e-mail do znajomych (80–100 słów), którzy jadą do Krakowa. Porównaj dwa hotele (cena, odległość od centrum, pokoje, obsługa, śniadania) i poleć jeden z nich.",
  "checklist": ["не меньше 4 сравнений", "1 описательная форма (bardziej / mniej …)", "1 мужско-личная форма (pracownicy są milsi)", "1 превосходная с z / w"]})

topic = {"id": "stopniowanie", "num": 14, "title": "Stopniowanie: сравнительная и превосходная степень", "level": "B1",
  "lang": "ru", "prev": "mowa-zalezna", "next": "swoj-siebie",
  "summary": "Степени сравнения прилагательных и наречий: -szy/-ejszy, чередования, неправильные формы, bardziej/najbardziej, мужско-личные формы, niż или od, coraz и im…tym.",
  "sections": sections, "exercises": exs}
save("stopniowanie", extract, topic)
