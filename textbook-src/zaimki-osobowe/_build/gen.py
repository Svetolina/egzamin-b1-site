# Генератор темы «Zaimki osobowe» (личные местоимения) — extract.json и topic.json
import json, os

OUT = '/home/claude/zo/zaimki-osobowe'
os.makedirs(OUT, exist_ok=True)

SOURCES = {
    "STD": "Dz.U. 2025 poz. 217 (файл проекта D20250217.pdf), Zał. 1, Część II",
    "PP": "Gramatyka z kulturą. Przez przypadki (B. Maliszewski), UMCS 2020 — таблицы «Zaimki osobowe»: s. 40 (dopełniacz), 56 (celownik), 74 (biernik), 94 (narzędnik), 110 (miejscownik)",
    "JPBG9": "Język polski bez granic, kl. IX (B1, cz. 1), Wspólnota Polska 2020: lekcja 6 s. 120 (biernik zaimków + «Uwaga!» о кратких формах и формах после предлогов), ćw. III s. 121, klucz s. 198; lekcja 8 s. 159 (narzędnik zaimków); lekcja 9 s. 175 (miejscownik zaimków), ćw. II s. 176",
    "PWN1": "M. Bańko, «mnie czy mi? tobie czy ci?», Poradnia Językowa PWN, 21.06.2004: https://sjp.pwn.pl/poradnia/haslo/mnie-czy-mi-tobie-czy-ci;5375.html",
    "PWN2": "M. Bańko, «mnie czy mi?», Poradnia Językowa PWN, 4.10.2010: https://sjp.pwn.pl/poradnia/haslo/mnie-czy-mi;11443.html",
    "ZPE": "ZPE, A. Grabarczyk, «Przemiany w deklinacji polskiej. Zaimek» (формы akcentowane/nieakcentowane, формы с n- после предлога): https://zpe.gov.pl/pdf/Pa0c6dTYP",
    "EGZ": "Egzamin B1, luty 2024, Poprawność gramatyczna, zad. I (odmiana rzeczowników, przymiotników i zaimków): «z (nam, nas, nami)», «podoba się (ich, im, nim) obydwu»; zad. VIII: «Proszę cię», «za tobą», «z nim», «od ciebie»",
    "MORF": "Morfeusz 2 (SGJP) — падеж, число, ударная/безударная форма (akc/nakc) и форма после предлога (praep/npraep)",
}

