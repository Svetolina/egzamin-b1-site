/* Движок заданий. Данные тестов лежат в tests/*.js, отрисовка и проверка здесь. */
(function(){
'use strict';
var B1=window.B1=window.B1||{};
B1.tests=B1.tests||[];
B1.register=function(t){B1.tests.push(t);};

/* ---------- утилиты ---------- */
function el(tag,cls,text){var e=document.createElement(tag);if(cls)e.className=cls;if(text!=null)e.textContent=text;return e;}
var fmt=function(n){return String(Math.round(n*4)/4).replace('.',',');};
var norm=function(s){return String(s==null?'':s).trim().toLowerCase().replace(/[„”“"]/g,'').replace(/\s+/g,' ').replace(/[.!?,;:]+$/,'');};
B1.util={el:el,fmt:fmt,norm:norm};

B1.h={
  LISTEN_A:'Proszę uważnie słuchać tego nagrania i wykonywać zadanie zgodnie z podanym przykładem. ',
  mc:function(q,o,a,extra){
    var it={q:q,opts:o.map(function(t,i){return {v:'abc'[i],t:t,label:'abc'[i]+')'};}),a:a};
    if(extra)for(var k in extra)it[k]=extra[k];
    return it;
  },
  tf:function(q,a){return {q:q,opts:[{v:'tak',t:'TAK'},{v:'nie',t:'NIE'}],a:a,inline:true};}
};

B1.sections=[
  {id:'sluch',pl:'Rozumienie ze słuchu',ru:'Аудирование'},
  {id:'czyt',pl:'Rozumienie tekstów pisanych',ru:'Чтение'},
  {id:'gram',pl:'Poprawność gramatyczna',ru:'Грамматика'},
  {id:'pis',pl:'Pisanie',ru:'Письмо'},
  {id:'mow',pl:'Mówienie',ru:'Говорение'}
];

/* ---------- хранилище (localStorage, по одному ключу на тест) ---------- */
function skey(tid){return 'b1site:'+tid;}
function loadSaved(tid){
  var s={a:{},r:{}};
  try{var r=JSON.parse(localStorage.getItem(skey(tid))||'{}');if(r&&typeof r==='object'){s.a=r.a||{};s.r=r.r||{};}}catch(e){}
  return s;
}
B1.results=function(tid){return loadSaved(tid).r;};

function countWords(s){var m=s.trim().match(/\S+/g);return m?m.length:0;}
function copyStr(str,out){
  function fb(){
    var ta=document.createElement('textarea');ta.value=str;ta.setAttribute('readonly','');
    ta.style.cssText='position:fixed;top:0;left:0;opacity:0';document.body.appendChild(ta);ta.select();
    var ok=false;try{ok=document.execCommand('copy');}catch(e){}
    document.body.removeChild(ta);
    out.textContent=ok?'Скопировано.':'Не удалось скопировать: выделите текст вручную.';
  }
  if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(str).then(function(){out.textContent='Скопировано.';},fb);}
  else fb();
}
function fmtTime(sec){return Math.floor(sec/60)+':'+String(Math.floor(sec%60)).padStart(2,'0');}

/* ---------- движок для одного теста ---------- */
B1.engine=function(test){
  var saved=loadSaved(test.id);
  function persist(){try{localStorage.setItem(skey(test.id),JSON.stringify(saved));}catch(e){}}
  function store(id,v){if(v===''||v==null)delete saved.a[id];else saved.a[id]=v;persist();}
  var allTasks=[];
  var cur=null;

  function refresh(){
    if(!cur)return;
    var done=allTasks.filter(function(t){return t.checked;});
    var e=done.reduce(function(s,t){return s+t.earned;},0);
    cur.stat.textContent=done.length?('Проверено заданий: '+done.length+' из '+allTasks.length+', баллы: '+fmt(e)+' / '+fmt(cur.max)):'';
  }

  /* --- аудио к заданию --- */
  function taskAudio(a){
    var box=el('div','taudio');
    var au=el('audio');au.controls=true;au.preload='metadata';au.src=a.src;
    au.setAttribute('aria-label','Nagranie do zadania');
    var row=el('div','taudio-b');
    row.append(el('span','hint',a.plays===1?'Запись звучит один раз.':'Запись звучит два раза.'));
    function jump(sec){return function(){au.currentTime=sec;var p=au.play();if(p&&p.catch)p.catch(function(){});};}
    if(a.skip){var b1=el('button','btn small','Пропустить паузу на чтение');b1.type='button';b1.addEventListener('click',jump(a.skip));row.append(b1);}
    if(a.pass2){var b2=el('button','btn small','Ко второму прослушиванию');b2.type='button';b2.addEventListener('click',jump(a.pass2));row.append(b2);}
    var err=el('p','msg','Запись не загрузилась. Проверьте, что папка audio лежит рядом с index.html.');err.hidden=true;
    au.addEventListener('error',function(){err.hidden=false;});
    box.append(au,row,err);
    return box;
  }

  /* --- оболочка задания --- */
  function shell(def){
    var t={id:def.id,max:def.max,cells:[],checked:false,earned:0,def:def};
    var sec=el('section','task');sec.id='t-'+def.id;
    var head=el('header','task-h');
    var ttl=el('div','task-t');ttl.append(el('span','rn',def.rn));
    var iw=el('div');(def.instr||[]).forEach(function(s,i){iw.append(el('p',i?'instr sub':'instr',s));});
    ttl.append(iw);
    var sc=el('div','score');var fill=el('span','fill','\u00a0');sc.append(fill,el('span','of','/ '+fmt(def.max)+' p.'));
    sc.setAttribute('role','status');
    head.append(ttl,sc);
    var body=el('div','task-b');
    if(def.audio)body.append(taskAudio(def.audio));
    var foot=el('footer','task-f');
    var msg=el('span','msg');msg.setAttribute('role','status');
    var trw=null;
    if(def.transcript){
      trw=el('details','tr');trw.hidden=true;trw.append(el('summary',null,'Транскрипция'));
      def.transcript.forEach(function(x){trw.append(el('p',null,x));});
    }
    var bc=el('button','btn primary','Проверить');bc.type='button';
    var br=el('button','btn','Сбросить');br.type='button';
    foot.append(bc,br,msg);
    sec.append(head,body);if(trw)sec.append(trw);sec.append(foot);
    t.sec=sec;t.body=body;t.fill=fill;
    t.say=function(s){msg.textContent=s||'';};
    t.touch=function(){if(t.checked)t.say('Ответы изменены. Нажмите «Проверить», чтобы обновить результат.');};
    t.check=function(){
      var e=0;t.cells.forEach(function(c){e+=c.evaluate();});
      t.earned=e;t.checked=true;t.fill.textContent=fmt(e);
      sc.setAttribute('aria-label','Wynik: '+fmt(e)+' z '+fmt(def.max)+' punktów');
      saved.r[def.id]=e;persist();
      if(trw)trw.hidden=false;
      t.say('');refresh();return true;
    };
    t.reset=function(){
      t.cells.forEach(function(c){c.clear();});
      t.checked=false;t.earned=0;t.fill.textContent='\u00a0';t.say('');
      delete saved.r[def.id];persist();
      if(trw){trw.hidden=true;trw.open=false;}
      refresh();
    };
    bc.addEventListener('click',t.check);
    br.addEventListener('click',t.reset);
    allTasks.push(t);
    return t;
  }

  /* --- поле (select / input) --- */
  function fieldCell(t,id,ctrl,o){
    var wrap=el('span','fld');var fix=el('span','fix');fix.hidden=true;
    wrap.append(ctrl);
    if(o.hint)wrap.append(el('span','hint','('+o.hint+')'));
    wrap.append(fix);
    var forced=saved.a['f-'+id]==='1';
    if(saved.a[id]!=null)ctrl.value=saved.a[id];
    function neutral(){ctrl.classList.remove('ok','bad');ctrl.removeAttribute('aria-invalid');fix.hidden=true;fix.textContent='';}
    ctrl.addEventListener(ctrl.tagName==='SELECT'?'change':'input',function(){
      store(id,ctrl.value);forced=false;store('f-'+id,'');
      if(t.checked){neutral();t.touch();}
    });
    t.cells.push({
      evaluate:function(){
        var exp=o.expected?o.expected():[];var val=ctrl.value;var earned;
        if(forced)earned=o.pts;
        else if(o.partial)earned=val===''?0:Math.min(o.pts,o.partial(val));
        else earned=(o.judge?o.judge(val):(val!==''&&exp.indexOf(norm(val))>-1))?o.pts:0;
        var ok=earned>=o.pts-1e-9;
        ctrl.classList.toggle('ok',ok);ctrl.classList.toggle('bad',!ok);
        ctrl.setAttribute('aria-invalid',ok?'false':'true');
        fix.textContent='';fix.hidden=ok;
        if(!ok){
          fix.append('→ '+o.display());
          if(earned>0)fix.append(' (засчитано '+fmt(earned)+' из '+fmt(o.pts)+' p.)');
          if(o.canForce&&val!==''){
            var b=el('button','link','засчитать');b.type='button';b.title='Мой вариант тоже верен';
            b.addEventListener('click',function(){forced=true;store('f-'+id,'1');t.check();});
            fix.append(' ',b);
          }
        }
        return earned;
      },
      clear:function(){forced=false;store('f-'+id,'');ctrl.value='';store(id,'');neutral();}
    });
    return wrap;
  }

  /* --- выбор (радио) --- */
  function choiceItem(t,def,it,o){
    var q=el('div','q'+(it.inline?' tfrow':'')+(o.example?' ex':''));
    if(it.text)q.append(el('p','src',it.text));
    var qt=el('p','q-text');
    if(o.example)qt.append(el('span','tagex','Przykład'));else qt.append(el('span','n',o.n+'.'));
    qt.append(' '+it.q);
    var group=el('div','opts'+(it.inline?' inline':''));
    group.setAttribute('role','radiogroup');group.setAttribute('aria-label',o.example?'Przykład':'Pytanie '+o.n);
    var name=t.id+'-q'+(o.example?'ex':o.n);var labs={};
    it.opts.forEach(function(op){
      var lab=el('label','opt');var inp=el('input');inp.type='radio';inp.name=test.id+'-'+name;inp.value=op.v;
      if(o.example){inp.disabled=true;if(it.a===op.v){inp.checked=true;lab.classList.add('on');}}
      lab.append(inp);if(op.label)lab.append(el('span','k',op.label));lab.append(el('span','tx',op.t));
      labs[op.v]=lab;group.append(lab);
    });
    q.append(qt,group);
    if(o.example)return q;
    function current(){var c=group.querySelector('input:checked');return c?c.value:'';}
    function wipe(){Object.keys(labs).forEach(function(k){labs[k].classList.remove('on','ok','bad','reveal');});}
    var sv=saved.a[name];if(sv&&labs[sv]){labs[sv].querySelector('input').checked=true;labs[sv].classList.add('on');}
    group.addEventListener('change',function(){
      wipe();var v=current();if(v)labs[v].classList.add('on');store(name,v);
      if(t.checked)t.touch();
    });
    t.cells.push({
      evaluate:function(){
        var exp=it.a;var sel=current();var ok=!!sel&&sel===exp;
        Object.keys(labs).forEach(function(k){labs[k].classList.remove('ok','bad','reveal');});
        if(sel)labs[sel].classList.add(ok?'ok':'bad');
        if(!ok&&exp&&labs[exp])labs[exp].classList.add('reveal');
        return ok?def.pts:0;
      },
      clear:function(){group.querySelectorAll('input').forEach(function(i){i.checked=false;});wipe();store(name,'');}
    });
    return q;
  }
  function buildChoice(def){
    var t=shell(def);
    if(def.passage){var ps=el('div','passage boxed');def.passage.forEach(function(p){ps.append(el('p',null,p));});t.body.append(ps);}
    if(def.stem)t.body.append(el('p','stem',def.stem));
    if(def.example)t.body.append(choiceItem(t,def,def.example,{example:true}));
    def.items.forEach(function(it,i){t.body.append(choiceItem(t,def,it,{n:i+1}));});
    return t;
  }

  /* --- пропуски в тексте --- */
  function renderRich(host,str,onGap){
    var re=/\{(e:[^}]*|\d+)\}/g,last=0,m;
    while((m=re.exec(str))){
      if(m.index>last)host.append(document.createTextNode(str.slice(last,m.index)));
      var tok=m[1];
      if(tok.indexOf('e:')===0){
        var parts=tok.slice(2).split('|');
        var s=el('span','eg',parts[0]);s.title='przykład';host.append(s);
        if(parts[1])host.append(el('span','hint',' ('+parts[1]+')'));
      }else onGap(parseInt(tok,10),host);
      last=re.lastIndex;
    }
    if(last<str.length)host.append(document.createTextNode(str.slice(last)));
  }
  function buildGaps(def){
    var t=shell(def);
    if(def.box){var bx=el('div','box');def.box.forEach(function(w){bx.append(el('span','w',w));});t.body.append(bx);}
    if(def.legend){var lg=el('div','legend');def.legend.forEach(function(f){var r=el('div','lg'+(f.ex?' used':''));r.append(el('b',null,f.k),el('span',null,f.t));lg.append(r);});t.body.append(lg);}
    var pass=el('div','passage');
    def.text.forEach(function(par){
      var p=el('p');var s=par;var sp=/^([A-ZĄĆĘŁŃÓŚŹŻ][a-ząćęłńóśźż]{2,12}):\s/.exec(s);
      if(sp){p.append(el('span','speaker',sp[1]+':'),document.createTextNode(' '));s=s.slice(sp[0].length);}
      renderRich(p,s,function(n,host){
        var g=def.gaps[n-1];var id=def.id+'-g'+n;var acc=[].concat(g.a);var ctrl;
        if(g.opts){
          ctrl=el('select','gap');ctrl.append(new Option('…',''));g.opts.forEach(function(o){ctrl.append(new Option(o,o));});
        }else{
          ctrl=el('input','gap');ctrl.type='text';ctrl.autocomplete='off';ctrl.spellcheck=false;ctrl.setAttribute('autocapitalize','none');
          ctrl.size=Math.max(8,Math.max.apply(null,acc.map(function(x){return x.length;}))+3);
        }
        ctrl.setAttribute('aria-label','Luka '+n);
        host.append(fieldCell(t,id,ctrl,{pts:def.pts,hint:g.hint,canForce:!g.opts,
          expected:function(){return acc.map(norm);},
          display:function(){return acc.join(' / ');}}));
      });
      pass.append(p);
    });
    t.body.append(pass);
    return t;
  }

  /* --- сопоставление --- */
  function buildMatch(def){
    var t=shell(def);
    if(def.heading)t.body.append(el('h3','hd',def.heading));
    var pic=!!def.pictures;
    function picEl(src,l){var im=el('img','pic');im.src=src;im.alt='Иллюстрация '+l;im.loading='lazy';return im;}
    if(!pic){
      var lg=el('div','legend');
      def.fragments.forEach(function(f){var r=el('div','lg'+(f.ex?' used':''));r.append(el('b',null,f.k),el('span',null,f.t));lg.append(r);});
      t.body.append(lg);
    }
    var rows=el('div','mrows');
    if(def.example){var r0=el('div','mrow ex');
      if(pic){r0.append(el('span','n','Przykład ('+def.example.l+')'),picEl(def.example.img,def.example.l),el('span','eg',def.example.a));}
      else r0.append(el('span','n','Przykład'),el('span','t',def.example.t),el('span','eg',def.example.a));
      rows.append(r0);}
    def.rows.forEach(function(row,i){
      var r=el('div','mrow');
      if(pic)r.append(el('span','n',row.l),picEl(row.img,row.l));else r.append(el('span','n',(i+1)+'.'),el('span','t',row.t));
      var ctrl=el('select','gap');ctrl.append(new Option('…',''));
      def.fragments.forEach(function(f){ctrl.append(new Option(f.k,f.k));});
      ctrl.setAttribute('aria-label',pic?'Numer tekstu do ilustracji '+row.l:'Odpowiedź '+(i+1));
      r.append(fieldCell(t,def.id+'-m'+(i+1),ctrl,{pts:def.pts,
        expected:function(){return [norm(row.a)];},
        display:function(){return row.a;}}));
      rows.append(r);
    });
    t.body.append(rows);
    return t;
  }

  /* --- аудирование IV: у строки один или два ответа в любом порядке --- */
  function buildSlots(def){
    var t=shell(def);
    if(def.stem)t.body.append(el('p','stem',def.stem));
    var rows=el('div','mrows');
    if(def.example){var r0=el('div','mrow ex');r0.append(el('span','n','Przykład'),el('span','t',def.example.t),el('span','eg','osoba '+def.example.v));rows.append(r0);}
    def.rows.forEach(function(r){
      var row=el('div','mrow');row.append(el('span','lt',r.l),el('span','t',r.t));
      var box=el('span','slots');var sels=[];
      var fix=el('span','fix');fix.hidden=true;
      for(var k=0;k<r.n;k++){
        (function(k){
          var s=el('select','gap');s.append(new Option('…',''));
          def.persons.forEach(function(p){s.append(new Option('osoba '+p,p));});
          s.setAttribute('aria-label','Opinia '+r.l+', wybór '+(k+1));
          var id=def.id+'-'+r.l+k;if(saved.a[id]!=null)s.value=saved.a[id];
          s.addEventListener('change',function(){store(id,s.value);if(t.checked){sels.forEach(function(x){x.classList.remove('ok','bad');});fix.hidden=true;t.touch();}});
          sels.push(s);box.append(s);
        })(k);
      }
      box.append(fix);row.append(box);rows.append(row);
      t.cells.push({
        evaluate:function(){
          var exp=r.a.map(String);var pool=exp.slice();var earned=0;var st=[];
          sels.forEach(function(s){var i=s.value?pool.indexOf(s.value):-1;if(i>-1){pool.splice(i,1);earned++;st.push(true);}else st.push(false);});
          sels.forEach(function(s,i){s.classList.toggle('ok',st[i]);s.classList.toggle('bad',!st[i]);});
          fix.hidden=earned===r.n;fix.textContent=earned===r.n?'':'→ '+exp.join(', ');
          return earned*def.pts;
        },
        clear:function(){sels.forEach(function(s,i){s.value='';s.classList.remove('ok','bad');store(def.id+'-'+r.l+i,'');});fix.hidden=true;fix.textContent='';}
      });
    });
    t.body.append(rows);
    return t;
  }

  /* --- грамматика V: вопрос к выделенной части --- */
  function buildQA(def){
    var t=shell(def);
    function sentence(it){var p=el('p');p.append(it.pre);p.append(el('u',null,it.u));p.append(it.post);return p;}
    var ex=el('div','qa');ex.append(el('p','ex-note','Przykład'),sentence(def.example),el('p',null,def.example.q),el('p',null,def.example.reply));
    t.body.append(ex);
    def.items.forEach(function(it,i){
      var box=el('div','qa');
      box.append(sentence(it));
      var ql=el('div','qline');ql.append(el('span',null,'–'));
      var ctrl=el('input','gap');ctrl.type='text';ctrl.autocomplete='off';ctrl.spellcheck=false;ctrl.setAttribute('autocapitalize','none');ctrl.size=12;
      ctrl.setAttribute('aria-label','Początek pytania '+(i+1));
      ql.append(fieldCell(t,def.id+'-q'+(i+1),ctrl,{pts:def.pts,canForce:true,
        partial:it.p?function(v){var n=norm(v);if(it.a.map(norm).indexOf(n)>-1)return def.pts;return it.p[n]||0;}:null,
        expected:function(){return it.a.map(norm);},display:function(){return it.a.join(' / ');}}));
      ql.append(el('span',null,it.after));
      box.append(ql,el('p',null,it.reply));
      t.body.append(box);
    });
    return t;
  }

  /* --- грамматика VI: перефразирование --- */
  function buildRewrite(def){
    var t=shell(def);
    if(def.example){var ex=el('div','rw');ex.append(el('p','ex-note','Przykład'),el('p','src2',def.example.src));
      if(def.example.hint)ex.append(el('p','hint','('+def.example.hint+')'));
      ex.append(el('p','src2',def.example.model));t.body.append(ex);}
    def.items.forEach(function(it,i){
      var box=el('div','rw');
      box.append(el('p','src2',(i+1)+'. '+it.src));if(it.hint)box.append(el('p','hint','('+it.hint+')'));
      var ctrl=el('input','gap wide');ctrl.type='text';ctrl.autocomplete='off';ctrl.spellcheck=false;
      ctrl.setAttribute('aria-label','Zdanie '+(i+1));
      var f=fieldCell(t,def.id+'-r'+(i+1),ctrl,{pts:def.pts,canForce:true,
        partial:it.parts?function(v){var s=norm(v).replace(/,/g,'').replace(/\s*\/\s*/g,' ');if(it.req&&!it.req.test(s))return 0;var e=0;it.parts.forEach(function(p){if(p.re.test(s))e+=p.pts;});return e;}:null,
        judge:function(v){var s=norm(v).replace(/,/g,'').replace(/\s*\/\s*/g,' ');return s!==''&&it.tests.every(function(r){return r.test(s);});},
        display:function(){return it.model;}});
      f.style.display='block';box.append(f);
      t.body.append(box);
    });
    return t;
  }
  var builders={choice:buildChoice,gaps:buildGaps,match:buildMatch,slots:buildSlots,qa:buildQA,rewrite:buildRewrite};

  /* --- таймер --- */
  function timer(minutes){
    var left=minutes*60,iv=null;
    var w=el('div','timer');var time=el('span','time');
    var go=el('button','btn small','Старт');go.type='button';
    var rs=el('button','btn small','Сброс');rs.type='button';
    var over=el('span','overmsg','время вышло');over.hidden=true;
    w.setAttribute('role','timer');w.setAttribute('aria-label','Таймер раздела');
    function draw(){time.textContent=fmtTime(left);w.classList.toggle('over',left===0);over.hidden=left>0;}
    function stop(){clearInterval(iv);iv=null;go.textContent='Старт';}
    go.addEventListener('click',function(){
      if(iv){stop();return;}
      if(left===0)left=minutes*60;
      go.textContent='Пауза';
      iv=setInterval(function(){if(!document.body.contains(w)){clearInterval(iv);return;}left--;if(left<=0){left=0;stop();}draw();},1000);
      draw();
    });
    rs.addEventListener('click',function(){stop();left=minutes*60;draw();});
    w.append(time,go,rs,over);draw();return w;
  }

  /* --- письмо --- */
  function genreLines(d){
    var g=d.gid&&B1.genres&&B1.genres[d.gid];
    if(!g)return [];
    var out=['Что жанр «'+g.pl+'» должен содержать (по методичке комиссии):'];
    g.req.forEach(function(x){out.push('- '+x);});
    return out;
  }
  function reviewPrompt(d,text){
    var n=countWords(text);
    var rub=(B1.rubrics&&B1.rubrics[test.rubric||'A'])||{lines:[]};
    var lines=[
      'Оцени письменную работу как экзаменатор государственного экзамена по польскому как иностранному, уровень B1. Будь строгим и не завышай оценки.','',
      'Задание ('+d.genre+', около '+d.words+' слов; в моём тексте '+n+'). В методичке объём считается по обеим частям вместе (например 25 + 175 = 200 слов), допустимое отклонение около 20 слов; слишком короткий текст снижает оценку за выполнение задания.',
      d.prompt+(d.ad?'\nОбъявление: '+d.ad.join(' '):'')+(d.img?'\n(К заданию есть фотография. Приложите её к сообщению или опишите словами: '+(d.imgAlt||'фотография к заданию')+'.)':'')
    ];
    var gl=genreLines(d);
    if(gl.length){lines.push('');lines=lines.concat(gl);}
    lines.push('');lines=lines.concat(rub.lines||[]);
    if(B1.rubrics&&B1.rubrics.anchors){lines.push('');lines=lines.concat(B1.rubrics.anchors);}
    lines.push('',
      'Формат ответа: 1) балл по каждому критерию с обоснованием в одно-два предложения; 2) итоговая сумма; 3) ошибки по группам (грамматика, лексика, стиль, орфография и пунктуация) с исправлениями, сначала самые важные; 4) исправленный текст; 5) что подтянуть в первую очередь. Оценка ориентировочная.',
      '','Мой текст:','',text);
    return lines.join('\n');
  }
  function writingTask(setId,letter,d){
    var id='w-'+setId+'-'+letter;
    var sec=el('section','task wtask');sec.id='t-'+id;
    var head=el('header','task-h');var ttl=el('div','task-t');ttl.append(el('span','rn',letter+'.'));
    var iw=el('div');iw.append(el('p','instr','Gatunek: '+d.genre+', około '+d.words+' słów'));ttl.append(iw);head.append(ttl);
    var body=el('div','task-b');
    if(d.ad){var ad=el('blockquote','adcard');d.ad.forEach(function(x){ad.append(el('p',null,x));});body.append(ad);}
    body.append(el('p','prompt',d.prompt));
    if(d.img){
      var fg=el('figure','wfig');var im=el('img');im.src=d.img;im.alt=d.imgAlt||'Фотография к заданию';fg.append(im);
      if(d.credit)fg.append(el('figcaption',null,'Źródło: '+d.credit));
      body.append(fg);
    }
    var g=d.gid&&B1.genres&&B1.genres[d.gid];
    if(g){
      var gd=el('details','genre');gd.append(el('summary',null,'Что должно быть в тексте: '+g.pl));
      var ul=el('ul');g.req.forEach(function(x){ul.append(el('li',null,x));});gd.append(ul);
      if(g.phrases){var pp=el('div','phr');g.phrases.forEach(function(x){pp.append(el('p',null,x));});gd.append(pp);}
      if(d.gnote)gd.append(el('p','hint',d.gnote));
      body.append(gd);
    }
    var ta=el('textarea','wr');ta.rows=Math.max(3,Math.round(d.words/16));ta.setAttribute('aria-label','Zadanie '+letter);
    ta.spellcheck=false;ta.value=saved.a[id]||'';
    var row=el('div','task-f');row.style.padding='0';row.style.border='0';
    var cnt=el('span','count');var out=el('span','msg');
    var cp=el('button','btn small','Копировать текст');cp.type='button';
    var cr=el('button','btn small primary','Копировать для проверки');cr.type='button';
    function upd(){var n=countWords(ta.value);cnt.textContent=n+' / '+d.words+' слов';cnt.className='count'+(n>=d.words*0.9&&n<=d.words*1.2?' near':(n>d.words*1.2?' over':''));}
    ta.addEventListener('input',function(){store(id,ta.value);upd();out.textContent='';});
    cp.addEventListener('click',function(){copyStr(ta.value,out);});
    cr.addEventListener('click',function(){
      if(!ta.value.trim()){out.textContent='Сначала напишите текст.';return;}
      copyStr(reviewPrompt(d,ta.value),out);
    });
    row.append(cnt,cr,cp,out);body.append(ta,row);
    sec.append(head,body);upd();return sec;
  }
  function buildWriting(panel){
    var note=el('div','note');
    note.append(
      el('p',null,'Выберите только один набор и выполните оба задания (a и b) из него. Писать нужно самому.'),
      el('p',null,'Кнопка «Копировать для проверки» собирает задание, требования жанра, критерии оценки ('+((B1.rubrics&&B1.rubrics[test.rubric||'A'])||{name:''}).name+') и ваш текст в один запрос. Вставьте его в чат с Claude, и вы получите баллы по критериям и разбор ошибок.'));
    panel.append(note);
    var rb=(B1.rubrics&&B1.rubrics[test.rubric||'A'])||{crit:[]};
    var crit=el('ul','crit');rb.crit.forEach(function(c){crit.append(el('li',null,c));});
    panel.append(crit);
    var sets=test.writing||[];
    var tabs=el('div','tabs');tabs.setAttribute('role','tablist');
    var holders={},btns={};
    function pick(id){
      Object.keys(holders).forEach(function(k){holders[k].hidden=k!==id;btns[k].setAttribute('aria-selected',String(k===id));});
      store('w-set',id);
    }
    sets.forEach(function(s){
      var b=el('button','tab','Zestaw '+s.id);b.type='button';b.setAttribute('role','tab');
      b.addEventListener('click',function(){pick(s.id);});btns[s.id]=b;tabs.append(b);
    });
    panel.append(tabs);
    sets.forEach(function(s){
      var h=el('div');h.append(writingTask(s.id,'a',s.a),writingTask(s.id,'b',s.b));holders[s.id]=h;panel.append(h);
    });
    if(sets.length)pick(saved.a['w-set']&&holders[saved.a['w-set']]?saved.a['w-set']:sets[0].id);
  }

  /* --- раздел целиком --- */
  function renderModule(m){
    var panel=el('section','panel');
    var hd=el('div','mod-h');var left=el('div');left.append(el('h2',null,m.title),el('p','meta',m.meta));
    hd.append(left,timer(m.minutes));panel.append(hd);
    if(m.note){var n=el('div','note');m.note.forEach(function(x){n.append(el('p',null,x));});panel.append(n);}
    var stat=el('span','prog');
    cur={stat:stat,max:m.max};
    if(m.id!=='pis'){
      var act=el('div','actions');
      var bAll=el('button','btn','Проверить все задания');bAll.type='button';
      var bRes=el('button','btn','Сбросить раздел');bRes.type='button';
      bAll.addEventListener('click',function(){allTasks.forEach(function(t){t.check();});});
      var armed=null;
      bRes.addEventListener('click',function(){
        if(!armed){bRes.textContent='Точно сбросить?';armed=setTimeout(function(){armed=null;bRes.textContent='Сбросить раздел';},3000);return;}
        clearTimeout(armed);armed=null;bRes.textContent='Сбросить раздел';
        allTasks.forEach(function(t){t.reset();});
      });
      act.append(bAll,bRes,stat);panel.append(act);
      m.tasks.forEach(function(d){panel.append(builders[d.kind](d).sec);});
      allTasks.forEach(function(t){if(saved.r[t.def.id]!=null)t.check();});
      refresh();
    }else{
      buildWriting(panel);
    }
    return panel;
  }

  /* --- одно задание отдельно (страница задания) --- */
  function renderTask(m,id){
    var d=(m.tasks||[]).filter(function(x){return x.id===id;})[0];
    if(!d)return null;
    var panel=el('section','panel single');
    cur={stat:el('span','prog'),max:d.max};
    panel.append(builders[d.kind](d).sec);
    allTasks.forEach(function(t){if(saved.r[t.def.id]!=null)t.check();});
    return panel;
  }

  return {renderModule:renderModule,renderTask:renderTask,tasks:allTasks};
};
})();
