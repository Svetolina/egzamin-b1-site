# Сверка фактов с учебниками проекта (шаг 3). Добавляется к refs; status — переопределение.
# PO = Przez osoby, PP = Przez przypadki (Gramatyka z kulturą), JPBG XI = Język polski bez granic kl. XI (B2),
# ZJP / ZJP Ćw / ZJP Por = Z językiem polskim każdego dnia B1 (podręcznik / ćwiczenia / poradnik).
R = {}
S = {}   # topic -> {fact: (status, decision)}
R['tryb-rozkazujacy'] = {
 'R1': ['PO s. 149–150 (таблицы форм ty / my / wy; «Przy 1. i 3. os. l. poj. oraz 3. os. l. mn. trybu rozkazującego używamy słowa niech»)'],
 'R2': ['PO s. 149 (формы от czasu teraźniejszego, у совершенных — от простого будущего: wrócisz → wróć, pójdziesz → pójdź, zrobisz → zrób)'],
 'R3': ['PO s. 149 («Wśród czasowników III koniugacji (-am, -asz) oraz IV koniugacji (-em, -esz) formy 2. os. l. poj. trybu rozkazującego tworzymy od formy 3 os. l. mn. czasu teraźniejszego: czytają, powiedzą»)'],
 'R4': ['PO s. 149 («Wśród czasowników I koniugacji (-ę, -esz) oraz II koniugacji (-ę, -isz / -ysz) formy 2. os. l. poj. … tworzymy od formy 2 os. l. poj. czasu teraźniejszego: piszesz, mówisz»; «Zwróć uwagę na miękkie spółgłoski!»)'],
 'R5': ['PO s. 149 («Przy zbitce spółgłosek zwykle dopisujemy -ij … ale są też i takie formy, które nie mają tej cząstki»; śpij)'],
 'R6': ['PO s. 149–150 («Tu zrób „ó”!»: zrób, stój; zróbcie, zróbmy)'],
 'R9': ['PO s. 150 («W 1. os. l. mn. trybu rozkazującego używamy końcówki -my … a w 2. os. l. mn. … końcówki -cie»)'],
 'R10': ['PO s. 150 (ucz+my się, ucz+cie się)'],
 'R11': ['PO s. 150 («używamy słowa niech oraz form czasu teraźniejszego albo przyszłego: Niech to zrobi ekspert!»)'],
 'R14': ['PO s. 154 («W przeczeniach (zakazach) używamy tylko czasowników niedokonanych, choć są wyjątki od tej reguły (np. nie zapomnij, nie spóźnij się, nie obraź się)»)'],
 'R16': ['PO s. 150 («Trybu rozkazującego używamy: przy poleceniach, nakazach i zakazach; przy prośbach; przy propozycjach; przy życzeniach»)', 'ZJP Ćw s. 42 (советы перед экзаменом: «Przed egzaminem pij dużo…»)'],
}
R['tryb-przypuszczajacy'] = {
 'R1': ['PO s. 173 («Trybu warunkowego (przypuszczającego) używamy: gdy wyrażamy swoje przekonania, przypuszczenia i wątpliwości…; gdy wyrażamy prośby…; gdy składamy propozycje…; gdy wyrażamy życzenia»)'],
 'R2': ['PO s. 173 (таблица: był+bym, był+byś, był+by … byli+byśmy, były+byśmy)', 'ZJP s. 29 (таблица: chciałabym / chciałbym, mogłabym / mógłbym)'],
 'R3': ['PO s. 173 (rodzaj męski, żeński, nijaki, męskoosobowy, niemęskoosobowy)', 'ZJP s. 29'],
 'R4': ['PO s. 173 (by + окончание присоединяется к форме 3 лица: był+bym, była+byś)'],
 'R5': ['PO s. 176 («Cząstki -bym, -byś, -byśmy, -byście, -by nie lubią stać w miejscu – łączą się z różnymi słowami»)'],
 'R6': ['PO s. 176 (слитно: «ze słowami: choć, jeśli, gdy, jak, to, niech»; раздельно — после местоимений, существительных, наречий: «Kto by to wiedział?»)'],
 'R7': ['PO s. 176 («piszemy osobno: … z formami: trzeba, warto, można: Trzeba by to jeszcze przemyśleć»; «z bezokolicznikami»)'],
 'R8': ['PO s. 173 («gdy wyrażamy prośby: Czy mógłbym zadać pytanie? Czy mogłabyś chwilkę poczekać?»)', 'PO s. 174 («Czy mógłby pan…? Czy mogłaby pani…? Czy mogliby państwo…?»)'],
 'R9': ['JPBG XI s. 226 («Gdybym zdał wszystkie egzaminy, wyjechałbym na wakacje»)', 'PO s. 178–179 (Gdybym był…, Gdybyś była…)'],
 'R11': ['JPBG XI s. 226 («Jeżeli będę miał czas, pójdę do kina»; «W zdaniu warunkowym można użyć trybu przypuszczającego: Jeżeli zdam… → Gdybym zdał…»)', 'JPBG XI s. 227 (упражнение: Jeżeli będzie ładna pogoda… → Gdyby była ładna pogoda…)'],
 'R12': ['PO s. 168, 181 («Jeśli miałbym czas…», «jeślibyśmy byli grzeczni» — jeśli + by в учебнике встречается)'],
 'R13': ['PO s. 177 («co by było, gdyby…»: Gdybyś … nie poznałbyś tam Magdy — о прошлом)'],
 'R14': ['PO s. 175 («poproś wybraną osobę, żeby napisała…»)'],
 'R15': ['PO s. 168 (zjadłby, obejrzałby — dk; podziwiałby, zwiedzałby — ndk)'],
 'R16': ['PO s. 180–181 («Gdybym był bogaty, to…», «Gdybyśmy je obchodzili, to…») и JPBG XI s. 226 (без to)'],
 'R17': ['ZJP Ćw s. 42 и ключ s. 56 («tryb przypuszczający: na twoim miejscu przed egzaminem piłbym dużo wody»)'],
}
R['czasowniki-ruchu'] = {
 'R2': ['JPBG XI s. 81 («Czasowniki ruchu możemy podzielić na jednokrotne i wielokrotne… jechać – jeździć; iść – chodzić; nieść – nosić; płynąć – pływać; lecieć – latać; wieźć – wozić, biec – biegać»; «jednokrotne oznaczają ruch ukierunkowany, zaś wielokrotne – ruch nieokreślony co do kierunku»)', 'ZJP s. 70 (рамка: czasowniki wielokrotne i jednokrotne)'],
 'R3': ['JPBG XI s. 81 («Jednokrotne oznaczają czynność jednorazową»; «Dzisiaj idę po zakupy do supermarketu»)', 'ZJP s. 70 («Czasowniki jednokrotne opisują pojedyncze lub konkretnie określone akcje ruchu»)'],
 'R4': ['JPBG XI s. 81 («wielokrotne – powtarzającą się»)', 'ZJP s. 70 («Czasowniki wielokrotne opisują ruch lub czynności, które są powtarzalne, cykliczne»)'],
 'R5': ['JPBG XI s. 81 (jednokrotne с приставкой «zmieniają aspekt z niedokonanego na dokonany»)', 'PO s. 92 (iść – szedł; pójść – poszedł, poszła)'],
 'R6': ['PO s. 92 («iść – szedł, szła; pójść – poszedł, poszła»; Poszedłem, Poszłam)'],
 'R7': ['PP s. 87 (narzędnik: «gdy mówimy, czym się poruszamy: autobusem, pociągiem, samolotem, taksówką, windą»)'],
 'R9': ['JPBG XI s. 81 («Czasowniki ruchu wielokrotne po dodaniu prefiksów pozostają niedokonane, zaś jednokrotne zmieniają aspekt…: wychodzić – wyjść; zawozić – zawieźć»)'],
 'R11': ['JPBG XI s. 81–82 («Znaczenie wybranych prefiksów w czasownikach ruchu»: do-, od(e)-, w(e)-, wy-, pod(e)-, z(e)-)'],
 'R12': ['PO s. 92, 94 (dojść – doszedł; wejść – wszedł, weszła; zejść – zszedł, zeszła; odejść – odszedł, odeszła; podejść – podszedł)'],
}
R['dopelniacz-po-negacji'] = {
 'R1': ['PP s. 40 («Dopełniacza używamy: … d) gdy dokonujemy negacji biernika (nie lubię bigosu, nie piję kawy, nie jem mięsa)»)'],
 'R2': ['PP s. 40 («c) gdy mówimy, że czegoś nie ma (nie ma chleba, nie ma bułki, nie ma masła)»)', 'PP s. 41 («Czego już nie ma? … Nie ma już …»)'],
 'R7': ['PP s. 40 («(nie ma) dobrego rosołu, słodkiego ciasta … dobrej kawy, słodkiej herbaty»)'],
}
R['liczebniki-z-rzeczownikami'] = {
 'R1': ['JPBG XI s. 95 («Liczebnik jeden występuje w trzech rodzajach i odmienia się … według deklinacji przymiotnikowej: jeden, jedna, jedno»)'],
 'R2': ['JPBG XI s. 96 (2, 3, 4; 22, 23, 24; 32, 33, 34 … + «rzeczownik … w mianowniku lm.»: Dwa samochody, Trzydzieści cztery samochody)'],
 'R3': ['JPBG XI s. 96 («od 5 do 21, od 25 do 31 … w dopełniaczu lm.»: Pięć samochodów, Sto dwadzieścia jeden samochodów)'],
 'R4': ['JPBG XI s. 96 (12–14 входят в группу «od 5 do 21» — dopełniacz lm.)'],
 'R5': ['JPBG XI s. 96 («Liczebnik jeden znajdujący się na końcu liczby, niezależnie od rodzaju rzeczownika, zawsze stawiamy w rodzaju męskim: dwadzieścia jeden okien, trzydzieści jeden kobiet»)'],
 'R6': ['JPBG XI s. 95 («Liczebnik dwa posiada także formę rodzaju żeńskiego»: dwaj/dwóch — dwie — dwa)'],
 'R7': ['JPBG XI s. 98 («Liczebniki 2, 3, 4 w mianowniku lm. występują w dwóch formach: dwaj – dwóch, trzej – trzech, czterej – czterech»; dwaj + mianownik, dwóch + dopełniacz)', 'JPBG XI s. 95 (męskoosobowe: pięciu, sześciu…)'],
 'R8': ['JPBG XI s. 96 («Dwa samochody jadą / jechały»; «Pięć samochodów jedzie / jechało»)', 'JPBG XI s. 98 («Dwaj robotnicy pracują / pracowali»; «Dwóch robotników pracuje / pracowało»; «Pięciu robotników pracuje / pracowało»)'],
 'R9': ['JPBG XI s. 134 («Liczebniki zbiorowe łączą się … z rzeczownikiem dziecko: dwoje, sześcioro, piętnaścioro dzieci»)'],
 'R10': ['ZJP s. 64 («Mieszkam w Polsce ponad (12) lat», «Przed (5) laty»)'],
}
R['tryb-przypuszczajacy']['R11'].append('ZJP s. 93 («Orzeczenie zdania podrzędnego warunkowego ze spójnikami: jeśli, jeżeli, gdy, kiedy – może być wyrażone za pomocą czasu teraźniejszego, przeszłego i przyszłego»)')
R['zdania-ktory'] = {
 'R1': ['ZJP s. 91 (zdania przydawkowe — pytania «jaki? który?»: «Ubrałam dzisiaj sukienkę, która zachwyciła gości»)'],
 'R2': ['PO s. 169 и ключ s. 226 («umówiłabym się ze znajomymi, (który, którzy, którymi) mieszkają we Wrocławiu» → «którzy»: падеж — по роли в придаточном)'],
 'R3': ['PO s. 169 / 226 (ludzie → którzy)', 'PO s. 46 («Nie ma ludzi, którzy wszystko wiedzą»)'],
 'R6': ['ZJP s. 91 (примеры zdań złożonych podrzędnie с запятой перед który / gdzie)'],
}
R['zeby-aby'] = {
 'R1': ['PO s. 187–191 (żebym chodził, żebyś się uczesał(a), żebyśmy byli, żebyście były — окончание на żeby)', 'PO s. 193 (рамка: żebym, żebyś, żeby, żebyśmy, żebyście)'],
 'R2': ['PO s. 167 («poszedłbym nad Wisłę, żeby popatrzeć na pomnik smoka»)', 'PO s. 187 («co robić, żeby mieć święty spokój»)'],
 'R3': ['PO s. 188 (упражнение «Mama namawia mnie, żebym (poszłam, poszła, poszedł) na kurs» — после żebym форма на -ł без окончания: poszła)'],
 'R5': ['PO s. 192 («Spójnika „żeby” używamy przy relacjonowaniu propozycji, życzeń, rad, próśb, poleceń: Poprosiła go, żeby zadzwonił do niej wieczorem»)', 'PO s. 187–189 («Mama często powtarza, żebym się uczył hiszpańskiego»; «Babcia prosi mnie, żebym…»)'],
 'R7': ['PO s. 192 («Spójnika „że” używamy przy relacjonowaniu informacji… Spójnika „żeby” — przy relacjonowaniu propozycji, życzeń, rad, próśb, poleceń»)'],
 'R9': ['PO s. 187 («ojciec mi mówi, żebym nie siedział tak długo…»), s. 191 («żebyśmy nie były takie poważne»)'],
}
R['mowa-zalezna'] = {
 'R1': ['PO s. 192 («Mowa zależna to niedokładne relacjonowanie cudzych (albo swoich) słów w zdaniach podrzędnych»: że — informacje, czy — pytania, żeby — prośby, polecenia)', 'PO s. 194 (рамка: kto, co, czy, jak długo, gdzie… że, żeby)'],
 'R2': ['PO s. 192 («„Po południu będę zajęta” → odpowiedziała mu, że po południu będzie zajęta» — время сохраняется)'],
 'R3': ['PO s. 192 («„Masz czas…?” → zapytał ją, czy ma czas»; «„Zadzwoń do mnie” → poprosiła go, żeby zadzwonił do niej»)'],
 'R4': ['PO s. 192 («Zapytał ją, czy ma czas po południu»)'],
 'R5': ['PO s. 194 (Zapytałam go, … proponuje / gdzie… — вопросительное слово сохраняется)'],
 'R6': ['PO s. 192 («poprosiła go, żeby zadzwonił do niej wieczorem»)'],
 'R7': ['PO s. 192 (mowa niezależna: «On zapytał: „Masz czas po południu?”» → mowa zależna без двоеточия и кавычек, с запятой перед czy / że / żeby)'],
 'R9': ['PO s. 192 («Odpowiedziała mu, że…», «Zapytał ją, czy…», «Poprosiła go, żeby…»)', 'PO s. 188 (упражнение «rodzice często mówili (mi, mnie, mną)» → mi)'],
}
R['strona-bierna'] = {
 'R1': ['JPBG XI s. 39 («strona bierna: podmiot jest odbiorcą czynności… W jej skład wchodzą formy osobowe czasowników być lub zostać oraz imiesłów przymiotnikowy bierny»)', 'PO s. 204 («W stronie biernej używamy imiesłowów przymiotnikowych biernych…»)'],
 'R2': ['JPBG XI s. 39 («Stronę bierną tworzymy tylko od czasowników przechodnich (tranzytywnych)»; «W zdaniach w stronie biernej funkcję podmiotu pełni dopełnienie ze strony czynnej»)'],
 'R3': ['JPBG XI s. 20 («Imiesłów przymiotnikowy bierny tworzy się od czasowników przechodnich zarówno dokonanych, jak i niedokonanych»; -ny, -ony, -ty)'],
 'R4': ['JPBG XI s. 20 («-ny, -na, -ne»: czyta-ł → czyta-ny, widzia-ł → widzia-ny)'],
 'R5': ['JPBG XI s. 20 («-ony, -ona, -one»: licz-ysz → liczony, zrob-isz → zrobiony, piecz-esz → pieczony)'],
 'R6': ['JPBG XI s. 20 («-ty, -ta, -te»: zaczę-li → zaczęty, my-li → myty, bi-li → bity)'],
 'R7': ['JPBG XI s. 21 («Imiesłowy … na -ony w mianowniku l.mn. rodzaju męskoosobowego kończą się na -eni»)', 'JPBG XI s. 39 (zostaliśmy przyjęci / zostałyśmy przyjęte; byli witani / były witane)'],
 'R8': ['JPBG XI s. 39 («czasownik posiłkowy zostać występuje tylko w stronie biernej tworzonej od czasowników dokonanych»; «być niekiedy jest używany … od dokonanych: jestem zaproszony»)', 'PO s. 204–205 («form czasownika zostać, jeśli imiesłowy pochodzą od czasowników dokonanych»; упражнение «Być czy zostać?»)'],
 'R9': ['JPBG XI s. 39 («Stronę bierną od czasowników niedokonanych tworzymy przy pomocy czasownika posiłkowego być: jest czytany… będzie oglądany»)', 'PO s. 204 («chętnie była / jest / będzie czytana przez młodzież»)'],
 'R10': ['JPBG XI s. 39–40 (zostanę zatrudniony; «Lekarze przyjmą wszystkich pacjentów → Wszyscy pacjenci zostaną przyjęci przez lekarzy»; będzie oglądany)'],
 'R11': ['PO s. 204 («W stronie biernej używamy konstrukcji: przez kogo, przez co (przez + biernik)»)', 'JPBG XI s. 39 («podmiot ze strony czynnej pełni funkcję dopełnienia wyrażonego w bierniku z przyimkiem przez»)'],
 'R13': ['JPBG XI s. 171 («Formy nieosobowe zakończone na -no, -to … mają znaczenie czasu przeszłego»; «nie zawierają informacji o wykonawcy czynności»)', 'PO s. 209 («FORMY NIEOSOBOWE – są zakończone na -no, -to»)'],
 'R14': ['JPBG XI s. 171–172 («Formy nieosobowe z zaimkiem się tworzymy przez dodanie się do czasownika w 3. osobie liczby pojedynczej»: Dzisiaj czyta się mało gazet)'],
}
R['imieslowy-przyslowkowe'] = {
 'R1': ['JPBG XI s. 62 (współczesny «wskazuje na dwie czynności wykonywane w tym samym czasie; tworzy się go tylko od czasowników niedokonanych»)'],
 'R2': ['JPBG XI s. 62 («do tematu 3. osoby liczby mnogiej czasu teraźniejszego dodajemy końcówkę -ąc: czytaj-ą – czytaj-ąc, pisz-ą – pisz-ąc»)'],
 'R4': ['JPBG XI s. 62 (uprzedni «wskazuje czynność wcześniejszą niż inna; tworzy się go tylko od czasowników dokonanych»)'],
 'R5': ['JPBG XI s. 62 («-wszy, gdy temat czasownika kończy się na samogłoskę: przeczyta-ł – przeczyta-wszy … -łszy, gdy … na spółgłoskę: zjad-ł – zjad-łszy»)'],
 'R6': ['JPBG XI s. 62 («Imiesłów przysłówkowy to nieodmienna i nieosobowa forma czasownika»)'],
 'R7': ['JPBG XI s. 62 («może być tylko jeden podmiot…»; «Kiedy jadł obiad, zaczęła się burza — użycie imiesłowu nie jest możliwe»)'],
 'R8': ['JPBG XI s. 62–63 (примеры с запятыми: «Czytając książkę, jadłam kanapkę»; «Kasia, pisząc wypracowanie, jadła jabłko»)'],
 'R9': ['JPBG XI s. 62 («Imiesłowy przysłówkowe z „nie” pisze się oddzielnie: nie jedząc, nie zjadłszy»)'],
 'R11': ['JPBG XI s. 19 («Imiesłowy przymiotnikowe czynne tworzy się tylko od czasowników niedokonanych przez dodanie do tematu 3. osoby l.mn. czasu teraźniejszego przyrostków -ący, -ąca, -ące»)'],
}
R['imieslowy-przyslowkowe']['R3'] = ['ZJP Por s. 55 (пример употребления: «Anna, będąc odpowiedzialną przyjaciółką, zauważyła…»)']
R['rzeczowniki-odczasownikowe'] = {
 'R1': ['PP s. 86 (narzędnik: «interesuje się … pływaniem, śpiewaniem, malowaniem, gotowaniem, sprzątaniem»)', 'JPBG XI s. 208 («przyznać się do grania w tę grę»)'],
 'R7': ['JPBG XI s. 207 («Dyrektor obiecał pracownikom, że podwyższy płace → … podwyżkę płac»; «Przed przejściem przez ulicę» — дополнение при существительном в родительном)'],
 'R8': ['PO s. 8, 20, 26 («A co jest do jedzenia?», «Co bierzemy do picia?», «czegoś do jedzenia»)'],
 'R9': ['JPBG XI s. 207–208 (замена придаточного предложным оборотом: «Zanim przejdziesz przez ulicę… – Przed przejściem przez ulicę…»; «(w celu)», «(po)», «(podczas)», «(bez)»)'],
}
R['stopniowanie'] = {
 'R1': ['KEY: ключи комиссии, Gramatyka III «Степени сравнения»: najstarszy (03.2022; сборник k4-1), delikatniejszy (02.2022), modniejsze (11.2023), smaczniejsze (06.2024) — tests/b1-*.js'],
 'R2': ['KEY: tańszy (11.2023), tańsze (06.2021), droższe (01.2021, 04.2024), dłuższy (2017, 11.2022), milszy (сборник k12-5), wyższy (06.2021), najniższa (04.2023), bliższy (06.2023), coraz weselszy (сборник k4-1)'],
 'R3': ['KEY: lepszy (2020), lepsza (05.2021), najlepsze (2017), najgorszy (04.2023), większą (02.2023), mniejszą (11.2021)'],
 'R4': ['KEY: bardziej zmęczony, bardziej posłuszny, najmniej opalony (сборник k4-1), najbardziej znanych (06.2021), bardziej niezależne, mniej kosztowne (04.2024)'],
 'R6': ['KEY: gorsi (образец 2020, Gramatyka III)'],
 'R7': ['ZJP s. 22 («Chętniej czyta niż słucha»)', 'PO s. 30 («wolimy lato niż zimę»)'],
 'R9': ['KEY: szybciej (02.2023, 02.2024, сборник k12-5), dłużej (01.2021, 06.2023), łatwiej (2020, 04.2024), rzadziej (02.2024), wyżej (2019), później (06.2022), wcześniej (02.2022)'],
 'R10': ['KEY: więcej (2017, 05.2021, 03.2022, 04.2023, 06.2023, 11.2023, 02.2024), mniej (2020, 11.2022), najlepiej (11.2021, 02.2023), najwięcej (06.2022), najmniej (06.2021)'],
 'R11': ['KEY: сборник k4-1 («coraz bardziej siwy», «coraz weselszy»)'],
}
R['swoj-siebie'] = {
 'R1': ['KEY: сборник 2017, Gramatyka 3.IV (k3-4), пример: «Jan … troszczy się o swoje dzieci. Kiedy patrzę na jego dzieci…»; ответы swojego, swoich, swojej'],
 'R2': ['KEY: k3-4 — пример swoje / jego; п. 3: «zaopiekujemy się waszymi dziećmi» (владелец не подлежащее — не swój)'],
 'R4': ['KEY: k3-4 — ключ принимает обе формы: «ze swoimi / z twoimi uczniami» (п. 5), «swoich / moich obrazów» (п. 9)'],
 'R6': ['KEY: k3-4 (swojego, swoich, swojej, swoimi)', 'PP s. 70 (упражнение: «(swój kot)», «(swój kolega)»)'],
 'R7': ['KEY: сборник 2017, Gramatyka 3.VI (k3-6): выбор siebie / sobie / sobą'],
 'R11': ['KEY: k3-6 («Nie lubiłam wtedy (siebie / sobie / sobą)» → siebie — о самом подлежащем)'],
 'R12': ['KEY: k3-6 («obie zaczęłyśmy ze (sobą) rozmawiać»)', 'PP s. 58, 80 («spędzać ze sobą czas», «lubimy ze sobą rozmawiać»)'],
}
R['zaimki-nieokreslone'] = {
 'R2': ['KEY: образец 2019, Gramatyka I — выбор формы coś / czegoś / czymś по падежу'],
 'R5': ['KEY: образец 2019, Gramatyka I («park, który kiedyś spodoba się…» — kiedyś о будущем)'],
 'R6': ['KEY: сборник 2017, Gramatyka 11.X (k11-10, отрицание): «Nikogo nie lubię i nikomu nie ufam», «Nigdy nie mam na nic czasu»', 'KEY: сборник 2017, 3.VI (k3-6): «Nikt w klasie nie lubił…», «nic nie powiedziałam»'],
 'R7': ['KEY: k11-10 (nikogo, nikomu)', 'KEY: экзамен 02.2022, Gramatyka I (nikt / nikogo / nikim)'],
 'R12': ['KEY: k11-10 («Nikt nie wysłał jeszcze listów do rodziców»)'],
}
R['spojniki-przyczyna-przyzwolenie'] = {
 'R1': ['KEY: ключи комиссии, Gramatyka II «союзы»: ponieważ (2019, 05.2021, 06.2021, 11.2021, 03.2022, 11.2022, 06.2023), bo (01.2021, 02.2022, 02.2023, 11.2023, 04.2024)', 'JPBG XI s. 207 («Nie możemy zrealizować tego zamówienia, ponieważ zabrakło nam towaru»; «Nie poszłam na spacer, bo padał deszcz»)'],
 'R3': ['JPBG XI s. 95, 128 («Często sama terapia nie wystarczy, dlatego że…»; «ludzkość rozwinęła się … dlatego, że ludzie potrafili sobie pomagać»)'],
 'R4': ['ZJP s. 91 («Wynikowe: więc, dlatego, zatem, toteż»; «Jutro wyjeżdżam, więc nie będzie mnie w domu»; «Nie mam samochodu, dlatego w mieście poruszam się rowerem»)', 'KEY: więc (2020, 02.2023, 04.2023, 11.2023, 04.2024), dlatego (01.2021, 05.2021, 06.2021, 06.2022)'],
 'R5': ['JPBG XI s. 207 (замена: «Nie poszłam na spacer, bo padał deszcz. (z powodu)»; «… ze względu na brak towaru»)'],
 'R6': ['KEY: chociaż (11.2021, 02.2022; сборник 12.VI, k12-6)', 'JPBG XI s. 207 («Chociaż miał dobre chęci, nie zdążył zrobić prezentacji» — без ale в главной части)'],
 'R8': ['JPBG XI s. 207 («Chociaż miał dobre chęci… (mimo)» → mimo + dopełniacz)'],
 'R9': ['ZJP s. 91 («Przeciwstawne: ale, lecz, jednak, a, zaś, natomiast»; «Miał padać deszcz, jednak niebo było bezchmurne»)', 'KEY: jednak (03.2022, Gramatyka II)'],
 'R10': ['ZJP s. 91 (przeciwstawne: ale, lecz)', 'KEY: ale (2020, 05.2021, 06.2022, 11.2023, 04.2024), lecz (2019, 02.2023, 02.2024)'],
}
