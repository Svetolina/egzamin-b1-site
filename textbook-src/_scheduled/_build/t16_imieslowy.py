import sys; sys.path.insert(0, '/home/claude/build')
from lib import S, item, ex, save

ZP = "https://zpe.gov.pl/watek/LP17S4zgSJ/7/a/imieslow-przyslowkowy/D8VcRm2NS"
ZR = "https://zpe.gov.pl/a/imieslowy-i-ich-rodzaje/DN28lvu36"
EAC = "https://elon.io/grammar/polish/verbs/participles/contemporary-adverb-ac"
EWS = "https://elon.io/grammar/polish/verbs/participles/anterior-adverb-wszy"
EAA = "https://elon.io/grammar/polish/verbs/participles/active-adjectival"
WIKI = "https://en.wikipedia.org/wiki/Polish_grammar"
KS = "https://wydawnictwo.ur.edu.pl/wp-content/uploads/2020/10/Imieslowy_mniej_klopotliwe.pdf"

zp = lambda l: S("ZPE (MEN) — «Imiesłów przysłówkowy»", ZP, l)
zr = lambda l: S("ZPE (MEN) — «Imiesłowy i ich rodzaje»", ZR, l)
eac = lambda l: S("elon.io — «The Contemporary Verbal Adverb (-ąc)»", EAC, l)
ews = lambda l: S("elon.io — «The Anterior Verbal Adverb (-wszy / -łszy)»", EWS, l)
eaa = lambda l: S("elon.io — «The Active Adjectival Participle (-ący)»", EAA, l)
wiki = lambda l: S("Wikipedia (en) — «Polish grammar»", WIKI, l)

F = [
 ("R1", "Imiesłów przysłówkowy współczesny на -ąc образуется только от глаголов несовершенного вида и обозначает действие, одновременное с главным: Czytając gazetę, pił kawę.",
  [zp("раздел о imiesłowie współczesnym"), zr("раздел imiesłów przysłówkowy współczesny"), eac("разделы Formation, Imperfective only"), wiki("Participles: present adverbial participle — imperfective only, śpiewając")]),
 ("R2", "Образование -ąc: 3-е л. мн. ч. настоящего времени + -c: czytają → czytając, robią → robiąc, idą → idąc, piszą → pisząc.",
  [zp("«czytają → czytając»"), eac("раздел Formation: robią → robiąc, idą → idąc")]),
 ("R3", "być → będąc (от основы будущего будę): Będąc w Krakowie, odwiedź Wawel.",
  [eac("раздел Formation: «Być is irregular: będąc»")]),
 ("R4", "Imiesłów przysłówkowy uprzedni на -wszy / -łszy образуется только от глаголов совершенного вида и обозначает действие, завершившееся до главного: Przeczytawszy list, zadzwoniła do matki.",
  [zp("раздел о imiesłowie uprzednim"), zr("«od czasowników dokonanych … wyłącznie imiesłowy uprzednie»"), ews("разделы Formation, Meaning"), wiki("past active participle: zabiwszy, perfective only")]),
 ("R5", "Образование: прош. вр. м. р. без -ł; после гласной + -wszy (zrobił → zrobiwszy, przeczytał → przeczytawszy, napisał → napisawszy), после согласной + -łszy (zjadł → zjadłszy, przyszedł → przyszedłszy, przyniósł → przyniósłszy).",
  [ews("раздел Formation"), zp("примеры przeczytawszy, przyniósłszy"), zr("примеры napisawszy, zmókłszy")]),
 ("R6", "Imiesłowy przysłówkowe не изменяются (как наречия): skończywszy, czytając — для любого рода и числа.",
  [zp("«Imiesłowy przysłówkowe tak jak przysłówek nie podlegają odmianie»"), ews("«The form is indeclinable»"), wiki("«this form is invariant»")]),
 ("R7", "Общее подлежащее: действие причастия выполняет подлежащее главного предложения. Ошибка: *Idąc do szkoły, padał deszcz*. Правильно: Idąc do szkoły, zmokłem.",
  [zp("раздел «Wspólny podmiot», пример с rzeką"), eac("раздел Same-subject rule"), ews("раздел Same subject")]),
 ("R8", "Оборот с imiesłowem przysłówkowym (imiesłowowy równoważnik zdania) выделяется запятыми.",
  [zp("раздел «Przecinek»: «Anna, czekając na tramwaj, …»"), zr("«A comma always…» — przecinek przy imiesłowach przysłówkowych")]),
 ("R9", "nie с imiesłowem przysłówkowym пишется раздельно: nie wiedząc, nie czytając, nie przeczytawszy.",
  [zp("раздел «Pisownia nie»"), S("K. Strycharz, «Imiesłowy mniej kłopotliwe», Gazeta Uniwersytecka (Uniwersytet Rzeszowski) nr 1/32, 2005", KS, "«z imiesłowami przysłówkowymi … obowiązuje pisownia rozdzielna»")]),
 ("R10", "Стиль: -ąc — книжная/официальная форма (в разговоре чаще kiedy/gdy + глагол), но устойчивые обороты (mówiąc szczerze) обычны и в речи; -wszy — очень книжная, в разговоре почти не употребляется.",
  [eac("раздел Register"), ews("раздел Register")]),
 ("R11", "Imiesłów przymiotnikowy czynny на -ący (czytający, -ąca, -ące) — от несовершенного вида, склоняется как прилагательное и заменяет придаточное с który: kobieta czytająca książkę = kobieta, która czyta książkę. В отличие от -ąc он относится к существительному.",
  [eaa("разделы Formation, Declension, Difference from -ąc"), zr("раздел imiesłów przymiotnikowy czynny"), wiki("present adjectival participle śpiewający")]),
]
extract = {"topic": "imieslowy-przyslowkowe", "title": "Imiesłowy przysłówkowe (-ąc, -wszy) и -ący", "facts": [
    {"id": i, "rule": r, "sources": s} for i, r, s in F]}