FACTS = [
 {"id":"Z1","claim":"ja / ty по падежам: mnie; mi/mnie; mnie; mną; mnie — ciebie/cię; tobie/ci; ciebie/cię; tobą; tobie.",
  "refs":["PP s. 40, 56, 74, 94, 110 (таблицы «Zaimki osobowe»)","JPBG9 s. 120 (biernik: mnie; cię, ciebie), s. 159 (mną, tobą), s. 175 (mnie, tobie)","MORF"],"status":"ok"},
 {"id":"Z2","claim":"on / ono: jego/go/niego; jemu/mu/niemu; on — jego/go/niego, ono — je/nie; nim; nim.",
  "refs":["PP s. 40, 56, 74, 94, 110","JPBG9 s. 120 (go, jego, niego; je, nie), s. 159 (nim), s. 175 (nim)","MORF"],"status":"ok"},
 {"id":"Z3","claim":"ona: jej/niej; jej/niej; ją/nią; nią; niej.",
  "refs":["PP s. 40, 56, 74, 94, 110","JPBG9 s. 120 (ją, nią), s. 159 (nią), s. 175 (niej)","MORF"],"status":"ok"},
 {"id":"Z4","claim":"my, wy, oni, one: nas, nam, nas, nami, nas — was, wam, was, wami, was — ich/nich, im/nim, oni: ich/nich, one: je/nie, nimi, nich.",
  "refs":["PP s. 40, 56, 74 (oni — ich/nich, one — je/nie), 94, 110","JPBG9 s. 120 (oni ich, nich; one je, nie), s. 159 (nami, wami, nimi), s. 175 (nas, was, nich)","MORF"],"status":"ok"},
 {"id":"Z5","claim":"Краткие формы (mi, ci, cię, go, mu) — безударные: стоят после глагола или в середине фразы, не в начале. В начале и при выделении — длинные (mnie, tobie, ciebie, jego, jemu).",
  "refs":["JPBG9 s. 120 («Uwaga!»: krótkie formy — zwykle po czasowniku lub w środku zdania, nigdy na początku zdania)","PWN1 (Mnie to daj — Daj mi to; Tobie wszystko zawdzięczam; Jego nie widzę; Widzę jego, a nie ją)","PWN2 (Mi się tak wydaje — «wciąż nie najlepsza polszczyzna»)","ZPE (formy akcentowane mnie, tobie — nieakcentowane mi, ci)","MORF (akc / nakc)"],"status":"ok"},
 {"id":"Z6","claim":"После предлога — длинная форма (mnie, ciebie, tobie) или форма с n- (niego, niemu, nią, niej, nim, nie, nich). Формы niego, niemu, niej, nich, nie и nią (кого? что?) — только после предлога; в творительном nim, nią, nimi — одна форма, с предлогом и без.",
  "refs":["JPBG9 s. 120 («Uwaga!»: po przyimkach — forma dłuższa (ciebie) albo forma z n- (niego, nią, nie))","ZPE (bez przyimka: jego, je, ją, jemu, jej — z przyimkiem: niego, nie, nią, niemu, niej)","PP s. 74 (Płacę za niego / za nią / za nie; Czekamy na nich / na nie), s. 94 (narzędnik: nim, nią, nimi; ćw. 11: Bardzo się … (on) interesuję)","JPBG9 s. 159 (ćw. IV: Bawi się … (one) codziennie — klucz s. 201: nimi)","MORF (praep / npraep)"],"status":"ok"},
 {"id":"Z7","claim":"С mną предлоги получают -e: ze mną, przede mną, nade mną, pode mną.",
  "refs":["PP s. 94 (ćw. 11: Chcesz ze mną…, Pójdziesz ze mną…)","JPBG9 s. 159 (ćw. IV: przede mną; klucz s. 201)"],"status":"ok"},
 {"id":"Z8","claim":"В письме к адресату формы ty пишут с большой буквы: Cię, Ciebie, Ci, Tobie, Tobą.",
  "refs":["STD B1 s. 78 (Kochana Mamo! Pozdrawiam Cię bardzo serdecznie z Poznania.)","PP s. 75 (ćw. 10: Pozdrawiam … (Ty), Całuję … (Ty))"],"status":"ok"},
]

PASSPORT = {
 "standard": "Dz.U. 2025 poz. 217, Zał. 1, Część II, E (B1), 2.2.1 pkt 1 lit. c «odmiana zaimków (liczba pojedyncza i mnoga): – odmiana zaimków osobowych: ja, ty, on, ona, ono», s. 76 Dz.U.",
 "examples_std": "s. 78: «Ten film o Polsce podobał mi się bardzo» (celownik), «Posłuchajcie go! Nie słuchajcie go!» (zdania rozkazujące), «Pozdrawiam Cię bardzo serdecznie z Poznania»",
 "level": "Та же строка уже на A2 (s. 67); на B2 (s. 88) — «odmiana zaimków osobowych…» без перечня. На B1 — все падежи, краткие/длинные формы и формы с n-.",
 "katalog_a": "6.1 pkt 1 lit. i «zapraszanie» (s. 82); 6.1 pkt 6 lit. e «wyrażanie upodobania» (s. 83); 6.1 pkt 7 lit. d «proponowanie, przyjmowanie i odrzucanie propozycji» (s. 83)",
 "katalog_b": "7.1 pkt 9 «relacje międzyludzkie», pkt 10 «utrzymywanie kontaktu (korespondowanie, spotkania)» (s. 84)",
 "exam": "Poprawność gramatyczna, zad. I «odmiana rzeczowników, przymiotników i zaimków» (luty 2024: z nas, im); Pisanie — формы Cię/Ciebie в письмах",
 "depends_on": "biernik, dopelniacz, celownik, narzednik, miejscownik, przyimki, mianownik-lm",
}

# формы для проверки Morfeusz: (форма, лемма, падеж, число)
FORMS = []
def F(forms, lemma, n):
    for f, c in forms:
        FORMS.append({"form": f, "kind": "przyp", "lemma": lemma, "case": c, "n": n})
