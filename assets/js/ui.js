/* Общие элементы интерфейса: шторки снизу, всплывающие уведомления, полоска выделения,
   формы «слово» и «комментарий», показ комментариев в тексте, кнопка «+»
   и правила экзаменационного режима (таймер идёт — ничего не выделяется и не добавляется). */
(function(){
'use strict';
var B1=window.B1,S=B1.store,el=B1.util.el;
var app=document.getElementById('app');

/* ---------- иконки ---------- */
var IC={
  close:'<path d="M6 6l12 12M18 6L6 18"/>',
  plus:'<path d="M12 5v14M5 12h14"/>',
  dots:'<circle cx="5" cy="12" r="1.6"/><circle cx="12" cy="12" r="1.6"/><circle cx="19" cy="12" r="1.6"/>',
  note:'<path d="M5 5h14v10H9l-4 4z"/>',
  book:'<path d="M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z"/><path d="M5 17a3 3 0 0 1 3-3h11"/>',
  check:'<path d="M5 12.5l4.5 4.5L19 7.5"/>',
  back:'<path d="M15 5l-7 7 7 7"/>',
  search:'<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4 4"/>'
};
function icon(name,size){
  var s=size||22;
  var span=document.createElement('span');span.className='ic';span.setAttribute('aria-hidden','true');
  span.innerHTML='<svg width="'+s+'" height="'+s+'" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">'+IC[name]+'</svg>';
  return span;
}
function btn(cls,text,onClick){var b=el('button',cls,text);b.type='button';if(onClick)b.addEventListener('click',onClick);return b;}

/* ---------- даты ---------- */
var MON=['янв','фев','мар','апр','мая','июн','июл','авг','сен','окт','ноя','дек'];
function shortDate(iso){var d=new Date(iso);return isNaN(d)?'':d.getDate()+' '+MON[d.getMonth()];}

/* ---------- экзаменационный режим ---------- */
var exam='idle'; /* idle | run | pause | over */
function examRunning(){return exam==='run';}
document.addEventListener('b1:exam',function(e){
  exam=e.detail||'idle';
  document.body.classList.toggle('exam-run',exam==='run');
  document.body.classList.toggle('exam-pause',exam==='pause');
  if(exam==='run'){
    try{var s=window.getSelection();if(s)s.removeAllRanges();}catch(er){}
    hideBar();closeFab();
  }
  renderComments();
});

/* ---------- уведомление снизу ---------- */
var toastEl=null,toastT=null;
function toast(text,undo){
  if(toastEl)toastEl.remove();clearTimeout(toastT);
  toastEl=el('div','toast');toastEl.setAttribute('role','status');
  toastEl.append(el('span',null,text));
  if(undo){toastEl.append(btn('toast-u','Отменить',function(){undo();hideToast();}));}
  document.body.append(toastEl);
  toastT=setTimeout(hideToast,6000);
}
function hideToast(){if(toastEl){toastEl.remove();toastEl=null;}}

/* ---------- шторка снизу ---------- */
var openSheet=null;
function sheet(title){
  if(openSheet)openSheet.close();
  var prevFocus=document.activeElement;
  var ov=el('div','sheet-ov');
  var sh=el('div','sheet');sh.setAttribute('role','dialog');sh.setAttribute('aria-modal','true');sh.setAttribute('aria-label',title);
  var grip=el('div','sheet-grip');grip.append(el('span'));
  var hd=el('div','sheet-h');var h=el('h2',null,title);
  var x=btn('icbtn',null,function(){api.close();});x.setAttribute('aria-label','Закрыть');x.append(icon('close'));
  hd.append(h,x);
  var body=el('div','sheet-b');
  sh.append(grip,hd,body);ov.append(sh);
  ov.addEventListener('click',function(e){if(e.target===ov)api.close();});
  function onKey(e){if(e.key==='Escape')api.close();}
  document.addEventListener('keydown',onKey);
  document.body.append(ov);document.body.classList.add('sheet-open');
  var api={el:sh,body:body,close:function(){
    ov.remove();document.removeEventListener('keydown',onKey);document.body.classList.remove('sheet-open');
    if(openSheet===api)openSheet=null;
    if(prevFocus&&prevFocus.focus&&document.body.contains(prevFocus))try{prevFocus.focus({preventScroll:true});}catch(e){}
  }};
  openSheet=api;
  setTimeout(function(){var f=sh.querySelector('textarea,input:not([type=checkbox])');(f||x).focus({preventScroll:true});},30);
  return api;
}
function field(label,id,value,o){
  o=o||{};
  var w=el('div','fld2');
  var l=el('label',null,label);l.htmlFor=id;
  var c=o.area?el('textarea'):el('input');c.id=id;
  if(!o.area)c.type='text';
  c.value=value||'';c.autocomplete='off';c.spellcheck=false;c.setAttribute('autocorrect','off');c.setAttribute('autocapitalize','none');
  if(o.pl)c.classList.add('pl');
  if(o.placeholder)c.placeholder=o.placeholder;
  w.append(l,c);
  var hint=o.hint?el('p','fhint',o.hint):null;if(hint)w.append(hint);
  var err=el('p','ferr');err.hidden=true;w.append(err);
  return {wrap:w,ctrl:c,err:function(t){err.textContent=t||'';err.hidden=!t;c.classList.toggle('bad',!!t);if(t)c.setAttribute('aria-invalid','true');else c.removeAttribute('aria-invalid');}};
}
function chips(label,names,cur,onPick){
  var w=el('div','fld2');w.append(el('span','flabel',label));
  var row=el('div','chiprow');row.setAttribute('role','group');row.setAttribute('aria-label',label);
  names.forEach(function(n){
    var b=btn('chip2'+(n===cur?' on':''),n,function(){
      row.querySelectorAll('.chip2').forEach(function(x){x.classList.remove('on');x.setAttribute('aria-pressed','false');});
      b.classList.add('on');b.setAttribute('aria-pressed','true');onPick(n);
    });
    b.setAttribute('aria-pressed',String(n===cur));row.append(b);
  });
  w.append(row);return {wrap:w,row:row};
}

/* ---------- подписи источника ---------- */
function pageKey(){return (location.hash||'#/').replace(/^#\/?/,'').replace(/\/$/,'')||'home';}
function labelFor(scopeEl){
  if(B1.app&&B1.app.labelFor)return B1.app.labelFor(scopeEl);
  return {src:(document.title||'').split(' | ')[0],href:location.hash||'#/'};
}

/* ---------- форма слова ---------- */
var DEF_TOPICS=['Семья','Работа','Город','Здоровье','Общение'];
function wordForm(o){
  o=o||{};
  var w=o.word||null,pre=o.prefill||{};
  var sh=sheet(w?'Изменить слово':'Новое слово');
  var b=sh.body;
  var dup=el('div','warn');dup.hidden=true;b.append(dup);
  var fPl=field('По-польски','wf-pl',w?w.pl:pre.pl,{pl:true});
  var fForms=field('Формы','wf-forms',w?w.forms:'',{pl:true,hint:'Впишите сами, например: odzywam się, odzywasz się'});
  var fTr=field('Перевод','wf-tr',w?w.tr:'',{hint:'Тоже печатаете сами: так слово запоминается лучше'});
  var fEx=field(pre.ex&&!w?'Пример из текста':'Пример','wf-ex',w?w.ex:pre.ex,{area:true,pl:true,placeholder:'Необязательно'});
  fEx.ctrl.rows=2;
  b.append(fPl.wrap,fForms.wrap,fTr.wrap,fEx.wrap);
  var topics=DEF_TOPICS.slice();
  S.words.all().forEach(function(x){if(x.topic&&topics.indexOf(x.topic)<0)topics.push(x.topic);});
  var topic=w?(w.topic||'Без темы'):'Без темы';
  if(topic!=='Без темы'&&topics.indexOf(topic)<0)topics.push(topic);
  var tp=chips('Тема',['Без темы'].concat(topics).concat(['Своя…']),topic,function(n){
    if(n==='Своя…'){own.hidden=false;own.querySelector('input').focus();topic='';}
    else{own.hidden=true;topic=n;}
  });
  var own=el('div','fld2');own.hidden=true;
  var ownIn=el('input');ownIn.type='text';ownIn.placeholder='Название темы';ownIn.setAttribute('aria-label','Своя тема');
  ownIn.addEventListener('input',function(){topic=ownIn.value.trim();});
  own.append(ownIn);
  b.append(tp.wrap,own);
  var two=el('label','chk');var cb=el('input');cb.type='checkbox';cb.checked=w?!!w.twoWay:true;
  two.append(cb,el('span',null,'Карточка в обе стороны: польский → перевод и обратно'));
  b.append(two);
  var src=w?w.src:pre.src;
  if(src)b.append(el('p','fhint','Источник: '+src));
  function checkDup(){
    var same=S.words.findSame(fPl.ctrl.value,w&&w.id);
    dup.replaceChildren();dup.hidden=!same;
    if(same){dup.append(el('span',null,'Слово «'+same.pl+'» уже есть в словаре. '));var a=el('a',null,'Открыть');a.href='#/dict/words?w='+encodeURIComponent(same.id);a.addEventListener('click',function(){sh.close();});dup.append(a);}
  }
  fPl.ctrl.addEventListener('input',function(){fPl.err('');checkDup();});
  fTr.ctrl.addEventListener('input',function(){fTr.err('');});
  checkDup();
  var save=btn('btn2 primary',w?'Сохранить изменения':'Добавить в словарь',function(){
    var pl=fPl.ctrl.value.trim(),tr=fTr.ctrl.value.trim(),bad=false;
    if(!pl){fPl.err('Впишите слово или фразу.');bad=true;}
    if(!tr){fTr.err('Впишите перевод. Так слово запоминается лучше.');bad=true;}
    if(bad){(pl?fTr:fPl).ctrl.focus();return;}
    var data={pl:pl,forms:fForms.ctrl.value.trim(),tr:tr,ex:fEx.ctrl.value.trim(),topic:topic&&topic!=='Без темы'?topic:'',twoWay:cb.checked};
    if(w){S.words.update(w.id,data);sh.close();toast('Слово изменено');}
    else{
      data.src=pre.src||'';data.srcHref=pre.href||'';
      var nw=S.words.add(data);sh.close();
      toast('Добавлено: '+pl,function(){S.words.remove(nw.id);});
    }
    if(o.onDone)o.onDone();
  });
  b.append(save);
  if(w){
    b.append(btn('btn2 danger','Удалить слово',function(){
      var rem=S.words.remove(w.id);sh.close();
      toast('Слово удалено',function(){S.words.restore(rem);});
      if(o.onDone)o.onDone();
    }));
  }
  return sh;
}

/* ---------- форма комментария ---------- */
var TAGS=['Вопрос','Запомнить','Ошибка в материале','Заметка'];
function commentForm(o){
  o=o||{};
  var c=o.comment||null,pre=o.prefill||{};
  var sh=sheet(c?'Изменить комментарий':(pre.tag==='Заметка'&&!pre.quote?'Новая заметка':'Новый комментарий'));
  var b=sh.body;
  var quote=c?c.quote:pre.quote;
  var src=c?c.src:pre.src;
  if(quote){
    var q=el('div','fld2');q.append(el('span','flabel','К фрагменту'));
    var qb=el('div','quote pl');qb.append(el('b',null,quote));q.append(qb);
    if(src)q.append(el('p','fhint',src));
    b.append(q);
  }else if(src){
    b.append(el('p','fhint',(pre.whole?'Ко всему заданию: ':'К странице: ')+src));
  }
  var f=field('Комментарий','cf-text',c?c.text:'',{area:true,placeholder:'Что хотите запомнить или спросить?'});
  f.ctrl.rows=4;b.append(f.wrap);
  var tag=c?c.tag:(pre.tag||'Вопрос');
  b.append(chips('Тип',TAGS,tag,function(n){tag=n;}).wrap);
  if(!c)b.append(el('p','fhint',quote?'Фрагмент будет подчёркнут в тексте, когда комментарии показаны. Все комментарии собраны в «Словарь › Комментарии».':'Комментарий появится в «Словарь › Комментарии».'));
  f.ctrl.addEventListener('input',function(){f.err('');});
  b.append(btn('btn2 primary',c?'Сохранить изменения':'Сохранить комментарий',function(){
    var text=f.ctrl.value.trim();
    if(!text){f.err('Напишите текст комментария.');f.ctrl.focus();return;}
    if(c){S.comments.update(c.id,{text:text,tag:tag,done:tag==='Заметка'?false:c.done});sh.close();toast('Комментарий изменён');}
    else{
      showComments=true;
      var nc=S.comments.add({scope:pre.scope,href:pre.href||'',src:pre.src||'',quote:pre.quote||'',occ:pre.occ||0,text:text,tag:tag,done:false});
      sh.close();
      toast('Комментарий сохранён',function(){S.comments.remove(nc.id);});
    }
    if(o.onDone)o.onDone();
  }));
  if(c){
    b.append(btn('btn2 danger','Удалить комментарий',function(){
      var rem=S.comments.remove(c.id);sh.close();
      toast('Комментарий удалён',function(){S.comments.restore(rem);});
      if(o.onDone)o.onDone();
    }));
  }
  return sh;
}

/* ---------- текст внутри области (без полей ввода и служебных блоков) ---------- */
var SKIP='input,select,textarea,button,option,.cnote,.ctoggle,.cbtn,script,style,audio,.fix';
function textNodes(root){
  var out=[];
  var tw=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,{acceptNode:function(n){
    var p=n.parentElement;if(!p||p.closest(SKIP))return NodeFilter.FILTER_REJECT;
    return NodeFilter.FILTER_ACCEPT;
  }});
  var n;while((n=tw.nextNode()))out.push(n);
  return out;
}
function offsetOf(root,node,off){
  if(node.nodeType!==3){
    var ch=node.childNodes[off];
    if(!ch){off=0;node=node.nextSibling||node;}
    else{var ts=textNodes(ch.nodeType===3?ch.parentNode:ch);node=ts[0]||ch;off=0;}
  }
  var nodes=textNodes(root),pos=0;
  for(var i=0;i<nodes.length;i++){if(nodes[i]===node)return pos+off;pos+=nodes[i].length;}
  return -1;
}
function positions(hay,needle){var out=[],i=hay.indexOf(needle);while(i>-1&&needle){out.push(i);i=hay.indexOf(needle,i+1);}return out;}
var BLOCK='p,li,.q,.mrow,.qa,.rw,.lg,.task-h,.prompt,.adcard,blockquote,h1,h2,h3,figcaption,.box,.ex-row,.card';

/* ---------- полоска выделения ---------- */
var bar=null,barTxt=null,ctx=null,keepBar=false;
function buildBar(){
  bar=el('div','selbar');bar.hidden=true;bar.setAttribute('role','toolbar');bar.setAttribute('aria-label','Действия с выделенным');
  var l=el('div','selbar-l');l.append(el('span','selbar-k','Выделено:'));barTxt=el('span','selbar-t pl');l.append(barTxt);
  var bw=btn('selbar-b','В словарь',function(){var c=ctx;hideBar();clearSel();if(c)wordForm({prefill:{pl:c.text,ex:c.ex,src:c.src,href:c.href}});});
  var bc=btn('selbar-b','Комментарий',function(){var c=ctx;hideBar();clearSel();if(c)commentForm({prefill:{quote:c.text,scope:c.scope,occ:c.occ,src:c.src,href:c.href}});});
  [bw,bc].forEach(function(b){b.addEventListener('pointerdown',function(e){e.preventDefault();});b.addEventListener('mousedown',function(e){e.preventDefault();});});
  bar.append(l,bw,bc);
  document.body.append(bar);
}
function hideBar(){if(bar){bar.hidden=true;document.body.classList.remove('sel-on');}ctx=null;}
function clearSel(){try{var s=window.getSelection();if(s)s.removeAllRanges();}catch(e){}}
var selT=null;
document.addEventListener('selectionchange',function(){clearTimeout(selT);selT=setTimeout(onSel,140);});
function onSel(){
  if(!bar)buildBar();
  if(examRunning()||openSheet){hideBar();return;}
  var s=window.getSelection();
  if(!s||!s.rangeCount||s.isCollapsed){hideBar();return;}
  var text=s.toString().replace(/\s+/g,' ').trim();
  if(!text||text.length>300){hideBar();return;}
  var r=s.getRangeAt(0);
  var node=r.commonAncestorContainer;var e=node.nodeType===1?node:node.parentElement;
  if(!e||!app.contains(e)||e.closest('input,textarea,select,.sheet,.selbar,.cnote,.nav-b,.no-sel')){hideBar();return;}
  var scopeEl=e.closest('[data-cscope]');
  var root=scopeEl||app;
  var scope=scopeEl?scopeEl.dataset.cscope:'page:'+pageKey();
  var full=textNodes(root).map(function(n){return n.data;}).join('');
  var start=offsetOf(root,r.startContainer,r.startOffset);
  var raw=s.toString().trim();
  var ps=positions(full,raw),occ=0;
  if(ps.length&&start>-1){var best=0;ps.forEach(function(p,i){if(Math.abs(p-start)<Math.abs(ps[best]-start))best=i;});occ=best;}
  var blk=e.closest(BLOCK)||e;
  var sentence=(blk.textContent||'').replace(/\s+/g,' ').trim();
  var parts=(sentence.match(/[^.!?…]+[.!?…]*/g)||[]).map(function(x){return x.trim();});
  var ex=parts.filter(function(x){return x.indexOf(text)>-1;})[0]||'';
  if(ex.length>300)ex='';
  if(ex===text)ex='';
  var lab=labelFor(scopeEl);
  ctx={text:ps.length?raw:text,occ:occ,scope:scope,ex:ex,src:lab.src,href:lab.href};
  barTxt.textContent=text.length>40?text.slice(0,38)+'…':text;
  bar.hidden=false;document.body.classList.add('sel-on');
}

/* ---------- комментарии в тексте ---------- */
var showComments=false;
function unwrap(){
  app.querySelectorAll('.cnote,.ctoggle').forEach(function(n){n.remove();});
  app.querySelectorAll('mark.cmark').forEach(function(m){var p=m.parentNode;while(m.firstChild)p.insertBefore(m.firstChild,m);p.removeChild(m);p.normalize();});
}
function pageScopes(){
  var sc=['page:'+pageKey()];
  app.querySelectorAll('[data-cscope]').forEach(function(x){sc.push(x.dataset.cscope);});
  return sc;
}
function wrapRange(root,start,len,cid){
  var nodes=textNodes(root),pos=0,first=null;
  for(var i=0;i<nodes.length&&len>0;i++){
    var n=nodes[i],L=n.length;
    if(pos+L<=start){pos+=L;continue;}
    var a=Math.max(0,start-pos),bb=Math.min(L,a+len);
    var mid=n;if(a>0)mid=n.splitText(a);
    if(bb-a<mid.length)mid.splitText(bb-a);
    var m=el('mark','cmark');m.dataset.cid=cid;mid.parentNode.insertBefore(m,mid);m.append(mid);
    if(!first)first=m;
    len-=(bb-a);start+=(bb-a);pos+=L;
  }
  return first;
}
var TAGCLS={'Вопрос':'t-q','Запомнить':'t-r','Ошибка в материале':'t-e','Заметка':'t-n'};
function noteCard(c){
  var d=el('div','cnote'+(c.done?' done':''));
  var h=el('div','cnote-h');h.append(el('span','ctag '+(TAGCLS[c.tag]||''),c.tag));
  if(c.done)h.append(el('span','cdone','решено'));
  d.append(h);
  if(c.quote)d.append(el('p','cnote-q pl','«'+c.quote+'»'));
  d.append(el('p','cnote-t',c.text));
  var row=el('div','cnote-a');
  row.append(btn('lnk','Изменить',function(){commentForm({comment:c});}));
  row.append(btn('lnk danger','Удалить',function(){var rem=S.comments.remove(c.id);toast('Комментарий удалён',function(){S.comments.restore(rem);});}));
  d.append(row);
  return d;
}
function renderComments(){
  unwrap();
  if(document.body.classList.contains('no-comments'))return;
  var list=S.comments.forScopes(pageScopes());
  decorate();
  if(!list.length||examRunning())return;
  var tg=el('div','ctoggle');
  var tb=btn('ctog'+(showComments?' on':''),null,function(){showComments=!showComments;renderComments();});
  tb.setAttribute('aria-pressed',String(showComments));
  tb.append(icon('note',18),el('span',null,'Комментарии · '+list.length),el('span','ctog-s',showComments?'Скрыть':'Показать'));
  tg.append(tb);
  if(!showComments)tg.append(el('span','fhint','Скрыты. Выделите текст, чтобы добавить новый.'));
  var anchor=app.querySelector('.crumbs, .tophead');
  if(anchor&&anchor.parentNode===app)anchor.after(tg);else app.prepend(tg);
  if(!showComments)return;
  list.slice().reverse().forEach(function(c){
    var root=c.scope.indexOf('page:')===0?app:app.querySelector('[data-cscope="'+(window.CSS&&CSS.escape?CSS.escape(c.scope):c.scope)+'"]');
    if(!root)return;
    var card=noteCard(c);
    if(c.quote){
      var full=textNodes(root).map(function(n){return n.data;}).join('');
      var ps=positions(full,c.quote);
      if(ps.length){
        var m=wrapRange(root,ps[Math.min(c.occ||0,ps.length-1)],c.quote.length,c.id);
        var blk=m&&(m.closest(BLOCK)||m.parentElement);
        if(blk&&root.contains(blk)&&blk!==root){
          if(blk.matches('.task-h')){blk.after(card);}
          else{var nx=blk;while(nx.nextElementSibling&&nx.nextElementSibling.classList.contains('cnote'))nx=nx.nextElementSibling;nx.after(card);}
          return;
        }
      }
    }
    var head=root.querySelector(':scope > .task-h');
    if(head)head.after(card);else if(root===app)tg.after(card);else root.prepend(card);
  });
}
/* кнопка «комментарий ко всему заданию» в шапке каждого задания */
function decorate(){
  app.querySelectorAll('[data-cscope]').forEach(function(sec){
    var head=sec.querySelector(':scope > .task-h');if(!head||head.querySelector('.cbtn'))return;
    var b=btn('icbtn cbtn',null,function(){
      var lab=labelFor(sec);
      commentForm({prefill:{scope:sec.dataset.cscope,src:lab.src,href:lab.href,whole:true,tag:'Заметка'}});
    });
    b.setAttribute('aria-label','Комментарий ко всему заданию');b.title='Комментарий ко всему заданию';b.append(icon('note',20));
    head.append(b);
  });
}
S.onChange(function(k){if(k==='comments')renderComments();});

/* ---------- кнопка «+» ---------- */
var fab=null,fabMenu=null;
function buildFab(){
  fab=btn('fab',null,function(){fabMenu.hidden=!fabMenu.hidden;fab.setAttribute('aria-expanded',String(!fabMenu.hidden));});
  fab.setAttribute('aria-label','Добавить своё слово или заметку');fab.setAttribute('aria-expanded','false');fab.append(icon('plus',26));
  fabMenu=el('div','fab-m');fabMenu.hidden=true;
  fabMenu.append(btn('fab-i','Своё слово',function(){closeFab();var lab=labelFor(null);wordForm({prefill:{src:lab.src,href:lab.href}});}));
  fabMenu.append(btn('fab-i','Заметка',function(){closeFab();var lab=labelFor(null);commentForm({prefill:{scope:'page:'+pageKey(),src:lab.src,href:lab.href,tag:'Заметка'}});}));
  document.body.append(fabMenu,fab);
  document.addEventListener('click',function(e){if(!fabMenu.hidden&&!fabMenu.contains(e.target)&&!fab.contains(e.target))closeFab();});
}
function closeFab(){if(fabMenu){fabMenu.hidden=true;fab.setAttribute('aria-expanded','false');}}

/* вызывается приложением после каждой смены страницы */
function afterRoute(o){
  o=o||{};
  if(!fab)buildFab();
  closeFab();hideBar();hideToastIfStale();
  if(openSheet)openSheet.close();
  showComments=false;
  document.body.classList.toggle('no-fab',!!o.noFab);
  document.body.classList.toggle('no-comments',!!o.noComments);
  if(exam!=='idle'&&!app.querySelector('.timer')){document.dispatchEvent(new CustomEvent('b1:exam',{detail:'idle'}));}
  else renderComments();
}
function hideToastIfStale(){}

B1.ui={icon:icon,btn:btn,toast:toast,sheet:sheet,wordForm:wordForm,commentForm:commentForm,
  afterRoute:afterRoute,renderComments:renderComments,shortDate:shortDate,TAGS:TAGS,TAGCLS:TAGCLS,
  examRunning:examRunning};
})();
