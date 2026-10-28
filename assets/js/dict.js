/* Раздел «Словарь»: карточки на повторение, список слов, все комментарии. */
(function(){
'use strict';
var B1=window.B1,el=B1.util.el,S=B1.store,UI=B1.ui;
var app=document.getElementById('app');
var st={tab:'cards',mode:'due',q:'',topic:'all',cf:'all',menu:null,queue:null,idx:0,flipped:false,reviewed:0,grading:false,hl:null};

function A(){return B1.app;}
function lower(s){return String(s||'').toLowerCase();}
function head(){
  A().tophead(null,'Мой словарь');
  var seg=el('div','seg');seg.setAttribute('role','tablist');
  [['cards','Карточки','#/dict'],['words','Слова','#/dict/words'],['comments','Комментарии','#/dict/comments']].forEach(function(x){
    var a=A().link(x[2],'seg-i'+(st.tab===x[0]?' on':''),x[1]);
    if(st.tab===x[0])a.setAttribute('aria-current','page');
    seg.append(a);
  });
  app.append(seg);
}
function searchBox(ph,onInput){
  var l=el('label','search-l');l.append(el('span','sr',ph));
  var i=el('input');i.type='search';i.placeholder=ph;i.value=st.q;i.autocomplete='off';i.spellcheck=false;i.setAttribute('autocapitalize','none');
  i.addEventListener('input',function(){st.q=i.value;onInput();});
  l.append(i);return l;
}
function addBtn(){
  return UI.btn('btn2 primary add-w',null,function(){UI.wordForm({prefill:{src:'Словарь'}});});
}
function withAdd(){var b=addBtn();b.append(UI.icon('plus',18),document.createTextNode('Добавить слово или фразу'));return b;}
function empty(h,p,btns){
  var e=el('div','empty');e.append(el('h2',null,h),el('p',null,p));
  btns.forEach(function(b){e.append(b);});
  app.append(e);
}
function emptyWords(){
  var b1=UI.btn('btn2 primary','Добавить своё слово',function(){UI.wordForm({prefill:{src:'Словарь'}});});
  empty('В словаре пока нет слов','Выделите слово в любом тексте сайта: долгое нажатие, затем «В словарь» в полоске сверху. Можно и вписать своё слово.',[b1,A().link('#/practice','btn2','Открыть задания')]);
}

/* ---------- карточки ---------- */
function buildQueue(){
  var list=S.words.cards(st.mode==='due');
  if(st.q){var n=lower(st.q);list=list.filter(function(c){return lower(c.w.pl+' '+c.w.tr).indexOf(n)>-1;});}
  st.queue=list.map(function(c){return {id:c.w.id,dir:c.dir,again:0};});
  st.idx=0;st.flipped=false;st.reviewed=0;
}
function cardsTab(){
  var total=S.words.all().length;
  if(!total){emptyWords();return;}
  app.append(searchBox('Найти слово',function(){buildQueue();renderCards();}));
  var due=S.words.dueCount(),all=S.words.cards(false).length;
  var cr=el('div','chiprow');
  [['due','К повторению · '+due],['all','Все · '+all]].forEach(function(x){
    cr.append(UI.btn('chip2'+(st.mode===x[0]?' on':''),x[1],function(){st.mode=x[0];buildQueue();B1.route();}));
  });
  app.append(cr);
  var host=el('div','cards-host');app.append(host);
  if(!st.queue)buildQueue();
  function renderCards(){
    host.replaceChildren();
    var q=st.queue;
    if(st.idx>=q.length){
      var e=el('div','empty');
      if(st.reviewed){e.append(el('h2',null,'На сегодня всё'),el('p',null,'Вы повторили '+st.reviewed+' '+A().plural(st.reviewed,'карточку','карточки','карточек')+'. Следующие карточки откроются, когда подойдёт их срок.'));}
      else if(st.q){e.append(el('h2',null,'Ничего не найдено'),el('p',null,'Ни одна карточка не подходит под «'+st.q+'».'));}
      else{e.append(el('h2',null,st.mode==='due'?'Сегодня повторять нечего':'Карточек нет'),el('p',null,'Все карточки повторены вовремя. Можно повторить всё равно или добавить новые слова.'));}
      e.append(A().link('#/dict/words','btn2','Открыть список слов'));
      e.append(UI.btn('btn2 primary','Повторить всё равно',function(){st.mode='all';buildQueue();B1.route();}));
      host.append(e);return;
    }
    var item=q[st.idx],w=S.words.get(item.id);
    if(!w){st.idx++;renderCards();return;}
    var back=item.dir==='b';
    host.append(el('p','meta cpos','Карточка '+(st.idx+1)+' из '+q.length+(back?' · перевод → польский':'')));
    var card=UI.btn('fcard'+(st.flipped?' flipped':''),null,function(){st.flipped=!st.flipped;renderCards();});
    card.setAttribute('aria-label',st.flipped?'Карточка, обратная сторона. Нажмите, чтобы перевернуть':'Карточка. Нажмите, чтобы перевернуть');
    if(!st.flipped){
      card.append(el('span','fc-main'+(back?'':' pl'),back?w.tr:w.pl),el('span','fc-hint','Нажмите, чтобы перевернуть'));
    }else{
      card.append(el('span','fc-main'+(back?' pl':''),back?w.pl:w.tr));
      if(w.forms)card.append(el('span','fc-forms pl',w.forms));
      if(w.ex)card.append(el('span','fc-ex pl',w.ex));
      if(w.src)card.append(el('span','fc-src','из раздела: '+w.src));
    }
    host.append(card);
    var row=el('div','fc-btns');
    row.append(UI.btn('btn2','Не помню',function(){grade(item,false);}),UI.btn('btn2 primary','Помню',function(){grade(item,true);}));
    host.append(row);
  }
  function grade(item,ok){
    st.grading=true;
    var w=S.words.get(item.id);
    var wasDue=w&&((w.srs||{})[item.dir]||{due:0}).due<=Date.now();
    if(!ok){S.words.grade(item.id,item.dir,false);if(item.again<2)st.queue.push({id:item.id,dir:item.dir,again:item.again+1});}
    else if(wasDue||st.mode==='due')S.words.grade(item.id,item.dir,true);
    st.grading=false;
    st.reviewed++;st.idx++;st.flipped=false;renderCards();
  }
  renderCards();
  app.append(withAdd());
}

/* ---------- список слов ---------- */
function wordsTab(query){
  var all=S.words.all();
  if(!all.length){emptyWords();return;}
  if(query&&query.w)st.hl=query.w;
  app.append(searchBox('Найти слово',function(){renderList();}));
  var topics=[];all.forEach(function(w){if(w.topic&&topics.indexOf(w.topic)<0)topics.push(w.topic);});
  if(topics.length){
    var cr=el('div','chiprow scroll');
    [['all','Все · '+all.length]].concat(topics.map(function(t){return [t,t+' · '+all.filter(function(w){return w.topic===t;}).length];})).forEach(function(x){
      cr.append(UI.btn('chip2'+(st.topic===x[0]?' on':''),x[1],function(){st.topic=x[0];B1.route();}));
    });
    app.append(cr);
  }
  var cnt=el('p','meta');app.append(cnt);
  var host=el('div','wlist');app.append(host);
  function renderList(){
    host.replaceChildren();
    var n=lower(st.q);
    var list=all.filter(function(w){return (st.topic==='all'||w.topic===st.topic)&&(!n||lower(w.pl+' '+w.tr+' '+w.forms).indexOf(n)>-1);});
    cnt.textContent='Слов в словаре: '+all.length+(list.length!==all.length?', показано: '+list.length:'');
    if(!list.length){host.append(el('p','meta','Ничего не найдено.'));return;}
    list.forEach(function(w){
      var r=el('div','witem'+(st.hl===w.id?' hl':''));r.id='w-'+w.id;
      var l=el('div','witem-l');
      l.append(el('span','witem-pl pl',w.pl));
      if(w.forms)l.append(el('span','witem-f pl',w.forms));
      l.append(el('span','witem-tr',w.tr));
      var meta=[];if(w.src)meta.push(w.src);if(w.topic)meta.push(w.topic);
      if(meta.length){var m=el('span','witem-s');if(w.srcHref){m.append(A().link(w.srcHref,null,meta[0]));if(meta[1])m.append(' · '+meta[1]);}else m.textContent=meta.join(' · ');l.append(m);}
      var mb=UI.btn('icbtn',null,function(){st.menu=st.menu===w.id?null:w.id;renderList();});
      mb.setAttribute('aria-label','Действия со словом '+w.pl);mb.setAttribute('aria-expanded',String(st.menu===w.id));mb.append(UI.icon('dots',22));
      r.append(l,mb);
      if(st.menu===w.id){
        var a=el('div','witem-a');
        a.append(UI.btn('btn2 small','Изменить',function(){st.menu=null;UI.wordForm({word:w});}));
        if(B1.review&&B1.review.on())a.append(UI.btn('btn2 small','Замечание',function(){st.menu=null;B1.review.form({prefill:{scope:'dict:'+w.id,quote:w.pl+' — '+w.tr,src:'Словарь › '+w.pl,href:'#/dict/words?w='+encodeURIComponent(w.id),type:'dict'}});}));
        a.append(UI.btn('btn2 small danger','Удалить',function(){st.menu=null;var rem=S.words.remove(w.id);UI.toast('Слово удалено',function(){S.words.restore(rem);});}));
        r.append(a);
      }
      host.append(r);
    });
    if(st.hl){var t=document.getElementById('w-'+st.hl);if(t)setTimeout(function(){t.scrollIntoView({block:'center'});},0);}
  }
  renderList();
  app.append(withAdd());
}

/* ---------- все комментарии ---------- */
var TYPES=[['all','Все'],['Вопрос','Вопросы'],['Запомнить','Запомнить'],['Ошибка в материале','Ошибки'],['Заметка','Заметки']];
function commentsTab(query){
  if(B1.review&&B1.review.on())return B1.review.commentsTab(query||{});
  var all=S.comments.all();
  if(query&&query.c)st.hl=query.c;
  if(!all.length){
    empty('Комментариев пока нет','Выделите текст в задании или правиле и нажмите «Комментарий» в полоске сверху. Ко всему заданию — кнопка с облачком в его шапке. На страницах комментарии скрыты, пока их не включить.',[A().link('#/practice','btn2 primary','Открыть задания')]);
    return;
  }
  app.append(searchBox('Найти комментарий',function(){renderList();}));
  var cr=el('div','chiprow scroll');
  TYPES.forEach(function(x){
    var n=x[0]==='all'?all.length:all.filter(function(c){return c.tag===x[0];}).length;
    if(x[0]!=='all'&&!n)return;
    cr.append(UI.btn('chip2'+(st.cf===x[0]?' on':''),x[1]+' · '+n,function(){st.cf=x[0];B1.route();}));
  });
  app.append(cr);
  var host=el('div','clist');app.append(host);
  function renderList(){
    host.replaceChildren();
    var n=lower(st.q);
    var list=all.filter(function(c){return (st.cf==='all'||c.tag===st.cf)&&(!n||lower(c.text+' '+c.quote+' '+c.src).indexOf(n)>-1);});
    if(!list.length){host.append(el('p','meta','Здесь пока ничего нет.'));return;}
    list.forEach(function(c){
      var d=el('div','ccard'+(c.done?' done':'')+(st.hl===c.id?' hl':''));d.id='c-'+c.id;
      var h=A().link(c.href||'#/','ccard-h');h.append(el('span','ccard-src',c.src||'Без источника'),el('span','ccard-d',UI.shortDate(c.created)));
      d.append(h);
      if(c.quote)d.append(el('p','quote pl',c.quote));
      d.append(el('p','ccard-t',c.text));
      var f=el('div','ccard-f');
      f.append(el('span','ctag '+(UI.TAGCLS[c.tag]||''),c.tag));
      var acts=el('span','ccard-a');
      if(c.tag!=='Заметка'){
        var rb=UI.btn('chip2 small'+(c.done?' ok':''),c.done?'Решено':'Отметить решённым',function(){S.comments.update(c.id,{done:!c.done});});
        rb.setAttribute('aria-pressed',String(!!c.done));acts.append(rb);
      }
      var mb=UI.btn('icbtn',null,function(){st.menu=st.menu===c.id?null:c.id;renderList();});
      mb.setAttribute('aria-label','Действия с комментарием');mb.setAttribute('aria-expanded',String(st.menu===c.id));mb.append(UI.icon('dots',22));
      acts.append(mb);f.append(acts);d.append(f);
      if(st.menu===c.id){
        var a=el('div','witem-a');
        a.append(UI.btn('btn2 small','Изменить',function(){st.menu=null;UI.commentForm({comment:c});}));
        a.append(UI.btn('btn2 small danger','Удалить',function(){st.menu=null;var rem=S.comments.remove(c.id);UI.toast('Комментарий удалён',function(){S.comments.restore(rem);});}));
        d.append(a);
      }
      host.append(d);
    });
    if(st.hl){var t=document.getElementById('c-'+st.hl);if(t)setTimeout(function(){t.scrollIntoView({block:'center'});},0);}
  }
  renderList();
}

B1.dictPages=function(tab,query){
  if(['cards','words','comments'].indexOf(tab)<0)tab='cards';
  if(st.tab!==tab){st.q='';st.menu=null;st.hl=null;}
  if(tab!=='cards')st.queue=null;
  st.tab=tab;
  A().title(tab==='cards'?'Словарь: карточки':tab==='words'?'Словарь: слова':'Словарь: комментарии');
  A().wide(false);
  head();
  if(tab==='cards')cardsTab();else if(tab==='words')wordsTab(query);else commentsTab(query);
};
S.onChange(function(k){
  if(st.grading)return;
  if(!/^#\/dict/.test(location.hash||''))return;
  if(k==='prefs')return;
  if(st.tab==='cards'&&k==='words')st.queue=null;
  var y=window.scrollY;B1.route();window.scrollTo(0,y);
});
})();
