/* Приложение: маршруты (#/...), главная, список тестов, страницы теста, типа заданий и отдельного задания. */
(function(){
'use strict';
var B1=window.B1,U=B1.util,el=U.el,fmt=U.fmt;
var app=document.getElementById('app'),nav=document.getElementById('nav');
var SEC=B1.sections;
var SITE='Egzamin B1';
var AUTO=['sluch','czyt','gram'];
var flt={src:'all',type:'all',todo:false};

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
function srcText(c){return c.kind==='sample'?c.name:(c.kind==='book'?c.name:'Прошлый экзамен, '+c.name);}
function badge(c){return el('span','badge '+(c.kind==='sample'?'b-sample':(c.kind==='book'?'b-book':'b-exam')),c.kind==='sample'?'Образец':(c.kind==='book'?'Сборник':'Экзамен'));}
function typeLabel(d){
  if(d.kind==='choice')return (d.items&&d.items[0]&&d.items[0].inline)?'TAK / NIE':'Выбор ответа';
  if(d.kind==='gaps'){if(d.legend)return 'Фрагменты в тексте';if(d.box)return 'Слова из рамки';return (d.gaps&&d.gaps[0]&&d.gaps[0].opts)?'Выбор формы':'Пропуски';}
  return {match:'Сопоставление',slots:'Сопоставление',qa:'Вопросы',rewrite:'Перефразирование'}[d.kind]||'Задание';
}
function countText(d){
  var n=(d.items&&d.items.length)||(d.gaps&&d.gaps.length)||(d.rows&&d.rows.length)||0;
  return n?n+' '+plural(n,'пункт','пункта','пунктов'):'';
}
function taskName(d){return d.name||typeLabel(d);}
function taskUrl(tid,sid,k){return '#/task/'+tid+'/'+sid+'/'+k.id;}
function officialFile(c,which){var u=c.official&&c.official[which];return u?{url:u,exact:true}:{url:c.page,exact:false};}
function sheetPageUrl(c,page){
  var f=officialFile(c,'sheet');
  return (f.exact&&page)?f.url+'#page='+page:f.url;
}
function officialLinks(c){
  var s=officialFile(c,'sheet'),a=officialFile(c,'audio'),k=officialFile(c,'key');
  function lab(t,f){return f.exact?t:t+': на странице комиссии';}
  return [{t:lab('Лист заданий (PDF)',s),u:s.url},{t:lab('Запись (mp3)',a),u:a.url},{t:lab('Транскрипция и ключ (PDF)',k),u:k.url},{t:'Страница на сайте комиссии',u:c.page}];
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
/* все задания одного типа изо всех тестов, что есть в тренажёре */
function typeRows(sid){
  var rows=[];
  (B1.catalog||[]).forEach(function(c){
    var t=dataById(c.id);if(!t)return;
    if(sid==='pis'){
      (t.writing||[]).forEach(function(w){rows.push({c:c,t:t,sid:sid,w:w,set:true});});
      return;
    }
    var m=findMod(t,sid);if(!m||!m.tasks)return;
    var res=B1.results(t.id);
    m.tasks.forEach(function(k){rows.push({c:c,t:t,sid:sid,k:k,res:res[k.id]});});
  });
  return rows;
}
function typeStat(sid){
  var rows=typeRows(sid),done=rows.filter(function(r){return r.res!=null;}).length;
  return {total:rows.length,done:done};
}

/* ---------- шапка ---------- */
function buildNav(){
  var a=link('#/tests',null,'Тесты целиком');a.dataset.key='tests';nav.append(a);
  SEC.forEach(function(s){var x=link('#/type/'+s.id,null,s.ru);x.dataset.key=s.id;nav.append(x);});
}
function setActive(key){
  Array.prototype.forEach.call(nav.children,function(a){
    if(a.dataset.key===key)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');
  });
}
function crumbs(items){
  var c=el('nav','crumbs');c.setAttribute('aria-label','Путь');
  items.forEach(function(it,i){
    if(i)c.append(el('span','sep','/'));
    if(it.href)c.append(link(it.href,null,it.t));else c.append(el('span','here',it.t));
  });
  return c;
}
function wide(on){app.classList.toggle('wide',!!on);}

/* ---------- мелкие блоки ---------- */
function bar(pct){var b=el('span','bar');var f=el('span');f.style.width=Math.max(0,Math.min(100,pct))+'%';b.append(f);return b;}
function tile(href,title,desc,done,total,cap){
  var a=link(href,'tile');
  a.append(el('span','tile-t',title),el('span','tile-d',desc));
  var foot=el('span','tile-f');
  foot.append(bar(total?done*100/total:0),el('span','tile-c',cap));
  a.append(foot);return a;
}
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

/* ---------- главная ---------- */
function home(){
  document.title=SITE+': тренажёр к экзамену по польскому';
  setActive(null);wide(true);
  var hero=el('section','hero');
  hero.append(el('h1',null,'Egzamin certyfikatowy B1'),
    el('p','lead','Тренажёр к государственному экзамену по польскому как иностранному для взрослых. Настоящие экзамены комиссии, образцы и сборник заданий. У каждого теста и каждого задания указан источник и есть ссылка на официальный файл.'));
  app.append(hero);

  var cat=B1.catalog||[];
  var s1=el('section','block');
  var h1=el('div','block-h');h1.append(el('h2',null,'Тесты целиком'),link('#/tests',null,'Все тесты'));s1.append(h1);
  var grid=el('div','tiles t2');
  [['sample','Образцы','Образцы комиссии для взрослых: 2017, 2019 и 2020 годов.','#/samples'],['exam','Прошлые экзамены','Настоящие экзамены 2021–2024 годов: лист заданий, запись и ключ к каждому.','#/exams']].forEach(function(g){
    var list=cat.filter(function(c){return c.kind===g[0];});
    var avail=list.filter(function(c){return dataById(c.id);});
    var done=avail.filter(function(c){return isDone(dataById(c.id));}).length;
    grid.append(tile(g[3],g[1],g[2],done,list.length,'Пройдено '+done+' из '+list.length+'. В тренажёре: '+avail.length));
  });
  s1.append(grid);app.append(s1);

  var s2=el('section','block');
  var h2=el('div','block-h');h2.append(el('h2',null,'Задания по типам'),link('#/type/sluch',null,'Все типы'));
  s2.append(h2,el('p','meta','Все задания из тестов и сборника, собранные по типам. У каждого задания подписан источник.'));
  var g2=el('div','tiles t6');
  SEC.forEach(function(s){
    var st=typeStat(s.id),cap,pct=st.total?st.done:0;
    var d=s.id==='mow'?'Говорение. Только сборник 2017.':s.ru+'. Из 18 тестов и сборника.';
    if(s.id==='mow')cap='Раздел появится позже';
    else if(s.id==='pis')cap='Наборов в тренажёре: '+st.total;
    else cap='Решено '+st.done+' из '+st.total;
    var a=tile('#/type/'+s.id,s.pl,d,s.id==='pis'?0:pct,s.id==='pis'?0:st.total,cap);
    a.classList.add(s.id==='pis'||s.id==='mow'?'span3':'span2');
    g2.append(a);
  });
  s2.append(g2);app.append(s2);
}

/* ---------- тесты целиком ---------- */
var LISTS={
  sample:{ttl:'Образцы',href:'#/samples',sub:'Три образца комиссии для взрослых: 2017, 2019 и 2020 годов. У каждого подписан источник, файлы комиссии лежат под кнопкой с тремя точками.'},
  exam:{ttl:'Прошлые экзамены',href:'#/exams',sub:'Настоящие экзамены комиссии 2021–2024 годов. Тест открывается целиком: четыре письменные части с таймером и общим счётом. Файлы комиссии лежат под кнопкой с тремя точками.'}
};
function testsPage(kind){
  var L=kind?LISTS[kind]:null;
  var ttl=L?L.ttl:'Тесты целиком';
  document.title=ttl+' | '+SITE;setActive('tests');wide(true);
  var cr=[{t:SITE,href:'#/'}];if(L)cr.push({t:'Тесты целиком',href:'#/tests'});cr.push({t:ttl});
  app.append(crumbs(cr));
  var cat=(B1.catalog||[]).filter(function(c){return c.kind!=='book'&&(!kind||c.kind===kind);});
  var avail=cat.filter(function(c){return dataById(c.id);}).length;
  var h=el('header','page-h');
  h.append(el('h1',null,ttl),el('p','sub',L?L.sub:'Тест открывается целиком: четыре письменные части с таймером и общим счётом. У каждого теста подписан источник, файлы комиссии лежат под кнопкой с тремя точками.'));
  if(L)h.append(el('p','meta','В тренажёре сейчас: '+avail+' из '+cat.length+'.'));
  app.append(h);
  var lists=el('div','rows');
  var shownKind=null,shownGroup=null;
  cat.forEach(function(c){
    if(!L&&c.kind!==shownKind){
      var h2=el('h2');h2.append(link(LISTS[c.kind].href,null,LISTS[c.kind].ttl));lists.append(h2);shownKind=c.kind;shownGroup=null;
    }
    if(c.kind==='exam'&&c.group!==shownGroup){lists.append(el('h3','grp',c.group));shownGroup=c.group;}
    var t=dataById(c.id);
    var row=el('div','trow2');
    var nm=el('div','trow2-n');
    if(t)nm.append(link('#/test/'+c.id,'trow2-a',c.name));else nm.append(el('span','trow2-a off',c.name));
    var note=c.note||'';if(!t)note=(note?note+'. ':'')+'В тренажёр добавим позже';
    if(note)nm.append(el('span','meta',note));
    row.append(nm,el('div','trow2-r',t?resultText(t):'—'),filesMenu(c));
    lists.append(row);
  });
  app.append(lists);
}

/* ---------- страница теста ---------- */
function testPage(tid){
  var c=entryById(tid),t=dataById(tid);
  if(!c)return home();
  if(c.kind==='book'){location.hash='#/type/gram';return;}
  document.title=srcText(c)+' | '+SITE;setActive('tests');wide(true);
  app.append(crumbs([{t:SITE,href:'#/'},{t:'Тесты целиком',href:'#/tests'},{t:LISTS[c.kind].ttl,href:LISTS[c.kind].href},{t:c.name}]));
  var h=el('header','page-h');h.append(el('h1',null,c.name),el('p','sub',(c.kind==='sample'?'Образец комиссии':'Прошлый экзамен')+', B1 для взрослых'+(c.note?'. '+c.note:'')));
  app.append(h);
  var wrap=el('div','two');
  var left=el('div','two-l');
  if(!t){
    left.append(el('div','note big',null));
    left.lastChild.append(el('p',null,'Этот тест ещё не добавлен в тренажёр. Официальные файлы можно открыть справа.'));
  }else{
    var st=autoStat(t);
    left.append(el('h2',null,'Части экзамена'));
    var toc=el('ol','toc');
    SEC.forEach(function(s){
      var li=el('li');
      if(!hasSection(t,s.id)){
        var d=el('div','toc-row off');d.append(el('span','pl',s.pl),el('span','ru',s.ru),el('span','cnt',s.id==='mow'?'в листе заданий нет':'нет в этом тесте'));li.append(d);
      }else{
        var a=link('#/test/'+t.id+'/'+s.id,'toc-row');var m=findMod(t,s.id);var p=modProgress(t,s.id);
        a.append(el('span','pl',s.pl),el('span','ru',s.ru));
        var cnt=el('span','cnt',s.id==='pis'?'разбор в чате':(p&&p.n?fmt(p.e)+' / '+fmt(p.max):'не начато'));
        a.append(cnt);
        a.append(el('span','tmeta',m?m.meta:''));
        li.append(a);
      }
      toc.append(li);
    });
    left.append(toc);
    var thr=el('section','card');
    thr.append(el('h2','h-s','Порог сдачи'),el('p','meta','Нужно набрать не меньше 50% в каждой части отдельно. Средний балл не считается.'));
    var g=el('div','thr');
    [['Аудирование','15 из 30'],['Чтение','15 из 30'],['Грамматика','15 из 30'],['Письмо','15 из 30'],['Говорение','20 из 40']].forEach(function(x){
      var b=el('div');b.append(el('span','k',x[0]),el('span','v',x[1]));g.append(b);
    });
    thr.append(g);left.append(thr);
  }
  var right=el('aside','two-r');
  var src=el('section','card');
  src.append(el('h2','h-s','Источник'),el('p','meta','Państwowa Komisja ds. Poświadczania Znajomości Języka Polskiego jako Obcego'));
  var ls=el('div','flist');
  officialLinks(c).forEach(function(l){var a=link(l.u,'flink');a.target='_blank';a.rel='noopener';a.append(el('span',null,l.t));ls.append(a);});
  src.append(ls);right.append(src);
  if(t){
    var rs=el('section','card');var st2=autoStat(t);
    rs.append(el('h2','h-s','Ваш результат'));
    var big=el('p','big-r');big.append(el('span',null,'Razem '),el('span','fill',st2.n?fmt(st2.e):'\u00a0'),el('span','of',' / '+fmt(st2.max)+' p.'));
    rs.append(big,el('p','meta','Три автоматически проверяемые части'+(st2.n?', проверено заданий: '+st2.n+' из '+st2.total:'')+'. Письмо разбираем отдельно.'));
    right.append(rs);
  }
  wrap.append(left,right);app.append(wrap);
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
function speakingBox(){
  var b=el('div','note big');
  b.append(el('p',null,'Раздел «Говорение» появится позже: сначала нужны материалы устной части (карточки заданий из сборника, критерии оценки).'),
           el('p',null,'Автоматически оценивать речь я не смогу, поэтому здесь будут карточки, таймер подготовки и ответа, запись вашего голоса в браузере и самооценка по критериям.'));
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
function typePage(sid){
  var s=secById(sid);if(!s)return home();
  if(flt.sid!==sid)flt={src:'all',type:'all',todo:false,sid:sid};
  document.title=s.ru+' | '+SITE;setActive(sid);wide(true);
  app.append(crumbs([{t:SITE,href:'#/'},{t:'Задания по типам'},{t:s.ru}]));
  var h=el('header','page-h');h.append(el('h1',null,s.pl),el('p','sub',s.ru));app.append(h);
  if(sid==='mow'){app.append(speakingBox());return;}
  var all=typeRows(sid);
  if(!all.length){app.append(el('p','meta','Заданий этого типа в тренажёре пока нет.'));return;}
  app.append(el('p','lead',sid==='pis'?'Наборы заданий из тестов. Выберите один набор и выполните оба задания, как на экзамене.':'Задания из тестов, что уже добавлены в тренажёр. Слева название, справа источник и ссылка на лист комиссии.'));
  var box=el('div','filters');var listHost=el('div','rows');
  function render(){
    box.replaceChildren();listHost.replaceChildren();
    var srcOpts=[{v:'all',t:'Все'}];
    if(all.some(function(r){return r.c.kind==='sample';}))srcOpts.push({v:'sample',t:'Образцы'});
    if(all.some(function(r){return r.c.kind==='exam';}))srcOpts.push({v:'exam',t:'Прошлые экзамены'});
    if(all.some(function(r){return r.c.kind==='book';}))srcOpts.push({v:'book',t:'Сборник'});
    box.append(chipRow('Источник',srcOpts,flt.src,function(v){flt.src=v;render();}));
    if(sid!=='pis'){
      var types=[];all.forEach(function(r){var l=typeLabel(r.k);if(types.indexOf(l)<0)types.push(l);});
      box.append(chipRow('Тип задания',[{v:'all',t:'Все'}].concat(types.map(function(x){return {v:x,t:x};})),flt.type,function(v){flt.type=v;render();}));
      box.append(chipRow('Показывать',[{v:false,t:'Все'},{v:true,t:'Нерешённые'}],flt.todo,function(v){flt.todo=v;render();}));
    }
    var rows=all.filter(function(r){
      if(flt.src!=='all'&&r.c.kind!==flt.src)return false;
      if(sid!=='pis'){if(flt.type!=='all'&&typeLabel(r.k)!==flt.type)return false;if(flt.todo&&r.res!=null)return false;}
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
        n.append(link('#/test/'+r.t.id+'/pis','trow2-a','Zestaw '+r.w.id+': '+r.w.a.genre+' + '+r.w.b.genre),el('span','meta','Два задания: a ('+r.w.a.words+' слов) и b ('+r.w.b.words+' слов)'));
        row.append(n,el('span',null,'Письмо'),el('span','pts','30'));
        pg=(findMod(r.t,'pis')||{}).page;
      }else{
        n.append(link(taskUrl(r.t.id,sid,r.k),'trow2-a',r.c.kind==='book'?taskName(r.k):romanOf(r.k)+'. '+taskName(r.k)),el('span','meta',countText(r.k)));
        row.append(n,el('span',null,typeLabel(r.k)),el('span','pts',fmt(r.k.max)));
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
  document.title='Задание '+romanOf(d)+', '+s.ru+', '+c.name+' | '+SITE;setActive(sid);wide(false);
  app.append(crumbs([{t:SITE,href:'#/'},{t:s.ru,href:'#/type/'+sid},{t:c.name,href:'#/test/'+tid},{t:'Задание '+romanOf(d)}]));
  var box=el('section','srcbar');
  var l=el('div');
  var top=el('div','srcbar-t');top.append(badge(c),el('strong',null,srcText(c)+', задание '+romanOf(d)));
  l.append(top,el('span','meta',c.kind==='book'?'Максимум '+fmt(d.max)+' баллов. '+taskName(d)+'.':'Максимум '+fmt(d.max)+' из '+fmt(m.max)+' баллов. '+taskName(d)+'.'));
  var a=link(sheetPageUrl(c,d.page),'flink',null);a.target='_blank';a.rel='noopener';a.append(el('span',null,officialFile(c,'sheet').exact?(d.page?'Открыть в листе комиссии, стр. '+d.page:'Открыть лист комиссии'):'Открыть страницу комиссии со сборником'));
  box.append(l,a);app.append(box);
  var engine=B1.engine(t);B1.current=engine;
  app.append(engine.renderTask(m,taskId));
  var i=m.tasks.indexOf(d);var pn=el('nav','pn');pn.setAttribute('aria-label','Соседние задания');
  if(i>0)pn.append(link(taskUrl(tid,sid,m.tasks[i-1]),'btn','← '+romanOf(m.tasks[i-1])+'. '+taskName(m.tasks[i-1])));else pn.append(el('span'));
  if(i<m.tasks.length-1)pn.append(link(taskUrl(tid,sid,m.tasks[i+1]),'btn',romanOf(m.tasks[i+1])+'. '+taskName(m.tasks[i+1])+' →'));
  app.append(pn);
  if(c.kind!=='book'){var more=el('p','meta');more.append(link('#/test/'+tid+'/'+sid,null,'Открыть весь раздел «'+s.ru+'» этого теста с таймером'));app.append(more);}
}

/* ---------- раздел теста целиком (с таймером) ---------- */
function modulePage(tid,sid,taskId){
  var c=entryById(tid),t=dataById(tid);
  if(!c||!t)return testPage(tid);
  var s=secById(sid);if(!s||!hasSection(t,sid))return testPage(tid);
  document.title=s.ru+', '+c.name+' | '+SITE;setActive(null);wide(false);
  app.append(crumbs([{t:SITE,href:'#/'},{t:'Тесты целиком',href:'#/tests'},{t:c.name,href:'#/test/'+tid},{t:s.ru}]));
  var m=findMod(t,sid);
  var box=el('section','srcbar');var l=el('div');
  var top=el('div','srcbar-t');top.append(badge(c),el('strong',null,srcText(c)));l.append(top);
  var a=link(sheetPageUrl(c,m.page),'flink',null);a.target='_blank';a.rel='noopener';a.append(el('span',null,m.page?'Открыть в листе комиссии, стр. '+m.page:'Открыть лист комиссии'));
  box.append(l,a);app.append(box);
  var engine=B1.engine(t);B1.current=engine;
  app.append(engine.renderModule(m));
  var avail=SEC.filter(function(x){return hasSection(t,x.id);});
  var i=avail.map(function(x){return x.id;}).indexOf(sid);
  var pn=el('nav','pn');pn.setAttribute('aria-label','Соседние разделы');
  if(i>0)pn.append(link('#/test/'+tid+'/'+avail[i-1].id,'btn',avail[i-1].ru));else pn.append(el('span'));
  if(i<avail.length-1)pn.append(link('#/test/'+tid+'/'+avail[i+1].id,'btn',avail[i+1].ru));
  app.append(pn);
  if(taskId){var target=document.getElementById('t-'+taskId);if(target)target.scrollIntoView();}
}

/* ---------- маршрутизатор ---------- */
function route(){
  var parts=(location.hash||'#/').replace(/^#\/?/,'').split('/').filter(Boolean).map(decodeURIComponent);
  app.replaceChildren();
  var p=parts[0];
  if(p==='tests')testsPage();
  else if(p==='samples')testsPage('sample');
  else if(p==='exams')testsPage('exam');
  else if(p==='type')typePage(parts[1]);
  else if(p==='section')typePage(parts[1]);
  else if(p==='task')taskPage(parts[1],parts[2],parts[3]);
  else if(p==='test'){if(parts.length<3)testPage(parts[1]);else modulePage(parts[1],parts[2],parts[3]);}
  else home();
  if(!(p==='test'&&parts[3]))window.scrollTo(0,0);
  app.focus({preventScroll:true});
}

function loadScript(src){
  return new Promise(function(res){
    var s=document.createElement('script');s.src=src;s.onload=res;
    s.onerror=function(){console.error('Не загрузился '+src);res();};
    document.head.appendChild(s);
  });
}
var manifest=window.B1_MANIFEST||[];
manifest.reduce(function(p,id){return p.then(function(){return loadScript('tests/'+id+'.js');});},Promise.resolve()).then(function(){
  buildNav();
  window.addEventListener('hashchange',route);
  route();
});
})();
