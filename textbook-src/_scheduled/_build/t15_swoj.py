import sys; sys.path.insert(0, '/home/claude/build')
from lib import S, item, ex, save

EM = "https://elon.io/grammar/polish/mistakes/swoj-vs-jego"
EJ = "https://elon.io/grammar/polish/pronouns/possessive/jego-jej-ich"
CZ = "https://www.clozemaster.com/blog/polish-possessive-pronouns/"
PD = "https://www.polskidaily.eu/wp-content/uploads/2020/11/B1-Zaimek-swoj.pdf"
ES = "https://elon.io/grammar/polish/pronouns/reflexive/siebie-sobie"
ER = "https://elon.io/grammar/polish/pronouns/each-other/wzajemnie"
WB = "https://de.wikibooks.org/wiki/Polnisch/_Grammatik/_Pronomen/_Reflexivpronomen"
LS = "https://en.langenscheidt.com/polish-german/siebie"
WIKI = "https://en.wikipedia.org/wiki/Polish_grammar"

em = lambda l: S("elon.io — «Confusing swój with mój/jego»", EM, l)
cz = lambda l: S("Clozemaster Blog — «The No-Nonsense Guide to Polish Possessive Pronouns»", CZ, l)
pd = lambda l: S("Polski Daily — «B1: Zaimek swój» (PDF, упражнения + схема)", PD, l)
es = lambda l: S("elon.io — «The Reflexive Pronoun: siebie, sobie, sobą»", ES, l)
er = lambda l: S("elon.io — «Reciprocal Expressions: się, siebie, nawzajem»", ER, l)
wb = lambda l: S("Wikibooks (de) — «Polnisch / Grammatik / Pronomen / Reflexivpronomen»", WB, l)
ls = lambda l: S("Langenscheidt Polish–German — «siebie»", LS, l)

F = [
 ("R1", "swój — «свой»: указывает на владельца, который является подлежащим того же предложения, и согласуется с предметом владения.",
  [em("раздел Core Rule"), cz("раздел о swój: «the subject must be the same as the owner»"), pd("схема: «Kto jest podmiotem?… Czy dopełnienie należy do podmiotu?»")]),
 ("R2", "В 3-м лице выбор меняет смысл: Jan kocha swoją żonę (свою) — Jan kocha jego żonę (жену другого человека). jego/jej/ich — когда владелец не подлежащее: Znam jego siostrę.",
  [em("раздел Third Person"), cz("jego, jej, ich — fixed 3rd person; swój — any person"), pd("ответы упражнений: jej / ich vs swoją / swoim")]),
 ("R3", "swój не бывает в подлежащем: Mój brat mieszka w Krakowie (не *Swój brat). Jego dom jest duży.",
  [em("раздел Subject Position"), pd("схема: если пропуск в подлежащем — «NIE UŻYWAJ ‘SWÓJ’»")]),
 ("R4", "В 1-м и 2-м лице swój предпочтителен в аккуратной речи, mój/twój тоже встречается (особенно в разговоре): Odwiedzam swojego / mojego brata.",
  [em("раздел First and Second Person"), cz("swój «can be used to mean any person»; пример Mam swoje własne problemy")]),
 ("R5", "jego, jej, ich не склоняются и не меняются по роду: jego dom, jego żona, z jego dziećmi.",
  [cz("раздел о 3-м лице: «always stay jej, jego, and ich»"), S("elon.io — «His, Her, Their: jego, jej, ich (Invariable)»", EJ, "весь раздел")]),
 ("R6", "swój склоняется как mój / прилагательное: swój, swoja, swoje; swojego, swojej, swoim, swoją, swoich, swoimi.",
  [em("раздел Declension of swój"), cz("swój «follows the same declension pattern as adjectives», swojego")]),
 ("R7", "siebie — возвратное местоимение без именительного падежа: D. siebie, C. sobie, B. siebie / się, N. sobą, Ms. (o) sobie.",
  [es("таблица Declension"), wb("таблица Reflexivpronomen"), ls("формы sobie, siebie / się, sobą")]),
 ("R8", "siebie / się — одна форма для всех лиц и чисел: myję się, myjesz się, myjemy się; kupiłem sobie, kupiłaś sobie.",
  [es("раздел «Same form for every person»"), S("Wikipedia (en) — «Polish grammar»", WIKI, "Pronouns: «The reflexive pronoun for all persons and numbers is się»")]),
 ("R9", "się — безударная частица при глаголе; после предлога и при логическом ударении — только полная форма: o sobie, dla siebie, ze sobą, do siebie, na sobie, u siebie (у себя дома). Не *o się.",
  [es("разделы «Się vs. siebie», «Prepositions», «Common mistakes»"), er("о sobie, ze sobą, do siebie, na siebie"), ls("фразы dla siebie, ze sobą, na sobie, przed sobą, obok siebie")]),
 ("R10", "sobie (дат. п.) — «себе, для себя»: Kupiłem sobie książkę (не *Kupiłem się książkę*). Nalej sobie kawy.",
  [es("Common mistakes: «Kupiłem się książkę → Kupiłem sobie książkę»"), wb("таблица: Dativ — sobie")]),
 ("R11", "Если речь о самом подлежащем, нужно siebie, а не личное местоимение: Ona myśli tylko o sobie (о себе) — o niej (о другой женщине). Jestem dumny z siebie.",
  [es("Common mistakes: «Ona myśli tylko o niej → o sobie», «Jestem dumny z mnie → z siebie»")]),
 ("R12", "Взаимность: się (kochają się, spotkaliśmy się), а если глагол требует другого падежа или предлога — sobie / siebie / sobą (pomagają sobie, piszą do siebie, rozmawiają ze sobą); усиление — nawzajem / wzajemnie. «Nawzajem!» — «И вам того же!».",
  [er("весь раздел"), ls("ze sobą — «miteinander sprechen»; siebie = «einander»")]),
]
extract = {"topic": "swoj-siebie", "title": "Swój / jego; siebie, sobie, się", "facts": [
    {"id": i, "rule": r, "sources": s} for i, r, s in F]}