for f in extract["facts"]:
    if len(f["sources"]) < 2:
        f["single_source_note"] = "Подтверждено одним источником — дано одной строкой с пометкой."
extract["facts"][9]["note"] = "Оба источника — разные страницы одного сайта (elon.io); стилистическое правило, не грамматическое."

sections = [
 {"id": "s1", "title": "Два деепричастия", "facts": ["R1", "R4", "R6"],
  "body": "Польские imiesłowy przysłówkowe — это русские деепричастия:",
  "table": {"head": ["", "-ąc (współczesny)", "-wszy / -łszy (uprzedni)"], "rows": [
     ["русский аналог", "читая", "прочитав"], ["вид глагола", "несовершенный", "совершенный"],
     ["время действия", "одновременно с главным", "до главного"], ["пример", "Czytając gazetę, pił kawę.", "Przeczytawszy list, zadzwoniła do matki."]]},
  "note": "Не изменяются по роду и числу: Wszedłszy do domu, zdjęła buty (о женщине — та же форма)."},
 {"id": "s2", "title": "Как образовать -ąc", "facts": ["R2", "R3"],
  "body": "Берём форму **oni** настоящего времени и добавляем **-c**.",
  "table": {"head": ["Инфинитив", "oni", "-ąc"], "rows": [
     ["czytać", "czytają", "czytając"], ["pisać", "piszą", "pisząc"], ["iść", "idą", "idąc"],
     ["jechać", "jadą", "jadąc"], ["pić", "piją", "pijąc"], ["jeść", "jedzą", "jedząc"], ["spać", "śpią", "śpiąc"],
     ["być", "(będą)", "będąc"]]},
  "note": "być → będąc — особая форма (одним источником)."},
 {"id": "s3", "title": "Как образовать -wszy / -łszy", "facts": ["R5"],
  "body": "Берём прошедшее время м. р. (**on**) и убираем **-ł**: осталась гласная → **-wszy**, согласная → **-łszy**.",
  "table": {"head": ["Инфинитив", "on", "uprzedni"], "rows": [
     ["zrobić", "zrobił", "zrobiwszy"], ["przeczytać", "przeczytał", "przeczytawszy"], ["skończyć", "skończył", "skończywszy"],
     ["zjeść", "zjadł", "zjadłszy"], ["przyjść", "przyszedł", "przyszedłszy"], ["przynieść", "przyniósł", "przyniósłszy"]]}},
 {"id": "s4", "title": "Главное правило: одно подлежащее", "facts": ["R7"],
  "body": "Деепричастие относится к подлежащему главного предложения — как и в русском.",
  "table": {"head": ["Ошибка", "Правильно"], "rows": [
     ["Idąc do szkoły, padał deszcz.", "Idąc do szkoły, zmokłem. / Kiedy szedłem do szkoły, padał deszcz."],
     ["Czytając książkę, zadzwonił telefon.", "Kiedy czytałam książkę, zadzwonił telefon."]]},
  "note": "Сравните ошибку «Подъезжая к станции, у меня слетела шляпа» в русском."},
 {"id": "s5", "title": "Запятая и nie", "facts": ["R8", "R9"],
  "body": "Оборот выделяется **запятыми**: *Anna, czekając na tramwaj, denerwowała się.* **nie** — раздельно: *nie wiedząc, nie czytając, nie przeczytawszy.*"},
 {"id": "s6", "title": "Где это встречается", "facts": ["R10"],
  "body": "-ąc — книжный и официальный стиль (тексты экзамена, новости, письма); в разговоре обычно говорят *kiedy / gdy* + глагол. Обиходные обороты: *mówiąc szczerze, biorąc pod uwagę*. -wszy — почти только в литературе: важно **понимать** при чтении."},
 {"id": "s7", "title": "-ąc или -ący?", "facts": ["R11"],
  "body": "**-ący** (czytający, czytająca, czytające) — причастие-прилагательное: относится к существительному, склоняется и заменяет *który*: *Kobieta czytająca książkę = kobieta, która czyta książkę.* **-ąc** — деепричастие: относится к действию, не меняется.",
  "examples": [["Śpiące dziecko wyglądało jak aniołek.", "Спящий ребёнок выглядел как ангелочек."], ["Czytając, zasnął.", "Читая, он уснул."]]},
]

