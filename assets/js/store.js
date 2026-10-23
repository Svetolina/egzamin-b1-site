/* Хранилище личных данных: словарь, комментарии, настройки.
   Сейчас всё лежит в localStorage этого браузера. Весь остальной код ходит только
   через B1.store, поэтому позже сюда можно подключить Supabase (вход по ссылке на почту)
   и синхронизацию, не трогая страницы. */
(function(){
'use strict';
var B1=window.B1=window.B1||{};
var KEYS={words:'pl:words',comments:'pl:comments',prefs:'pl:prefs'};
var mem={};
function read(k){
  if(mem[k])return mem[k];
  var v=null;
  try{v=JSON.parse(localStorage.getItem(KEYS[k])||'null');}catch(e){v=null;}
  if(k==='prefs'){if(!v||typeof v!=='object'||Array.isArray(v))v={};}
  else if(!Array.isArray(v))v=[];
  mem[k]=v;return v;
}
function write(k){
  try{localStorage.setItem(KEYS[k],JSON.stringify(mem[k]));}catch(e){}
  emit(k);
}
var subs=[];
function emit(k){subs.forEach(function(f){try{f(k);}catch(e){console.error(e);}});}
function uid(){return Date.now().toString(36)+Math.random().toString(36).slice(2,7);}
function now(){return new Date().toISOString();}

function collection(k){
  return {
    all:function(){return read(k).slice();},
    get:function(id){return read(k).filter(function(x){return x.id===id;})[0]||null;},
    add:function(obj){var o=Object.assign({},obj,{id:obj.id||uid(),created:obj.created||now(),updated:now()});read(k).unshift(o);write(k);return o;},
    update:function(id,patch){var list=read(k);for(var i=0;i<list.length;i++){if(list[i].id===id){list[i]=Object.assign({},list[i],patch,{updated:now()});write(k);return list[i];}}return null;},
    remove:function(id){var list=read(k);for(var i=0;i<list.length;i++){if(list[i].id===id){var o=list.splice(i,1)[0];write(k);return {item:o,index:i};}}return null;},
    restore:function(rem){if(!rem)return;var list=read(k);list.splice(Math.min(rem.index,list.length),0,rem.item);write(k);}
  };
}

/* интервальное повторение: коробки Лейтнера, интервалы в днях */
var STEPS=[0,1,3,7,14,30,60];
var DAY=864e5;
function startOfDay(t){var d=new Date(t);d.setHours(0,0,0,0);return d.getTime();}
function srsFresh(){return {box:0,due:0};}
function cardsOf(w){
  var out=[{w:w,dir:'f'}];
  if(w.twoWay)out.push({w:w,dir:'b'});
  return out;
}
function srsOf(w,dir){var s=(w.srs||{})[dir];return s?s:srsFresh();}
function isDue(w,dir,t){return srsOf(w,dir).due<=(t||Date.now());}

var words=collection('words');
words.cards=function(onlyDue){
  var t=Date.now(),out=[];
  read('words').forEach(function(w){cardsOf(w).forEach(function(c){if(!onlyDue||isDue(w,c.dir,t))out.push(c);});});
  return out;
};
words.dueCount=function(){return words.cards(true).length;};
words.grade=function(id,dir,ok){
  var w=words.get(id);if(!w)return;
  var s=Object.assign({},srsOf(w,dir));
  if(ok){s.box=Math.min(STEPS.length-1,s.box+1);s.due=startOfDay(Date.now())+STEPS[s.box]*DAY;}
  else{s.box=0;s.due=0;}
  var srs=Object.assign({},w.srs||{});srs[dir]=s;
  var list=read('words');for(var i=0;i<list.length;i++)if(list[i].id===id){list[i]=Object.assign({},list[i],{srs:srs});}
  write('words');
};
words.findSame=function(pl,exceptId){
  var n=String(pl||'').trim().toLowerCase();if(!n)return null;
  return read('words').filter(function(w){return w.id!==exceptId&&String(w.pl).trim().toLowerCase()===n;})[0]||null;
};

var comments=collection('comments');
comments.forScopes=function(scopes){
  return read('comments').filter(function(c){return scopes.indexOf(c.scope)>-1;});
};

var prefs={
  get:function(k,d){var p=read('prefs');return p[k]===undefined?d:p[k];},
  set:function(k,v){read('prefs')[k]=v;write('prefs');}
};

B1.store={words:words,comments:comments,prefs:prefs,
  onChange:function(f){subs.push(f);},
  /* на будущее: место для синхронизации с сервером */
  backend:'local'};
window.addEventListener('storage',function(e){
  Object.keys(KEYS).forEach(function(k){if(e.key===KEYS[k]){delete mem[k];emit(k);}});
});
})();