for f in extract["facts"]:
    if len(f["sources"]) < 2:
        f["single_source_note"] = "Подтверждено одним источником напрямую (вытекает также из R1 и R8) — дано одной строкой с пометкой."

sections = [
 {"id": "s1", "title": "swój — «свой»", "facts": ["R1", "R2"],
  "body": "**swój** указывает на владельца-подлежащее: *Jan kocha swoją żonę.* Если владелец — кто-то другой, нужны **jego / jej / ich**: *Jan kocha jego żonę* — Ян любит жену другого человека (!).",
  "table": {"head": ["Владелец = подлежащее", "Владелец — другой"], "rows": [
     ["Anna odwiedza swoją babcię.", "Anna odwiedza jej babcię (чужую)."], ["Oni sprzedali swój dom.", "Oni kupili ich dom."], ["Piotr jedzie swoim samochodem.", "Piotr jedzie jego samochodem (чужим)."]]},
  "note": "Как в русском «свой / его»: «Ян любит свою жену» — «его жену»."},
 {"id": "s2", "title": "Где swój нельзя", "facts": ["R3", "R5"],
  "body": "В подлежащем — никогда: ***Mój** brat mieszka w Krakowie. **Jego** dom jest duży.* Не *Swój brat…*.\n\n**jego, jej, ich** не склоняются: *jego dom, jego żona, z jego dziećmi.*"},
 {"id": "s3", "title": "Я и ты: swój или mój?", "facts": ["R4"],
  "body": "С «я», «ты», «мы», «вы» в аккуратной речи лучше **swój**: *Odwiedzam swojego brata.* Форма *mojego* тоже встречается, особенно в разговоре, — ошибкой смысла она не будет. В упражнениях засчитываются обе."},
 {"id": "s4", "title": "Склонение swój", "facts": ["R6"],
  "table": {"head": ["Падеж", "м. р.", "ж. р.", "ср. р.", "мн. ч."], "rows": [
     ["M.", "swój", "swoja", "swoje", "swoi / swoje"], ["D.", "swojego", "swojej", "swojego", "swoich"],
     ["C.", "swojemu", "swojej", "swojemu", "swoim"], ["B.", "swój / swojego", "swoją", "swoje", "swoich / swoje"],
     ["N.", "swoim", "swoją", "swoim", "swoimi"], ["Ms.", "swoim", "swojej", "swoim", "swoich"]]},
  "note": "Склоняется точно как mój (mojego, mojej, moim…)."},
 {"id": "s5", "title": "siebie, sobie, sobą, się", "facts": ["R7", "R8"],
  "table": {"head": ["Падеж", "Форма", "Пример"], "rows": [
     ["M.", "—", "(нет)"], ["D.", "siebie", "dla siebie, do siebie, u siebie"], ["C.", "sobie", "kupiłem sobie"],
     ["B.", "siebie / się", "myję się; patrzę na siebie"], ["N.", "sobą", "ze sobą"], ["Ms.", "sobie", "o sobie, na sobie"]]},
  "body": "Одна форма для всех лиц: *myję się, myjesz się, myjemy się.*"},
 {"id": "s6", "title": "się или siebie?", "facts": ["R9", "R10"],
  "body": "**się** — безударное, стоит при глаголе: *Myję się każdego ranka.* **siebie** — полное: после предлога и при противопоставлении: *Myję tylko siebie.*\n\n**sobie** — «себе»: *Kupiłem sobie książkę. Nalej sobie kawy.*",
  "note": "Ошибки: *o się → o sobie; *Kupiłem się książkę → Kupiłem sobie książkę."},
 {"id": "s7", "title": "o sobie или o niej?", "facts": ["R11"],
  "body": "Если речь о самом подлежащем — **siebie / sobie**: *Ona myśli tylko o sobie.* Личное местоимение означает другого человека: *Ona myśli tylko o niej* — о другой женщине. (Прямо подтверждено одним источником.)"},
 {"id": "s8", "title": "Друг друга", "facts": ["R12"],
  "body": "**się**: *Kochają się. Spotkaliśmy się na lotnisku.* Если глагол требует другого падежа/предлога — **sobie / siebie / sobą**: *Pomagają sobie. Piszą do siebie. Rozmawiają ze sobą.* Усиление — **nawzajem**: *Pomagamy sobie nawzajem.*",
  "note": "«Miłego weekendu!» — «Nawzajem!» (И вам!)."},
]

