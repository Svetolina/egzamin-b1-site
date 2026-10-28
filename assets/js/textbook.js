/* Учебник: список тем (#/learn/grammar) и страница темы.
   #/topic/<id>            — теория (?s=t4 — сразу к разделу)
   #/topic/<id>/ex         — список упражнений
   #/topic/<id>/ex/<eid>   — одно упражнение (?i=3 — к пункту)
   Тема берётся из textbook-src/<id>/topic.json и extract.json (источники);
   список тем и счётчики — из textbook-src/index.js (собирается tools/build_textbook_index.py).
   В режиме проверки (B1.review) добавляются «ок» по разделам и упражнениям, замечания и счётчики. */
(function(){
'use strict';
var B1=window.B1,el=B1.util.el,S=B1.store,UI=B1.ui;
var app=document.getElementById('app');
function A(){return B1.app;}
function R(){return B1.review;}
function rv(){return !!(R()&&R().on());}
function idx(){return window.B1_TEXTBOOK||[];}
function meta(id){return idx().filter(function(t){return t.id===id;})[0]||null;}
var LV={1:'Узнать',2:'Образовать',3:'Применить',4:'Свой текст'};

/* ---------- загрузка темы ---------- */
var cache={};
function getJSON(u){return fetch(u+'?v='+(B1.ASSET_VER||'1'),{cache:'no-cache'}).then(function(r){if(!r.ok)throw new Error(u+': HTTP '+r.status);return r.json();});}
function loadTopic(id){
  if(cache[id])return Promise.resolve(cache[id]);
  var base='textbook-src/'+encodeURIComponent(id)+'/';
  return getJSON(base+'topic.json').then(function(t){
    return getJSON(base+(t.facts_file||'extract.json')).catch(function(){return {facts:[],sources:{}};}).then(function(x){
      var facts={};(x.facts||[]).forEach(function(f){facts[f.id]=f;});
      var d={id:id,topic:t,facts:facts,sources:x.sources||{}};
      cache[id]=d;return d;
    });
  });
}

/* ---------- разметка текста: [[…]] — польский, **…** — выделение ---------- */
function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c];});}
function rich(s){return esc(s).replace(/\[\[(.+?)\]\]/g,'<span class="pl">$1</span>').replace(/\*\*(.+?)\*\*/g,'<span class="hl">$1</span>');}
function linkify(s){return esc(s).replace(/(https?:\/\/[^\s;)]+)/g,'<a href="$1" target="_blank" rel="noopener">$1</a>');}
function html(tag,cls,h){var e=el(tag,cls);e.innerHTML=h;return e;}
function block(b){
  switch(b.type){
    case 'p':return html('p','tb-p',rich(b.text));
    case 'note':
      if(b.kind==='mark'){var n=html('div','tb-note mark',rich(b.text));n.prepend(el('b',null,'С пометкой'));return n;}
      return html('div','tb-note',rich(b.text));
    case 'chips':{var c=el('div','tb-chips');(b.items||[]).forEach(function(i){c.append(html('span','pl',rich(i)));});return c;}
    case 'ex':{var x=el('div','tb-ex');(b.items||[]).forEach(function(i){var r=el('div');r.append(el('div','pl',i.pl),el('div','ru',i.ru||''));x.append(r);});return x;}
    case 'fix':{var f=el('div','tb-fix');(b.items||[]).forEach(function(i){f.append(el('span','bad pl',i.bad),el('span','arr','→'),el('span','good pl',i.good));});f.querySelectorAll('.arr').forEach(function(a){a.setAttribute('aria-hidden','true');});return f;}
    case 'steps':{var o=el('ol','tb-steps');(b.items||[]).forEach(function(i){o.append(html('li',null,rich(i)));});return o;}
    case 'table':{
      var pc=b.pl_cols||[],head=b.head||[];
      var w=el('div','tb-tw'),t=el('table','tb-t');
      if(head.some(function(h){return h;})){var th=el('thead'),tr=el('tr');head.forEach(function(h){tr.append(html('th',null,rich(h)));});th.append(tr);t.append(th);}
      var tb=el('tbody');
      (b.rows||[]).forEach(function(r){
        var tr=el('tr');
        r.forEach(function(c,i){
          var lab=i===0&&head[0]==='',pl=pc.indexOf(i)>-1;
          var td=el('td',(lab?'lab':'')+(pl?' pl':''));
          if(pl)td.textContent=String(c).replace(/\[\[|\]\]/g,'');else td.innerHTML=rich(c);
          tr.append(td);
        });
        tb.append(tr);
      });
      t.append(tb);w.append(t);return w;
    }
  }
  return el('div');
}
function sourcesBox(d,ids){
  var out=[],used={},abbr=Object.keys(d.sources||{});
  (ids||[]).forEach(function(id){
    var refs=id==='EXAM'?((d.topic.exam_ref||{}).refs||[]):((d.facts[id]||{}).refs||[]);
    refs.forEach(function(r){out.push(r);abbr.forEach(function(a){if(new RegExp('(^|[^A-ZŁ])'+a+'([^A-ZŁ]|$)').test(r))used[a]=1;});});
  });
  var det=el('details','tb-src');
  det.append(el('summary',null,'Источники · '+out.length));
  var ul=el('ul');
  out.forEach(function(r){ul.append(html('li',null,linkify(r)));});
  Object.keys(used).forEach(function(a){ul.append(html('li','leg','<b>'+esc(a)+'</b> — '+linkify(d.sources[a])));});
  det.append(ul);return det;
}

