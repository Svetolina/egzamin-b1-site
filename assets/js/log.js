/* Журнал страницы: ошибки скриптов, переходы, ответы в упражнениях учебника, синхронизация.
   Хранится только в этом браузере (последние 400 записей) и попадает в «Скопировать для разбора». */
(function(){
'use strict';
var B1=window.B1=window.B1||{};
var KEY='pl:log',MAX=400,buf=null;
function load(){if(buf)return buf;try{buf=JSON.parse(localStorage.getItem(KEY)||'[]');}catch(e){buf=[];}if(!Array.isArray(buf))buf=[];return buf;}
function save(){try{localStorage.setItem(KEY,JSON.stringify(buf));}catch(e){}}
var T=null;
function add(type,text,extra){
  load();
  var e={t:new Date().toISOString(),type:type,msg:String(text==null?'':text).slice(0,500),hash:location.hash||'#/'};
  if(extra)for(var k in extra)e[k]=extra[k];
  buf.push(e);if(buf.length>MAX)buf.splice(0,buf.length-MAX);
  clearTimeout(T);T=setTimeout(save,300);
  return e;
}
B1.log=add;
B1.log.all=function(){return load().slice();};
B1.log.clear=function(){buf=[];save();};
window.addEventListener('error',function(e){
  add('error',(e.message||'Ошибка')+(e.filename?' @ '+e.filename.replace(/^.*\//,'')+':'+e.lineno+':'+e.colno:''));
});
window.addEventListener('unhandledrejection',function(e){
  var r=e.reason;add('error','Promise: '+((r&&(r.message||r.msg))||String(r)));
});
['error','warn'].forEach(function(lv){
  var orig=console[lv];if(!orig)return;
  console[lv]=function(){
    try{add(lv==='error'?'error':'warn',Array.prototype.map.call(arguments,function(a){return a&&a.stack?a.message:typeof a==='object'?JSON.stringify(a):String(a);}).join(' '));}catch(x){}
    return orig.apply(console,arguments);
  };
});
window.addEventListener('hashchange',function(){add('nav',location.hash);});
window.addEventListener('pagehide',save);
})();
