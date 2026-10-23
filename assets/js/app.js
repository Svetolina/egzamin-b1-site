/* Приложение: маршруты (#/...) и страницы.
   Меню: Учить · Тексты · Практика · Словарь · Прогресс (на телефоне снизу, на компьютере в шапке). */
(function(){
'use strict';
var B1=window.B1,U=B1.util,el=U.el,fmt=U.fmt,S=B1.store,UI=B1.ui;
var app=document.getElementById('app');
var SEC=B1.sections;
var SITE='Polski';
var ASSET_VER='20261023b'; /* бампать при каждом обновлении файлов — иначе браузер/CDN может отдавать старый кеш tests/<id>.js */
var AUTO=['sluch','czyt','gram'];
var flt={src:'all',type:'all',todo:false};
var pageLabel='';

/* ---------- данные ---------- */
function secById(id){return SEC.filter(function(s){return s.id===id;})[0];}
function dataById(id){return B1.tests.filter(function(t){return t.id===id;})[0];}
function entryById(id){return (B1.catalog||[]).filter(function(c){return c.id===id;})[0];}
function findMod(test,sid){return (test.modules||[]).filter(function(m){return m.id===sid;})[0];}
function hasSection(test,sid){
  if(sid==='mow')return !!test.speaking;
  if(sid==='pis')return !!(test.writing&&test.writing.length);
  var m=findMod(test,sid);return !!(m&&m.tasks&&m.tasks.length);
}
function plural(n,a,b,c){var m=n%100,d=n%10;if(m>10&&m<15)return c;if(d===1)return a;if(d>1&&d<5)return b;return c;}
function link(href,cls,text){var a=el('a',cls,text);a.href=href;return a;}
function romanOf(t){return (t.rn||t.id).replace(/\.$/,'');}
function srcText(c){return c.kind==='sample'||c.kind==='book'||c.kind==='other'?c.name:'Прошлый экзамен, '+c.name;}
var KIND_LABEL={sample:'Образец',book:'Сборник',other:'Другой источник',exam:'Экзамен'};
var KIND_CLS={sample:'b-sample',book:'b-book',other:'b-other',exam:'b-exam'};
function badge(c){return el('span','badge '+(KIND_CLS[c.kind]||'b-exam'),KIND_LABEL[c.kind]||'Экзамен');}
function typeLabel(d){
  if(d.kind==='choice'){
    var it0=d.items&&d.items[0];
    if(it0&&it0.inline){
      var vs=(it0.opts||[]).map(function(o){return o.v;}).join('/');
      if(vs==='p/f/bi')return 'P / F / BI';
      if(vs==='p/f')return 'P / F';
      return 'TAK / NIE';
    }
    return 'Выбор ответа';
  }
  if(d.kind==='gaps'){if(d.legend)return 'Фрагменты в тексте';if(d.box)return 'Слова из рамки';return (d.gaps&&d.gaps[0]&&d.gaps[0].opts)?'Выбор формы':'Пропуски';}
  return {match:'Сопоставление',order:'Порядок фрагментов',slots:'Сопоставление',qa:'Вопросы',rewrite:'Перефразирование'}[d.kind]||'Задание';
}
/* как отвечают на задание: тап по вариантам или ввод с клавиатуры */
function modeOf(d){
  if(d.kind==='qa'||d.kind==='rewrite')return 'kb';
  if(d.kind==='gaps')return (d.gaps&&d.gaps[0]&&d.gaps[0].opts)?'tap':'kb';
  return 'tap';
}
var MODE={tap:'тап',kb:'клавиатура',voice:'голос'};
function modeTag(mode){return el('span','mode m-'+mode,MODE[mode]);}
function secMode(sid,m){
  if(sid==='pis')return 'kb';if(sid==='mow')return 'voice';
  if(m&&m.tasks&&m.tasks.some(function(d){return modeOf(d)==='kb';})&&sid==='gram')return 'kb';
  return 'tap';
}
function countText(d){
  var n=(d.items&&d.items.length)||(d.gaps&&d.gaps.length)||(d.rows&&d.rows.length)||0;
  return n?n+' '+plural(n,'пункт','пункта','пунктов'):'';
}
function taskName(d){return d.name||typeLabel(d);}
function taskUrl(tid,sid,k){return '#/task/'+tid+'/'+sid+'/'+k.id;}
function officialFile(c,which){var u=c.official&&c.official[which];return u?{url:u,exact:true}:{url:c.page||null,exact:false};}
function sheetPageUrl(c,page){
  var f=officialFile(c,'sheet');
  return (f.exact&&page)?f.url+'#page='+page:f.url;
}
function officialLinks(c){
  var s=officialFile(c,'sheet'),a=officialFile(c,'audio'),k=officialFile(c,'key');
  function lab(t,f){return f.exact?t:t+': на странице источника';}
  var out=[];
  if(s.url)out.push({t:lab('Лист заданий (PDF)',s),u:s.url});
  if(a.url)out.push({t:lab('Запись (mp3)',a),u:a.url});
  if(k.url)out.push({t:lab('Транскрипция и ключ (PDF)',k),u:k.url});
  if(c.page)out.push({t:'Страница источника',u:c.page});
  return out;
}
function autoStat(t){
  var res=B1.results(t.id),e=0,n=0,total=0,max=0;
  AUTO.forEach(function(sid){var m=findMod(t,sid);if(!m)return;max+=m.max;m.tasks.forEach(function(k){total++;if(res[k.id]!=null){e+=res[k.id];n++;}});});
  return {e:e,n:n,total:total,max:max};
}
function resultText(t){var s=autoStat(t);return s.n?fmt(s.e)+' / '+fmt(s.max):'—';}
function isDone(t){var s=autoStat(t);return s.total>0&&s.n===s.total;}
function modProgress(t,sid){
  var m=findMod(t,sid);if(!m||!m.tasks||!m.tasks.length)return null;
  var res=B1.results(t.id),e=0,n=0;
  m.tasks.forEach(function(k){if(res[k.id]!=null){e+=res[k.id];n++;}});
  return {e:e,n:n,total:m.tasks.length,max:m.max};
}
/* состояние раздела для кружков: done / started / none / off */
function secState(t,sid){
  if(!hasSection(t,sid))return 'off';
  if(sid==='pis'||sid==='mow'){
    var a=B1.answers(t.id),pre=sid==='pis'?'w-':'m-';
    return Object.keys(a).some(function(k){return k.indexOf(pre)===0&&k!=='w-set'&&k!=='m-set'&&String(a[k]).trim();})?'started':'none';
  }
  var p=modProgress(t,sid);
  if(!p||!p.n)return 'none';
  return p.n===p.total?'done':'started';
}
var SEC_LETTER={sluch:'С',czyt:'Ч',gram:'Г',pis:'П',mow:'М'};
var SEC_STATE_RU={done:'пройден',started:'начат',none:'не начат',off:'нет в тесте'};
function dots(t){
  var w=el('span','dots');
  SEC.forEach(function(s){
    var st=t?secState(t,s.id):'off';
    var d=el('span','dot d-'+st,SEC_LETTER[s.id]);d.title=s.ru+': '+SEC_STATE_RU[st];
    w.append(d);
  });
  w.setAttribute('aria-label',SEC.map(function(s){return s.ru+' '+SEC_STATE_RU[t?secState(t,s.id):'off'];}).join(', '));
  return w;
}
/* все задания одного типа изо всех тестов, что есть в тренажёре */
function typeRows(sid){
  var rows=[];
  (B1.catalog||[]).forEach(function(c){
    var t=dataById(c.id);if(!t)return;
    if(sid==='pis'){(t.writing||[]).forEach(function(w){rows.push({c:c,t:t,sid:sid,w:w,set:true});});return;}
    if(sid==='mow'){(t.speaking||[]).forEach(function(sp){rows.push({c:c,t:t,sid:sid,sp:sp,set:true});});return;}
    var m=findMod(t,sid);if(!m||!m.tasks)return;
    var res=B1.results(t.id);
    m.tasks.forEach(function(k){rows.push({c:c,t:t,sid:sid,k:k,res:res[k.id]});});
  });
  return rows;
}
function typeStat(sid,kind){
  var rows=typeRows(sid).filter(function(r){return !kind||r.c.kind===kind;});
  var done=rows.filter(function(r){return r.res!=null;}).length;
  return {total:rows.length,done:done};
}
function mistakes(){
  var out=[];
  (B1.catalog||[]).forEach(function(c){
    var t=dataById(c.id);if(!t)return;var res=B1.results(t.id);
    AUTO.forEach(function(sid){var m=findMod(t,sid);if(!m)return;
      m.tasks.forEach(function(k){if(res[k.id]!=null&&res[k.id]<k.max-1e-9)out.push({c:c,t:t,sid:sid,k:k,res:res[k.id]});});
    });
  });
  return out;
}

/* ---------- шапка и меню ---------- */
var NAV=[
  {k:'learn',h:'#/',t:'Учить',i:'<path d="M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z"/><path d="M5 17a3 3 0 0 1 3-3h11"/>'},
  {k:'texts',h:'#/texts',t:'Тексты',i:'<path d="M5 6h14M5 11h14M5 16h9"/>'},
  {k:'practice',h:'#/practice',t:'Практика',i:'<circle cx="12" cy="12" r="9"/><path d="M8 12.5l3 3 5-6"/>'},
  {k:'dict',h:'#/dict',t:'Словарь',i:'<rect x="4" y="8" width="16" height="12" rx="2"/><path d="M7 4h10"/>'},
  {k:'progress',h:'#/progress',t:'Прогресс',i:'<path d="M6 20v-8M12 20V5M18 20v-5"/>'}
];
var navTop,navBot,lvlChip;
function buildChrome(){
  var hdr=document.querySelector('header.site');hdr.replaceChildren();
  var brand=link('#/','brand');brand.append(el('span','brand-t pl','Polski'),el('span','brand-s','Подготовка к экзамену'));
  navTop=el('nav','nav-t');navTop.setAttribute('aria-label','Разделы');
  var tools=el('div','hdr-tools');
  var sr=link('#/search','icbtn');sr.setAttribute('aria-label','Поиск');sr.append(UI.icon('search',22));
  lvlChip=link('#/settings','lvl','B1 · RU');lvlChip.setAttribute('aria-label','Уровень и язык: B1, русский');
  tools.append(sr,lvlChip);
  hdr.append(brand,navTop,tools);
  navBot=el('nav','nav-b');navBot.setAttribute('aria-label','Разделы');
  NAV.forEach(function(n){
    [navTop,navBot].forEach(function(host){
      var a=link(n.h);a.dataset.key=n.k;
      a.insertAdjacentHTML('beforeend','<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'+n.i+'</svg>');
      a.append(el('span',null,n.t));host.append(a);
    });
  });
  document.body.append(navBot);
}
function setActive(key){
  [navTop,navBot].forEach(function(host){
    Array.prototype.forEach.call(host.children,function(a){
      if(a.dataset.key===key)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');
    });
  });
}
function wide(on){app.classList.toggle('wide',!!on);}
function title(t){pageLabel=t;document.title=t+' | '+SITE;}
/* заголовок внутренней страницы: «назад», название, подзаголовок */
function tophead(back,h,sub,extra){
  var w=el('div','tophead');
  if(back){var a=link(back,'icbtn back');a.setAttribute('aria-label','Назад');a.append(UI.icon('back',22));w.append(a);}
  var t=el('div','tophead-t');t.append(el('h1',null,h));if(sub)t.append(el('p','sub',sub));
  w.append(t);if(extra)w.append(extra);
  app.append(w);return w;
}
function crumbs(items){
  var c=el('nav','crumbs');c.setAttribute('aria-label','Путь');
  items.forEach(function(it,i){
    if(i)c.append(el('span','sep','/'));
    if(it.href)c.append(link(it.href,null,it.t));else c.append(el('span','here',it.t));
  });
  return c;
}
function section(h,sub){var s=el('section','block');if(h)s.append(el('h2',null,h));if(sub)s.append(el('p','meta',sub));app.append(s);return s;}
/* строка-ссылка как в макетах: название, подпись, справа значок или число */
function rowLink(href,t,sub,right,cls){
  var a=href?link(href,'lrow'+(cls?' '+cls:'')):el('div','lrow off'+(cls?' '+cls:''));
  var l=el('span','lrow-l');l.append(el('span','lrow-t',t));
  if(sub){if(typeof sub==='string')l.append(el('span','lrow-s',sub));else l.append(sub);}
  a.append(l);
  if(right!=null){if(typeof right==='string'||typeof right==='number')a.append(el('span','lrow-r',String(right)));else a.append(right);}
  return a;
}
function bar(pct){var b=el('span','bar');var f=el('span');f.style.width=Math.max(0,Math.min(100,pct))+'%';b.append(f);return b;}
function filesMenu(c){
  var d=el('details','menu');
  var s=el('summary');s.setAttribute('aria-label','Файлы теста: лист, запись, ключ');
  s.innerHTML='<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><circle cx="5" cy="12" r="1.8"/><circle cx="12" cy="12" r="1.8"/><circle cx="19" cy="12" r="1.8"/></svg>';
  d.append(s);
  var p=el('div','menu-p');
  officialLinks(c).forEach(function(l){var a=link(l.u,null,l.t);a.target='_blank';a.rel='noopener';p.append(a);});
  d.append(p);return d;
}
document.addEventListener('click',function(e){
  Array.prototype.forEach.call(document.querySelectorAll('details.menu[open]'),function(d){if(!d.contains(e.target))d.open=false;});
});
function soon(){return el('span','soon','скоро');}

/* ---------- «продолжить» и недавние страницы ---------- */
function remember(href,t,s){S.prefs.set('last',{href:href,t:t,s:s});}
function rememberVisit(){
  var h=location.hash||'#/';
  if(/^#\/(search|settings|welcome)/.test(h)||h==='#/'||!pageLabel)return;
  var r=S.prefs.get('recent',[]).filter(function(x){return x.href!==h;});
  r.unshift({href:h,t:pageLabel,at:new Date().toISOString()});
  S.prefs.set('recent',r.slice(0,6));
}
function continueCard(host){
  var last=S.prefs.get('last',null);if(!last)return false;
  var a=link(last.href,'cont');
  a.append(el('span','cont-k','Продолжить'),el('span','cont-t',last.t),el('span','cont-s',last.s||''));
  host.append(a);return true;
}
function dueCard(host){
  var n=S.words.dueCount(),all=S.words.all().length;
  if(!all)return;
  var d=el('div','due');
  d.append(el('span',null,n?'К повторению: '+n+' '+plural(n,'карточка','карточки','карточек'):'Все карточки на сегодня повторены'));
  d.append(link('#/dict','btn2 small'+(n?' primary':''),n?'Начать':'Словарь'));
  host.append(d);
}

/* ---------- Учить (главная) ---------- */
var LEARN=[
  {k:'grammar',t:'Грамматика',s:'Правила и упражнения',
   about:'Правила с таблицами и упражнениями, каждое правило подтверждено двумя учебниками. Сейчас готовятся темы czas przyszły и czas teraźniejszy.',
   go:{h:'#/type/gram',t:'Пока можно решать задания по грамматике из экзаменов и сборника'}},
  {k:'vocab',t:'Лексика',s:'Слова по темам',about:'Слова по темам экзамена: семья, работа, здоровье, город. Любое слово можно будет добавить в свой словарь одним нажатием.',
   go:{h:'#/dict',t:'Пока можно собирать свой словарь: выделите слово в любом тексте сайта'}},
  {k:'phrases',t:'Фразы',s:'Для разных ситуаций',about:'Готовые обороты для письма и говорения: просьба, жалоба, приглашение, благодарность.',
   go:{h:'#/type/pis',t:'Обороты для письма уже есть в справочнике жанров'}},
  {k:'texts',t:'Тексты',s:'Образцы ответов',about:'Короткие образцы на темы устной и письменной части: семья, работа, город, хобби. В образец можно будет подставить свои данные.',
   go:{h:'#/type/mow',t:'Пока можно потренировать говорение по сборнику'}}
];
function home(){
  if(!S.prefs.get('onboarded',false))return welcome(1);
  title('Учить');setActive('learn');wide(false);
  var top=el('div','learn-top');app.append(top);
  var had=continueCard(top);
  dueCard(top);
  if(!had){
    var st=section('С чего начать');
    var ol=el('div','steps');
    [['#/exams','Пробный тест','Один тест из прошлых лет, чтобы увидеть свой уровень'],
     ['#/type/gram','Задания по грамматике','Все грамматические задания экзаменов и сборника'],
     ['#/dict','Первое слово','Выделите слово в тексте или впишите своё']].forEach(function(x,i){
      var a=rowLink(x[0],x[1],x[2]);a.prepend(el('span','num',String(i+1)));ol.append(a);
    });
    st.append(ol);
  }
  var s=section('Учить');
  var g=el('div','grid2');
  LEARN.forEach(function(l){var a=link('#/learn/'+l.k,'ltile');a.append(el('span','ltile-t',l.t),el('span','ltile-s',l.s),soon());g.append(a);});
  s.append(g);
  var p=section();
  var pa=link('#/practice','ptile');
  pa.append(el('span','ptile-t','Практика'),el('span','ptile-s','Экзамены прошлых лет · '+(B1.catalog||[]).filter(function(c){return c.kind==='exam'||c.kind==='sample';}).length+' тестов, сборник 2017'));
  p.append(pa);
}
function learnPage(k){
  var l=LEARN.filter(function(x){return x.k===k;})[0];if(!l)return home();
  title(l.t);setActive(k==='texts'?'texts':'learn');wide(false);
  tophead('#/',l.t,l.s);
  var c=el('div','card');
  c.append(el('p','badge-line',null));c.lastChild.append(soon(),document.createTextNode(' Раздел готовится'));
  c.append(el('p',null,l.about));
  c.append(link(l.go.h,'btn2',l.go.t));
  app.append(c);
}
function textsPage(){
  title('Тексты');setActive('texts');wide(false);
  tophead(null,'Тексты','Образцы ответов для устной и письменной части');
  var c=el('div','card');
  c.append(el('p','badge-line',null));c.lastChild.append(soon(),document.createTextNode(' Раздел готовится'));
  c.append(el('p',null,'Здесь будет библиотека коротких образцов по темам: семья, работа, город, хобби. Для каждого: вопрос экзаменатора и запись ответа, а для письма — свой вариант текста с подставленными данными.'));
  c.append(link('#/type/mow','btn2','Пока: говорение по сборнику'),link('#/type/pis','btn2','Письмо: задания и жанры'));
  app.append(c);
}

/* ---------- Практика ---------- */
var PTS={sluch:30,czyt:30,gram:30,pis:30,mow:40};
function practicePage(){
  title('Практика');setActive('practice');wide(false);
  tophead(null,'Практика','Реальные задания экзамена B1');
  var top=el('div','learn-top');app.append(top);
  continueCard(top);
  var mk=mistakes();
  var me=el('div','due');
  me.append(el('span',null,mk.length?'Мои ошибки: '+mk.length+' '+plural(mk.length,'задание','задания','заданий')+' не на полный балл':'Мои ошибки: пока пусто'));
  me.append(link('#/mistakes','btn2 small','Разобрать'));
  top.append(me);
  var cat=B1.catalog||[];
  var s1=section('Тесты целиком');
  var nS=cat.filter(function(c){return c.kind==='sample';}).length,nE=cat.filter(function(c){return c.kind==='exam';}).length;
  s1.append(rowLink('#/samples','Образцы комиссии','2017 · 2019 · 2020',el('span','cnt',String(nS))),
    rowLink('#/exams','Прошлые экзамены','2021–2024',el('span','cnt',String(nE))));
  var s2=section('По разделам экзамена','Задания одного типа изо всех тестов сразу, с фильтрами: источник, тип, нерешённые');
  SEC.forEach(function(s){
    var r=el('span','lrow-x');r.append(el('span','pts',PTS[s.id]+' б'),modeTag(secMode(s.id,s.id==='gram'?{tasks:typeRows('gram').map(function(x){return x.k;})}:null)));
    var sub=el('span','lrow-s pl',s.pl);
    s2.append(rowLink('#/type/'+s.id,s.ru,sub,r));
  });
  var book=cat.filter(function(c){return c.kind==='book';})[0];
  var bt=book&&dataById(book.id);
  if(bt){
    var s3=section('Сборник 2017','Zbiór zadań: не целые тесты, а задания по разделам');
    [['gram','упражнения'],['czyt','упражнений'],['sluch','упражнений, с записями'],['pis',''],['mow','']].forEach(function(x){
      var sid=x[0];if(!hasSection(bt,sid))return;
      var s=secById(sid),sub;
      if(sid==='pis'||sid==='mow'){var n=(sid==='pis'?bt.writing:bt.speaking).length;sub=n+' '+plural(n,'набор','набора','наборов')+', '+(sid==='pis'?n*2:n*3)+' заданий';}
      else{var st=typeStat(sid,'book');sub=st.total+' '+plural(st.total,'упражнение','упражнения','упражнений')+(sid==='sluch'?', с записями':'')+' · решено '+st.done;}
      s3.append(rowLink('#/type/'+sid+'/book',s.ru,sub,modeTag(sid==='pis'?'kb':sid==='mow'?'voice':sid==='gram'?'kb':'tap')));
    });
  }
  var others=cat.filter(function(c){return c.kind==='other';});
  var s4=section('Другие источники');
  if(others.length)s4.append(rowLink('#/others','Тесты из других пособий',others.length+' '+plural(others.length,'тест','теста','тестов')));
  else s4.append(el('p','meta','Пока пусто. Сюда попадут тесты не от комиссии: другие сборники, telc и т. д.'));
}
function mistakesPage(){
  title('Мои ошибки');setActive('practice');wide(false);
  tophead('#/practice','Мои ошибки','Задания, проверенные не на полный балл');
  var mk=mistakes();
  if(!mk.length){
    var e=el('div','empty');e.append(el('h2',null,'Ошибок нет'),el('p',null,'Здесь собираются задания, где после проверки балл ниже максимума. Решите и проверьте любое задание в «Практике».'),link('#/practice','btn2 primary','К практике'));
    app.append(e);return;
  }
  var by={};
  mk.forEach(function(r){var k=r.c.id;(by[k]=by[k]||[]).push(r);});
  Object.keys(by).forEach(function(k){
    var c=entryById(k);var s=section(c.name);
    by[k].forEach(function(r){
      var sec=secById(r.sid);
      s.append(rowLink(taskUrl(r.t.id,r.sid,r.k),(r.c.kind==='book'?'':romanOf(r.k)+'. ')+taskName(r.k),sec.ru+' · '+typeLabel(r.k),el('span','res',fmt(r.res)+' / '+fmt(r.k.max))));
    });
  });
}

/* ---------- тесты целиком ---------- */
var LISTS={
  sample:{ttl:'Образцы',href:'#/samples'},
  exam:{ttl:'Прошлые экзамены',href:'#/exams'},
  other:{ttl:'Другие источники',href:'#/others'}
};
function testsPage(kind){
  title(kind&&LISTS[kind]?LISTS[kind].ttl:'Тесты целиком');setActive('practice');wide(false);
  tophead('#/practice','Тесты целиком','Образцы и прошлые экзамены');
  var cat=B1.catalog||[];
  var fl=el('div','chiprow wrap');
  var opts=[[null,'Все','#/tests'],['sample','Образцы','#/samples'],['exam','Экзамены','#/exams']];
  if(cat.some(function(c){return c.kind==='other';}))opts.push(['other','Другие','#/others']);
  opts.forEach(function(o){
    var n=cat.filter(function(c){return c.kind!=='book'&&(!o[0]||c.kind===o[0]);}).length;
    var a=link(o[2],'chip2'+((kind||null)===o[0]?' on':''),o[1]+' · '+n);
    if((kind||null)===o[0])a.setAttribute('aria-current','page');
    fl.append(a);
  });
  app.append(fl);
  var list=cat.filter(function(c){return c.kind!=='book'&&(!kind||c.kind===kind);});
  if(!list.length){app.append(el('p','meta','Пока пусто. Сюда попадут тесты не от комиссии.'));return;}
  var host=el('div','tlist');var gk=null;
  list.forEach(function(c){
    var g=c.kind==='exam'?'Прошлые экзамены · '+c.group:(c.kind==='sample'?'Образцы комиссии':c.group||'Другие источники');
    if(g!==gk){host.append(el('h2','grp',g));gk=g;}
    var t=dataById(c.id);
    var row=el('div','trow4');
    var a=t?link('#/test/'+c.id,'trow4-a'):el('div','trow4-a off');
    var nm=el('span','trow4-n',c.name);
    var sub=el('span','trow4-s');sub.append(badge(c),dots(t));
    a.append(nm,sub);
    if(c.note)a.append(el('span','meta',c.note));
    if(!t)a.append(el('span','meta','В тренажёр добавим позже'));
    row.append(a,el('span','res',t?resultText(t):'—'),filesMenu(c));
    host.append(row);
  });
  app.append(host);
  var lg=el('p','meta legend2');
  lg.textContent='С слух · Ч чтение · Г грамматика · П письмо · М говорение. Сплошной кружок: раздел пройден, жирная рамка: начат, пунктир: не начат.';
  app.append(lg);
}

/* ---------- карточка теста ---------- */
function testPage(tid){
  var c=entryById(tid),t=dataById(tid);
  if(!c)return home();
  title(c.name);setActive('practice');wide(false);
  var back=c.kind==='book'?'#/practice':(LISTS[c.kind]?LISTS[c.kind].href:'#/tests');
  var sub=(c.kind==='sample'?'Образец комиссии':c.kind==='book'?'Сборник заданий':c.kind==='other'?(c.source||'Другой источник'):'Прошлый экзамен')+' · B1'+(c.note?'. '+c.note:'');
  tophead(back,c.name,sub);
  if(!t){
    var n=el('div','card');n.append(el('p',null,'Этот тест ещё не добавлен в тренажёр. Официальные файлы можно открыть ниже.'));app.append(n);
  }else{
    var st=autoStat(t);
    var rs=el('div','card result');
    var big=el('p','big-r');big.append(el('span',null,'Razem '),el('span','fill',st.n?fmt(st.e):' '),el('span','of',' / '+fmt(st.max)+' p.'));
    rs.append(big,el('p','meta','Три автоматически проверяемые части'+(st.n?', проверено заданий: '+st.n+' из '+st.total:'')+'. Письмо и говорение разбираются в чате.'));
    app.append(rs);
    var list=el('div','seclist');
    SEC.forEach(function(s){
      var box=el('section','seccard'+(hasSection(t,s.id)?'':' off'));
      var m=findMod(t,s.id);
      if(!hasSection(t,s.id)){
        box.append(el('div','sec-t',s.ru),el('div','sec-pl pl',s.pl),el('p','meta',s.id==='mow'?'В листе заданий нет':'Нет в этом тесте'));
        list.append(box);return;
      }
      var a=link('#/test/'+t.id+'/'+s.id,'sec-head');
      var l=el('span','sec-l');l.append(el('span','sec-t',s.ru),el('span','sec-pl pl',s.pl));
      var mt=[];
      if(m&&m.tasks)mt.push(m.tasks.length+' '+plural(m.tasks.length,'задание','задания','заданий'));
      if(m&&m.minutes)mt.push(m.minutes+' мин');
      if(m)mt.push(fmt(m.max)+' б');
      if(!m&&s.id==='mow')mt.push('3 набора');
      l.append(el('span','meta',mt.join(' · ')));
      var r=el('span','sec-r');
      var p=modProgress(t,s.id);
      r.append(el('span','res',s.id==='pis'||s.id==='mow'?'':(p&&p.n?fmt(p.e)+' / '+fmt(p.max):'')),modeTag(secMode(s.id,m)));
      a.append(l,r);box.append(a);
      if(m&&m.tasks&&m.tasks.length){
        var d=el('details','sec-tasks');d.append(el('summary',null,'Задания'));
        var res=B1.results(t.id);
        m.tasks.forEach(function(k){
          var ra=link(taskUrl(t.id,s.id,k),'trk');
          ra.append(el('span','trk-n',c.kind==='book'?'':romanOf(k)),el('span','trk-t',taskName(k)));
          var rr=el('span','trk-r');rr.append(el('span','res',res[k.id]!=null?fmt(res[k.id])+'/'+fmt(k.max):''),modeTag(modeOf(k)));
          ra.append(rr);d.append(ra);
        });
        if(s.id==='gram')d.open=true;
        box.append(d);
      }
      list.append(box);
    });
    app.append(list);
    var first=SEC.filter(function(s){return hasSection(t,s.id);})[0];
    if(first&&c.kind!=='book')app.append(link('#/test/'+t.id+'/'+first.id,'btn2 primary wide-b','Начать с раздела «'+first.ru+'»'));
    if(c.kind!=='book'){
      var thr=el('section','card');
      thr.append(el('h2','h-s','Порог сдачи'),el('p','meta','Нужно набрать не меньше 50% в каждой части отдельно. Средний балл не считается.'));
      var g=el('div','thr');
      [['Аудирование','15 из 30'],['Чтение','15 из 30'],['Грамматика','15 из 30'],['Письмо','15 из 30'],['Говорение','20 из 40']].forEach(function(x){
        var b=el('div');b.append(el('span','k',x[0]),el('span','v',x[1]));g.append(b);
      });
      thr.append(g);app.append(thr);
    }
  }
  var src=el('section','card');
  src.append(el('h2','h-s','Официальные файлы'),el('p','meta',c.source||'Państwowa Komisja ds. Poświadczania Znajomości Języka Polskiego jako Obcego'));
  var ls=el('div','flist');
  officialLinks(c).forEach(function(l){var a=link(l.u,'flink');a.target='_blank';a.rel='noopener';a.append(el('span',null,l.t));ls.append(a);});
  src.append(ls);app.append(src);
}

/* ---------- тип заданий ---------- */
function genresBlock(){
  var b=el('section','block');
  b.append(el('h2',null,'Справочник жанров'),el('p','meta','Что должно быть в тексте по методичке комиссии. Нажмите на жанр.'));
  Object.keys(B1.genres||{}).forEach(function(k){
    var g=B1.genres[k];var d=el('details','genre');d.append(el('summary',null,g.pl));
    var ul=el('ul');g.req.forEach(function(x){ul.append(el('li',null,x));});d.append(ul);
    if(g.phrases){var pp=el('div','phr');g.phrases.forEach(function(x){pp.append(el('p',null,x));});d.append(pp);}
    b.append(d);
  });
  return b;
}
function chipRow(label,opts,cur,onPick){
  var row=el('div','frow');row.append(el('span','fl',label));
  opts.forEach(function(o){
    var b=el('button','fchip'+(o.v===cur?' on':''),o.t);b.type='button';b.setAttribute('aria-pressed',String(o.v===cur));
    b.addEventListener('click',function(){onPick(o.v);});row.append(b);
  });
  return row;
}
function typePage(sid,preset){
  var s=secById(sid);if(!s)return practicePage();
  var key=sid+'|'+(preset||'');
  if(flt.key!==key)flt={src:preset||'all',type:'all',todo:false,key:key};
  title(s.ru+(preset==='book'?' · сборник':''));setActive('practice');wide(true);
  tophead('#/practice',s.ru,s.pl);
  var all=typeRows(sid);
  if(!all.length){app.append(el('p','meta','Заданий этого типа в тренажёре пока нет.'));return;}
  app.append(el('p','lead',sid==='pis'?'Наборы заданий из тестов. Выберите один набор и выполните оба задания, как на экзамене.':sid==='mow'?'Наборы заданий из сборника. Выберите один набор и по очереди ответьте на все три задания — запись голоса делается прямо в браузере.':'Задания из тестов, что уже добавлены в тренажёр. У каждого подписан источник и есть ссылка на лист комиссии.'));
  var box=el('div','filters');var listHost=el('div','rows');
  function render(){
    box.replaceChildren();listHost.replaceChildren();
    var srcOpts=[{v:'all',t:'Все'}];
    if(all.some(function(r){return r.c.kind==='sample';}))srcOpts.push({v:'sample',t:'Образцы'});
    if(all.some(function(r){return r.c.kind==='exam';}))srcOpts.push({v:'exam',t:'Прошлые экзамены'});
    if(all.some(function(r){return r.c.kind==='book';}))srcOpts.push({v:'book',t:'Сборник'});
    if(all.some(function(r){return r.c.kind==='other';}))srcOpts.push({v:'other',t:'Другие источники'});
    box.append(chipRow('Источник',srcOpts,flt.src,function(v){flt.src=v;render();}));
    if(sid!=='pis'&&sid!=='mow'){
      var types=[];all.forEach(function(r){var l=typeLabel(r.k);if(types.indexOf(l)<0)types.push(l);});
      box.append(chipRow('Тип задания',[{v:'all',t:'Все'}].concat(types.map(function(x){return {v:x,t:x};})),flt.type,function(v){flt.type=v;render();}));
      box.append(chipRow('Показывать',[{v:false,t:'Все'},{v:true,t:'Нерешённые'}],flt.todo,function(v){flt.todo=v;render();}));
    }
    var rows=all.filter(function(r){
      if(flt.src!=='all'&&r.c.kind!==flt.src)return false;
      if(sid!=='pis'&&sid!=='mow'){if(flt.type!=='all'&&typeLabel(r.k)!==flt.type)return false;if(flt.todo&&r.res!=null)return false;}
      return true;
    });
    if(!rows.length){listHost.append(el('p','meta','По этим фильтрам ничего нет.'));return;}
    var head=el('div','trow3 th');['Задание','Тип','Баллы','Источник','Результат'].forEach(function(x,i){head.append(el('span',i===4?'r':null,x));});
    listHost.append(head);
    rows.forEach(function(r){
      var row=el('div','trow3');
      var n=el('div','c-n');
      var pg;
      if(r.set){
        if(sid==='pis'){
          var pmod=findMod(r.t,'pis')||{};
          n.append(link('#/test/'+r.t.id+'/pis','trow2-a','Zestaw '+r.w.id+': '+r.w.a.genre+' + '+r.w.b.genre),el('span','meta','Два задания: a ('+r.w.a.words+' слов) и b ('+r.w.b.words+' слов)'));
          row.append(n,el('span',null,'Письмо'),el('span','pts',fmt(pmod.max)));
          pg=pmod.page;
        }else{
          var mmod=findMod(r.t,'mow')||{};
          n.append(link('#/test/'+r.t.id+'/mow','trow2-a','Zestaw '+r.sp.id+': opis, monolog, sytuacja'),el('span','meta','Три задания устной части'));
          row.append(n,el('span',null,'Говорение'),el('span','pts',fmt(mmod.max)));
          pg=mmod.page;
        }
      }else{
        n.append(link(taskUrl(r.t.id,sid,r.k),'trow2-a',r.c.kind==='book'?taskName(r.k):romanOf(r.k)+'. '+taskName(r.k)),el('span','meta',countText(r.k)));
        var tl=el('span','c-t');tl.append(document.createTextNode(typeLabel(r.k)+' '),modeTag(modeOf(r.k)));
        row.append(n,tl,el('span','pts',fmt(r.k.max)));
        pg=r.k.page;
      }
      var so=el('div','c-s');so.append(badge(r.c),el('span',null,srcText(r.c)));
      var a=link(sheetPageUrl(r.c,pg),'pdf',pg?'PDF, стр. '+pg:'PDF');a.target='_blank';a.rel='noopener';so.append(a);
      row.append(so,el('span','r res',r.set?'—':(r.res!=null?fmt(r.res)+' / '+fmt(r.k.max):'—')));
      listHost.append(row);
    });
  }
  render();app.append(box,listHost);
  if(sid==='pis')app.append(genresBlock());
}

/* ---------- отдельное задание ---------- */
function taskPage(tid,sid,taskId){
  var c=entryById(tid),t=dataById(tid),s=secById(sid);
  if(!c||!t||!s)return home();
  var m=findMod(t,sid),d=m&&m.tasks.filter(function(k){return k.id===taskId;})[0];
  if(!d)return typePage(sid);
  title(c.name+' › '+s.ru+' · зад. '+romanOf(d));setActive('practice');wide(false);
  remember(location.hash,c.name,s.ru+', задание '+romanOf(d)+(d.name?' · '+d.name:''));
  tophead('#/test/'+tid,s.ru+' · '+(c.kind==='book'?taskName(d):'задание '+romanOf(d)),srcText(c));
  var box=el('section','srcbar');
  var l=el('div');
  var top=el('div','srcbar-t');top.append(badge(c),el('strong',null,taskName(d)));
  l.append(top,el('span','meta',c.kind==='book'?'Максимум '+fmt(d.max)+' баллов.':'Максимум '+fmt(d.max)+' из '+fmt(m.max)+' баллов.'));
  var a=link(sheetPageUrl(c,d.page),'flink',null);a.target='_blank';a.rel='noopener';a.append(el('span',null,officialFile(c,'sheet').exact?(d.page?'Лист комиссии, стр. '+d.page:'Лист комиссии'):'Страница комиссии'));
  box.append(l,a);app.append(box);
  var engine=B1.engine(t);B1.current=engine;
  app.append(engine.renderTask(m,taskId));
  var i=m.tasks.indexOf(d);var pn=el('nav','pn');pn.setAttribute('aria-label','Соседние задания');
  if(i>0)pn.append(link(taskUrl(tid,sid,m.tasks[i-1]),'btn','← '+romanOf(m.tasks[i-1])));else pn.append(el('span'));
  if(i<m.tasks.length-1)pn.append(link(taskUrl(tid,sid,m.tasks[i+1]),'btn',romanOf(m.tasks[i+1])+' →'));
  app.append(pn);
  if(c.kind!=='book'){var more=el('p','meta');more.append(link('#/test/'+tid+'/'+sid,null,'Открыть весь раздел «'+s.ru+'» этого теста с таймером'));app.append(more);}
}

/* ---------- раздел теста целиком (с таймером) ---------- */
function modulePage(tid,sid,taskId){
  var c=entryById(tid),t=dataById(tid);
  if(!c||!t)return testPage(tid);
  var s=secById(sid);if(!s||!hasSection(t,sid))return testPage(tid);
  title(c.name+' › '+s.ru);setActive('practice');wide(false);
  remember(location.hash.split('/').slice(0,4).join('/'),c.name,s.ru+', весь раздел');
  tophead('#/test/'+tid,s.ru,srcText(c));
  var m=findMod(t,sid);
  var engine=B1.engine(t);B1.current=engine;
  app.append(engine.renderModule(m));
  var box=el('section','srcbar');var l=el('div');
  var top=el('div','srcbar-t');top.append(badge(c),el('strong',null,srcText(c)));l.append(top);
  var a=link(sheetPageUrl(c,m.page),'flink',null);a.target='_blank';a.rel='noopener';a.append(el('span',null,m.page?'Лист комиссии, стр. '+m.page:'Лист комиссии'));
  box.append(l,a);app.append(box);
  var avail=SEC.filter(function(x){return hasSection(t,x.id);});
  var i=avail.map(function(x){return x.id;}).indexOf(sid);
  var pn=el('nav','pn');pn.setAttribute('aria-label','Соседние разделы');
  if(i>0)pn.append(link('#/test/'+tid+'/'+avail[i-1].id,'btn','← '+avail[i-1].ru));else pn.append(el('span'));
  if(i<avail.length-1)pn.append(link('#/test/'+tid+'/'+avail[i+1].id,'btn',avail[i+1].ru+' →'));
  app.append(pn);
  if(taskId){var target=document.getElementById('t-'+taskId);if(target)setTimeout(function(){target.scrollIntoView();},0);}
}

/* ---------- Прогресс ---------- */
function progressPage(){
  title('Прогресс');setActive('progress');wide(false);
  tophead(null,'Прогресс','Что уже решено и что повторять');
  var cat=(B1.catalog||[]).filter(function(c){return (c.kind==='exam'||c.kind==='sample')&&dataById(c.id);});
  var done=cat.filter(function(c){return isDone(dataById(c.id));}).length;
  var started=cat.filter(function(c){var s=autoStat(dataById(c.id));return s.n>0;}).length;
  var g=el('div','stats');
  function stat(v,k,href){var a=href?link(href,'stat'):el('div','stat');a.append(el('span','stat-v',String(v)),el('span','stat-k',k));g.append(a);}
  stat(done+' / '+cat.length,'тестов пройдено целиком','#/tests');
  stat(started,'тестов начато','#/tests');
  stat(mistakes().length,'заданий с ошибками','#/mistakes');
  stat(S.words.all().length,'слов в словаре','#/dict/words');
  stat(S.words.dueCount(),'карточек к повторению','#/dict');
  stat(S.comments.all().filter(function(c){return c.tag==='Вопрос'&&!c.done;}).length,'открытых вопросов','#/dict/comments');
  app.append(g);
  var s=section('Задания по разделам','Все задания из тестов и сборника');
  SEC.forEach(function(x){
    var st=typeStat(x.id);
    var a=link('#/type/'+x.id,'prow');
    var l=el('span','prow-l');l.append(el('span','lrow-t',x.ru));
    if(x.id==='pis'||x.id==='mow'){l.append(el('span','lrow-s','Наборов в тренажёре: '+st.total+'. Оценка в чате.'));}
    else{l.append(el('span','lrow-s','Решено '+st.done+' из '+st.total));l.append(bar(st.total?st.done*100/st.total:0));}
    a.append(l);s.append(a);
  });
}

/* ---------- Поиск ---------- */
function searchPage(){
  title('Поиск');setActive(null);wide(false);
  var hd=el('div','tophead search-h');
  var bk=link('#/','icbtn back');bk.setAttribute('aria-label','Назад');bk.append(UI.icon('back',22));
  bk.addEventListener('click',function(e){if(history.length>1){e.preventDefault();history.back();}});
  var lab=el('label','search-l');lab.append(el('span','sr','Поиск по сайту'));
  var inp=el('input');inp.type='search';inp.placeholder='Тесты, задания, слова, комментарии';inp.autocomplete='off';inp.spellcheck=false;inp.setAttribute('autocorrect','off');inp.setAttribute('autocapitalize','none');
  lab.append(inp);hd.append(bk,lab);app.append(hd);
  var out=el('div','search-r');app.append(out);
  function lower(s){return String(s||'').toLowerCase();}
  function render(){
    var q=inp.value.trim();out.replaceChildren();
    if(q.length<2){
      var rq=S.prefs.get('sq',[]);
      if(rq.length){var s1=el('section','block');s1.append(el('h2','h-s','Недавние запросы'));var cr=el('div','chiprow wrap');rq.forEach(function(x){cr.append(UI.btn('chip2 pl',x,function(){inp.value=x;render();}));});s1.append(cr);out.append(s1);}
      var rc=S.prefs.get('recent',[]);
      if(rc.length){var s2=el('section','block');s2.append(el('h2','h-s','Недавно открывали'));rc.forEach(function(x){s2.append(rowLink(x.href,x.t,UI.shortDate(x.at)));});out.append(s2);}
      if(!rq.length&&!rc.length)out.append(el('p','meta','Начните печатать: найдутся тесты, задания, слова из словаря и комментарии.'));
      return;
    }
    var n=lower(q),groups=[];
    var tests=(B1.catalog||[]).filter(function(c){return lower(c.name+' '+c.note).indexOf(n)>-1;}).map(function(c){return {h:'#/test/'+c.id,t:c.name,s:KIND_LABEL[c.kind]};});
    groups.push(['Тесты',tests]);
    var tasks=[];
    (B1.catalog||[]).forEach(function(c){var t=dataById(c.id);if(!t)return;
      AUTO.forEach(function(sid){var m=findMod(t,sid);if(!m)return;m.tasks.forEach(function(k){
        var hay=lower(taskName(k)+' '+typeLabel(k)+' '+(k.instr||[]).join(' '));
        if(hay.indexOf(n)>-1)tasks.push({h:taskUrl(t.id,sid,k),t:(c.kind==='book'?'':romanOf(k)+'. ')+taskName(k),s:c.name+' · '+secById(sid).ru});
      });});
    });
    groups.push(['Задания',tasks]);
    groups.push(['Слова',S.words.all().filter(function(w){return lower(w.pl+' '+w.tr+' '+w.forms).indexOf(n)>-1;}).map(function(w){return {h:'#/dict/words?w='+w.id,t:w.pl,s:w.tr,pl:true};})]);
    groups.push(['Комментарии',S.comments.all().filter(function(c){return lower(c.text+' '+c.quote).indexOf(n)>-1;}).map(function(c){return {h:'#/dict/comments?c='+c.id,t:(c.quote?'«'+c.quote+'» · ':'')+c.text,s:c.src};})]);
    var any=false;
    groups.forEach(function(g){
      if(!g[1].length)return;any=true;
      var s=el('section','block');s.append(el('h2','h-s',g[0]+' · '+g[1].length));
      g[1].slice(0,8).forEach(function(r){var a=rowLink(r.h,r.t,r.s);if(r.pl)a.querySelector('.lrow-t').classList.add('pl');a.addEventListener('click',function(){saveQ(q);});s.append(a);});
      if(g[1].length>8)s.append(el('p','meta','И ещё '+(g[1].length-8)+'. Уточните запрос.'));
      out.append(s);
    });
    if(!any){
      var e=el('div','empty');
      e.append(el('h2',null,'Ничего не найдено по «'+q+'»'),el('p',null,'Проверьте написание или попробуйте часть слова. Если это слово из текста, его можно сразу добавить в словарь.'));
      e.append(UI.btn('btn2 primary','Добавить «'+q+'» в словарь',function(){saveQ(q);UI.wordForm({prefill:{pl:q,src:'Поиск'}});}));
      out.append(e);
    }
  }
  function saveQ(q){var r=S.prefs.get('sq',[]).filter(function(x){return x!==q;});r.unshift(q);S.prefs.set('sq',r.slice(0,6));}
  var deb=null;inp.addEventListener('input',function(){clearTimeout(deb);deb=setTimeout(render,120);});
  inp.addEventListener('keydown',function(e){if(e.key==='Enter'&&inp.value.trim().length>1)saveQ(inp.value.trim());});
  render();setTimeout(function(){inp.focus();},50);
}

/* ---------- Уровень и язык; первый запуск ---------- */
function choiceCard(t,sub,on,disabled,onPick){
  var b=UI.btn('opt2'+(on?' on':''),null,disabled?null:onPick);
  b.setAttribute('aria-pressed',String(!!on));
  if(disabled){b.disabled=true;b.classList.add('dis');}
  var r=el('span','ring');b.append(r);
  var l=el('span','opt2-l');l.append(el('span','opt2-t',t),el('span','opt2-s',sub));b.append(l);
  if(disabled)b.append(soon());
  return b;
}
function settingsBody(host){
  host.append(el('h2','h-s','Уровень'));
  host.append(choiceCard('A2','Основа для B1',false,true),choiceCard('B1','Экзамены и учебник',true,false,function(){}),choiceCard('B2','Всё из B1 плюс новое для B2',false,true));
  host.append(el('p','meta','Уровни складываются: B2 будет показывать всё из B1 и добавлять своё. Слова в словаре уровня не имеют, прогресс и ошибки остаются.'));
  host.append(el('h2','h-s','Язык объяснений'));
  host.append(choiceCard('Русский','Объяснения и переводы слов',true,false,function(){}),choiceCard('English','Explanations and word translations',false,true));
  host.append(el('p','meta','Польский текст и примеры не переводятся. Меняются объяснения, подсказки и переводы слов.'));
}
function settingsPage(){
  title('Уровень и язык');setActive(null);wide(false);
  tophead('#/','Уровень и язык');
  var c=el('div','settings');settingsBody(c);app.append(c);
  app.append(link('#/','btn2 primary wide-b','Готово'));
}
function welcome(step){
  title('Добро пожаловать');setActive(null);wide(false);
  document.body.classList.add('first-run');
  if(step!==2){
    var w=el('div','welcome');
    w.append(el('p','step','Шаг 1 из 2'),el('h1','pl','Polski'),el('p','lead','Подготовка к экзамену B1 и учебник польского'));
    var c=el('div','settings');settingsBody(c);w.append(c);
    w.append(UI.btn('btn2 primary wide-b','Далее',function(){app.replaceChildren();welcome(2);UI.afterRoute({noFab:true});}));
    app.append(w);return;
  }
  var w2=el('div','welcome');
  var bk=UI.btn('icbtn back',null,function(){app.replaceChildren();welcome(1);UI.afterRoute({noFab:true});});bk.setAttribute('aria-label','Назад');bk.append(UI.icon('back',22));
  w2.append(bk,el('p','step','Шаг 2 из 2'),el('h1',null,'С чего начнём?'));
  function done(){S.prefs.set('onboarded',true);document.body.classList.remove('first-run');}
  [['#/exams','Пробный тест','Увидеть свой уровень на реальном экзамене'],
   ['#/type/gram','Грамматика','Задания по грамматике из экзаменов и сборника'],
   ['#/dict','Первое слово','Добавить слово в свой словарь']].forEach(function(x,i){
    var a=rowLink(x[0],x[1],x[2]);a.prepend(el('span','num',String(i+1)));a.addEventListener('click',done);w2.append(a);
  });
  var sk=link('#/','btn2 wide-b','Пропустить, посмотреть сайт');sk.addEventListener('click',function(e){done();e.preventDefault();route();});
  w2.append(sk);app.append(w2);
}

/* ---------- подпись источника для слов и комментариев ---------- */
function labelFor(scopeEl){
  if(scopeEl&&scopeEl.dataset.cscope){
    var p=scopeEl.dataset.cscope.split('/'),tid=p[0],kid=p.slice(1).join('/');
    var c=entryById(tid),t=dataById(tid);
    if(c&&t){
      if(/^w-/.test(kid))return {src:c.name+' › Письмо · '+kid.replace(/^w-/,'zestaw ').replace(/-(a|b)$/,', $1'),href:'#/test/'+tid+'/pis'};
      if(/^m-/.test(kid))return {src:c.name+' › Говорение',href:'#/test/'+tid+'/mow'};
      for(var i=0;i<AUTO.length;i++){var m=findMod(t,AUTO[i]);if(!m)continue;
        var k=m.tasks.filter(function(x){return x.id===kid;})[0];
        if(k)return {src:c.name+' › '+secById(AUTO[i]).ru+' · зад. '+romanOf(k),href:taskUrl(tid,AUTO[i],k)};
      }
    }
  }
  return {src:pageLabel||SITE,href:location.hash||'#/'};
}
B1.app={labelFor:labelFor,tophead:tophead,title:title,setActive:setActive,wide:wide,section:section,rowLink:rowLink,link:link,plural:plural};

/* ---------- маршрутизатор ---------- */
function route(){
  var hash=location.hash||'#/';
  var q=hash.indexOf('?');var query={};
  if(q>-1){hash.slice(q+1).split('&').forEach(function(kv){var p=kv.split('=');query[decodeURIComponent(p[0])]=decodeURIComponent(p[1]||'');});hash=hash.slice(0,q);}
  var parts=hash.replace(/^#\/?/,'').split('/').filter(Boolean).map(decodeURIComponent);
  app.replaceChildren();pageLabel='';
  document.body.classList.remove('first-run');
  var p=parts[0],opts={};
  if(p==='tests')testsPage();
  else if(p==='samples')testsPage('sample');
  else if(p==='exams')testsPage('exam');
  else if(p==='others')testsPage('other');
  else if(p==='practice')practicePage();
  else if(p==='mistakes')mistakesPage();
  else if(p==='type'||p==='section')typePage(parts[1],parts[2]);
  else if(p==='task')taskPage(parts[1],parts[2],parts[3]);
  else if(p==='test'){if(parts.length<3)testPage(parts[1]);else modulePage(parts[1],parts[2],parts[3]);}
  else if(p==='learn')learnPage(parts[1]);
  else if(p==='texts')textsPage();
  else if(p==='progress')progressPage();
  else if(p==='search'){searchPage();opts.noFab=true;opts.noComments=true;}
  else if(p==='settings'){settingsPage();opts.noFab=true;}
  else if(p==='welcome'){welcome(1);opts.noFab=true;}
  else if(p==='dict'){B1.dictPages(parts[1]||'cards',query);setActive('dict');opts.noFab=true;opts.noComments=true;}
  else home();
  if(document.body.classList.contains('first-run'))opts.noFab=true;
  if(!(p==='test'&&parts[3]))window.scrollTo(0,0);
  app.focus({preventScroll:true});
  rememberVisit();
  updateStickyOffsets();
  setupAudioAutopause();
  UI.afterRoute(opts);
}
B1.route=route;

/* --- закреплённые при прокрутке шапка раздела и плееры: смежные .mod-h/.taudio
   занимают одну и ту же полосу сверху и сменяют друг друга по мере прокрутки;
   когда плеер уходит вверх за пределы экрана, его звук останавливается --- */
function updateStickyOffsets(){
  var site=document.querySelector('.site');
  document.documentElement.style.setProperty('--hdr-h',(site?site.offsetHeight:56)+'px');
  var modh=document.querySelector('.mod-h');
  document.documentElement.style.setProperty('--modh-h',(modh?modh.offsetHeight:0)+'px');
}
window.addEventListener('resize',updateStickyOffsets);

var audioObserver=null;
function setupAudioAutopause(){
  if(audioObserver){audioObserver.disconnect();audioObserver=null;}
  var boxes=document.querySelectorAll('.taudio');
  if(!boxes.length||typeof IntersectionObserver==='undefined')return;
  var hdrPx=parseInt(getComputedStyle(document.documentElement).getPropertyValue('--hdr-h'))||56;
  audioObserver=new IntersectionObserver(function(entries){
    entries.forEach(function(en){
      if(en.isIntersecting||en.boundingClientRect.top>=0)return;
      var au=en.target.querySelector('audio');
      if(au&&!au.paused)au.pause();
    });
  },{rootMargin:'-'+hdrPx+'px 0px 0px 0px',threshold:0});
  boxes.forEach(function(box){audioObserver.observe(box);});
}

function loadScript(src){
  return new Promise(function(res){
    var s=document.createElement('script');s.src=src;s.onload=res;
    s.onerror=function(){console.error('Не загрузился '+src);res();};
    document.head.appendChild(s);
  });
}
var manifest=window.B1_MANIFEST||[];
buildChrome();
manifest.reduce(function(p,id){return p.then(function(){return loadScript('tests/'+id+'.js?v='+ASSET_VER);});},Promise.resolve()).then(function(){
  window.addEventListener('hashchange',route);
  route();
});
})();