/* ---------- общие кусочки ---------- */
function secNum(d,sid){var i=-1;d.topic.theory.forEach(function(s,k){if(s.id===sid)i=k;});return i+1;}
function secById(d,sid){return d.topic.theory.filter(function(s){return s.id===sid;})[0]||null;}
function exById(d,eid){return (d.topic.exercises||[]).filter(function(e){return e.id===eid;})[0]||null;}
/* какие упражнения опираются на раздел теории */
function exForSec(d,sid){
  return (d.topic.exercises||[]).filter(function(e){
    return e.t===sid||(e.items||[]).some(function(i){return String(i.t||'').split(/[,\s]+/).indexOf(sid)>-1;});
  }).map(function(e){return e.id;});
}
function tvals(it){return String(it.t||'').split(/[,\s]+/).filter(Boolean);}
function okBtn(markId,label,onChange){
  var on=S.marks.isOk(markId);
  var b=UI.btn('tb-ok'+(on?' on':''),null,function(){
    var v=S.marks.toggle(markId,{topic:markId.split('/')[0].replace(/^tb:/,'')});
    b.classList.toggle('on',v);b.setAttribute('aria-pressed',String(v));
    b.lastChild.textContent=v?'ок':'Отметить';
    if(onChange)onChange(v);
  });
  b.setAttribute('aria-pressed',String(on));
  b.setAttribute('aria-label',(on?'Проверено: ':'Отметить проверенным: ')+label);
  b.append(UI.icon('check',18),document.createTextNode(on?'ок':'Отметить'));
  return b;
}
function reviewBtn(prefill,small){
  var b=UI.btn('tb-cm'+(small?' sm':''),null,function(){R().form({prefill:prefill()});});
  b.append(UI.icon('note',18));
  if(!small)b.append(document.createTextNode('Замечание'));
  else b.setAttribute('aria-label','Замечание');
  return b;
}

/* ---------- «Вернуться» после перехода ---------- */
var back=null,backEl=null;
function setBack(b){back=b;showBack();}
function showBack(){
  if(!backEl){
    backEl=UI.btn('tb-back',null,function(){
      var b=back;back=null;showBack();if(!b)return;
      if(b.hash&&b.hash!==location.hash){pendingY=b.y;location.hash=b.hash;}
      else window.scrollTo({top:b.y||0,behavior:'smooth'});
    });
    document.body.append(backEl);
  }
  backEl.hidden=!back;
  backEl.replaceChildren(UI.icon('back',20),document.createTextNode(back?back.label||'Вернуться':''));
}
var pendingY=null;