def kiedy(base_m, base_f, rest):
    out = []
    for c in ("Kiedy", "Gdy"):
        out += [f"{c} {base_m} {rest}".strip(), f"{c} {base_f} {rest}".strip()]
    return "|".join(out)

exs = []
ac = [("czytać", "czytając"), ("pisać", "pisząc"), ("robić", "robiąc"), ("iść", "idąc"), ("jechać", "jadąc"), ("mówić", "mówiąc"),
      ("słuchać", "słuchając"), ("pić", "pijąc"), ("jeść", "jedząc"), ("siedzieć", "siedząc"), ("uśmiechać się", "uśmiechając się"),
      ("wracać", "wracając"), ("patrzeć", "patrząc"), ("myśleć", "myśląc"), ("być", "będąc"), ("czekać", "czekając"),
      ("prowadzić", "prowadząc"), ("spać", "śpiąc")]
exs.append(ex("e1", "Образуйте форму на -ąc", "gaps", "Напечатайте imiesłów przysłówkowy współczesny.",
  [item(f"{a} → {{1}}", b) for a, b in ac], ["R2", "R3"]))
ws = [("zrobić", "zrobiwszy"), ("przeczytać", "przeczytawszy"), ("napisać", "napisawszy"), ("skończyć", "skończywszy"),
      ("zjeść", "zjadłszy"), ("przyjść", "przyszedłszy"), ("wejść", "wszedłszy"), ("wrócić", "wróciwszy"), ("zamknąć", "zamknąwszy"),
      ("obudzić się", "obudziwszy się"), ("kupić", "kupiwszy"), ("wypić", "wypiwszy"), ("przynieść", "przyniósłszy"), ("usiąść", "usiadłszy")]
exs.append(ex("e2", "Образуйте форму на -wszy / -łszy", "gaps", "Напечатайте imiesłów przysłówkowy uprzedni (подсказка: от формы «on» прошедшего времени).",
  [item(f"{a} → {{1}}", b) for a, b in ws], ["R5"]))

exs.append(ex("e3", "-ąc или -wszy?", "gaps", "Поставьте глагол в форму -ąc (одновременно) или -wszy/-łszy (раньше).", [
  item("{1} (czytać) gazetę, pił kawę.", "Czytając"),
  item("{1} (zjeść) obiad, wyszedł na spacer.", "Zjadłszy"),
  item("{1} (wracać) do domu, spotkałam sąsiadkę.", "Wracając"),
  item("{1} (przeczytać) list, zadzwoniła do matki.", "Przeczytawszy"),
  item("{1} (słuchać) muzyki, gotuję obiad.", "Słuchając"),
  item("{1} (skończyć) pracę, poszliśmy do kina.", "Skończywszy"),
  item("Szedł ulicą, {1} (rozmawiać) przez telefon.", "rozmawiając"),
  item("{1} (być) w Krakowie, odwiedź Wawel.", "Będąc"),
  item("{1} (wejść) do pokoju, zapalił światło.", "Wszedłszy"),
  item("Dzieci bawiły się, {1} (śmiać się) głośno.", "śmiejąc się"),
  item("{1} (mówić) szczerze, nie lubię tego filmu.", "Mówiąc"),
  item("{1} (wrócić) z pracy, zjadła kolację.", "Wróciwszy"),
 ], ["R1", "R4", "R6"]))

