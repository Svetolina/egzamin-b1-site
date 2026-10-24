# Образцы письменных заданий. Для тем 4–10 — тексты черновика (где коротки — дополнены до объёма задания),
# для тем 11–19 в черновике образцов не было — написаны заново.
MODELS = {

# ---------- czasowniki ruchu ----------
('czasowniki-ruchu', 'w1'): {
 'need': 'Не меньше 5 глаголов движения, из них 3 с приставкой; транспорт в творительном; предлоги do / z / przez / na.',
 'forms': ['wyjdziesz', 'przejdź', 'idź', 'jedź', 'wysiądź', 'wejdź', 'wjedź', 'tramwajem'],
},
('czasowniki-ruchu', 'w2'): {
 'need': 'Привычка с разнонаправленным глаголом, фон с szedłem / jechałam, не меньше 4 приставочных глаголов в прошедшем.',
 'model': 'Zwykle jeżdżę do rodziców pociągiem, ale w zeszłe święta postanowiłam pojechać autobusem, bo było taniej. Wyszłam z domu bardzo wcześnie i poszłam na dworzec. Autobus przyjechał punktualnie i wszystko było dobrze. Kiedy jechaliśmy przez góry, nagle zaczął padać śnieg. Kierowca zatrzymał autobus i powiedział, że dalej nie pojedziemy. Wszyscy wysiedliśmy i poszliśmy pieszo do małej wioski. Szliśmy przez las prawie godzinę, a śnieg ciągle padał. Tam weszliśmy do restauracji i czekaliśmy trzy godziny. W końcu przyjechał inny autobus i dojechaliśmy do miasta w nocy. Mama czekała na przystanku. Byłam zmęczona, ale cała i zdrowa. Kierowca autobusu bardzo nas przepraszał. Od tamtej pory zawsze jeżdżę pociągiem!',
 'forms': ['jeżdżę', 'jechaliśmy', 'szliśmy', 'wyszłam', 'przyjechał', 'wysiedliśmy', 'weszliśmy', 'dojechaliśmy'],
},

# ---------- dopełniacz po negacji ----------
('dopelniacz-po-negacji', 'w1'): {
 'need': 'Не меньше 3 «nie było + родительный» и 3 «nie + глагол + родительный»; одно отрицание без смены падежа.',
 'model': 'Szanowni Państwo,\nw dniach 3–7 sierpnia mieszkałam w Państwa hotelu. Niestety, nie jestem zadowolona z pobytu. W ofercie był basen, ale na miejscu nie było basenu. W pokoju nie było klimatyzacji ani sejfu, a przez dwa dni nie mieliśmy ciepłej wody. Codziennie prosiłam o nowe ręczniki, ale nie dostałam ręczników ani razu. W restauracji nie było też wegetariańskich dań. Przez cały pobyt nie widziałam też sprzątaczki. Recepcja nie interesowała się naszymi problemami i nikt nam nie pomógł. Oczekuję zwrotu części pieniędzy i przeprosin.\nZ poważaniem\nIrina Petrenko',
 'forms': ['basenu', 'klimatyzacji', 'sejfu', 'ciepłej wody', 'ręczników', 'dań', 'naszymi problemami'],
},
('dopelniacz-po-negacji', 'w2'): {
 'need': 'Nie ma / nie było / nie będzie + родительный; żaden или nigdy… nie; две группы «прилагательное + существительное» в родительном.',
 'model': 'Mieszkam na małym osiedlu na obrzeżach miasta. Jest tu spokojnie, ale brakuje wielu rzeczy. Nie ma dużego supermarketu ani żadnej dobrej kawiarni. Nie ma też żadnego kina. Dziesięć lat temu nie było nawet przystanku autobusowego i wszyscy jeździli samochodami. Teraz mamy autobus, ale nie ma ścieżki rowerowej. Dzieci nie mają placu zabaw, więc bawią się na parkingu. Miasto obiecało nowy park, ale w tym roku na pewno nie będzie pieniędzy na inwestycje. Mimo to lubię to miejsce i nigdy nie chciałam się stąd wyprowadzić.',
 'forms': ['dużego supermarketu', 'żadnej dobrej kawiarni', 'przystanku autobusowego', 'ścieżki rowerowej', 'placu zabaw', 'pieniędzy'],
},

# ---------- liczebniki ----------
('liczebniki-z-rzeczownikami', 'w1'): {
 'need': 'Не меньше 6 сочетаний числительное + существительное из разных групп; мужско-личная форма; dwoje / troje dzieci.',
 'forms': ['dwadzieścia dwie osoby', 'piętnastu dorosłych', 'pięciu kolegów', 'dwoje dzieci', 'trzy duże sałatki', 'ośmiuset złotych'],
},
('liczebniki-z-rzeczownikami', 'w2'): {
 'need': 'Возраст с lata и lat, не меньше 2 форм с 5+ и 2 с 2–4, собирательное или мужско-личное, глагол в согласовании с 5+.',
 'model': 'Moja rodzina jest duża. Mam męża i troje dzieci. Najstarszy syn ma dwadzieścia dwa lata, córka ma osiemnaście lat, a najmłodszy syn — pięć lat. Mieszkamy w domu, który ma sześć pokoi i dwie łazienki. Mamy też dwa koty i jednego psa. W Polsce mieszkamy od siedmiu lat. Mój mąż ma trzech braci, więc na święta przyjeżdża do nas dwanaście osób. W zeszłe święta przy stole siedziało aż piętnaście osób! Było głośno, ale bardzo wesoło. Na kolację przygotowałam dwanaście dań. Razem było nas osiemnaście osób.',
 'forms': ['troje dzieci', 'dwadzieścia dwa lata', 'osiemnaście lat', 'sześć pokoi', 'dwie łazienki', 'trzech braci', 'siedziało'],
},

# ---------- tryb przypuszczający ----------
('tryb-przypuszczajacy', 'w1'): {
 'need': 'Не меньше 2 предложений с gdyby и 5 форм условного наклонения; одно реальное условие с jeśli; одно chciałbym, żeby…',
 'model': 'Gdybym mogła zmienić jedną rzecz w moim mieście, zbudowałabym więcej ścieżek rowerowych. Teraz wszyscy jeżdżą samochodami i w centrum są korki. Gdyby było więcej ścieżek, ludzie jeździliby do pracy na rowerze, a powietrze byłoby czystsze. Dzieci mogłyby bezpiecznie dojeżdżać do szkoły, a rodzice nie musieliby ich wozić. Chciałabym też, żeby miasto posadziło więcej drzew. Wtedy latem w centrum byłoby chłodniej. Na pewno mieszkałoby się tu przyjemniej. Jeśli władze miasta przeczytają ten wpis, może coś się zmieni! A wy? Co zmienilibyście w swoim mieście?',
 'forms': ['zbudowałabym', 'jeździliby', 'byłoby', 'mogłyby', 'musieliby', 'zmienilibyście'],
},
('tryb-przypuszczajacy', 'w2'): {
 'need': 'Chciałbym / Chciałabym…, не меньше 2 вежливых вопросов (Czy mogliby Państwo…? Czy byłaby możliwość…?), Byłbym wdzięczny / Byłabym wdzięczna…',
 'model': 'Szanowni Państwo,\nchciałabym zapisać się na kurs języka polskiego na poziomie B1. Czy mogliby Państwo przesłać mi informacje o terminach zajęć w semestrze zimowym? Najbardziej odpowiadałyby mi zajęcia wieczorem, ponieważ pracuję do siedemnastej. Chciałabym też zapytać o cenę kursu. Interesowałby mnie również kurs online. Czy mogłabym najpierw przyjść na lekcję próbną? Czy byłaby możliwość zapłacenia w dwóch ratach? Byłabym wdzięczna za szybką odpowiedź.\nZ poważaniem\nAnna Kowalenko',
 'forms': ['chciałabym', 'mogliby', 'odpowiadałyby', 'byłaby', 'byłabym'],
},

# ---------- tryb rozkazujący ----------
('tryb-rozkazujacy', 'w1'): {
 'need': 'Не меньше 5 форм для ty: 3 совершенных и 2 запрета с nie + несовершенный; одно nie + совершенный (предупреждение); одна форма niech.',
 'model': 'Cześć Kuba!\nKlucze są u sąsiadki, pani Ewy. Rozgość się! Weź z lodówki, co chcesz. Zjedz też ciasto z lodówki. Wieczorem podlej kwiaty na balkonie i wyrzuć śmieci. Nie otwieraj okna w sypialni — jest zepsute. Nie używaj też pralki, bo cieknie. Jeśli ktoś zadzwoni domofonem, niech zostawi paczkę pod drzwiami. Uważaj, nie zgub kluczy i nie zapomnij zamknąć drzwi, kiedy wychodzisz!\nDobrej zabawy,\nAnia',
 'forms': ['weź', 'podlej', 'wyrzuć', 'nie otwieraj', 'nie używaj', 'niech zostawi', 'nie zgub', 'nie zapomnij'],
},
('tryb-rozkazujacy', 'w2'): {
 'need': 'Не меньше 4 конструкций proszę + инфинитив, одна форма niech, без форм для ty.',
 'forms': ['proszę zapisywać się', 'proszę nie zostawiać', 'proszę wyczyścić', 'proszę nie palić', 'niech oddadzą'],
},

# ---------- zdania z który ----------
('zdania-ktory', 'w1'): {
 'need': 'Не меньше 5 предложений с który в разных падежах, 2 — с предлогом, одно во мн. ч.; jaki или co.',
 'model': 'Osoba, która jest dla mnie bardzo ważna, to moja babcia Hanna. To kobieta, którą wszyscy w rodzinie podziwiają. Ma siwe włosy i oczy, które zawsze się śmieją. Mieszka w małym domu, w którym spędziłam całe dzieciństwo. Babcia ma ogród, o który dba codziennie. Ludzie, którzy ją znają, mówią, że jest najlepszą sąsiadką, jaką można mieć. To ona nauczyła mnie gotować i czytać. Wszystko, co dziś umiem, zawdzięczam też jej. Jest osobą, z którą mogę porozmawiać o wszystkim. Dzwonię do niej co tydzień.',
 'forms': ['która', 'którą', 'które', 'w którym', 'o który', 'którzy', 'jaką', 'co', 'z którą'],
},
('zdania-ktory', 'w2'): {
 'need': 'Заголовок, не меньше 4 предложений с który, одно с предлогом + który, контакт.',
 'forms': ['który', 'która', 'na które', 'w której', 'które'],
},

# ---------- 11 żeby / aby ----------
('zeby-aby', 'w1'): {
 'need': 'Не меньше 4 конструкций с żeby, 2 — с другим субъектом (żebyś, żebyśmy), одна żeby nie…',
 'model': 'Cześć Kasiu!\nW sobotę przeprowadzam się do nowego mieszkania, bo chcę mieszkać bliżej pracy. Mam do Ciebie wielką prośbę. Czy mogłabyś przyjść w sobotę rano, żeby pomóc mi spakować książki i naczynia? Chciałabym, żebyśmy skończyły do południa, bo samochód przyjedzie o pierwszej. Wieczorem zapakuję ubrania, żeby nie tracić czasu w sobotę. Poproszę też brata, żeby przyniósł kartony. Może też Twój mąż mógłby przyjść, żeby pomóc nosić meble? Chcę, żebyś po wszystkim została na kolację. Ugotuję Twoje ulubione pierogi, żeby Ci podziękować! Daj znać, czy masz czas.\nŚciskam,\nOla',
 'forms': ['żeby pomóc', 'żebyśmy skończyły', 'żeby nie tracić', 'żeby przyniósł', 'żebyś po wszystkim została', 'żeby Ci podziękować'],
},
('zeby-aby', 'w2'): {
 'need': 'Официальное обращение, не меньше 3 конструкций с aby, просьба «Uprzejmie proszę, aby…», подпись Z poważaniem.',
 'model': 'Szanowni Państwo,\nod tygodnia w moim mieszkaniu przy ulicy Długiej 15 m. 8 nie działa ogrzewanie. Kaloryfery są zimne, a temperatura w pokojach spadła do piętnastu stopni. Zgłaszałam problem telefonicznie, ale nikt nie przyszedł. Uprzejmie proszę, aby Państwo jak najszybciej przysłali fachowca. Proszę również, aby ktoś zadzwonił do mnie wcześniej, abym mogła być w domu w czasie wizyty. Najlepiej pasowałby mi termin po godzinie szesnastej. Mój numer telefonu to 600 100 200. Proszę też o kontakt mailowy, aby potwierdzić termin. Liczę na szybką reakcję.\nZ poważaniem\nMaria Kowalczyk',
 'forms': ['aby Państwo jak najszybciej przysłali', 'aby ktoś zadzwonił', 'abym mogła', 'aby potwierdzić'],
},

# ---------- 12 strona bierna ----------
('strona-bierna', 'w1'): {
 'need': 'Не меньше 4 форм страдательного залога, один исполнитель с przez + винительный, 2 формы на -no / -to, без «ja».',
 'model': 'Nowy park w centrum miasta\nW sobotę w naszym mieście został otwarty nowy park nad rzeką. Uroczystość została zorganizowana przez urząd miasta. Na otwarcie zaproszono mieszkańców i uczniów z pobliskich szkół. Park został zaprojektowany przez młodą architektkę z Poznania. Posadzono w nim ponad dwieście drzew, a przy wejściu zbudowano plac zabaw dla dzieci. Wieczorem na scenie zagrał lokalny zespół. W przyszłym roku obok parku zostanie zbudowana ścieżka rowerowa, a stary most zostanie wyremontowany. Mieszkańcy są zadowoleni, bo na taki park czekali wiele lat.',
 'forms': ['został otwarty', 'została zorganizowana', 'zaproszono', 'został zaprojektowany', 'posadzono', 'zbudowano', 'zostanie zbudowana', 'zostanie wyremontowany'],
},
('strona-bierna', 'w2'): {
 'need': 'Даты с zostać, процесс с być, состояние сегодня, одна форма будущего.',
 'model': 'Pałac Kultury i Nauki w Warszawie\nPałac Kultury i Nauki to najwyższy budynek w Warszawie. Był budowany przez trzy lata, od tysiąc dziewięćset pięćdziesiątego drugiego roku. Został zaprojektowany przez rosyjskiego architekta. Wtedy był nazywany darem od Związku Radzieckiego. Przez wiele lat odbywały się w nim koncerty i kongresy, a w kinach były pokazywane filmy. Później budynek został częściowo wyremontowany. Dziś Pałac jest używany przez teatry, muzea i biura. Jest otwarty dla turystów codziennie, a z tarasu widać całe miasto. Za kilka lat wokół Pałacu zostanie zbudowany nowy plac.',
 'forms': ['był budowany', 'został zaprojektowany', 'był nazywany', 'były pokazywane', 'został częściowo wyremontowany', 'jest używany', 'jest otwarty', 'zostanie zbudowany'],
},

# ---------- 13 mowa zależna ----------
('mowa-zalezna', 'w1'): {
 'need': 'Не меньше 2 утверждений с że, вопрос с czy и вопрос с вопросительным словом, просьба с żeby; время не сдвинуто, без кавычек.',
 'model': 'Cześć Marek!\nWczoraj poznałam nowego sąsiada. Ma na imię Piotr. Powiedział, że jest informatykiem i pracuje w dużej firmie w centrum. Opowiedział też, że ma psa i dwoje dzieci. Zapytał mnie, czy długo tu mieszkam i gdzie jest najbliższy sklep. Odpowiedziałam, że mieszkam tu od trzech lat, a sklep jest za rogiem. Potem zapytał, kiedy przyjeżdża śmieciarka. Na koniec poprosił mnie, żebym podlewała jego kwiaty, kiedy wyjedzie na urlop. Powiedziałam, że chętnie mu pomogę. Wydaje się bardzo miły!\nPozdrawiam,\nAnia',
 'forms': ['powiedział, że', 'zapytał mnie, czy', 'gdzie jest', 'kiedy przyjeżdża', 'poprosił mnie, żebym', 'odpowiedziałam, że'],
},
('mowa-zalezna', 'w2'): {
 'need': 'Kto dzwonił i co powiedział (że), o co pytał (czy / kiedy), o co prosił (żebyś); правильные падежи после powiedzieć / zapytać.',
 'model': 'Cześć Tomek,\ndzwonił do Ciebie pan Nowak z firmy Delta. Powiedział, że jest Twoim nowym klientem i że wysłał Ci wczoraj zamówienie. Pytał, czy już je dostałeś i kiedy może dostać fakturę. Prosił, żebyś do niego oddzwonił jeszcze dzisiaj. Powiedział mi, że będzie w biurze do szesnastej. Jego numer masz w mailu.\nPozdrawiam,\nKasia',
 'forms': ['powiedział, że', 'pytał, czy', 'kiedy może', 'prosił, żebyś', 'powiedział mi'],
},

# ---------- 14 stopniowanie ----------
('stopniowanie', 'w1'): {
 'need': 'Не меньше 5 форм сравнительной степени, одна неправильная, сравнение с niż и с od, одна превосходная, coraz или im… tym.',
 'model': 'Gdzie lepiej mieszkać?\nMieszkałam w dużym mieście i na wsi, więc mogę porównać. W mieście życie jest droższe, mieszkania są mniejsze, a czynsz jest wyższy niż na wsi. Za to transport jest dużo lepszy: autobusy jeżdżą częściej i szybciej dojeżdżam do pracy. Na wsi jest spokojniej i ciszej, a powietrze jest czystsze. Przyroda jest piękniejsza od miejskich parków. Największym problemem na wsi jest praca, bo ofert jest coraz mniej. Im dłużej mieszkam w mieście, tym bardziej tęsknię za spokojem. Mimo to na razie wybieram miasto, bo tu mam pracę.',
 'forms': ['droższe', 'mniejsze', 'wyższy niż', 'lepszy', 'częściej', 'czystsze', 'piękniejsza od', 'największym', 'coraz mniej', 'im dłużej', 'tym bardziej'],
},
('stopniowanie', 'w2'): {
 'need': 'Не меньше 4 сравнений, одна описательная форма (bardziej / mniej), одна мужско-личная (milsi), одна превосходная с z / w.',
 'model': 'Cześć!\nSzukałam dla Was hotelu w Krakowie i porównałam dwa. Hotel „Wawel” jest tańszy od hotelu „Rynek” o sto złotych za noc, ale jest dalej od centrum. Do Rynku idzie się stamtąd dwadzieścia minut. Pokoje w „Rynku” są większe i bardziej nowoczesne, a łóżka są wygodniejsze. Pracownicy w „Rynku” są też milsi i lepiej mówią po angielsku. Śniadania w obu hotelach są dobre, ale w „Rynku” wybór jest większy. Według opinii to jeden z najlepszych hoteli w mieście. Dlatego polecam Wam „Rynek” — jest droższy, ale warto!\nBuziaki,\nIrena',
 'forms': ['tańszy od', 'dalej', 'większe', 'bardziej nowoczesne', 'wygodniejsze', 'milsi', 'lepiej', 'jeden z najlepszych', 'droższy'],
},

# ---------- 15 swój / siebie ----------
('swoj-siebie', 'w1'): {
 'need': 'Не меньше 4 форм swój в разных падежах, 2 формы jego / jej / ich, ни одного swój в подлежащем, sobie или ze sobą.',
 'model': 'Moja rodzina\nMoja siostra Ola mieszka w Gdańsku ze swoim mężem i dwójką dzieci. Jej mąż jest lekarzem, a ich syn chodzi już do szkoły. Ola bardzo kocha swoją pracę w bibliotece i często opowiada o swoich czytelnikach. Mój brat Paweł mieszka sam. Jego mieszkanie jest małe, ale ma w nim swój ulubiony fotel i dużo książek. W weekendy jeździ na rowerze ze swoimi kolegami. Moi rodzice mieszkają na wsi. Mają duży ogród i sami uprawiają warzywa dla siebie i dla nas. Kiedy się spotykamy, zawsze mamy sobie dużo do powiedzenia.',
 'forms': ['ze swoim mężem', 'swoją pracę', 'o swoich czytelnikach', 'swój ulubiony fotel', 'ze swoimi kolegami', 'jej mąż', 'ich syn', 'jego mieszkanie', 'dla siebie', 'sobie'],
},
('swoj-siebie', 'w2'): {
 'need': 'Ze sobą, sobie, siebie — хотя бы по одному разу; взаимное действие с się; nawzajem; 2 формы swój.',
 'model': 'Cześć Magda!\nWłaśnie wróciłam z Zakopanego. Pojechałam tam z Kasią i Michałem. Każdy wziął ze sobą tylko jeden plecak, bo chcieliśmy chodzić po górach. Codziennie spotykaliśmy się rano na śniadaniu i planowaliśmy trasę. W górach bardzo sobie pomagaliśmy: Michał niósł wodę dla wszystkich, a ja miałam swoją apteczkę. Wieczorami opowiadaliśmy sobie historie ze swojego dzieciństwa i dużo się śmialiśmy. Na pamiątkę kupiliśmy sobie wełniane czapki. Kasia kupiła też coś dla siebie — piękny sweter. Obiecaliśmy sobie nawzajem, że za rok znowu pojedziemy razem.\nŚciskam,\nZuza',
 'forms': ['ze sobą', 'spotykaliśmy się', 'sobie pomagaliśmy', 'swoją apteczkę', 'ze swojego dzieciństwa', 'dla siebie', 'sobie nawzajem'],
},

# ---------- 16 imiesłowy przysłówkowe ----------
('imieslowy-przyslowkowe', 'w1'): {
 'need': 'Не меньше 3 форм на -ąc и 2 на -wszy / -łszy; подлежащее везде одно; запятые вокруг оборотов; nie + деепричастие раздельно.',
 'model': 'Dzień, którego nie zapomnę\nTo był zwykły poniedziałek. Wstawszy wcześnie, zjadłam szybkie śniadanie i wyszłam z domu. Idąc na przystanek, zobaczyłam na chodniku mały portfel. Podniósłszy go, zajrzałam do środka: były tam dokumenty i dużo pieniędzy. Nie wiedząc, co zrobić, zadzwoniłam do mojego brata. Słuchając jego rady, poszłam na policję. Spiesząc się potem do biura, wiedziałam, że się spóźnię, ale byłam szczęśliwa. Wieczorem zadzwoniła do mnie starsza pani, właścicielka portfela. Dziękując mi, płakała ze wzruszenia. Następnego dnia przyniosła mi do pracy pyszne ciasto.',
 'forms': ['wstawszy', 'idąc', 'podniósłszy', 'nie wiedząc', 'słuchając', 'spiesząc się', 'dziękując'],
},
('imieslowy-przyslowkowe', 'w2'): {
 'need': 'Będąc w…, warto…; chcąc…, należy…; один устойчивый оборот (mówiąc szczerze, biorąc pod uwagę); одна форма на -ący.',
 'model': 'Poradnik dla turystów: Szczecin\nBędąc w Szczecinie, warto zobaczyć Wały Chrobrego i zamek. Chcąc poznać miasto szybko, należy kupić bilet dobowy na tramwaje. Spacerując po centrum, warto mieć w telefonie mapę, bo ulice tworzą gwiazdy. Mówiąc szczerze, najpiękniej jest tu wieczorem. Wychodząc wieczorem, warto zabrać ciepłą kurtkę, bo od morza wieje wiatr. Nie znając języka, można spokojnie pytać ludzi o drogę. Osoby lubiące przyrodę powinny pojechać nad jezioro Szmaragdowe. Biorąc pod uwagę pogodę, lepiej przyjechać latem.',
 'forms': ['będąc', 'chcąc', 'spacerując', 'mówiąc szczerze', 'lubiące', 'biorąc pod uwagę'],
},

# ---------- 17 rzeczowniki odczasownikowe ----------
('rzeczowniki-odczasownikowe', 'w1'): {
 'need': 'Не меньше 6 отглагольных существительных, дополнения в родительном, хотя бы 3 разных предлога (po, przed, podczas, w celu), официальный стиль.',
 'model': 'Regulamin domu studenckiego\n1. Palenie papierosów w budynku jest zabronione.\n2. Picie alkoholu w kuchni jest niedozwolone.\n3. Cisza nocna obowiązuje od 22:00 do 6:00.\n4. Podczas ciszy nocnej słuchanie głośnej muzyki jest zabronione.\n5. Po gotowaniu należy umyć naczynia.\n6. Przed wyjazdem obowiązkowe jest oddanie klucza w recepcji.\n7. W celu przedłużenia pobytu prosimy o kontakt z administracją.\n8. Przyjmowanie gości jest możliwe do godziny 21:00.\n9. Za zniszczenie wyposażenia płaci mieszkaniec.',
 'forms': ['palenie papierosów', 'picie alkoholu', 'podczas ciszy', 'słuchanie głośnej muzyki', 'po gotowaniu', 'przed wyjazdem', 'oddanie klucza', 'w celu przedłużenia', 'przyjmowanie gości', 'zniszczenie'],
},
('rzeczowniki-odczasownikowe', 'w2'): {
 'need': 'Interesuję się …-niem, moje hobby to…, 2 формы с po / podczas, lubię + инфинитив.',
 'model': 'Moje zainteresowania\nInteresuję się gotowaniem i podróżowaniem. Moje hobby to pieczenie chleba. W weekendy lubię gotować dla przyjaciół i próbować nowych przepisów. Po pracy często chodzę na pływanie, bo pływanie pomaga mi odpocząć. Podczas podróży zawsze robię zdjęcia i kupuję lokalne przyprawy. Lubię też czytanie kryminałów, szczególnie przed spaniem. Nie lubię natomiast sprzątania i prasowania. Najgorsze jest dla mnie mycie okien! Na szczęście mój mąż lubi porządki. Marzę o zwiedzaniu Japonii i nauce japońskiej kuchni. W przyszłym roku planuję zapisanie się na kurs tańca.',
 'forms': ['gotowaniem', 'podróżowaniem', 'pieczenie chleba', 'pływanie', 'podczas podróży', 'czytanie kryminałów', 'przed spaniem', 'sprzątania', 'prasowania', 'mycie okien', 'zwiedzaniu'],
},

# ---------- 18 zaimki nieokreślone ----------
('zaimki-nieokreslone', 'w1'): {
 'need': 'Не меньше 5 отрицательных слов (nikt, nic, nigdy, nigdzie, żaden), везде nie при глаголе, żaden в родительном, официальное обращение и подпись.',
 'model': 'Szanowni Państwo,\nw zeszłym tygodniu spędziłem trzy noce w Państwa hotelu i niestety jestem bardzo rozczarowany. Nic nie działało tak, jak obiecano w ofercie. Kiedy dzwoniłem do recepcji, nikt nie odbierał telefonu. W pokoju nie było żadnych ręczników ani mydła. Nigdzie nie można było zaparkować samochodu, chociaż parking był w cenie. Nikogo nie interesowały moje skargi. Nigdzie w mieście nie widziałem tak brudnego hotelu. Nigdy wcześniej nie spotkałem się z taką obsługą. Proszę o zwrot części pieniędzy i odpowiedź na tego maila.\nZ poważaniem\nAndrzej Nowicki',
 'forms': ['nic nie działało', 'nikt nie odbierał', 'żadnych ręczników', 'nigdzie nie można', 'nikogo nie interesowały', 'nigdy wcześniej nie spotkałem'],
},
('zaimki-nieokreslone', 'w2'): {
 'need': 'Szukam kogoś, kto…; одна форма jakiś в нужном роде; одна форма на -kolwiek; coś + прилагательное в родительном.',
 'model': 'Szukam kogoś do opieki nad kotem!\nW sierpniu wyjeżdżam na dwa tygodnie i szukam kogoś, kto zaopiekuje się moim kotem. Kot jest spokojny i nie potrzebuje niczego specjalnego. Wystarczy go karmić i trochę się z nim pobawić. Może jakaś studentka z osiedla? Zapłacę i zostawię w lodówce coś dobrego dla opiekuna. Proszę dzwonić kiedykolwiek po osiemnastej: 600 300 400.',
 'forms': ['kogoś, kto', 'niczego specjalnego', 'jakaś studentka', 'coś dobrego', 'kiedykolwiek'],
},

# ---------- 19 spójniki ----------
('spojniki-przyczyna-przyzwolenie', 'w1'): {
 'need': 'Официальные ponieważ, gdyż, zatem; z powodu + родительный; уступка (chociaż, mimo że, mimo + родительный); dlatego или więc; без bo в начале предложения.',
 'model': 'Szanowni Państwo,\npiszę do Państwa, ponieważ jestem niezadowolona z wycieczki do Grecji, którą kupiłam w Państwa biurze. W ofercie był hotel przy plaży, jednak mieszkaliśmy dwa kilometry od morza. Codziennie musieliśmy jeździć autobusem, dlatego traciliśmy dużo czasu. Z powodu remontu basen był zamknięty przez cały tydzień. Chociaż płaciliśmy za wycieczki z przewodnikiem, przewodnik dwa razy nie przyszedł, gdyż był chory. Hotel był też głośny z powodu dyskoteki obok. Mimo naszych próśb nikt nie zaproponował nam innego rozwiązania. Wycieczka nie była zatem taka, jak w ofercie. Mimo że rozumiem trudności, oczekuję zwrotu części pieniędzy, więc proszę o szybką odpowiedź. Liczę na zrozumienie.\nZ poważaniem\nOksana Melnyk',
 'forms': ['ponieważ', 'dlatego', 'z powodu remontu', 'chociaż', 'gdyż', 'mimo naszych próśb', 'zatem', 'mimo że', 'więc'],
},
('spojniki-przyczyna-przyzwolenie', 'w2'): {
 'need': 'Две причины (bo, ponieważ), две уступки (chociaż, mimo + родительный), mimo to или jednak, dzięki + дательный, вывод с więc или dlatego.',
 'model': 'Praca zdalna — tak czy nie?\nOd roku pracuję z domu i jestem zadowolona, bo nie tracę czasu na dojazdy. Dzięki temu mam więcej czasu dla rodziny. Pracuję też spokojniej, ponieważ nikt mi nie przeszkadza. Chociaż w domu jest wygodnie, czasem brakuje mi rozmów z kolegami. Mimo dobrego internetu spotkania online są męczące. Niektórzy mówią, że w domu trudno się skupić. Mimo to uważam, że praca zdalna jest lepsza, jeśli ma się swój pokój. Najlepiej pracować w biurze raz albo dwa razy w tygodniu, więc wybieram model mieszany.',
 'forms': ['bo', 'dzięki temu', 'ponieważ', 'chociaż', 'mimo dobrego internetu', 'mimo to', 'więc'],
},
}