/* ---------- список тем ---------- */
function topicStats(t){
  var id=t.id,secs=t.theory.length,exs=t.exercises.length;
  var okS=t.theory.filter(function(s){return S.marks.isOk('tb:'+id+'/'+s.id);}).length;
  var okE=t.exercises.filter(function(e){return S.marks.isOk('tb:'+id+'/'+e.id);}).length;
  var open=R()?R().openCount(id):0;
  return {secs:secs,exs:exs,okS:okS,okE:okE,open:open,done:secs+exs>0&&okS===secs&&okE===exs};
}
function listPage(){
  A().title('Грамматика');A().setActive('learn');A().wide(false);
  var bar=null;
  if(B1.review&&B1.review.reviewer())bar=R().toggle(function(){B1.route();});
  A().tophead('#/','Грамматика','Правила с таблицами и упражнениями · '+idx().length+' '+A().plural(idx().length,'тема','темы','тем'),bar);
  if(!idx().length){var c=el('div','card');c.append(el('p',null,'Список тем не загрузился. Обновите страницу.'));app.append(c);return;}
  if(rv()){
    var all=idx().map(topicStats),done=all.filter(function(s){return s.done;}).length;
    var sum=el('div','tb-rvsum');
    sum.append(el('span',null,'Проверено тем: '+done+' из '+all.length));
    var cl=A().link('#/dict/comments','btn2 small','Замечания');sum.append(cl);
    sum.append(A().link('#/review/export','btn2 small primary','Для разбора'));
    app.append(sum);
  }
  var groups=[];
  idx().forEach(function(t){var g=groups.filter(function(x){return x.name===t.group;})[0];if(!g){g={name:t.group,items:[]};groups.push(g);}g.items.push(t);});
  groups.forEach(function(g){
    var s=A().section(g.name);
    var list=el('div','tb-list');
    g.items.forEach(function(t){
      var a=A().link('#/topic/'+t.id,'tb-row');
      var l=el('span','tb-row-l');
      l.append(el('span','tb-row-t pl',t.title_pl),el('span','tb-row-s',t.title_ru));
      var r=el('span','tb-row-r');
      if(t.level&&t.level!=='B1')r.append(el('span','lvl-b',t.level));
      if(rv()){
        var st=topicStats(t);
        var p=el('span','tb-prog'+(st.done?' done':''),'✓ '+(st.okS+st.okE)+'/'+(st.secs+st.exs));
        r.append(p);
        if(st.open)r.append(el('span','tb-open',String(st.open)));
        if(!st.exs)r.append(el('span','tb-warn','нет упражнений'));
      }else r.append(el('span','tb-row-n',t.theory.length+' · '+t.exercises.length));
      a.append(l,r);list.append(a);
    });
    s.append(list);
  });
  if(!rv())app.append(el('p','fhint','Числа справа: разделов теории · упражнений.'));
}