exs.append(ex("e4", "Исправьте ошибку", "gaps",
  "В предложении разные подлежащие — деепричастие тут нельзя. Замените его на kiedy/gdy + глагол (говорит «я»; засчитываются обе формы рода).", [
  item("Idąc do szkoły, padał deszcz. → {1}, padał deszcz.", kiedy("szedłem", "szłam", "do szkoły")),
  item("Jadąc autobusem, zepsuł się silnik. → {1}, zepsuł się silnik.", kiedy("jechałem", "jechałam", "autobusem")),
  item("Czytając książkę, zadzwonił telefon. → {1}, zadzwonił telefon.", kiedy("czytałem", "czytałam", "książkę")),
  item("Wchodząc do sklepu, zaczęła się burza. → {1}, zaczęła się burza.", kiedy("wchodziłem", "wchodziłam", "do sklepu")),
  item("Będąc dzieckiem, mama czytała mi bajki. → {1}, mama czytała mi bajki.", kiedy("byłem", "byłam", "dzieckiem")),
  item("Wróciwszy do domu, pies na mnie czekał. → {1}, pies na mnie czekał.", kiedy("wróciłem", "wróciłam", "do domu")),
 ], ["R7"]))

exs.append(ex("e5", "Замените на деепричастие", "gaps", "Подлежащее одно — замените придаточное деепричастием (-ąc или -wszy/-łszy).", [
  item("Kiedy czekała na tramwaj, czytała książkę. → {1}, czytała książkę.", "Czekając na tramwaj"),
  item("Kiedy zjadł śniadanie, wyszedł z domu. → {1}, wyszedł z domu.", "Zjadłszy śniadanie"),
  item("Gdy prowadzę samochód, nie rozmawiam przez telefon. → {1}, nie rozmawiam przez telefon.", "Prowadząc samochód"),
  item("Kiedy skończyła studia, wyjechała do Anglii. → {1}, wyjechała do Anglii.", "Skończywszy studia"),
  item("Kiedy wracaliśmy z kina, rozmawialiśmy o filmie. → {1}, rozmawialiśmy o filmie.", "Wracając z kina"),
  item("Kiedy przeczytał wiadomość, uśmiechnął się. → {1}, uśmiechnął się.", "Przeczytawszy wiadomość"),
  item("Gdy mieszkałem w Polsce, nauczyłem się polskiego. → {1}, nauczyłem się polskiego.", "Mieszkając w Polsce"),
  item("Kiedy otworzyła drzwi, zobaczyła kwiaty. → {1}, zobaczyła kwiaty.", "Otworzywszy drzwi"),
  item("Ponieważ nie wiedział, co robić, zadzwonił do brata. → {1}, co robić, zadzwonił do brata.", "Nie wiedząc"),
  item("Kiedy weszła do domu, zdjęła buty. → {1}, zdjęła buty.", "Wszedłszy do domu"),
 ], ["R1", "R4", "R5", "R6", "R9"]))

exs.append(ex("e6", "-ąc или -ący?", "gaps", "Поставьте глагол в форму -ąc (деепричастие) или -ący (причастие, согласуйте!).", [
  item("Kobieta {1} (czytać) książkę nie zauważyła deszczu.", "czytająca"),
  item("{1} (czytać) książkę, kobieta nie zauważyła deszczu.", "Czytając"),
  item("{1} (spać) dziecko wyglądało jak aniołek.", "Śpiące"),
  item("Znam wielu ludzi {1} (mówić) po polsku.", "mówiących"),
  item("Rozmawiałam z {1} (pracować) tu panią.", "pracującą"),
  item("{1} (pracować) w nocy, śpię w dzień.", "Pracując"),
  item("Studenci {1} (uczyć się) w bibliotece muszą być cicho.", "uczący się"),
  item("Wyszła z domu, nie {1} (mówić) ani słowa.", "mówiąc"),
  item("Przy stole siedział mężczyzna {1} (pić) kawę.", "pijący"),
  item("Lubię patrzeć na {1} (bawić się) dzieci.", "bawiące się"),
 ], ["R11", "R1"]))