exs = []
exs.append(ex("e1", "swój или jego / jej / ich?", "gaps", "Впишите swój (в нужной форме) или jego / jej / ich. В скобках — чья вещь.", [
  item("Jan kocha {1} żonę. (жену Яна)", "swoją"),
  item("Jan zna Piotra i {1} żonę. (жену Петра)", "jego"),
  item("Anna odwiedza {1} babcię. (свою)", "swoją"),
  item("Piotr i Ewa sprzedali {1} samochód. (свой)", "swój"),
  item("Marek pożyczył auto od Tomka i jedzie {1} samochodem. (Томека)", "jego"),
  item("Dzieci bawią się {1} zabawkami. (своими)", "swoimi"),
  item("Ewa spotkała Kasię i {1} męża. (мужа Каси)", "jej"),
  item("Oni rozmawiają o {1} problemach. (своих)", "swoich"),
  item("Sąsiedzi wyjechali, a my podlewamy {1} kwiaty. (соседей)", "ich"),
  item("Profesor czyta {1} artykuł. (свою статью)", "swój"),
  item("Mama dzwoni do {1} siostry. (своей)", "swojej"),
  item("Lubię Martę, ale nie lubię {1} psa. (Марты)", "jej"),
  item("Tomek mieszka ze {1} rodzicami. (своими)", "swoimi"),
  item("Studenci oddali {1} prace. (свои)", "swoje"),
  item("Nie znam {1} adresu. (его)", "jego"),
 ], ["R1", "R2", "R5", "R6"]))

exs.append(ex("e2", "swój в нужном падеже", "gaps", "Поставьте swój в нужную форму. С «я/мы» засчитывается и mój/nasz.", [
  item("Pomagam {1} mamie.", "swojej|mojej"),
  item("Jadę do pracy {1} samochodem.", "swoim|moim"),
  item("On nie ma {1} pokoju.", "swojego"),
  item("Ewa myśli o {1} przyszłości.", "swojej"),
  item("Dziadek opowiada o {1} młodości.", "swojej"),
  item("Kasia przedstawiła mi {1} chłopaka.", "swojego"),
  item("Oni zaprosili {1} przyjaciół.", "swoich"),
  item("Marek dał prezent {1} siostrze.", "swojej"),
  item("Każdy ma {1} zdanie.", "swoje"),
  item("Rodzice są dumni ze {1} dzieci.", "swoich"),
  item("Ona rozmawia ze {1} szefem.", "swoim"),
  item("Wróciliśmy do {1} domu.", "swojego|naszego"),
 ], ["R6", "R4"]))