/* ---------- страница темы ---------- */
var routeN=0;
function topicPage(parts,query){
  var id=parts[1],tab=parts[2]==='ex'?'ex':'theory',eid=parts[3]||null;
  var my=++routeN;
  var m=meta(id);
  A().title(m?m.title_pl:'Тема');A().setActive('learn');A().wide(false);
  if(back&&back.topic!==id){back=null;showBack();}
  var wait=el('p','fhint','Загружаю тему…');app.append(wait);
  loadTopic(id).then(function(d){
    if(my!==routeN)return;
    wait.remove();
    if(tab==='ex'&&eid)exercisePage(d,eid,query);
    else render(d,tab,query);
    if(pendingY!=null){var y=pendingY;pendingY=null;setTimeout(function(){window.scrollTo(0,y);},30);}
    UI.renderComments();
    if(B1.updateSticky)B1.updateSticky();
  }).catch(function(e){
    if(my!==routeN)return;
    wait.textContent='Тема не загрузилась: '+e.message;
    if(B1.log)B1.log('error','Тема '+id+': '+e.message);
  });
}
function header(d,tab){
  var t=d.topic;
  var top=el('div','tb-top');
  var bk=A().link('#/learn/grammar','icbtn back');bk.setAttribute('aria-label','К списку тем');bk.append(UI.icon('back',22));
  top.append(bk,el('span','tb-crumb','Грамматика · '+(t.group||'')));
  if(R()&&R().reviewer())top.append(R().toggle(function(){B1.route();}));
  app.append(top);
  var h=el('header','tb-head');
  h.append(el('h1','pl',t.title_pl));
  var sub=el('p','sub',t.title_ru+(t.level?' · '+t.level:''));h.append(sub);
  if(tab==='theory'&&t.lead)h.append(html('p','lead',rich(t.lead)));
  app.append(h);
  if(rv()&&t.stage)app.append(el('p','tb-draft','Черновик: '+t.stage));
  var tabs=el('nav','tb-tabs');tabs.setAttribute('aria-label','Части темы');
  var nT=t.theory.length,nE=(t.exercises||[]).length;
  [['theory','Теория · '+nT,'#/topic/'+d.id],['ex','Упражнения · '+nE,'#/topic/'+d.id+'/ex']].forEach(function(x){
    var a=A().link(x[2],'tb-tab',x[1]);if(x[0]===tab)a.setAttribute('aria-current','page');tabs.append(a);
  });
  app.append(tabs);
  /* закреплённая полоска: оглавление и счётчик замечаний */
  var bar=el('div','tb-bar');
  var tb=UI.btn('tb-toc',null,function(){toc(d,tab);});
  tb.append(UI.icon('dots',18),el('span',null,'Оглавление'));
  if(rv()){
    var done=tab==='theory'?t.theory.filter(function(s){return S.marks.isOk('tb:'+d.id+'/'+s.id);}).length:(t.exercises||[]).filter(function(e){return S.marks.isOk('tb:'+d.id+'/'+e.id);}).length;
    tb.append(el('span','tb-prog'+(done===(tab==='theory'?nT:nE)&&done?' done':''),'✓ '+done+' из '+(tab==='theory'?nT:nE)));
  }
  bar.append(tb);
  if(rv()){
    var n=R().openCount(d.id);
    var cl=A().link('#/dict/comments?topic='+encodeURIComponent(d.id),'tb-cnt');
    cl.setAttribute('aria-label','Замечания по теме: открыто '+n);
    cl.append(UI.icon('note',18),el('span',null,String(n)));
    bar.append(cl);
  }
  app.append(bar);
}
function render(d,tab,query){
  header(d,tab);
  if(tab==='ex')return exList(d);
  var t=d.topic;
  t.theory.forEach(function(sec,i){
    var s=el('section','card tb-sec'+(rv()&&S.marks.isOk('tb:'+d.id+'/'+sec.id)?' ok':''));
    s.id='s-'+sec.id;s.dataset.cscope='tb:'+d.id+'/'+sec.id;
    var hd=el('div','tb-sec-h');
    var ht=el('div');ht.append(el('span','tb-num','Раздел '+(i+1)),html('h2',null,rich(sec.title)));
    hd.append(ht);
    if(rv())hd.append(okBtn('tb:'+d.id+'/'+sec.id,sec.title,function(v){s.classList.toggle('ok',v);}));
    s.append(hd);
    sec.blocks.forEach(function(b){s.append(block(b));});
    s.append(sourcesBox(d,sec.facts));
    if(rv()){
      var row=el('div','tb-rv');
      row.append(reviewBtn(function(){return R().prefillFor('tb:'+d.id+'/'+sec.id,{type:'rule'});}));
      var ex=exForSec(d,sec.id);
      var info=el('span','tb-rv-ex');
      if(ex.length){info.append(document.createTextNode('В упражнениях: '));ex.forEach(function(e,k){if(k)info.append(document.createTextNode(', '));info.append(A().link('#/topic/'+d.id+'/ex/'+e,null,e));});}
      else info.textContent='В упражнениях не встречается';
      row.append(info);s.append(row);
    }
    app.append(s);
  });
  var ex=t.exercises||[];
  if(ex.length){
    var nx=A().link('#/topic/'+d.id+'/ex','btn2 primary tb-next','К упражнениям · '+ex.length);app.append(nx);
  }
  if(query.s){
    var target=document.getElementById('s-'+query.s);
    if(target){setTimeout(function(){target.scrollIntoView({block:'start'});target.classList.add('tb-hl');setTimeout(function(){target.classList.remove('tb-hl');},2200);},40);}
  }
}
function exState(d,e){
  if(S.marks.isOk('tb:'+d.id+'/'+e.id))return {t:'проверено',c:'ok'};
  var n=(e.items||[]).length;if(!n)return {t:'не начато',c:''};
  var a=answers(),k=0;for(var i=0;i<n;i++)if(a[d.id+'/'+e.id+'/'+(i+1)])k++;
  return k?{t:(rv()?'проверено ':'решено ')+k+' из '+n,c:'part'}:{t:'не начато',c:''};
}
function exList(d){
  var ex=d.topic.exercises||[];
  if(!ex.length){var c=el('div','card');c.append(el('p',null,'В этой теме пока нет упражнений.'));app.append(c);return;}
  var list=el('div','tb-exlist');
  ex.forEach(function(e){
    var a=A().link('#/topic/'+d.id+'/ex/'+e.id,'tb-exrow');
    a.append(el('span','tb-lvl',e.id+' · Ступень '+e.level+' · '+(LV[e.level]||'')+(e.format==='exam'?' · экзамен':'')));
    var tl=el('span','tb-exrow-t');tl.append(el('span',e.kind==='text'||e.kind==='write'?'pl':null,e.title));
    var st=exState(d,e);
    if(rv()||st.c)tl.append(el('span','tb-st '+st.c,st.t));
    a.append(tl);
    var n=(e.items||[]).length;
    var mtxt=e.kind==='write'?'письменное задание':n+' '+A().plural(n,'пункт','пункта','пунктов');
    if(rv()){var oc=R().openCount(d.id,e.id);if(oc)mtxt+=' · '+oc+' '+A().plural(oc,'замечание','замечания','замечаний');}
    a.append(el('span','tb-exrow-m',mtxt));
    list.append(a);
  });
  app.append(list);
}

