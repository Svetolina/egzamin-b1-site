/* Каталог: все тесты, которые должны быть на сайте, с официальными ссылками.
   Сам тест открывается, только если рядом лежит файл tests/<id>.js и id есть в manifest.js.
   Ссылку на файл ставлю только там, где она подтверждена; иначе null, и сайт даёт ссылку на страницу комиссии. */
(function(){
'use strict';
var U='https://certyfikatpolski.pl/wp-content/uploads/';
var PAGE_EX='https://certyfikatpolski.pl/o-egzaminie/testy-egzaminacyjne-z-poprzednich-lat/';
var PAGE_SM='https://certyfikatpolski.pl/o-egzaminie/przykladowe-testy-zbiory-zadan/';
function ex(id,year,name,o){return {id:id,kind:'exam',group:String(year),name:name,note:o.note||'',page:PAGE_EX,official:{sheet:o.sheet||null,audio:o.audio||null,key:o.key||null}};}
function sm(id,name,note,o){return {id:id,kind:'sample',group:'Образцы',name:name,note:note,page:PAGE_SM,official:{sheet:o.sheet||null,audio:o.audio||null,key:o.key||null}};}
B1.catalog=[
 {id:'b1-sbornik',kind:'book',group:'Сборник',name:'Сборник заданий 2017',note:'Грамматика',page:PAGE_SM,official:{sheet:null,audio:null,key:null}},
 sm('b1-2020-03','Образец 2020','Тест-образец комиссии, март 2020',{}),
 sm('b1-2019','Образец 2019','Тест-образец комиссии, 2019',{audio:U+'2019/09/B1_audio.mp3',key:U+'2019/09/B1_klucz.pdf'}),
 sm('b1-2017','Образец 2017','Тест-образец комиссии, 2017',{audio:U+'2017/03/Egzamin-Przykładowy-B1-gru2016.mp3',key:U+'2017/03/5_B1_tr-klucz.pdf'}),

 ex('b1-2024-06',2024,'22–23 июня 2024',{sheet:U+'2025/02/22-23.06.2024-B1_arkusz_egzaminacyjny.pdf',audio:U+'2025/02/22-23.06.2024-B1_pilk_dzwiekowy.mp3',key:U+'2025/02/22-23.06.2024-B1_transkrypcja.pdf'}),
 ex('b1-2024-04',2024,'20–21 апреля 2024',{audio:U+'2025/02/20-21.04.2024-B1_plik_dzwiekowy.mp3',key:U+'2025/02/20-21.04.2024-B1_transkrypcja.pdf'}),
 ex('b1-2024-02',2024,'4–5 февраля 2024',{sheet:U+'2025/02/4-5.02.2024-B1_arkusz_egzaminacyjny.pdf',audio:U+'2025/02/4-5.02.2024-B1_plik_dzwiekowy.mp3',key:U+'2025/02/4-5.02.2024-B1_transkrypcja.pdf'}),

 ex('b1-2023-11',2023,'18–19 ноября 2023',{audio:U+'2025/07/2023_11_18_19_B1_plik_dzwiekowy.mp3',key:U+'2025/07/2023_11_18_19_B1_transkrypcja.pdf'}),
 ex('b1-2023-06',2023,'24–25 июня 2023',{audio:U+'2025/07/2023_06_24_25_B1_plik_dzwiekowy_v2.mp3',key:U+'2025/07/2023_06_24_25_B1_transkrypcja.pdf'}),
 ex('b1-2023-04',2023,'15–16 апреля 2023',{audio:U+'2025/07/2023_04_15_16_B1_plik_dzwiekowy.mp3.mp3',key:U+'2025/07/2023_04_15_16_B1_transkrypcja.pdf'}),
 ex('b1-2023-02',2023,'5–6 февраля 2023',{audio:U+'2025/07/2023_02_5_6_B1_plik_dzwiekowy.mp3',key:U+'2025/07/2023_02_5_6_B1_transkrypcja.pdf'}),

 ex('b1-2022-11',2022,'5–6 ноября 2022',{sheet:U+'2026/01/2022.11.5-6_B1_Arkusz_egzaminacyjny.pdf',audio:U+'2026/01/2022.11.5-6_B1_Plik_dzwiekowy.mp3',key:U+'2026/01/2022.11.5-6_B1_Transkrypcja_nagran.pdf'}),
 ex('b1-2022-06',2022,'25–26 июня 2022',{audio:U+'2026/09/2022.06.25-26_B1_Plik_dzwiekowy_v2.mp3',key:U+'2026/01/2022.06.25-26_B1_Transkrypcja_nagran.pdf'}),
 ex('b1-2022-03',2022,'26–27 марта 2022',{audio:U+'2026/01/2022.03.26-27_B1_Plik_dzwiekowy.mp3',key:U+'2026/01/2022.03.26-27_B1_Transkrypcja_nagran.pdf'}),
 ex('b1-2022-02',2022,'6–7 февраля 2022',{audio:U+'2026/01/2022.02.6-7_B1_Plik_dzwiekowy.mp3',key:U+'2026/01/2022.02.6-7_B1_Transkrypcja_nagran.pdf'}),

 ex('b1-2021-11',2021,'20–21 ноября 2021',{audio:U+'2026/07/2021.11.20-21_B1_Plik_dzwiekowy.mp3',key:U+'2026/07/2021.11.20-21_B1_Transkrypcja_nagran.pdf'}),
 ex('b1-2021-06',2021,'19–20 июня 2021',{audio:U+'2026/07/2021.06.19-20_B1_Plik_dzwiekowy.mp3',key:U+'2026/07/2021.06.19-20_B1_Transkrypcja_nagran.pdf'}),
 ex('b1-2021-05',2021,'8–9 мая 2021',{note:'На бланке напечатано «март 2021»',audio:U+'2026/07/2021.05.8-9_B1_Plik_dzwiekowy.mp3',key:U+'2026/07/2021.05.8-9_B1_Transkrypcja_nagran.pdf'}),
 ex('b1-2021-01',2021,'30–31 января 2021',{audio:U+'2026/07/2021.01.30-31_B1_Plik_dzwiekowy.mp3',key:U+'2026/07/2021.01.30-31_B1_Transkrypcja_nagran.pdf'})
];
})();