F([("mnie","gen"),("mi","dat"),("mnie","dat"),("mnie","acc"),("mną","inst"),("mnie","loc")],"ja","sg")
F([("ciebie","gen"),("cię","gen"),("tobie","dat"),("ci","dat"),("ciebie","acc"),("cię","acc"),("tobą","inst"),("tobie","loc")],"ty","sg")
F([("jego","gen"),("go","gen"),("niego","gen"),("jemu","dat"),("mu","dat"),("niemu","dat"),("jego","acc"),("go","acc"),("niego","acc"),("nim","inst"),("nim","loc"),("je","acc"),("nie","acc")],"on","sg")
F([("jej","gen"),("niej","gen"),("jej","dat"),("niej","dat"),("ją","acc"),("nią","acc"),("nią","inst"),("niej","loc")],"on","sg")
F([("nas","gen"),("nam","dat"),("nas","acc"),("nami","inst"),("nas","loc")],"my","pl")
F([("was","gen"),("wam","dat"),("was","acc"),("wami","inst"),("was","loc")],"wy","pl")
F([("ich","gen"),("nich","gen"),("im","dat"),("nim","dat"),("ich","acc"),("nich","acc"),("je","acc"),("nie","acc"),("nimi","inst"),("nich","loc")],"on","pl")

def P(t): return {"type":"p","text":t}
def TB(head, rows, pl): return {"type":"table","head":head,"rows":rows,"pl_cols":pl}
def EX(*items): return {"type":"ex","items":[{"pl":a,"ru":b} for a,b in items]}
def NOTE(t, kind="tip"): return {"type":"note","kind":kind,"text":t}
def FIX(*items): return {"type":"fix","items":[{"bad":a,"good":b} for a,b in items]}
def CH(*items): return {"type":"chips","items":list(items)}
def ST(*items): return {"type":"steps","items":list(items)}

