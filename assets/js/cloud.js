/* Синхронизация с сервером (Supabase): вход по ссылке на почту, словарь, замечания и отметки «ок».
   Пока вы не вошли, всё работает как раньше — данные лежат только в этом браузере.
   После входа каждая запись отправляется в таблицу user_items, а при открытии сайта
   (и при возвращении на вкладку) подтягивается всё, что изменилось на других устройствах.
   Правило слияния простое: побеждает более поздняя правка (поле updated).
   Ключ ниже — публичный (publishable), его можно хранить в коде сайта: без входа
   он не даёт ни читать, ни писать — это закрывают правила доступа в supabase/schema.sql. */
(function(){
'use strict';
var B1=window.B1,S=B1.store;
var CFG={
  url:'https://lsxsdgghjpyoxuytqkkh.supabase.co',
  key:'sb_publishable_NMcZ0GTkqu6_3yuHenpD2Q_MWbUAP0Z',
  table:'user_items'
};
var OUT='pl:outbox',SYNCAT='pl:syncAt';
var client=null,user=null,state='off',lastErr='',subs=[],flushT=null,pulling=false;

function setState(s,err){state=s;lastErr=err||'';subs.forEach(function(f){try{f();}catch(e){}});}
function ls(k,v){try{if(v===undefined)return JSON.parse(localStorage.getItem(k)||'null');localStorage.setItem(k,JSON.stringify(v));}catch(e){return null;}}
function outbox(){var o=ls(OUT);return o&&typeof o==='object'?o:{};}

/* --- изменения на этом устройстве копятся в «исходящих», пока не уйдут на сервер --- */
function changed(coll,item,deleted){
  var o=outbox();
  o[coll+'/'+item.id]={coll:coll,id:item.id,data:deleted?{id:item.id,updated:item.updated}:item,deleted:!!deleted};
  ls(OUT,o);
  schedule();
}
function schedule(){clearTimeout(flushT);flushT=setTimeout(flush,700);}
function flush(){
  if(!client||!user)return Promise.resolve();
  var o=outbox(),keys=Object.keys(o);
  if(!keys.length)return Promise.resolve();
  var rows=keys.map(function(k){var x=o[k];return {user_id:user.id,coll:x.coll,id:x.id,data:x.data,deleted:x.deleted,updated_at:new Date().toISOString()};});
  setState('sync');
  return client.from(CFG.table).upsert(rows,{onConflict:'user_id,coll,id'}).then(function(r){
    if(r.error)throw r.error;
    var now=outbox();keys.forEach(function(k){if(now[k]&&JSON.stringify(now[k])===JSON.stringify(o[k]))delete now[k];});
    ls(OUT,now);
    ls(SYNCAT,new Date().toISOString());
    setState('ok');
    if(Object.keys(now).length)schedule();
  }).catch(function(e){
    log('Не отправилось на сервер: '+msg(e));
    setState('err',msg(e));
    clearTimeout(flushT);flushT=setTimeout(flush,15000);
  });
}

/* --- забрать всё с сервера и слить с тем, что есть здесь --- */
function ts(x){var t=Date.parse(x&&x.updated);return isNaN(t)?0:t;}
function pull(){
  if(!client||!user||pulling)return Promise.resolve();
  pulling=true;setState('sync');
  return client.from(CFG.table).select('coll,id,data,deleted').in('coll',S.SYNCED).then(function(r){
    if(r.error)throw r.error;
    var pend=outbox(),byColl={};
    (r.data||[]).forEach(function(row){(byColl[row.coll]=byColl[row.coll]||{})[row.id]=row;});
    S.SYNCED.forEach(function(coll){
      var remote=byColl[coll]||{},local=S[coll].all(),out=[],seen={},dirty=false;
      local.forEach(function(it){
        seen[it.id]=1;
        var rr=remote[it.id];
        if(!rr){
          /* есть только здесь — отправить (кроме уже стоящих в очереди) */
          if(!pend[coll+'/'+it.id])changed(coll,it,false);
          out.push(it);return;
        }
        if(ts(rr.data)>ts(it)){dirty=true;if(!rr.deleted)out.push(rr.data);}
        else{out.push(it);if(ts(it)>ts(rr.data)&&!pend[coll+'/'+it.id])changed(coll,it,false);}
      });
      Object.keys(remote).forEach(function(id){
        if(seen[id])return;var rr=remote[id];
        if(rr.deleted||pend[coll+'/'+id])return;
        out.push(rr.data);dirty=true;
      });
      if(dirty){
        out.sort(function(a,b){return Date.parse(b.created||0)-Date.parse(a.created||0);});
        S[coll]._replace(out);
      }
    });
    ls(SYNCAT,new Date().toISOString());
    pulling=false;setState('ok');
    return flush();
  }).catch(function(e){
    pulling=false;
    log('Не загрузилось с сервера: '+msg(e));
    setState('err',msg(e));
  });
}
function msg(e){
  var m=(e&&(e.message||e.error_description||e.msg))||String(e);
  if(/relation .*user_items.* does not exist|Could not find the table/i.test(m))return 'в базе нет таблицы user_items — выполните supabase/schema.sql';
  if(/Failed to fetch|NetworkError|Load failed/i.test(m))return 'нет связи с сервером';
  return m;
}
function log(t){if(B1.log)B1.log('sync',t);else console.warn(t);}

/* --- вход по ссылке --- */
function redirectUrl(){return location.origin+location.pathname;}
function sendLink(email){
  if(!client)return Promise.reject(new Error('Библиотека Supabase не загрузилась (нет сети?)'));
  return client.auth.signInWithOtp({email:email,options:{emailRedirectTo:redirectUrl(),shouldCreateUser:true}}).then(function(r){
    if(r.error)throw r.error;
    try{localStorage.setItem('pl:loginEmail',email);}catch(e){}
  });
}
function signOut(){
  if(!client)return Promise.resolve();
  return client.auth.signOut().then(function(){user=null;setState('off');});
}

function start(){
  if(!window.supabase||!window.supabase.createClient){setState('off','нет библиотеки');return;}
  try{
    client=window.supabase.createClient(CFG.url,CFG.key,{auth:{flowType:'pkce',persistSession:true,autoRefreshToken:true,detectSessionInUrl:true}});
  }catch(e){setState('err',msg(e));return;}
  client.auth.onAuthStateChange(function(ev,session){
    var was=user&&user.id;
    user=session&&session.user||null;
    if(user){
      S.prefs.set('reviewer',true);
      if(user.id!==was){pull();}
      /* после перехода по ссылке из письма убрать ?code=… из адреса */
      if(/[?&]code=/.test(location.search)){
        history.replaceState(null,'',location.pathname+(location.hash&&location.hash!=='#'?location.hash:'#/admin'));
        if(B1.route)B1.route();
      }
    }else setState('off');
  });
  /* ошибка в ссылке (просрочена, уже использована) приходит в адресе */
  var q=new URLSearchParams(location.search);
  if(q.get('error_description')){
    setState('err',q.get('error_description'));
    log('Вход: '+q.get('error_description'));
    history.replaceState(null,'',location.pathname+'#/login');
  }
  document.addEventListener('visibilitychange',function(){if(document.visibilityState==='visible'&&user)pull();});
  window.addEventListener('online',function(){if(user)flush();});
}

B1.cloud={
  changed:changed,pull:pull,flush:flush,sendLink:sendLink,signOut:signOut,
  user:function(){return user;},
  state:function(){return state;},
  error:function(){return lastErr;},
  pending:function(){return Object.keys(outbox()).length;},
  lastSync:function(){return ls(SYNCAT);},
  onState:function(f){subs.push(f);},
  ready:function(){return !!client;}
};
start();
})();