exs.append(ex("e7", "Тест в формате экзамена: рассказ", "gaps",
  "Uzupełnij tekst. Wpisz imiesłów przysłówkowy (-ąc albo -wszy/-łszy) od czasownika w nawiasie.", [
  item("Wczoraj, {1} (wracać) z pracy, zobaczyłam na ulicy małego psa.", "wracając"),
  item("{1} (siedzieć) pod drzewem, pies cicho skomlał.", "Siedząc"),
  item("{1} (nie wiedzieć), co zrobić, zadzwoniłam do siostry.", "Nie wiedząc"),
  item("{1} (wysłuchać) mnie, siostra powiedziała: „Weź go do domu!”.", "Wysłuchawszy"),
  item("{1} (wziąć) psa na ręce, poszłam do domu.", "Wziąwszy"),
  item("Mąż, {1} (zobaczyć) nas, bardzo się zdziwił.", "zobaczywszy"),
  item("{1} (umyć) psa,", "Umywszy"),
  item("i {1} (nakarmić) go, zrobiliśmy mu zdjęcie", "nakarmiwszy"),
  item("i, {1} (chcieć) znaleźć właściciela, wrzuciliśmy je do internetu.", "chcąc"),
  item("Następnego dnia zadzwoniła starsza pani, {1} (płakać) ze szczęścia.", "płacząc"),
  item("{1} (przyjechać) po psa, przywiozła nam ciasto.", "Przyjechawszy"),
  item("{1} (mówić) szczerze, trochę żal mi było się z nim rozstać.", "Mówiąc"),
 ], ["R1", "R2", "R4", "R5", "R7", "R9"], fmt="exam-text"))

exs.append(ex("e8", "Przekształcenia", "gaps", "Перестройте на разговорный вариант (kiedy/gdy, ponieważ/bo, który). Напечатайте вставку.", [
  item("Zjadłszy obiad, wyszedł na spacer. → {1}, wyszedł na spacer.", "Kiedy zjadł obiad|Gdy zjadł obiad"),
  item("Czytając gazetę, pił kawę. → {1}, pił kawę.", "Kiedy czytał gazetę|Gdy czytał gazetę"),
  item("Nie mając czasu, nie przyszła na spotkanie. → {1}, nie przyszła na spotkanie.", "Ponieważ nie miała czasu"),
  item("Będąc w Krakowie, odwiedziliśmy Wawel. → {1}, odwiedziliśmy Wawel.", "Kiedy byliśmy w Krakowie|Gdy byliśmy w Krakowie"),
  item("Przeczytawszy list, zadzwoniła do matki. → {1}, zadzwoniła do matki.", "Kiedy przeczytała list|Gdy przeczytała list"),
  item("Mieszkając blisko, chodzę do pracy pieszo. → {1}, chodzę do pracy pieszo.", "Ponieważ mieszkam blisko"),
  item("Kobieta czytająca książkę to moja siostra. → Kobieta, {1}, to moja siostra.", "która czyta książkę"),
  item("Ludzie mieszkający w centrum narzekają na hałas. → Ludzie, {1}, narzekają na hałas.", "którzy mieszkają w centrum"),
 ], ["R1", "R4", "R10", "R11"], fmt="rewrite"))

exs.append({"id": "w1", "kind": "writing", "title": "Необычный день (рассказ)", "facts": ["R1", "R4", "R7", "R8"],
  "instr": "Napisz opowiadanie (80–100 słów): „Dzień, którego nie zapomnę”. Opisz, co się stało, co robiłeś/robiłaś i jak to się skończyło.",
  "checklist": ["не меньше 3 форм на -ąc", "не меньше 2 форм на -wszy/-łszy", "в каждом обороте подлежащее совпадает с главным", "запятые вокруг оборотов", "хотя бы 1 nie + деепричастие раздельно"]})
exs.append({"id": "w2", "kind": "writing", "title": "Советы туристам", "facts": ["R1", "R3", "R10"],
  "instr": "Napisz krótki poradnik dla turystów (60–80 słów) o Twoim mieście: co warto zobaczyć, jak się poruszać, na co uważać.",
  "checklist": ["будąc w …, warto …", "chcąc …, należy …", "1 устойчивый оборот (mówiąc szczerze / biorąc pod uwagę)", "1 форма -ący (osoby lubiące …)"]})

topic = {"id": "imieslowy-przyslowkowe", "num": 16, "title": "Imiesłowy przysłówkowe: -ąc, -wszy (и -ący)", "level": "B1",
  "lang": "ru", "prev": "swoj-siebie", "next": None,
  "summary": "Польские деепричастия: -ąc (одновременно, несов. вид) и -wszy/-łszy (раньше, сов. вид); общее подлежащее, запятые, nie раздельно; отличие от причастия -ący.",
  "sections": sections, "exercises": exs}
save("imieslowy-przyslowkowe", extract, topic)