THEORY = [
 {"id":"t1","title":"Главное за полминуты","facts":["Z5","Z6"],"blocks":[
   P("У многих местоимений по две-три формы одного падежа. Выбор зависит от двух вопросов: **есть ли предлог** и **падает ли на слово ударение**."),
   ST("После предлога — длинная форма или форма с n-: [[do mnie, dla ciebie, z nim, o niej]].",
      "Без предлога, в середине фразы — короткая: [[Daj mi. Widzę go. Kocham cię.]]",
      "В начале фразы или когда выделяем — длинная: [[Mnie to daj. Jego nie widzę.]]"),
 ]},
 {"id":"t2","title":"Ja и ty по падежам","facts":["Z1"],"blocks":[
   TB(["падеж","ja","ty"],[
     ["кого? чего?","mnie","ciebie / cię"],
     ["кому?","mi / mnie","ci / tobie"],
     ["кого? что?","mnie","ciebie / cię"],
     ["кем? чем?","mną","tobą"],
     ["о ком?","mnie","tobie"]],[1,2]),
   NOTE("Через косую черту: сначала короткая (безударная) форма, потом длинная. У [[ja]] короткая есть только в дательном: [[mi]]."),
 ]},
 {"id":"t3","title":"On и ono","facts":["Z2"],"blocks":[
   TB(["падеж","без предлога","после предлога"],[
     ["кого? чего?","go / jego","niego"],
     ["кому?","mu / jemu","niemu"],
     ["кого? что? (on)","go / jego","niego"],
     ["что? (ono)","je","nie"],
     ["кем? чем?","nim","nim"],
     ["о ком?","—","nim"]],[1,2]),
   EX(("To jest Marek. Znam go od dziecka.","Это Марек. Я знаю его с детства."),
      ("Mam dla niego prezent.","У меня для него подарок."),
      ("To okno jest brudne. Umyję je.","Это окно грязное. Я его вымою.")),
 ]},
 {"id":"t4","title":"Ona","facts":["Z3"],"blocks":[
   TB(["падеж","без предлога","после предлога"],[
     ["кого? чего?","jej","niej"],
     ["кому?","jej","niej"],
     ["кого? что?","ją","nią"],
     ["кем? чем?","nią","nią"],
     ["о ком?","—","niej"]],[1,2]),
   EX(("Kupię jej kwiaty.","Я куплю ей цветы."),
      ("Byłam u niej wczoraj.","Я была у неё вчера."),
      ("Lubię ją. Często z nią rozmawiam.","Я её люблю. Часто с ней разговариваю.")),
   NOTE("Не путайте [[ją]] (кого? что?) и [[nią]] (кем? — и после предлога): [[Widzę ją]], но [[Idę z nią]], [[Czekam na nią]]."),
 ]},
 {"id":"t5","title":"My, wy, oni, one","facts":["Z4"],"blocks":[
   TB(["падеж","my","wy","oni / one"],[
     ["кого? чего?","nas","was","ich / nich"],
     ["кому?","nam","wam","im / nim"],
     ["кого? что?","nas","was","oni: ich / nich · one: je / nie"],
     ["кем? чем?","nami","wami","nimi"],
     ["о ком?","nas","was","nich"]],[1,2,3]),
   P("В винительном различаем **мужчин (oni)** и **всех остальных (one)**: [[Zapraszam braci — zapraszam ich]], но [[Zapraszam siostry — zapraszam je]]."),
   EX(("Odwiedźcie nas w sobotę!","Приходите к нам в субботу!"),
      ("Rozmawiałam z nimi wczoraj.","Я разговаривала с ними вчера."),
      ("Te książki są nowe. Czytam je.","Эти книги новые. Я их читаю.")),
 ]},
 {"id":"t6","title":"Короткая или длинная?","facts":["Z5"],"blocks":[
   P("Короткие формы [[mi, ci, cię, go, mu]] безударные — они «прилипают» к глаголу. Поэтому **в начале фразы их не ставят**. Там и при противопоставлении нужна длинная форма."),
   TB(["обычно","с выделением"],[
     ["Daj mi to.","Mnie to daj, nie jemu."],
     ["Dużo ci zawdzięczam.","Tobie wszystko zawdzięczam."],
     ["Nie widzę go.","Jego nie widzę, ale widzę ją."]],[0,1]),
   FIX(("Mi się to nie podoba.","Mnie się to nie podoba.")),
   NOTE("В разговоре [[Mi się wydaje…]] слышно часто, но по норме в начале фразы — [[Mnie]]. На экзамене пишите [[Mnie się podoba]]."),
 ]},
 {"id":"t7","title":"После предлога","facts":["Z6"],"blocks":[
   P("После предлога короткие формы не бывают. Берём длинную форму или форму с **n-**. Формы [[niego, niemu, niej, nich, nie]] и [[nią]] (кого? что?) бывают **только** после предлога."),
   NOTE("В творительном одна форма — [[nim, nią, nimi]], и с предлогом, и без: [[Idę z nim]], [[Interesuję się nim]]."),
   TB(["без предлога","после предлога"],[
     ["Znam go.","Czekam na niego."],
     ["Dam mu.","Idę ku niemu? — редко; обычно: Dzięki niemu."],
     ["Lubię ją.","Myślę o niej. Idę z nią."],
     ["Pomagam jej.","Mam coś dla niej."],
     ["Zapraszam ich.","Idę do nich."],
     ["Widzisz cię? — нет: Widzę cię.","To dla ciebie."]],[0,1]),
   FIX(("Czekam na go.","Czekam na niego."),
       ("Rozmawiałam z ją.","Rozmawiałam z nią."),
       ("To list do jej.","To list do niej.")),
 ]},
 {"id":"t8","title":"Ze mną, przede mną","facts":["Z7"],"blocks":[
   P("Перед [[mną]] предлоги получают -e:"),
   CH("ze mną","przede mną","nade mną","pode mną"),
   EX(("Chodź ze mną do kina!","Пойдём со мной в кино!"),
      ("Przede mną stał wysoki pan.","Передо мной стоял высокий мужчина.")),
 ]},
 {"id":"t9","title":"В письме","facts":["Z8"],"blocks":[
   P("Когда пишем письмо человеку, формы [[ty]] обычно пишут с большой буквы — из вежливости:"),
   EX(("Pozdrawiam Cię serdecznie!","Сердечно тебя приветствую!"),
      ("Dziękuję Ci za pomoc.","Спасибо тебе за помощь."),
      ("Mam dla Ciebie niespodziankę.","У меня для тебя сюрприз.")),
 ]},
 {"id":"t10","title":"На экзамене","facts":["EXAM"],"blocks":[
   P("В части «Poprawność gramatyczna» есть задание на выбор формы, где среди вариантов — местоимения (в феврале 2024: [[z nas]], [[podoba się im]]). А в письме формы [[Cię, Ci, Ciebie]] нужны почти всегда."),
   ST("Есть предлог? → длинная или с n-: [[dla niego, z nią, o nich]].",
      "Начало фразы или выделение? → длинная: [[Mnie, Tobie, Jego]].",
      "Иначе → короткая: [[mi, ci, cię, go, mu]].",
      "Мужчины → [[ich / nich]], все остальные → [[je / nie]] (кого? что?)."),
 ]},
]

