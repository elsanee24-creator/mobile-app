import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="mobile.app",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

APP = r"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
*{box-sizing:border-box}

:root{
 --mint:#65f5c1;--aqua:#35d8e8;--blue:#668cff;
 --violet:#a77bff;--gold:#ffd477;
 --ink:#102b35;--paper:#f2fff9;--muted:#b9d9d5;
}

html,body{
 margin:0;padding:0;width:100%;min-height:100%;
 font-family:Arial,sans-serif;
 background:linear-gradient(135deg,#c8fff0,#b8d9ff,#e5caff,#fff0c9);
 color:white;
}

body{
 padding:12px 8px 24px;
 background:
 radial-gradient(ellipse at 10% 5%,#70f5cf88,transparent 38%),
 radial-gradient(ellipse at 90% 15%,#8a9dff88,transparent 35%),
 radial-gradient(ellipse at 50% 100%,#ffcf7a66,transparent 42%),
 linear-gradient(135deg,#d7fff1,#d9e7ff 52%,#f1ddff);
}

.phone{
 width:100%;max-width:440px;min-height:820px;
 margin:0 auto;padding:10px;border-radius:38px;
 background:linear-gradient(145deg,#e5fff7,#8be7d3 24%,#92aaff 58%,#d6a9ff 82%,#ffe0a0);
 box-shadow:0 25px 65px #344e7960,inset 0 0 0 2px #ffffffb0;
}

.screen{
 min-height:800px;overflow:hidden;position:relative;
 border-radius:30px;padding:18px 15px 24px;
 background:
 radial-gradient(circle at 5% 0%,#35e9bd55,transparent 35%),
 radial-gradient(circle at 100% 30%,#826bff55,transparent 38%),
 linear-gradient(145deg,#153d49,#173c50 45%,#292c5a 100%);
 border:1px solid #ffffff55;
 transition:background .35s ease;
}

.screen:has(#login-page:not(.hidden)),
.screen:has(#pin-page:not(.hidden)){
 background:radial-gradient(circle at 15% 10%,#40e9c766,transparent 40%),linear-gradient(145deg,#123e4b,#183c61 55%,#44316e);
}
.screen:has(#home-page:not(.hidden)){
 background:radial-gradient(circle at 90% 5%,#ffb75a66,transparent 35%),linear-gradient(145deg,#193b50,#254b67 50%,#51416e);
}
.screen:has(#calculator-page:not(.hidden)){
 background:radial-gradient(circle at 90% 10%,#ffcf6c55,transparent 38%),linear-gradient(145deg,#47304c,#713e55 55%,#a15b55);
}
.screen:has(#password-page:not(.hidden)){
 background:radial-gradient(circle at 90% 5%,#64e7ff55,transparent 38%),linear-gradient(145deg,#123d57,#176b80 55%,#315b83);
}
.screen:has(#notes-page:not(.hidden)){
 background:radial-gradient(circle at 90% 5%,#ffe49a55,transparent 38%),linear-gradient(145deg,#493c2d,#75543c 55%,#986d4d);
}
.screen:has(#games-page:not(.hidden)),
.screen:has(#guess-page:not(.hidden)),
.screen:has(#typing-page:not(.hidden)){
 background:radial-gradient(circle at 90% 5%,#c77bff55,transparent 38%),linear-gradient(145deg,#30265a,#49346e 55%,#743e75);
}
.screen:has(#flappy-page:not(.hidden)){
 background:radial-gradient(circle at 90% 5%,#ffe08b55,transparent 38%),linear-gradient(145deg,#15516c,#267d9b 55%,#55a9a5);
}
.screen:has(#snake-page:not(.hidden)){
 background:radial-gradient(circle at 90% 5%,#a4ff7750,transparent 38%),linear-gradient(145deg,#102f28,#15543d 55%,#28704c);
}
.screen:has(#settings-page:not(.hidden)){
 background:radial-gradient(circle at 90% 5%,#ff9fc855,transparent 38%),linear-gradient(145deg,#482c51,#754267 55%,#a45c70);
}
.screen:has(#about-page:not(.hidden)){
 background:radial-gradient(circle at 90% 5%,#ffe58a55,transparent 38%),linear-gradient(145deg,#51402c,#80603d 55%,#9d8050);
}
.screen:has(#car-page:not(.hidden)){
 background:radial-gradient(circle at 90% 5%,#62f0a855,transparent 38%),linear-gradient(145deg,#102e32,#14564b 55%,#267b62);
}

.topbar{display:flex;justify-content:space-between;align-items:center;color:#eafffa;font-size:12px;margin:2px 4px 20px}
.brand{font-weight:900;letter-spacing:2px;font-size:17px}
.pill{padding:7px 11px;border-radius:30px;background:#ffffff20;border:1px solid #ffffff35;color:#eafffa;font-size:11px}

h1,h2,h3,p{margin-top:0}
h1{font-size:30px;line-height:1.1;margin-bottom:9px}
h2{font-size:21px;margin-bottom:8px}
p{color:#c5e3e2;line-height:1.5;font-size:13px}

button{border:0;cursor:pointer;font-weight:800;font-size:13px;color:#12323a}
.primary{width:100%;padding:15px;border-radius:16px;background:linear-gradient(100deg,var(--mint),var(--aqua),#9bceff);box-shadow:0 8px 22px #36e4ca45}
.secondary{width:100%;padding:14px;border-radius:16px;color:#effffb;background:#ffffff16;border:1px solid #ffffff38}

.login-wrap{min-height:690px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:12px 5px}
.clock-panel{width:100%;display:flex;align-items:center;justify-content:center;gap:20px;margin:0 auto 25px;padding:20px 12px;border-radius:25px;background:linear-gradient(135deg,#ffffff20,#ffffff09);border:1px solid #ffffff40;box-shadow:0 12px 35px #071b3740}
.clock-face{width:116px;height:116px;position:relative;flex-shrink:0;border-radius:50%;background:radial-gradient(circle at 35% 25%,#fff,#d7fff1 55%,#91d9d0);border:5px solid #f5fffc;box-shadow:0 0 0 5px #70f5c155,0 8px 25px #061b3a70}
.clock-face:before{content:"";position:absolute;inset:8px;border-radius:50%;border:1px solid #7aa9a2}
.clock-face .number{position:absolute;color:#24515a;font-size:10px;font-weight:900;transform:translate(-50%,-50%)}
.hand{position:absolute;left:50%;bottom:50%;transform-origin:50% 100%;border-radius:8px}
.hour-hand{width:5px;height:29px;background:#244c62}
.minute-hand{width:3px;height:39px;background:#287c86}
.second-hand{width:2px;height:43px;background:#ed8b65}
.clock-pin{position:absolute;width:9px;height:9px;border-radius:50%;background:#e89a58;left:50%;top:50%;transform:translate(-50%,-50%)}
.time-info{text-align:left;min-width:0}
.digital-time{font-size:25px;font-weight:900;color:#fff;letter-spacing:1px}
.digital-date{font-size:11px;color:#c9e9e5;margin-top:7px;line-height:1.5}
.login-title{font-size:34px;font-weight:900;letter-spacing:1px;background:linear-gradient(90deg,#a5ffe1,#8ceaff,#d8b4ff,#ffe1a1);-webkit-background-clip:text;background-clip:text;color:transparent}
.login-sub{max-width:290px;margin:8px auto 25px}
.login-actions{width:100%;max-width:310px;display:grid;gap:12px}
.section{margin:18px 0}

.card{padding:15px;border-radius:20px;background:linear-gradient(135deg,#ffffff20,#ffffff0c);border:1px solid #ffffff35;box-shadow:0 8px 24px #081b3440}
.tile-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:9px}
.tile{min-height:104px;padding:13px 7px;border-radius:18px;background:linear-gradient(145deg,#176b67,#244b83);border:1px solid #8ce9df;text-align:center;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;color:#f4fffd}
.tile .emoji{font-size:27px}
.tile span:last-child{font-size:11px;font-weight:800}
.wide-tile{width:100%;display:flex;align-items:center;gap:15px;padding:18px;border-radius:20px;text-align:left;color:white;background:linear-gradient(110deg,#a35b27,#b83f70,#6545a6);border:1px solid #ffe0a8;box-shadow:0 10px 25px #081b3440}
.wide-icon{font-size:37px}
.wide-title{font-size:18px;font-weight:900;margin-bottom:5px}
.wide-desc{font-size:11px;color:#effffb;line-height:1.45}
.row-tile{width:100%;display:flex;align-items:center;gap:12px;padding:14px 16px;margin-top:10px;border-radius:16px;text-align:left;color:#f2fffc;background:linear-gradient(110deg,#274d70,#345d57);border:1px solid #91d6c7}
.row-tile .emoji{font-size:22px}
.logout-btn{background:#e53935!important;border-color:#e53935!important;color:#fff!important}
.page-head{display:flex;align-items:center;gap:12px;margin:6px 0 18px}
.back{padding:10px 13px;border-radius:12px;color:#effffb;background:#ffffff1c;border:1px solid #ffffff35}
.field{width:100%;padding:13px;border-radius:13px;border:1px solid #ffffff55;background:#ffffffed;color:#183a42;font-size:14px;margin:5px 0 12px}
.output{padding:14px;border-radius:14px;background:#ffffffed;color:#183a42;overflow-wrap:anywhere;margin:10px 0}
.calc-display{background:#eafff7;color:#173b42;border-radius:15px;padding:18px;text-align:right;font-size:27px;font-weight:900;min-height:65px;margin-bottom:10px;overflow-wrap:anywhere}
.calc-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:7px}
.calc-key{padding:17px 3px;border-radius:13px;background:#f2fff9;color:#173b42;font-size:16px}
.calc-key.op{background:#ffd477}
.calc-key.equal{background:#65f5c1}
.calc-key.clear{background:#ffb8a8}
.game-canvas{width:100%;display:block;border-radius:17px;background:linear-gradient(#6bd8ff,#b8f1ff);border:2px solid #ffffff55;touch-action:none}
.small-note{font-size:11px;color:#c3e2df}
.hidden{display:none!important}

/* TYPING GAME */
#typing-page .card{padding:14px}
#typing-sentence{padding:14px;border-radius:14px;background:#ffffffed;color:#183a42;font-size:14px;line-height:1.8;min-height:110px}
#typing-input{min-height:105px;resize:vertical}
.typing-stats{display:grid;grid-template-columns:repeat(2,1fr);gap:8px;margin:12px 0}
.typing-stat{padding:12px 8px;border-radius:14px;background:#ffffff18;border:1px solid #ffffff30;text-align:center}
.typing-stat b{display:block;font-size:19px;color:#a5ffe1;margin-bottom:4px}
.typing-stat span{font-size:10px;color:#d6e9ed}
#typing-result{margin-top:10px;white-space:pre-line}

/* SNAKE */
#snake-page{touch-action:none;overscroll-behavior:none}
#snake-page .page-head{margin-bottom:8px}
#snake-page .card{padding:10px;background:linear-gradient(145deg,#ffffff19,#ffffff08);border-color:#aaffbb55}
#snake-page .card>p:first-child{margin-bottom:8px;font-size:11px}
#snake-canvas{width:min(100%,288px);height:auto;aspect-ratio:1/1;margin:0 auto 8px;border-radius:13px;background:linear-gradient(145deg,#092b25,#124c38);border:2px solid #8cffb855;touch-action:none}
#snake-controls{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;max-width:225px;margin:5px auto 8px}
#snake-controls button{min-height:42px;padding:7px;border-radius:12px;font-size:19px;background:linear-gradient(145deg,#d9ffe9,#8af0b7);color:#17432f;box-shadow:0 4px 10px #061b1644}
#snake-controls .empty-control{visibility:hidden}
#snake-page .primary{padding:11px;margin-top:4px}
#snake-page #snake-score{margin:8px 0 0;text-align:center;font-weight:800;color:#c9ffdc}

/* CAR RACING */
#car-page{touch-action:pan-y}
#car-page .card{padding:10px}
#car-canvas{width:100%;max-width:340px;height:auto;display:block;margin:0 auto 10px;border-radius:15px;border:2px solid #ffffff55;background:#245b45;touch-action:none}
.car-controls{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:10px}
.car-controls button{padding:15px;border-radius:15px;background:linear-gradient(145deg,#d9ffe9,#8af0b7);color:#17432f;font-size:20px}
.car-score{display:flex;justify-content:space-between;gap:8px;margin:8px 0}
.car-score div{flex:1;text-align:center;padding:10px 5px;border-radius:12px;background:#ffffff18}
.car-score b{display:block;font-size:18px;color:#b5ffcf}
.car-score span{font-size:10px;color:#e2f8e8}
#car-page .small-note{text-align:center}

@media(max-width:360px){
 body{padding:7px 5px 12px}
 .phone{padding:7px;border-radius:30px}
 .screen{padding:14px 11px 18px;border-radius:24px}
 .clock-panel{gap:12px;padding:15px 8px}
 .clock-face{width:96px;height:96px}
 .digital-time{font-size:20px}
 .tile-grid{gap:7px}
 .tile{min-height:96px}
 #snake-canvas{width:min(100%,260px)}
 #snake-controls{max-width:210px}
 #snake-controls button{min-height:39px}
}

/* ABOUT MY SCHOOL — additions scoped to the new school pages */
.school-page{min-height:760px;border-radius:22px;overflow:hidden;background-image:linear-gradient(180deg,#071d2bc9,#071d2b9c),var(--school-bg);background-size:cover;background-position:center;}
.school-overlay{min-height:760px;padding:16px 12px;background:linear-gradient(180deg,#081b2b55,#081b2b9c)}
.school-menu{display:grid;gap:14px;margin-top:28px}
.school-option{width:100%;display:flex;align-items:center;justify-content:space-between;padding:17px 15px;border-radius:17px;color:white;font-weight:800;text-align:left;border:1px solid #ffffff80;box-shadow:0 8px 22px #06172580}
.school-option span{font-size:23px}
.history-option{background:linear-gradient(110deg,#174d79,#247d83)}
.mission-option{background:linear-gradient(110deg,#80501e,#b17b2e)}
.myself-option{background:linear-gradient(110deg,#563b83,#8b477d)}
.school-detail{min-height:760px;padding:12px;border-radius:22px;}
.history-detail{background:linear-gradient(145deg,#102f49,#176b70)}
.mission-detail{background:linear-gradient(145deg,#3a2c60,#80502e)}
.myself-detail{background:linear-gradient(145deg,#263b67,#613b71)}
.school-text-card{padding:16px;border-radius:18px;background:#fffdf5f5;color:#10232b;line-height:1.75;font-size:16px;font-family:'URW Chancery L','Brush Script MT','Segoe Print',cursive;font-weight:600;text-shadow:0 0 0 transparent}
.school-text-card p{margin:0 0 15px;color:#10232b}
.school-text-card p:last-child{margin-bottom:0}
.school-text-card h3{margin:10px 0 6px;color:#10232b;font-family:'URW Chancery L','Brush Script MT','Segoe Print',cursive;font-size:20px;font-weight:800}
.school-text-card ol{padding-left:24px;margin:8px 0 0;color:#10232b}
.school-text-card li{margin:8px 0;color:#10232b}

/* NEON BREAKOUT — isolated game styles */
#breakout-page{color:#effcff;background:radial-gradient(ellipse at 50% 0%,#183c66 0%,transparent 48%),linear-gradient(160deg,#07101f,#10172c 60%,#17102b);border:1px solid #68eaff35;border-radius:22px;padding:13px;overflow:hidden}
#breakout-page .nb-hero{padding:15px;border:1px solid #72eaff44;border-radius:17px;background:linear-gradient(135deg,#142d49dd,#20163ddd);box-shadow:0 12px 28px #0005}
#breakout-page .nb-kicker{font-size:8px;letter-spacing:.2em;color:#76f5ff;font-weight:900}
#breakout-page h2{color:#f4fbff}#breakout-page h3{font-size:12px;color:#dffaff;margin:15px 2px 8px}
#breakout-page p{font-size:10px;line-height:1.55;color:#a9bfd6}
#breakout-page .nb-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:7px;margin-top:12px}
#breakout-page .nb-stat{padding:8px 4px;border-radius:11px;background:#ffffff0c;border:1px solid #ffffff18;text-align:center}
#breakout-page .nb-stat b{display:block;font-size:17px;color:#fff}#breakout-page .nb-stat small{font-size:7px;color:#9fc9dc;letter-spacing:.1em}
#breakout-page .nb-panel{padding:11px;border-radius:15px;border:1px solid #78eaff28;background:linear-gradient(145deg,#ffffff12,#ffffff06);margin-top:9px}
#breakout-page canvas{width:100%;display:block;border-radius:13px;border:1px solid #71eaff44;background:#050b19;touch-action:none;box-shadow:0 0 22px #35caff18}
#breakout-page .nb-row{display:flex;gap:7px;flex-wrap:wrap;align-items:center}
#breakout-page .nb-btn{border:1px solid #72eaff66;background:linear-gradient(110deg,#126d8b,#5541a0);color:white;border-radius:10px;padding:10px 12px;font-size:9px;font-weight:900}
#breakout-page .nb-ghost{background:#ffffff0c;border:1px solid #ffffff25;color:#e2f8ff;border-radius:10px;padding:9px 11px;font-size:9px}
#breakout-page .nb-btn:disabled{opacity:.4}
#breakout-page .nb-levels{display:grid;grid-template-columns:repeat(5,1fr);gap:6px}
#breakout-page .nb-level{padding:9px 2px;border:1px solid #6feaff33;background:#ffffff0b;color:#eafaff;border-radius:9px;font-size:9px}
#breakout-page .nb-level.current{background:#1a7790;border-color:#8af5ff;box-shadow:0 0 12px #55eaff55}
#breakout-page .nb-level:disabled{opacity:.3}
#breakout-page .nb-power{padding:8px;border-radius:10px;background:#071526;border:1px solid #ffffff18;margin:5px 0;font-size:9px;color:#b9d6e6}
#breakout-page .nb-power b{color:#fff}
#breakout-page .nb-status{font-size:9px;color:#8df5ff;min-height:16px}


/* LIVE EARTH — isolated dashboard styles */
.earth-hero{background:radial-gradient(circle at 50% 42%,#123d4b,#071722 65%,#040b13);border:1px solid #55d9dc55;border-radius:24px;padding:14px;overflow:hidden;box-shadow:0 15px 40px #00121c88}
.earth-kicker{font-size:10px;letter-spacing:2px;color:#71e7dc;font-weight:800}
.earth-layout{display:grid;grid-template-columns:minmax(0,1fr) 112px;gap:8px;align-items:center}
#earth-globe{width:100%;height:310px;min-width:0;touch-action:pan-y;cursor:grab;position:relative}
#earth-globe:active{cursor:grabbing}
.earth-side{display:grid;gap:8px}
.earth-stat{background:linear-gradient(145deg,#ffffff12,#ffffff05);border:1px solid #8ce8e455;border-radius:13px;padding:10px 7px;min-width:0;box-shadow:inset 0 0 18px #49d9df0b}
.earth-stat b{display:block;color:#e8ffff;font-size:16px;line-height:1.2;overflow-wrap:anywhere;font-variant-numeric:tabular-nums}
.earth-stat small{display:block;color:#91bfc5;font-size:9px;letter-spacing:.7px;margin-top:5px}
.earth-live-dot{display:inline-block;width:7px;height:7px;background:#55f0a2;border-radius:50%;box-shadow:0 0 9px #55f0a2;margin-right:6px;animation:earthPulse 1.5s infinite}
@keyframes earthPulse{50%{opacity:.35;box-shadow:0 0 2px #55f0a2}}
.earth-tools{display:flex;gap:7px;flex-wrap:wrap;margin-top:10px}
.earth-btn{border:1px solid #69ded866;background:linear-gradient(135deg,#10303a,#174753);color:#dffefa;border-radius:12px;padding:10px 12px;font-weight:700;font-size:12px}
.earth-info{background:#0b202b;border:1px solid #64d8d533;border-radius:16px;padding:13px;margin-top:12px}
.earth-info-grid{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:9px}
.earth-info-cell{background:#ffffff0a;padding:9px;border-radius:10px}
.earth-info-cell small{display:block;color:#9ac1c6;font-size:10px}.earth-info-cell b{font-size:13px;color:#e8ffff}
.earth-note{font-size:10px;color:#9bbbc1;line-height:1.5;margin:9px 2px 0}
.earth-search{display:grid;grid-template-columns:1fr auto;gap:7px;margin:10px 0 0}
.earth-search input{width:100%;min-width:0;background:#071a25;color:#eaffff;border:1px solid #67d8d866;border-radius:11px;padding:11px;font-size:12px;outline:none}
.earth-search input:focus{border-color:#71f3dc;box-shadow:0 0 0 2px #71f3dc22}
.earth-search button{background:#14515b;color:#eaffff;border:1px solid #69ded866;border-radius:11px;padding:0 14px;font-weight:700}
.earth-suggest{display:none;max-height:150px;overflow:auto;background:#0b202b;border:1px solid #64d8d555;border-radius:10px;margin-top:5px}
.earth-suggest button{display:block;width:100%;text-align:left;padding:9px 11px;background:transparent;color:#eaffff;border:0;border-bottom:1px solid #ffffff12;font-size:12px}
.earth-suggest button:last-child{border:0}
.earth-status{font-size:10px;color:#a8d2d5;min-height:15px;margin:5px 2px}
@media(max-width:370px){.earth-layout{grid-template-columns:minmax(0,1fr) 96px}#earth-globe{height:270px}.earth-stat b{font-size:13px}}
</style>
<script src="https://unpkg.com/globe.gl"></script>
</head>

<body>
<div class="phone">
 <main class="screen">

  <div class="topbar">
   <div class="brand">✦ MOBILE.APP</div>
   <div class="pill" id="top-time">--:--</div>
  </div>

  <section id="login-page" class="login-wrap">
   <div class="clock-panel">
    <div class="clock-face" id="clock-face">
     <span class="number" style="left:50%;top:13%">12</span>
     <span class="number" style="left:83%;top:50%">3</span>
     <span class="number" style="left:50%;top:87%">6</span>
     <span class="number" style="left:17%;top:50%">9</span>
     <div class="hand hour-hand" id="hour-hand"></div>
     <div class="hand minute-hand" id="minute-hand"></div>
     <div class="hand second-hand" id="second-hand"></div>
     <div class="clock-pin"></div>
    </div>
    <div class="time-info">
     <div class="digital-time" id="digital-time">00:00:00</div>
     <div class="digital-date" id="digital-date">Loading date...</div>
    </div>
   </div>

   <div class="login-title">Welcome</div>
   <h2 style="color:#f5fffc;margin:5px 0">Your space. Your apps.</h2>
   <p class="login-sub">A little world of useful tools, notes and games—made for you.</p>

   <div class="login-actions">
    <button class="primary" onclick="login()">LOGIN</button>
    <button class="secondary" onclick="guestLogin()">EXPLORE AS GUEST</button>
   </div>
   <p class="small-note" style="margin-top:24px">A brighter way to use your phone.</p>
  </section>

  <section id="home-page" class="hidden">
   <div class="section">
    <p style="margin-bottom:5px">WELCOME BACK</p>
    <h1 id="welcome-name">Hello!</h1>
    <p>Your personal mobile space is ready.</p>
   </div>

   <div class="section tile-grid">
    <button class="tile" onclick="openPage('calculator-page')"><span class="emoji">🧮</span><span>Calculator</span></button>
    <button class="tile" onclick="openPage('password-page')"><span class="emoji">🔐</span><span>Password</span></button>
    <button class="tile" onclick="openPage('notes-page')"><span class="emoji">📝</span><span>Notes</span></button>
   </div>

   <div class="section">
    <button class="wide-tile" onclick="openPage('games-page')">
     <span class="wide-icon">🧩</span>
     <span><div class="wide-title">Gaming Hub</div><div class="wide-desc">Play, challenge yourself and enjoy your mini-games collection.</div></span>
     <span style="margin-left:auto;font-size:23px">›</span>
    </button>
   </div>

   <div class="section">
    <button class="row-tile" onclick="openPage('settings-page')"><span class="emoji">⚙️</span><b>Settings</b><span style="margin-left:auto">›</span></button>
    <button class="row-tile" onclick="openPage('about-page')"><span class="emoji">✨</span><b>About</b><span style="margin-left:auto">›</span></button>
    <button class="row-tile school-home-btn" onclick="openPage('school-page')"><span class="emoji">🏫</span><b>About My School</b><span style="margin-left:auto">›</span></button>
    <button class="row-tile" style="background:linear-gradient(110deg,#102d50,#49327e);border-color:#72eaff66" onclick="openPage('breakout-page');breakoutInit()"><span class="emoji">🟣</span><b>NEON BREAKOUT</b><span style="margin-left:auto">›</span></button>
    <button class="row-tile" style="background:linear-gradient(110deg,#062b38,#125a60);border-color:#55dedb77" onclick="openPage('earth-page');earthInit()"><span class="emoji">🌍</span><b>LIVE EARTH 4D</b><span style="margin-left:auto">›</span></button>
    <button class="row-tile logout-btn" onclick="logout()"><span class="emoji">🚪</span><b>Logout</b><span style="margin-left:auto">›</span></button>
   </div>
  </section>

  <section id="breakout-page" class="hidden">
   <div class="page-head"><button class="back" onclick="breakoutStop();goHome()">‹ Back</button><h2>🟣 Neon Breakout</h2></div>
   <div class="nb-hero"><div class="nb-kicker">ARCADE CHALLENGE / SEASON 01</div><h2 style="font-size:24px;margin:8px 0">BREAK THE GRID.</h2><p>Control the energy paddle, smash neon blocks, collect power-ups and clear 30 handcrafted stages.</p><div class="nb-stats"><div class="nb-stat"><b id="nb-score">0</b><small>SCORE</small></div><div class="nb-stat"><b id="nb-lives">3</b><small>LIVES</small></div><div class="nb-stat"><b id="nb-best">0</b><small>BEST</small></div></div></div>
   <h3>⚡ ARCADE ARENA</h3><div class="nb-panel"><canvas id="nb-canvas" width="360" height="520"></canvas><div class="nb-row" style="justify-content:space-between;margin:9px 0"><b id="nb-level-label">LEVEL 01 / 30</b><span id="nb-status" class="nb-status">Tap START to play</span></div><div class="nb-row"><button class="nb-btn" id="nb-start" onclick="breakoutToggle()">START GAME</button><button class="nb-ghost" onclick="breakoutPause()">Ⅱ PAUSE</button><button class="nb-ghost" onclick="breakoutRestart()">↻ RESTART</button></div><p style="margin-bottom:0">Controls: drag your finger across the arena, or use the buttons below.</p><div class="nb-row" style="justify-content:center;margin-top:8px"><button class="nb-ghost" onpointerdown="breakoutMove(-1)" onpointerup="breakoutMove(0)" onpointerleave="breakoutMove(0)">◀ LEFT</button><button class="nb-ghost" onpointerdown="breakoutMove(1)" onpointerup="breakoutMove(0)" onpointerleave="breakoutMove(0)">RIGHT ▶</button></div></div>
   <h3>🧩 STAGE SELECT</h3><div class="nb-panel"><div id="nb-levels" class="nb-levels"></div><p>Clear a stage to unlock the next one. Your unlocked stages and best score are saved on this device.</p></div>
   <h3>✨ POWER-UP GUIDE</h3><div class="nb-panel"><div class="nb-power">🟢 <b>WIDE PADDLE</b> — temporarily increases paddle width.</div><div class="nb-power">🔵 <b>SLOW BALL</b> — slows the ball for easier control.</div><div class="nb-power">🟣 <b>MULTI-BALL</b> — releases extra balls into the arena.</div><div class="nb-power">🟠 <b>LASER</b> — activates a short burst of paddle lasers.</div><p style="margin-bottom:0">Some blocks need two hits. Explosive blocks clear nearby blocks when broken.</p></div>
   <h3>🏆 PROGRESS</h3><div class="nb-panel"><div class="nb-row" style="justify-content:space-between"><b id="nb-progress-label">0 / 30 stages cleared</b><b id="nb-coins">0 ✦</b></div><div style="height:7px;background:#ffffff18;border-radius:20px;overflow:hidden;margin-top:9px"><div id="nb-progress" style="height:100%;width:0;background:linear-gradient(90deg,#4ce7e9,#b16cff)"></div></div></div>
  </section>

  <section id="earth-page" class="hidden">
   <div class="page-head"><button class="back" onclick="earthStop();goHome()">‹ Back</button><h2>🌍 Live Earth</h2></div>
   <div class="earth-hero">
    <div class="earth-kicker"><span class="earth-live-dot"></span>EARTH OBSERVATORY · CONTINUOUS 3D VIEW</div>
    <h2 style="font-size:22px;margin:7px 0 3px">Our planet, in motion.</h2>
    <p style="font-size:11px;color:#a9cbd0;margin:0 0 8px">Drag to rotate · Pinch or use controls to zoom · Animated day/night globe</p>
    <div class="earth-layout"><div id="earth-globe" aria-label="Interactive 3D Earth globe"></div>
     <div class="earth-side">
      <div class="earth-stat"><b id="earth-pop">8.2B</b><small>EST. POPULATION</small></div>
      <div class="earth-stat"><b id="earth-births">+0</b><small>BIRTHS TODAY*</small></div>
      <div class="earth-stat"><b id="earth-deaths">+0</b><small>DEATHS TODAY*</small></div>
      <div class="earth-stat"><b id="earth-clock">--:--:--</b><small>UTC TIME</small></div>
     </div>
    </div>
    <div class="earth-tools"><button class="earth-btn" onclick="earthZoom(1.35)">＋ Zoom in</button><button class="earth-btn" onclick="earthZoom(.74)">－ Zoom out</button><button class="earth-btn" onclick="earthReset()">◎ Reset view</button><button class="earth-btn" id="earth-spin" onclick="earthToggleSpin()">Ⅱ Pause rotation</button></div>
    <p class="earth-note">*Global population and daily births/deaths are model-based estimates, not exact live counts. Country search works with the online country database or a small offline fallback. Globe textures and borders need internet access. “4D” here means animated time, lighting and rotation effects on a 3D globe.</p>
   </div>
   <div class="earth-info"><div class="earth-kicker">COUNTRY EXPLORER</div>
    <div class="earth-search"><input id="earth-country-input" type="search" autocomplete="off" placeholder="Search country or capital…" oninput="earthSearchCountry(this.value)" onkeydown="if(event.key==='Enter')earthChooseFirst()"><button onclick="earthChooseFirst()">SEARCH</button></div>
    <div id="earth-suggest" class="earth-suggest"></div><div id="earth-search-status" class="earth-status">Search by country or capital, or tap a country on the globe.</div>
    <h3 id="earth-country-name" style="margin:7px 0">Select a country</h3><p id="earth-country-desc" style="font-size:12px;color:#b5d2d5;margin:0">Explore country details on the interactive globe.</p>
    <div class="earth-info-grid"><div class="earth-info-cell"><small>REGION</small><b id="earth-region">—</b></div><div class="earth-info-cell"><small>CAPITAL</small><b id="earth-capital">—</b></div><div class="earth-info-cell"><small>POPULATION</small><b id="earth-country-pop">—</b></div><div class="earth-info-cell"><small>AREA</small><b id="earth-country-area">—</b></div></div>
   </div>
  </section>

  <section id="calculator-page" class="hidden">
   <div class="page-head"><button class="back" onclick="goHome()">‹ Back</button><h2>Calculator</h2></div>
   <div class="calc-display" id="calc-display">0</div>
   <div class="calc-grid" id="calc-grid">
    <button class="calc-key clear" onclick="calcClear()">AC</button>
    <button class="calc-key op" onclick="calcInput('%')">%</button>
    <button class="calc-key op" onclick="calcInput('/')">÷</button>
    <button class="calc-key op" onclick="calcInput('*')">×</button>
    <button class="calc-key" onclick="calcInput('7')">7</button>
    <button class="calc-key" onclick="calcInput('8')">8</button>
    <button class="calc-key" onclick="calcInput('9')">9</button>
    <button class="calc-key op" onclick="calcInput('-')">−</button>
    <button class="calc-key" onclick="calcInput('4')">4</button>
    <button class="calc-key" onclick="calcInput('5')">5</button>
    <button class="calc-key" onclick="calcInput('6')">6</button>
    <button class="calc-key op" onclick="calcInput('+')">+</button>
    <button class="calc-key" onclick="calcInput('1')">1</button>
    <button class="calc-key" onclick="calcInput('2')">2</button>
    <button class="calc-key" onclick="calcInput('3')">3</button>
    <button class="calc-key equal" onclick="calcResult()">=</button>
    <button class="calc-key" style="grid-column:span 2" onclick="calcInput('0')">0</button>
    <button class="calc-key" onclick="calcInput('.')">.</button>
    <button class="calc-key" onclick="calcBack()">⌫</button>
   </div>
  </section>

  <section id="password-page" class="hidden">
   <div class="page-head"><button class="back" onclick="goHome()">‹ Back</button><h2>Password Generator</h2></div>
   <div class="card">
    <p>Create a strong random password.</p>
    <label>Password length</label>
    <input class="field" id="pass-length" type="number" min="6" max="40" value="16">
    <button class="primary" onclick="generatePassword()">GENERATE PASSWORD</button>
    <div class="output" id="password-output">Your password appears here.</div>
    <button class="secondary" onclick="copyPassword()">COPY PASSWORD</button>
   </div>
  </section>

  <section id="notes-page" class="hidden">
   <div class="page-head"><button class="back" onclick="goHome()">‹ Back</button><h2>My Notes</h2></div>
   <div class="card">
    <input class="field" id="note-title" placeholder="Note title">
    <textarea class="field" id="note-body" rows="5" placeholder="Write your note..."></textarea>
    <button class="primary" onclick="saveNote()">SAVE NOTE</button>
    <div id="notes-list" style="margin-top:15px"></div>
   </div>
  </section>

  <section id="games-page" class="hidden">
   <div class="page-head"><button class="back" onclick="goHome()">‹ Back</button><h2>Gaming Hub</h2></div>
   <p>Choose a game and enjoy your break.</p>
   <div class="tile-grid">
    <button class="tile" onclick="openPage('guess-page')"><span class="emoji">🔢</span><span>Number Guess</span></button>
    <button class="tile" onclick="openPage('typing-page')"><span class="emoji">⌨️</span><span>Typing Speed</span></button>
    <button class="tile" onclick="openPage('flappy-page')"><span class="emoji">🐦</span><span>Flappy Bird</span></button>
    <button class="tile" onclick="openPage('snake-page')"><span class="emoji">🐍</span><span>Snake</span></button>
    <button class="tile" onclick="openPage('car-page')"><span class="emoji">🏎️</span><span>Car Racing</span></button>
   </div>
  </section>

  <section id="guess-page" class="hidden">
   <div class="page-head"><button class="back" onclick="openPage('games-page')">‹ Games</button><h2>Number Guess</h2></div>
   <div class="card">
    <p>Guess the secret number from 1 to 100. You have 10 chances.</p>
    <input class="field" id="guess-input" type="number" min="1" max="100" placeholder="Your guess">
    <button class="primary" onclick="makeGuess()">GUESS</button>
    <p id="guess-message">10 chances remaining.</p>
    <button class="secondary" onclick="resetGuess()">RESTART GAME</button>
   </div>
  </section>

  <section id="typing-page" class="hidden">
   <div class="page-head"><button class="back" onclick="openPage('games-page')">‹ Games</button><h2>Typing Speed</h2></div>
   <div class="card">
    <p>Type the paragraph accurately before the 60-second timer ends.</p>
    <div id="typing-sentence">Press START to get a random paragraph.</div>
    <div class="typing-stats">
     <div class="typing-stat"><b id="typing-time">60</b><span>SECONDS LEFT</span></div>
     <div class="typing-stat"><b id="typing-live-wpm">0</b><span>LIVE WPM</span></div>
    </div>
    <textarea class="field" id="typing-input" rows="4" placeholder="Press START, then type here..." disabled></textarea>
    <button class="primary" id="typing-start-button" onclick="startTyping()">START NEW TEST</button>
    <div id="typing-results" class="hidden">
     <div class="typing-stats">
      <div class="typing-stat"><b id="typing-final-wpm">0</b><span>WORDS PER MINUTE</span></div>
      <div class="typing-stat"><b id="typing-accuracy">0%</b><span>ACCURACY</span></div>
      <div class="typing-stat"><b id="typing-correct">0</b><span>CORRECT CHARACTERS</span></div>
      <div class="typing-stat"><b id="typing-mistakes">0</b><span>MISTAKES</span></div>
     </div>
     <p id="typing-result"></p>
     <button class="secondary" onclick="startTyping()">TRY ANOTHER PARAGRAPH</button>
    </div>
   </div>
  </section>

  <section id="flappy-page" class="hidden">
   <div class="page-head"><button class="back" onclick="openPage('games-page')">‹ Games</button><h2>Flappy Bird</h2></div>
   <div class="card">
    <p>Tap the game area to flap and avoid the obstacles.</p>
    <canvas id="flappy-canvas" class="game-canvas" width="360" height="460"></canvas>
    <button class="primary" onclick="startFlappy()">PLAY / RESTART</button>
        <p id="flappy-score">Score: 0</p>
   </div>
  </section>

  <section id="snake-page" class="hidden">
   <div class="page-head"><button class="back" onclick="openPage('games-page')">‹ Games</button><h2>Snake</h2></div>
   <div class="card">
    <p>Collect the glowing fruit. Avoid the walls and your tail.</p>
    <canvas id="snake-canvas" class="game-canvas" width="288" height="288"></canvas>
    <div id="snake-controls">
     <button class="empty-control" aria-hidden="true"> </button>
     <button onclick="snakeDirection(0,-1)">⬆️</button>
     <button class="empty-control" aria-hidden="true"> </button>
     <button onclick="snakeDirection(-1,0)">⬅️</button>
     <button onclick="snakeDirection(0,1)">⬇️</button>
     <button onclick="snakeDirection(1,0)">➡️</button>
    </div>
    <button class="primary" onclick="startSnake()">PLAY / RESTART</button>
    <p id="snake-score">Score: 0</p>
   </div>
  </section>

  <section id="car-page" class="hidden">
   <div class="page-head"><button class="back" onclick="openPage('games-page')">‹ Games</button><h2>Car Racing</h2></div>
   <div class="card">
    <p>Swipe left or right to change lanes. Avoid the traffic!</p>
    <div class="car-score">
     <div><b id="car-score">0</b><span>SCORE</span></div>
     <div><b id="car-level">1</b><span>LEVEL</span></div>
     <div><b id="car-speed">1x</b><span>SPEED</span></div>
    </div>
    <canvas id="car-canvas" width="340" height="510"></canvas>
    <div class="car-controls">
     <button onclick="moveCar(-1)">⬅ LEFT</button>
     <button onclick="moveCar(1)">RIGHT ➡</button>
    </div>
    <button class="primary" style="margin-top:12px" onclick="startCarGame()">PLAY / RESTART</button>
    <p id="car-message" class="small-note">Use swipe, arrow keys or A/D to drive.</p>
   </div>
  </section>

  <section id="settings-page" class="hidden">
   <div class="page-head"><button class="back" onclick="goHome()">‹ Back</button><h2>Settings</h2></div>
   <div class="card">
    <label>Your name</label>
    <input class="field" id="setting-name" placeholder="Enter your name">
    <label>Set a PIN (optional)</label>
    <input class="field" id="setting-pin" type="password" maxlength="8" placeholder="Create a PIN">
    <button class="primary" onclick="saveSettings()">SAVE SETTINGS</button>
    <p class="small-note">Your notes and settings are saved on this device.</p>
   </div>
  </section>

  <section id="about-page" class="hidden">
   <div class="page-head"><button class="back" onclick="goHome()">‹ Back</button><h2>About</h2></div>
   <div class="card">
    <h2>✦ mobile.app</h2>
    <p>A personal mini-app space with everyday tools, notes and games.</p>
    <p>Designed with a colorful premium interface and made to work without an AI API.</p>
    <div style="margin-top:18px;padding:13px;border-radius:14px;background:#ffffff15">
     <p style="margin-bottom:8px"><b>Version:</b> 1.0</p>
     <p style="margin-bottom:0"><b>Made by:</b> Kashan Boss</p>
    </div>
   </div>
  </section>

  <section id="school-page" class="hidden school-page" style="--school-bg:url(1000015111.jpg)">
   <div class="school-overlay">
    <div class="page-head"><button class="back" onclick="goHome()">‹ Back</button><h2>About My School</h2></div>
    <div class="school-menu">
     <button class="school-option history-option" onclick="openPage('school-history-page')">📚 &nbsp; History of UPSS <span>›</span></button>
     <button class="school-option mission-option" onclick="openPage('school-mission-page')">🌟 &nbsp; Mission of UPSS <span>›</span></button>
    </div>
   </div>
  </section>

  <section id="school-history-page" class="hidden school-detail history-detail">
   <div class="page-head"><button class="back" onclick="openPage('school-page')">‹ School</button><h2>History of UPSS</h2></div>
   <div class="school-text-card">
    <p>Usman Public School System (UPSS) began its educational journey in 1989. It was established with the aim of providing quality education while keeping Islamic values and character development at the heart of learning.</p>
    <p>From its beginning, the school system has focused on developing students academically, morally and socially. Its educational approach encourages discipline, responsibility, respect and a strong sense of purpose.</p>
    <p>Over the years, UPSS has grown beyond its first campus and expanded its educational work through campuses in Karachi. This growth has helped the school system reach more families and provide learning opportunities to a wider community.</p>
    <p>UPSS places importance on combining contemporary education with Islamic teachings. Along with classroom learning, students are encouraged to build good character, explore knowledge and understand their responsibilities towards society.</p>
    <p>Today, the journey of UPSS continues with an emphasis on education, values and the development of future generations. Its history reflects a continuing effort to prepare students to contribute positively to the Muslim Ummah and the wider world.</p>
   </div>
  </section>

  <section id="school-mission-page" class="hidden school-detail mission-detail">
   <div class="page-head"><button class="back" onclick="openPage('school-page')">‹ School</button><h2>Mission of UPSS</h2></div>
   <div class="school-text-card">
    <h3>Mission</h3>
    <p>To motivate the students in becoming future leaders capable of providing guidance to the Muslim Ummah in all spheres of life and lead the contemporary world in accordance with the teachings of Islam.</p>
    <h3>Vision</h3>
    <p>Nurturing students in becoming future leaders.</p>
    <h3>Core Values</h3>
    <ol>
     <li>Taqwa</li>
     <li>Following Prophet Muhammad (SAW) as a role model</li>
     <li>Research &amp; Explore</li>
     <li>Service of Mankind</li>
     <li>Enjoining Good and Forbidding Evil</li>
     <li>Protection of Ideology of Pakistan</li>
    </ol>
   </div>
  </section>

  <section id="pin-page" class="hidden">
   <div class="login-wrap" style="min-height:650px">
    <h1>Welcome back</h1>
    <p>Enter your PIN to continue.</p>
    <input class="field" id="pin-entry" type="password" placeholder="Enter PIN">
    <button class="primary" onclick="unlockApp()">UNLOCK</button>
    <p id="pin-message"></p>
   </div>
  </section>

 </main>
</div>
"""
APP += r"""
<script>
// ===============================
// MOBILE.APP - MAIN JAVASCRIPT
// ===============================

const $ = id => document.getElementById(id);

const store = {
  get(key, fallback) {
    try {
      const value = localStorage.getItem(key);
      return value === null ? fallback : JSON.parse(value);
    } catch (e) {
      return fallback;
    }
  },
  set(key, value) {
    try {
      localStorage.setItem(key, JSON.stringify(value));
    } catch (e) {}
  }
};

let userName = store.get("mobile_name", "Guest");
let appPin = store.get("mobile_pin", "");
let isGuest = false;
let calcExpression = "";
let secretNumber = 0;
let guessCount = 0;
let guessFinished = false;

let typingStarted = false;
let typingStartTime = 0;
let typingTimer = null;
let typingSeconds = 60;
let typingText = "";
let typingUsed = [];

let flappyTimer = null;
let flappyRunning = false;
let flappyBird = null;
let flappyPipes = [];
let flappyScore = 0;

let snakeFrame = null;
let snakeRunning = false;
let snakeBody = [];
let snakePreviousBody = [];
let snakeFood = null;
let snakeDir = {x:1,y:0};
let snakeNextDir = {x:1,y:0};
let snakePoints = 0;
let snakeLastTime = 0;
let snakeAccumulator = 0;
let snakeStep = 115;
let snakeTouchStart = null;

let carFrame = null;
let carRunning = false;
let carLastTime = 0;
let carPlayerLane = 1;
let carPlayerX = 0;
let carObstacles = [];
let carScore = 0;
let carSpeed = 190;
let carSpawnTimer = 0;
let carRoadOffset = 0;
let carTouchStart = null;

function updateClock() {
  const now = new Date();
    const h = now.getHours();
  const m = now.getMinutes();
  const s = now.getSeconds();

  const hour = (h % 12) * 30 + m * 0.5;
  const minute = m * 6 + s * 0.1;
  const second = s * 6;

  if ($("hour-hand"))
    $("hour-hand").style.transform =
      `translateX(-50%) rotate(${hour}deg)`;

  if ($("minute-hand"))
    $("minute-hand").style.transform =
      `translateX(-50%) rotate(${minute}deg)`;

  if ($("second-hand"))
    $("second-hand").style.transform =
      `translateX(-50%) rotate(${second}deg)`;

  const time = now.toLocaleTimeString([], {
    hour:"2-digit", minute:"2-digit", second:"2-digit"
  });

  if ($("digital-time")) $("digital-time").textContent = time;

  if ($("top-time")) {
    $("top-time").textContent = now.toLocaleTimeString([], {
      hour:"2-digit", minute:"2-digit"
    });
  }

  if ($("digital-date")) {
    $("digital-date").textContent = now.toLocaleDateString([], {
      weekday:"long", day:"numeric", month:"long", year:"numeric"
    });
  }
}

updateClock();
setInterval(updateClock, 1000);

// PAGE NAVIGATION

const pages = [
  "login-page","home-page","calculator-page","password-page",
  "notes-page","games-page","guess-page","typing-page",
  "flappy-page","snake-page","car-page","settings-page",
  "about-page","school-page","school-history-page","school-mission-page","breakout-page","earth-page","pin-page"
];

function stopFlappy() {
  if (flappyTimer !== null) {
    clearInterval(flappyTimer);
    flappyTimer = null;
  }
  flappyRunning = false;
}

function stopSnake() {
  if (snakeFrame !== null) {
    cancelAnimationFrame(snakeFrame);
    snakeFrame = null;
  }
  snakeRunning = false;
}

function stopTyping() {
  if (typingTimer !== null) {
    clearInterval(typingTimer);
    typingTimer = null;
  }
  typingStarted = false;
}

function stopCar() {
  if (carFrame !== null) {
    cancelAnimationFrame(carFrame);
    carFrame = null;
  }
  carRunning = false;
}

function showPage(id) {
  stopFlappy();
  stopSnake();
  stopTyping();
  stopCar();

  pages.forEach(page => {
    const el = $(page);
    if (el) el.classList.toggle("hidden", page !== id);
  });

  if (id === "notes-page") renderNotes();

  if (id === "settings-page") {
    $("setting-name").value = store.get("mobile_name", "Guest");
    $("setting-pin").value = "";
  }

  if (id === "flappy-page") drawFlappy();
  if (id === "snake-page") drawSnake();
  if (id === "car-page") drawCar();
}

function openPage(id) {
  showPage(id);
}

function goHome() {
  if (appPin && !isGuest) {
    showPage("pin-page");
    return;
  }
  showPage("home-page");
}

// LOGIN / LOGOUT

function login() {
  isGuest = false;

  if (appPin) {
    showPage("pin-page");
    return;
  }

  enterHome();
}

function guestLogin() {
  isGuest = true;
  userName = "Guest";
  enterHome();
}

function enterHome() {
  $("welcome-name").textContent = "Hello, " + userName + "!";
  showPage("home-page");
}

function logout() {
  stopFlappy();
  stopSnake();
  stopTyping();
  stopCar();

  isGuest = false;
  $("pin-entry").value = "";
  $("pin-message").textContent = "";
  showPage("login-page");
}

function unlockApp() {
  const entered = $("pin-entry").value;

  if (entered === appPin) {
    $("pin-entry").value = "";
    $("pin-message").textContent = "";
    enterHome();
  } else {
    $("pin-message").textContent = "Incorrect PIN. Try again.";
  }
}

// CALCULATOR

function calcUpdate() {
  $("calc-display").textContent = calcExpression || "0";
}

function calcInput(value) {
  if (calcExpression.length > 35) return;

  if (calcExpression === "Error") calcExpression = "";

  calcExpression += value;
  calcUpdate();
}

function calcClear() {
  calcExpression = "";
  calcUpdate();
}

function calcBack() {
  calcExpression = calcExpression.slice(0, -1);
  calcUpdate();
}

function calcResult() {
  try {
    if (
      !calcExpression ||
      !/^[0-9+\-*/%.() ]+$/.test(calcExpression)
    ) throw Error();

    const result = Function(
      '"use strict";return (' + calcExpression + ')'
    )();

    if (!Number.isFinite(result)) throw Error();

    calcExpression = String(Number(result.toFixed(10)));
  } catch (e) {
    calcExpression = "Error";
  }

  calcUpdate();
}

// PASSWORD GENERATOR

function generatePassword() {
  let length = parseInt($("pass-length").value, 10);

  if (!Number.isFinite(length)) length = 16;
  length = Math.max(6, Math.min(40, length));

  $("pass-length").value = length;

  const chars =
    "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz23456789!@#$%&*?";

  let result = "";
  const random = new Uint32Array(length);

  if (window.crypto && window.crypto.getRandomValues) {
    window.crypto.getRandomValues(random);
  } else {
    for (let i = 0; i < length; i++) {
      random[i] = Math.floor(Math.random() * 100000);
    }
  }

  for (let i = 0; i < length; i++) {
    result += chars[random[i] % chars.length];
  }

  $("password-output").textContent = result;
}

async function copyPassword() {
  const value = $("password-output").textContent;

  if (!value || value === "Your password appears here.") return;

  try {
    await navigator.clipboard.writeText(value);
    $("password-output").textContent = value + "  ✓ Copied";
  } catch (e) {
    $("password-output").textContent = value + "  (Select to copy)";
  }
}

// NOTES

function getNotes() {
  return store.get("mobile_notes", []);
}

function saveNote() {
  const title = $("note-title").value.trim();
  const body = $("note-body").value.trim();

  if (!title && !body) return;

  const notes = getNotes();

  notes.unshift({
    id: Date.now(),
    title: title || "Untitled",
    body
  });

  store.set("mobile_notes", notes);

  $("note-title").value = "";
  $("note-body").value = "";

  renderNotes();
}

function renderNotes() {
  const notes = getNotes();
  $("notes-list").innerHTML = "";

  if (!notes.length) {
    $("notes-list").innerHTML =
      '<p class="small-note">No notes yet. Create your first note.</p>';
    return;
  }

  notes.forEach(note => {
    const card = document.createElement("div");
    card.className = "card";
    card.style.marginBottom = "10px";

    const heading = document.createElement("h3");
    heading.textContent = note.title;

    const content = document.createElement("p");
    content.textContent = note.body;

    const remove = document.createElement("button");
    remove.className = "secondary";
    remove.textContent = "DELETE";

    remove.onclick = () => {
      store.set(
        "mobile_notes",
        getNotes().filter(n => n.id !== note.id)
      );
      renderNotes();
    };

    card.append(heading, content, remove);
    $("notes-list").appendChild(card);
  });
}

// SETTINGS

function saveSettings() {
  const name = $("setting-name").value.trim() || "Guest";
  const pin = $("setting-pin").value.trim();

  if (pin && !/^\d{4,8}$/.test(pin)) {
    alert("PIN must contain 4 to 8 digits.");
    return;
  }

  userName = name;
  appPin = pin;

  store.set("mobile_name", name);
  store.set("mobile_pin", pin);

  $("welcome-name").textContent = "Hello, " + userName + "!";

  alert("Settings saved successfully.");
  goHome();
}

// NUMBER GUESSING GAME

function resetGuess() {
  secretNumber = Math.floor(Math.random() * 100) + 1;
  guessCount = 0;
  guessFinished = false;

  $("guess-input").value = "";
  $("guess-message").textContent =
    "10 chances remaining. Guess from 1 to 100.";
}

function makeGuess() {
  if (guessFinished) return;

  const guess = Number($("guess-input").value);

  if (!Number.isInteger(guess) || guess < 1 || guess > 100) {
    $("guess-message").textContent =
      "Enter a number from 1 to 100.";
    return;
  }

  guessCount++;
  const remaining = 10 - guessCount;

  if (guess === secretNumber) {
    $("guess-message").textContent =
      "🎉 Correct! You guessed it in " + guessCount + " attempts.";
    guessFinished = true;
  } else if (guessCount >= 10) {
    $("guess-message").textContent =
      "Game over! The number was " + secretNumber + ".";
    guessFinished = true;
  } else {
    $("guess-message").textContent =
      (guess < secretNumber
        ? "Too low! Try higher."
        : "Too high! Try lower.") +
      " " + remaining + " chances left.";
  }

  $("guess-input").value = "";
}

// TYPING SPEED GAME

const typingParagraphs = [
  "Technology has changed the way people communicate, learn and work. Every day, new ideas and inventions make life more connected. Learning how to use these tools wisely can help us become more creative and productive.",
  "Success is not always about doing something quickly. It is about staying consistent, learning from mistakes and improving a little every day. Small efforts can create meaningful results over time.",
  "A peaceful morning can make the entire day feel better. Fresh air, a clear mind and a positive attitude help us focus on important tasks. Good habits often begin with simple daily actions.",
  "Reading is a powerful way to explore new ideas and understand the world. Books introduce us to different people, places and experiences. Even a few minutes of reading can improve knowledge and vocabulary.",
  "The world around us is full of interesting discoveries. Science helps us understand nature, space, energy and the human body. Asking questions and exploring answers is an important part of learning.",
  "Time is valuable, so it is important to use it carefully. Planning our tasks can reduce stress and help us achieve our goals. A balanced routine also leaves room for rest and enjoyment.",
  "Good communication is an important skill in everyday life. Listening carefully, choosing clear words and respecting other opinions can make conversations more meaningful. Practice helps people express ideas with confidence.",
  "Nature gives us beautiful landscapes, fresh air and many useful resources. Protecting the environment is a shared responsibility. Simple actions such as saving water and reducing waste can make a difference.",
  "Every challenge gives us a chance to learn something new. Instead of giving up when a task becomes difficult, we can try another approach. Patience and practice help us move forward.",
  "A healthy routine includes enough sleep, regular movement and balanced meals. These habits support concentration and energy throughout the day. Taking care of ourselves helps us enjoy everyday activities."
];

function getRandomTypingParagraph() {
  let available = typingParagraphs
    .map((p, i) => i)
    .filter(i => !typingUsed.includes(i));

  if (!available.length) {
    typingUsed = [];
    available = typingParagraphs.map((p, i) => i);
  }

  const selected =
    available[Math.floor(Math.random() * available.length)];

  typingUsed.push(selected);
  return typingParagraphs[selected];
}

function startTyping() {
  stopTyping();

  typingText = getRandomTypingParagraph();
  typingSeconds = 60;
  typingStarted = true;
  typingStartTime = Date.now();

  $("typing-sentence").textContent = typingText;
  $("typing-input").value = "";
  $("typing-input").disabled = false;
  $("typing-input").focus();

  $("typing-time").textContent = "60";
  $("typing-live-wpm").textContent = "0";
  $("typing-results").classList.add("hidden");
  $("typing-result").textContent = "";
  $("typing-start-button").textContent = "RESTART TEST";

  $("typing-input").oninput = updateTypingProgress;

  typingTimer = setInterval(() => {
    const elapsed = Math.floor(
      (Date.now() - typingStartTime) / 1000
    );

    typingSeconds = Math.max(0, 60 - elapsed);
    $("typing-time").textContent = typingSeconds;

    updateTypingStats();

    if (typingSeconds <= 0) finishTyping();
  }, 250);
}

function getTypingStats() {
  const typed = $("typing-input").value;
  let correct = 0;
  let mistakes = 0;

  for (let i = 0; i < typed.length; i++) {
    if (typed[i] === typingText[i]) correct++;
    else mistakes++;
  }

  const total = typed.length;
  const accuracy = total ? Math.round(correct / total * 100) : 0;
  const elapsed = Math.max(
    1,
    (Date.now() - typingStartTime) / 1000
  );

  const wpm = Math.round((correct / 5) / (elapsed / 60));

  return {typed, correct, mistakes, total, accuracy, wpm};
}

function updateTypingStats() {
  if (!typingStarted) return;

  const stats = getTypingStats();
  $("typing-live-wpm").textContent = stats.wpm;
}

function updateTypingProgress() {
  if (!typingStarted) return;

  const stats = getTypingStats();
  $("typing-live-wpm").textContent = stats.wpm;

  if (stats.typed === typingText) finishTyping();
}

function finishTyping() {
  if (!typingStarted) return;

  const stats = getTypingStats();
  stopTyping();

  $("typing-input").disabled = true;
  $("typing-time").textContent = "0";

  $("typing-final-wpm").textContent = stats.wpm;
  $("typing-accuracy").textContent = stats.accuracy + "%";
  $("typing-correct").textContent = stats.correct;
  $("typing-mistakes").textContent = stats.mistakes;

  $("typing-result").textContent =
    stats.typed === typingText
      ? "Paragraph completed! Excellent work."
      : "Time is up! Here is your result.";

  $("typing-results").classList.remove("hidden");
  $("typing-start-button").textContent = "START NEW TEST";
}

// FLAPPY BIRD

const fc = $("flappy-canvas");
const fx = fc.getContext("2d");

function drawFlappy() {
  const w = fc.width;
  const h = fc.height;

  const sky = fx.createLinearGradient(0, 0, 0, h);
  sky.addColorStop(0, "#51c9f5");
  sky.addColorStop(1, "#d3f7ff");

  fx.fillStyle = sky;
  fx.fillRect(0, 0, w, h);

  fx.fillStyle = "#ffffff99";

  [[55,65,20],[175,105,27],[285,55,23]].forEach(([x,y,r]) => {
    fx.beginPath();
    fx.arc(x, y, r, 0, Math.PI * 2);
    fx.arc(x + r, y - 8, r * 0.8, 0, Math.PI * 2);
    fx.arc(x + r * 2, y, r, 0, Math.PI * 2);
    fx.fill();
  });

  fx.fillStyle = "#75d68b";
  fx.fillRect(0, h - 35, w, 35);

  fx.fillStyle = "#3eae74";
  fx.fillRect(0, h - 35, w, 7);

  if (flappyBird) {
    fx.save();
    fx.translate(flappyBird.x, flappyBird.y);
    fx.rotate(
      Math.max(-0.45, Math.min(0.65, flappyBird.velocity * 0.055))
    );

    fx.fillStyle = "#ffd447";
    fx.beginPath();
    fx.ellipse(0, 0, 16, 12, 0, 0, Math.PI * 2);
    fx.fill();

    fx.fillStyle = "#f3a928";
    fx.beginPath();
    fx.ellipse(-5, Math.sin(Date.now() / 65) * 4, 9, 5, -0.3, 0, Math.PI * 2);
    fx.fill();

    fx.fillStyle = "#ed9c30";
    fx.beginPath();
    fx.moveTo(-13, -2);
    fx.lineTo(-21, -8);
    fx.lineTo(-19, 2);
    fx.closePath();
    fx.fill();

    fx.fillStyle = "#fff";
    fx.beginPath();
    fx.arc(7, -6, 5, 0, Math.PI * 2);
    fx.fill();

    fx.fillStyle = "#172c42";
    fx.beginPath();
    fx.arc(9, -6, 2.2, 0, Math.PI * 2);
    fx.fill();

    fx.fillStyle = "#f07836";
    fx.beginPath();
    fx.moveTo(14, -1);
    fx.lineTo(25, 3);
    fx.lineTo(14, 6);
    fx.closePath();
    fx.fill();

    fx.restore();
  }

  flappyPipes.forEach(p => {
    const gradient = fx.createLinearGradient(p.x, 0, p.x + 48, 0);
    gradient.addColorStop(0, "#168b77");
    gradient.addColorStop(0.5, "#43d5a1");
    gradient.addColorStop(1, "#137b70");

    fx.fillStyle = gradient;
    fx.fillRect(p.x, 0, 48, p.top);
    fx.fillRect(p.x, p.top - 12, 48, 12);
    fx.fillRect(p.x, p.bottom, 48, h - p.bottom - 35);
    fx.fillRect(p.x, p.bottom, 48, 12);
  });

  if (!flappyRunning) {
    fx.fillStyle = "#174b61";
    fx.textAlign = "center";
    fx.font = "bold 19px Arial";
    fx.fillText("Tap PLAY to start", w / 2, h / 2);
  }
}

function startFlappy() {
  stopFlappy();

  flappyBird = {x:80, y:200, velocity:0};
  flappyPipes = [];
  flappyScore = 0;

  $("flappy-score").textContent = "Score: 0";
  flappyRunning = true;

  let frame = 0;

  flappyTimer = setInterval(() => {
    if (!flappyRunning) return;

    frame++;

    flappyBird.velocity += 0.45;
    flappyBird.y += flappyBird.velocity;

    if (frame % 68 === 0) {
      const top = 55 + Math.random() * 135;

      flappyPipes.push({
        x:fc.width,
        top,
        bottom:top + 82,
        passed:false
      });
    }

    flappyPipes.forEach(p => {
      p.x -= 4.2;

      if (!p.passed && p.x + 48 < flappyBird.x) {
        p.passed = true;
        flappyScore++;
        $("flappy-score").textContent = "Score: " + flappyScore;
      }

      const overlaps =
        flappyBird.x + 11 > p.x &&
        flappyBird.x - 11 < p.x + 48;

      const hitsPipe =
        flappyBird.y - 11 < p.top ||
        flappyBird.y + 11 > p.bottom;

      if (overlaps && hitsPipe) endFlappy();
    });

    flappyPipes = flappyPipes.filter(p => p.x > -55);

    if (
          flappyBird.y > fc.height - 48 ||
      flappyBird.y < 10
    ) endFlappy();

    drawFlappy();
  }, 25);
}

function flap() {
  if (!flappyRunning) return;
  flappyBird.velocity = -6.8;
}

function endFlappy() {
  if (!flappyRunning) return;

  stopFlappy();
  drawFlappy();

  $("flappy-score").textContent =
    "Game over! Score: " + flappyScore;
}

fc.addEventListener("pointerdown", flap);

// SNAKE

const sc = $("snake-canvas");
const sx = sc.getContext("2d");
const cell = 20;
const gridSize = 14;

function newSnakeFood() {
  let point;

  do {
    point = {
      x:Math.floor(Math.random() * gridSize),
      y:Math.floor(Math.random() * gridSize)
    };
  } while (
    snakeBody.some(p => p.x === point.x && p.y === point.y)
  );

  return point;
}

function resetSnake() {
  stopSnake();

  snakeBody = [
    {x:5,y:7},
    {x:4,y:7},
    {x:3,y:7}
  ];
  snakePreviousBody = snakeBody.map(p => ({...p}));

  snakeDir = {x:1,y:0};
  snakeNextDir = {x:1,y:0};
  snakeFood = newSnakeFood();
  snakePoints = 0;
  snakeStep = 115;
  snakeAccumulator = 0;
  snakeLastTime = 0;

  $("snake-score").textContent = "Score: 0";
  drawSnake();
}

function drawSnake() {
  const w = sc.width;
  const h = sc.height;

  // Calm, layered green garden background.
  const bg = sx.createLinearGradient(0, 0, w, h);
  bg.addColorStop(0, "#174b3b");
  bg.addColorStop(0.52, "#0d684d");
  bg.addColorStop(1, "#123b50");
  sx.fillStyle = bg;
  sx.fillRect(0, 0, w, h);

  // Subtle leafy shapes add texture without a distracting dotted grid.
  sx.save();
  sx.globalAlpha = 0.12;
  for (let i = 0; i < 14; i++) {
    const x = (i * 47 + 19) % w;
    const y = (i * 71 + 13) % h;
    sx.fillStyle = i % 2 ? "#c4ffcf" : "#69e6b0";
    sx.beginPath();
    sx.ellipse(x, y, 18, 6, -0.6, 0, Math.PI * 2);
    sx.fill();
  }
  sx.restore();

  // Interpolate between grid steps so the snake glides instead of jumping.
  const progress = snakeRunning ? Math.min(1, snakeAccumulator / snakeStep) : 1;
  const points = snakeBody.map((p, i) => {
    const old = snakePreviousBody[i] || p;
    return {
      x: (old.x + (p.x - old.x) * progress) * cell + cell / 2,
      y: (old.y + (p.y - old.y) * progress) * cell + cell / 2
    };
  });

  // Small, clearly visible apple.
  if (snakeFood) {
    const fx = snakeFood.x * cell + cell / 2;
    const fy = snakeFood.y * cell + cell / 2;
    sx.save();
    sx.shadowColor = "#ff4355";
    sx.shadowBlur = 8;
    sx.fillStyle = "#ff4055";
    sx.beginPath();
    sx.arc(fx - 3, fy + 1, 5, 0, Math.PI * 2);
    sx.arc(fx + 3, fy + 1, 5, 0, Math.PI * 2);
    sx.fill();
    sx.shadowBlur = 0;
    sx.strokeStyle = "#74452a";
    sx.lineWidth = 1.5;
    sx.beginPath();
    sx.moveTo(fx, fy - 3);
    sx.lineTo(fx + 1, fy - 8);
    sx.stroke();
    sx.fillStyle = "#9cff9c";
    sx.beginPath();
    sx.ellipse(fx + 4, fy - 6, 3, 1.7, -0.5, 0, Math.PI * 2);
    sx.fill();
    sx.restore();
  }

  // Continuous rounded snake body, not separate dotted blocks.
  if (points.length > 1) {
    sx.save();
    sx.lineCap = "round";
    sx.lineJoin = "round";
    sx.strokeStyle = "#f3ad35";
    sx.lineWidth = 14;
    sx.beginPath();
    points.forEach((point, i) => {
      if (i === 0) sx.moveTo(point.x, point.y);
      else sx.lineTo(point.x, point.y);
    });
    sx.stroke();
    sx.strokeStyle = "#ffd36b";
    sx.lineWidth = 9;
    sx.stroke();
    sx.restore();
  }

  // Distinct head, eyes and a small mouth.
  if (points.length) {
    const head = points[0];
    sx.save();
    sx.translate(head.x, head.y);
    const angle = Math.atan2(snakeDir.y, snakeDir.x);
    sx.rotate(angle);
    sx.fillStyle = "#fff0a6";
    sx.beginPath();
    sx.arc(0, 0, 8, 0, Math.PI * 2);
    sx.fill();
    sx.fillStyle = "#17352b";
    sx.beginPath();
    sx.arc(2, -3, 1.5, 0, Math.PI * 2);
    sx.arc(2, 3, 1.5, 0, Math.PI * 2);
    sx.fill();
    sx.strokeStyle = "#9b3c36";
    sx.lineWidth = 1.5;
    sx.beginPath();
    sx.moveTo(5, 0);
    sx.lineTo(9, 0);
    sx.stroke();
    sx.restore();
  }

  if (!snakeRunning) {
    sx.fillStyle = "#fff";
    sx.textAlign = "center";
    sx.font = "bold 16px Arial";
    sx.fillText("Press PLAY to start", w / 2, h / 2);
  }
}
function snakeMove() {
  snakePreviousBody = snakeBody.map(p => ({...p}));
  snakeDir = {...snakeNextDir};

  const head = {
    x:snakeBody[0].x + snakeDir.x,
    y:snakeBody[0].y + snakeDir.y
  };

  const eating =
    head.x === snakeFood.x &&
    head.y === snakeFood.y;

  const bodyToCheck = eating
    ? snakeBody
    : snakeBody.slice(0, -1);

  if (
    head.x < 0 || head.y < 0 ||
    head.x >= gridSize || head.y >= gridSize ||
    bodyToCheck.some(p => p.x === head.x && p.y === head.y)
  ) {
    stopSnake();
    $("snake-score").textContent =
      "Game over! Score: " + snakePoints;
    drawSnake();
    return;
  }

  snakeBody.unshift(head);

  if (eating) {
    snakePoints++;
    snakeFood = newSnakeFood();

    $("snake-score").textContent = "Score: " + snakePoints;
    snakeStep = Math.max(65, 115 - snakePoints * 3);
  } else {
    snakeBody.pop();
  }

  drawSnake();
}

function snakeAnimation(timestamp) {
  if (!snakeRunning) return;

  if (!snakeLastTime) snakeLastTime = timestamp;

  const delta = Math.min(timestamp - snakeLastTime, 50);
  snakeLastTime = timestamp;
  snakeAccumulator += delta;

  while (snakeAccumulator >= snakeStep && snakeRunning) {
    snakeAccumulator -= snakeStep;
    snakeMove();
  }

  if (snakeRunning) {
    snakeFrame = requestAnimationFrame(snakeAnimation);
  }
}

function startSnake() {
  resetSnake();

  snakeRunning = true;
  drawSnake();

  snakeFrame = requestAnimationFrame(snakeAnimation);
}

function snakeDirection(x, y) {
  if (!snakeRunning) return;

  if (x === -snakeDir.x && y === -snakeDir.y) return;

  snakeNextDir = {x,y};
}

sc.addEventListener("touchstart", e => {
  const t = e.touches[0];
  snakeTouchStart = {x:t.clientX,y:t.clientY};
}, {passive:true});

sc.addEventListener("touchmove", e => {
  if (snakeTouchStart) e.preventDefault();
}, {passive:false});

sc.addEventListener("touchend", e => {
  if (!snakeTouchStart) return;

  const t = e.changedTouches[0];
  const dx = t.clientX - snakeTouchStart.x;
  const dy = t.clientY - snakeTouchStart.y;

  if (Math.max(Math.abs(dx), Math.abs(dy)) > 20) {
    if (Math.abs(dx) > Math.abs(dy)) {
      snakeDirection(dx > 0 ? 1 : -1, 0);
    } else {
      snakeDirection(0, dy > 0 ? 1 : -1);
    }
  }

  snakeTouchStart = null;
}, {passive:true});

// CAR RACING GAME

const cc = $("car-canvas");
const cx = cc.getContext("2d");

const carRoad = {
  left:35,
  right:305,
  width:270,
  laneWidth:90
};

function carLaneX(lane) {
  return carRoad.left + carRoad.laneWidth * lane +
    carRoad.laneWidth / 2;
}

// Keep the player's car centered on the road before the game starts.
carPlayerX = carLaneX(1);

function drawCarVehicle(ctx, x, y, color, scale=1) {
  ctx.save();
  ctx.translate(x, y);
  ctx.scale(scale, scale);

  ctx.fillStyle = "#111d20";
  ctx.fillRect(-15, -25, 30, 52);

  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.roundRect(-12, -25, 24, 50, 7);
  ctx.fill();

  ctx.fillStyle = "#bdefff";
  ctx.fillRect(-9, -16, 18, 10);

  ctx.fillStyle = "#263b43";
  ctx.fillRect(-9, 5, 18, 9);

  ctx.fillStyle = "#fff4bb";
  ctx.fillRect(-10, -23, 5, 4);
  ctx.fillRect(5, -23, 5, 4);

  ctx.fillStyle = "#f65d5d";
  ctx.fillRect(-10, 20, 5, 4);
  ctx.fillRect(5, 20, 5, 4);

  ctx.restore();
}

function drawCar() {
  const w = cc.width;
  const h = cc.height;

  cx.fillStyle = "#286b4d";
  cx.fillRect(0, 0, w, h);

  // Road
  cx.fillStyle = "#343b42";
  cx.fillRect(carRoad.left, 0, carRoad.width, h);

  // Road edges
  cx.fillStyle = "#f4f1d4";
  cx.fillRect(carRoad.left - 5, 0, 5, h);
  cx.fillRect(carRoad.right, 0, 5, h);

  // Roadside stripes
  for (let y = -50; y < h + 50; y += 65) {
    const offset = carRoadOffset % 65;

    cx.fillStyle = "#f5d66b";
    cx.fillRect(10, y + offset, 12, 27);
    cx.fillRect(318, y + offset, 12, 27);

    cx.fillStyle = "#19543e";
    cx.beginPath();
    cx.arc(16, y + offset - 15, 10, 0, Math.PI * 2);
    cx.arc(324, y + offset - 15, 10, 0, Math.PI * 2);
    cx.fill();
  }

  // Lane markings
  cx.fillStyle = "#ffffffaa";

  for (let lane = 1; lane <= 2; lane++) {
    const x = carRoad.left + lane * carRoad.laneWidth - 2;

    for (let y = -70; y < h + 70; y += 85) {
      cx.fillRect(x, y + (carRoadOffset % 85), 4, 42);
    }
  }

  // Traffic
  carObstacles.forEach(obstacle => {
    drawCarVehicle(
      cx,
      obstacle.x,
      obstacle.y,
      obstacle.color,
      0.95
    );
  });

  // Player car
  drawCarVehicle(
    cx,
    carPlayerX,
    365,
    "#45d9ff",
    1.12
  );

  if (!carRunning) {
    cx.fillStyle = "#ffffff";
    cx.textAlign = "center";
    cx.font = "bold 19px Arial";
    cx.fillText("Tap PLAY to start", w / 2, 250);
  }
}

function updateCarScore() {
  $("car-score").textContent = Math.floor(carScore);
  $("car-level").textContent =
    Math.floor(carScore / 10) + 1;

  $("car-speed").textContent =
    (carSpeed / 190).toFixed(1) + "x";
}

function moveCar(direction) {
  if (!carRunning) return;

  carPlayerLane = Math.max(
    0,
    Math.min(2, carPlayerLane + direction)
  );

  carPlayerX = carLaneX(carPlayerLane);
  drawCar();
}

function startCarGame() {
  stopCar();

  carRunning = true;
  carPlayerLane = 1;
  carPlayerX = carLaneX(1);
  carObstacles = [];
  carScore = 0;
  carSpeed = 320;
  carSpawnTimer = 0;
  carRoadOffset = 0;
  carLastTime = 0;

  $("car-message").textContent =
    "Use swipe, arrow keys or A/D to drive.";

  updateCarScore();
  drawCar();

  carFrame = requestAnimationFrame(carAnimation);
}

function carAnimation(timestamp) {
  if (!carRunning) return;

  if (!carLastTime) carLastTime = timestamp;

  const delta = Math.min((timestamp - carLastTime) / 1000, 0.05);
  carLastTime = timestamp;

  carScore += delta * 2;
  carSpeed = Math.min(620, 320 + carScore * 5.0);
  carRoadOffset += carSpeed * delta;

  carSpawnTimer += delta;

  if (carSpawnTimer >= Math.max(0.32, 0.68 - carScore * 0.005)) {
    carSpawnTimer = 0;

    const lane = Math.floor(Math.random() * 3);

    carObstacles.push({
      lane,
      x:carLaneX(lane),
      y:-45,
      color:["#ff765f","#ffd166","#b28cff","#f1f4f5"][
        Math.floor(Math.random() * 4)
      ]
    });
  }

  carObstacles.forEach(obstacle => {
    obstacle.y += carSpeed * delta;

    const closeX = Math.abs(obstacle.x - carPlayerX) < 30;
    const closeY = Math.abs(obstacle.y - 365) < 42;

    if (closeX && closeY) {
      endCarGame();
    }
  });

  carObstacles = carObstacles.filter(
    obstacle => obstacle.y < cc.height + 60
  );

  updateCarScore();
  drawCar();

  if (carRunning) {
    carFrame = requestAnimationFrame(carAnimation);
  }
}

function endCarGame() {
  if (!carRunning) return;

  stopCar();

  $("car-message").textContent =
    "Game over! Final score: " + Math.floor(carScore) +
    ". Press PLAY to try again.";

  drawCar();
}

cc.addEventListener("pointerdown", e => {
  carTouchStart = {x:e.clientX,y:e.clientY};
}, {passive:true});

cc.addEventListener("pointerup", e => {
  if (!carTouchStart) return;

  const dx = e.clientX - carTouchStart.x;
  const dy = e.clientY - carTouchStart.y;

  if (!carRunning) {
    if (Math.max(Math.abs(dx), Math.abs(dy)) <= 20) {
      startCarGame();
    }
  } else if (Math.abs(dx) > 20) {
    moveCar(dx > 0 ? 1 : -1);
  }

  carTouchStart = null;
});

cc.addEventListener("pointercancel", () => {
  carTouchStart = null;
});

document.addEventListener("keydown", e => {
  if (!$("car-page") || $("car-page").classList.contains("hidden")) {
    return;
  }

  if (
    e.key === "ArrowLeft" ||
    e.key === "a" ||
    e.key === "A"
  ) {
    e.preventDefault();
    moveCar(-1);
  }

  if (
    e.key === "ArrowRight" ||
    e.key === "d" ||
    e.key === "D"
  ) {
    e.preventDefault();
    moveCar(1);
  }
});


// ================= NEON BREAKOUT: COMPLETE GAME SYSTEM =================
// ================= NEON BREAKOUT GAME =================
const nbCanvas=document.getElementById('nb-canvas');
const nbCtx=nbCanvas?nbCanvas.getContext('2d'):null;
const NB_W=360,NB_H=520,NB_LEVELS=30;
const nbColors=['#4de9e9','#8d78ff','#ff69b4','#ffb45d','#83f28f'];
let nbSave=nbLoad(),nbRunning=false,nbPaused=false,nbFrame=0,nbLast=0,nbPaddle={x:150,w:60},nbBalls=[],nbBricks=[],nbDrops=[],nbLasers=[],nbScore=0,nbLives=3,nbLevel=1,nbCoins=nbSave.coins,nbMove=0,nbEffects={wide:0,slow:0,laser:0},nbPointer=null,nbMessage='Tap START to play',nbLevelWon=false;
function nbLoad(){try{const d=JSON.parse(localStorage.getItem('mobile_neon_breakout_v1')||'{}');return {best:Number(d.best)||0,unlocked:Math.max(1,Math.min(30,Number(d.unlocked)||1)),cleared:Array.isArray(d.cleared)?d.cleared:[],coins:Number(d.coins)||0};}catch(e){return {best:0,unlocked:1,cleared:[],coins:0};}}
function nbPersist(){try{localStorage.setItem('mobile_neon_breakout_v1',JSON.stringify(nbSave));}catch(e){}nbRenderMeta();}
function nbRenderMeta(){const el=id=>document.getElementById(id);if(!el('nb-best'))return;el('nb-best').textContent=nbSave.best;el('nb-coins').textContent=nbSave.coins+' ✦';el('nb-progress-label').textContent=nbSave.cleared.length+' / 30 stages cleared';el('nb-progress').style.width=(nbSave.cleared.length/30*100)+'%';el('nb-levels').innerHTML=Array.from({length:30},(_,i)=>'<button class="nb-level '+(i+1===nbLevel?'current':'')+'" '+(i+1>nbSave.unlocked?'disabled':'')+' onclick="breakoutSetLevel('+(i+1)+')">'+String(i+1).padStart(2,'0')+'</button>').join('');}
function nbResetStage(){nbPaddle={x:150,w:nbEffects.wide>0?92:60};nbBalls=[{x:180,y:455,vx:2.3,vy:-3.5,r:6,stuck:true}];nbDrops=[];nbLasers=[];nbLevelWon=false;nbBricks=[];const rows=3+Math.min(4,Math.floor((nbLevel-1)/5)),cols=8;for(let r=0;r<rows;r++)for(let c=0;c<cols;c++){let pattern=(r*7+c*3+nbLevel)%11;if(nbLevel%4===0&&pattern===0)continue;nbBricks.push({x:9+c*43,y:65+r*25,w:39,h:18,hp:pattern===1?2:1,max:pattern===1?2:1,color:nbColors[(r+c+nbLevel)%nbColors.length],type:pattern===0?'explosive':'normal'});}}
function breakoutInit(){nbRenderMeta();nbDraw();}
function breakoutSetLevel(n){if(n>nbSave.unlocked)return;breakoutStop();nbLevel=n;nbScore=0;nbLives=3;nbEffects={wide:0,slow:0,laser:0};nbResetStage();nbMessage='Level '+n+' ready';nbUpdateHud();nbDraw();nbRenderMeta();}
function breakoutToggle(){if(nbRunning){breakoutPause();return;}if(nbLevelWon){breakoutNext();return;}if(!nbBalls.length||nbLives<=0)breakoutRestart();nbRunning=true;nbPaused=false;nbMessage='Game running';document.getElementById('nb-start').textContent='RUNNING';nbLast=0;nbFrame=requestAnimationFrame(breakoutLoop);nbUpdateHud();}
function breakoutPause(){if(!nbRunning)return;nbRunning=false;nbPaused=true;cancelAnimationFrame(nbFrame);nbMessage='Paused';document.getElementById('nb-start').textContent='RESUME';nbDraw();nbUpdateHud();}
function breakoutStop(){if(nbRunning){nbRunning=false;cancelAnimationFrame(nbFrame);}nbPaused=false;}
function breakoutRestart(){breakoutStop();nbScore=0;nbLives=3;nbEffects={wide:0,slow:0,laser:0};nbResetStage();nbMessage='Ready';document.getElementById('nb-start').textContent='START GAME';nbUpdateHud();nbDraw();}
function breakoutMove(dir){nbMove=dir;}
function nbUpdateHud(){const el=id=>document.getElementById(id);if(!el('nb-score'))return;el('nb-score').textContent=nbScore;el('nb-lives').textContent=nbLives;el('nb-level-label').textContent='LEVEL '+String(nbLevel).padStart(2,'0')+' / 30';el('nb-status').textContent=nbMessage;el('nb-start').textContent=nbRunning?'RUNNING':nbPaused?'RESUME':nbLevelWon?'NEXT LEVEL':'START GAME';}
function nbDrop(x,y){if(Math.random()>.23)return;const types=['wide','slow','multi','laser'];nbDrops.push({x,y,type:types[Math.floor(Math.random()*types.length)],vy:1.7});}
function nbApplyDrop(d){if(d.type==='wide'){nbEffects.wide=600;nbPaddle.w=92;}if(d.type==='slow')nbEffects.slow=600;if(d.type==='laser')nbEffects.laser=600;if(d.type==='multi'){const b=nbBalls[0];if(b)for(let i=0;i<2;i++)nbBalls.push({x:b.x,y:b.y,vx:i? -b.vx:b.vx,vy:b.vy,r:6,stuck:false});}nbMessage=({wide:'WIDE PADDLE!',slow:'SLOW BALL!',laser:'LASER READY!',multi:'MULTI-BALL!'}[d.type]);}
function nbHitBrick(index){const b=nbBricks[index];if(!b)return;b.hp--;if(b.hp<=0){nbScore+=b.type==='explosive'?35:10;nbCoins+=1;nbSave.coins+=1;nbDrop(b.x+b.w/2,b.y+b.h/2);nbBricks.splice(index,1);if(b.type==='explosive'){for(let i=nbBricks.length-1;i>=0;i--){const q=nbBricks[i];if(Math.hypot(q.x-b.x,q.y-b.y)<72){nbScore+=8;nbBricks.splice(i,1);}}}}else nbScore+=3;}
function breakoutLoop(t){if(!nbRunning)return;const dt=Math.min(2,(t-(nbLast||t))/16.67||1);nbLast=t;const speed=4.1*(nbEffects.slow>0?.65:1);if(nbMove)nbPaddle.x+=nbMove*5.5*dt;nbPaddle.x=Math.max(0,Math.min(NB_W-nbPaddle.w,nbPaddle.x));if(nbEffects.wide>0)nbEffects.wide-=dt;else nbPaddle.w=60;if(nbEffects.slow>0)nbEffects.slow-=dt;if(nbEffects.laser>0)nbEffects.laser-=dt;
 for(const b of nbBalls){if(b.stuck){b.x=nbPaddle.x+nbPaddle.w/2;b.y=NB_H-65;continue;}b.x+=b.vx*dt*speed/4.1;b.y+=b.vy*dt*speed/4.1;if(b.x<b.r||b.x>NB_W-b.r)b.vx*=-1;if(b.y<b.r+25)b.vy=Math.abs(b.vy);if(b.y>NB_H-58&&b.y<NB_H-43&&b.x>nbPaddle.x&&b.x<nbPaddle.x+nbPaddle.w&&b.vy>0){b.vy=-Math.abs(b.vy);b.vx=((b.x-(nbPaddle.x+nbPaddle.w/2))/(nbPaddle.w/2))*3.8;}
  for(let i=nbBricks.length-1;i>=0;i--){const q=nbBricks[i];if(b.x+b.r>q.x&&b.x-b.r<q.x+q.w&&b.y+b.r>q.y&&b.y-b.r<q.y+q.h){b.vy*=-1;nbHitBrick(i);break;}}}
 nbBalls=nbBalls.filter(b=>b.y<NB_H+15);if(!nbBalls.length){nbLives--;if(nbLives<=0){nbRunning=false;nbMessage='GAME OVER · Restart to try again';nbSave.best=Math.max(nbSave.best,nbScore);nbPersist();}else{nbBalls=[{x:nbPaddle.x+nbPaddle.w/2,y:NB_H-65,vx:2.2,vy:-3.4,r:6,stuck:true}];nbMessage='Life lost · Tap to launch';}}
 for(const d of nbDrops){d.y+=d.vy*dt;if(d.y>NB_H-65&&d.y<NB_H-45&&d.x>nbPaddle.x&&d.x<nbPaddle.x+nbPaddle.w)nbApplyDrop(d);}nbDrops=nbDrops.filter(d=>d.y<NB_H+10);
 if(nbEffects.laser>0&&Math.floor(t/160)%4===0){nbLasers.push({x:nbPaddle.x+nbPaddle.w*.25,y:NB_H-70},{x:nbPaddle.x+nbPaddle.w*.75,y:NB_H-70});}for(const l of nbLasers)l.y-=8*dt;nbLasers=nbLasers.filter(l=>l.y>35);for(let i=nbLasers.length-1;i>=0;i--){const l=nbLasers[i],j=nbBricks.findIndex(b=>l.x>=b.x&&l.x<=b.x+b.w&&l.y>=b.y&&l.y<=b.y+b.h);if(j>=0){nbHitBrick(j);nbLasers.splice(i,1);}}
 if(!nbBricks.length&&!nbLevelWon){nbLevelWon=true;nbRunning=false;nbSave.cleared=Array.from(new Set([...nbSave.cleared,nbLevel]));nbSave.unlocked=Math.max(nbSave.unlocked,Math.min(30,nbLevel+1));nbSave.best=Math.max(nbSave.best,nbScore);nbSave.coins=nbCoins;nbPersist();nbMessage=nbLevel===30?'ALL 30 LEVELS CLEARED!':'STAGE CLEAR · NEXT LEVEL UNLOCKED';}
 nbDraw();nbUpdateHud();if(nbRunning)nbFrame=requestAnimationFrame(breakoutLoop);}
function breakoutNext(){if(nbLevel<30){nbLevel++;breakoutRestart();breakoutToggle();}}
function nbDraw(){if(!nbCtx)return;const c=nbCtx;const g=c.createLinearGradient(0,0,0,NB_H);g.addColorStop(0,'#0b1730');g.addColorStop(1,'#070914');c.fillStyle=g;c.fillRect(0,0,NB_W,NB_H);for(let i=0;i<55;i++){c.fillStyle='rgba(180,225,255,'+(0.12+(i%4)*.05)+')';c.fillRect((i*67)%NB_W,(i*97)%NB_H,1.4,1.4);}c.fillStyle='#8ceeff';c.font='bold 10px Arial';c.fillText('NEON SECTOR  '+String(nbLevel).padStart(2,'0'),12,18);for(const b of nbBricks){c.shadowBlur=12;c.shadowColor=b.color;c.fillStyle=b.color;c.beginPath();c.roundRect(b.x,b.y,b.w,b.h,5);c.fill();c.shadowBlur=0;c.fillStyle='#07111f';c.font='bold 9px Arial';c.textAlign='center';c.fillText(b.hp>1?'Ⅱ':b.type==='explosive'?'✹':'',b.x+b.w/2,b.y+12);}c.textAlign='left';for(const d of nbDrops){c.fillStyle=({wide:'#72f28d',slow:'#59caff',multi:'#c28aff',laser:'#ffb45d'}[d.type]);c.shadowBlur=10;c.shadowColor=c.fillStyle;c.beginPath();c.arc(d.x,d.y,7,0,Math.PI*2);c.fill();c.shadowBlur=0;}for(const l of nbLasers){c.fillStyle='#ffad55';c.fillRect(l.x-2,l.y,4,12);}c.shadowBlur=16;c.shadowColor='#62f5ff';c.fillStyle='#69efff';c.beginPat
