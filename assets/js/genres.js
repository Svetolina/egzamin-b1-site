/* Справочные данные для письма: требования к жанрам и шкалы оценки.
   Источники: методичка комиссии «Pisanie» (жанры, образцы оценённых работ) и тест-образец B1 2020 (шкала из 30 баллов). */
(function(){
'use strict';
var B1=window.B1=window.B1||{};

B1.genres={
  zyczenia:{pl:'Życzenia',req:[
    'miejsce i data',
    'обращение к адресату: звательный падеж с «!», в первой строке по центру (в нейтральном тексте не обязательно)',
    'основная часть: повод и пожелания, логично выстроенные, части графически отделены',
    'подпись под текстом справа',
    'официальные: формальные обращения и полное имя с фамилией; частные: неформальные, можно только имя']},
  pozdrowienia:{pl:'Pozdrowienia',req:[
    'miejsce i data (правый верхний или левый нижний угол)',
    'обращение к адресату: звательный падеж с «!», по центру',
    'основная часть',
    'подпись под текстом справа',
    'официальные: формальные обращения и полное имя; частные: неформальные, можно только имя']},
  zaproszenie:{pl:'Zaproszenie',req:[
    'kto i kogo zaprasza',
    'z jakiej okazji',
    'gdzie i kiedy odbędzie się wydarzenie',
    'по желанию: dress code и просьба подтвердить приход',
    'официальное: формальные обращения, подпись полным именем; частное: неформальные обращения, можно только имя (справа под текстом)']},
  zawiadomienie:{pl:'Zawiadomienie',req:[
    'miejsce i data',
    'co, gdzie, kiedy ma się wydarzyć (lub się wydarzyło)',
    'kto zawiadamia',
    'стиль зависит от того, официальное оно или частное']},
  ogloszenie:{pl:'Ogłoszenie',req:[
    'kto ogłasza (osoba prywatna, instytucja)',
    'w jakim celu (sprzedaje, kupuje, zamienia, wynajmuje, poszukuje)',
    'co jest przedmiotem ogłoszenia',
    'jak się skontaktować (telefon, adres)',
    'текст должен быть кратким']},
  list:{pl:'List',req:[
    'в правом верхнем углу: miejsce i data',
    'grzecznościowy zwrot do adresata: звательный падеж с «!» (Szanowny Panie Dyrektorze!, Kochana Babciu!)',
    'wstęp (цель письма), rozwinięcie, zakończenie (могут быть просьбы или пожелания)',
    'заключительная формула (Serdecznie pozdrawiam, Całuję)',
    'podpis, при желании PS',
    'частное неформальное: на «ты», разговорный тон; частное формальное: на «Вы» (Pan/Pani), вежливые формулы']},
  opis_osoby:{pl:'Opis osoby',req:[
    'wstęp: imię, nazwisko, wiek, okoliczności, w których autor poznał osobę',
    'rozwinięcie: wygląd (sylwetka, twarz, oczy, włosy, sposób ubierania się)',
    'zakończenie: komentarz i odczucia autora',
    'описание объективное, в определённом порядке']},
  charakterystyka:{pl:'Charakterystyka',req:[
    'dane postaci (imię, wiek, zawód)',
    'wygląd zewnętrzny (wzrost, figura, kolor włosów i oczu)',
    'cechy charakteru (pozytywne i negatywne)',
    'cechy umysłowe (mądry, zdolny)',
    'zainteresowania',
    'ocena postaci (sympatyczny, nie lubię go)']},
  opowiadanie:{pl:'Opowiadanie',req:[
    'три части: wstęp, rozwinięcie, zakończenie',
    'обычно прошедшее время, могут быть диалоги, от 1-го или 3-го лица',
    'свой замысел и логичная последовательность событий'],
    phrases:[
      'Wstęp: Zdarzyło się to... / Było to... / Działo się to... / Pewnego dnia... / Pewnego razu...',
      'Rozwinięcie: kiedy? kilka lat/dni/tygodni temu, niedawno, wczoraj. Gdzie? w pewnym mieście, na wsi, w górach, nad morzem. Kto? pewien pan, pewna pani, jakiś człowiek. Co się wydarzyło? nagle..., w pewnej chwili..., w pewnym momencie...',
      'Zakończenie: W końcu... / Aż wreszcie... / Kiedy wróciliśmy... / Cała ta historia...']},
  sprawozdanie:{pl:'Sprawozdanie',req:[
    'czas, miejsce, okoliczności, cel wydarzeń',
    'przebieg wydarzeń (chronologicznie)',
    'ocena wydarzeń',
    'обычно прошедшее время; это отчёт о поездке, отпуске, концерте, соревновании']
    ,phrases:[
      'Początek: W zeszłym miesiącu byliśmy na wycieczce w Krakowie.',
      'Przebieg: Zwiedziliśmy Wawel i... Potem spacerowaliśmy po Rynku. Wieczorem...',
      'Ocena: Kraków bardzo mi się podobał.']},
  recenzja:{pl:'Recenzja (własna opinia)',req:[
    'wstęp: о чём вы высказываете мнение',
    'rozwinięcie: элементы описания, пересказа, отчёта',
    'zakończenie: субъективная оценка с обоснованием']
    ,phrases:[
      'Wstęp: W sobotę w klubie... wystąpił mój ulubiony zespół...',
      'Rozwinięcie: Koncert zaczął się od... Publiczność tańczyła...',
      'Zakończenie: Bardzo się cieszę, że poszłam na ten koncert, ponieważ...']},
  esej:{pl:'Esej',req:[
    'три части: wstęp, rozwinięcie, zakończenie',
    'субъективные взгляды автора: мнение, комментарий, размышления, чувства',
    'аргументы в поддержку этих взглядов']
    ,phrases:[
      'Wstęp: Ostatnio wszyscy mówią o... / Warto zastanowić się nad...',
      'Rozwinięcie: Wydaje mi się, że... / Uważam... / Sądzę... / Moim zdaniem... / Według mnie... / Można porównać...',
      'Zakończenie: Ogólnie można powiedzieć... / Na zakończenie chciał(a)bym...']}
};

/* Две шкалы оценки, которые встречаются в материалах комиссии. */
B1.rubrics={
  A:{
    name:'шкала из тест-образца 2020 (30 баллов)',
    crit:['wykonanie zadania 0–10 p.','środki językowe 0–10 p.','poprawność językowa 0–10 p.','razem maksymalnie 30 p.'],
    lines:[
      'Критерии (шкала теста-образца 2020, каждый 0–10, всего 30):',
      '1. wykonanie zadania: тема, жанр и форма, все пункты задания, объём, композиция;',
      '2. środki językowe: богатство и уместность лексики и конструкций, стиль;',
      '3. poprawność językowa: грамматика, орфография, пунктуация.',
      'Дополнительно, для диагностики, дай разбивку по пяти критериям методички (каждый 0–4, шаг 0,25): wykonanie zadania, poprawność gramatyczna, słownictwo, styl, ortografia i interpunkcja.']
  },
  B:{
    name:'шкала из методички (5 критериев, 40 баллов)',
    crit:['wykonanie zadania (treść, długość, forma, kompozycja) 0–4','poprawność gramatyczna 0–4','słownictwo 0–4','styl 0–4','ortografia i interpunkcja 0–4','razem 20 p. от одного экзаменатора; на экзамене два экзаменатора, сумма 40 p.'],
    lines:[
      'Критерии (шкала методички: каждый 0–4, шаг 0,25; сумма 20 от одного экзаменатора, на экзамене два экзаменатора и итог из 40):',
      '1. wykonanie zadania (treść, długość, forma, kompozycja);',
      '2. poprawność gramatyczna;',
      '3. słownictwo;',
      '4. styl;',
      '5. ortografia i interpunkcja.',
      'Дай баллы по каждому критерию и сумму из 20; для сравнения с образцами умножь сумму на 2 (получится шкала из 40).']
  },
  anchors:[
    'Ориентиры из официальных оценённых работ (сумма двух экзаменаторов, из 40):',
    '37,75: форма и композиция верны, тема раскрыта, объём в норме; ошибки редкие и не мешают, коммуникация очень хорошая.',
    '34,5: форма и композиция верны, тема раскрыта не до конца, но текст оригинален; грамматические ошибки не мешают понять замысел; лексика богатая, но выше уровня и с ошибками; мелкие ошибки пунктуации.',
    '27,75: одно задание выполнено хорошо, во втором нарушены форма и объём; много ошибок (грамматика, орфография, стиль), но замысел понятен; есть логические нарушения.',
    '22: нет нужной формы и композиции, текст короче нормы (179 слов вместо 200 за оба задания); ошибки мешают понять и исправить текст; работа не отвечает требованиям B1.'
  ]
};
})();