exs.append(ex("e3", "Подлежащее или дополнение?", "gaps", "Впишите местоимение (в скобках — по-русски). Помните: swój не бывает в подлежащем.", [
  item("{1} brat mieszka w Krakowie. (мой)", "Mój"),
  item("Odwiedzam {1} brata w Krakowie. (своего, я)", "swojego|mojego"),
  item("Marek i {1} żona przyszli na imprezę. (его)", "jego"),
  item("Ewa przyszła ze {1} mężem. (своим)", "swoim"),
  item("{1} dzieci chodzą do szkoły. (её)", "Jej"),
  item("Anna kocha {1} dzieci. (своих)", "swoje"),
  item("Czy {1} samochód jest nowy? (твой)", "twój"),
  item("Sprzedałeś już {1} samochód? (свой, ты)", "swój|twój"),
  item("{1} rodzice są lekarzami. (их)", "Ich"),
  item("Oni odwiedzają {1} rodziców co tydzień. (своих)", "swoich"),
 ], ["R3", "R4", "R5"]))

exs.append(ex("e4", "siebie, sobie, sobą или się?", "gaps", "Впишите нужную форму.", [
  item("Kupiłam {1} nową sukienkę.", "sobie"),
  item("Myję {1} każdego ranka.", "się"),
  item("Opowiedz mi coś o {1}.", "sobie"),
  item("Zrobiłem to dla {1}.", "siebie"),
  item("On zawsze myśli tylko o {1}.", "sobie"),
  item("Masz przy {1} dokumenty?", "sobie"),
  item("Jestem z {1} dumny.", "siebie"),
  item("Wracam do {1}. (домой)", "siebie"),
  item("Weź parasol ze {1}.", "sobą"),
  item("Patrzyła na {1} w lustrze.", "siebie"),
  item("Ona nie jest pewna {1}.", "siebie"),
  item("Co masz na {1}? (какая одежда)", "sobie"),
  item("Usiedliśmy obok {1}.", "siebie"),
  item("Nalej {1} kawy.", "sobie"),
 ], ["R7", "R8", "R9", "R10"]))

exs.append(ex("e5", "Себя или его/её?", "gaps", "Впишите siebie/sobie/sobą или личное местоимение — по смыслу в скобках.", [
  item("Ona myśli tylko o {1}. (о себе)", "sobie"),
  item("Ona myśli tylko o {1}. (о ней — о другой)", "niej"),
  item("Marek kupił {1} książkę. (себе)", "sobie"),
  item("Marek kupił {1} książkę. (ему — другому)", "mu|jemu"),
  item("Jestem dumna z {1}. (собой)", "siebie"),
  item("Jestem dumna z {1}. (тобой)", "ciebie"),
  item("Oni rozmawiają o {1}. (о себе)", "sobie"),
  item("Oni rozmawiają o {1}. (о них — о других)", "nich"),
  item("Zabierz psa ze {1}. (с собой)", "sobą"),
  item("Zrobiłam to dla {1}. (для него)", "niego"),
 ], ["R11", "R9"]))

exs.append(ex("e6", "Друг друга", "gaps", "Впишите się, sobie, siebie, sobą или nawzajem.", [
  item("Anna i Piotr kochają {1} od liceum.", "się"),
  item("Pomagamy {1} nawzajem.", "sobie"),
  item("Piszą do {1} długie listy.", "siebie"),
  item("Długo rozmawiali ze {1}.", "sobą"),
  item("Spotkaliśmy {1} przypadkiem na lotnisku.", "się"),
  item("Patrzyli na {1} bez słowa.", "siebie"),
  item("Znamy {1} od dziecka.", "się"),
  item("— Miłego weekendu! — {1}!", "Nawzajem|Wzajemnie"),
 ], ["R12"]))