/* ---------- оглавление ---------- */
function toc(d,tab){
  var t=d.topic,isT=tab==='theory';
  var sh=UI.sheet(isT?'Оглавление · теория':'Оглавление · упражнения');
  if(rv()){
    var arr=isT?t.theory:(t.exercises||[]);
    var done=arr.filter(function(x){return S.marks.isOk('tb:'+d.id+'/'+x.id);}).length;
    sh.body.append(el('p','fhint','Проверено '+done+' из '+arr.length+' · открытых замечаний: '+R().openCount(d.id)));
  }
  var list=el('div','tb-toclist');
  (isT?t.theory:(t.exercises||[])).forEach(function(x,i){
    var a=el('a','tb-tocrow');
    a.href=isT?'#/topic/'+d.id+'?s='+x.id:'#/topic/'+d.id+'/ex/'+x.id;
    if(rv()){var ok=S.marks.isOk('tb:'+d.id+'/'+x.id);var dot=el('span','tb-dot'+(ok?' on':''));if(ok)dot.append(UI.icon('check',14));a.append(dot);}
    a.append(el('span','tb-tocrow-t',isT?(i+1)+'. '+x.title.replace(/\[\[|\]\]/g,''):x.id+' · '+x.title));
    if(rv()){var n=R().openCount(d.id,x.id);if(n)a.append(el('span','tb-open',String(n)));}
    a.addEventListener('click',function(ev){
      sh.close();
      if(isT){
        ev.preventDefault();
        var target=document.getElementById('s-'+x.id);
        if(target){setBack({y:window.scrollY,label:'Вернуться',topic:d.id});target.scrollIntoView({block:'start'});}
        else{location.hash=a.getAttribute('href');}
      }
    });
    list.append(a);
  });
  sh.body.append(list);
}

