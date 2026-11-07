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

.login-wrap{min-height:620px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:4px 5px}
.clock-panel{width:100%;display:flex;align-items:center;justify-content:center;gap:20px;margin:0 auto 16px;padding:15px 12px;border-radius:25px;background:linear-gradient(135deg,#ffffff20,#ffffff09);border:1px solid #ffffff40;box-shadow:0 12px 35px #071b3740}
.login-wrap .clock-panel{transform:translateY(-10px)}
.login-wrap .login-actions{transform:translateY(-10px)}
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
.login-sub{max-width:290px;margin:6px auto 16px}
.login-actions{width:100%;max-width:310px;display:grid;gap:9px}
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
/* COMPACT HOME SHORTCUTS — square neon buttons */
.home-shortcuts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:8px;margin-top:8px}
.home-shortcut{min-width:0;min-height:78px;padding:8px 4px;border-radius:15px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;text-align:center;color:#f2fffc;background:linear-gradient(145deg,#123b55,#174e55 55%,#382b67);border:1px solid #67f5db88;box-shadow:0 0 12px #42e9d51c,inset 0 0 12px #8cffff0d}
.home-shortcut .emoji{font-size:22px;line-height:1.1}
.home-shortcut b{font-size:10px;line-height:1.2;overflow-wrap:anywhere}
.home-shortcut.neon-shortcut{background:linear-gradient(145deg,#17234d,#38216b);border-color:#a98cff;box-shadow:0 0 13px #9d75ff30}
.home-shortcut.earth-shortcut{background:linear-gradient(145deg,#063b43,#075e60);border-color:#55dedb;box-shadow:0 0 13px #55dedb30}
.home-shortcut.logout-shortcut{background:linear-gradient(145deg,#5b242d,#842e3b);border-color:#ff8c9a}

/* 3D DEPTH FINISH — preserves the existing app background palette */
.phone{box-shadow:0 28px 70px #263d6a70,inset 0 3px 5px #ffffffb8,inset 0 -8px 18px #20345a22}
.screen{box-shadow:inset 0 2px 4px #ffffff30,inset 0 -22px 38px #07142635,0 12px 28px #07142635}
.screen:before{content:"";position:absolute;inset:0;z-index:0;pointer-events:none;border-radius:inherit;background:linear-gradient(145deg,#ffffff0b,transparent 32%,#0000000b 100%);box-shadow:inset 0 1px 0 #ffffff25,inset 0 0 28px #ffffff08}
.screen>*{position:relative;z-index:1}
/* Extra layered depth on the existing pastel background — original colors retained. */
body{background-attachment:fixed;background-image:radial-gradient(ellipse at 12% 12%,#ffffffa8 0,transparent 26%),radial-gradient(ellipse at 88% 18%,#ffffff70 0,transparent 24%),radial-gradient(ellipse at 50% 92%,#ffffff55 0,transparent 32%),radial-gradient(ellipse at 50% 50%,#8bc8ff20 0,transparent 62%),linear-gradient(135deg,#d7fff1,#d9e7ff 52%,#f1ddff)}
.phone{background-image:linear-gradient(145deg,#ffffffa8 0%,#e5fff7 10%,#8be7d3 25%,#92aaff 58%,#d6a9ff 82%,#ffe0a0 100%);box-shadow:0 34px 82px #263d6a75,0 8px 18px #ffffffa0,inset 0 3px 5px #ffffffd0,inset 0 -10px 22px #20345a30}
.screen{background-image:radial-gradient(ellipse at 12% 8%,#ffffff20,transparent 32%),radial-gradient(ellipse at 88% 25%,#8b9dff20,transparent 36%),radial-gradient(ellipse at 50% 100%,#00000018,transparent 48%),radial-gradient(circle at 50% 50%,#ffffff08,transparent 70%),linear-gradient(145deg,#153d49,#173c50 45%,#292c5a 100%)}
button{position:relative;overflow:hidden;transform:translateZ(0);box-shadow:inset 0 2px 0 #ffffff55,inset 0 -4px 0 #00000020,0 7px 14px #06172b38;transition:transform .12s ease,filter .12s ease,box-shadow .12s ease}
button:active{transform:translateY(2px);filter:brightness(.97);box-shadow:inset 0 3px 5px #00000022,0 2px 5px #06172b35}
.card,.clock-panel,.tile,.wide-tile,.row-tile,.home-shortcut,.nb-panel,.earth-panel,.school-option,.school-text-card{box-shadow:inset 0 2px 0 #ffffff35,inset 0 -5px 0 #00000018,0 10px 20px #06172b38}
.home-shortcut{border-width:1px 1px 3px}
.home-shortcut:nth-child(1){background:linear-gradient(145deg,#287e91,#164b69);border-color:#8ce9df}
.home-shortcut:nth-child(2){background:linear-gradient(145deg,#7452a8,#39275f);border-color:#c7a6ff}
.home-shortcut:nth-child(3){background:linear-gradient(145deg,#a87836,#654329);border-color:#ffe0a8}
.home-shortcut.neon-shortcut{background:linear-gradient(145deg,#5d42a4,#27214f);border-color:#c4a4ff}
.home-shortcut.earth-shortcut{background:linear-gradient(145deg,#168b82,#064b50);border-color:#75f2e2}
.home-shortcut.music-shortcut{background:linear-gradient(145deg,#287bb5,#17436f);border-color:#8bd7ff}
.home-shortcut.music-shortcut.is-on{background:linear-gradient(145deg,#248b73,#105447);border-color:#8dffd1}
#music-toggle{width:100%;height:auto;min-height:78px;padding:8px 4px;border-radius:15px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:5px;color:#f2fffc;font-size:10px;letter-spacing:0}
#music-toggle .emoji{font-size:22px;line-height:1.1}
#music-toggle b{font-size:10px;line-height:1.2}
.logout-row{width:100%;min-height:48px;margin-top:9px;padding:10px 15px;border-radius:14px;display:flex;align-items:center;gap:10px;text-align:left;color:#fff;background:linear-gradient(110deg,#a83b43,#702b43);border:1px solid #ff9da5;border-bottom-width:3px}
.logout-row .emoji{font-size:20px}
.logout-row b{font-size:11px;letter-spacing:.6px}
.logout-arrow{margin-left:auto;font-size:22px}
#home-page .section{margin:11px 0}
#home-page .tile{min-height:88px;padding:9px 5px;gap:5px}
#home-page .tile-grid .tile:nth-child(1){background:linear-gradient(145deg,#176b67,#244b83);border-color:#8ce9df}
#home-page .tile-grid .tile:nth-child(2){background:linear-gradient(145deg,#7452a8,#39275f);border-color:#c7a6ff}
#home-page .tile-grid .tile:nth-child(3){background:linear-gradient(145deg,#a87836,#654329);border-color:#ffe0a8}
#home-page .tile .emoji{font-size:23px}
#home-page .wide-tile{padding:12px;gap:10px;border-radius:16px}
#home-page .wide-icon{font-size:29px}
#home-page .wide-title{font-size:15px;margin-bottom:2px}
#home-page .wide-desc{font-size:10px}
@media(max-height:760px){
 #home-page .section{margin:8px 0}
 .home-shortcut{min-height:70px}
}

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


/* LIVE EARTH — compact single-screen observatory */
#earth-page{
display:flex;
flex-direction:column;
gap:8px
}

#earth-page .page-head{
margin:1px 0 2px;
gap:9px
}

#earth-page .page-head h2{
font-size:18px;
margin:0
}

#earth-page .back{
padding:7px 10px;
font-size:11px
}

.earth-hero{
position:relative;
background-color:#000!important;
background-image:radial-gradient(1px 1px at 7% 13%,#ffffffdd 98%,transparent),radial-gradient(1px 1px at 18% 72%,#9bdcffcc 98%,transparent),radial-gradient(1.5px 1.5px at 31% 28%,#ffffffcc 98%,transparent),radial-gradient(1px 1px at 43% 83%,#ffffffaa 98%,transparent),radial-gradient(1px 1px at 58% 17%,#c8eaffdd 98%,transparent),radial-gradient(1px 1px at 72% 64%,#ffffffcc 98%,transparent),radial-gradient(1.5px 1.5px at 88% 31%,#ffffffdd 98%,transparent),radial-gradient(1px 1px at 94% 82%,#9bdcffcc 98%,transparent),radial-gradient(ellipse at 50% 45%,#101a32 0%,#03050d 48%,#000 78%);
background-size:100% 100%;
border:1px solid #55d9dc66;
border-radius:20px;
padding:8px;
overflow:hidden;
box-shadow:0 20px 46px #00121caa,inset 0 2px 0 #ffffff24,inset 0 -12px 24px #00000030;
transform:perspective(1100px) translateZ(0)
}

.earth-kicker{
font-size:9px;
letter-spacing:1.5px;
color:#71e7dc;
font-weight:800
}

.earth-hero h2{
font-size:17px!important;
margin:5px 0 1px!important
}

.earth-hero>p{
font-size:9px!important;
margin:0!important;
line-height:1.3!important
}

.earth-layout{
display:block;
position:relative
}

.earth-celestial-row{
display:flex;
align-items:center;
justify-content:space-between;
gap:12px;
padding:9px 12px;
margin-top:7px;
border:1px solid #ffffff18;
border-radius:13px;
background:linear-gradient(110deg,#111827,#0b1520 55%,#171521);

}

.earth-celestial-item{
display:flex;
align-items:center;
gap:9px;
min-width:0;
color:#e8f5ff;
font-size:9px;
font-weight:800;
letter-spacing:.5px
}

.earth-celestial-item small{
display:block;
color:#a6b8c9;
font-size:7px;
font-weight:500;
letter-spacing:.2px;
margin-top:3px
}

.earth-sun,.earth-moon{
position:relative;
inset:auto;
flex:0 0 auto
}

.earth-sun{
width:42px;
height:42px
}

.earth-moon{
width:34px;
height:34px
}

.earth-orbit{
position:relative;
width:100%;
height:224px;
overflow:hidden;
background-color:#000;
background-image:radial-gradient(1px 1px at 8% 18%,#fff 98%,transparent),radial-gradient(1px 1px at 23% 75%,#9bdcff 98%,transparent),radial-gradient(1.5px 1.5px at 43% 12%,#fff 98%,transparent),radial-gradient(1px 1px at 66% 84%,#fff 98%,transparent),radial-gradient(1px 1px at 91% 34%,#d9efff 98%,transparent),radial-gradient(ellipse at 50% 50%,#071326 0%,#01030a 68%,#000 100%)
}

#earth-globe{
width:100%;
height:224px;
min-width:0;
touch-action:none;
cursor:grab;
position:relative;
z-index:1
}

#earth-globe:active{
cursor:grabbing
}

.earth-sun{
position:absolute;
z-index:3;
left:9px;
top:13px;
width:56px;
height:56px;
border-radius:50%;
pointer-events:none;
background-color:#ff9d35;
background-image:url('https://www.solarsystemscope.com/textures/download/2k_sun.jpg'),radial-gradient(circle at 32% 27%,#fffbd0 0 2%,#ffe18a 15%,#ff9a32 52%,#9f2515 100%);
background-size:cover;
background-position:center;
background-blend-mode:normal;
box-shadow:0 0 16px 7px #ffcf6bba,0 0 38px 20px #ff8b2e88,0 0 76px 34px #ff5b1d55,inset -9px -7px 15px #7b170b88;
animation:earthSunTurn 42s linear infinite
}

.earth-sun:after{
content:"";
position:absolute;
inset:-8px;
border-radius:50%;
background:radial-gradient(circle,#ffb34b22 42%,#ff8a2b18 60%,transparent 72%);
filter:blur(3px)
}

@keyframes earthSunTurn{
to{
transform:rotate(360deg)
}

}

/* Realistic light direction, lunar surface and solar corona for the Earth observatory. */
.earth-orbit{
isolation:isolate
}

#earth-globe{
touch-action:none;
user-select:none;
-webkit-user-select:none
}

#earth-globe canvas{
touch-action:none;
outline:none
}

#earth-globe:after{
content:"";
position:absolute;
z-index:2;
pointer-events:none;
width:min(66vw,190px);
height:min(66vw,190px);
max-height:190px;
max-width:190px;
left:50%;
top:50%;
transform:translate(-50%,-50%);
border-radius:50%;
background:linear-gradient(112deg,rgba(255,245,205,.035) 0%,rgba(255,255,255,0) 34%,rgba(0,5,18,.10) 58%,rgba(0,3,16,.54) 100%);
box-shadow:inset -13px -2px 24px rgba(0,0,0,.22);

}

.earth-sun{
background-image:url('https://www.solarsystemscope.com/textures/download/2k_sun.jpg'),radial-gradient(circle at 32% 27%,#fffbd0 0 2%,#ffe18a 15%,#ff9a32 52%,#9f2515 100%);
background-size:cover;
background-position:center;
box-shadow:0 0 18px 8px #ffcf6bba,0 0 44px 22px #ff8b2e88,0 0 90px 40px #ff5b1d55,inset -9px -7px 15px #7b170b88;

}

.earth-sun:before{
content:"";
position:absolute;
inset:-16px;
border-radius:50%;
background:conic-gradient(from 20deg,transparent 0 8%,#ffb33b55 10%,transparent 13% 27%,#ffd06a55 30%,transparent 34% 61%,#ff8b2b66 64%,transparent 68% 100%);
filter:blur(5px);
animation:earthSunTurn 24s linear infinite;

}

.earth-moon{
position:absolute;
z-index:3;
right:14px;
bottom:13px;
width:39px;
height:39px;
border-radius:50%;
pointer-events:none;
background-color:#aab4c4;
background-image:url('https://www.solarsystemscope.com/textures/download/2k_moon.jpg'),radial-gradient(circle at 30% 28%,#f2f4f7,#8c98aa 68%,#303b4c);
background-size:cover;
background-position:center;
box-shadow:0 0 13px 4px #b7d5ff44,inset -8px -5px 12px #111b30aa;
animation:earthMoonDrift 9s ease-in-out infinite;

}

.earth-moon:after{
content:"";
position:absolute;
inset:0;
border-radius:50%;
background:radial-gradient(circle at 27% 30%,transparent 0 12%,#34405433 13% 17%,transparent 18%),radial-gradient(circle at 65% 58%,transparent 0 9%,#26324755 10% 15%,transparent 16%),radial-gradient(circle at 42% 76%,transparent 0 7%,#26324755 8% 12%,transparent 13%),linear-gradient(110deg,#ffffff16 0%,transparent 40%,#07102099 100%);

}

@keyframes earthMoonDrift{
0%,100%{
transform:translateY(0)
}
50%{
transform:translateY(-4px)
}

}

.earth-stats-overlay{
display:none!important
}
.earth-stats-row{
display:grid;
grid-template-columns:repeat(3,minmax(0,1fr));
gap:5px;
margin-top:5px;

}

.earth-stats-row .earth-stat{
min-width:0;
text-align:center;
padding:5px 3px;
background:linear-gradient(145deg,#102f3bdc,#071721df);
border:1px solid #8ce8e477;
border-radius:9px;
padding:5px 6px;
min-width:0;
box-shadow:0 4px 12px #0008,inset 0 1px 0 #ffffff22;
backdrop-filter:blur(5px)
}

.earth-stat b{
display:block;
color:#e8ffff;
font-size:12px;
line-height:1.15;
overflow-wrap:anywhere;
font-variant-numeric:tabular-nums
}

.earth-stat small{
display:block;
color:#91cbd0;
font-size:7px;
letter-spacing:.45px;
margin-top:3px
}

.earth-live-dot{
display:inline-block;
width:6px;
height:6px;
background:#55f0a2;
border-radius:50%;
box-shadow:0 0 9px #55f0a2;
margin-right:5px;
animation:earthPulse 1.5s infinite
}

@keyframes earthPulse{
50%{
opacity:.35;
box-shadow:0 0 2px #55f0a2
}

}

.earth-tools{
display:grid;
grid-template-columns:repeat(4,minmax(0,1fr));
gap:5px;
margin-top:5px
}

.earth-btn{
min-width:0;
border:1px solid #69ded866;
background:linear-gradient(135deg,#10303a,#174753);
color:#dffefa;
border-radius:9px;
padding:7px 2px;
font-weight:800;
font-size:9px;
white-space:nowrap
}

.earth-btn:nth-child(1){
background:linear-gradient(135deg,#145c62,#168c86);
border-color:#6ef5db
}

.earth-btn:nth-child(2){
background:linear-gradient(135deg,#244b78,#386bb0);
border-color:#8abaff
}

.earth-btn:nth-child(3){
background:linear-gradient(135deg,#684a24,#a66b2c);
border-color:#ffd477
}

.earth-btn:nth-child(4){
background:linear-gradient(135deg,#4d3475,#8054ad);
border-color:#c8a6ff
}

.earth-info{
background:linear-gradient(145deg,#0b202b,#102d38);
border:1px solid #64d8d544;
border-radius:15px;
padding:9px;
margin-top:0;
box-shadow:0 9px 22px #00121c55,inset 0 1px 0 #ffffff14
}

.earth-info-grid{
display:grid;
grid-template-columns:1fr 1fr;
gap:4px;
margin-top:4px
}

.earth-info-cell{
background:#ffffff0a;
padding:6px;
border-radius:8px;
min-width:0
}

.earth-info-cell small{
display:block;
color:#9ac1c6;
font-size:8px
}
.earth-info-cell b{
font-size:10px;
color:#e8ffff;
overflow-wrap:anywhere
}

.earth-note{
font-size:7px;
color:#9bbbc1;
line-height:1.2;
margin:3px 2px 0
}

.earth-search{
display:grid;
grid-template-columns:minmax(0,1fr) 62px;
gap:5px;
margin:6px 0 0
}

.earth-search input{
width:100%;
min-width:0;
background:#071a25;
color:#eaffff;
border:1px solid #67d8d866;
border-radius:9px;
padding:8px;
font-size:10px;
outline:none
}

.earth-search input:focus{
border-color:#71f3dc;
box-shadow:0 0 0 2px #71f3dc22
}

.earth-search button{
background:linear-gradient(135deg,#14515b,#167e7c);
color:#eaffff;
border:1px solid #69ded866;
border-radius:9px;
padding:0 7px;
font-weight:800;
font-size:9px
}

.earth-suggest{
display:none;
max-height:92px;
overflow:auto;
background:#0b202b;
border:1px solid #64d8d555;
border-radius:9px;
margin-top:4px
}

.earth-suggest button{
display:block;
width:100%;
text-align:left;
padding:7px 9px;
background:transparent;
color:#eaffff;
border:0;
border-bottom:1px solid #ffffff12;
font-size:10px
}

.earth-suggest button:last-child{
border:0
}

.earth-status{
font-size:8px;
color:#a8d2d5;
min-height:10px;
margin:3px 2px
}

#earth-country-name{
font-size:13px;
margin:4px 0 2px!important;
color:#f0ffff
}

#earth-country-desc{
font-size:9px!important;
line-height:1.25!important;
margin:0!important
}

@media(max-width:370px){

 #earth-globe,.earth-orbit{
height:216px
}

 .earth-stats-overlay{
width:82px;
right:2px
}

 .earth-stat{
padding:4px 5px
}

 .earth-stat b{
font-size:11px
}

 .earth-sun{
width:40px;
height:40px;
left:7px;
top:14px
}

 .earth-btn{
font-size:8px;
padding:7px 1px
}

}

@media(max-height:760px){

 #earth-globe,.earth-orbit{
height:202px
}

 #earth-page{
gap:6px
}

 .earth-hero{
padding:8px
}

 .earth-info{
padding:7px
}

 .earth-info-grid{
gap:4px
}

 .earth-info-cell{
padding:5px
}

}

/* FINAL COMPACT GAME LAYOUT — controls remain visible; page scrolling stays enabled. */
#flappy-page .page-head,#snake-page .page-head,#car-page .page-head,#breakout-page .page-head{margin:2px 0 7px;gap:8px}
#flappy-page .card,#snake-page .card,#car-page .card{padding:8px;margin:0}
#flappy-page .card>p:first-child,#snake-page .card>p:first-child,#car-page .card>p:first-child{font-size:10px;line-height:1.25;margin:0 0 5px}
#flappy-canvas{height:clamp(245px,39vh,330px);max-height:330px;width:100%;border-radius:12px;border:1px solid #ffffff55}
#flappy-page .primary{padding:9px 10px;margin-top:6px;font-size:11px}
#flappy-score{margin:5px 0 0;text-align:center;font-size:10px}
#snake-canvas{width:min(100%,min(260px,37vh));max-width:260px;margin:0 auto 5px}
#snake-controls{max-width:195px;gap:4px;margin:3px auto 5px}
#snake-controls button{min-height:34px;padding:4px;font-size:16px}
#snake-page .primary{padding:8px;margin-top:2px;font-size:11px}
#snake-page #snake-score{font-size:10px;margin:4px 0 0}
#car-canvas{height:clamp(245px,39vh,330px);max-height:330px;max-width:310px;margin:0 auto 5px;border-radius:12px}
#car-page .car-score{gap:5px;margin:4px 0}
#car-page .car-score div{padding:5px 3px}
#car-page .car-score b{font-size:14px}
#car-page .car-score span{font-size:8px}
#car-page .car-controls{gap:7px;margin-top:5px}
#car-page .car-controls button{padding:8px;border-radius:11px;font-size:15px}
#car-page .primary{padding:8px;margin-top:6px!important;font-size:11px}
#car-page .small-note{font-size:9px;margin:4px 0 0}
#breakout-page{padding:8px;border-radius:16px}
#breakout-page .nb-hero{padding:8px;border-radius:12px}
#breakout-page .nb-hero h2{font-size:17px!important;margin:3px 0!important}
#breakout-page .nb-hero p{display:none}
#breakout-page .nb-stats{gap:4px;margin-top:5px}
#breakout-page .nb-stat{padding:5px 3px}
#breakout-page .nb-stat b{font-size:13px}
#breakout-page h3{font-size:10px;margin:7px 2px 4px}
#breakout-page .nb-panel{padding:7px;margin-top:5px;border-radius:11px}
#breakout-page canvas{height:clamp(250px,39vh,335px);max-height:335px;width:100%}
#breakout-page .nb-row{gap:5px}
#breakout-page .nb-btn,#breakout-page .nb-ghost{padding:7px 8px;font-size:8px}
#breakout-page .nb-levels{gap:3px}
#breakout-page .nb-level{padding:5px 1px;font-size:8px}
#breakout-page .nb-power{padding:5px;margin:3px 0;font-size:8px}
#games-page .tile-grid{gap:6px}
#games-page .tile{min-height:76px;padding:7px 4px;gap:4px}
#games-page .tile .emoji{font-size:21px}
#games-page .tile span:last-child{font-size:9px}
@media(max-height:700px){
 #flappy-canvas,#car-canvas{height:225px}
 #breakout-page canvas{height:225px}
 #snake-canvas{width:min(220px,31vh)}
}
/* EARTH 4D — natural atmosphere, larger solar system objects, no artificial blue rim. */
.earth-orbit{height:300px;min-height:300px;overflow:hidden;background-color:#02050b}
#earth-globe{height:300px;min-height:300px;touch-action:none;overscroll-behavior:contain}
#earth-globe:after{display:none!important;content:none!important}
#earth-globe canvas{outline:0!important;touch-action:none!important}
.earth-hero{border-color:#ffffff20;background-image:radial-gradient(1px 1px at 7% 13%,#ffffffdd 98%,transparent),radial-gradient(1px 1px at 18% 72%,#9bdcffcc 98%,transparent),radial-gradient(1.5px 1.5px at 31% 28%,#ffffffcc 98%,transparent),radial-gradient(1px 1px at 43% 83%,#ffffffaa 98%,transparent),radial-gradient(1px 1px at 58% 17%,#c8eaffdd 98%,transparent),radial-gradient(1px 1px at 72% 64%,#ffffffcc 98%,transparent),radial-gradient(1.5px 1.5px at 88% 31%,#ffffffdd 98%,transparent),radial-gradient(1px 1px at 94% 82%,#9bdcffcc 98%,transparent),radial-gradient(ellipse at 50% 45%,#101a32 0%,#03050d 48%,#000 78%)}
.earth-sun{width:82px;height:82px;left:8px;top:10px;z-index:4;background-color:#ff9d35;background-image:url('https://www.solarsystemscope.com/textures/download/2k_sun.jpg'),radial-gradient(circle at 32% 27%,#fffbd0 0 2%,#ffe18a 15%,#ff9a32 52%,#9f2515 100%);background-size:cover;background-position:center;border-radius:50%;box-shadow:0 0 22px 10px #ffcf6bcc,0 0 55px 28px #ff8b2e99,0 0 105px 48px #ff5b1d66,inset -12px -9px 19px #7b170baa}
.earth-sun:after{inset:-13px;filter:blur(5px);background:radial-gradient(circle,#ffdb8a22 38%,#ff9c3528 57%,transparent 74%)}
.earth-sun:before{content:"";position:absolute;inset:-22px;border-radius:50%;pointer-events:none;background:conic-gradient(from 15deg,transparent 0 7%,#ffd27a66 9%,transparent 13% 24%,#ff9a3c77 27%,transparent 32% 57%,#ffce6b66 61%,transparent 66% 100%);filter:blur(7px);animation:earthSunTurn 28s linear infinite}
.earth-moon{width:54px;height:54px;right:10px;bottom:10px;background-size:cover;box-shadow:0 0 17px 5px #c8ddff55,inset -10px -7px 14px #101a2cbb}
.earth-tools{grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}
.earth-btn{font-size:10px;padding:8px 3px}
.earth-btn:nth-child(1){background:linear-gradient(135deg,#145c62,#168c86);border-color:#6ef5db}
.earth-btn:nth-child(2){background:linear-gradient(135deg,#244b78,#386bb0);border-color:#8abaff}
.earth-btn:nth-child(3),.earth-btn:nth-child(4){background:linear-gradient(135deg,#4d3475,#8054ad);border-color:#c8a6ff}
.earth-search{grid-template-columns:minmax(0,1fr) 58px}
.earth-search input{font-size:11px}
.earth-info{padding:8px}
.earth-info-grid{grid-template-columns:1fr 1fr}
#earth-country-capital{display:none}
@media(max-width:370px){.earth-orbit,#earth-globe{height:270px;min-height:270px}.earth-sun{width:70px;height:70px}.earth-moon{width:47px;height:47px}}
@media(max-height:700px){.earth-orbit,#earth-globe{height:250px;min-height:250px}.earth-hero{padding:7px}}

/* Music switch is styled as a home shortcut above. */

</style>
<script src="https://cdn.jsdelivr.net/npm/globe.gl" onerror="this.onerror=null;this.src='https://unpkg.com/globe.gl'"></script>
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

   <div class="home-shortcuts">
    <button class="home-shortcut" onclick="openPage('settings-page')"><span class="emoji">⚙️</span><b>SETTINGS</b></button>
    <button class="home-shortcut" onclick="openPage('about-page')"><span class="emoji">✨</span><b>ABOUT</b></button>
    <button class="home-shortcut" onclick="openPage('school-page')"><span class="emoji">🏫</span><b>ABOUT MY SCHOOL</b></button>
    <button class="home-shortcut neon-shortcut" onclick="openPage('breakout-page');breakoutInit()"><span class="emoji">🟣</span><b>NEON BREAKOUT</b></button>
    <button class="home-shortcut earth-shortcut" onclick="openPage('earth-page');earthInit()"><span class="emoji">🌍</span><b>LIVE EARTH 4D</b></button>
    <button id="music-toggle" class="home-shortcut music-shortcut" type="button" onclick="toggleBackgroundMusic()" aria-label="Turn background music on"><span class="emoji">♫</span><b>MUSIC OFF</b></button>
   </div>
   <button class="logout-row" onclick="logout()"><span class="emoji">🚪</span><b>LOGOUT</b><span class="logout-arrow">›</span></button>
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
    <h2>Our planet, in motion.</h2>
    <p>Drag in any direction to explore the whole planet · Pinch to zoom</p>
    <div class="earth-layout"><div class="earth-orbit">
     <div id="earth-globe" aria-label="Interactive 3D Earth globe"></div>
     </div></div>
    <div class="earth-celestial-row" aria-label="Sun and Moon reference display">
     <div class="earth-celestial-item"><div class="earth-sun" aria-hidden="true"></div><span>SUN<small>Solar surface · animated texture</small></span></div>
     <div class="earth-celestial-item"><div class="earth-moon" aria-hidden="true"></div><span>MOON<small>Lunar surface · crater detail</small></span></div>
    </div>
    <div class="earth-tools"><button class="earth-btn" onclick="earthZoom(1.35)">＋ ZOOM IN</button><button class="earth-btn" onclick="earthZoom(.74)">－ ZOOM OUT</button><button class="earth-btn" id="earth-spin" onclick="earthToggleSpin()">Ⅱ STOP ROTATION</button></div>
    <div class="earth-stats-row">
     <div class="earth-stat"><b id="earth-pop">8.2B</b><small>POPULATION</small></div>
     <div class="earth-stat"><b id="earth-births">+0</b><small>BIRTHS TODAY*</small></div>
     <div class="earth-stat"><b id="earth-deaths">+0</b><small>DEATHS TODAY*</small></div>
    </div>
    <p class="earth-note">*Population, births and deaths are model-based estimates. Globe texture and full country database require internet access.</p>
   </div>
   <div class="earth-info"><div class="earth-kicker">COUNTRY EXPLORER</div>
    <div class="earth-search"><input id="earth-country-input" type="search" autocomplete="off" placeholder="Search a country…" oninput="earthSearchCountry(this.value)" onkeydown="if(event.key==='Enter')earthChooseFirst()"><button onclick="earthChooseFirst()">SEARCH</button></div>
    <div id="earth-suggest" class="earth-suggest"></div><div id="earth-search-status" class="earth-status">Search from 100 popular countries.</div>
    <h3 id="earth-country-name">Select a country</h3><p id="earth-country-desc">Explore country details on the interactive globe.</p>
    <div class="earth-info-grid"><div class="earth-info-cell"><small>REGION</small><b id="earth-region">—</b></div><div class="earth-info-cell"><small>COUNTRY CODE</small><b id="earth-capital">—</b></div><div class="earth-info-cell"><small>POPULATION</small><b id="earth-country-pop">—</b></div><div class="earth-info-cell"><small>AREA</small><b id="earth-country-area">—</b></div></div>
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
let guessFinished = false;let typingStarted = false;
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
let snakeStep = 125;
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
    const pipeGradient = fx.createLinearGradient(p.x, 0, p.x + 48, 0);
    pipeGradient.addColorStop(0, "#075343");
    pipeGradient.addColorStop(0.13, "#168b77");
    pipeGradient.addColorStop(0.48, "#55e3a7");
    pipeGradient.addColorStop(0.76, "#168b77");
    pipeGradient.addColorStop(1, "#063e39");
    const drawPipeBody = (x, y, width, height) => {
      if (height <= 0) return;
      fx.save();
      fx.fillStyle = pipeGradient;
      fx.fillRect(x, y, width, height);
      fx.fillStyle = "rgba(220,255,239,.18)";
      fx.fillRect(x + 7, y + 2, 4, Math.max(0, height - 4));
      fx.fillStyle = "rgba(0,20,18,.20)";
      fx.fillRect(x + width - 7, y + 2, 4, Math.max(0, height - 4));
      fx.strokeStyle = "#071b19";
      fx.lineWidth = 3;
      fx.strokeRect(x + 1.5, y + 1.5, width - 3, Math.max(0, height - 3));
      fx.strokeStyle = "rgba(196,255,226,.42)";
      fx.lineWidth = 1;
      fx.beginPath();
      fx.moveTo(x + 13, y + 4);
      fx.lineTo(x + 13, y + height - 4);
      fx.stroke();
      fx.restore();
    };
    const drawPipeCap = (x, y, width, height) => {
      const cap = fx.createLinearGradient(x, y, x + width, y);
      cap.addColorStop(0, "#064238");
      cap.addColorStop(.18, "#1c9b7d");
      cap.addColorStop(.5, "#70edb5");
      cap.addColorStop(.82, "#16836d");
      cap.addColorStop(1, "#042e2c");
      fx.fillStyle = cap;
      fx.fillRect(x, y, width, height);
      fx.strokeStyle = "#071714";
      fx.lineWidth = 3;
      fx.strokeRect(x + 1.5, y + 1.5, width - 3, height - 3);
      fx.strokeStyle = "rgba(220,255,239,.65)";
      fx.lineWidth = 1;
      fx.beginPath();
      fx.moveTo(x + 5, y + 3);
      fx.lineTo(x + width - 5, y + 3);
      fx.stroke();
    };
    drawPipeBody(p.x, 0, 48, p.top - 12);
    drawPipeCap(p.x - 4, p.top - 13, 56, 14);
    drawPipeBody(p.x, p.bottom + 12, 48, h - p.bottom - 47);
    drawPipeCap(p.x - 4, p.bottom, 56, 14);
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
  snakeStep = 125;
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
    snakeStep = Math.max(112, 125 - snakePoints * 0.35);
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
function nbResetStage(){nbPaddle={x:150,w:nbEffects.wide>0?92:60};nbBalls=[{x:180,y:455,vx:2.3,vy:-3.5,r:6,stuck:true}];nbDrops=[];nbLasers=[];nbLevelWon=false;nbBricks=[];const
rows=3+Math.min(4,Math.floor((nbLevel-1)/5)),cols=8;for(let r=0;r<rows;r++)for(let c=0;c<cols;c++){let pattern=(r*7+c*3+nbLevel)%11;if(nbLevel%4===0&&pattern===0)continue;nbBricks.push({x:9+c*43,y:65+r*25,w:39,h:18,hp:pattern===1?2:1,max:pattern===1?2:1,color:nbColors[(r+c+nbLevel)%nbColors.length],type:pattern===0?'explosive':'normal'});}}
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
function nbDraw(){if(!nbCtx)return;const c=nbCtx;const g=c.createLinearGradient(0,0,0,NB_H);g.addColorStop(0,'#0b1730');g.addColorStop(1,'#070914');c.fillStyle=g;c.fillRect(0,0,NB_W,NB_H);for(let i=0;i<55;i++){c.fillStyle='rgba(180,225,255,'+(0.12+(i%4)*.05)+')';c.fillRect((i*67)%NB_W,(i*97)%NB_H,1.4,1.4);}c.fillStyle='#8ceeff';c.font='bold 10px Arial';c.fillText('NEON SECTOR  '+String(nbLevel).padStart(2,'0'),12,18);for(const b of nbBricks){c.shadowBlur=12;c.shadowColor=b.color;c.fillStyle=b.color;c.beginPath();c.roundRect(b.x,b.y,b.w,b.h,5);c.fill();c.shadowBlur=0;c.fillStyle='#07111f';c.font='bold 9px Arial';c.textAlign='center';c.fillText(b.hp>1?'Ⅱ':b.type==='explosive'?'✹':'',b.x+b.w/2,b.y+12);}c.textAlign='left';for(const d of nbDrops){c.fillStyle=({wide:'#72f28d',slow:'#59caff',multi:'#c28aff',laser:'#ffb45d'}[d.type]);c.shadowBlur=10;c.shadowColor=c.fillStyle;c.beginPath();c.arc(d.x,d.y,7,0,Math.PI*2);c.fill();c.shadowBlur=0;}for(const l of nbLasers){c.fillStyle='#ffad55';c.fillRect(l.x-2,l.y,4,12);}c.shadowBlur=16;c.shadowColor='#62f5ff';c.fillStyle='#69efff';c.beginPath();c.roundRect(nbPaddle.x,NB_H-48,nbPaddle.w,10,5);c.fill();c.shadowBlur=0;for(const b of nbBalls){c.shadowBlur=14;c.shadowColor='#fff';c.fillStyle='#fff';c.beginPath();c.arc(b.x,b.y,b.r,0,Math.PI*2);c.fill();c.shadowBlur=0;}if(!nbRunning){c.fillStyle='rgba(3,8,20,.52)';c.fillRect(0,NB_H/2-26,NB_W,52);c.fillStyle='#eafcff';c.font='bold 14px Arial';c.textAlign='center';c.fillText(nbMessage,NB_W/2,NB_H/2+5);c.textAlign='left';}}
if(nbCanvas){nbCanvas.addEventListener('pointerdown',e=>{nbPointer=e.clientX;const b=nbBalls.find(x=>x.stuck);if(b){b.stuck=false;nbMessage='Good luck!';}if(!nbRunning&&!nbLevelWon&&nbLives>0&&nbPaused===false){/* start remains explicit */}});nbCanvas.addEventListener('pointermove',e=>{if(nbPointer===null&&e.buttons===0)return;const r=nbCanvas.getBoundingClientRect();const x=(e.clientX-r.left)*NB_W/r.width;nbPaddle.x=Math.max(0,Math.min(NB_W-nbPaddle.w,x-nbPaddle.w/2));if(nbBalls[0]?.stuck)nbBalls[0].x=nbPaddle.x+nbPaddle.w/2;});nbCanvas.addEventListener('pointerup',()=>nbPointer=null);nbCanvas.addEventListener('pointercancel',()=>nbPointer=null);}
// Replace start button behavior after stage clear with next stage.
const nbStartButton=document.getElementById('nb-start');if(nbStartButton)nbStartButton.addEventListener('click',()=>{if(nbLevelWon)breakoutNext();else if(nbBalls[0]?.stuck)nbBalls[0].stuck=false;});
nbRenderMeta();nbResetStage();nbUpdateHud();nbDraw();
// ================= END NEON BREAKOUT =================

// ================= LIVE EARTH DASHBOARD =================
let earthGlobe=null,earthSpin=true,earthTimer=null,earthCountriesData=[],earthCountryReady=false,earthStartedAt=Date.now(),earthGeoFeatures=[],earthSelectedFeature=null,earthBoundaryLoading=false;
const earthFallback=[
 {name:'Pakistan',capital:'Islamabad',region:'Asia',subregion:'Southern Asia',population:255000000,area:881912,lat:30.3753,lng:69.3451},
 {name:'India',capital:'New Delhi',region:'Asia',subregion:'Southern Asia',population:1460000000,area:3287263,lat:20.5937,lng:78.9629},
 {name:'China',capital:'Beijing',region:'Asia',subregion:'Eastern Asia',population:1410000000,area:9596961,lat:35.8617,lng:104.1954},
 {name:'United States',capital:'Washington, D.C.',region:'Americas',subregion:'North America',population:347000000,area:9833520,lat:37.0902,lng:-95.7129},
 {name:'Brazil',capital:'Brasília',region:'Americas',subregion:'South America',population:212000000,area:8515767,lat:-14.235,lng:-51.9253},
 {name:'United Kingdom',capital:'London',region:'Europe',subregion:'Northern Europe',population:69600000,area:243610,lat:55.3781,lng:-3.436},
 {name:'France',capital:'Paris',region:'Europe',subregion:'Western Europe',population:66500000,area:551695,lat:46.2276,lng:2.2137},
 {name:'Germany',capital:'Berlin',region:'Europe',subregion:'Western Europe',population:84000000,area:357114,lat:51.1657,lng:10.4515},
 {name:'Japan',capital:'Tokyo',region:'Asia',subregion:'Eastern Asia',population:123000000,area:377975,lat:36.2048,lng:138.2529},
 {name:'Australia',capital:'Canberra',region:'Oceania',subregion:'Australia and New Zealand',population:27000000,area:7692024,lat:-25.2744,lng:133.7751},
 {name:'Canada',capital:'Ottawa',region:'Americas',subregion:'North America',population:41300000,area:9984670,lat:56.1304,lng:-106.3468},
 {name:'Egypt',capital:'Cairo',region:'Africa',subregion:'Northern Africa',population:118000000,area:1002450,lat:26.8206,lng:30.8025},
 {name:'South Africa',capital:'Pretoria',region:'Africa',subregion:'Southern Africa',population:64000000,area:1221037,lat:-30.5595,lng:22.9375},
 {name:'Saudi Arabia',capital:'Riyadh',region:'Asia',subregion:'Western Asia',population:34500000,area:2149690,lat:23.8859,lng:45.0792},
 {name:'Turkey',capital:'Ankara',region:'Asia',subregion:'Western Asia',population:87000000,area:783562,lat:38.9637,lng:35.2433}
];
const earthNum=n=>Number(n||0).toLocaleString('en-US');
let earthFallbackFrame=null,earthFallbackCanvas=null,earthFallbackCtx=null,earthFallbackTexture=null,earthFallbackAngle=0,earthFallbackTilt=0,earthFallbackZoom=1,earthFallbackDrag=null;
function earthFallbackDraw(){
 const canvas=earthFallbackCanvas,ctx=earthFallbackCtx;
if(!canvas||!ctx)return;
 const w=canvas.clientWidth||canvas.width,h=canvas.clientHeight||canvas.height,d=Math.min(w*.68,h*.92),cx=w*.49,cy=h*.52,r=d/2;
 ctx.clearRect(0,0,w,h);
 ctx.save();
ctx.shadowColor='rgba(0,0,0,0)';
ctx.shadowBlur=0;
 const halo=ctx.createRadialGradient(cx,cy,r*.72,cx,cy,r*1.2);
halo.addColorStop(0,'#5edfff18');
halo.addColorStop(1,'#5edfff00');
ctx.fillStyle=halo;
ctx.beginPath();
ctx.arc(cx,cy,r*1.22,0,Math.PI*2);
ctx.fill();
ctx.restore();
 ctx.save();
ctx.translate(cx,cy);
ctx.rotate(earthFallbackTilt);
ctx.translate(-cx,-cy);
ctx.beginPath();
ctx.arc(cx,cy,r,0,Math.PI*2);
ctx.clip();
 const shade=ctx.createLinearGradient(cx-r,cy-r,cx+r,cy+r);
shade.addColorStop(0,'#d8f7ff');
shade.addColorStop(.16,'#397f9d');
shade.addColorStop(.52,'#092d50');
shade.addColorStop(1,'#020a20');
ctx.fillStyle=shade;
ctx.fillRect(cx-r,cy-r,d,d);
 if(earthFallbackTexture&&earthFallbackTexture.complete&&earthFallbackTexture.naturalWidth){
  const tw=earthFallbackTexture.naturalWidth,th=earthFallbackTexture.naturalHeight,drawW=d*2.05,drawH=d;
  const offset=((earthFallbackAngle%(Math.PI*2))/(Math.PI*2))*drawW;
  ctx.globalAlpha=.98;
  for(let k=-1;k<=1;k++)ctx.drawImage(earthFallbackTexture,0,0,tw,th,cx-d+offset+k*drawW,cy-r,drawW,drawH);
 }
 const oceanShade=ctx.createRadialGradient(cx-r*.35,cy-r*.4,r*.05,cx,cy,r*1.08);
oceanShade.addColorStop(0,'#ffffff08');
oceanShade.addColorStop(.58,'#001b3b00');
oceanShade.addColorStop(1,'#000615d9');
ctx.fillStyle=oceanShade;
ctx.fillRect(cx-r,cy-r,d,d);
 ctx.restore();
 /* No artificial blue outline: only a subtle natural atmospheric haze is drawn. */
 const atm=ctx.createRadialGradient(cx-r*.22,cy-r*.28,r*.65,cx,cy,r*1.15);
atm.addColorStop(.75,'#6feaff00');
atm.addColorStop(.92,'#75eaff35');
atm.addColorStop(1,'#79eaff00');
ctx.fillStyle=atm;
ctx.beginPath();
ctx.arc(cx,cy,r*1.12,0,Math.PI*2);
ctx.fill();
 if(earthSpin&&!earthFallbackDrag)earthFallbackAngle+=.0028;
 earthFallbackFrame=requestAnimationFrame(earthFallbackDraw);
}
function earthStartFallback(){
 const host=document.getElementById('earth-globe');
if(!host)return;
 if(earthFallbackFrame)cancelAnimationFrame(earthFallbackFrame);
 host.innerHTML='<canvas id="earth-fallback-canvas" aria-label="Realistic rotating Earth"></canvas>';
 earthFallbackCanvas=host.querySelector('canvas');
earthFallbackCtx=earthFallbackCanvas.getContext('2d');
 const resize=()=>{if(!earthFallbackCanvas)return;
const box=host.getBoundingClientRect(),ratio=Math.min(window.devicePixelRatio||1,1.7);
earthFallbackCanvas.style.width='100%';
earthFallbackCanvas.style.height='100%';
earthFallbackCanvas.width=Math.max(1,Math.floor(box.width*ratio));
earthFallbackCanvas.height=Math.max(1,Math.floor(box.height*ratio));
earthFallbackCtx.setTransform(ratio,0,0,ratio,0,0);
};
 resize();
window.addEventListener('resize',resize);
 earthFallbackTexture=new Image();
earthFallbackTexture.crossOrigin='anonymous';
earthFallbackTexture.onload=()=>{};
earthFallbackTexture.src='https://unpkg.com/three-globe/example/img/earth-blue-marble.jpg';
 earthFallbackCanvas.addEventListener('pointerdown',e=>{earthFallbackDrag={x:e.clientX,y:e.clientY,angle:earthFallbackAngle,tilt:earthFallbackTilt};earthFallbackCanvas.setPointerCapture(e.pointerId);});
 earthFallbackCanvas.addEventListener('pointermove',e=>{if(earthFallbackDrag){earthFallbackAngle=earthFallbackDrag.angle+(e.clientX-earthFallbackDrag.x)*.008;earthFallbackTilt=earthFallbackDrag.tilt+(e.clientY-earthFallbackDrag.y)*.004;}});
 earthFallbackCanvas.addEventListener('pointerup',()=>earthFallbackDrag=null);
 earthFallbackCanvas.addEventListener('pointercancel',()=>earthFallbackDrag=null);
 earthFallbackDraw();
}
function earthInit(){
 const host=document.getElementById('earth-globe');
if(!host)return;
 if(!earthGlobe&&!earthFallbackCanvas){
  if(typeof Globe!=='function'){earthStartFallback();
}
  else try{
   earthGlobe=Globe()(host,{rendererConfig:{antialias:true,alpha:true,powerPreference:'default',preserveDrawingBuffer:false}})
    .backgroundColor('rgba(0,0,0,0)')
    .globeImageUrl('https://unpkg.com/three-globe/example/img/earth-blue-marble.jpg')
    .bumpImageUrl('https://unpkg.com/three-globe/example/img/earth-topology.png').bumpScale(.075)
    .showAtmosphere(false).atmosphereAltitude(0)
    .width(host.clientWidth||340).height(host.clientHeight||300)
    .enablePointerInteraction(true).onGlobeClick(({lat,lng})=>earthSelectCoords(lat,lng))
    .polygonsData([])
    .polygonCapColor(feature=>feature===earthSelectedFeature?'rgba(255,255,255,.12)':'rgba(0,0,0,0)')
    .polygonSideColor(feature=>feature===earthSelectedFeature?'rgba(255,255,255,.08)':'rgba(0,0,0,0)')
    .polygonStrokeColor(feature=>feature===earthSelectedFeature?'#ffffff':'rgba(0,0,0,0)')
    .polygonAltitude(feature=>feature===earthSelectedFeature?.012:.0012)
    .polygonsTransitionDuration(650);
   earthGlobe.pointOfView({lat:22,lng:65,altitude:2.05},0);
   const ctl=earthGlobe.controls();
ctl.autoRotate=true;
ctl.autoRotateSpeed=.34;
ctl.enableDamping=true;
ctl.dampingFactor=.075;
ctl.enableRotate=true;
ctl.enableZoom=true;
ctl.enablePan=false;
ctl.rotateSpeed=1.55;
ctl.zoomSpeed=.9;
ctl.minPolarAngle=.0001;
ctl.maxPolarAngle=Math.PI-.0001;
ctl.minDistance=55;
ctl.maxDistance=900;
earthInstallSolarLighting();
ctl.addEventListener('end',()=>{if(earthSpin){ctl.autoRotate=true;}});
   window.addEventListener('resize',earthResize);
document.addEventListener('visibilitychange',earthVisibility);
  }catch(e){console.warn('3D globe unavailable; using textured globe fallback.',e);
earthGlobe=null;
earthStartFallback();
}
 }
 if(earthGlobe)earthGlobe.width(host.clientWidth||340).height(host.clientHeight||300);
 earthLoadCountries();
earthLoadBoundaries();
earthStartCounters();
earthEnsureSpin();
earthPreparePanel();
}
function earthInstallSolarLighting(){
 if(!earthGlobe||earthGlobe.__solarLightingInstalled)return;
 try{
  const scene=earthGlobe.scene();
  scene.traverse(object=>{
   if(object&&object.isDirectionalLight){
    object.position.set(-360,190,260);
    object.intensity=Math.max(1.15,object.intensity||0);
    object.castShadow=false;
   }
   if(object&&object.isAmbientLight)object.intensity=Math.min(object.intensity||.45,.48);
  });
  earthGlobe.__solarLightingInstalled=true;
 }catch(error){console.warn('Solar light adjustment unavailable; using globe default lighting.',error);
}
}
function earthVisibility(){if(!document.hidden&&earthGlobe&&earthSpin)earthEnsureSpin();
}
function earthEnsureSpin(){if(!earthGlobe)return;
const c=earthGlobe.controls();
c.enableRotate=true;
c.enableZoom=true;
c.enablePan=false;
c.rotateSpeed=1.55;
c.minPolarAngle=.0001;
c.maxPolarAngle=Math.PI-.0001;
c.enableDamping=true;
c.dampingFactor=.075;
if(earthSpin){c.autoRotate=true;
c.autoRotateSpeed=.34;
}}
function earthResize(){const host=document.getElementById('earth-globe');
if(earthGlobe&&host&&!document.getElementById('earth-page').classList.contains('hidden'))earthGlobe.width(host.clientWidth||340).height(host.clientHeight||300);
}
function earthNormalizeName(value){return String(value||'').normalize('NFD').replace(/[\u0300-\u036f]/g,'').toLowerCase().replace(/&/g,'and').replace(/[^a-z0-9]+/g,' ').trim();
}
function earthAliases(value){const q=earthNormalizeName(value);
const aliases={usa:'united states',us:'united states',uk:'united kingdom',uae:'united arab emirates',russia:'russian federation',iran:'iran islamic republic of',syria:'syrian arab republic',vietnam:'viet nam',laos:'lao peoples democratic republic',bolivia:'bolivia plurinational state of',venezuela:'venezuela bolivarian republic of',tanzania:'united republic of tanzania',moldova:'republic of moldova',brunei:'brunei darussalam',swaziland:'eswatini',burma:'myanmar','ivory coast':'cote divoire', 'south korea':'korea republic of', 'north korea':'korea democratic peoples republic of', 'czech republic':'czechia', 'cape verde':'cabo verde'};
return aliases[q]?[aliases[q]]:[];
}
function earthLoadCountries(){if(earthCountryReady)return;
earthCountryReady=true;
earthCountriesData=earthFallback.slice();
fetch('https://restcountries.com/v3.1/all?fields=name,capital,region,subregion,population,area,latlng,cca3,cca2,altSpellings,independent').then(r=>{if(!r.ok)throw Error('countries');return r.json();}).then(rows=>{earthCountriesData=rows.map(x=>({name:x.name?.common||x.name?.official||'',official:x.name?.official||'',capital:x.capital?.[0]||'—',region:x.region||'—',subregion:x.subregion||'—',population:x.population||0,area:x.area||0,lat:x.latlng?.[0]??0,lng:x.latlng?.[1]??0,cca3:x.cca3||'',cca2:x.cca2||'',aliases:Array.isArray(x.altSpellings)?x.altSpellings:[],independent:x.independent})).filter(x=>x.name&&x.independent!==false).sort((a,b)=>b.population-a.population);const status=document.getElementById('earth-search-status');if(status)status.textContent=earthCountriesData.length+' countries loaded';earthSyncPendingCountry();}).catch(()=>{const status=document.getElementById('earth-search-status');if(status)status.textContent='Offline country list active · connect to internet for the complete country list';});
}
function earthLoadBoundaries(){if(earthBoundaryLoading||earthGeoFeatures.length)return;
earthBoundaryLoading=true;
const urls=['https://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson','https://raw.githubusercontent.com/deldesierto/countries-geojson/master/countries.geojson'];
(async()=>{let error=null;for(const url of urls){try{const response=await fetch(url);if(!response.ok)throw Error('boundary data unavailable');const data=await response.json();const features=(data.features||[]).filter(f=>f.geometry&&(f.geometry.type==='Polygon'||f.geometry.type==='MultiPolygon'));if(features.length<150)throw Error('boundary data incomplete');earthGeoFeatures=features;if(earthGlobe)earthGlobe.polygonsData(earthSelectedFeature?[earthSelectedFeature]:[]);const input=document.getElementById('earth-country-input');const selectedQuery=earthNormalizeName(input?.value||'');if(selectedQuery){const selectedCountry=earthCountriesData.find(country=>[country.name,country.official,...(country.aliases||[])].map(earthNormalizeName).includes(selectedQuery));if(selectedCountry)earthSelectedFeature=earthFindBoundary(selectedCountry);}if(earthSelectedFeature)earthUpdateSelectedBoundary();const status=document.getElementById('earth-search-status');if(status)status.textContent='Global country boundaries loaded · '+features.length+' regions';return;}catch(e){error=e;}}throw error||Error('boundaries unavailable');})().catch(()=>{const status=document.getElementById('earth-search-status');if(status)status.textContent='Country search works; boundaries require an internet connection.';}).finally(()=>{earthBoundaryLoading=false;});
}
function earthSyncPendingCountry(){const input=document.getElementById('earth-country-input');
if(!input||!input.value||!earthGeoFeatures.length)return;
const q=earthNormalizeName(input.value);
const country=earthCountriesData.find(item=>earthCountryNames(item).some(name=>earthNormalizeName(name)===q));
if(country){earthSelectedFeature=earthFindBoundary(country);
earthUpdateSelectedBoundary();
}}
function earthCountryNames(country){return [country?.name,country?.official,...(country?.aliases||[]),...earthAliases(country?.name||'')].filter(Boolean);
}
function earthFindBoundary(country){if(!country||!earthGeoFeatures.length)return null;
const code=String(country.cca3||'').toUpperCase();
const names=earthCountryNames(country).map(earthNormalizeName).filter(Boolean);
return earthGeoFeatures.find(feature=>{const p=feature.properties||{};const codes=[p.ISO_A3,p.ISO_A3_EH,p.ADM0_A3,p.SOV_A3,p.iso_a3,p.ISO3,p.iso3,p.ADM0_A3_US,p.GU_A3].map(v=>String(v||'').toUpperCase());if(code&&codes.includes(code))return true;const labels=[p.ADMIN,p.name,p.name_en,p.NAME,p.NAME_EN,p.SOVEREIGNT,p.FORMAL_EN,p.ADMIN_EN,p.BRK_NAME,p.GEOUNIT,p.GU_A3];return labels.some(v=>names.includes(earthNormalizeName(v)));})||null;
}
function earthUpdateSelectedBoundary(){if(!earthGlobe)return;
earthGlobe.polygonsData(earthSelectedFeature?[earthSelectedFeature]:[]);
}
function earthSearchCountry(value){const box=document.getElementById('earth-suggest'),q=earthNormalizeName(value);
if(!q){box.style.display='none';
box.innerHTML='';
return;
}const terms=[q,...earthAliases(value).map(earthNormalizeName)];
const found=earthCountriesData.filter(c=>[c.name,c.official,...(c.aliases||[])].map(earthNormalizeName).some(name=>terms.some(term=>name.includes(term)||term.includes(name)))).slice(0,10);
box.innerHTML=found.map(c=>'<button type="button" onclick="earthPickCountry('+earthCountriesData.indexOf(c)+')"><b>'+earthEsc(c.name)+'</b> <span style="color:#9cc4c8">· '+earthEsc(c.region)+'</span></button>').join('');
box.style.display=found.length?'block':'none';
if(!found.length){const status=document.getElementById('earth-search-status');
if(status)status.textContent='No match found. Try the official or common country name.';
}}
function earthChooseFirst(){const input=document.getElementById('earth-country-input'),q=earthNormalizeName(input?.value||'');
if(!q)return;
const terms=[q,...earthAliases(input.value).map(earthNormalizeName)];
const found=earthCountriesData.find(c=>[c.name,c.official,...(c.aliases||[])].map(earthNormalizeName).some(n=>terms.includes(n)))||earthCountriesData.find(c=>[c.name,c.official,...(c.aliases||[])].map(earthNormalizeName).some(n=>terms.some(t=>n.includes(t))));
if(found)earthPickCountry(earthCountriesData.indexOf(found));
else{const status=document.getElementById('earth-search-status');
if(status)status.textContent='No match found. If the country list is loading, try again shortly.';
}}
function earthPickCountry(i){const c=earthCountriesData[i];
if(!c)return;
const box=document.getElementById('earth-suggest'),input=document.getElementById('earth-country-input');
if(box)box.style.display='none';
if(input)input.value=c.name;
earthCommitCountrySelection(c);
}
function earthShowCountry(c){document.getElementById('earth-country-name').textContent=c.name;
document.getElementById('earth-country-desc').textContent='Country overview · population and area are published estimates/data, not a live headcount.';
document.getElementById('earth-region').textContent=(c.region||'—')+' · '+(c.subregion||'');
document.getElementById('earth-capital').textContent=c.cca3||'—';
document.getElementById('earth-country-pop').textContent=earthNum(c.population);
document.getElementById('earth-country-area').textContent=earthNum(Math.round(c.area))+' km²';
document.getElementById('earth-search-status').textContent='Selected · '+c.name;
}
function earthSelectCountry(feature){const p=feature.properties||{},name=p.ADMIN||p.name||p.name_en||p.NAME_EN||'';
const c=earthCountriesData.find(x=>x.name.toLowerCase()===name.toLowerCase())||earthCountriesData.find(x=>name.toLowerCase().includes(x.name.toLowerCase())||x.name.toLowerCase().includes(name.toLowerCase()));
if(c)earthShowCountry(c);
else{document.getElementById('earth-country-name').textContent=name||'Selected country';
document.getElementById('earth-country-desc').textContent='Country selected on globe. Search by name to load detailed information.';
}}
function earthSelectCoords(lat,lng){document.getElementById('earth-country-name').textContent='Location selected';
document.getElementById('earth-country-desc').textContent='Latitude '+lat.toFixed(2)+'°, longitude '+lng.toFixed(2)+'°.';
document.getElementById('earth-region').textContent='Coordinates';
document.getElementById('earth-capital').textContent='—';
document.getElementById('earth-country-pop').textContent='—';
document.getElementById('earth-country-area').textContent='—';
}
function earthZoom(f){earthZoomByFactor(f);
}
function earthReset(){earthSelectedFeature=null;
if(earthGlobe){earthGlobe.polygonsData([]);
earthGlobe.pointOfView({lat:22,lng:65,altitude:2.05},700);
}if(earthFallbackCanvas){earthFallbackZoom=1;
earthFallbackCanvas.style.transform='scale(1)';
earthFallbackAngle=0;
earthFallbackTilt=0;
}earthSpin=true;
earthEnsureSpin();
earthUpdateSpinButton();
}
function earthToggleSpin(){earthSpin=!earthSpin;
if(earthGlobe)earthGlobe.controls().autoRotate=earthSpin;
earthUpdateSpinButton();
}
function earthStartCounters(){if(earthTimer)clearInterval(earthTimer);
const dayStart=new Date();
dayStart.setUTCHours(0,0,0,0);
earthStartedAt=dayStart.getTime();
const basePop=8200000000,birthPerSec=4.35,deathPerSec=1.95;
const update=()=>{const elapsed=Math.max(0,(Date.now()-earthStartedAt)/1000),pop=basePop+elapsed*(birthPerSec-deathPerSec);
const put=(id,val)=>{const el=document.getElementById(id);
if(el)el.textContent=val;
};
put('earth-pop', (pop/1e9).toFixed(3)+'B');
put('earth-births','+'+earthNum(Math.floor(elapsed*birthPerSec)));
put('earth-deaths','+'+earthNum(Math.floor(elapsed*deathPerSec)));
};
update();
earthTimer=setInterval(update,1000);
}
function earthStop(){if(earthTimer){clearInterval(earthTimer);
earthTimer=null;
}if(earthGlobe&&earthSpin)earthGlobe.controls().autoRotate=false;
if(earthFallbackFrame){cancelAnimationFrame(earthFallbackFrame);
earthFallbackFrame=null;
}}
// -----------------------------------------------------------------------------
// EARTH 4D INTERACTION, CAMERA, SEARCH AND ACCESSIBILITY HELPERS
// These helpers are intentionally scoped to the Earth observatory only.
// -----------------------------------------------------------------------------
// Keep the rotation control label synchronized with the actual animation state.
function earthUpdateSpinButton(){
 const button=document.getElementById('earth-spin');
 if(!button)return;
 button.textContent=earthSpin?'Ⅱ STOP ROTATION':'▶ RESUME ROTATION';
 button.setAttribute('aria-pressed',earthSpin?'true':'false');
 button.setAttribute('aria-label',earthSpin?'Stop automatic Earth rotation':'Resume automatic Earth rotation');
}

// Convert country names to a stable comparison key for international aliases.
function earthCountryKey(value){
 return earthNormalizeName(value)
  .replace(/\b(the|of|and)\b/g,' ')
  .replace(/\s+/g,' ')
  .trim();
}

// Resolve a country by its common name, official name, ISO-3 code or alias.
function earthResolveCountry(query){
 const key=earthCountryKey(query);
 if(!key)return null;
 const aliasKeys=[key,...earthAliases(query).map(earthCountryKey)];
 const exact=earthCountriesData.find(country=>{
  const names=earthCountryNames(country).map(earthCountryKey);
  return names.some(name=>aliasKeys.includes(name))||String(country.cca3||'').toLowerCase()===key;
 });
 if(exact)return exact;
 return earthCountriesData.find(country=>{
  const names=earthCountryNames(country).map(earthCountryKey);
  return names.some(name=>aliasKeys.some(alias=>name.startsWith(alias)||alias.startsWith(name)));
 })||null;
}

// Keep the search result list safe when country names contain punctuation.
function earthBuildSuggestion(country,index){
 const button=document.createElement('button');
 button.type='button';
 button.className='earth-country-suggestion';
 button.setAttribute('role','option');
 button.setAttribute('aria-label','Select '+country.name);
 const title=document.createElement('b');
 title.textContent=country.name;
 const region=document.createElement('span');
 region.textContent=' · '+(country.region||'Region unavailable');
 region.style.color='#9cc4c8';
 button.append(title,region);
 button.addEventListener('click',()=>earthPickCountry(index));
 return button;
}

// Rebuild suggestions with DOM nodes rather than injecting remote text as HTML.
function earthRenderSuggestions(matches){
 const box=document.getElementById('earth-suggest');
 if(!box)return;
 box.replaceChildren();
 matches.slice(0,10).forEach(country=>{
  const index=earthCountriesData.indexOf(country);
  if(index>=0)box.appendChild(earthBuildSuggestion(country,index));
 });
 box.style.display=matches.length?'block':'none';
 box.setAttribute('role','listbox');
}

// Return a valid camera target while protecting against incomplete country data.
function earthCountryCamera(country){
 const latitude=Number(country?.lat);
 const longitude=Number(country?.lng);
 return {
  lat:Number.isFinite(latitude)?Math.max(-89.5,Math.min(89.5,latitude)):0,
  lng:Number.isFinite(longitude)?Math.max(-180,Math.min(180,longitude)):0,
  altitude:.72
 };
}

// Animate the globe to a requested geographic position.
function earthMoveCamera(target,duration=1400){
 if(!earthGlobe||!target)return false;
 const camera={
  lat:Math.max(-89.5,Math.min(89.5,Number(target.lat)||0)),
  lng:Math.max(-180,Math.min(180,Number(target.lng)||0)),
  altitude:Math.max(.58,Math.min(5,Number(target.altitude)||1.2))
 };
 earthGlobe.pointOfView(camera,Math.max(0,Number(duration)||0));
 return true;
}

// A single selection transaction updates details, outline, camera and rotation.
function earthCommitCountrySelection(country){
 if(!country)return false;
 earthShowCountry(country);
 earthSelectedFeature=earthFindBoundary(country);
 earthUpdateSelectedBoundary();
 earthSpin=false;
 if(earthGlobe){
  earthGlobe.controls().autoRotate=false;
  earthMoveCamera(earthCountryCamera(country),1450);
 }
 if(earthFallbackCanvas){
  earthFallbackCenter(country);
 }
 earthUpdateSpinButton();
 if(earthGeoFeatures.length&&!earthSelectedFeature){
  const status=document.getElementById('earth-search-status');
  if(status)status.textContent='Selected '+country.name+' · this boundary is not present in the current map dataset.';
 }
 return true;
}

// Search can be called while the country dataset is still loading.
function earthSearchWhenReady(query){
 const country=earthResolveCountry(query);
 if(country){earthPickCountry(earthCountriesData.indexOf(country));
return true;
}
 const status=document.getElementById('earth-search-status');
 if(status)status.textContent=earthCountryReady?'No matching country found. Check the spelling.':'Country list is loading. Please try again in a moment.';
 return false;
}

// Keep keyboard users able to close the suggestion panel without changing pages.
function earthInstallSearchKeyboard(){
 const input=document.getElementById('earth-country-input');
 const box=document.getElementById('earth-suggest');
 if(!input||input.dataset.earthKeyboard==='ready')return;
 input.dataset.earthKeyboard='ready';
 input.addEventListener('keydown',event=>{
  if(event.key==='Escape'&&box){box.style.display='none';return;}
  if(event.key==='Enter'){
   event.preventDefault();
   earthSearchWhenReady(input.value);
  }
 });
}

// Provide a safe resize path for mobile orientation changes.
function earthRefreshViewport(){
 const host=document.getElementById('earth-globe');
 if(!host)return;
 if(earthGlobe){
  earthGlobe.width(Math.max(1,host.clientWidth)).height(Math.max(1,host.clientHeight));
 }
 if(earthFallbackCanvas){
  const ratio=Math.min(window.devicePixelRatio||1,1.7);
  const width=Math.max(1,host.clientWidth);
  const height=Math.max(1,host.clientHeight);
  earthFallbackCanvas.width=Math.floor(width*ratio);
  earthFallbackCanvas.height=Math.floor(height*ratio);
  earthFallbackCtx?.setTransform(ratio,0,0,ratio,0,0);
 }
}

// Normalize a point-of-view request and avoid impossible camera values.
function earthClampView(view){
 const safe=view||{};
 return {
  lat:Math.max(-89.9,Math.min(89.9,Number(safe.lat)||0)),
  lng:Math.max(-180,Math.min(180,Number(safe.lng)||0)),
  altitude:Math.max(.58,Math.min(5,Number(safe.altitude)||2.05))
 };
}

// Move the fallback globe in a predictable way when the 3D library is blocked.
function earthFallbackCenter(country){
 if(!earthFallbackCanvas||!country)return;
 const longitude=Number(country.lng)||0;
 const latitude=Number(country.lat)||0;
 earthFallbackAngle=-longitude*Math.PI/180;
 earthFallbackTilt=Math.max(-.7,Math.min(.7,latitude*Math.PI/180*.35));
 earthFallbackZoom=1.18;
 earthFallbackCanvas.style.transform='scale(1.18)';
}

// Return a short diagnostics snapshot for local debugging of the Earth panel.
function earthDiagnostics(){
 return {
  globeAvailable:!!earthGlobe,
  fallbackAvailable:!!earthFallbackCanvas,
  countryCount:earthCountriesData.length,
  boundaryCount:earthGeoFeatures.length,
  selectedCountry:document.getElementById('earth-country-name')?.textContent||'',
  selectedBoundary:!!earthSelectedFeature,
  autoRotation:earthSpin
 };
}

// Keep the button and controls consistent after a browser tab becomes active.
function earthResumeAfterVisibility(){
 if(document.hidden)return;
 if(earthGlobe){
  const controls=earthGlobe.controls();
  controls.autoRotate=!!earthSpin;
  controls.enabled=true;
 }
 if(earthSpin&&!earthFallbackFrame&&earthFallbackCanvas)earthFallbackDraw();
 earthUpdateSpinButton();
}

// Stop only Earth-specific animation loops when the user leaves this page.
function earthPausePanel(){
 if(earthGlobe&&earthGlobe.controls())earthGlobe.controls().autoRotate=false;
 if(earthFallbackFrame){cancelAnimationFrame(earthFallbackFrame);
earthFallbackFrame=null;
}
}

// Restore Earth rendering when the page is opened again.
function earthResumePanel(){
 const page=document.getElementById('earth-page');
 if(!page||page.classList.contains('hidden'))return;
 if(earthGlobe){
  earthRefreshViewport();
  earthGlobe.controls().autoRotate=!!earthSpin;
 }else if(earthFallbackCanvas&&!earthFallbackFrame){
  earthFallbackDraw();
 }
 earthUpdateSpinButton();
}

// Keep all country information fields populated even for partial API records.
function earthSafeCountryValue(value,fallback='—'){
 if(value===null||value===undefined||value==='')return fallback;
 return String(value);
}

// Format population and area without displaying NaN or Infinity.
function earthFormatMetric(value,suffix=''){
 const numeric=Number(value);
 if(!Number.isFinite(numeric)||numeric<0)return '—';
 return earthNum(Math.round(numeric))+(suffix?' '+suffix:'');
}

// Convert a GeoJSON feature's country label into a display-safe string.
function earthFeatureName(feature){
 const properties=feature?.properties||{};
 const candidates=[properties.ADMIN,properties.NAME,properties.NAME_EN,properties.name,properties.name_en,properties.SOVEREIGNT];
 return candidates.find(value=>typeof value==='string'&&value.trim())||'Unknown country';
}

// Compare a boundary feature to the selected country's common and official names.
function earthBoundaryNameMatches(feature,country){
 const featureName=earthCountryKey(earthFeatureName(feature));
 if(!featureName)return false;
 return earthCountryNames(country).some(name=>earthCountryKey(name)===featureName);
}

// Country codes vary across GeoJSON publishers; test all common ISO variants.
function earthBoundaryCodeMatches(feature,country){
 const code=String(country?.cca3||'').toUpperCase();
 if(!code)return false;
 const properties=feature?.properties||{};
 const candidates=[properties.ISO_A3,properties.ISO_A3_EH,properties.ADM0_A3,properties.SOV_A3,properties.iso_a3,properties.ISO3,properties.iso3,properties.ADM0_A3_US,properties.GU_A3];
 return candidates.some(value=>String(value||'').toUpperCase()===code);
}

// Resolve the best matching GeoJSON feature without relying on one property schema.
function earthBestBoundaryMatch(country){
 if(!country||!earthGeoFeatures.length)return null;
 const byCode=earthGeoFeatures.find(feature=>earthBoundaryCodeMatches(feature,country));
 if(byCode)return byCode;
 return earthGeoFeatures.find(feature=>earthBoundaryNameMatches(feature,country))||null;
}

// Keep a selected outline visible after the boundary file is loaded asynchronously.
function earthReapplySelectedBoundary(){
 if(!earthGlobe)return;
 if(!earthSelectedFeature){earthGlobe.polygonsData([]);
return;
}
 earthGlobe.polygonsData([earthSelectedFeature]);
}

// Check the search box after network responses arrive, without selecting partial text.
function earthResolveQueuedSearch(){
 const input=document.getElementById('earth-country-input');
 if(!input)return;
 const query=input.value.trim();
 if(!query)return;
 const country=earthResolveCountry(query);
 if(country&&earthGeoFeatures.length){
  earthSelectedFeature=earthBestBoundaryMatch(country);
  earthReapplySelectedBoundary();
 }
}

// Make the country panel usable if the remote service returns a partial response.
function earthCountryCountLabel(){
 const count=earthCountriesData.length;
 if(count===0)return 'Country database unavailable';
 return count+' countries available';
}

// Keep country suggestion matching tolerant of spacing and punctuation.
function earthCountryMatchesQuery(country,query){
 const terms=[earthCountryKey(query),...earthAliases(query).map(earthCountryKey)].filter(Boolean);
 const names=earthCountryNames(country).map(earthCountryKey);
 return names.some(name=>terms.some(term=>name===term||name.startsWith(term)||term.startsWith(name)));
}

// Return the closest country result first, then other partial matches.
function earthRankCountryMatches(query){
 const exact=[];
 const partial=[];
 earthCountriesData.forEach(country=>{
  const names=earthCountryNames(country).map(earthCountryKey);
  const key=earthCountryKey(query);
  if(names.includes(key))exact.push(country);
  else if(earthCountryMatchesQuery(country,query))partial.push(country);
 });
 return exact.concat(partial).slice(0,10);
}

// Rebuild the suggestion list using the shared ranking rules.
function earthSearchRanked(value){
 const input=document.getElementById('earth-country-input');
 const box=document.getElementById('earth-suggest');
 const query=String(value||'').trim();
 if(!query){if(box){box.replaceChildren();
box.style.display='none';
}return;
}
 const matches=earthRankCountryMatches(query);
 earthRenderSuggestions(matches);
 if(input)input.setAttribute('aria-expanded',matches.length?'true':'false');
 const status=document.getElementById('earth-search-status');
 if(status&&!matches.length)status.textContent='No matching country found.';
}

// Recenter the camera without changing the currently selected country.
function earthRecenter(){
 if(earthGlobe){
  const current=earthGlobe.pointOfView();
  earthMoveCamera(earthClampView(current),550);
 }
}

// Keep zoom operations inside a safe, comfortable range.
function earthZoomByFactor(factor){
 const amount=Number(factor);
 if(!Number.isFinite(amount)||amount<=0)return;
 if(earthGlobe){
  const current=earthGlobe.pointOfView();
  earthMoveCamera({...current,altitude:current.altitude/amount},420);
  return;
 }
 if(earthFallbackCanvas){
  earthFallbackZoom=Math.max(.75,Math.min(1.8,earthFallbackZoom*amount));
  earthFallbackCanvas.style.transform='scale('+earthFallbackZoom+')';
 }
}

// Update all accessible labels for the interactive globe and its buttons.
function earthSetAccessibility(){
 const globe=document.getElementById('earth-globe');
 if(globe){
  globe.setAttribute('role','img');
  globe.setAttribute('aria-label','Interactive Earth. Drag to rotate and use the zoom controls.');
  globe.setAttribute('tabindex','0');
 }
 earthUpdateSpinButton();
 earthInstallSearchKeyboard();
}

// Avoid registering resize and visibility handlers repeatedly across page visits.
function earthInstallLifecycle(){
 if(window.__mobileEarthLifecycleInstalled)return;
 window.__mobileEarthLifecycleInstalled=true;
 window.addEventListener('resize',earthRefreshViewport,{passive:true});
 window.addEventListener('orientationchange',()=>setTimeout(earthRefreshViewport,120),{passive:true});
 document.addEventListener('visibilitychange',earthResumeAfterVisibility);
}

// Add a keyboard shortcut for returning to the default Earth camera.
function earthInstallCameraKeyboard(){
 if(document.documentElement.dataset.earthCameraKeys==='ready')return;
 document.documentElement.dataset.earthCameraKeys='ready';
 document.addEventListener('keydown',event=>{
  const page=document.getElementById('earth-page');
  if(!page||page.classList.contains('hidden'))return;
  if(event.target&&['INPUT','TEXTAREA','SELECT'].includes(event.target.tagName))return;
  if(event.key==='0')earthReset();
  if(event.key==='+'||event.key==='=')earthZoomByFactor(1.2);
  if(event.key==='-')earthZoomByFactor(.84);
 });
}

// A consistent entry point for restoring the complete Earth experience.
function earthPreparePanel(){
 earthSetAccessibility();
 earthInstallLifecycle();
 earthInstallCameraKeyboard();
 earthResolveQueuedSearch();
 earthResumePanel();
}

// -----------------------------------------------------------------------------
// END EARTH 4D INTERACTION HELPERS
// -----------------------------------------------------------------------------

// ================= END LIVE EARTH =================


// ===============================
// ORIGINAL INSTRUMENTAL BACKGROUND GROOVE
// Starts only after the user taps the in-app music button.
// ===============================
let musicAudio = null;
let musicTimer = null;
let musicStep = 0;
let musicNoiseBuffer = null;

function musicSetButton(on){
 const b=document.getElementById('music-toggle');
 if(!b)return;
 const label=b.querySelector('b');
 if(label)label.textContent=on?'MUSIC ON':'MUSIC OFF';
 b.classList.toggle('is-on',on);
 b.setAttribute('aria-label',on?'Turn background music off':'Turn background music on');
}
function musicMakeNoiseBuffer(){
 const length=Math.floor(musicAudio.sampleRate*.24);
 const buffer=musicAudio.createBuffer(1,length,musicAudio.sampleRate);
 const data=buffer.getChannelData(0);
 for(let i=0;i<length;i++)data[i]=(Math.random()*2-1)*(1-i/length);
 return buffer;
}
function musicTone(time,frequency,duration,volume,type='triangle',filterFreq=0){
 const osc=musicAudio.createOscillator(),gain=musicAudio.createGain();
 const filter=filterFreq?musicAudio.createBiquadFilter():null;
 osc.type=type;osc.frequency.setValueAtTime(frequency,time);
 gain.gain.setValueAtTime(.0001,time);
 gain.gain.exponentialRampToValueAtTime(volume,time+.012);
 gain.gain.exponentialRampToValueAtTime(.0001,time+duration);
 if(filter){filter.type='lowpass';filter.frequency.setValueAtTime(filterFreq,time);osc.connect(filter);filter.connect(gain);}
 else osc.connect(gain);
 gain.connect(musicAudio.destination);osc.start(time);osc.stop(time+duration+.02);
}
function musicKick(time){
 const osc=musicAudio.createOscillator(),gain=musicAudio.createGain();
 osc.type='sine';osc.frequency.setValueAtTime(145,time);osc.frequency.exponentialRampToValueAtTime(42,time+.16);
 gain.gain.setValueAtTime(.0001,time);gain.gain.exponentialRampToValueAtTime(.42,time+.008);gain.gain.exponentialRampToValueAtTime(.0001,time+.23);
 osc.connect(gain);gain.connect(musicAudio.destination);osc.start(time);osc.stop(time+.24);
}
function musicSnare(time){
 const noise=musicAudio.createBufferSource(),filter=musicAudio.createBiquadFilter(),gain=musicAudio.createGain();
 noise.buffer=musicNoiseBuffer;filter.type='highpass';filter.frequency.value=1050;
 gain.gain.setValueAtTime(.0001,time);gain.gain.exponentialRampToValueAtTime(.15,time+.005);gain.gain.exponentialRampToValueAtTime(.0001,time+.16);
 noise.connect(filter);filter.connect(gain);gain.connect(musicAudio.destination);noise.start(time);noise.stop(time+.17);
 musicTone(time,185,.09,.055,'triangle');
}
function musicHat(time,accent=false){
 const noise=musicAudio.createBufferSource(),filter=musicAudio.createBiquadFilter(),gain=musicAudio.createGain();
 noise.buffer=musicNoiseBuffer;filter.type='highpass';filter.frequency.value=accent?8500:6800;
 gain.gain.setValueAtTime(.0001,time);gain.gain.exponentialRampToValueAtTime(accent?.035:.018,time+.002);gain.gain.exponentialRampToValueAtTime(.0001,time+.045);
 noise.connect(filter);filter.connect(gain);gain.connect(musicAudio.destination);noise.start(time);noise.stop(time+.05);
}
function musicBass(time,frequency){
 musicTone(time,frequency,.22,.13,'sawtooth',420);
}
function musicPluck(time,frequency){
 musicTone(time,frequency,.19,.075,'triangle',2600);
 musicTone(time,frequency*2,.11,.018,'sine');
}
function musicPad(time,frequencies){
 frequencies.forEach((frequency,index)=>{
  const osc=musicAudio.createOscillator(),gain=musicAudio.createGain(),filter=musicAudio.createBiquadFilter();
  osc.type='sawtooth';osc.frequency.setValueAtTime(frequency,time);
  filter.type='lowpass';filter.frequency.value=1150;
  gain.gain.setValueAtTime(.0001,time);gain.gain.linearRampToValueAtTime(.026,time+.12);gain.gain.setValueAtTime(.022,time+.48);gain.gain.exponentialRampToValueAtTime(.0001,time+.9);
  osc.connect(filter);filter.connect(gain);gain.connect(musicAudio.destination);osc.start(time);osc.stop(time+.92);
 });
}
function musicSchedule(){
 if(!musicAudio||musicAudio.state!=='running')return;
 const now=musicAudio.currentTime+.035,step=musicStep%16;
 const chords=[
  [220.00,261.63,329.63],   // Am
  [174.61,220.00,261.63],   // F
  [130.81,164.81,196.00],   // C
  [196.00,246.94,293.66]    // G
 ];
 const bass=[110,87.31,65.41,98];
 const melody=[440,523.25,659.25,523.25,392,440,523.25,659.25,
               493.88,587.33,739.99,587.33,392,493.88,587.33,659.25];
 if(step===0)musicPad(now,chords[Math.floor(musicStep/16)%4]);
 if(step===0||step===8)musicKick(now);
 if(step===4||step===12)musicSnare(now);
 if(step%2===0)musicHat(now,step===0||step===8);
 if(step===0||step===4||step===8||step===12)musicBass(now,bass[Math.floor(musicStep/16)%4]);
 if(step%2===0)musicPluck(now,melody[step]);
 musicStep++;
}
async function toggleBackgroundMusic(){
 const b=document.getElementById('music-toggle');
 if(musicTimer!==null){
  clearInterval(musicTimer);musicTimer=null;
  if(musicAudio){musicAudio.close().catch(()=>{});musicAudio=null;}
  musicNoiseBuffer=null;musicSetButton(false);return;
 }
 try{
  const AudioCtx=window.AudioContext||window.webkitAudioContext;
  if(!AudioCtx)throw new Error('Audio unavailable');
  musicAudio=new AudioCtx();
  await musicAudio.resume();
  musicNoiseBuffer=musicMakeNoiseBuffer();musicStep=0;
  musicSchedule();musicTimer=setInterval(musicSchedule,143);musicSetButton(true);
 }catch(e){
  if(musicAudio){musicAudio.close().catch(()=>{});musicAudio=null;}
  musicSetButton(false);
  if(b){const label=b.querySelector('b');if(label)label.textContent='MUSIC N/A';}
 }
}
// ================= END BACKGROUND MUSIC =================

// ================= END BACKGROUND MUSIC =================

// INITIAL SETUP

resetGuess();
resetSnake();
drawFlappy();
drawCar();
renderNotes();
showPage("login-page");

</script>
</body>
</html>
"""

components.html(APP, height=950, scrolling=True)