exs.append(ex("e7", "Тест в формате экзамена: письмо", "gaps",
  "Uzupełnij list. Wpisz swój / jego / jej / ich w odpowiedniej formie albo siebie / sobie / sobą / się. W nawiasie — podpowiedź po rosyjsku.", [
  item("Droga Aniu! Mój brat Tomek wreszcie kupił {1} pierwsze mieszkanie. (своё)", "swoje|własne"),
  item("Mieszka w nim ze {1} dziewczyną. (своей)", "swoją"),
  item("{1} dziewczyna ma na imię Ola. (его)", "Jego"),
  item("Ola pracuje w szkole i bardzo lubi {1} pracę. (свою)", "swoją"),
  item("W sobotę zaprosili nas do {1}. (к себе)", "siebie"),
  item("Tomek pokazał nam {1} nowe meble, (свои)", "swoje"),
  item("a Ola opowiadała o {1} rodzinie. (своей)", "swojej"),
  item("{1} rodzice mieszkają w Gdańsku. (её)", "Jej"),
  item("Wieczorem Tomek i Ola pomagali {1} w kuchni. (друг другу)", "sobie"),
  item("Widać, że dobrze czują się ze {1}. (друг с другом)", "sobą"),
  item("Mama była bardzo dumna ze {1} syna. (своего)", "swojego"),
  item("Następnym razem zaprosimy ich do {1}. (к себе) Całuję, Kasia", "siebie"),
 ], ["R1", "R2", "R3", "R6", "R9", "R12"], fmt="exam-text"))

exs.append(ex("e8", "Przekształcenia", "gaps", "Перестройте предложение, используя swój или siebie/sobie/sobą. Напечатайте продолжение.", [
  item("Marek myje samochód. Samochód należy do Marka. → Marek myje {1}.", "swój samochód"),
  item("Anna rozmawia z mamą Anny. → Anna rozmawia ze {1}.", "swoją mamą"),
  item("Kupiłem książkę dla siebie. → Kupiłem {1} książkę.", "sobie"),
  item("Oni pomagają jeden drugiemu. → Oni pomagają {1}.", "sobie nawzajem|sobie|nawzajem sobie"),
  item("Przyjechał mój brat i żona mojego brata. → Przyjechał mój brat i {1}.", "jego żona"),
  item("Piotr odwiedza babcię Piotra. → Piotr odwiedza {1}.", "swoją babcię"),
  item("Tomek rozmawiał z Olą, a Ola z Tomkiem. → Tomek i Ola rozmawiali {1}.", "ze sobą"),
  item("Klucze są ze mną. → Mam klucze przy {1}.", "sobie"),
 ], ["R1", "R2", "R9", "R10", "R12"], fmt="rewrite"))

exs.append({"id": "w1", "kind": "writing", "title": "Моя семья", "facts": ["R1", "R2", "R3", "R5"],
  "instr": "Napisz tekst o swojej rodzinie (80–100 słów): przedstaw dwie lub trzy osoby — gdzie mieszkają, co robią, z kim, jakie mają hobby.",
  "checklist": ["не меньше 4 форм swój в разных падежах", "не меньше 2 форм jego / jej / ich", "ни одного swój в подлежащем", "хотя бы 1 sobie / ze sobą"]})
exs.append({"id": "w2", "kind": "writing", "title": "Отпуск с друзьями", "facts": ["R9", "R10", "R12"],
  "instr": "Napisz e-mail do koleżanki (80–100 słów) o wyjeździe z przyjaciółmi: co zabraliście ze sobą, jak sobie pomagaliście, co kupiliście sobie na pamiątkę, o czym rozmawialiście.",
  "checklist": ["ze sobą, sobie, siebie — хотя бы по 1 разу", "1 взаимное действие с się (spotkaliśmy się…)", "1 nawzajem", "2 формы swój"]})

topic = {"id": "swoj-siebie", "num": 15, "title": "Swój или jego; siebie, sobie, się", "level": "B1",
  "lang": "ru", "prev": "stopniowanie", "next": "imieslowy-przyslowkowe",
  "summary": "Когда «свой» — swój, а когда jego/jej/ich; почему swój не бывает подлежащим; возвратное местоимение siebie/sobie/sobą/się и взаимные действия.",
  "sections": sections, "exercises": exs}
save("swoj-siebie", extract, topic)