/* ---------- ответы в упражнениях (хранятся только в этом браузере) ---------- */
var ANS='pl:tb-ans',ansMem=null;
function answers(){if(ansMem)return ansMem;try{ansMem=JSON.parse(localStorage.getItem(ANS)||'{}');}catch(e){ansMem={};}if(!ansMem||typeof ansMem!=='object')ansMem={};return ansMem;}
function saveAns(place,v){answers()[place]=v;try{localStorage.setItem(ANS,JSON.stringify(ansMem));}catch(e){}}
function dropAns(prefix){var a=answers();Object.keys(a).forEach(function(k){if(k.indexOf(prefix)===0)delete a[k];});try{localStorage.setItem(ANS,JSON.stringify(ansMem));}catch(e){}}
function norm(v){return String(v).trim().toLowerCase().replace(/[„”“"]/g,'').replace(/\s+/g,' ').replace(/[.!?,;:]+$/,'');}
function plain(v){return norm(v).normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/ł/g,'l');}

/* ---------- шторка с правилом ---------- */
function ruleSheet(d,sid,from){
  var sec=secById(d,sid);if(!sec)return;
  var n=secNum(d,sid);
  var sh=UI.sheet('Раздел '+n+' · '+sec.title.replace(/\[\[|\]\]/g,''));
  var box=el('div','tb-sheetsec');box.dataset.cscope='tb:'+d.id+'/'+sid;
  sec.blocks.forEach(function(b){box.append(block(b));});
  sh.body.append(box);
  var row=el('div','tb-sheet-a');
  if(rv())row.append(reviewBtn(function(){return R().prefillFor('tb:'+d.id+'/'+sid,{type:'rule'});}));
  var go=UI.btn('btn2 primary','Открыть в теории',function(){
    sh.close();
    setBack({hash:'#/topic/'+d.id+'/ex/'+from.eid+'?i='+from.n,label:'Вернуться к заданию '+from.n,topic:d.id});
    location.hash='#/topic/'+d.id+'?s='+sid;
  });
  row.append(go);sh.body.append(row);
}

/* ---------- одно упражнение ---------- */
function exercisePage(d,eid,query){
  var t=d.topic,e=exById(d,eid),all=t.exercises||[];
  if(!e){header(d,'ex');app.append(el('p','fhint','Нет такого упражнения: '+eid));return;}
  A().title(e.title+' · '+t.title_pl);
  var top=el('div','tb-top');
  var bk=A().link('#/topic/'+d.id+'/ex','icbtn back');bk.setAttribute('aria-label','К упражнениям темы');bk.append(UI.icon('back',22));
  top.append(bk,el('span','tb-crumb',t.title_pl+' › Упражнения'));
  if(R()&&R().reviewer())top.append(R().toggle(function(){B1.route();}));
  app.append(top);
  var card=el('section','card tb-excard');card.dataset.cscope='tb:'+d.id+'/'+e.id;
  var hd=el('div','tb-sec-h');
  var ht=el('div');ht.append(el('span','tb-lvl',e.id+' · Ступень '+e.level+' · '+(LV[e.level]||'')+(e.format==='exam'?' · формат экзамена':'')));
  ht.append(el('h2',e.kind==='text'||e.kind==='write'?'pl':null,e.title));
  hd.append(ht);
  if(rv())hd.append(okBtn('tb:'+d.id+'/'+e.id,e.title));
  card.append(hd);
  if(e.instr)card.append(html('p','tb-instr',rich(e.instr)));
  var place0=d.id+'/'+e.id+'/';
  if(e.kind==='write'){writeTask(d,e,card);}
  else{
    if(e.kind==='text'&&e.passage){
      var ps=el('div','tb-passage pl');
      ps.innerHTML=esc(e.passage).replace(/\{(\d+)\}/g,'<span class="tb-gap">($1)&nbsp;____</span>');
      card.append(ps);
    }
    var score=el('p','score');
    var items=e.items||[];
    items.forEach(function(it,i){card.append(itemEl(d,e,it,i+1,score));});
    card.append(score);updScore();
    var reset=UI.btn('btn2 small tb-reset','Начать заново',function(){dropAns(place0);B1.route();});
    card.append(reset);
    function updScore(){var a=answers(),k=0,ok=0;items.forEach(function(x,i){var v=a[place0+(i+1)];if(v){k++;if(v.ok)ok++;}});score.textContent=k?'Отвечено '+k+' из '+items.length+', верно '+ok+'.':'';}
    card.addEventListener('b1:ans',updScore);
  }
  if(rv()){
    var rr=el('div','tb-rv');
    rr.append(reviewBtn(function(){return R().prefillFor('tb:'+d.id+'/'+e.id,{type:'task'});}));
    rr.append(el('span','tb-rv-ex','Замечание ко всему упражнению'));
    card.append(rr);
  }
  app.append(card);
  /* соседние упражнения */
  var k=all.indexOf(e),nav=el('nav','tb-pn');nav.setAttribute('aria-label','Другие упражнения');
  if(k>0)nav.append(A().link('#/topic/'+d.id+'/ex/'+all[k-1].id,'btn2','← '+all[k-1].id));else nav.append(el('span'));
  if(k<all.length-1)nav.append(A().link('#/topic/'+d.id+'/ex/'+all[k+1].id,'btn2 primary',all[k+1].id+' →'));
  else nav.append(A().link('#/topic/'+d.id,'btn2','К теории'));
  app.append(nav);
  if(query.i){var tg=document.getElementById('it-'+e.id+'-'+query.i);if(tg)setTimeout(function(){tg.scrollIntoView({block:'center'});tg.classList.add('tb-hl');setTimeout(function(){tg.classList.remove('tb-hl');},2200);},40);}
}
function itemEl(d,e,it,n,score){
  var place=d.id+'/'+e.id+'/'+n;
  var w=el('div','tb-it');w.id='it-'+e.id+'-'+n;w.dataset.cscope='tb:'+place;
  var q=el('div','q');
  if(e.kind==='text')q.innerHTML='<b>('+n+')</b> '+esc(it.q);
  else q.innerHTML=n+'. '+esc(it.q).replace(/\*\*(.+?)\*\*/g,'<span class="bold">$1</span>');
  w.append(q);
  var fb=el('div','tb-fb');fb.hidden=true;fb.setAttribute('role','status');
  var prev=answers()[place];
  var a=it.a||[];
  function check(v){
    var vv=norm(v);if(!vv)return;
    var ok=a.some(function(x){return norm(x)===vv;});
    var dia=!ok&&a.some(function(x){return plain(x)===plain(v);});
    show(ok,dia,v);
    if(!dia){
      saveAns(place,{v:v,ok:ok,at:new Date().toISOString()});
      if(B1.log)B1.log('ans',ok?'верно':'неверно: '+v,{place:place,ok:ok,val:v});
      w.closest('.tb-excard').dispatchEvent(new Event('b1:ans'));
    }
    return ok;
  }
  function show(ok,dia,v){
    fb.className='tb-fb '+(ok?'ok':dia?'dia':'no');
    var more=a.length>1?' Подходят: '+a.join(', ')+'.':'';
    fb.replaceChildren();
    if(ok)fb.append(document.createTextNode('Верно. '+(it.expl||'')+more));
    else if(dia)fb.append(document.createTextNode('Почти: проверьте диакритику (ą, ę, ł, ś, ź, ż…).'));
    else{fb.append(document.createTextNode('Нет. Правильно: '),el('b','pl',a[0]||''),document.createTextNode('. '+(it.expl||'')+more));}
    fb.hidden=false;
  }
  if(e.kind==='choice'){
    var row=el('div','tb-opts');
    (it.opts||[]).forEach(function(o){
      var b=UI.btn('tb-opt pl',o,function(){
        row.querySelectorAll('.tb-opt').forEach(function(x){x.classList.remove('ok','no');});
        var ok=check(o);b.classList.add(ok?'ok':'no');
      });
      if(prev&&prev.v===o)b.classList.add(prev.ok?'ok':'no');
      row.append(b);
    });
    w.append(row);
  }else{
    var f=el('form','tb-in');
    var inp=el('input');inp.type='text';inp.lang='pl';inp.autocomplete='off';inp.spellcheck=false;
    inp.setAttribute('autocapitalize','off');inp.setAttribute('autocorrect','off');inp.setAttribute('aria-label','Ответ на пункт '+n);
    if(prev){inp.value=prev.v;inp.classList.add(prev.ok?'ok':'no');}
    var sb=el('button','btn','Проверить');sb.type='submit';
    f.append(inp,sb);
    f.addEventListener('submit',function(ev){ev.preventDefault();inp.classList.remove('ok','no');var ok=check(inp.value);if(ok!==undefined&&!fb.classList.contains('dia'))inp.classList.add(ok?'ok':'no');});
    inp.addEventListener('input',function(){inp.classList.remove('ok','no');});
    w.append(f);
  }
  w.append(fb);
  if(prev)show(prev.ok,false,prev.v);
  /* правило и замечание */
  var acts=el('div','tb-it-a');
  tvals(it).forEach(function(sid){
    var sec=secById(d,sid);if(!sec)return;
    var b=UI.btn('tb-rule',null,function(){ruleSheet(d,sid,{eid:e.id,n:n});});
    b.append(UI.icon('book',16),el('span','tb-rule-n','§'+secNum(d,sid)),el('span','tb-rule-t',sec.title.replace(/\[\[|\]\]/g,'')));
    acts.append(b);
  });
  if(rv()){
    acts.append(reviewBtn(function(){
      var p=answers()[place];
      return R().prefillFor('tb:'+place,{type:'key',quote:it.q,key:a.join(' / '),mine:p&&!p.ok?p.v:''});
    },true));
  }
  w.append(acts);
  return w;
}
function writeTask(d,e,card){
  var place=d.id+'/'+e.id+'/text';
  if(e.need)card.append(el('p','tb-need',e.need+(e.words?' Объём: '+e.words[0]+'–'+e.words[1]+' слов.':'')));
  var ta=el('textarea','pl tb-write');ta.lang='pl';ta.spellcheck=false;ta.rows=7;ta.setAttribute('aria-label','Ваш текст');
  var prev=answers()[place];if(prev)ta.value=prev.v||'';
  var wc=el('p','score');
  function count(){
    var n=(ta.value.match(/[A-Za-zĄĆĘŁŃÓŚŹŻąćęłńóśźż]+/g)||[]).length;
    wc.textContent=n+' слов'+(e.words?(n<e.words[0]?' · мало':n>e.words[1]?' · много':' · в норме'):'');
  }
  var T=null;
  ta.addEventListener('input',function(){count();clearTimeout(T);T=setTimeout(function(){saveAns(place,{v:ta.value,ok:true});},500);});
  count();
  card.append(ta,wc);
  var m=el('div','tb-model');m.hidden=true;
  if(e.model)m.append(el('div','tb-modeltext pl',e.model));
  if(e.model_future&&e.model_future.length){var p=el('p','fhint');p.append(document.createTextNode('Нужные формы в образце: '),el('span','pl',e.model_future.join(', ')));m.append(p);}
  if(e.checklist){
    var ul=el('ul','tb-check');
    e.checklist.forEach(function(c,i){var li=el('li'),lab=el('label'),cb=el('input');cb.type='checkbox';lab.append(cb,el('span',null,c));li.append(lab);ul.append(li);});
    m.append(ul);
  }
  var sb=UI.btn('btn2','Показать образец и чек-лист',function(){m.hidden=!m.hidden;sb.textContent=m.hidden?'Показать образец и чек-лист':'Скрыть образец';});
  card.append(sb,m);
}

/* новое или изменённое замечание — обновить счётчики на странице темы, не сбивая прокрутку */
S.onChange(function(k){
  if(k!=='comments'||!/^#\/(topic|learn\/grammar)/.test(location.hash||''))return;
  setTimeout(function(){
    if(document.body.classList.contains('sheet-open'))return;
    pendingY=window.scrollY;B1.route();
  },0);
});
B1.textbook={listPage:listPage,topicPage:topicPage,meta:meta,index:idx,loadTopic:loadTopic,answers:answers,secNum:secNum};
})();