# t7 — убираем сомнительные строки, оставляем ясные пары
THEORY[6]["blocks"][1] = TB(["без предлога","после предлога"],[
     ["Znam go.","Czekam na niego."],
     ["Pomagam mu.","Dzięki niemu zdałam egzamin."],
     ["Lubię ją.","Idę z nią do kina."],
     ["Kupię jej kwiaty.","Mam coś dla niej."],
     ["Zapraszam ich.","Idę do nich."],
     ["Widzę cię.","To dla ciebie."]],[0,1])

def I(q,a,expl,t,opts=None):
    d={"q":q,"a":a if isinstance(a,list) else [a],"expl":expl,"t":t}
    if opts: d["opts"]=opts
    return d

EXS = [
 {"id":"e1","level":1,"kind":"choice","title":"Выберите форму","items":[
   I("Idziesz ze ___ do kina?","mną","С кем? — творительный: mną.","t8",["mną","mnie","mi"]),
   I("___ się ten film nie podobał, a tobie?","Mnie","Начало фразы и противопоставление — длинная форма.","t6",["Mnie","Mi","Mną"]),
   I("To prezent dla ___.","ciebie","После предлога — длинная форма.","t7",["ciebie","cię","ci"]),
   I("Znasz Marka? Często o ___ myślę.","nim","O kim? — предложный: nim.","t3",["nim","niego","jego"]),
   I("Gdzie jest Ania? Czekam na ___ od rana.","nią","Czekać na kogo? — винительный после предлога: nią.","t4",["nią","ją","niej"]),
   I("Lubisz te piosenki? Słucham ___ codziennie.","ich","Słuchać кого? чего? — родительный, без предлога: ich.","t5",["ich","je","nich"]),
   I("Kupiłam nowe buty i chodzę w ___ cały dzień.","nich","W czym? — предложный: nich.","t5",["nich","ich","nie"]),
   I("Gdzie są dzieci? Widzę ___ w ogrodzie.","je","Dzieci — не мужчины: в винительном je.","t5",["je","ich","nie"]),
 ]},
 {"id":"e2","level":1,"kind":"type","title":"Исправьте ошибку","instr":"Выделенная форма неверна. Впишите правильную.","items":[
   I("Czekam na **go** od godziny.","niego","После предлога — форма с n-.","t7"),
   I("**Mi** się to wcale nie podoba.","Mnie","В начале фразы — длинная форма.","t6"),
   I("Rozmawiałam wczoraj z **ją**.","nią","После предлога z — nią.","t7"),
   I("To jest list do **jej**.","niej","После предлога — форма с n-.","t7"),
   I("Często myślę o **ciebie**.","tobie","O kim? — предложный: tobie.","t2"),
   I("**Cię** szukam, a nie Marka.","Ciebie","Начало фразы и противопоставление — длинная форма.","t6"),
   I("Nie mogę bez **cię** żyć.","ciebie","После предлога — длинная форма.","t7"),
 ]},
 {"id":"e3","level":2,"kind":"type","title":"Ja и ty","instr":"Поставьте местоимение в скобках в нужную форму.","items":[
   I("Zadzwoń do ___ wieczorem! (ja)","mnie","Do kogo? — родительный: mnie.","t2"),
   I("Zjesz ze ___ obiad? (ja)","mną","Z kim? — mną.","t8"),
   I("Bardzo tęsknię za ___. (ty)","tobą","Tęsknić za kim? — творительный: tobą.","t2"),
   I("Kocham ___! (ty)",["cię","ciebie"],"Обычно cię; ciebie — если выделяем.","t6"),
   I("Myślę o ___ cały dzień. (ty)","tobie","O kim? — предложный: tobie.","t2"),
   I("Czy ten prezent jest dla ___? (ja)","mnie","Dla kogo? — родительный: mnie.","t2"),
   I("Pokażę ___ moje zdjęcia z wakacji. (ty)",["ci","tobie"],"Кому? Обычно ci; tobie — если выделяем.","t6"),
   I("Nie było ___ wczoraj na lekcji. (ja)","mnie","Kogo nie było? — родительный: mnie.","t2"),
   I("Bez ___ nie pojadę na wycieczkę. (ty)","ciebie","Bez kogo? — после предлога длинная: ciebie.","t7"),
   I("W kinie siedziałaś obok ___. (ja)","mnie","Obok kogo? — родительный: mnie.","t2"),
 ]},
 {"id":"e4","level":2,"kind":"type","title":"On, ona, ono","instr":"Поставьте местоимение в скобках в нужную форму.","items":[
   I("To jest Marek. Znam ___ od dziecka. (on)","go","Kogo? без предлога, без выделения — go.","t3"),
   I("To jest Ewa. Bardzo ___ lubię. (ona)","ją","Kogo? — винительный: ją.","t4"),
   I("Ewa ma jutro urodziny. Mam dla ___ prezent. (ona)","niej","Dla kogo? — после предлога: niej.","t4"),
   I("Kup ___ kwiaty na urodziny! (ona)","jej","Komu? без предлога — jej.","t4"),
   I("Dziadek jest chory. Często ___ pomagam. (on)","mu","Komu? без выделения — mu.","t3"),
   I("Idę do Tomka. Muszę z ___ porozmawiać. (on)","nim","Z kim? — nim.","t3"),
   I("Lubię to miasto. Mieszkam w ___ od roku. (ono)","nim","W czym? — предложный: nim.","t3"),
   I("Gdzie jest dziecko? Szukam ___ wszędzie. (ono)","go","Szukać kogo? — родительный: go.","t3"),
   I("To moja przyjaciółka Ola. Byłam u ___ wczoraj. (ona)","niej","U kogo? — после предлога: niej.","t4"),
   I("To jest Adam. Kupiłam dla ___ książkę. (on)","niego","Dla kogo? — после предлога: niego.","t3"),
 ]},
 {"id":"e5","level":2,"kind":"type","title":"My, wy, oni, one","instr":"Поставьте местоимение в скобках в нужную форму.","items":[
   I("Odwiedźcie ___ w sobotę! (my)","nas","Kogo? — nas.","t5"),
   I("Dam ___ znać jutro. (wy)","wam","Komu? — wam.","t5"),
   I("Rodzice? Rozmawiałam z ___ wczoraj. (oni)","nimi","Z kim? — nimi.","t5"),
   I("Koledzy są w kawiarni. Idę do ___. (oni)","nich","Do kogo? — после предлога: nich.","t5"),
   I("Znasz moje siostry? Zaprosiłam ___ na imprezę. (one)","je","Kogo? siostry — не мужчины: je.","t5"),
   I("Moi bracia mieszkają daleko. Rzadko ___ widzę. (oni)","ich","Kogo? bracia — мужчины: ich.","t5"),
   I("Sąsiedzi mają problem. Muszę ___ pomóc. (oni)","im","Komu? без предлога — im.","t5"),
   I("To dla ___, kochani! (wy)","was","Dla kogo? — was.","t5"),
   I("Wakacje już niedługo. Czekam na ___ cały rok. (one)","nie","Na co? wakacje — не мужчины, после предлога: nie.","t5"),
 ]},
 {"id":"e6","level":3,"kind":"text","format":"exam","title":"List od Oli","instr":"Как на экзамене: поставьте местоимения в скобках в нужную форму. В письме формы ty можно писать с большой буквы.",
  "passage":"Droga Kasiu! Dziękuję {1} za długi list. Tak się cieszę, że w sobotę przyjedziesz do {2}! Mój brat Paweł bardzo chce {3} poznać, bo dużo {4} o Tobie opowiadałam. W sobotę wieczorem pójdziemy do moich przyjaciół – Ani i Tomka. Byłam u {5} wczoraj i pytali o {6}. Ania ma dla {7} mały prezent, a Tomek chce {8} pokazać swoje zdjęcia z Japonii. Mama prosi, żebyś zadzwoniła do {9} przed przyjazdem. Czekam na {10}! Ściskam Cię, Ola",
  "items":[
   I("(Ty)",["Ci","ci","Tobie","tobie"],"Komu? после глагола — Ci.","t9"),
   I("(my)","nas","Do kogo? — nas.","t5"),
   I("(Ty)",["Cię","cię"],"Kogo? без предлога — Cię.","t9"),
   I("(on)","mu","Komu? без выделения — mu.","t3"),
   I("(oni)","nich","U kogo? — после предлога: nich.","t5"),
   I("(Ty)",["Ciebie","ciebie"],"O kogo? — после предлога длинная: Ciebie.","t7"),
   I("(Ty)",["Ciebie","ciebie"],"Dla kogo? — Ciebie.","t7"),
   I("(Ty)",["Ci","ci"],"Komu? после глагола — Ci.","t9"),
   I("(ona)","niej","Do kogo? — после предлога: niej.","t4"),
   I("(Ty)",["Ciebie","ciebie"],"Na kogo? — после предлога: Ciebie.","t7"),
  ]},
 {"id":"e7","level":3,"kind":"type","format":"exam","title":"Перефразирование","instr":"Перепишите по образцу: впишите одно слово.","items":[
   I("Daj mi to. → ___ to daj, nie jemu.","Mnie","Начало фразы и противопоставление — длинная.","t6"),
   I("Nie widzę go. → ___ nie widzę, ale widzę ją.","Jego","Начало фразы — длинная форма.","t6"),
   I("Czekam na Marka. → Czekam na ___.","niego","После предлога — niego.","t7"),
   I("Rozmawiam z Anną. → Rozmawiam z ___.","nią","Z kim? — nią.","t4"),
   I("Myślę o rodzicach. → Myślę o ___.","nich","O kim? — nich.","t5"),
   I("Pomagam babci. → Pomagam ___.","jej","Komu? без предлога — jej.","t4"),
   I("Znam twoje siostry. → Znam ___.","je","Siostry — не мужчины: je.","t5"),
 ]},
 {"id":"e8","level":4,"kind":"write","title":"Zaproszenie","instr":"Пригласите подругу Магду на день рождения: кто ещё придёт, что вы для неё приготовите, когда она должна позвонить.","words":[40,50],
  "need":"Минимум 6 форм личных местоимений, из них 2 — после предлога; формы ty — с большой буквы.",
  "model":"Droga Magdo! W sobotę mam urodziny i bardzo chcę Cię zaprosić. Przyjdą też Marek i Ola – na pewno ich pamiętasz. Rozmawiałam z nimi wczoraj. Marek przyniesie gitarę, a ja upiekę dla Ciebie sernik. Zadzwoń do mnie jutro! Pozdrawiam Cię serdecznie, Kasia",
  "model_future":["Cię","ich","nimi","Ciebie","mnie"],
  "checklist":["Обращение в звательном (Droga Magdo!)","Cię / Ciebie с большой буквы","После предлога — длинная форма или с n- (z nimi, dla Ciebie)","Без предлога — короткая (Cię, ich)","Не начинаю фразу с mi / ci / go","Есть подпись"],"t":"t9"},
]

