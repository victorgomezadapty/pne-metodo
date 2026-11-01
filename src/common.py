# Shared CSS and JS. Palette is ink blue and copper, separate from the lumbar green/amber site.
P = dict(bg="#10141c", bg2="#161c28", card="#1c2433", card2="#243044", line="#314056", line2="#41516c",
         ink="#e7eef8", muted="#a9b6c9", soft="#8493a8", coral="#e3946a", cyan="#6aa6ff", coralg="#f0b48a",
         cyang="#9cc4ff", focus="#d7e6ff")
CSS = """
*{box-sizing:border-box}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{margin:0;background:BG;color:INK;font:17px/1.65 BODYF;overflow-x:hidden;
background-image:linear-gradient(BG2 1px,transparent 1px),linear-gradient(90deg,BG2 1px,transparent 1px);background-size:48px 48px}
a{color:CYANG}
:focus-visible{outline:2px solid FOCUS;outline-offset:3px;border-radius:4px}
.skip{position:absolute;inset-inline-start:-9999px}.skip:focus{inset-inline-start:12px;top:12px;z-index:60;background:INK;color:BG;padding:8px 12px;border-radius:8px}
.sr{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0,0,0,0);border:0}
.wrap{max-width:1160px;margin:0 auto;padding:0 24px}
.progress{position:fixed;top:0;left:0;height:2px;width:100%;transform-origin:0 50%;transform:scaleX(0);background:linear-gradient(90deg,CYAN,CORAL);z-index:40}
.topbar{position:sticky;top:0;z-index:30;background:rgba(16,20,28,.9);backdrop-filter:blur(12px);border-bottom:1px solid LINE}
.topbar .wrap{display:flex;align-items:center;gap:18px;height:64px}
.brand{display:flex;align-items:center;gap:10px;color:INK;text-decoration:none;font:600 16px HEADF;white-space:nowrap}
.brand svg{width:30px;height:30px;flex:none}
.nav{display:flex;gap:2px;margin-inline-start:auto;overflow-x:auto;min-width:0;flex:1}
.nav a{color:MUTED;text-decoration:none;font-size:13.5px;padding:6px 8px;border-radius:8px;white-space:nowrap}
.nav a:hover,.nav a.on{color:INK;background:CARD}
.lang{display:inline-flex;border:1px solid LINE2;border-radius:9px;overflow:hidden;flex:none}
.lang a{color:MUTED;font:600 12px MONOF;padding:7px 10px;text-decoration:none}
.lang a[aria-current]{background:INK;color:BG}
.kicker{font:600 12px MONOF;letter-spacing:2px;text-transform:uppercase;color:CYANG}
.kicker .dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:CORAL;margin-inline-end:8px;box-shadow:0 0 12px CORALG;animation:pulse 2s infinite}
@keyframes pulse{50%{opacity:.35}}
h1,h2,h3{font-family:HEADF;font-weight:600;letter-spacing:-.02em;line-height:1.12;margin:0}
h1{font-size:clamp(36px,5.6vw,68px);margin:18px 0 22px}
h1 .c{color:CORAL} h1 .y{color:CYAN}
h2{font-size:clamp(28px,3.6vw,44px);margin:12px 0 16px}
h3{font-size:21px;margin:28px 0 8px}
.lead{font-size:clamp(18px,2vw,21px);color:MUTED;max-width:760px}
.muted{color:MUTED}.small{font-size:14px}.soft{color:SOFT}
p{color:#d5deea}
.num{font:600 12px MONOF;color:SOFT;letter-spacing:2px}
.cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:30px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:12px 18px;border-radius:10px;font:600 15px BODYF;text-decoration:none;border:1px solid LINE2;color:INK;background:CARD;transition:transform .2s,border-color .2s}
.btn:hover{transform:translateY(-1px);border-color:SOFT}
.btn.primary{background:CORAL;border-color:CORAL;color:#2a1408}
section{padding:84px 0;border-top:1px solid LINE;scroll-margin-top:72px}
.grid-2{display:grid;grid-template-columns:1fr 1fr;gap:28px;align-items:start}
.grid-3{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.grid-2>*,.grid-3>*,.hero-grid>*,.toc>*,.kpis>*{min-width:0}
.card{background:CARD;border:1px solid LINE;border-radius:18px;padding:26px}
.card.glow{box-shadow:0 30px 80px -40px rgba(106,166,255,.35)}
.tag{display:inline-block;font:600 11px MONOF;letter-spacing:1px;text-transform:uppercase;padding:4px 9px;border-radius:6px;background:CARD2;color:CYANG;border:1px solid LINE2}
.tag.coral{color:CORALG}
.callout{border-inline-start:3px solid CORAL;background:CARD;padding:18px 22px;border-radius:14px;margin:26px 0;color:MUTED}
.callout strong{color:INK}
.callout.cy{border-inline-start-color:CYAN}
.hero{padding-top:70px;padding-bottom:20px}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:36px}
.kpi{background:CARD;border:1px solid LINE;border-radius:14px;padding:18px}
.kpi b{display:block;font:600 32px/1.1 MONOF;font-variant-numeric:tabular-nums}
.kpi b.c{color:CORAL}.kpi b.y{color:CYAN}
.kpi span{font-size:13px;color:MUTED}
.toc{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin-top:26px}
.toc a{display:block;background:CARD;border:1px solid LINE;border-radius:16px;padding:18px;text-decoration:none;color:INK;transition:transform .3s,border-color .3s}
.toc a:hover{transform:translateY(-4px);border-color:CORAL}
.toc .k{font:600 12px MONOF;color:CORALG}
.toc b{display:block;font:600 17px HEADF;margin:6px 0}
.toc span{font-size:13.5px;color:MUTED}
.table-wrap{overflow-x:auto;border:1px solid LINE;border-radius:14px;background:CARD;margin:22px 0}
table{border-collapse:collapse;width:100%;font-size:14.5px}
th,td{text-align:start;padding:12px 14px;border-bottom:1px solid LINE;vertical-align:top}
th{font:600 11px MONOF;letter-spacing:1px;text-transform:uppercase;color:SOFT;background:CARD2}
td b{color:INK}
tr:last-child td{border-bottom:0}
ul,ol{color:#d5deea}
li{margin:6px 0}
.rules{list-style:none;padding:0;margin:18px 0;display:grid;gap:10px;counter-reset:r}
.rules li{background:CARD2;border:1px solid LINE;border-radius:12px;padding:14px 16px 14px 56px;position:relative;counter-increment:r}
.rules li::before{content:counter(r,decimal-leading-zero);position:absolute;inset-inline-start:16px;top:14px;font:600 13px MONOF;color:CORALG}
.rules li small{display:block;color:SOFT;font-size:12.5px;margin-top:4px}
ol.refs{padding-inline-start:24px;font-size:14.5px;color:#d5deea}
ol.refs li{margin-bottom:12px;overflow-wrap:anywhere}
ol.refs .st{display:inline-block;margin-inline-start:6px;color:SOFT;font-size:12.5px}
footer{border-top:1px solid LINE;padding:44px 0 60px;color:MUTED;font-size:14px}
.disc{border:1px solid LINE2;border-radius:14px;padding:16px 18px;background:CARD;color:INK;margin:24px 0}
.js .reveal{opacity:0;transform:translateY(24px);transition:opacity .8s ease,transform .8s cubic-bezier(.2,.7,.2,1)}
.js .reveal.in{opacity:1;transform:none}
.js .reveal.d1{transition-delay:.1s}.js .reveal.d2{transition-delay:.2s}.js .reveal.d3{transition-delay:.3s}.js .reveal.d4{transition-delay:.4s}
.tabs main section[data-panel]{display:none}
.tabs main section[data-panel].active{display:block;animation:panel .35s ease}
@keyframes panel{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.nav a.on{color:INK;background:CARD;box-shadow:inset 0 -2px 0 CORAL}
.pager{display:none}
.tabs .pager{display:flex;flex-wrap:wrap;gap:12px;margin-top:56px;padding-top:24px;border-top:1px solid LINE}
.pager a{display:inline-flex;align-items:center;min-height:44px;padding:10px 16px;border-radius:10px;border:1px solid LINE2;background:CARD;color:INK;text-decoration:none;font:600 14px BODYF}
.pager a:hover{border-color:CORAL}
.pager .next{margin-inline-start:auto;background:CORAL;border-color:CORAL;color:#2a1408}
.forest{display:grid;gap:12px;margin:18px 0}
.frow{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(140px,.9fr) minmax(148px,auto);gap:12px;align-items:center}
.flab b{display:block;font:600 14.5px HEADF;color:INK}
.flab span{display:block;color:SOFT;font-size:12.5px}
.ftrack{position:relative;height:32px;background:CARD2;border:1px solid LINE;border-radius:8px}
.fzero{position:absolute;top:3px;bottom:3px;width:1px;background:SOFT}
.fwh{position:absolute;top:13px;height:6px;border-radius:3px;background:CYAN}
.fwh.soft{background:CORAL}
.fdot{position:absolute;top:8px;width:16px;height:16px;margin-left:-8px;border-radius:50%;background:CYAN;box-shadow:0 0 0 3px rgba(16,20,28,.85)}
.fdot.soft{background:CORAL}
.fnum{font:600 12.5px/1.35 MONOF;text-align:end;color:INK}
.dose-grid{display:grid;grid-template-columns:repeat(5,1fr);gap:12px;margin:18px 0}
.dose{background:CARD2;border:1px solid LINE;border-radius:14px;padding:16px}
.dose b{display:block;font:600 12px MONOF;color:CYANG;letter-spacing:.04em;text-transform:uppercase}
.dose .big{display:block;font:600 26px MONOF;color:CORALG;margin:6px 0}
.dose p{margin:0;font-size:14px}
.dose .src{display:block;margin-top:8px;color:SOFT;font-size:12.5px}
.ladder{position:relative;height:78px;margin:28px 8px 8px}
.ladder-line{position:absolute;left:0;right:0;top:14px;height:3px;border-radius:2px;background:linear-gradient(90deg,LINE2,CYAN,CORAL)}
.mark{position:absolute;top:6px;transform:translateX(-50%);font:600 12px MONOF;color:INK;text-align:center;white-space:nowrap}
.mark i{display:block;width:14px;height:14px;border-radius:50%;background:BG;border:3px solid CYAN;margin:0 auto 8px}
.filters{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin:18px 0}
.filters input{background:CARD;color:INK;border:1px solid LINE2;border-radius:10px;padding:10px 12px;font:16px BODYF;min-width:min(100%,280px)}
.filter-pills{display:flex;flex-wrap:wrap;gap:8px}
.filter-pills button{background:CARD;color:INK;border:1px solid LINE2;border-radius:999px;padding:8px 12px;font:600 13px BODYF;cursor:pointer}
.filter-pills button[aria-pressed=true]{background:INK;color:BG;border-color:INK}
code{font-family:MONOF;font-size:.92em;color:CYANG}
.cols{display:flex;flex-wrap:wrap;gap:6px;margin:8px 0 16px}
.cols code{background:CARD2;border:1px solid LINE;border-radius:6px;padding:3px 6px}
.pick{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:28px 0}
.pick a{text-decoration:none;color:INK}
.pick a:hover{border-color:CORAL}
@media (max-width:1180px){
.topbar .wrap{height:auto;min-height:58px;flex-wrap:wrap;padding-top:8px;padding-bottom:8px;gap:8px}
.nav{order:3;flex:none;width:100%;margin-inline-start:0}
.lang{margin-inline-start:auto}}
@media (max-width:980px){.grid-2,.frow,.dose-grid{grid-template-columns:1fr 1fr}.kpis{grid-template-columns:1fr 1fr}.toc{grid-template-columns:1fr 1fr}.grid-3{grid-template-columns:1fr 1fr}.frow{grid-template-columns:1fr}.fnum{text-align:start}}
@media (max-width:720px){body{font-size:16px}.wrap{padding:0 16px}
.topbar .wrap{height:auto;min-height:58px;flex-wrap:wrap;padding-top:8px;padding-bottom:8px;gap:8px}
.nav{order:3;width:100%;margin-inline-start:0}.lang{margin-inline-start:auto}
section{padding:56px 0}.kpis,.toc,.grid-3,.dose-grid,.pick,.grid-2{grid-template-columns:1fr}.card{padding:20px}
.ladder{height:auto}.ladder-line{display:none}.mark{position:static;transform:none;display:inline-block;margin:0 10px 8px 0}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}
.js .reveal,.toc a,.btn{transition:none!important;transform:none!important;opacity:1!important}
.kicker .dot{animation:none}.tabs main section[data-panel].active{animation:none}}
@media print{.topbar,.progress,.cta,.pager,.filters{display:none}body{background:#fff;color:#000}
.tabs main section[data-panel]{display:block!important}.js .reveal{opacity:1!important;transform:none!important}}
"""
JS = """
document.documentElement.classList.add('js');
(function(){
var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
var loc=document.documentElement.dataset.loc||'en-US';
var bar=document.querySelector('.progress');
function onScroll(){var h=document.documentElement;var k=h.scrollTop/Math.max(1,h.scrollHeight-h.clientHeight);if(bar)bar.style.transform='scaleX('+k+')';}
addEventListener('scroll',onScroll,{passive:true});onScroll();
function fmt(n,v){var d=+(n.dataset.dec||0);return v.toLocaleString(loc,{minimumFractionDigits:d,maximumFractionDigits:d})+(n.dataset.suf||'');}
function countUp(n){var to=parseFloat(n.dataset.count);if(reduce){n.textContent=fmt(n,to);return;}var t0=performance.now();
function st(t){var k=Math.min(1,(t-t0)/1400);n.textContent=fmt(n,to*(1-Math.pow(1-k,3)));if(k<1)requestAnimationFrame(st);}requestAnimationFrame(st);}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var t=e.target;t.classList.add('in');if(t.dataset.count)countUp(t);io.unobserve(t);});},{threshold:0.2,rootMargin:'0px 0px -40px 0px'});
document.querySelectorAll('.reveal,[data-count]').forEach(function(n){io.observe(n);});
var panels=[].slice.call(document.querySelectorAll('main section[id]'));
var navLinks=[].slice.call(document.querySelectorAll('.nav a[href^="#"]'));
if(panels.length>1){
document.documentElement.classList.add('tabs');
function label(id){var a=document.querySelector('.nav a[href="#'+id+'"]');return a?a.textContent.trim():id;}
panels.forEach(function(p,i){p.setAttribute('data-panel','');
var f=document.createElement('nav');f.className='pager';f.setAttribute('aria-label',label(p.id));
if(i>0){var a=document.createElement('a');a.href='#'+panels[i-1].id;a.className='prev';a.textContent='\\u2190 '+label(panels[i-1].id);f.appendChild(a);}
if(i<panels.length-1){var b=document.createElement('a');b.href='#'+panels[i+1].id;b.className='next';b.textContent=label(panels[i+1].id)+' \\u2192';f.appendChild(b);}
(p.querySelector('.wrap')||p).appendChild(f);});
function show(id,target,url){panels.forEach(function(p){p.classList.toggle('active',p.id===id);});
navLinks.forEach(function(l){var on=l.getAttribute('href')==='#'+id;l.classList.toggle('on',on);if(on)l.setAttribute('aria-current','true');else l.removeAttribute('aria-current');});
if(url&&history.replaceState)history.replaceState(null,'','#'+id);
if(target)target.scrollIntoView({behavior:reduce?'auto':'smooth',block:'start'});}
document.addEventListener('click',function(e){var a=e.target.closest('a[href^="#"]');if(!a)return;var id=a.getAttribute('href').slice(1);var t=id&&document.getElementById(id);var p=t&&t.closest('section[data-panel]');if(!p)return;e.preventDefault();show(p.id,t,true);});
var h=decodeURIComponent(location.hash.slice(1)),ht=h&&document.getElementById(h),hp=ht&&ht.closest('section[data-panel]');
show(hp?hp.id:panels[0].id,null,false);if(hp)setTimeout(function(){ht.scrollIntoView({block:'start'});},60);
}
var q=document.getElementById('q');
var pills=[].slice.call(document.querySelectorAll('.filter-pills button'));
var items=[].slice.call(document.querySelectorAll('ol.refs li'));
var count=document.getElementById('src-count');
if(q&&items.length){
var st='all';
function apply(){
var s=(q.value||'').trim().toLowerCase();
var n=0;
items.forEach(function(li){
var okSt=st==='all'||li.getAttribute('data-st')===st;
var okQ=!s||li.textContent.toLowerCase().indexOf(s)>=0;
var show=okSt&&okQ;
li.hidden=!show;
if(show)n++;
});
if(count)count.textContent=n+' '+(count.getAttribute('data-label')||'');
}
q.addEventListener('input',apply);
pills.forEach(function(btn){btn.addEventListener('click',function(){
st=btn.getAttribute('data-st');
pills.forEach(function(b){b.setAttribute('aria-pressed',b===btn?'true':'false');});
apply();
});});
}
})();
"""
def css(lang, extra=""):
    head = "'Space Grotesk',system-ui,sans-serif"
    body = "'IBM Plex Sans',system-ui,-apple-system,'Segoe UI',sans-serif"
    s = (CSS + extra).replace("HEADF", head).replace("BODYF", body).replace("MONOF", "'JetBrains Mono',ui-monospace,Consolas,monospace")
    for k, v in sorted(P.items(), key=lambda x: -len(x[0])):
        s = s.replace(k.upper(), v)
    return s
