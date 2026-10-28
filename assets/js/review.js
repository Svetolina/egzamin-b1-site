/* Режим проверки (первая версия суперадминки).
   #/admin          — вход, синхронизация, переключатель режима, журнал
   #/login          — вход по ссылке на почту
   #/review/export  — «Скопировать для разбора» (текст для нового чата)
   Словарь › Комментарии в режиме проверки показывает все замечания с фильтрами.
   Замечание — это обычный комментарий (B1.store.comments) с полями
   kind (тип), status, place (где: тема/раздел или тема/упражнение/пункт), topic, fix, key, mine. */
(function(){
'use strict';
var B1=window.B1,el=B1.util.el,S=B1.store,UI=B1.ui;
var app=document.getElementById('app');
function A(){return B1.app;}
function TB(){return B1.textbook;}

var TYPES=[['rule','Правило'],['key','Ключ'],['task','Задание'],['unclear','Непонятно'],['weak','Моё слабое место'],['dict','Словарь']];
var TYPE={};TYPES.forEach(function(x){TYPE[x[0]]=x[1];});
var ST={open:'открыто',fixed:'исправлено · проверьте',checked:'проверено',noerr:'не ошибка',learned:'усвоено'};
var CLOSED=['checked','noerr','learned'];

/* ---------- режим ---------- */
function reviewer(){return !!S.prefs.get('reviewer',false);}
function on(){return reviewer()&&S.prefs.get('review',true)!==false;}
function toggle(after){
  var v=on();
  var b=UI.btn('rv-tog'+(v?' on':''),null,function(){S.prefs.set('review',!on());if(after)after();});
  b.setAttribute('aria-pressed',String(v));
  b.append(UI.icon('check',16),el('span',null,v?'Проверка':'Проверка выкл.'));
  return b;
}

/* ---------- данные замечаний ---------- */
function kindOf(c){return c.kind||'';}
function statusOf(c){if(c.status)return c.status;return c.done?'checked':'open';}
function isOpen(c){return CLOSED.indexOf(statusOf(c))<0;}
function topicOf(c){
  if(c.topic)return c.topic;
  var sc=String(c.scope||'');
  if(sc.indexOf('tb:')===0)return sc.slice(3).split('/')[0];
  if(sc.indexOf('dict:')===0)return 'dict';
  return 'other';
}
function placeOf(c){
  if(c.place)return c.place;
  var sc=String(c.scope||'');
  if(sc.indexOf('tb:')===0)return sc.slice(3);
  return sc.replace(/^page:/,'');
}
function review(){return S.comments.all().filter(function(c){return !!c.kind;});}
function openCount(topic,sub){
  return review().filter(function(c){
    if(topicOf(c)!==topic||!isOpen(c))return false;
    if(!sub)return true;
    var p=placeOf(c).split('/');return p[1]===sub;
  }).length;
}
function shortId(c){return '#'+String(c.id).slice(-5);}
function topicTitle(id){
  if(id==='dict')return 'Словарь';
  if(id==='other')return 'Другие страницы';
  var m=TB()&&TB().meta(id);if(m)return m.title_pl;
  var c=(B1.catalog||[]).filter(function(x){return x.id===id;})[0];
  return c?c.name:id;
}
/* подпись и ссылка для места */
function labelForScope(scope){
  var sc=String(scope||'');
  if(sc.indexOf('tb:')===0){
    var p=sc.slice(3).split('/'),id=p[0],m=TB()&&TB().meta(id),t=m?m.title_pl:id;
    if(!p[1])return {src:t,href:'#/topic/'+id};
    if(/^t/.test(p[1])&&m){
      var i=-1;m.theory.forEach(function(s,k){if(s.id===p[1])i=k;});
      var st=i>-1?m.theory[i].title.replace(/\[\[|\]\]/g,''):p[1];
      return {src:t+' › Теория · '+(i+1)+'. '+st,href:'#/topic/'+id+'?s='+p[1]};
    }
    if(p[2]==='text')return {src:t+' › '+p[1]+' · текст',href:'#/topic/'+id+'/ex/'+p[1]};
    if(p[2])return {src:t+' › '+p[1]+' · пункт '+p[2],href:'#/topic/'+id+'/ex/'+p[1]+'?i='+p[2]};
    return {src:t+' › '+p[1],href:'#/topic/'+id+'/ex/'+p[1]};
  }
  return null;
}
function prefillFor(scope,o){
  o=o||{};
  var lab=labelForScope(scope)||(A()&&A().labelFor?A().labelFor(null):{src:'',href:location.hash});
  return {scope:scope,src:lab.src,href:lab.href,type:o.type,quote:o.quote||'',key:o.key||'',mine:o.mine||'',occ:0};
}

/* ---------- форма замечания ---------- */
function form(o){
  o=o||{};
  var c=o.comment||null,pre=o.prefill||{};
  if(!c&&pre.scope&&!pre.src){var lab=labelForScope(pre.scope);if(lab){pre.src=lab.src;pre.href=lab.href;}}
  var scope=c?c.scope:pre.scope;
  var isDict=String(scope||'').indexOf('dict:')===0;
  var type=c?(c.kind||'task'):(pre.type||(isDict?'dict':(String(scope).indexOf('tb:')===0&&String(scope).split('/').length>2?'key':'rule')));
  var sh=UI.sheet(c?'Замечание '+shortId(c):'Новое замечание');
  var b=sh.body;
  var place=c?placeOf(c):(String(scope||'').indexOf('tb:')===0?String(scope).slice(3):isDict?'dict/'+(pre.quote||'').split(' — ')[0]:String(scope||'').replace(/^page:/,''));
  var box=el('div','rv-place');
  var top=el('div','rv-place-h');top.append(el('span',null,(c?c.src:pre.src)||''),el('code',null,place));
  box.append(top);
  var quote=c?c.quote:pre.quote;
  if(quote)box.append(el('div','pl rv-quote',quote));
  var key=c?c.key:pre.key,mine=c?c.mine:pre.mine;
  if(key||mine){
    var km=el('div','rv-km');
    if(key){var k1=el('span');k1.append(document.createTextNode('Ключ: '),el('b','pl ok',key));km.append(k1);}
    if(mine){var k2=el('span');k2.append(document.createTextNode('Мой ответ: '),el('b','pl no',mine));km.append(k2);}
    box.append(km);
  }
  b.append(box);
  var lblWhat=el('label',null,'');lblWhat.htmlFor='rv-what';
  var what=el('textarea');what.id='rv-what';what.rows=4;what.value=c?c.text:'';
  var fixW=el('div','fld2');
  var lblFix=el('label',null,'Как должно быть · можно пропустить');lblFix.htmlFor='rv-fix';
  var fix=el('input');fix.type='text';fix.id='rv-fix';fix.placeholder='Если знаете, как правильно';fix.value=c?(c.fix||''):'';fix.autocomplete='off';fix.spellcheck=false;
  fixW.append(lblFix,fix);
  function sync(){
    lblWhat.textContent=type==='weak'?'Что не получается':type==='unclear'?'Что непонятно':'Что не так';
    fixW.hidden=type==='weak'||type==='unclear';
  }
  var tp=el('div','fld2');tp.append(el('span','flabel','Тип'));
  var row=el('div','chiprow wrap');row.setAttribute('role','group');row.setAttribute('aria-label','Тип замечания');
  TYPES.forEach(function(x){
    var bt=UI.btn('chip2'+(x[0]===type?' on':''),x[1],function(){
      row.querySelectorAll('.chip2').forEach(function(y){y.classList.remove('on');y.setAttribute('aria-pressed','false');});
      bt.classList.add('on');bt.setAttribute('aria-pressed','true');type=x[0];sync();
    });
    bt.setAttribute('aria-pressed',String(x[0]===type));row.append(bt);
  });
  tp.append(row);b.append(tp);
  var ww=el('div','fld2');ww.append(lblWhat,what);var err=el('p','ferr');err.hidden=true;ww.append(err);
  b.append(ww,fixW);sync();
  var status=c?statusOf(c):'open';
  if(c){
    var sw=el('div','fld2');sw.append(el('span','flabel','Статус'));
    var sr=el('div','chiprow wrap');
    var opts=type==='weak'?['open','learned']:['open','fixed','checked','noerr'];
    if(opts.indexOf(status)<0)opts.push(status);
    opts.forEach(function(s){
      var bt=UI.btn('chip2'+(s===status?' on':''),ST[s],function(){
        sr.querySelectorAll('.chip2').forEach(function(y){y.classList.remove('on');});bt.classList.add('on');status=s;
      });sr.append(bt);
    });
    sw.append(sr);b.append(sw);
  }else{
    var stl=el('p','fhint');stl.append(document.createTextNode('Статус: '),el('span','rv-st s-open','открыто'),document.createTextNode(type==='weak'?' · потом «усвоено»':' · потом: исправлено → проверено'));
    b.append(stl);
  }
  what.addEventListener('input',function(){err.hidden=true;});
  b.append(UI.btn('btn2 primary',c?'Сохранить':'Сохранить замечание',function(){
    var text=what.value.trim();
    if(!text){err.textContent='Напишите, что не так.';err.hidden=false;what.focus();return;}
    var data={text:text,kind:type,tag:TYPE[type],fix:fixW.hidden?'':fix.value.trim(),status:status,done:CLOSED.indexOf(status)>-1};
    if(c){S.comments.update(c.id,data);sh.close();UI.toast('Замечание сохранено');}
    else{
      Object.assign(data,{scope:scope,href:pre.href||'',src:pre.src||'',quote:pre.quote||'',occ:pre.occ||0,place:place,
        topic:isDict?'dict':String(scope||'').indexOf('tb:')===0?place.split('/')[0]:'other',key:pre.key||'',mine:pre.mine||''});
      var nc=S.comments.add(data);sh.close();
      UI.toast('Замечание сохранено',function(){S.comments.remove(nc.id);});
    }
    if(o.onDone)o.onDone();
  }));
  if(c){
    b.append(UI.btn('btn2 danger','Удалить замечание',function(){
      var rem=S.comments.remove(c.id);sh.close();UI.toast('Замечание удалено',function(){S.comments.restore(rem);});
      if(o.onDone)o.onDone();
    }));
  }
  setTimeout(function(){what.focus({preventScroll:true});},40);
  return sh;
}

/* ---------- список замечаний (Словарь › Комментарии в режиме проверки) ---------- */
var st={sf:'open',tf:'all',topic:'all',q:'',menu:null};
function commentsTab(query){
  if(query&&query.topic){st.topic=query.topic;st.sf='open';}
  var all=S.comments.all();
  var bar=el('div','rv-listbar');
  bar.append(A().link('#/review/export','btn2 small primary','Для разбора'));
  bar.append(el('span','fhint','Всего: '+all.length));
  app.append(bar);
  function inTopic(c){return st.topic==='all'||topicOf(c)===st.topic;}
  function tkey(c){return c.kind||'note:'+(c.tag||'Заметка');}
  function inType(c){return st.tf==='all'||tkey(c)===st.tf;}
  function inSt(c,k){var s=statusOf(c);return k==='all'?true:k==='done'?CLOSED.indexOf(s)>-1:s===k;}
  var base=all.filter(function(c){return inTopic(c)&&inType(c);});
  var r1=el('div','chiprow scroll');
  [['open','Открыто'],['fixed','Исправлено'],['done','Закрыто'],['all','Все']].forEach(function(x){
    r1.append(UI.btn('chip2'+(st.sf===x[0]?' on':''),x[1]+' · '+base.filter(function(c){return inSt(c,x[0]);}).length,function(){st.sf=x[0];B1.route();}));
  });
  app.append(r1);
  var types=[['all','Все типы']].concat(TYPES);
  all.forEach(function(c){if(!c.kind){var k=tkey(c);if(!types.some(function(t){return t[0]===k;}))types.push([k,c.tag||'Заметка']);}});
  var r2=el('div','chiprow scroll small');
  types.forEach(function(x){
    var n=x[0]==='all'?0:all.filter(function(c){return inTopic(c)&&tkey(c)===x[0];}).length;
    if(x[0]!=='all'&&!n&&st.tf!==x[0])return;
    r2.append(UI.btn('chip2 small'+(st.tf===x[0]?' on':''),x[1]+(n?' · '+n:''),function(){st.tf=x[0];B1.route();}));
  });
  app.append(r2);
  var tops=[];all.forEach(function(c){var t=topicOf(c);if(tops.indexOf(t)<0)tops.push(t);});
  var lab=el('label','rv-sel');lab.append(el('span',null,'Тема'));
  var sel=el('select');
  [['all','Все темы']].concat(tops.map(function(t){return [t,topicTitle(t)];})).forEach(function(x){var o=el('option',null,x[1]);o.value=x[0];if(st.topic===x[0])o.selected=true;sel.append(o);});
  if(st.topic!=='all'&&tops.indexOf(st.topic)<0){var o2=el('option',null,topicTitle(st.topic));o2.value=st.topic;o2.selected=true;sel.append(o2);}
  sel.addEventListener('change',function(){st.topic=sel.value;B1.route();});
  lab.append(sel);app.append(lab);
  var list=el('div','rv-list');app.append(list);
  var items=base.filter(function(c){return inSt(c,st.sf);});
  if(!items.length){list.append(el('p','empty-s','По этим фильтрам ничего нет'));return;}
  items.forEach(function(c){list.append(card(c,query&&query.c===c.id));});
  if(query&&query.c){var t=document.getElementById('c-'+query.c);if(t)setTimeout(function(){t.scrollIntoView({block:'center'});},0);}
}
function card(c,hl){
  var d=el('div','rv-card'+(hl?' hl':''));d.id='c-'+c.id;
  var h=A().link(c.href||'#/','rv-card-h');
  h.append(el('span',null,c.src||placeOf(c)),el('code',null,shortId(c)));
  d.append(h);
  if(c.quote)d.append(el('div','pl rv-quote',c.quote));
  if(c.key||c.mine){
    var km=el('div','rv-km');
    if(c.key){var k1=el('span');k1.append(document.createTextNode('Ключ: '),el('b','pl ok',c.key));km.append(k1);}
    if(c.mine){var k2=el('span');k2.append(document.createTextNode('Мой ответ: '),el('b','pl no',c.mine));km.append(k2);}
    d.append(km);
  }
  d.append(el('p','rv-text',c.text));
  if(c.fix){var f=el('p','rv-fix');f.append(el('b',null,'Как должно быть: '),document.createTextNode(c.fix));d.append(f);}
  var row=el('div','rv-card-a');
  var badges=el('span','rv-badges');
  var s=statusOf(c);
  badges.append(el('span','rv-ty t-'+(c.kind||'note'),c.kind?TYPE[c.kind]:(c.tag||'Заметка')),el('span','rv-st s-'+s,ST[s]||s));
  row.append(badges);
  var acts=el('span','rv-acts');
  var weak=c.kind==='weak';
  var nx=weak?(s==='open'?['learned','Усвоено']:null):(s==='open'?['fixed','Исправлено']:s==='fixed'?['checked','Проверено']:null);
  if(!c.kind)nx=c.done?null:['checked','Решено'];
  if(nx)acts.append(UI.btn('btn2 small',nx[1]+' ›',function(){S.comments.update(c.id,{status:nx[0],done:CLOSED.indexOf(nx[0])>-1});}));
  var mb=UI.btn('icbtn',null,function(){st.menu=st.menu===c.id?null:c.id;B1.route();});
  mb.setAttribute('aria-label','Ещё действия');mb.setAttribute('aria-expanded',String(st.menu===c.id));mb.append(UI.icon('dots',22));
  acts.append(mb);row.append(acts);d.append(row);
  if(st.menu===c.id){
    var m=el('div','rv-menu');
    if(!weak&&s!=='noerr')m.append(UI.btn('btn2 small','Не ошибка',function(){st.menu=null;S.comments.update(c.id,{status:'noerr',done:true});}));
    if(s!=='open')m.append(UI.btn('btn2 small','Открыть снова',function(){st.menu=null;S.comments.update(c.id,{status:'open',done:false});}));
    m.append(UI.btn('btn2 small','Изменить',function(){st.menu=null;if(c.kind)form({comment:c});else UI.commentForm({comment:c});}));
    m.append(UI.btn('btn2 small danger','Удалить',function(){st.menu=null;var rem=S.comments.remove(c.id);UI.toast('Удалено',function(){S.comments.restore(rem);});}));
    d.append(m);
  }
  return d;
}

/* ---------- текст для разбора ---------- */
function device(){
  var ua=navigator.userAgent,os=/Android [\d.]+/.exec(ua)||/iPhone OS [\d_]+|iPad|Mac OS X [\d_]+|Windows NT [\d.]+/.exec(ua);
  var br=/(Edg|OPR|Chrome|Firefox|Version)\/[\d]+/.exec(ua);
  return (os?os[0].replace(/_/g,'.'):'?')+' · '+(br?br[0].replace('Version','Safari'):'?')+' · экран '+window.innerWidth+'×'+window.innerHeight;
}
function fmtDate(d){return ('0'+d.getDate()).slice(-2)+'.'+('0'+(d.getMonth()+1)).slice(-2)+'.'+d.getFullYear();}
var ex={tp:null,pt:{open:true,fixed:true,unchecked:true,wrong:true,log:true}};
function exportTopics(){
  var ids=[];
  review().forEach(function(c){var t=topicOf(c);if(ids.indexOf(t)<0)ids.push(t);});
  (TB()?TB().index():[]).forEach(function(t){
    var touched=t.theory.concat(t.exercises).some(function(x){return S.marks.isOk('tb:'+t.id+'/'+x.id);});
    if(touched&&ids.indexOf(t.id)<0)ids.push(t.id);
  });
  var order=(TB()?TB().index():[]).map(function(t){return t.id;}).concat(['dict','other']);
  ids.sort(function(a,b){var x=order.indexOf(a),y=order.indexOf(b);return (x<0?999:x)-(y<0?999:y);});
  return ids;
}
function wrongAnswers(topic){
  var by={};
  (B1.log?B1.log.all():[]).forEach(function(e){
    if(e.type!=='ans'||e.ok||!e.place||e.place.split('/')[0]!==topic)return;
    var p=e.place.split('/').slice(1).join('/');(by[p]=by[p]||[]).push(e.val);
  });
  return by;
}
function buildText(sel){
  var out='РАЗБОР ПРОВЕРКИ · '+fmtDate(new Date())+' · сайт v'+(B1.ASSET_VER||'?')+'\n';
  out+='Устройство: '+device()+'\n';
  var any=false;
  sel.forEach(function(tid){
    var cs=review().filter(function(c){return topicOf(c)===tid;});
    var lines=[];
    function cl(c){
      var s='- '+shortId(c)+' ['+(TYPE[c.kind]||c.kind).toLowerCase()+'] '+placeOf(c);
      if(c.quote)s+=' «'+c.quote.replace(/\s+/g,' ')+'»';
      if(c.key)s+='\n    ключ: '+c.key;
      if(c.mine)s+=' · мой ответ: '+c.mine;
      s+='\n    '+c.text.replace(/\n+/g,' / ');
      if(c.fix)s+='\n    → '+c.fix;
      return s;
    }
    if(ex.pt.open){var o=cs.filter(function(c){return statusOf(c)==='open';});if(o.length)lines.push('Открытые замечания ('+o.length+'):\n'+o.map(cl).join('\n'));}
    if(ex.pt.fixed){var f=cs.filter(function(c){return statusOf(c)==='fixed';});if(f.length)lines.push('Исправлено, ждёт проверки ('+f.length+'): '+f.map(function(c){return shortId(c)+' '+placeOf(c);}).join(', '));}
    var m=TB()&&TB().meta(tid);
    if(m&&ex.pt.unchecked){
      var un=m.theory.concat(m.exercises).filter(function(x){return !S.marks.isOk('tb:'+tid+'/'+x.id);}).map(function(x){return x.id;});
      lines.push(un.length?'Не отмечены «ок»: '+un.join(', '):'Все разделы и упражнения отмечены «ок».');
    }
    if(m&&ex.pt.wrong){
      var w=wrongAnswers(tid),ks=Object.keys(w);
      if(ks.length)lines.push('Неверные ответы в упражнениях: '+ks.map(function(k){return k+' ×'+w[k].length+' ('+w[k].slice(-3).join('; ')+')';}).join(', '));
    }
    if(!lines.length)return;
    any=true;
    out+='\n== '+topicTitle(tid)+(m?' ('+tid+')':'')+' ==\n'+lines.join('\n')+'\n';
  });
  if(ex.pt.log&&B1.log){
    var errs=B1.log.all().filter(function(e){return e.type==='error'||e.type==='warn'||e.type==='sync';});
    if(errs.length){
      any=true;
      out+='\n== Журнал страницы: ошибки ('+errs.length+', последние 30) ==\n'+errs.slice(-30).map(function(e){return e.t.slice(5,16).replace('T',' ')+' ['+e.type+'] '+e.hash+' — '+e.msg;}).join('\n')+'\n';
    }
  }
  if(!any)out+='\nВыберите хотя бы одну тему или часть с данными.';
  return out;
}
function copyText(t){
  if(navigator.clipboard&&window.isSecureContext)return navigator.clipboard.writeText(t);
  return new Promise(function(res,rej){
    var ta=el('textarea');ta.value=t;ta.style.position='fixed';ta.style.opacity='0';document.body.append(ta);ta.select();
    try{document.execCommand('copy')?res():rej(new Error('copy'));}catch(e){rej(e);}ta.remove();
  });
}
function exportPage(){
  A().title('Для разбора в чате');A().setActive('dict');A().wide(false);
  A().tophead('#/dict/comments','Для разбора в чате','Текст с замечаниями, отметками и журналом');
  var ids=exportTopics();
  if(!ex.tp){ex.tp={};ids.forEach(function(t){ex.tp[t]=true;});}
  var s1=A().section('Темы');
  var box=el('div','rv-checks');
  if(!ids.length)box.append(el('p','fhint','Пока нет ни замечаний, ни отметок «ок».'));
  ids.forEach(function(t){
    var cs=review().filter(function(c){return topicOf(c)===t;});
    var o=cs.filter(function(c){return statusOf(c)==='open';}).length,f=cs.filter(function(c){return statusOf(c)==='fixed';}).length;
    var m=TB()&&TB().meta(t),un=m?m.theory.concat(m.exercises).filter(function(x){return !S.marks.isOk('tb:'+t+'/'+x.id);}).length:0;
    var lab=el('label','rv-check');var cb=el('input');cb.type='checkbox';cb.checked=ex.tp[t]!==false;
    cb.addEventListener('change',function(){ex.tp[t]=cb.checked;upd();});
    var tx=el('span');tx.append(el('span','rv-check-t'+(m?' pl':''),topicTitle(t)),el('span','rv-check-s',[o?'открыто '+o:'',f?'исправлено '+f:'',un?'не отмечено '+un:''].filter(Boolean).join(' · ')||'всё проверено'));
    lab.append(cb,tx);box.append(lab);
  });
  s1.append(box);
  var s2=A().section('Что включить');
  var row=el('div','chiprow wrap');
  [['open','Открытые'],['fixed','Исправленные'],['unchecked','Непроверенные разделы'],['wrong','Неверные ответы'],['log','Ошибки страницы']].forEach(function(x){
    var b=UI.btn('chip2'+(ex.pt[x[0]]?' on':''),x[1],function(){ex.pt[x[0]]=!ex.pt[x[0]];b.classList.toggle('on',ex.pt[x[0]]);b.setAttribute('aria-pressed',String(ex.pt[x[0]]));upd();});
    b.setAttribute('aria-pressed',String(!!ex.pt[x[0]]));row.append(b);
  });
  s2.append(row);
  var s3=A().section('Что попадёт в чат');
  var size=el('p','fhint');var pre=el('pre','rv-pre');s3.append(size,pre);
  var cp=UI.btn('btn2 primary wide-b',null,function(){
    copyText(pre.textContent).then(function(){UI.toast('Скопировано · '+pre.textContent.length+' знаков');},function(){
      UI.toast('Не получилось скопировать. Выделите текст вручную.');
      var r=document.createRange();r.selectNodeContents(pre);var s=window.getSelection();s.removeAllRanges();s.addRange(r);
    });
  });
  cp.append(UI.icon('note',18),document.createTextNode('Скопировать'));
  app.append(cp);
  app.append(el('p','fhint center','Откройте новый чат в проекте egzamin-b1-site и вставьте текст.'));
  function upd(){var sel=ids.filter(function(t){return ex.tp[t]!==false;});var t=buildText(sel);pre.textContent=t;size.textContent=t.length+' знаков';}
  upd();
}

/* ---------- вход ---------- */
function loginPage(){
  A().title('Вход');A().setActive('');A().wide(false);
  var C=B1.cloud;
  var w=el('div','rv-login');
  w.append(el('div','pl rv-hi','Dzień dobry!'));
  app.append(w);
  if(C&&C.user()){
    w.append(el('p',null,'Вы вошли как '+(C.user().email||'')+'.'));
    w.append(A().link('#/admin','btn2 primary wide-b','К проверке'));
    return;
  }
  var formEl=el('form','rv-lform');
  formEl.append(el('p',null,'Войдите, чтобы словарь, отметки и замечания сохранялись и были видны с любого телефона.'));
  var lab=el('label',null,'Электронная почта');lab.htmlFor='rv-em';
  var inp=el('input');inp.type='email';inp.id='rv-em';inp.autocomplete='email';inp.inputMode='email';inp.placeholder='you@example.com';
  try{inp.value=localStorage.getItem('pl:loginEmail')||'';}catch(e){}
  var err=el('p','ferr');err.hidden=true;
  var sb=el('button','btn2 primary wide-b','Прислать ссылку для входа');sb.type='submit';
  formEl.append(lab,inp,err,sb,el('p','fhint','Пароль не нужен. Откройте письмо на этом же устройстве и в этом же браузере.'));
  w.append(formEl);
  if(C&&C.state()==='err'&&C.error())err.textContent=C.error(),err.hidden=false;
  formEl.addEventListener('submit',function(ev){
    ev.preventDefault();
    var em=inp.value.trim();
    if(!/^\S+@\S+\.\S+$/.test(em)){err.textContent='Проверьте адрес почты.';err.hidden=false;return;}
    sb.disabled=true;sb.textContent='Отправляю…';
    (C?C.sendLink(em):Promise.reject(new Error('Синхронизация не загрузилась'))).then(function(){
      w.replaceChildren(el('div','pl rv-hi','Проверьте почту'),
        el('p',null,'Ссылка отправлена на '+em+'. Откройте письмо на этом устройстве и нажмите ссылку. Она работает один час.'),
        el('p','fhint','Письма нет? Загляните в «Спам». Повторно отправить можно через минуту.'));
      var again=UI.btn('btn2','Другой адрес',function(){B1.route();});w.append(again);
    }).catch(function(e){
      sb.disabled=false;sb.textContent='Прислать ссылку для входа';
      var m=(e&&e.message)||String(e);
      if(/rate limit|seconds/i.test(m))m='Слишком часто. Подождите минуту и попробуйте снова.';
      err.textContent='Не отправилось: '+m;err.hidden=false;
      if(B1.log)B1.log('sync','Вход: '+m);
    });
  });
}

/* ---------- суперадминка ---------- */
function adminPage(){
  S.prefs.set('reviewer',true);
  A().title('Проверка');A().setActive('');A().wide(false);
  A().tophead('#/','Проверка','Учебник, замечания, синхронизация');
  var C=B1.cloud;
  var s1=A().section('Аккаунт');
  var acc=el('div','card rv-acc');s1.append(acc);
  function drawAcc(){
    acc.replaceChildren();
    var u=C&&C.user();
    if(u){
      acc.append(el('p',null,'Вход: '+(u.email||u.id)));
      var stx={off:'не подключено',sync:'синхронизация…',ok:'синхронизировано',err:'ошибка'}[C.state()]||C.state();
      var p=el('p','fhint','Сервер: '+stx+(C.lastSync()?' · '+new Date(C.lastSync()).toLocaleString('ru-RU',{day:'numeric',month:'short',hour:'2-digit',minute:'2-digit'}):'')+(C.pending()?' · не отправлено: '+C.pending():''));
      acc.append(p);
      if(C.state()==='err')acc.append(el('p','ferr',C.error()));
      var r=el('div','rv-row');
      r.append(UI.btn('btn2 small','Синхронизировать сейчас',function(){C.pull();}));
      r.append(UI.btn('btn2 small','Выйти',function(){C.signOut().then(function(){B1.route();});}));
      acc.append(r);
    }else{
      acc.append(el('p',null,'Вы не вошли. Всё сохраняется только в этом браузере.'));
      if(C&&C.state()==='err'&&C.error())acc.append(el('p','ferr',C.error()));
      if(C&&C.pending())acc.append(el('p','fhint','Ждут отправки после входа: '+C.pending()));
      acc.append(A().link('#/login','btn2 primary','Войти по ссылке'));
    }
  }
  drawAcc();
  if(C)C.onState(function(){if(document.body.contains(acc))drawAcc();});
  var s2=A().section('Режим проверки');
  var lab=el('label','chk');var cb=el('input');cb.type='checkbox';cb.checked=on();
  cb.addEventListener('change',function(){S.prefs.set('review',cb.checked);});
  lab.append(cb,el('span',null,'Показывать «ок», замечания и счётчики на страницах учебника'));
  s2.append(lab);
  var s3=A().section('Куда');
  var all=S.comments.all().filter(function(c){return c.kind;}),open=all.filter(isOpen).length;
  s3.append(A().rowLink('#/learn/grammar','Учебник: темы',(TB()?TB().index().length:0)+' тем'),
    A().rowLink('#/dict/comments','Все замечания','открыто '+open+' из '+all.length),
    A().rowLink('#/review/export','Скопировать для разбора','текст для нового чата'));
  var s4=A().section('Журнал страницы');
  var lg=B1.log?B1.log.all():[];
  var errs=lg.filter(function(e){return e.type==='error'||e.type==='warn'||e.type==='sync';});
  s4.append(el('p','fhint','Записей: '+lg.length+' · ошибок: '+errs.length+'. Ошибки попадают в «Скопировать для разбора».'));
  var det=el('details','rv-log');det.append(el('summary',null,'Показать последние 60'));
  var pre=el('pre','rv-pre');pre.textContent=lg.slice(-60).reverse().map(function(e){return e.t.slice(5,19).replace('T',' ')+' ['+e.type+'] '+e.hash+' '+e.msg;}).join('\n')||'Пусто';
  det.append(pre);s4.append(det);
  s4.append(UI.btn('btn2 small','Очистить журнал',function(){if(B1.log)B1.log.clear();B1.route();}));
  var s5=A().section('Версия');
  s5.append(el('p','fhint','Сайт v'+(B1.ASSET_VER||'?')+' · '+device()));
}

B1.review={on:on,reviewer:reviewer,toggle:toggle,form:form,prefillFor:prefillFor,openCount:openCount,
  commentsTab:commentsTab,exportPage:exportPage,loginPage:loginPage,adminPage:adminPage,labelForScope:labelForScope,
  TYPES:TYPES,ST:ST,statusOf:statusOf,isOpen:isOpen};
})();