TOPIC = {
 "topic":"zaimki-osobowe","level":"B1","group":"Местоимения","title_pl":"Zaimki osobowe","title_ru":"Личные местоимения",
 "lead":"Mi или mnie? Go или niego? Как склоняются ja, ty, on, ona, my, wy, oni и когда нужна короткая форма.",
 "facts_file":"extract.json","stage":"теория и упражнения — ждёт проверки","markup":"[[…]] — польский текст",
 "exam_ref":{"id":"EXAM","refs":["Egzamin B1, luty 2024, Poprawność gramatyczna, zad. I — odmiana rzeczowników, przymiotników i zaimków (z nas; podoba się im)","Dz.U. 2025 poz. 217, B1, 2.2.1 pkt 1 lit. c, s. 76"]},
 "forms":[],"theory":THEORY,"exercises":EXS,
}

EXTRACT = {"topic":"zaimki-osobowe","passport":PASSPORT,"sources":SOURCES,"facts":FACTS,"forms":FORMS,"checked":"28.10.2026"}

json.dump(EXTRACT, open(f'{OUT}/extract.json','w'), ensure_ascii=False, indent=1)
json.dump(TOPIC, open(f'{OUT}/topic.json','w'), ensure_ascii=False, indent=1)
n = sum(len(e.get('items',[])) for e in EXS if e['kind']!='write')
print('items', n, 'theory', len(THEORY), 'facts', len(FACTS), 'forms', len(FORMS))
