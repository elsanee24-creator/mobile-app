import json
import streamlit as st

st.set_page_config(
    page_title="mobile.app",
    page_icon="📱",
    layout="wide",
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
.login-actions button{padding-top:16px;padding-bottom:16px}
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
.card,.clock-panel,.tile,.wide-tile,.row-tile,.home-shortcut,.nb-panel,.school-option,.school-text-card{box-shadow:inset 0 2px 0 #ffffff35,inset 0 -5px 0 #00000018,0 10px 20px #06172b38}
.home-shortcut{border-width:1px 1px 3px}
.home-shortcut:nth-child(1){background:linear-gradient(145deg,#287e91,#164b69);border-color:#8ce9df}
.home-shortcut:nth-child(2){background:linear-gradient(145deg,#7452a8,#39275f);border-color:#c7a6ff}
.home-shortcut:nth-child(3){background:linear-gradient(145deg,#a87836,#654329);border-color:#ffe0a8}
.home-shortcut.neon-shortcut{background:linear-gradient(145deg,#5d42a4,#27214f);border-color:#c4a4ff}
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
/* TWO-SCREEN HOME NAVIGATION + WEATHER FORECAST */
.home-pager{display:flex;width:200%;align-items:flex-start;transition:transform .32s cubic-bezier(.2,.75,.25,1);touch-action:pan-y;will-change:transform}
.home-panel{width:50%;min-width:50%;padding:0 1px}
.home-pagination{display:flex;align-items:center;justify-content:space-between;margin:13px 0 2px;padding:0 8px}
.home-arrow{width:38px;height:34px;border-radius:12px;color:#effffb;background:#ffffff20;border:1px solid #ffffff45;font-size:23px;line-height:1}
.home-dots{display:flex;gap:8px;align-items:center}
.home-dot{width:8px;height:8px;padding:0;border-radius:50%;background:#ffffff55;box-shadow:none}
.home-dot.active{width:22px;border-radius:8px;background:linear-gradient(90deg,#65f5c1,#8dbbff)}
.home-second-heading{display:flex;align-items:center;gap:12px;margin:18px 3px 18px;padding:17px;border-radius:18px;background:linear-gradient(120deg,#ffffff22,#ffffff0c);border:1px solid #ffffff35}
.home-second-heading>span{font-size:31px}.home-second-heading b{display:block;font-size:17px;letter-spacing:1px}.home-second-heading small{display:block;color:#c5e3e2;font-size:10px;margin-top:4px}
.home-shortcuts-second{grid-template-columns:repeat(2,minmax(0,1fr));gap:11px;margin-top:0}
.home-shortcuts-second .home-shortcut{min-height:105px}.home-shortcuts-second .home-shortcut .emoji{font-size:28px}.home-shortcuts-second .home-shortcut b{font-size:11px}
.weather-shortcut{background:linear-gradient(145deg,#176c91,#244a83)!important;border-color:#9be8ff!important}
.home-page-note{text-align:center;color:#c5e3e2;font-size:10px;margin:17px 0 4px}
.weather-hero{padding:16px;border-radius:23px;background:linear-gradient(145deg,#164c70,#246a83 55%,#4d5793);border:1px solid #9ce8f2;box-shadow:inset 0 2px 0 #ffffff35,0 12px 25px #06172b40}
.weather-search{display:flex;gap:7px}.weather-search .field{flex:1;min-width:0;margin:0}.weather-search-btn{padding:0 13px;border-radius:12px;background:linear-gradient(100deg,#65f5c1,#7ddcff);font-size:10px}
.weather-status{font-size:10px;color:#d2f4f2;margin:10px 2px 12px}.weather-current{display:flex;justify-content:space-between;align-items:center;min-height:135px}.weather-place{font-size:19px;font-weight:900}.weather-condition{font-size:12px;color:#d4f4f1;margin-top:4px}.weather-temp{font-size:57px;font-weight:900;line-height:1.15;margin-top:6px}.weather-range{font-size:11px;color:#d2f4f2}.weather-icon{font-size:65px;filter:drop-shadow(0 7px 9px #07172c55)}
.weather-stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:6px;margin-top:13px}.weather-stats>div{padding:9px 5px;border-radius:12px;background:#ffffff17;text-align:center}.weather-stats small{display:block;font-size:8px;color:#d2eeec}.weather-stats b{display:block;font-size:12px;margin-top:5px}
.weather-section{margin-top:18px}.weather-section-title{display:flex;align-items:center;justify-content:space-between}.weather-section-title h3{font-size:16px;margin:0}.weather-section-title span{font-size:9px;letter-spacing:1px;color:#bcece7}.weather-hourly{display:flex;gap:8px;overflow-x:auto;padding:10px 1px 8px;scrollbar-width:thin}.weather-hour{flex:0 0 66px;text-align:center;padding:10px 5px;border-radius:14px;background:#ffffff16;border:1px solid #ffffff20}.weather-hour small{display:block;font-size:10px;color:#d4e9ed}.weather-hour span{display:block;font-size:21px;margin:7px 0}.weather-hour b{font-size:13px}
.weather-daily{display:grid;gap:7px;margin-top:10px}.weather-day{display:grid;grid-template-columns:1fr 30px 45px 45px;align-items:center;gap:7px;padding:10px 11px;border-radius:13px;background:#ffffff14;border:1px solid #ffffff20}.weather-day b{font-size:11px}.weather-day span{font-size:17px;text-align:center}.weather-day small{font-size:10px;color:#d1e8e8;text-align:right}.weather-day strong{font-size:11px;text-align:right}
.weather-error{padding:12px;border-radius:12px;background:#8c303c55;color:#fff;font-size:12px}
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
/* SOLAR SYSTEM EXPLORER */
#solar-page{color:#eef5ff}
.solar-hero{position:relative;overflow:hidden;padding:14px;border:1px solid #ffffff20;border-radius:20px;background:radial-gradient(ellipse at 50% 42%,#172c52 0%,#091326 42%,#030711 78%);box-shadow:inset 0 1px #ffffff16,0 14px 28px #0007}
.solar-kicker{font-size:9px;letter-spacing:2px;color:#8bd9ff;font-weight:800}
.solar-hero h2{font-size:22px;line-height:1.15;margin:8px 0 5px;color:#fff}
.solar-hero>p{font-size:11px;color:#b7c8e4;line-height:1.55;margin:0 0 12px}
.solar-stage{position:relative;width:100%;height:310px;overflow:hidden;border-radius:15px;background:radial-gradient(1px 1px at 8% 16%,#fff 98%,transparent),radial-gradient(1px 1px at 18% 78%,#c6dcff 98%,transparent),radial-gradient(1.5px 1.5px at 32% 28%,#fff 98%,transparent),radial-gradient(1px 1px at 47% 86%,#d7e8ff 98%,transparent),radial-gradient(1px 1px at 61% 13%,#fff 98%,transparent),radial-gradient(1px 1px at 76% 66%,#d8e8ff 98%,transparent),radial-gradient(1px 1px at 92% 31%,#fff 98%,transparent),radial-gradient(ellipse at center,#0c1b35,#030711 72%)}
.solar-system{position:absolute;left:50%;top:50%;width:270px;height:270px;transform:translate(-50%,-50%)}
.solar-sun{position:absolute;left:50%;top:50%;width:42px;height:42px;transform:translate(-50%,-50%);border-radius:50%;z-index:5;background-image:radial-gradient(circle at 32% 28%,#ffffff22 0 8%,transparent 36%),url("https://www.solarsystemscope.com/textures/download/2k_sun.jpg");background-size:cover;background-position:center;box-shadow:0 0 13px 5px #ffcf6b,0 0 33px 15px #ff8a2b99,0 0 65px 25px #ff5b1d66,inset -8px -6px 12px #65160099}
.solar-orbit{position:absolute;left:50%;top:50%;border:1px solid #8bb5e52c;border-radius:50%;transform:translate(-50%,-50%);animation:solarOrbit linear infinite}
.solar-orbit .solar-body{position:absolute;left:50%;top:0;border-radius:50%;transform:translate(-50%,-50%);box-shadow:0 0 9px #ffffff55}
.solar-orbit.o1{width:54px;height:54px;animation-duration:5s}.solar-orbit.o2{width:78px;height:78px;animation-duration:8s}.solar-orbit.o3{width:105px;height:105px;animation-duration:12s}.solar-orbit.o4{width:132px;height:132px;animation-duration:18s}.solar-orbit.o5{width:174px;height:174px;animation-duration:28s}.solar-orbit.o6{width:213px;height:213px;animation-duration:38s}.solar-orbit.o7{width:246px;height:246px;animation-duration:48s}.solar-orbit.o8{width:276px;height:276px;animation-duration:60s}
.solar-orbit .solar-body{background-size:cover;background-position:center;box-shadow:inset -3px -2px 5px #000b,0 0 8px #ffffff66}
.solar-orbit.o1 .solar-body{width:6px;height:6px;background-image:url("https://www.solarsystemscope.com/textures/download/2k_mercury.jpg")}
.solar-orbit.o2 .solar-body{width:8px;height:8px;background-image:url("https://www.solarsystemscope.com/textures/download/2k_venus_surface.jpg")}
.solar-orbit.o3 .solar-body{width:10px;height:10px;background-image:url("https://www.solarsystemscope.com/textures/download/2k_earth_daymap.jpg")}
.solar-orbit.o4 .solar-body{width:8px;height:8px;background-image:url("https://www.solarsystemscope.com/textures/download/2k_mars.jpg")}
.solar-orbit.o5 .solar-body{width:18px;height:18px;background-image:url("https://www.solarsystemscope.com/textures/download/2k_jupiter.jpg")}
.solar-orbit.o6 .solar-body{width:16px;height:16px;background-image:url("https://www.solarsystemscope.com/textures/download/2k_saturn.jpg");outline:2px solid #d9c18a88;outline-offset:2px}
.solar-orbit.o7 .solar-body{width:12px;height:12px;background-image:url("https://www.solarsystemscope.com/textures/download/2k_uranus.jpg")}
.solar-orbit.o8 .solar-body{width:11px;height:11px;background-image:url("https://www.solarsystemscope.com/textures/download/2k_neptune.jpg")}
.solar-orbit.o6 .solar-body:after{content:"";position:absolute;left:50%;top:50%;width:185%;height:48%;border:1px solid #d8c28a99;border-radius:50%;transform:translate(-50%,-50%) rotate(-18deg);pointer-events:none}
@keyframes solarOrbit{from{transform:translate(-50%,-50%) rotate(0)}to{transform:translate(-50%,-50%) rotate(360deg)}}
.solar-stage-label{position:absolute;left:10px;bottom:9px;font-size:8px;letter-spacing:1px;color:#8fa9cb}
.solar-toolbar{display:flex;gap:7px;flex-wrap:wrap;margin:10px 0}.solar-tool{border:1px solid #4d759d;background:linear-gradient(135deg,#183b60,#152847);color:#eaf5ff;border-radius:10px;padding:9px 11px;font-size:10px;font-weight:800}.solar-tool.active{border-color:#6fe0d3;background:linear-gradient(135deg,#075d61,#174c73)}
.solar-planet-list{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:7px;margin:12px 0}.solar-pick{min-width:0;padding:9px 4px;border:1px solid #ffffff20;border-radius:12px;background:#101d32;color:#e8f1ff;font-size:10px;font-weight:800}.solar-pick .dot{display:block;width:19px;height:19px;border-radius:50%;margin:0 auto 6px;box-shadow:0 0 9px #ffffff44}.solar-pick.selected{border-color:#69e6d1;background:linear-gradient(145deg,#124c59,#172d50);box-shadow:0 0 0 1px #69e6d144}

.solar-pick .dot{background-size:cover!important;background-position:center!important;box-shadow:inset -3px -2px 5px #000a,0 0 9px #ffffff55!important}
#solar-pick-mercury .dot{background-image:url("https://www.solarsystemscope.com/textures/download/2k_mercury.jpg")!important}
#solar-pick-venus .dot{background-image:url("https://www.solarsystemscope.com/textures/download/2k_venus_surface.jpg")!important}
#solar-pick-earth .dot{background-image:url("https://www.solarsystemscope.com/textures/download/2k_earth_daymap.jpg")!important}
#solar-pick-mars .dot{background-image:url("https://www.solarsystemscope.com/textures/download/2k_mars.jpg")!important}
#solar-pick-jupiter .dot{background-image:url("https://www.solarsystemscope.com/textures/download/2k_jupiter.jpg")!important}
#solar-pick-saturn .dot{background-image:url("https://www.solarsystemscope.com/textures/download/2k_saturn.jpg")!important}
#solar-pick-uranus .dot{background-image:url("https://www.solarsystemscope.com/textures/download/2k_uranus.jpg")!important}
#solar-pick-neptune .dot{background-image:url("https://www.solarsystemscope.com/textures/download/2k_neptune.jpg")!important}
.solar-detail-orb{background-size:cover;background-position:center;box-shadow:inset -11px -8px 15px #000b,0 0 18px #ffffff35}
.solar-detail-orb.sun-selected{box-shadow:0 0 18px 5px #ffb13b99,0 0 42px 12px #ff7b2e66,inset -8px -6px 12px #65160099}
.solar-detail{padding:13px;border:1px solid #ffffff20;border-radius:17px;background:linear-gradient(145deg,#101f38,#0a1425);margin-top:10px}.solar-detail-top{display:flex;align-items:center;gap:11px}.solar-detail-orb{width:53px;height:53px;flex:0 0 53px;border-radius:50%;box-shadow:inset -9px -7px 14px #0009,0 0 18px #ffffff25}.solar-detail h3{margin:0;font-size:19px;color:#fff}.solar-detail small{font-size:9px;color:#9db6d6;letter-spacing:1px}.solar-detail p{font-size:11px;line-height:1.65;color:#c7d5e9;margin:10px 0}.solar-facts{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:7px}.solar-fact{padding:9px;border-radius:10px;background:#ffffff09;border:1px solid #ffffff12}.solar-fact b{display:block;font-size:12px;color:#fff}.solar-fact span{font-size:8px;color:#9db6d6;letter-spacing:.7px}.solar-section-title{font-size:13px;color:#eaf4ff;margin:15px 0 8px}.solar-moon-list{display:flex;flex-wrap:wrap;gap:6px}.solar-moon-chip{font-size:9px;padding:6px 8px;border-radius:20px;background:#21324b;border:1px solid #5c789b;color:#d9e9ff}.solar-note{font-size:9px;color:#91a8c6;line-height:1.55;margin:9px 2px 0}
@media(max-width:370px){.solar-stage{height:285px}.solar-system{transform:translate(-50%,-50%) scale(.88)}.solar-planet-list{gap:5px}.solar-pick{font-size:9px}}
@media(prefers-reduced-motion:reduce){.solar-orbit{animation-play-state:paused!important}}

/* Planet texture fallback gradients keep every world visible if remote textures fail. */
.solar-orbit.o1 .solar-body{background-image:radial-gradient(circle at 28% 24%,#f4eee2 0%,#aaa39a 38%,#55545a 72%,#252832 100%),url("https://www.solarsystemscope.com/textures/download/2k_mercury.jpg")}
.solar-orbit.o2 .solar-body{background-image:radial-gradient(circle at 28% 24%,#fff0bf 0%,#d6a15d 45%,#8e5935 78%,#38251f 100%),url("https://www.solarsystemscope.com/textures/download/2k_venus_surface.jpg")}
.solar-orbit.o3 .solar-body{background-image:radial-gradient(circle at 28% 24%,#baf4ff 0%,#268ed0 43%,#17603c 62%,#071d55 100%),url("https://www.solarsystemscope.com/textures/download/2k_earth_daymap.jpg")}
.solar-orbit.o4 .solar-body{background-image:radial-gradient(circle at 28% 24%,#ffd4a2 0%,#c65d37 48%,#743323 78%,#291b20 100%),url("https://www.solarsystemscope.com/textures/download/2k_mars.jpg")}
.solar-orbit.o5 .solar-body{background-image:repeating-linear-gradient(8deg,#e9c9a2 0 3px,#a96f4f 4px 6px,#f2dfbf 7px 9px),url("https://www.solarsystemscope.com/textures/download/2k_jupiter.jpg")}
.solar-orbit.o6 .solar-body{background-image:radial-gradient(circle at 28% 24%,#fff2cb 0%,#d3b17c 48%,#8d6b48 80%,#3a3029 100%),url("https://www.solarsystemscope.com/textures/download/2k_saturn.jpg")}
.solar-orbit.o7 .solar-body{background-image:radial-gradient(circle at 28% 24%,#e0ffff 0%,#91dce0 48%,#478eaa 80%,#1b3d59 100%),url("https://www.solarsystemscope.com/textures/download/2k_uranus.jpg")}
.solar-orbit.o8 .solar-body{background-image:radial-gradient(circle at 28% 24%,#b9dcff 0%,#426fce 48%,#203b91 80%,#101d52 100%),url("https://www.solarsystemscope.com/textures/download/2k_neptune.jpg")}
#solar-pick-mercury .dot{background-image:radial-gradient(circle at 28% 24%,#f4eee2 0%,#aaa39a 38%,#55545a 72%,#252832 100%),url("https://www.solarsystemscope.com/textures/download/2k_mercury.jpg")!important}
#solar-pick-venus .dot{background-image:radial-gradient(circle at 28% 24%,#fff0bf 0%,#d6a15d 45%,#8e5935 78%,#38251f 100%),url("https://www.solarsystemscope.com/textures/download/2k_venus_surface.jpg")!important}
#solar-pick-earth .dot{background-image:radial-gradient(circle at 28% 24%,#baf4ff 0%,#268ed0 43%,#17603c 62%,#071d55 100%),url("https://www.solarsystemscope.com/textures/download/2k_earth_daymap.jpg")!important}
#solar-pick-mars .dot{background-image:radial-gradient(circle at 28% 24%,#ffd4a2 0%,#c65d37 48%,#743323 78%,#291b20 100%),url("https://www.solarsystemscope.com/textures/download/2k_mars.jpg")!important}
#solar-pick-jupiter .dot{background-image:repeating-linear-gradient(8deg,#e9c9a2 0 3px,#a96f4f 4px 6px,#f2dfbf 7px 9px),url("https://www.solarsystemscope.com/textures/download/2k_jupiter.jpg")!important}
#solar-pick-saturn .dot{background-image:radial-gradient(circle at 28% 24%,#fff2cb 0%,#d3b17c 48%,#8d6b48 80%,#3a3029 100%),url("https://www.solarsystemscope.com/textures/download/2k_saturn.jpg")!important}
#solar-pick-uranus .dot{background-image:radial-gradient(circle at 28% 24%,#e0ffff 0%,#91dce0 48%,#478eaa 80%,#1b3d59 100%),url("https://www.solarsystemscope.com/textures/download/2k_uranus.jpg")!important}
#solar-pick-neptune .dot{background-image:radial-gradient(circle at 28% 24%,#b9dcff 0%,#426fce 48%,#203b91 80%,#101d52 100%),url("https://www.solarsystemscope.com/textures/download/2k_neptune.jpg")!important}
.solar-stage{height:285px}

/* END SOLAR SYSTEM EXPLORER */

/* QURAN READER — added feature */
#quran-page .quran-panel{padding:13px;border-radius:17px;background:linear-gradient(145deg,#ffffff20,#ffffff0c);border:1px solid #ffffff35;margin:10px 0}
#quran-page .quran-control{width:100%;padding:11px;border-radius:12px;border:1px solid #ffffff55;background:#f5fffc;color:#173b42;font-size:13px;margin:5px 0 10px}
#quran-page label{display:block;font-size:11px;color:#d9f4ed;font-weight:800;margin-top:5px}
#quran-page .quran-arabic{font-family:'Amiri','Scheherazade New','Noto Naskh Arabic',serif;direction:rtl;text-align:right;font-size:2rem;line-height:1.65;margin:15px 0;color:#fff;overflow-wrap:anywhere}
#quran-page .quran-translation{font-size:13px;line-height:1.7;color:#e1f0ec;margin:7px 0 15px}
#quran-page .quran-bismillah{text-align:center;font-family:'Amiri','Noto Naskh Arabic',serif;font-size:1.8rem;line-height:1.8;margin:15px 0;color:#fff}
#quran-page .quran-ayah{padding:10px 0;border-bottom:1px solid #ffffff25}
#quran-page .quran-ayah audio{width:100%;height:36px;margin:5px 0}
#quran-page .quran-meta{font-size:11px;color:#c4e4dd;line-height:1.6}
#quran-page .quran-status{font-size:12px;color:#cffff0;min-height:20px;margin:7px 0}
#quran-page .quran-range{width:100%;accent-color:#65f5c1;margin:8px 0 12px}




/* REQUESTED DESIGN UPDATE: three-tone premium palette, wider phone and compact spacing. */
body{background-attachment:fixed;background-image:radial-gradient(ellipse at 12% 8%,#79f3d755,transparent 32%),radial-gradient(ellipse at 88% 20%,#a58aff55,transparent 34%),radial-gradient(ellipse at 50% 100%,#ff927b40,transparent 38%),linear-gradient(135deg,#071d28 0%,#123e48 48%,#34254f 100%)}
.phone{background:linear-gradient(135deg,#8ff5d7 0%,#8ba8ff 52%,#ffb18f 100%);}
.screen{padding:12px 13px 18px;background:radial-gradient(circle at 8% 0%,#39e9bd45,transparent 34%),radial-gradient(circle at 95% 28%,#a47bff45,transparent 38%),linear-gradient(145deg,#102d3a 0%,#174653 52%,#30264f 100%)}
.dynamic-island{width:92px;height:23px;margin:0 auto 8px;border-radius:20px;background:linear-gradient(110deg,#020509,#10151b);border:1px solid #52606b88;box-shadow:inset 0 1px 3px #ffffff22,0 2px 8px #0006;display:flex;align-items:center;justify-content:flex-end;padding:0 10px;position:relative;z-index:3}
.dynamic-island span{width:7px;height:7px;border-radius:50%;background:#172b3d;box-shadow:inset 0 0 3px #65a6d8,0 0 4px #4c8ecb;margin-right:2px}
.dynamic-island i{width:5px;height:5px;border-radius:50%;background:#172d3b;box-shadow:0 0 3px #3c8bba}
.topbar{margin:0 4px 13px}
.section{margin:12px 0}
.card{padding:12px}
.page-head{margin:3px 0 12px}
.tile{min-height:84px;padding:9px 6px}
@media(max-width:480px){.phone{max-width:100%;padding:7px;border-radius:30px}.screen{padding:10px 11px 16px;border-radius:24px}.dynamic-island{height:21px;width:86px;margin-bottom:7px}}

.screen:has(#games-page:not(.hidden)){background:radial-gradient(circle at 8% 5%,#55e6d055,transparent 35%),radial-gradient(circle at 92% 20%,#b07bff55,transparent 38%),linear-gradient(145deg,#172b50,#34265e 55%,#743d68)}
.screen:has(#solar-page:not(.hidden)){background:radial-gradient(circle at 10% 5%,#54d9d955,transparent 35%),radial-gradient(circle at 92% 20%,#8c83ff55,transparent 38%),linear-gradient(145deg,#071a30,#142d50 55%,#34264e)}
.screen:has(#house-page:not(.hidden)){background:radial-gradient(circle at 8% 5%,#e7bd8055,transparent 35%),radial-gradient(circle at 92% 20%,#93c7d955,transparent 38%),linear-gradient(145deg,#253849,#425166 55%,#68475a)}
.screen:has(#quran-page:not(.hidden)){background:radial-gradient(circle at 8% 5%,#65e9bd55,transparent 35%),radial-gradient(circle at 92% 20%,#e0b36b44,transparent 38%),linear-gradient(145deg,#123c43,#18565a 55%,#3d3458)}
.screen:has(#typing-page:not(.hidden)){background:radial-gradient(circle at 8% 5%,#6ae6d355,transparent 35%),radial-gradient(circle at 92% 20%,#ff9cbb44,transparent 38%),linear-gradient(145deg,#302653,#55335f 55%,#78465b)}


/* SECTION-SPECIFIC COLOUR THEMES — individual colour mixes for each screen. */
.screen:has(#app-login-page:not(.hidden)){background:radial-gradient(circle at 8% 8%,#ff6f9160,transparent 34%),radial-gradient(circle at 92% 18%,#63b8ff55,transparent 36%),linear-gradient(145deg,#301c43,#63304f 54%,#173c5a)}
.screen:has(#guess-page:not(.hidden)){background:radial-gradient(circle at 10% 8%,#ffce5b55,transparent 34%),radial-gradient(circle at 92% 18%,#ff718755,transparent 36%),linear-gradient(145deg,#4b2a3c,#78452e 55%,#34305c)}
.screen:has(#flappy-page:not(.hidden)){background:radial-gradient(circle at 8% 8%,#ffe66d66,transparent 34%),radial-gradient(circle at 92% 18%,#55e5e055,transparent 36%),linear-gradient(145deg,#15516d,#258b9a 55%,#3e668d)}
.screen:has(#snake-page:not(.hidden)){background:radial-gradient(circle at 8% 8%,#a5ff7655,transparent 34%),radial-gradient(circle at 92% 18%,#58d9ff44,transparent 36%),linear-gradient(145deg,#123b31,#17634b 55%,#244c70)}
.screen:has(#car-page:not(.hidden)){background:radial-gradient(circle at 8% 8%,#ffcc5b55,transparent 34%),radial-gradient(circle at 92% 18%,#ff758a44,transparent 36%),linear-gradient(145deg,#422c38,#795039 55%,#35476c)}
.screen:has(#settings-page:not(.hidden)){background:radial-gradient(circle at 8% 8%,#ff9bc855,transparent 34%),radial-gradient(circle at 92% 18%,#8e9aff55,transparent 36%),linear-gradient(145deg,#46294e,#75416a 55%,#38446f)}
.screen:has(#about-page:not(.hidden)){background:radial-gradient(circle at 8% 8%,#ffe27a55,transparent 34%),radial-gradient(circle at 92% 18%,#ff9d7350,transparent 36%),linear-gradient(145deg,#51402c,#86543e 55%,#54416e)}
.screen:has(#school-page:not(.hidden)),.screen:has(#school-history-page:not(.hidden)),.screen:has(#school-mission-page:not(.hidden)){background:radial-gradient(circle at 8% 8%,#69dfff55,transparent 34%),radial-gradient(circle at 92% 18%,#ffd46a44,transparent 36%),linear-gradient(145deg,#173d60,#285b69 55%,#55406c)}
.screen:has(#password-page:not(.hidden)){background:radial-gradient(circle at 8% 8%,#61e9ff55,transparent 34%),radial-gradient(circle at 92% 18%,#b28cff44,transparent 36%),linear-gradient(145deg,#153d5b,#176c78 55%,#3b477a)}
.screen:has(#notes-page:not(.hidden)){background:radial-gradient(circle at 8% 8%,#ffe17c55,transparent 34%),radial-gradient(circle at 92% 18%,#ff9e7c44,transparent 36%),linear-gradient(145deg,#51402e,#80583e 55%,#5b4569)}
.screen:has(#shopping-page:not(.hidden)){background:radial-gradient(circle at 8% 5%,#ff6d8c55,transparent 35%),radial-gradient(circle at 92% 18%,#69baff55,transparent 36%),radial-gradient(circle at 50% 100%,#ffe06a33,transparent 40%),linear-gradient(145deg,#271f42,#3e315c 52%,#174e60)}
.shop-hero{padding:13px;border-radius:18px;background:linear-gradient(130deg,#ffffff20,#ffffff08);border:1px solid #ffffff35;box-shadow:0 8px 20px #07172d30}.shop-kicker{font-size:8px;letter-spacing:2px;font-weight:900;color:#ffd88b}.shop-hero h2{font-size:21px;margin:6px 0;color:#fff}.shop-hero p{font-size:10px;margin:0 0 8px}.shop-search-row{display:flex;gap:7px;align-items:center}.shop-search-row .field{margin:0;min-width:0;padding:10px;font-size:12px;flex:1}.shop-cart-button{min-width:58px;padding:11px 8px;border-radius:12px;color:#fff;background:linear-gradient(135deg,#e65b7b,#8c4ac1);border:1px solid #ffffff66}.shop-categories{display:flex;gap:6px;overflow-x:auto;padding:10px 0 5px;scrollbar-width:none}.shop-categories::-webkit-scrollbar{display:none}.shop-category{white-space:nowrap;padding:8px 10px;border-radius:20px;color:#f5f4ff;background:#ffffff16;border:1px solid #ffffff35;font-size:9px}.shop-category.active{background:linear-gradient(110deg,#ff718b,#8c6bff);border-color:#ffd1df;color:#fff}.shop-section-head{display:flex;align-items:center;justify-content:space-between;margin:8px 1px}.shop-section-head h3{font-size:14px;margin:0;color:#fff}.shop-section-head span{font-size:9px;color:#d7d8ef}.shop-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px}.shop-product{min-width:0;padding:8px;border-radius:15px;background:linear-gradient(145deg,#ffffff20,#ffffff0b);border:1px solid #ffffff35;box-shadow:0 6px 14px #07172d30;contain:layout paint}.shop-product-art{height:92px;border-radius:11px;display:flex;align-items:center;justify-content:center;font-size:43px;background:linear-gradient(135deg,#ffbd8a,#e77d9f 48%,#8679d9);margin-bottom:7px}.shop-product:nth-child(4n+2) .shop-product-art{background:linear-gradient(135deg,#77d8d1,#6e9ee7,#aa83dc)}.shop-product:nth-child(4n+3) .shop-product-art{background:linear-gradient(135deg,#ffe18c,#e9a36f,#dc7e9e)}.shop-product:nth-child(4n+4) .shop-product-art{background:linear-gradient(135deg,#8ce6aa,#5ca9a9,#6c82cf)}.shop-product h4{font-size:11px;line-height:1.25;margin:4px 0;color:#fff;min-height:27px}.shop-product .shop-category-name{font-size:8px;color:#d5d9f0}.shop-product .shop-price{font-size:12px;font-weight:900;color:#ffe39a;margin:5px 0}.shop-product .shop-old-price{font-size:8px;color:#d2cde0;text-decoration:line-through;margin-left:4px}.shop-add{width:100%;padding:8px 5px;border-radius:9px;background:linear-gradient(100deg,#64e5c1,#73b9ff);font-size:9px}.shop-cart-panel{margin-top:12px;padding:12px;border-radius:16px;background:linear-gradient(145deg,#172a4b,#4c315c);border:1px solid #ffffff55}.shop-cart-head{display:flex;justify-content:space-between;align-items:center}.shop-cart-head h3{font-size:15px;margin:0 0 8px}.shop-close{background:#ffffff20;color:white;border-radius:8px;padding:6px 9px}.shop-cart-line{display:flex;align-items:center;gap:8px;padding:8px 0;border-bottom:1px solid #ffffff20;font-size:10px}.shop-cart-line span:nth-child(2){flex:1}.shop-cart-line button{padding:4px 7px;border-radius:7px;background:#ffffff20;color:white}.shop-total{display:flex;justify-content:space-between;padding:12px 0;color:#fff;font-size:12px}.shop-total b{color:#ffe39a}.shop-message{font-size:11px;color:#c8ffe9;min-height:15px;margin:7px 0}.shop-shortcut{background:linear-gradient(145deg,#bd4e78,#7044a6)!important;border-color:#ffc0dc!important}
@media(max-width:360px){.shop-product-art{height:78px}.shop-grid{gap:6px}.shop-product{padding:6px}}
/* Pause off-screen orbital motion to reduce background CPU use on phones. */
.screen:has(#solar-page.hidden) .solar-orbit{animation-play-state:paused!important}


/* MOBILE FIT + UPDATED RED / WARM ACCENT PALETTE */
#home-page{width:100%;max-width:100%;overflow:hidden;position:relative;isolation:isolate}
#home-page>.home-pager{width:200%;max-width:none;overflow:visible;flex-wrap:nowrap}
#home-page .home-panel{flex:0 0 50%;width:50%;min-width:50%;max-width:50%}
.screen:has(#home-page:not(.hidden)){
 background:
 radial-gradient(ellipse at 92% 8%,#ff526b55,transparent 34%),
 radial-gradient(ellipse at 8% 78%,#b64b7850,transparent 38%),
 linear-gradient(145deg,#182c48 0%,#382b50 48%,#612f49 100%);
}
body{background:
 radial-gradient(ellipse at 12% 12%,#ff657533,transparent 28%),
 radial-gradient(ellipse at 88% 18%,#b46cff35,transparent 26%),
 linear-gradient(135deg,#171e36,#39283f 55%,#512d3d)!important}
.phone{background:linear-gradient(145deg,#ffe0e5 0%,#d86a7d 24%,#7861a9 58%,#393b67 100%)!important}
.screen{background:
 radial-gradient(ellipse at 12% 8%,#ff75851e,transparent 32%),
 radial-gradient(ellipse at 88% 25%,#a88bff20,transparent 36%),
 linear-gradient(145deg,#172b43,#27334f 48%,#472b46 100%)!important}
.weather-hero{
 background:radial-gradient(circle at 90% 5%,#ff9b6c55,transparent 38%),
 linear-gradient(145deg,#422b50,#71364e 58%,#34456e);
 border-color:#ffb1a9;
 box-shadow:inset 0 2px 0 #ffffff42,0 14px 28px #06172b55
}
.weather-search-btn{background:linear-gradient(110deg,#ff6b70,#ffad70);color:#fff;border:1px solid #ffd0b8}
.weather-stats>div{background:linear-gradient(145deg,#ffffff22,#ffffff0b);border:1px solid #ffffff22}
.weather-stats b{color:#ffe0bd}
.weather-section{padding:12px;border-radius:17px;background:linear-gradient(145deg,#ffffff12,#ffffff06);border:1px solid #ffffff20}
.weather-section-title span{color:#ffc2bd}
.weather-hour{background:linear-gradient(160deg,#ffffff20,#ffffff09);border-color:#ffffff30}
.weather-day{background:linear-gradient(110deg,#ffffff1c,#ffffff08);border-color:#ffffff2b}
.weather-extra-stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:7px;margin-top:9px}
.weather-extra-stats>div{padding:10px 6px;border-radius:13px;text-align:center;background:#ffffff16;border:1px solid #ffffff24}
.weather-extra-stats small{display:block;font-size:8px;color:#f2dce3}
.weather-extra-stats b{display:block;font-size:11px;margin-top:5px;color:#fff0dc}
.weather-kicker{font-size:9px;letter-spacing:1.8px;font-weight:900;color:#ffc1a9;margin:0 0 5px}
.weather-place{font-size:20px}
.weather-status{color:#f4dfe5}
.weather-temp{text-shadow:0 5px 18px #160c2d66}


/* GENTLE MOBILE FIT: slightly roomier controls, only a little page scroll */
@media(max-width:480px){
 body{padding:7px 4px 12px}
 .phone{max-width:440px;min-height:0;padding:8px;border-radius:30px}
 .screen{min-height:0;padding:15px 12px 17px;border-radius:25px}
 .topbar{margin:0 4px 13px}
 #home-page .section{margin:9px 0}
 #home-page .section:first-child p{font-size:10.5px;margin-bottom:3px}
 #home-page .section:first-child h1{font-size:26px;margin:3px 0 4px}
 #home-page .section:first-child p:last-child{font-size:10.5px;margin-bottom:1px}
 #home-page .tile-grid{gap:8px}
 #home-page .tile{min-height:82px;padding:9px 6px;gap:5px;border-radius:15px}
 #home-page .tile .emoji{font-size:24px}
 #home-page .tile span:last-child{font-size:11px}
 #home-page .wide-tile{padding:11px 12px;gap:10px;border-radius:15px}
 #home-page .wide-icon{font-size:28px}
 #home-page .wide-title{font-size:15px}
 #home-page .wide-desc{font-size:10px;line-height:1.3}
 #home-page .home-shortcuts{gap:8px;margin-top:8px}
 #home-page .home-shortcut{min-height:72px;padding:8px 5px;gap:5px;border-radius:14px}
 #home-page .home-shortcut .emoji{font-size:22px}
 #home-page .home-shortcut b{font-size:9px;line-height:1.18}
 #home-page .home-shortcuts-second{gap:8px}
 #home-page .home-shortcuts-second .home-shortcut{min-height:84px}
 #home-page .home-shortcuts-second .home-shortcut .emoji{font-size:24px}
 #home-page .home-shortcuts-second .home-shortcut b{font-size:10px}
 #home-page .home-second-heading{margin:10px 3px 10px;padding:11px;border-radius:15px}
 #home-page .home-second-heading>span{font-size:25px}
 #home-page .home-second-heading b{font-size:14.5px}
 #home-page .home-second-heading small{font-size:9.5px}
 #home-page .home-page-note{font-size:9.5px;margin:9px 0 3px}
 #home-page .logout-row{min-height:42px;margin-top:8px;padding:8px 12px;border-radius:12px}
 #home-page .logout-row .emoji{font-size:17px}
 #home-page .home-pagination{margin:9px 0 0;padding:0 6px}
 #home-page .home-arrow{width:34px;height:31px;font-size:21px}
}


/* Restore the original centered smartphone frame; do not stretch it to the browser. */
html,body{width:100%!important;min-width:0!important;overflow-x:hidden!important}
body{padding:12px 8px 24px!important}
.phone{width:100%!important;max-width:440px!important;min-height:820px!important;height:auto!important;margin:0 auto!important;padding:10px!important;border:0!important;border-radius:38px!important;box-shadow:0 25px 65px #344e7960,inset 0 0 0 2px #ffffffb0!important}
.screen{width:100%!important;max-width:100%!important;min-height:800px!important;height:auto!important;margin:0!important;padding:12px 13px 18px!important;border:1px solid #ffffff55!important;border-radius:30px!important;overflow:hidden!important;box-shadow:none!important}
@media(max-width:480px){body{padding:8px 5px 18px!important}.phone{max-width:440px!important;padding:7px!important;border-radius:30px!important}.screen{padding:10px 11px 16px!important;border-radius:24px!important}}

/* Product detail interaction */
.shop-product{cursor:pointer;transition:transform .16s ease,border-color .16s ease}
.shop-product:active{transform:scale(.975)}
.shop-detail{position:relative;margin:10px 0;padding:14px;border-radius:17px;background:linear-gradient(145deg,#182d50,#57365e);border:1px solid #ffffff55;color:#fff;box-shadow:0 12px 28px #07172d55}
.shop-detail-art{height:130px;display:flex;align-items:center;justify-content:center;font-size:68px;border-radius:13px;background:linear-gradient(135deg,#ffbd8a,#e77d9f 48%,#8679d9);margin:8px 0 12px}
.shop-detail h3{font-size:17px;margin:5px 0}.shop-detail p{font-size:11px;line-height:1.5;color:#e4e5f6}
.shop-detail-actions{display:flex;gap:8px}.shop-detail-actions button{flex:1;padding:10px 6px;border-radius:10px;font-size:10px;font-weight:900}
.shop-detail-add{background:linear-gradient(100deg,#64e5c1,#73b9ff);color:#10263b}.shop-detail-buy{background:linear-gradient(100deg,#ffd477,#ff9d8a);color:#3c2330}.shop-detail-close{position:absolute;right:10px;top:10px;border-radius:8px;padding:5px 9px;background:#ffffff22;color:#fff}


/* HOUSE DESIGNER — isolated responsive floor-plan studio */
#house-page{color:#f4fbff}
.hd-hero{padding:15px;border-radius:19px;background:radial-gradient(circle at 90% 0%,#e7b56b44,transparent 40%),linear-gradient(140deg,#183b4d,#34405d 60%,#68415c);border:1px solid #f0d0a766;box-shadow:0 12px 25px #07172b55}
.hd-kicker{font-size:8px;letter-spacing:2px;color:#ffdc9c;font-weight:900}.hd-hero h2{font-size:22px;margin:7px 0 5px;color:#fff}.hd-hero p{font-size:10px;color:#d9e7ed;line-height:1.5;margin:0}.hd-stats{display:grid;grid-template-columns:repeat(3,1fr);gap:7px;margin-top:13px}.hd-stats div{padding:8px 4px;border-radius:11px;background:#ffffff12;border:1px solid #ffffff20;text-align:center}.hd-stats b{display:block;font-size:18px;color:#ffe1a8}.hd-stats span{font-size:7px;letter-spacing:1px;color:#d5e5ed}
.hd-toolbar{display:grid;grid-template-columns:1fr 1fr;gap:7px;margin:10px 0}.hd-tab{padding:11px 5px;border-radius:11px;background:#ffffff12;border:1px solid #ffffff30;color:#eaf8ff;font-size:9px}.hd-tab.active{background:linear-gradient(110deg,#d8a66b,#f1d6a0);border-color:#ffe6b6;color:#342b2a}.hd-canvas-wrap{position:relative;padding:7px;border-radius:16px;background:linear-gradient(145deg,#101c2c,#25364a);border:1px solid #ffffff35;box-shadow:inset 0 1px #ffffff20,0 12px 25px #06172b55}.hd-canvas-wrap canvas{width:100%;height:auto;display:block;border-radius:10px;background:#e9e2d4;touch-action:none}.hd-canvas-hint{font-size:8px;color:#c5d8e5;text-align:center;padding:7px 2px 1px}.hd-controls{display:grid;gap:9px;margin-top:10px}.hd-panel{padding:11px;border-radius:15px;background:linear-gradient(145deg,#ffffff18,#ffffff09);border:1px solid #ffffff28;box-shadow:inset 0 1px #ffffff20,0 8px 18px #06172b30}.hd-panel-head{display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:9px}.hd-panel-head h3{font-size:13px;margin:0;color:#fff}.hd-panel-head span{font-size:7px;letter-spacing:1px;color:#f3d29d}.hd-choice-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:6px}.hd-choice-grid button{min-width:0;min-height:58px;padding:7px 3px;border-radius:10px;background:linear-gradient(145deg,#29475b,#39435d);border:1px solid #9bb8c355;color:#fff;font-size:19px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px}.hd-choice-grid button b{font-size:8px}.hd-furniture-grid button{background:linear-gradient(145deg,#58465b,#384765);border-color:#d2a7bc55}.hd-help{font-size:8px;color:#c4d8e1;line-height:1.5;margin:8px 1px 0}.hd-empty{font-size:9px;color:#c4d8e1;padding:8px 2px}.hd-label{display:block;font-size:9px;font-weight:800;color:#d9e9ed;margin:6px 0 2px}.hd-panel .field{padding:9px;margin:3px 0 7px;font-size:11px}.hd-two-fields{display:grid;grid-template-columns:1fr 1fr;gap:8px}.hd-color{width:100%;height:36px;border:1px solid #ffffff55;border-radius:9px;background:#ffffff18;padding:3px}.hd-action-row{display:flex;gap:6px;flex-wrap:wrap;margin-top:8px}.hd-action{flex:1;min-width:0;padding:9px 6px;border-radius:9px;background:linear-gradient(110deg,#d5ad7c,#a8c7d8);color:#182d3c;font-size:8px;font-weight:900;border:1px solid #ffffff45}.hd-action.danger{background:linear-gradient(110deg,#ff9a9c,#e66c79);color:#431c2a}.hd-status{font-size:8px;color:#c5e7dc;min-height:14px;margin:8px 2px 0}.hd-project-actions .hd-action{flex:1 1 42%}
@media(max-width:370px){.hd-hero{padding:12px}.hd-choice-grid{gap:4px}.hd-choice-grid button{min-height:53px}.hd-panel{padding:9px}.hd-action{font-size:7px;padding:8px 4px}}


/* MIMESIS — isolated game styling */
#mimesis-page{color:#eef7ff;background:radial-gradient(ellipse at 50% 0%,#26365b 0%,#11172d 48%,#090d19 100%);min-height:780px;padding:12px;border-radius:22px;overflow:hidden;position:relative}
#mimesis-page .page-head{margin-bottom:10px}
#mimesis-page .page-head h2{color:#f2eaff}
.mi-intro{border:1px solid #8b8bdc66;background:linear-gradient(135deg,#28284eaa,#14263dcc);border-radius:18px;padding:14px;margin:8px 0 12px}
.mi-kicker{font-size:9px;letter-spacing:3px;color:#a9baff;font-weight:900}
.mi-intro h2{font-size:25px;margin:6px 0;color:#fff;letter-spacing:1px}
.mi-intro p{font-size:11px;line-height:1.6;color:#c7d5ef;margin:5px 0}
.mi-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin:10px 0}
.mi-stat{background:#ffffff0c;border:1px solid #ffffff20;border-radius:11px;padding:8px 5px;text-align:center}
.mi-stat b{display:block;font-size:16px;color:#b7f4ff}
.mi-stat small{display:block;font-size:8px;color:#aebbd4;letter-spacing:1px;margin-top:3px}
.mi-world{position:relative;border:1px solid #8ca5e866;border-radius:17px;overflow:hidden;background:#080d1b;box-shadow:0 12px 34px #0008}
#mi-canvas{display:block;width:100%;height:auto;aspect-ratio:1.35;touch-action:none;background:#10182a}
.mi-overlay{position:absolute;inset:0;pointer-events:none;display:flex;flex-direction:column;justify-content:space-between;padding:9px}
.mi-topline{display:flex;justify-content:space-between;gap:5px}
.mi-chip{font-size:8px;letter-spacing:1px;padding:6px 8px;border-radius:30px;background:#071020c9;border:1px solid #a9c6ff55;color:#dbe9ff}
.mi-bottomline{display:flex;justify-content:space-between;align-items:end}
.mi-hint{font-size:9px;color:#e5efff;background:#071020c9;border:1px solid #a9c6ff55;padding:7px 9px;border-radius:10px;max-width:78%}
.mi-interact{pointer-events:auto;border:1px solid #b4e5ff88;border-radius:50%;width:43px;height:43px;background:#6d8cffcc;color:white;font-size:20px}
.mi-controls{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;max-width:190px;margin:9px auto}
.mi-controls button,.mi-action{border:1px solid #8ca5e866;border-radius:12px;background:linear-gradient(145deg,#27345d,#19223f);color:#eff6ff;padding:11px 8px;font-weight:800}
.mi-controls button{font-size:17px;min-height:42px}
.mi-controls .empty{visibility:hidden}
.mi-panel{background:#ffffff0b;border:1px solid #ffffff1d;border-radius:15px;padding:12px;margin:9px 0}
.mi-panel h3{font-size:13px;margin:0 0 8px;color:#d8d5ff}
.mi-panel p{font-size:10px;line-height:1.55;color:#c0cbe0}
.mi-progress{height:7px;border-radius:20px;background:#ffffff18;overflow:hidden;margin:7px 0}
.mi-progress span{display:block;height:100%;background:linear-gradient(90deg,#5de3d1,#a88aff);width:0%;transition:width .3s}
.mi-actions{display:grid;grid-template-columns:1fr 1fr;gap:7px}
.mi-action{font-size:10px;min-height:40px}
.mi-action:active,.mi-controls button:active{transform:scale(.97)}
.mi-log{max-height:145px;overflow:auto;font-size:9px;line-height:1.55;color:#c8d6ec}
.mi-log div{padding:5px 0;border-bottom:1px solid #ffffff12}
.mi-modal{position:absolute;inset:0;background:#050914ef;z-index:8;display:none;align-items:center;justify-content:center;padding:16px}
.mi-modal.open{display:flex}
.mi-modal-card{width:100%;max-width:390px;max-height:90%;overflow:auto;background:linear-gradient(145deg,#202b4d,#111a31);border:1px solid #a7baff77;border-radius:18px;padding:16px;box-shadow:0 20px 60px #000b}
.mi-modal-card h3{color:#fff;font-size:18px;margin:0 0 8px}
.mi-modal-card p{font-size:11px;line-height:1.6;color:#c9d5eb}
.mi-choice{display:block;width:100%;text-align:left;padding:11px;margin:7px 0;border:1px solid #9bb3e655;border-radius:11px;background:#ffffff0c;color:#eef4ff;font-size:10px}
.mi-close{width:100%;margin-top:8px;padding:10px;border:0;border-radius:10px;background:#647ce8;color:white;font-weight:900}
.mi-foot{font-size:8px;color:#8f9bb7;text-align:center;margin:12px 0}
@media(max-width:360px){.mi-stats{grid-template-columns:repeat(2,1fr)}.mi-intro h2{font-size:22px}}


/* MOBILE.APP IMMERSIVE MOTION LAYER — continuous, lightweight, page-aware */
.screen{isolation:isolate;transform:translateZ(0)}
.screen:after{
 content:"";position:absolute;inset:-35%;z-index:0;pointer-events:none;opacity:.62;
 background:
  radial-gradient(ellipse at 18% 22%,#70ffe455 0,transparent 24%),
  radial-gradient(ellipse at 78% 28%,#8c80ff55 0,transparent 27%),
  radial-gradient(ellipse at 55% 82%,#ffad7850 0,transparent 25%),
  conic-gradient(from 0deg at 50% 50%,#45d9ce08,#9b78ff16,#ffb46b12,#45d9ce08);
 filter:blur(17px);animation:mobileAmbientDrift 22s ease-in-out infinite alternate;
}
@keyframes mobileAmbientDrift{
 0%{transform:translate3d(-3%,-2%,0) rotate(-7deg) scale(.98);background-position:0 0,100% 0,50% 100%,center}
 50%{transform:translate3d(2%,3%,0) rotate(5deg) scale(1.08);background-position:35% 25%,65% 40%,40% 70%,center}
 100%{transform:translate3d(-1%,1%,0) rotate(11deg) scale(1.02);background-position:70% 40%,20% 80%,85% 15%,center}
}
.screen:has(#login-page:not(.hidden)):after,
.screen:has(#app-login-page:not(.hidden)):after{opacity:.9;animation-duration:15s;filter:blur(12px)}
.screen:has(#flappy-page:not(.hidden)):after{background:radial-gradient(ellipse at 15% 20%,#fff9a866,transparent 22%),radial-gradient(ellipse at 80% 70%,#62f6e766,transparent 28%),linear-gradient(120deg,#2ca9e522,#f7d66a22);animation-duration:18s}
.screen:has(#snake-page:not(.hidden)):after{background:radial-gradient(ellipse at 20% 20%,#91ff8a66,transparent 23%),radial-gradient(ellipse at 80% 75%,#27d69d66,transparent 28%),linear-gradient(130deg,#0b4a3b22,#78ffb422);animation-duration:13s}
.screen:has(#car-page:not(.hidden)):after{background:repeating-linear-gradient(115deg,#ffffff08 0 2px,transparent 2px 48px),radial-gradient(ellipse at 50% 20%,#ffc36b66,transparent 30%),radial-gradient(ellipse at 80% 80%,#ff668866,transparent 25%);animation-duration:10s}
.screen:has(#solar-page:not(.hidden)):after{background:radial-gradient(ellipse at 50% 50%,#ff9a3d38,transparent 20%),radial-gradient(ellipse at 15% 25%,#4caaff55,transparent 28%),radial-gradient(ellipse at 85% 75%,#a66dff44,transparent 30%);animation-duration:30s}
.screen:has(#calculator-page:not(.hidden)):after{background:radial-gradient(ellipse at 15% 20%,#ffd47766,transparent 25%),radial-gradient(ellipse at 85% 80%,#ff8e7966,transparent 28%),linear-gradient(120deg,#a77bff22,#65f5c122)}
.screen:has(#settings-page:not(.hidden)):after{background:radial-gradient(ellipse at 18% 18%,#ff9acb66,transparent 26%),radial-gradient(ellipse at 80% 75%,#8d9cff66,transparent 28%),linear-gradient(120deg,#a77bff22,#65f5c122)}
.card,.tile,.home-shortcut,.wide-tile,.row-tile,.solar-detail,.weather-hero,.nb-panel{
 transform:perspective(900px) translateZ(0);transition:transform .28s ease,box-shadow .28s ease,filter .28s ease;
}
.card:active,.tile:active,.home-shortcut:active,.wide-tile:active,.row-tile:active{transform:perspective(900px) translateY(2px) scale(.985)}
button:not(.home-dot):hover{filter:brightness(1.09) saturate(1.08)}
@media(hover:hover){.card:hover,.tile:hover,.home-shortcut:hover{transform:perspective(900px) translateY(-3px) rotateX(1deg);box-shadow:0 18px 34px #020b1d55,inset 0 2px #ffffff55}}
/* Sun fallback: never depend on a remote texture to render the star. */
.solar-sun{
 background-color:#ff9d25!important;
 background-image:
  radial-gradient(circle at 28% 24%,#fffbd1 0 5%,#fff0a0 8%,transparent 23%),
  repeating-radial-gradient(ellipse at 40% 55%,#fff18b00 0 3px,#ffcf4d88 4px 5px,transparent 7px 10px),
  radial-gradient(circle at 38% 35%,#fff06b 0,#ffbd35 28%,#ff8124 58%,#d94313 82%,#7e210c 100%)!important;
 background-size:cover!important;
 animation:sunSurfaceMotion 8s linear infinite, sunPulse 3.5s ease-in-out infinite alternate;
 box-shadow:0 0 15px 7px #ffe16c,0 0 38px 19px #ff8b2bba,0 0 78px 34px #ff4d1d77,inset -9px -7px 13px #7e210c99!important;
}
.solar-sun:before{content:"";position:absolute;inset:-17%;border-radius:50%;background:conic-gradient(from 0deg,transparent,#ffd36a88,transparent,#ff7a2388,transparent);filter:blur(5px);animation:sunCoronaSpin 14s linear infinite}
.solar-sun:after{content:"";position:absolute;inset:8%;border-radius:50%;background:repeating-linear-gradient(25deg,transparent 0 4px,#fff09a30 5px 6px,transparent 8px 11px);mix-blend-mode:screen;animation:sunSurfaceMotion 5s linear infinite}
@keyframes sunSurfaceMotion{from{background-position:0 0,0 0,0 0}to{background-position:0 0,80px 45px,0 0}}
@keyframes sunPulse{from{filter:brightness(1) saturate(1.08)}to{filter:brightness(1.22) saturate(1.3)}}
@keyframes sunCoronaSpin{to{transform:rotate(360deg)}}
.solar-detail-orb.sun-selected{
 background-color:#ff9d25!important;
 background-image:radial-gradient(circle at 28% 24%,#fffbd1 0 5%,#fff0a0 8%,transparent 23%),repeating-radial-gradient(ellipse at 40% 55%,#fff18b00 0 3px,#ffcf4d88 4px 5px,transparent 7px 10px),radial-gradient(circle at 38% 35%,#fff06b 0,#ffbd35 28%,#ff8124 58%,#d94313 82%,#7e210c 100%)!important;
 animation:sunSurfaceMotion 8s linear infinite,sunPulse 3.5s ease-in-out infinite alternate;
}
.weather-sun-real{position:relative;display:inline-block;width:68px;height:68px;border-radius:50%;background:radial-gradient(circle at 30% 28%,#fffbd0 0 7%,#ffe78a 16%,#ffb52f 48%,#f46a19 78%,#a93410 100%);box-shadow:0 0 18px 7px #ffd15d,0 0 42px 17px #ff8d2b88;animation:sunPulse 3s ease-in-out infinite alternate}
.weather-sun-real:before{content:"";position:absolute;inset:-12px;border:2px solid #ffd36a88;border-radius:50%;animation:sunCoronaSpin 18s linear infinite}
.settings-live-panel{margin-top:16px;padding:13px;border-radius:17px;background:linear-gradient(145deg,#ffffff20,#ffffff09);border:1px solid #ffffff35}
.settings-live-panel h3{font-size:13px;letter-spacing:1px;margin:0 0 10px;color:#fff}
.settings-switch{display:flex!important;align-items:center;justify-content:space-between;gap:10px;padding:11px 2px;border-top:1px solid #ffffff20}
.settings-switch span{display:grid;gap:4px}.settings-switch b{font-size:12px;color:#fff}.settings-switch small{font-size:9px;color:#c5e3e2}
.settings-switch input{width:19px;height:19px;accent-color:#65f5c1;flex:0 0 auto}
.settings-reset{margin-top:10px}
body.mobile-no-glow .card,body.mobile-no-glow .tile,body.mobile-no-glow button{box-shadow:none!important}
body.mobile-no-motion .screen:after,body.mobile-no-motion .solar-sun,body.mobile-no-motion .solar-sun:before,body.mobile-no-motion .solar-sun:after{animation:none!important}
@media(prefers-reduced-motion:reduce){.screen:after,.solar-sun,.solar-sun:before,.solar-sun:after{animation:none!important}}

</style>
</head>

<body>
<div class="phone">
 <main class="screen">

  <div class="dynamic-island" aria-hidden="true"><span></span><i></i></div>
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

  <section id="app-login-page" class="hidden">
   <div class="login-wrap" style="min-height:620px">
    <div class="login-title">Sign in</div>
    <h2 style="color:#f5fffc;margin:5px 0 12px">Welcome to mobile.app</h2>
    <p class="login-sub">Enter your Gmail address and your mobile.app password.</p>
    <div class="card" style="width:100%;max-width:320px;text-align:left">
     <label for="app-login-email">Gmail address</label>
     <input class="field" id="app-login-email" type="email" inputmode="email" autocomplete="username" placeholder="yourname@gmail.com">
     <label for="app-login-password">mobile.app password</label>
     <input class="field" id="app-login-password" type="password" autocomplete="current-password" placeholder="Enter app password">
     <p class="small-note">Use an app-specific password here, not your real Google/Gmail password. This demo checks the format and that a password was entered; it does not authenticate with Google.</p>
     <button class="primary" onclick="submitAppLogin()">CONTINUE</button>
     <p id="app-login-message" class="small-note" role="status" style="margin:10px 0 0"></p>
    </div>
    <button class="secondary" style="max-width:320px;margin-top:10px" onclick="showPage('login-page')">BACK</button>
   </div>
  </section>

  <section id="home-page" class="hidden">
   <div class="home-pager" id="home-pager">
    <div class="home-panel" id="home-panel-0">
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
     </div>
     <button class="logout-row" onclick="logout()"><span class="emoji">🚪</span><b>LOGOUT</b><span class="logout-arrow">›</span></button>
    </div>
    <div class="home-panel" id="home-panel-1">
     <div class="home-second-heading"><span>📱</span><div><b>MORE APPS</b><small>Swipe to explore your mobile space</small></div></div>
     <div class="home-shortcuts home-shortcuts-second">
      <button class="home-shortcut" style="background:linear-gradient(145deg,#152d58,#38265e);border-color:#9bb7ff" onclick="openPage('solar-page');solarSelect('earth')"><span class="emoji">🪐</span><b>SOLAR SYSTEM</b></button>
      <button class="home-shortcut" style="background:linear-gradient(145deg,#176b67,#17436f);border-color:#8dffd1" onclick="openPage('quran-page')"><span class="emoji">📖</span><b>QURAN READER</b></button>
      <button class="home-shortcut shop-shortcut" onclick="openPage('shopping-page');shopRender()"><span class="emoji">🛍️</span><b>SHOPPING STORE</b></button>
      <button class="home-shortcut" style="background:linear-gradient(145deg,#145c69,#303b76);border-color:#8ff5e0" onclick="openPage('house-page')"><span class="emoji">🏠</span><b>HOUSE DESIGNER</b></button>
      <button class="home-shortcut weather-shortcut" onclick="openPage('weather-page');weatherLoad()"><span class="emoji">🌦️</span><b>WEATHER FORECAST</b></button>
       <button class="home-shortcut" style="background:linear-gradient(145deg,#172b50,#49336f);border-color:#c5b4ff;grid-column:1/-1;min-height:74px" onclick="openPage('mimesis-page');miStart()"><span class="emoji">◈</span><b>MIMESIS — THE WORLD THAT STUDIES YOU</b></button>
     </div>
     <div class="home-page-note">Your apps are arranged across two home screens.</div>
     <button class="logout-row" onclick="logout()"><span class="emoji">🚪</span><b>LOGOUT</b><span class="logout-arrow">›</span></button>
    </div>
   </div>
   <div class="home-pagination">
    <button type="button" class="home-arrow" id="home-prev" onclick="homeSwipeTo(0)" aria-label="Previous home screen">‹</button>
    <div class="home-dots"><button id="home-dot-0" class="home-dot active" onclick="homeSwipeTo(0)" aria-label="Home screen one"></button><button id="home-dot-1" class="home-dot" onclick="homeSwipeTo(1)" aria-label="Home screen two"></button></div>
    <button type="button" class="home-arrow" id="home-next" onclick="homeSwipeTo(1)" aria-label="Next home screen">›</button>
   </div>
  </section>

  <section id="weather-page" class="hidden">
   <div class="page-head"><button class="back" onclick="goHome()">‹ Back</button><h2>🌦️ Weather Forecast</h2></div>
   <div class="weather-hero">
    <div class="weather-kicker">LIVE CONDITIONS · 7 DAY OUTLOOK</div>
    <div class="weather-search"><input id="weather-city" class="field" type="search" value="Karachi" placeholder="Search city..." onkeydown="if(event.key==='Enter')weatherLoad()"><button class="weather-search-btn" onclick="weatherLoad()">SEARCH</button></div>
    <div id="weather-status" class="weather-status">Live weather powered by Open-Meteo</div>
    <div class="weather-current"><div><div id="weather-place" class="weather-place">Karachi</div><div id="weather-condition" class="weather-condition">Loading forecast...</div><div id="weather-temp" class="weather-temp">--°</div><div id="weather-range" class="weather-range">H: --°  L: --°</div></div><div id="weather-icon" class="weather-icon">🌤️</div></div>
    <div class="weather-stats"><div><small>FEELS LIKE</small><b id="weather-feels">--°</b></div><div><small>HUMIDITY</small><b id="weather-humidity">--%</b></div><div><small>WIND</small><b id="weather-wind">-- km/h</b></div><div><small>UV INDEX</small><b id="weather-uv">--</b></div></div>
    <div class="weather-extra-stats"><div><small>🌅 SUNRISE</small><b id="weather-sunrise">--:--</b></div><div><small>🌇 SUNSET</small><b id="weather-sunset">--:--</b></div><div><small>🌧️ RAIN CHANCE</small><b id="weather-rain">--%</b></div></div>
   </div>
   <div class="weather-section"><div class="weather-section-title"><h3>Next 12 hours</h3><span>HOURLY</span></div><div id="weather-hourly" class="weather-hourly"><p>Forecast will appear here.</p></div></div>
   <div class="weather-section"><div class="weather-section-title"><h3>7-day forecast</h3><span>DAILY</span></div><div id="weather-daily" class="weather-daily"><p>Forecast will appear here.</p></div></div>
   <p class="small-note">Forecast data is provided by Open-Meteo. Internet connection is required.</p>
  </section>


  <section id="house-page" class="hidden">
   <div class="page-head"><button class="back" onclick="goHome()">‹ Back</button><h2>🏠 House Designer</h2></div>
   <div class="hd-hero"><div class="hd-kicker">MOBILE.APP DESIGN STUDIO</div><h2>Build your dream home</h2><p>Plan rooms, arrange furniture, customize finishes and switch to an isometric 3D-style view.</p><div class="hd-stats"><div><b id="hd-room-count">0</b><span>ROOMS</span></div><div><b id="hd-item-count">0</b><span>OBJECTS</span></div><div><b id="hd-area">0</b><span>m² APPROX.</span></div></div></div>
   <div class="hd-toolbar"><button class="hd-tab active" id="hd-tab-plan" onclick="hdSetView('plan')">▦ 2D FLOOR PLAN</button><button class="hd-tab" id="hd-tab-3d" onclick="hdSetView('3d')">◇ 3D PREVIEW</button></div>
   <div class="hd-canvas-wrap"><canvas id="hd-canvas" width="900" height="620" aria-label="Interactive house plan"></canvas><div class="hd-canvas-hint" id="hd-canvas-hint">Tap an object to select · Drag to move · Pinch/zoom with controls</div></div>
   <div class="hd-controls">
    <div class="hd-panel"><div class="hd-panel-head"><h3>＋ Add rooms</h3><span>ROOM BUILDER</span></div><div class="hd-choice-grid"><button onclick="hdAddRoom('Living Room')">🛋️<b>Living</b></button><button onclick="hdAddRoom('Bedroom')">🛏️<b>Bedroom</b></button><button onclick="hdAddRoom('Kitchen')">🍳<b>Kitchen</b></button><button onclick="hdAddRoom('Bathroom')">🛁<b>Bathroom</b></button><button onclick="hdAddRoom('Dining')">🍽️<b>Dining</b></button><button onclick="hdAddRoom('Study')">📚<b>Study</b></button></div><p class="hd-help">Add a room, then drag it around the floor plan. Select a room to rename, resize or recolour it.</p></div>
    <div class="hd-panel"><div class="hd-panel-head"><h3>＋ Furniture</h3><span>PLACE OBJECTS</span></div><div class="hd-choice-grid hd-furniture-grid"><button onclick="hdAddItem('Sofa')">🛋️<b>Sofa</b></button><button onclick="hdAddItem('Bed')">🛏️<b>Bed</b></button><button onclick="hdAddItem('Table')">🪑<b>Table</b></button><button onclick="hdAddItem('Chair')">💺<b>Chair</b></button><button onclick="hdAddItem('Wardrobe')">🚪<b>Wardrobe</b></button><button onclick="hdAddItem('Plant')">🪴<b>Plant</b></button><button onclick="hdAddItem('Kitchen')">🍽️<b>Counter</b></button><button onclick="hdAddItem('Shower')">🚿<b>Shower</b></button><button onclick="hdAddItem('TV')">📺<b>TV</b></button><button onclick="hdAddItem('Lamp')">💡<b>Lamp</b></button></div></div>
    <div class="hd-panel" id="hd-selection-panel"><div class="hd-panel-head"><h3>Selected element</h3><span id="hd-selection-type">NOTHING SELECTED</span></div><div id="hd-selection-empty" class="hd-empty">Select a room or furniture item on the plan to edit it.</div><div id="hd-selection-edit" class="hidden"><label class="hd-label" for="hd-name">Name</label><input id="hd-name" class="field" maxlength="28" oninput="hdUpdateSelected('name',this.value)"><div class="hd-two-fields"><div><label class="hd-label" for="hd-width">Width (m)</label><input id="hd-width" class="field" type="number" min="0.5" max="20" step="0.5" onchange="hdUpdateSelected('w',this.value)"></div><div><label class="hd-label" for="hd-height">Length (m)</label><input id="hd-height" class="field" type="number" min="0.5" max="20" step="0.5" onchange="hdUpdateSelected('h',this.value)"></div></div><label class="hd-label" for="hd-color">Colour / finish</label><input id="hd-color" class="hd-color" type="color" value="#d8b18a" oninput="hdUpdateSelected('color',this.value)"><div class="hd-action-row"><button class="hd-action" onclick="hdRotateSelected()">↻ Rotate</button><button class="hd-action danger" onclick="hdDeleteSelected()">Delete</button></div></div></div>
    <div class="hd-panel"><div class="hd-panel-head"><h3>Doors & windows</h3><span>DETAILS</span></div><div class="hd-action-row"><button class="hd-action" onclick="hdAddOpening('Door')">🚪 Add door</button><button class="hd-action" onclick="hdAddOpening('Window')">▣ Add window</button></div><p class="hd-help">Doors and windows are visual markers you can move around the plan.</p></div>
    <div class="hd-panel"><div class="hd-panel-head"><h3>Project tools</h3><span>SAVE & EXPORT</span></div><div class="hd-action-row hd-project-actions"><button class="hd-action" onclick="hdSave()">💾 Save design</button><button class="hd-action" onclick="hdLoad()">↩ Load saved</button><button class="hd-action" onclick="hdExport()">⬇ Export image</button><button class="hd-action" onclick="hdNew()">＋ New plan</button></div><div class="hd-action-row"><button class="hd-action" onclick="hdUndo()">↶ Undo</button><button class="hd-action" onclick="hdZoom(-1)">－ Zoom out</button><button class="hd-action" onclick="hdZoom(1)">＋ Zoom in</button></div><p id="hd-status" class="hd-status" role="status">Your design is stored on this device when you save it.</p></div>
   </div>
  </section>

  <section id="shopping-page" class="hidden">
   <div class="page-head"><button class="back" onclick="goHome()">‹ Back</button><h2>🛍️ Shopping Store</h2></div>
   <div class="shop-hero"><div class="shop-kicker">MOBILE.APP MARKETPLACE</div><h2>Find something you love.</h2><p>Explore clothes, gadgets, shoes and everyday essentials.</p>
    <div class="shop-search-row"><input id="shop-search" class="field" type="search" placeholder="Search products..." oninput="shopRender()" aria-label="Search products"><button class="shop-cart-button" onclick="shopToggleCart()">🛒 <span id="shop-cart-count">0</span></button></div>
   </div>
   <div class="shop-categories" id="shop-categories">
    <button class="shop-category active" onclick="shopSetCategory('All',this)">All</button><button class="shop-category" onclick="shopSetCategory('Clothing',this)">Clothing</button><button class="shop-category" onclick="shopSetCategory('Shoes',this)">Shoes</button><button class="shop-category" onclick="shopSetCategory('Electronics',this)">Electronics</button><button class="shop-category" onclick="shopSetCategory('Accessories',this)">Accessories</button><button class="shop-category" onclick="shopSetCategory('Home',this)">Home</button><button class="shop-category" onclick="shopSetCategory('Beauty',this)">Beauty</button>
   </div>
   <div class="shop-section-head"><h3>Popular products</h3><span id="shop-result-count">100 items</span></div><div class="shop-grid" id="shop-products"></div>
   <div id="shop-detail" class="shop-detail hidden" aria-live="polite"></div>
   <div id="shop-cart-panel" class="shop-cart-panel hidden"><div class="shop-cart-head"><h3>Your cart</h3><button class="shop-close" onclick="shopToggleCart()">✕</button></div><div id="shop-cart-items"></div><div class="shop-total"><span>Total</span><b id="shop-total">Rs. 0</b></div><button class="primary" onclick="shopCheckout()">PLACE DEMO ORDER</button><p class="small-note">Demo store only — no real payment or order is processed.</p></div>
   <p id="shop-message" class="shop-message" role="status"></p><p class="small-note">Demo prices are shown in Pakistani rupees. Product availability and checkout are simulated.</p>
  </section>

  <section id="breakout-page" class="hidden">
   <div class="page-head"><button class="back" onclick="breakoutStop();goHome()">‹ Back</button><h2>🟣 Neon Breakout</h2></div>
   <div class="nb-hero"><div class="nb-kicker">ARCADE CHALLENGE / SEASON 01</div><h2 style="font-size:24px;margin:8px 0">BREAK THE GRID.</h2><p>Control the energy paddle, smash neon blocks, collect power-ups and clear 30 handcrafted stages.</p><div class="nb-stats"><div class="nb-stat"><b id="nb-score">0</b><small>SCORE</small></div><div class="nb-stat"><b id="nb-lives">3</b><small>LIVES</small></div><div class="nb-stat"><b id="nb-best">0</b><small>BEST</small></div></div></div>
   <h3>⚡ ARCADE ARENA</h3><div class="nb-panel"><div class="nb-row" style="justify-content:space-between;margin:2px 0 7px"><b id="nb-level-label">LEVEL 01 / 30</b><span id="nb-status" class="nb-status">Tap START to play</span></div><div class="nb-row" style="margin-bottom:7px"><button class="nb-btn" id="nb-start" onclick="breakoutToggle()">START GAME</button><button class="nb-ghost" onclick="breakoutPause()">Ⅱ PAUSE</button><button class="nb-ghost" onclick="breakoutRestart()">↻ RESTART</button></div><canvas id="nb-canvas" width="360" height="520"></canvas><p style="margin-bottom:0">Controls: drag your finger across the arena, or use the buttons below.</p><div class="nb-row" style="justify-content:center;margin-top:8px"><button class="nb-ghost" onpointerdown="breakoutMove(-1)" onpointerup="breakoutMove(0)" onpointerleave="breakoutMove(0)">◀ LEFT</button><button class="nb-ghost" onpointerdown="breakoutMove(1)" onpointerup="breakoutMove(0)" onpointerleave="breakoutMove(0)">RIGHT ▶</button></div></div>
   <h3>🧩 STAGE SELECT</h3><div class="nb-panel"><div id="nb-levels" class="nb-levels"></div><p>Clear a stage to unlock the next one. Your unlocked stages and best score are saved on this device.</p></div>
   <h3>✨ POWER-UP GUIDE</h3><div class="nb-panel"><div class="nb-power">🟢 <b>WIDE PADDLE</b> — temporarily increases paddle width.</div><div class="nb-power">🔵 <b>SLOW BALL</b> — slows the ball for easier control.</div><div class="nb-power">🟣 <b>MULTI-BALL</b> — releases extra balls into the arena.</div><div class="nb-power">🟠 <b>LASER</b> — activates a short burst of paddle lasers.</div><p style="margin-bottom:0">Some blocks need two hits. Explosive blocks clear nearby blocks when broken.</p></div>
   <h3>🏆 PROGRESS</h3><div class="nb-panel"><div class="nb-row" style="justify-content:space-between"><b id="nb-progress-label">0 / 30 stages cleared</b><b id="nb-coins">0 ✦</b></div><div style="height:7px;background:#ffffff18;border-radius:20px;overflow:hidden;margin-top:9px"><div id="nb-progress" style="height:100%;width:0;background:linear-gradient(90deg,#4ce7e9,#b16cff)"></div></div></div>
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
    <button class="tile" style="background:linear-gradient(145deg,#4c368c,#192d59);border-color:#c4a4ff" onclick="openPage('breakout-page');breakoutInit()"><span class="emoji">🟣</span><span>Neon Breakout</span></button>
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
    <button class="primary" onclick="startFlappy()">PLAY / RESTART</button>
    <canvas id="flappy-canvas" class="game-canvas" width="360" height="460"></canvas>
        <p id="flappy-score">Score: 0</p>
   </div>
  </section>

  <section id="snake-page" class="hidden">
   <div class="page-head"><button class="back" onclick="openPage('games-page')">‹ Games</button><h2>Snake</h2></div>
   <div class="card">
    <p>Collect the glowing fruit. Avoid the walls and your tail.</p>
    <button class="primary" onclick="startSnake()">PLAY / RESTART</button>
    <canvas id="snake-canvas" class="game-canvas" width="288" height="288"></canvas>
    <div id="snake-controls">
     <button class="empty-control" aria-hidden="true"> </button>
     <button onclick="snakeDirection(0,-1)">⬆️</button>
     <button class="empty-control" aria-hidden="true"> </button>
     <button onclick="snakeDirection(-1,0)">⬅️</button>
     <button onclick="snakeDirection(0,1)">⬇️</button>
     <button onclick="snakeDirection(1,0)">➡️</button>
    </div>
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
    <button class="primary" style="margin-top:4px" onclick="startCarGame()">PLAY / RESTART</button>
    <canvas id="car-canvas" width="340" height="510"></canvas>
    <div class="car-controls">
     <button onclick="moveCar(-1)">⬅ LEFT</button>
     <button onclick="moveCar(1)">RIGHT ➡</button>
    </div>
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
    <div class="settings-live-panel">
     <h3>✨ EXPERIENCE CONTROLS</h3>
     <label class="settings-switch"><span><b>Moving 3D ambience</b><small>Animated light fields and depth layers</small></span><input id="pref-motion" type="checkbox" checked onchange="mobileSetPreference('motion',this.checked)"><i></i></label>
     <label class="settings-switch"><span><b>Interface sound</b><small>Soft feedback for supported actions</small></span><input id="pref-sound" type="checkbox" checked onchange="mobileSetPreference('sound',this.checked)"><i></i></label>
     <label class="settings-switch"><span><b>Extra visual glow</b><small>Enhanced highlights and ambient lighting</small></span><input id="pref-glow" type="checkbox" checked onchange="mobileSetPreference('glow',this.checked)"><i></i></label>
     <button class="secondary settings-reset" onclick="mobileResetPreferences()">RESET EXPERIENCE</button>
    </div>
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
     <p style="margin-bottom:0"><b>Made by:</b> Mustafa &amp; Kashan</p>
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


  <section id="solar-page" class="hidden">
   <div class="page-head"><button class="back" onclick="solarStop();goHome()">‹ Back</button><h2>🪐 Solar Explorer</h2></div>
   <div class="solar-hero">
    <div class="solar-kicker">SPACE OBSERVATORY · INTERACTIVE PLANET GUIDE</div>
    <h2>Explore our Solar System.</h2>
    <p>Watch the planets orbit the Sun, select a world and discover its atmosphere, moons and remarkable facts.</p>
    <div class="solar-stage" aria-label="Animated solar system model">
     <div class="solar-system">
      <div class="solar-sun" title="Sun"></div>
      <div class="solar-orbit o1"><span class="solar-body"></span></div><div class="solar-orbit o2"><span class="solar-body"></span></div>
      <div class="solar-orbit o3"><span class="solar-body"></span></div><div class="solar-orbit o4"><span class="solar-body"></span></div>
      <div class="solar-orbit o5"><span class="solar-body"></span></div><div class="solar-orbit o6"><span class="solar-body"></span></div>
      <div class="solar-orbit o7"><span class="solar-body"></span></div><div class="solar-orbit o8"><span class="solar-body"></span></div>
     </div>
     <div class="solar-stage-label">SCHEMATIC ORBITS · NOT TO SCALE</div>
    </div>
    <div class="solar-toolbar">
     <button class="solar-tool active" id="solar-motion-btn" onclick="solarToggleMotion()">Ⅱ PAUSE ORBITS</button>
     <button class="solar-tool" onclick="solarSelect('sun')">☀ EXPLORE SUN</button>
     <button class="solar-tool" onclick="solarSelect('pluto')">PLUTO</button>
    </div>
   </div>
   <h3 class="solar-section-title">SELECT A PLANET</h3>
   <div class="solar-planet-list">
    <button class="solar-pick" id="solar-pick-mercury" onclick="solarSelect('mercury')"><span class="dot" style="background:radial-gradient(circle at 30% 25%,#ddd,#777)"></span>Mercury</button>
    <button class="solar-pick" id="solar-pick-venus" onclick="solarSelect('venus')"><span class="dot" style="background:radial-gradient(circle at 30% 25%,#fff0b0,#bd743c)"></span>Venus</button>
    <button class="solar-pick" id="solar-pick-earth" onclick="solarSelect('earth')"><span class="dot" style="background:radial-gradient(circle at 30% 25%,#c4f2ff,#2687c7)"></span>Earth</button>
    <button class="solar-pick" id="solar-pick-mars" onclick="solarSelect('mars')"><span class="dot" style="background:radial-gradient(circle at 30% 25%,#ffd1a1,#b84b2b)"></span>Mars</button>
    <button class="solar-pick" id="solar-pick-jupiter" onclick="solarSelect('jupiter')"><span class="dot" style="background:radial-gradient(circle at 30% 25%,#fff0c6,#d99b5d)"></span>Jupiter</button>
    <button class="solar-pick" id="solar-pick-saturn" onclick="solarSelect('saturn')"><span class="dot" style="background:radial-gradient(circle at 30% 25%,#fff1c8,#c89b62);outline:3px solid #d9c18a88;outline-offset:1px"></span>Saturn</button>
    <button class="solar-pick" id="solar-pick-uranus" onclick="solarSelect('uranus')"><span class="dot" style="background:radial-gradient(circle at 30% 25%,#d7ffff,#77cbd1)"></span>Uranus</button>
    <button class="solar-pick" id="solar-pick-neptune" onclick="solarSelect('neptune')"><span class="dot" style="background:radial-gradient(circle at 30% 25%,#b6d9ff,#3155a2)"></span>Neptune</button>
   </div>
   <div class="solar-detail">
    <div class="solar-detail-top"><div class="solar-detail-orb" id="solar-detail-orb"></div><div><small id="solar-detail-type">PLANET</small><h3 id="solar-detail-name">Earth</h3><small id="solar-detail-distance">1 AU FROM THE SUN</small></div></div>
    <p id="solar-detail-description">Earth is our home world, with liquid-water oceans and a nitrogen- and oxygen-rich atmosphere.</p>
    <div class="solar-facts">
     <div class="solar-fact"><b id="solar-fact-year">365.25 days</b><span>ORBITAL PERIOD</span></div>
     <div class="solar-fact"><b id="solar-fact-day">24 hours</b><span>ROTATION PERIOD</span></div>
     <div class="solar-fact"><b id="solar-fact-size">12,742 km</b><span>MEAN DIAMETER</span></div>
     <div class="solar-fact"><b id="solar-fact-temp">15°C</b><span>AVERAGE TEMPERATURE</span></div>
    </div>
    <h4 class="solar-section-title">NOTABLE MOONS</h4><div class="solar-moon-list" id="solar-moons"><span class="solar-moon-chip">Moon</span></div>
   </div>
   <p class="solar-note">Distances and sizes are approximate reference values. The animated orbital layout is a visual model, not a scale representation of real distances or orbital speeds. Planet surface maps: Solar System Scope (CC BY 4.0).</p>
  </section>

  <section id="quran-page" class="hidden">
   <div class="page-head"><button class="back" onclick="goHome()">‹ Back</button><h2>📖 Quran Reader &amp; Player</h2></div>
   <div class="quran-panel">
    <label for="quran-surah">Surah</label>
    <select class="quran-control" id="quran-surah" onchange="loadQuranSurah()"><option>Loading surah list...</option></select>
    <label for="quran-translation">Translation</label>
    <select class="quran-control" id="quran-translation" onchange="loadQuranSurah()">
     <option value="">None</option>
     <option value="en.sahih" selected>English (Sahih International)</option>
     <option value="ur.jalandhry">Urdu (Jalandhry)</option>
     <option value="ur.maududi">Urdu (Maududi)</option>
     <option value="hi.hindi">Hindi</option>
     <option value="id.indonesian">Indonesian</option>
     <option value="tr.diyanet">Turkish</option>
    </select>
    <label for="quran-reciter">Reciter</label>
    <select class="quran-control" id="quran-reciter" onchange="updateQuranFullAudio()">
     <option value="https://server8.mp3quran.net/afs/{n}.mp3">Mishary Alafasy</option>
     <option value="https://server7.mp3quran.net/basit/{n}.mp3">Abdul Basit (Murattal)</option>
     <option value="https://server11.mp3quran.net/sds/{n}.mp3">Abdurrahman As-Sudais</option>
     <option value="https://server7.mp3quran.net/shur/{n}.mp3">Saud Ash-Shuraim</option>
     <option value="https://server12.mp3quran.net/maher/{n}.mp3">Maher Al-Muaiqly</option>
    </select>
    <label for="quran-font-size">Arabic font size: <span id="quran-font-label">2.0</span> rem</label>
    <input class="quran-range" id="quran-font-size" type="range" min="1.2" max="3.5" step="0.1" value="2" oninput="changeQuranFont(this.value)">
    <label style="display:flex;align-items:center;gap:8px"><input id="quran-ayah-audio" type="checkbox" onchange="toggleQuranAyahAudio()"> Show audio player for each ayah</label>
   </div>
   <div class="quran-panel">
    <h3 id="quran-surah-heading">Choose a Surah</h3>
    <p id="quran-surah-meta" class="quran-meta"></p>
    <h3 style="margin-top:12px">🎧 Listen to the full surah</h3>
    <audio id="quran-full-audio" controls preload="none" style="width:100%"></audio>
    <p id="quran-status" class="quran-status" role="status">Loading Quran data...</p>
   </div>
   <h3>📜 Read</h3>
   <div id="quran-content" class="quran-panel"><p>Surah text will appear here.</p></div>
   <p class="small-note">Text and translations: api.alquran.cloud · Audio: mp3quran.net / islamic.network</p>
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

 
  <section id="mimesis-page" class="hidden">
   <div class="page-head"><button class="back" onclick="goHome()">‹ Home</button><h2>◈ MIMESIS</h2></div>
   <div class="mi-intro">
    <div class="mi-kicker">AN ADAPTIVE WORLD · OFFLINE EXPERIENCE</div>
    <h2>THE WORLD THAT STUDIES YOU</h2>
    <p>It watches how you explore. It remembers what you avoid, what you repeat, and what you choose. The world will not stay the same.</p>
    <div class="mi-stats">
     <div class="mi-stat"><b id="mi-level">01</b><small>DEPTH</small></div><div class="mi-stat"><b id="mi-memories">0</b><small>MEMORIES</small></div>
     <div class="mi-stat"><b id="mi-fragments">0</b><small>FRAGMENTS</small></div><div class="mi-stat"><b id="mi-instinct">0%</b><small>WORLD READ</small></div>
    </div>
   </div>
   <div class="mi-world">
    <canvas id="mi-canvas" width="900" height="660" aria-label="Mimesis exploration world"></canvas>
    <div class="mi-overlay"><div class="mi-topline"><span class="mi-chip" id="mi-biome">THE QUIET REACH</span><span class="mi-chip" id="mi-world-state">OBSERVING</span></div>
     <div class="mi-bottomline"><span class="mi-hint" id="mi-hint">Move around. The world is paying attention.</span><button class="mi-interact" onclick="miInteract()" aria-label="Interact">✦</button></div>
    </div>
    <div class="mi-modal" id="mi-modal"><div class="mi-modal-card" id="mi-modal-content"></div></div>
   </div>
   <div class="mi-controls" aria-label="Movement controls"><span class="empty"></span><button onclick="miMove(0,-1)">▲</button><span class="empty"></span>
    <button onclick="miMove(-1,0)">◀</button><button onclick="miInteract()">✦</button><button onclick="miMove(1,0)">▶</button>
    <span class="empty"></span><button onclick="miMove(0,1)">▼</button><span class="empty"></span></div>
   <div class="mi-panel"><h3>WORLD RESPONSE</h3><p id="mi-response">A distant shape turns when you move. It may be coincidence. It may not.</p>
    <div class="mi-progress"><span id="mi-adapt-bar"></span></div>
    <div class="mi-actions"><button class="mi-action" onclick="miScan()">⌕ SCAN AREA</button><button class="mi-action" onclick="miRest()">◌ LISTEN</button>
     <button class="mi-action" onclick="miJournal()">▤ MEMORY LOG</button><button class="mi-action" onclick="miSave()">⬡ SAVE WORLD</button></div></div>
   <div class="mi-panel"><h3>RECENT MEMORIES</h3><div class="mi-log" id="mi-log"><div>Your first steps have not yet been recorded.</div></div></div>
   <div class="mi-foot">MIMESIS · Your choices shape the simulation · Progress saves on this device</div>
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
  "login-page","app-login-page","home-page","calculator-page","password-page",
  "notes-page","games-page","guess-page","typing-page",
  "flappy-page","snake-page","car-page","settings-page",
  "about-page","school-page","school-history-page","school-mission-page","breakout-page","mimesis-page","solar-page","quran-page","shopping-page","house-page","weather-page","pin-page"
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

  if (id === "home-page") homeSwipeTo(0);
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
  if (id === "quran-page") initQuranReader();
  if (id === "house-page") hdInit();
}

function goHome() {
  if (appPin && !isGuest) {
    showPage("pin-page");
    return;
  }
  showPage("home-page");
}


// HOME SCREEN SWIPE CONTROLS
let homeScreenIndex = 0;
function homeSwipeTo(index) {
  homeScreenIndex = Math.max(0, Math.min(1, Number(index) || 0));
  const pager = $("home-pager");
  if (pager) pager.style.transform = `translateX(-${homeScreenIndex * 50}%)`;
  [0,1].forEach(i => {
    const dot = $("home-dot-" + i);
    if (dot) dot.classList.toggle("active", i === homeScreenIndex);
  });
  const prev = $("home-prev"), next = $("home-next");
  if (prev) prev.style.opacity = homeScreenIndex === 0 ? ".45" : "1";
  if (next) next.style.opacity = homeScreenIndex === 1 ? ".45" : "1";
}
(function initHomeSwipe(){
  const pager = $("home-pager");
  if (!pager) return;
  let startX = 0, startY = 0, tracking = false;
  pager.addEventListener("touchstart", e => {
    if (!e.touches || e.touches.length !== 1) return;
    startX = e.touches[0].clientX; startY = e.touches[0].clientY; tracking = true;
  }, {passive:true});
  pager.addEventListener("touchend", e => {
    if (!tracking || !e.changedTouches || !e.changedTouches.length) return;
    const dx = e.changedTouches[0].clientX - startX;
    const dy = e.changedTouches[0].clientY - startY;
    if (Math.abs(dx) > 45 && Math.abs(dx) > Math.abs(dy) * 1.25) homeSwipeTo(dx < 0 ? 1 : 0);
    tracking = false;
  }, {passive:true});
  let pointerX = 0, pointerY = 0, pointerDown = false;
  pager.addEventListener("pointerdown", e => {
    if (e.pointerType === "mouse" && e.button === 0) { pointerX=e.clientX; pointerY=e.clientY; pointerDown=true; }
  });
  pager.addEventListener("pointerup", e => {
    if (!pointerDown) return;
    const dx=e.clientX-pointerX, dy=e.clientY-pointerY;
    if (Math.abs(dx)>55 && Math.abs(dx)>Math.abs(dy)*1.25) homeSwipeTo(dx<0?1:0);
    pointerDown=false;
  });
  pager.addEventListener("pointercancel",()=>{pointerDown=false;});
  document.addEventListener("keydown", e => {
    if (!$("home-page") || $("home-page").classList.contains("hidden")) return;
    if (e.key === "ArrowRight") homeSwipeTo(1);
    if (e.key === "ArrowLeft") homeSwipeTo(0);
  });
  homeSwipeTo(0);
})();

// LIVE WEATHER FORECAST — Open-Meteo (no API key required)
const weatherCodeInfo = code => {
  if (code === 0) return ["Clear sky","☀️"];
  if ([1,2].includes(code)) return ["Mainly clear","🌤️"];
  if (code === 3) return ["Overcast","☁️"];
  if ([45,48].includes(code)) return ["Foggy","🌫️"];
  if ([51,53,55,56,57].includes(code)) return ["Drizzle","🌦️"];
  if ([61,63,65,66,67,80,81,82].includes(code)) return ["Rain showers","🌧️"];
  if ([71,73,75,77,85,86].includes(code)) return ["Snow","❄️"];
  if ([95,96,99].includes(code)) return ["Thunderstorm","⛈️"];
  return ["Variable conditions","🌥️"];
};
function weatherSetText(id, value) { const el=$(id); if(el) el.textContent=value; }
async function weatherLoad(){
  const input=$("weather-city"), status=$("weather-status");
  const city=(input?.value||"Karachi").trim();
  if(!city){if(status)status.textContent="Enter a city name first.";return;}
  if(status)status.textContent="Searching location and loading live forecast…";
  const hourly=$("weather-hourly"), daily=$("weather-daily");
  try{
    const geoUrl="https://geocoding-api.open-meteo.com/v1/search?name="+encodeURIComponent(city)+"&count=1&language=en&format=json";
    const geoResponse=await fetch(geoUrl);
    if(!geoResponse.ok)throw new Error("Could not search for this city.");
    const geo=await geoResponse.json();
    if(!geo.results?.length)throw new Error("City not found. Check the spelling and try again.");
    const place=geo.results[0];
    const params=new URLSearchParams({latitude:place.latitude,longitude:place.longitude,current:"temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,weather_code,wind_speed_10m",hourly:"temperature_2m,precipitation_probability,weather_code",daily:"weather_code,temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max",timezone:"auto",forecast_days:"7"});
    const response=await fetch("https://api.open-meteo.com/v1/forecast?"+params.toString());
    if(!response.ok)throw new Error("Weather service is temporarily unavailable.");
    const data=await response.json(), current=data.current, d=data.daily;
    const [condition,icon]=weatherCodeInfo(current.weather_code);
    weatherSetText("weather-place",[place.name,place.admin1,place.country].filter(Boolean).join(", "));
    weatherSetText("weather-condition",condition);
    weatherSetText("weather-temp",Math.round(current.temperature_2m)+"°");
    weatherSetText("weather-range","H: "+Math.round(d.temperature_2m_max[0])+"°  L: "+Math.round(d.temperature_2m_min[0])+"°");
    weatherSetText("weather-feels",Math.round(current.apparent_temperature)+"°");
    weatherSetText("weather-humidity",current.relative_humidity_2m+"%");
    weatherSetText("weather-wind",Math.round(current.wind_speed_10m)+" km/h");
    weatherSetText("weather-uv",d.uv_index_max?.[0] ?? "--");
    weatherSetText("weather-sunrise",d.sunrise?.[0] ? new Date(d.sunrise[0]).toLocaleTimeString([], {hour:"2-digit",minute:"2-digit"}) : "--:--");
    weatherSetText("weather-sunset",d.sunset?.[0] ? new Date(d.sunset[0]).toLocaleTimeString([], {hour:"2-digit",minute:"2-digit"}) : "--:--");
    const nextRain=(data.hourly.precipitation_probability||[]).find((value,i)=>new Date(data.hourly.time[i]).getTime()>=new Date(current.time).getTime());
    weatherSetText("weather-rain",nextRain==null ? "--%" : nextRain+"%");
    weatherSetText("weather-icon",icon);
    if(status)status.textContent="Updated just now · Local time: "+new Date(current.time).toLocaleTimeString([], {hour:"2-digit",minute:"2-digit"});
    if(hourly){
      const now=new Date(current.time).getTime();
      let indexes=data.hourly.time.map((t,i)=>({t,i})).filter(x=>new Date(x.t).getTime()>=now).slice(0,12);
      hourly.innerHTML=indexes.map(({t,i})=>{const [label,ico]=weatherCodeInfo(data.hourly.weather_code[i]);return `<div class="weather-hour"><small>${new Date(t).toLocaleTimeString([], {hour:"numeric"})}</small><span title="${label}">${ico}</span><b>${Math.round(data.hourly.temperature_2m[i])}°</b><small>💧 ${data.hourly.precipitation_probability?.[i]??0}%</small></div>`;}).join("")||"<p>No hourly forecast available.</p>";
    }
    if(daily){
      daily.innerHTML=d.time.map((day,i)=>{const [label,ico]=weatherCodeInfo(d.weather_code[i]);const date=new Date(day+"T12:00:00");const dayName=i===0?"Today":date.toLocaleDateString([], {weekday:"short"});return `<div class="weather-day"><b>${dayName}</b><span title="${label}">${ico}</span><small>${Math.round(d.temperature_2m_min[i])}°</small><strong>${Math.round(d.temperature_2m_max[i])}°</strong></div>`;}).join("");
    }
  }catch(error){
    if(status)status.textContent="Weather could not be loaded.";
    if(hourly)hourly.innerHTML='<div class="weather-error">'+String(error.message||error).replace(/[<>]/g,"")+"</div>";
    if(daily)daily.innerHTML="";
  }
}

// LOGIN / LOGOUT

function login() {
  isGuest = false;
  $("app-login-email").value = "";
  $("app-login-password").value = "";
  $("app-login-message").textContent = "";
  showPage("app-login-page");
}

function submitAppLogin() {
  const email = $("app-login-email").value.trim();
  const password = $("app-login-password").value;
  const emailPattern = /^[A-Z0-9._%+-]+@gmail\.com$/i;
  const message = $("app-login-message");

  if (!emailPattern.test(email)) {
    message.textContent = "Please enter a valid address ending in @gmail.com.";
    return;
  }
  if (!password.trim()) {
    message.textContent = "Please enter your mobile.app password.";
    return;
  }

  // This is a local demo sign-in only. Never save or transmit the password.
  userName = email.split("@")[0];
  isGuest = false;
  $("app-login-password").value = "";
  message.textContent = "";

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
        mobileSfx("point");
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
function nbApplyDrop(d){mobileSfx('coin');if(d.type==='wide'){nbEffects.wide=600;nbPaddle.w=92;}if(d.type==='slow')nbEffects.slow=600;if(d.type==='laser')nbEffects.laser=600;if(d.type==='multi'){const b=nbBalls[0];if(b)for(let i=0;i<2;i++)nbBalls.push({x:b.x,y:b.y,vx:i? -b.vx:b.vx,vy:b.vy,r:6,stuck:false});}nbMessage=({wide:'WIDE PADDLE!',slow:'SLOW BALL!',laser:'LASER READY!',multi:'MULTI-BALL!'}[d.type]);}
function nbHitBrick(index){const b=nbBricks[index];if(!b)return;b.hp--;if(b.hp<=0){nbScore+=b.type==='explosive'?35:10;nbCoins+=1;nbSave.coins+=1;nbDrop(b.x+b.w/2,b.y+b.h/2);nbBricks.splice(index,1);if(b.type==='explosive'){for(let i=nbBricks.length-1;i>=0;i--){const q=nbBricks[i];if(Math.hypot(q.x-b.x,q.y-b.y)<72){nbScore+=8;nbBricks.splice(i,1);}}}}else nbScore+=3;}
function breakoutLoop(t){if(!nbRunning)return;const dt=Math.min(2,(t-(nbLast||t))/16.67||1);nbLast=t;const speed=4.1*(nbEffects.slow>0?.65:1);if(nbMove)nbPaddle.x+=nbMove*5.5*dt;nbPaddle.x=Math.max(0,Math.min(NB_W-nbPaddle.w,nbPaddle.x));if(nbEffects.wide>0)nbEffects.wide-=dt;else nbPaddle.w=60;if(nbEffects.slow>0)nbEffects.slow-=dt;if(nbEffects.laser>0)nbEffects.laser-=dt;
 for(const b of nbBalls){if(b.stuck){b.x=nbPaddle.x+nbPaddle.w/2;b.y=NB_H-65;continue;}b.x+=b.vx*dt*speed/4.1;b.y+=b.vy*dt*speed/4.1;if(b.x<b.r||b.x>NB_W-b.r)b.vx*=-1;if(b.y<b.r+25)b.vy=Math.abs(b.vy);if(b.y>NB_H-58&&b.y<NB_H-43&&b.x>nbPaddle.x&&b.x<nbPaddle.x+nbPaddle.w&&b.vy>0){b.vy=-Math.abs(b.vy);b.vx=((b.x-(nbPaddle.x+nbPaddle.w/2))/(nbPaddle.w/2))*3.8;}
  for(let i=nbBricks.length-1;i>=0;i--){const q=nbBricks[i];if(b.x+b.r>q.x&&b.x-b.r<q.x+q.w&&b.y+b.r>q.y&&b.y-b.r<q.y+q.h){b.vy*=-1;nbHitBrick(i);break;}}}
 nbBalls=nbBalls.filter(b=>b.y<NB_H+15);if(!nbBalls.length){nbLives--;if(nbLives<=0){mobileSfx('gameover');nbRunning=false;nbMessage='GAME OVER · Restart to try again';nbSave.best=Math.max(nbSave.best,nbScore);nbPersist();}else{nbBalls=[{x:nbPaddle.x+nbPaddle.w/2,y:NB_H-65,vx:2.2,vy:-3.4,r:6,stuck:true}];nbMessage='Life lost · Tap to launch';}}
 for(const d of nbDrops){d.y+=d.vy*dt;if(d.y>NB_H-65&&d.y<NB_H-45&&d.x>nbPaddle.x&&d.x<nbPaddle.x+nbPaddle.w)nbApplyDrop(d);}nbDrops=nbDrops.filter(d=>d.y<NB_H+10);
 if(nbEffects.laser>0&&Math.floor(t/160)%4===0){nbLasers.push({x:nbPaddle.x+nbPaddle.w*.25,y:NB_H-70},{x:nbPaddle.x+nbPaddle.w*.75,y:NB_H-70});}for(const l of nbLasers)l.y-=8*dt;nbLasers=nbLasers.filter(l=>l.y>35);for(let i=nbLasers.length-1;i>=0;i--){const l=nbLasers[i],j=nbBricks.findIndex(b=>l.x>=b.x&&l.x<=b.x+b.w&&l.y>=b.y&&l.y<=b.y+b.h);if(j>=0){nbHitBrick(j);nbLasers.splice(i,1);}}
 if(!nbBricks.length&&!nbLevelWon){mobileSfx('success');nbLevelWon=true;nbRunning=false;nbSave.cleared=Array.from(new Set([...nbSave.cleared,nbLevel]));nbSave.unlocked=Math.max(nbSave.unlocked,Math.min(30,nbLevel+1));nbSave.best=Math.max(nbSave.best,nbScore);nbSave.coins=nbCoins;nbPersist();nbMessage=nbLevel===30?'ALL 30 LEVELS CLEARED!':'STAGE CLEAR · NEXT LEVEL UNLOCKED';}
 nbDraw();nbUpdateHud();if(nbRunning)nbFrame=requestAnimationFrame(breakoutLoop);}
function breakoutNext(){if(nbLevel<30){nbLevel++;breakoutRestart();breakoutToggle();}}
function nbDraw(){if(!nbCtx)return;const c=nbCtx;const g=c.createLinearGradient(0,0,0,NB_H);g.addColorStop(0,'#0b1730');g.addColorStop(1,'#070914');c.fillStyle=g;c.fillRect(0,0,NB_W,NB_H);for(let i=0;i<55;i++){c.fillStyle='rgba(180,225,255,'+(0.12+(i%4)*.05)+')';c.fillRect((i*67)%NB_W,(i*97)%NB_H,1.4,1.4);}c.fillStyle='#8ceeff';c.font='bold 10px Arial';c.fillText('NEON SECTOR  '+String(nbLevel).padStart(2,'0'),12,18);for(const b of nbBricks){c.shadowBlur=12;c.shadowColor=b.color;c.fillStyle=b.color;c.beginPath();c.roundRect(b.x,b.y,b.w,b.h,5);c.fill();c.shadowBlur=0;c.fillStyle='#07111f';c.font='bold 9px Arial';c.textAlign='center';c.fillText(b.hp>1?'Ⅱ':b.type==='explosive'?'✹':'',b.x+b.w/2,b.y+12);}c.textAlign='left';for(const d of nbDrops){c.fillStyle=({wide:'#72f28d',slow:'#59caff',multi:'#c28aff',laser:'#ffb45d'}[d.type]);c.shadowBlur=10;c.shadowColor=c.fillStyle;c.beginPath();c.arc(d.x,d.y,7,0,Math.PI*2);c.fill();c.shadowBlur=0;}for(const l of nbLasers){c.fillStyle='#ffad55';c.fillRect(l.x-2,l.y,4,12);}c.shadowBlur=16;c.shadowColor='#62f5ff';c.fillStyle='#69efff';c.beginPath();c.roundRect(nbPaddle.x,NB_H-48,nbPaddle.w,10,5);c.fill();c.shadowBlur=0;for(const b of nbBalls){c.shadowBlur=14;c.shadowColor='#fff';c.fillStyle='#fff';c.beginPath();c.arc(b.x,b.y,b.r,0,Math.PI*2);c.fill();c.shadowBlur=0;}if(!nbRunning){c.fillStyle='rgba(3,8,20,.52)';c.fillRect(0,NB_H/2-26,NB_W,52);c.fillStyle='#eafcff';c.font='bold 14px Arial';c.textAlign='center';c.fillText(nbMessage,NB_W/2,NB_H/2+5);c.textAlign='left';}}
if(nbCanvas){nbCanvas.addEventListener('pointerdown',e=>{nbPointer=e.clientX;const b=nbBalls.find(x=>x.stuck);if(b){b.stuck=false;nbMessage='Good luck!';}if(!nbRunning&&!nbLevelWon&&nbLives>0&&nbPaused===false){/* start remains explicit */}});nbCanvas.addEventListener('pointermove',e=>{if(nbPointer===null&&e.buttons===0)return;const r=nbCanvas.getBoundingClientRect();const x=(e.clientX-r.left)*NB_W/r.width;nbPaddle.x=Math.max(0,Math.min(NB_W-nbPaddle.w,x-nbPaddle.w/2));if(nbBalls[0]?.stuck)nbBalls[0].x=nbPaddle.x+nbPaddle.w/2;});nbCanvas.addEventListener('pointerup',()=>nbPointer=null);nbCanvas.addEventListener('pointercancel',()=>nbPointer=null);}
// Replace start button behavior after stage clear with next stage.
const nbStartButton=document.getElementById('nb-start');if(nbStartButton)nbStartButton.addEventListener('click',()=>{if(nbLevelWon)breakoutNext();else if(nbBalls[0]?.stuck)nbBalls[0].stuck=false;});
nbRenderMeta();nbResetStage();nbUpdateHud();nbDraw();
// ================= END NEON BREAKOUT =================




// Music feature removed as requested.


// ================= SHOPPING STORE (LOCAL DEMO) =================
const shopProductSeeds=[
["Clothing","Classic Hoodie","🧥"],["Clothing","Everyday T-Shirt","👕"],["Clothing","Denim Jacket","🧥"],["Clothing","Cotton Kurta","🥻"],["Clothing","Casual Jeans","👖"],["Clothing","Summer Dress","👗"],["Clothing","Sports Shorts","🩳"],["Clothing","Warm Sweater","🧶"],["Clothing","Formal Shirt","👔"],["Clothing","Rain Jacket","🌧️"],
["Shoes","Street Sneakers","👟"],["Shoes","Running Shoes","🥾"],["Shoes","Canvas Shoes","👟"],["Shoes","Leather Loafers","👞"],["Shoes","Sandals","🩴"],["Shoes","Hiking Boots","🥾"],["Shoes","School Shoes","👞"],["Shoes","Slip-on Shoes","👟"],["Shoes","Sports Trainers","👟"],["Shoes","House Slippers","🥿"],
["Electronics","Wireless Headphones","🎧"],["Electronics","Smart Watch","⌚"],["Electronics","Bluetooth Speaker","🔊"],["Electronics","Portable Charger","🔋"],["Electronics","Gaming Mouse","🖱️"],["Electronics","Mechanical Keyboard","⌨️"],["Electronics","Tablet Stand","📱"],["Electronics","USB Desk Fan","🌀"],["Electronics","LED Monitor Light","💡"],["Electronics","Mini Projector","📽️"],
["Accessories","Travel Backpack","🎒"],["Accessories","Classic Wrist Watch","⌚"],["Accessories","Sunglasses","🕶️"],["Accessories","Leather Wallet","👛"],["Accessories","Sports Cap","🧢"],["Accessories","Steel Water Bottle","🍼"],["Accessories","Travel Pouch","🧳"],["Accessories","Card Holder","💳"],["Accessories","Keychain Set","🔑"],["Accessories","Crossbody Bag","👜"],
["Home","Desk Lamp","💡"],["Home","Cozy Cushion","🛋️"],["Home","Wall Clock","🕰️"],["Home","Storage Basket","🧺"],["Home","Coffee Mug","☕"],["Home","Bedsheet Set","🛏️"],["Home","Table Organizer","🗂️"],["Home","Mini Plant Pot","🪴"],["Home","Laundry Hamper","🧺"],["Home","Decorative Mirror","🪞"],
["Beauty","Care Gift Set","🧴"],["Beauty","Face Wash","🫧"],["Beauty","Hand Cream","🧴"],["Beauty","Hair Brush","🪮"],["Beauty","Body Lotion","🧴"],["Beauty","Scented Soap","🧼"],["Beauty","Nail Care Kit","💅"],["Beauty","Shampoo Bottle","🧴"],["Beauty","Lip Balm","💄"],["Beauty","Skin Care Pouch","🧖"],
["Electronics","Wireless Earbuds","🎶"],["Electronics","Phone Tripod","📷"],["Electronics","Power Bank 20000mAh","🔋"],["Electronics","USB-C Hub","🔌"],["Electronics","Smart LED Bulb","💡"],["Electronics","Webcam","📹"],["Electronics","Portable SSD Case","💾"],["Electronics","Bluetooth Keyboard","⌨️"],["Electronics","Gaming Controller","🎮"],["Electronics","Laptop Cooling Pad","💻"],
["Clothing","Graphic Sweatshirt","👚"],["Clothing","Polo T-Shirt","👕"],["Clothing","Track Pants","👖"],["Clothing","Flannel Shirt","👔"],["Clothing","Winter Gloves","🧤"],["Clothing","Baseball Jersey","🥇"],["Clothing","Zip-up Hoodie","🧥"],["Clothing","Cotton Socks Pack","🧦"],["Clothing","Lightweight Scarf","🧣"],["Clothing","Casual Waistcoat","🦺"],
["Home","Non-stick Pan","🍳"],["Home","Glass Water Set","🥛"],["Home","Kitchen Storage Jars","🫙"],["Home","LED String Lights","✨"],["Home","Foldable Stool","🪑"],["Home","Door Mat","🟫"],["Home","Food Container Set","🥡"],["Home","Wall Art Frame","🖼️"],["Home","Desk Calendar","🗓️"],["Home","Reusable Shopping Bags","🛍️"],
["Accessories","Travel Neck Pillow","🛌"],["Accessories","Minimal Bracelet","📿"],["Accessories","Sports Backpack","🎒"],["Accessories","Laptop Sleeve","💼"],["Accessories","Foldable Umbrella","☂️"],["Accessories","Digital Alarm Clock","⏰"],["Accessories","Reusable Lunch Box","🍱"],["Accessories","Gym Duffel Bag","👜"],["Accessories","Insulated Flask","🧋"],["Accessories","Compact Card Case","💳"]
];
const shopPriceSeed=()=>{let x=Date.now()>>>0;return()=>{x=(x*1664525+1013904223)>>>0;return x/4294967296;};};
const shopRandom=shopPriceSeed();
const shopProducts=shopProductSeeds.map((item,index)=>{const base=650+Math.floor(shopRandom()*11400);return{id:index+1,category:item[0],name:item[1],emoji:item[2],price:Math.round(base/10)*10,old:Math.round(base*(1.12+shopRandom()*.28)/10)*10,stock:4+Math.floor(shopRandom()*47),description:`${item[1]} is a handy ${item[0].toLowerCase()} item selected for the Mobile.app demo marketplace. Check the details, add it to your cart, or try the demo buy option.`,rating:(3.7+shopRandom()*1.3).toFixed(1)};});
let shopCategory="All",shopCart={};
const shopMoney=value=>"Rs. "+Number(value).toLocaleString("en-PK");
function shopSetCategory(category,button){shopCategory=category;document.querySelectorAll(".shop-category").forEach(el=>el.classList.remove("active"));if(button)button.classList.add("active");shopRender();}
function shopRender(){const host=$("shop-products");if(!host)return;const query=($("shop-search")?.value||"").trim().toLowerCase();const visible=shopProducts.filter(p=>(shopCategory==="All"||p.category===shopCategory)&&(p.name.toLowerCase().includes(query)||p.category.toLowerCase().includes(query)));$("shop-result-count").textContent=visible.length+" of 100 items";host.innerHTML=visible.map(p=>`<article class="shop-product" role="button" tabindex="0" aria-label="View ${p.name}" onclick="shopShowDetails(${p.id})" onkeydown="if(event.key==='Enter'||event.key===' '){event.preventDefault();shopShowDetails(${p.id})}"><div class="shop-product-art" aria-hidden="true">${p.emoji}</div><div class="shop-category-name">${p.category.toUpperCase()}</div><h4>${p.name}</h4><div class="shop-price">${shopMoney(p.price)}<span class="shop-old-price">${shopMoney(p.old)}</span></div><button class="shop-add" onclick="event.stopPropagation();shopAdd(${p.id})">＋ ADD TO CART</button></article>`).join("")||'<p class="small-note">No products found. Try another search.</p>';shopUpdateCart();}
function shopShowDetails(id){const p=shopProducts.find(x=>x.id===Number(id));const panel=$("shop-detail");if(!p||!panel)return;panel.innerHTML=`<button class="shop-detail-close" onclick="shopCloseDetails()" aria-label="Close details">✕</button><div class="shop-detail-art">${p.emoji}</div><div class="shop-category-name">${p.category.toUpperCase()} · PRODUCT #${p.id}</div><h3>${p.name}</h3><div class="shop-price">${shopMoney(p.price)} <span class="shop-old-price">${shopMoney(p.old)}</span></div><p>${p.description}</p><p>⭐ ${p.rating}/5 · Demo stock: ${p.stock} available</p><div class="shop-detail-actions"><button class="shop-detail-add" onclick="shopAdd(${p.id});shopCloseDetails()">ADD TO CART</button><button class="shop-detail-buy" onclick="shopBuyNow(${p.id})">BUY NOW</button></div>`;panel.classList.remove("hidden");panel.scrollIntoView({behavior:"smooth",block:"nearest"});}
function shopCloseDetails(){const panel=$("shop-detail");if(panel)panel.classList.add("hidden");}
function shopBuyNow(id){shopAdd(id);shopToggleCart();shopCloseDetails();const msg=$("shop-message");if(msg)msg.textContent="Added to cart. Review your demo order below; no payment is processed.";}

function shopAdd(id){shopCart[id]=(shopCart[id]||0)+1;$("shop-message").textContent="Added to your cart.";shopUpdateCart();}
function shopUpdateCart(){const count=Object.values(shopCart).reduce((a,b)=>a+b,0);const countEl=$("shop-cart-count");if(countEl)countEl.textContent=count;const rows=Object.entries(shopCart).filter(([,qty])=>qty>0);const list=$("shop-cart-items");if(list)list.innerHTML=rows.length?rows.map(([id,qty])=>{const p=shopProducts.find(x=>x.id===Number(id));return `<div class="shop-cart-line"><span>${p.emoji}</span><span>${p.name}<br>${shopMoney(p.price)} × ${qty}</span><b>${shopMoney(p.price*qty)}</b><button onclick="shopRemove(${id})" aria-label="Remove one">−</button></div>`;}).join(""):'<p class="small-note">Your cart is empty.</p>';const total=rows.reduce((sum,[id,qty])=>sum+shopProducts.find(p=>p.id===Number(id)).price*qty,0);const totalEl=$("shop-total");if(totalEl)totalEl.textContent=shopMoney(total);}
function shopRemove(id){if(!shopCart[id])return;shopCart[id]--;if(shopCart[id]<=0)delete shopCart[id];shopUpdateCart();}
function shopToggleCart(){const panel=$("shop-cart-panel");if(panel)panel.classList.toggle("hidden");shopUpdateCart();}
function shopCheckout(){const count=Object.values(shopCart).reduce((a,b)=>a+b,0);if(!count){$("shop-message").textContent="Add a product to your cart first.";return;}$("shop-message").textContent="Demo order complete! No payment was taken.";shopCart={};shopUpdateCart();$("shop-cart-panel").classList.add("hidden");}
// ================= END SHOPPING STORE =================




// ================= HOUSE DESIGNER =================
const HD_W=900,HD_H=620,HD_SCALE=1;
let hdRooms=[],hdItems=[],hdOpenings=[],hdSelected=null,hdView='plan',hdZoomLevel=1,hdDrag=null,hdUndoStack=[];
const hdRoomStyles={'Living Room':'#d8c5a8','Bedroom':'#c7d8e7','Kitchen':'#d8d2ad','Bathroom':'#b9d9d8','Dining':'#dec7b1','Study':'#c9c2df'};
const hdFurniture={'Sofa':['🛋️',105,48,'#9b7890'],'Bed':['🛏️',112,76,'#d2b9a2'],'Table':['▱',72,52,'#b78a5c'],'Chair':['◉',34,34,'#8a9b9f'],'Wardrobe':['▤',75,35,'#9b806a'],'Plant':['🪴',35,35,'#75a67a'],'Kitchen':['▰',110,38,'#a5a6a0'],'Shower':['🚿',48,48,'#8bbdc5'],'TV':['▰',70,18,'#333b48'],'Lamp':['💡',28,28,'#e9c96f'],'Door':['🚪',54,12,'#a87951'],'Window':['▥',58,12,'#77b9d0']};
function hdCanvas(){return $('hd-canvas')}
function hdStatus(t){const e=$('hd-status');if(e)e.textContent=t;}
function hdSnapshot(){hdUndoStack.push(JSON.stringify({rooms:hdRooms,items:hdItems,openings:hdOpenings}));if(hdUndoStack.length>25)hdUndoStack.shift();}
function hdInit(){if(!hdCanvas()||hdCanvas().__hdReady)return;hdCanvas().__hdReady=true;hdCanvas().addEventListener('pointerdown',hdPointerDown);hdCanvas().addEventListener('pointermove',hdPointerMove);window.addEventListener('pointerup',hdPointerUp);hdRender();}
function hdAddRoom(name){hdSnapshot();const n=hdRooms.length;const room={id:'r'+Date.now()+Math.random(),name,x:70+(n%3)*245,y:75+Math.floor(n/3)*205,w:210,h:155,color:hdRoomStyles[name]||'#d8c5a8',rotation:0};hdRooms.push(room);hdSelected={type:'room',id:room.id};hdRender();hdSyncSelection();hdStatus(name+' added. Drag it to position.');}
function hdAddItem(name){hdSnapshot();const f=hdFurniture[name]||['•',50,40,'#aaa'];const item={id:'i'+Date.now()+Math.random(),name,x:120+Math.random()*500,y:130+Math.random()*300,w:f[1],h:f[2],color:f[3],rotation:0,emoji:f[0]};hdItems.push(item);hdSelected={type:'item',id:item.id};hdRender();hdSyncSelection();hdStatus(name+' added to your plan.');}
function hdAddOpening(name){hdSnapshot();const f=hdFurniture[name];const item={id:'o'+Date.now()+Math.random(),name,x:260+Math.random()*300,y:300,w:f[1],h:f[2],color:f[3],rotation:0,emoji:f[0]};hdOpenings.push(item);hdSelected={type:'opening',id:item.id};hdRender();hdSyncSelection();hdStatus(name+' marker added.');}
function hdFind(){if(!hdSelected)return null;const list=hdSelected.type==='room'?hdRooms:hdSelected.type==='opening'?hdOpenings:hdItems;return list.find(x=>x.id===hdSelected.id)||null;}
function hdUpdateSelected(key,value){const o=hdFind();if(!o)return;if(key==='w'||key==='h'){const v=Number(value);if(!Number.isFinite(v)||v<0.5)return;o[key]=Math.max(22,Math.min(700,v*44));}else o[key]=value;hdRender();}
function hdSyncSelection(){const o=hdFind(),empty=$('hd-selection-empty'),edit=$('hd-selection-edit');if(!o){empty?.classList.remove('hidden');edit?.classList.add('hidden');$('hd-selection-type').textContent='NOTHING SELECTED';return;}empty?.classList.add('hidden');edit?.classList.remove('hidden');$('hd-selection-type').textContent=hdSelected.type.toUpperCase();$('hd-name').value=o.name;$('hd-width').value=(o.w/44).toFixed(1);$('hd-height').value=(o.h/44).toFixed(1);$('hd-color').value=o.color||'#d8b18a';}
function hdDeleteSelected(){if(!hdSelected)return;hdSnapshot();const list=hdSelected.type==='room'?hdRooms:hdSelected.type==='opening'?hdOpenings:hdItems;const i=list.findIndex(x=>x.id===hdSelected.id);if(i>=0)list.splice(i,1);hdSelected=null;hdRender();hdSyncSelection();hdStatus('Selected element deleted.');}
function hdRotateSelected(){const o=hdFind();if(!o)return;hdSnapshot();o.rotation=((o.rotation||0)+90)%360;hdRender();}
function hdHit(x,y){for(const [type,list] of [['opening',hdOpenings],['item',hdItems],['room',hdRooms]])for(let i=list.length-1;i>=0;i--){const o=list[i];if(x>=o.x&&x<=o.x+o.w&&y>=o.y&&y<=o.y+o.h)return{type,id:o.id};}return null;}
function hdPoint(e){const r=hdCanvas().getBoundingClientRect();const sx=(e.clientX-r.left)/r.width*HD_W,sy=(e.clientY-r.top)/r.height*HD_H;return{x:(sx-HD_W/2)/hdZoomLevel+HD_W/2,y:(sy-HD_H/2)/hdZoomLevel+HD_H/2};}
function hdPointerDown(e){if(hdView!=='plan')return;const p=hdPoint(e),hit=hdHit(p.x,p.y);hdSelected=hit;if(hit){hdSnapshot();hdDrag={x:p.x,y:p.y,obj:hdFind(),ox:hdFind().x,oy:hdFind().y};hdCanvas().setPointerCapture(e.pointerId);}hdRender();hdSyncSelection();}
function hdPointerMove(e){if(!hdDrag)return;const p=hdPoint(e);hdDrag.obj.x=Math.max(8,Math.min(HD_W-hdDrag.obj.w-8,hdDrag.ox+p.x-hdDrag.x));hdDrag.obj.y=Math.max(8,Math.min(HD_H-hdDrag.obj.h-8,hdDrag.oy+p.y-hdDrag.y));hdRender();}
function hdPointerUp(){hdDrag=null;}
function hdDrawGrid(ctx){ctx.fillStyle='#eee8dc';ctx.fillRect(0,0,HD_W,HD_H);ctx.strokeStyle='#d8d0c2';ctx.lineWidth=1;for(let x=0;x<=HD_W;x+=22){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,HD_H);ctx.stroke();}for(let y=0;y<=HD_H;y+=22){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(HD_W,y);ctx.stroke();}}
function hdDrawRoom(ctx,r){ctx.save();ctx.translate(r.x+r.w/2,r.y+r.h/2);ctx.rotate((r.rotation||0)*Math.PI/180);ctx.fillStyle=r.color;ctx.globalAlpha=.76;ctx.fillRect(-r.w/2,-r.h/2,r.w,r.h);ctx.globalAlpha=1;ctx.strokeStyle='#55483d';ctx.lineWidth=7;ctx.strokeRect(-r.w/2,-r.h/2,r.w,r.h);ctx.fillStyle='#51463d';ctx.font='bold 17px Arial';ctx.textAlign='center';ctx.fillText(r.name,0,0);ctx.font='11px Arial';ctx.fillStyle='#77695d';ctx.fillText((r.w/44).toFixed(1)+'m × '+(r.h/44).toFixed(1)+'m',0,18);ctx.restore();if(hdSelected?.id===r.id){ctx.strokeStyle='#2479c8';ctx.lineWidth=4;ctx.setLineDash([8,5]);ctx.strokeRect(r.x-4,r.y-4,r.w+8,r.h+8);ctx.setLineDash([]);}}
function hdDrawItem(ctx,o,type){ctx.save();ctx.translate(o.x+o.w/2,o.y+o.h/2);ctx.rotate((o.rotation||0)*Math.PI/180);ctx.fillStyle=o.color||'#aaa';ctx.strokeStyle='#51483f';ctx.lineWidth=2;ctx.fillRect(-o.w/2,-o.h/2,o.w,o.h);ctx.strokeRect(-o.w/2,-o.h/2,o.w,o.h);ctx.fillStyle=type==='opening'?'#273c4d':'#27323a';ctx.font='bold 13px Arial';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(o.emoji||'•',0,-2);ctx.font='10px Arial';ctx.fillText(o.name,0,o.h/2+12);ctx.restore();if(hdSelected?.id===o.id){ctx.strokeStyle='#1679d0';ctx.lineWidth=3;ctx.setLineDash([5,4]);ctx.strokeRect(o.x-4,o.y-4,o.w+8,o.h+8);ctx.setLineDash([]);}}
function hdRenderPlan(ctx){hdDrawGrid(ctx);ctx.fillStyle='#9d8e7a';ctx.font='bold 15px Arial';ctx.fillText('FLOOR PLAN · 1 GRID = 0.5 m',20,27);hdRooms.forEach(r=>hdDrawRoom(ctx,r));hdItems.forEach(o=>hdDrawItem(ctx,o,'item'));hdOpenings.forEach(o=>hdDrawItem(ctx,o,'opening'));if(!hdRooms.length){ctx.fillStyle='#887e72';ctx.textAlign='center';ctx.font='bold 22px Arial';ctx.fillText('Your home starts here',HD_W/2,HD_H/2-8);ctx.font='14px Arial';ctx.fillText('Add rooms below to create your floor plan',HD_W/2,HD_H/2+20);ctx.textAlign='left';}}
function hdIso(ctx,x,y,z){return{x:(x-y)*.72+450,y:(x+y)*.38-z+110};}
function hdPoly(ctx,pts,fill,stroke='#5c5148'){ctx.beginPath();pts.forEach((p,i)=>i?ctx.lineTo(p.x,p.y):ctx.moveTo(p.x,p.y));ctx.closePath();ctx.fillStyle=fill;ctx.fill();ctx.strokeStyle=stroke;ctx.lineWidth=2;ctx.stroke();}
function hdRender3D(ctx){ctx.fillStyle='#dce8ed';ctx.fillRect(0,0,HD_W,HD_H);const rooms=hdRooms.length?hdRooms:[{x:170,y:160,w:480,h:300,name:'Your Home',color:'#d8c5a8'}];rooms.forEach(r=>{const x=r.x/1.5,y=r.y/1.5,w=r.w/1.5,h=r.h/1.5,z=75;const a=hdIso(ctx,x,y,0),b=hdIso(ctx,x+w,y,0),c=hdIso(ctx,x+w,y+h,0),d=hdIso(ctx,x,y+h,0),a2=hdIso(ctx,x,y,z),b2=hdIso(ctx,x+w,y,z),d2=hdIso(ctx,x,y+h,z);hdPoly(ctx,[a,b,c,d],'#b69a79');hdPoly(ctx,[a,b,b2,a2],'#e5d8c5');hdPoly(ctx,[a,d,d2,a2],'#cbb99f');hdPoly(ctx,[a2,b2,hdIso(ctx,x+w,y+h,z),d2],r.color||'#d8c5a8','#77685a');ctx.fillStyle='#403a35';ctx.font='bold 14px Arial';ctx.textAlign='center';const label=hdIso(ctx,x+w/2,y+h/2,z+2);ctx.fillText(r.name,label.x,label.y);});hdItems.forEach(o=>{const q=hdIso(ctx,o.x/1.5+o.w/3,o.y/1.5+o.h/3,18);ctx.fillStyle=o.color||'#999';ctx.fillRect(q.x-14,q.y-10,28,20);ctx.strokeStyle='#554';ctx.strokeRect(q.x-14,q.y-10,28,20);ctx.fillStyle='#28343c';ctx.font='12px Arial';ctx.textAlign='center';ctx.fillText(o.emoji||'•',q.x,q.y+4);});ctx.fillStyle='#42596a';ctx.font='bold 15px Arial';ctx.textAlign='left';ctx.fillText('ISOMETRIC 3D-STYLE PREVIEW',20,28);ctx.font='11px Arial';ctx.fillText('Concept view · room layout and furniture arrangement',20,48);}
function hdRender(){const c=hdCanvas();if(!c)return;const ctx=c.getContext('2d');ctx.save();ctx.clearRect(0,0,HD_W,HD_H);ctx.translate(HD_W/2,HD_H/2);ctx.scale(hdZoomLevel,hdZoomLevel);ctx.translate(-HD_W/2,-HD_H/2);if(hdView==='3d')hdRender3D(ctx);else hdRenderPlan(ctx);ctx.restore();$('hd-tab-plan')?.classList.toggle('active',hdView==='plan');$('hd-tab-3d')?.classList.toggle('active',hdView==='3d');$('hd-canvas-hint').textContent=hdView==='plan'?'Tap an object to select · Drag to move · Use controls to edit':'Isometric preview of your current rooms and furniture';$('hd-room-count').textContent=hdRooms.length;$('hd-item-count').textContent=hdItems.length+hdOpenings.length;$('hd-area').textContent=Math.round(hdRooms.reduce((a,r)=>a+(r.w/44)*(r.h/44),0));}
function hdSetView(v){hdView=v;hdRender();}
function hdZoom(d){hdZoomLevel=Math.max(.65,Math.min(1.35,hdZoomLevel+d*.1));hdRender();}
function hdSave(){try{localStorage.setItem('mobile_app_house_design',JSON.stringify({rooms:hdRooms,items:hdItems,openings:hdOpenings}));hdStatus('Design saved on this device.');}catch(e){hdStatus('Could not save. Device storage may be unavailable.');}}
function hdLoad(){try{const raw=localStorage.getItem('mobile_app_house_design');if(!raw){hdStatus('No saved design found on this device.');return;}const d=JSON.parse(raw);hdRooms=Array.isArray(d.rooms)?d.rooms:[];hdItems=Array.isArray(d.items)?d.items:[];hdOpenings=Array.isArray(d.openings)?d.openings:[];hdSelected=null;hdRender();hdSyncSelection();hdStatus('Saved design loaded.');}catch(e){hdStatus('Saved design could not be read.');}}
function hdUndo(){const raw=hdUndoStack.pop();if(!raw){hdStatus('Nothing to undo yet.');return;}const d=JSON.parse(raw);hdRooms=d.rooms;hdItems=d.items;hdOpenings=d.openings;hdSelected=null;hdRender();hdSyncSelection();hdStatus('Last change undone.');}
function hdNew(){if(!confirm('Start a new house plan? Unsaved changes will be cleared.'))return;hdSnapshot();hdRooms=[];hdItems=[];hdOpenings=[];hdSelected=null;hdRender();hdSyncSelection();hdStatus('New empty plan created.');}
function hdExport(){const c=hdCanvas();if(!c)return;const a=document.createElement('a');a.download='mobile-app-house-design.png';a.href=c.toDataURL('image/png');a.click();hdStatus('Plan image exported.');}
// ================= END HOUSE DESIGNER =================

// INITIAL SETUP

resetGuess();
shopRender();
resetSnake();
drawFlappy();
drawCar();
renderNotes();
showPage("login-page");


// ================= QURAN READER =================
const QURAN_API = "https://api.alquran.cloud/v1";
const QURAN_RECITERS = {
  "Mishary Alafasy": "https://server8.mp3quran.net/afs/{n}.mp3",
  "Abdul Basit (Murattal)": "https://server7.mp3quran.net/basit/{n}.mp3",
  "Abdurrahman As-Sudais": "https://server11.mp3quran.net/sds/{n}.mp3",
  "Saud Ash-Shuraim": "https://server7.mp3quran.net/shur/{n}.mp3",
  "Maher Al-Muaiqly": "https://server12.mp3quran.net/maher/{n}.mp3"
};
let quranSurahList = [];
let quranLoadedSurah = 0;
let quranRequestToken = 0;
let quranAyahAudioData = null;

function quranEscape(value) {
  return String(value ?? "").replace(/[&<>"']/g, ch => ({
    "&":"&amp;", "<":"&lt;", ">":"&gt;", '"':"&quot;", "'":"&#39;"
  })[ch]);
}

async function initQuranReader() {
  const status = $("quran-status");
  if (quranSurahList.length) {
    if (!quranLoadedSurah) loadQuranSurah();
    return;
  }
  status.textContent = "Loading surah list...";
  try {
    const response = await fetch(QURAN_API + "/surah");
    if (!response.ok) throw new Error("HTTP " + response.status);
    const result = await response.json();
    quranSurahList = result.data || [];
    const select = $("quran-surah");
    select.innerHTML = quranSurahList.map(s =>
      `<option value="${s.number}">${s.number}. ${quranEscape(s.englishName)} (${quranEscape(s.name)})</option>`
    ).join("");
    status.textContent = "Surah list loaded.";
    loadQuranSurah();
  } catch (error) {
    status.textContent = "Could not load surah list. Check your internet connection. " + error.message;
  }
}

function updateQuranFullAudio() {
  if (!quranLoadedSurah) return;
  const template = $("quran-reciter").value;
  const source = template.replace("{n}", String(quranLoadedSurah).padStart(3, "0"));
  const player = $("quran-full-audio");
  if (player.src !== source) {
    player.src = source;
    player.load();
  }
}

function changeQuranFont(value) {
  $("quran-font-label").textContent = Number(value).toFixed(1);
  document.querySelectorAll("#quran-content .quran-arabic").forEach(el => {
    el.style.fontSize = value + "rem";
    el.style.lineHeight = (Number(value) * 1.6) + "rem";
  });
}

function toggleQuranAyahAudio() {
  if (quranLoadedSurah) renderQuranAyahAudio();
}

function renderQuranAyahAudio() {
  const enabled = $("quran-ayah-audio").checked;
  document.querySelectorAll("#quran-content .quran-ayah-audio-slot").forEach((slot, index) => {
    if (!enabled || !quranAyahAudioData || !quranAyahAudioData[index]) {
      slot.innerHTML = "";
      return;
    }
    const audioUrl = quranAyahAudioData[index].audio;
    slot.innerHTML = audioUrl ? `<audio controls preload="none" src="${quranEscape(audioUrl)}"></audio>` : "";
  });
}

async function loadQuranSurah() {
  if (!quranSurahList.length) return;
  const number = Number($("quran-surah").value || 1);
  const translation = $("quran-translation").value;
  const token = ++quranRequestToken;
  const status = $("quran-status");
  const content = $("quran-content");
  status.textContent = "Loading surah...";
  content.innerHTML = "";
  quranLoadedSurah = number;
  updateQuranFullAudio();

  const editions = "quran-uthmani,ar.alafasy" + (translation ? "," + translation : "");
  try {
    const response = await fetch(`${QURAN_API}/surah/${number}/editions/${editions}`);
    if (!response.ok) throw new Error("HTTP " + response.status);
    const result = await response.json();
    if (token !== quranRequestToken) return;
    const data = result.data || [];
    const arabic = data.find(d => d.edition.identifier === "quran-uthmani");
    const audio = data.find(d => d.edition.identifier === "ar.alafasy");
    const trans = data.find(d => d.edition.type === "translation") || null;
    if (!arabic || !audio) throw new Error("Required Quran editions were not returned.");

    const meta = quranSurahList[number - 1];
    $("quran-surah-heading").textContent = meta.englishName + " — " + meta.name;
    $("quran-surah-meta").textContent = `${meta.englishNameTranslation} • ${meta.numberOfAyahs} ayahs • ${meta.revelationType}`;
    quranAyahAudioData = audio.ayahs || [];

    let html = "";
    if (number !== 1 && number !== 9) {
      html += '<div class="quran-bismillah">بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ</div>';
    }
    arabic.ayahs.forEach((ayah, index) => {
      let text = ayah.text;
      if (number !== 1 && index === 0) {
        const bism = "بِسْمِ ٱللَّهِ ٱلرَّحْمَـٰنِ ٱلرَّحِيمِ";
        if (text.startsWith(bism)) text = text.slice(bism.length).trim();
      }
      const ayahNumber = ayah.numberInSurah;
      const translationText = trans && trans.ayahs[index] ? trans.ayahs[index].text : "";
      html += `<div class="quran-ayah"><div class="quran-arabic" style="font-size:${$("quran-font-size").value}rem;line-height:${Number($("quran-font-size").value)*1.6}rem">${quranEscape(text)} ﴿${ayahNumber}﴾</div>`;
      if (translationText) html += `<div class="quran-translation">${quranEscape(translationText)}</div>`;
      html += `<div class="quran-ayah-audio-slot"></div></div>`;
    });
    content.innerHTML = html;
    renderQuranAyahAudio();
    status.textContent = "Surah loaded successfully.";
  } catch (error) {
    if (token !== quranRequestToken) return;
    status.textContent = "Could not load surah text. " + error.message;
  }
}
// ================= END QURAN READER =================

// ================= SOLAR SYSTEM EXPLORER =================
const solarData = {
 mercury:{texture:"https://www.solarsystemscope.com/textures/download/2k_mercury.jpg",name:"Mercury",type:"TERRESTRIAL PLANET",distance:"0.39 AU FROM THE SUN",year:"88 Earth days",day:"58.6 Earth days",size:"4,879 km",temp:"167°C",color:"radial-gradient(circle at 30% 25%,#e4e0d8,#77736e 65%,#292a31)",description:"Mercury is the smallest planet and the closest to the Sun. Its ancient, heavily cratered surface records billions of years of impacts. It has almost no atmosphere to retain heat, so temperatures vary dramatically between day and night.",moons:["No natural moons"]},
 venus:{texture:"https://www.solarsystemscope.com/textures/download/2k_venus_surface.jpg",name:"Venus",type:"TERRESTRIAL PLANET",distance:"0.72 AU FROM THE SUN",year:"225 Earth days",day:"243 Earth days",size:"12,104 km",temp:"464°C",color:"radial-gradient(circle at 30% 25%,#fff0bd,#d18a45 55%,#74401e)",description:"Venus is wrapped in thick clouds of sulfuric acid droplets. Its atmosphere is mostly carbon dioxide, creating an intense greenhouse effect that makes its surface hotter than Mercury's. It rotates slowly in the opposite direction to most planets.",moons:["No natural moons"]},
 earth:{texture:"https://www.solarsystemscope.com/textures/download/2k_earth_daymap.jpg",name:"Earth",type:"TERRESTRIAL PLANET",distance:"1 AU FROM THE SUN",year:"365.25 days",day:"23 h 56 min",size:"12,742 km",temp:"15°C",color:"radial-gradient(circle at 30% 25%,#d5f8ff 0 8%,#46b7e7 25%,#1765a5 58%,#082b59 82%)",description:"Earth is the only world currently known to support life. Its surface has vast oceans of liquid water, active geology and a protective magnetic field. Nitrogen and oxygen dominate its atmosphere, while clouds and weather continually reshape the view from space.",moons:["The Moon"]},
 mars:{texture:"https://www.solarsystemscope.com/textures/download/2k_mars.jpg",name:"Mars",type:"TERRESTRIAL PLANET",distance:"1.52 AU FROM THE SUN",year:"687 Earth days",day:"24 h 37 min",size:"6,779 km",temp:"−65°C",color:"radial-gradient(circle at 30% 25%,#ffd1a1,#bd5832 58%,#55251d)",description:"Mars is a cold desert world with a thin carbon-dioxide atmosphere. Its surface contains enormous volcanoes, deep canyons, ancient river channels and polar ice caps. Robotic explorers study whether liquid water once persisted there for long periods.",moons:["Phobos","Deimos"]},
 jupiter:{texture:"https://www.solarsystemscope.com/textures/download/2k_jupiter.jpg",name:"Jupiter",type:"GAS GIANT",distance:"5.20 AU FROM THE SUN",year:"11.86 Earth years",day:"9 h 56 min",size:"139,820 km",temp:"−110°C",color:"repeating-linear-gradient(8deg,#d9b18b 0 7%,#9b684b 8% 13%,#f0d4ac 14% 20%,#a96f4f 21% 27%)",description:"Jupiter is the largest planet, a giant world made mostly of hydrogen and helium. Its colorful cloud bands are shaped by powerful winds, and the Great Red Spot is a giant storm that has persisted for centuries. Jupiter has a large family of moons.",moons:["Io","Europa","Ganymede","Callisto"]},
 saturn:{texture:"https://www.solarsystemscope.com/textures/download/2k_saturn.jpg",name:"Saturn",type:"GAS GIANT",distance:"9.58 AU FROM THE SUN",year:"29.4 Earth years",day:"10 h 33 min",size:"116,460 km",temp:"−140°C",color:"radial-gradient(circle at 30% 25%,#fff1c8,#c89b62 62%,#725034)",description:"Saturn is a gas giant famous for its spectacular rings, made mostly of countless pieces of water ice with some rocky material. The planet is less dense than water on average. Its moon Titan has lakes and seas of liquid hydrocarbons.",moons:["Titan","Enceladus","Rhea","Dione","Iapetus"]},
 uranus:{texture:"https://www.solarsystemscope.com/textures/download/2k_uranus.jpg",name:"Uranus",type:"ICE GIANT",distance:"19.2 AU FROM THE SUN",year:"84 Earth years",day:"17 h 14 min",size:"50,724 km",temp:"−195°C",color:"radial-gradient(circle at 30% 25%,#e0ffff,#8ad5dc 58%,#397f99)",description:"Uranus is an ice giant with a blue-green appearance caused by methane in its atmosphere. Its rotation axis is tilted by about 98 degrees, so it effectively rolls around the Sun. It has faint rings and a cold, dynamic atmosphere.",moons:["Miranda","Ariel","Umbriel","Titania","Oberon"]},
 neptune:{texture:"https://www.solarsystemscope.com/textures/download/2k_neptune.jpg",name:"Neptune",type:"ICE GIANT",distance:"30.1 AU FROM THE SUN",year:"164.8 Earth years",day:"16 h 6 min",size:"49,244 km",temp:"−200°C",color:"radial-gradient(circle at 30% 25%,#b8dcff,#386fce 58%,#122b78)",description:"Neptune is a distant ice giant with a deep-blue atmosphere and some of the fastest winds measured on any planet. It receives very little sunlight, yet its atmosphere remains active with storms and changing cloud patterns.",moons:["Triton","Proteus","Nereid"]},
 pluto:{name:"Pluto",type:"DWARF PLANET",distance:"39.5 AU FROM THE SUN (AVERAGE)",year:"248 Earth years",day:"6.4 Earth days",size:"2,377 km",temp:"−225°C",color:"radial-gradient(circle at 30% 25%,#f4dfc8,#a78a78 65%,#554a48)",description:"Pluto is a dwarf planet in the Kuiper Belt beyond Neptune. It has mountains of water ice, broad plains of frozen nitrogen and a thin atmosphere that changes as it travels along its elongated orbit. NASA's New Horizons spacecraft flew past it in 2015.",moons:["Charon","Styx","Nix","Kerberos","Hydra"]},
 sun:{texture:"https://www.solarsystemscope.com/textures/download/2k_sun.jpg",name:"The Sun",type:"STAR · THE CENTRE OF OUR SOLAR SYSTEM",distance:"0 AU · CENTRAL STAR",year:"About 225 million years per galactic orbit",day:"About 25–35 days (varies by latitude)",size:"1.39 million km",temp:"5,500°C at surface",color:"radial-gradient(circle at 32% 25%,#fffbd0 0 5%,#ffe18a 18%,#ff9a32 52%,#b72d12 100%)",description:"The Sun is a G-type main-sequence star containing about 99.86% of the Solar System's mass. Its energy is produced by nuclear fusion in the core. Sunlight and the solar wind influence every planet and many smaller bodies.",moons:["No moons — planets orbit the Sun"]}
};
let solarMotion=true;
function solarSelect(key){
 const d=solarData[key];if(!d)return;
 const put=(id,value)=>{const el=$(id);if(el)el.textContent=value;};
 put("solar-detail-type",d.type);put("solar-detail-name",d.name);put("solar-detail-distance",d.distance);
 put("solar-detail-description",d.description);put("solar-fact-year",d.year);put("solar-fact-day",d.day);
 put("solar-fact-size",d.size);put("solar-fact-temp",d.temp);
 const orb=$("solar-detail-orb");if(orb){orb.style.backgroundImage=d.texture?`radial-gradient(circle at 30% 25%,#ffffff22 0%,transparent 42%,#0008 100%),url("${d.texture}"),${d.color}`:d.color;orb.style.backgroundColor="#27364a";orb.classList.toggle("sun-selected",key==="sun");}
 const moons=$("solar-moons");if(moons)moons.innerHTML=d.moons.map(m=>'<span class="solar-moon-chip">'+m+'</span>').join("");
 document.querySelectorAll(".solar-pick").forEach(b=>b.classList.remove("selected"));
 const chosen=$("solar-pick-"+key);if(chosen)chosen.classList.add("selected");
}
function solarToggleMotion(){
 solarMotion=!solarMotion;
 document.querySelectorAll(".solar-orbit").forEach(o=>o.style.animationPlayState=solarMotion?"running":"paused");
 const b=$("solar-motion-btn");if(b){b.textContent=solarMotion?"Ⅱ PAUSE ORBITS":"▶ RESUME ORBITS";b.classList.toggle("active",solarMotion);}
}
function solarStop(){}
document.querySelectorAll(".solar-orbit").forEach(o=>o.style.animationPlayState="running");
solarSelect("earth");
// =============== END SOLAR SYSTEM EXPLORER ===============


// ================= MOBILE.APP SOUND ENGINE =================
// All effects are synthesized locally with Web Audio; no sound files or API keys needed.
let mobileAudioContext = null;
let mobileMasterGain = null;
let mobileLastTypeSound = 0;

function mobileAudioReady(){
  const AudioCtor = window.AudioContext || window.webkitAudioContext;
  if(!AudioCtor) return false;
  if(!mobileAudioContext){
    mobileAudioContext = new AudioCtor();
    mobileMasterGain = mobileAudioContext.createGain();
    mobileMasterGain.gain.value = 0.34;
    mobileMasterGain.connect(mobileAudioContext.destination);
  }
  if(mobileAudioContext.state === "suspended") mobileAudioContext.resume();
  return true;
}
function mobileTone(freq, duration, wave="sine", volume=0.18, endFreq=null, delay=0){
  if(!mobileAudioReady()) return;
  const ctx=mobileAudioContext, start=ctx.currentTime+delay;
  const osc=ctx.createOscillator(), gain=ctx.createGain();
  osc.type=wave; osc.frequency.setValueAtTime(freq,start);
  if(endFreq) osc.frequency.exponentialRampToValueAtTime(Math.max(1,endFreq),start+duration);
  gain.gain.setValueAtTime(0.0001,start);
  gain.gain.exponentialRampToValueAtTime(Math.max(0.0002,volume),start+Math.min(.018,duration*.25));
  gain.gain.exponentialRampToValueAtTime(0.0001,start+duration);
  osc.connect(gain); gain.connect(mobileMasterGain);
  osc.start(start); osc.stop(start+duration+.025);
}
function mobileSfx(kind){
  if(!mobileAudioContext) return;
  mobileLastSfxAt=Date.now();
  switch(kind){
    case "click": mobileTone(720,.045,"sine",.075,560); break;
    case "nav": mobileTone(520,.07,"triangle",.10,760); break;
    case "success": mobileTone(660,.12,"sine",.13);mobileTone(880,.18,"sine",.12,null,.10);mobileTone(1100,.20,"sine",.10,null,.22);break;
    case "error": mobileTone(260,.16,"triangle",.13,180);mobileTone(190,.20,"triangle",.10,130,.13);break;
    case "move": mobileTone(420,.055,"triangle",.09,520);break;
    case "left": mobileTone(360,.065,"triangle",.10,270);break;
    case "right": mobileTone(520,.065,"triangle",.10,760);break;
    case "flap": mobileTone(390,.075,"triangle",.12,690);break;
    case "point": mobileTone(880,.09,"sine",.12,1120);break;
    case "gameover": mobileTone(420,.16,"sawtooth",.10,300);mobileTone(300,.22,"triangle",.12,145,.15);break;
    case "start": mobileTone(440,.09,"triangle",.10,660);mobileTone(660,.12,"triangle",.10,880,.10);break;
    case "hit": mobileTone(210,.045,"square",.055,130);break;
    case "coin": mobileTone(980,.08,"sine",.12,1250);mobileTone(1320,.11,"sine",.10,null,.07);break;
    case "cart": mobileTone(520,.07,"triangle",.11,760);mobileTone(900,.10,"sine",.10,null,.07);break;
    case "purchase": mobileTone(523,.12,"sine",.12);mobileTone(659,.12,"sine",.12,null,.11);mobileTone(784,.18,"sine",.13,null,.22);mobileTone(1047,.22,"sine",.11,null,.37);break;
    case "space": mobileTone(180,.32,"sine",.065,260);mobileTone(360,.42,"sine",.035,310,.05);break;
    case "weather": mobileTone(560,.10,"sine",.09,720);mobileTone(740,.14,"sine",.09,880,.11);break;
    case "type": mobileTone(640,.025,"square",.035,520);break;
    case "crash": mobileTone(150,.18,"sawtooth",.12,65);break;
  }
}
// No background ambience: every sound is a short effect triggered by an action.
let mobileLastSfxAt = 0;
// Unlock audio on the first real touch/click, before inline game handlers run.
document.addEventListener("pointerdown",()=>{mobileAudioReady();},{once:true,capture:true});
document.addEventListener("click",event=>{
  const control=event.target.closest("button,[role=button],.clickable");
  if(!control) return;
  // Specific game/action handlers run before this bubbling fallback.
  if(Date.now()-mobileLastSfxAt<90) return;
  mobileSfx("click");
},false);

// Typing feedback is intentionally quiet and rate-limited.
document.addEventListener("change",event=>{
  if(event.target && event.target.tagName==="SELECT") mobileSfx("nav");
});
document.addEventListener("input",event=>{
  if(event.target && event.target.id==="typing-input"){
    const now=Date.now();
    if(now-mobileLastTypeSound>85){mobileLastTypeSound=now;mobileSfx("type");}
  }
});

// Small reusable wrappers keep the original app/game logic intact.
function mobileWrapSound(functionName, callback){
  const original=window[functionName];
  if(typeof original!=="function" || original.__mobileSoundWrapped) return;
  const wrapped=function(...args){
    const result=original.apply(this,args);
    try{callback.apply(this,args);}catch(error){}
    return result;
  };
  wrapped.__mobileSoundWrapped=true;
  window[functionName]=wrapped;
}

// Navigation and Solar System
mobileWrapSound("openPage",function(id){mobileSfx("nav");});
mobileWrapSound("goHome",function(){mobileSfx("nav");});
mobileWrapSound("solarSelect",function(){mobileSfx("space");});
mobileWrapSound("solarToggleMotion",function(){mobileSfx("move");});

// Guessing and typing games
mobileWrapSound("resetGuess",function(){mobileSfx("start");});
mobileWrapSound("makeGuess",function(){
  const message=$("guess-message")?.textContent||"";
  if(message.includes("Correct!")) mobileSfx("success");
  else if(message.includes("Game over!")) mobileSfx("gameover");
  else if(message.includes("Too low")||message.includes("Too high")) mobileSfx("error");
});
mobileWrapSound("startTyping",function(){mobileSfx("start");});
mobileWrapSound("finishTyping",function(){
  const result=$("typing-result")?.textContent||"";
  mobileSfx(result.includes("Excellent")?"success":"gameover");
});

// Flappy Bird
mobileWrapSound("startFlappy",function(){mobileSfx("start");});
mobileWrapSound("flap",function(){mobileSfx("flap");});
mobileWrapSound("endFlappy",function(){mobileSfx("gameover");});

// Snake
mobileWrapSound("startSnake",function(){mobileSnakeLastScore=0;mobileSnakeStepCounter=0;mobileSfx("start");});
let mobileSnakeLastScore=0;
let mobileSnakeStepCounter=0;
mobileWrapSound("snakeDirection",function(){mobileSfx("move");});
mobileWrapSound("snakeMove",function(){
  const score=$("snake-score")?.textContent||"";
  if(score.includes("Game over")) mobileSfx("gameover");
  else {
    const current=Number((score.match(/\d+/)||[])[0])||0;
    if(current>mobileSnakeLastScore) mobileSfx("coin");
    else if(++mobileSnakeStepCounter%4===0) mobileSfx("move");
    mobileSnakeLastScore=current;
  }
});

// Car Racing
mobileWrapSound("startCarGame",function(){mobileSfx("start");});
mobileWrapSound("moveCar",function(direction){mobileSfx(direction<0?"left":"right");});
mobileWrapSound("endCarGame",function(){mobileSfx("crash");mobileSfx("gameover");});

// Neon Breakout
mobileWrapSound("breakoutToggle",function(){mobileSfx(nbRunning?"start":"click");});
mobileWrapSound("breakoutPause",function(){mobileSfx("click");});
mobileWrapSound("breakoutRestart",function(){mobileSfx("start");});
mobileWrapSound("breakoutSetLevel",function(){mobileSfx("nav");});
mobileWrapSound("nbHitBrick",function(){mobileSfx("hit");});
mobileWrapSound("breakoutNext",function(){mobileSfx("success");});

// Shopping Store
mobileWrapSound("shopAdd",function(){mobileSfx("cart");});
mobileWrapSound("shopRemove",function(){mobileSfx("move");});
mobileWrapSound("shopSetCategory",function(){mobileSfx("nav");});
mobileWrapSound("shopToggleCart",function(){mobileSfx("cart");});
mobileWrapSound("shopCheckout",function(){
  const message=$("shop-message")?.textContent||"";
  mobileSfx(message.includes("complete")?"purchase":"error");
});

// Weather
mobileWrapSound("weatherLoad",function(){
  // The weather function is async; its completion tone is handled below.
});
const mobileWeatherLoadOriginal=window.weatherLoad;
if(typeof mobileWeatherLoadOriginal==="function" && !mobileWeatherLoadOriginal.__mobileWeatherSound){
  const wrappedWeather=async function(...args){
    mobileSfx("weather");
    const result=await mobileWeatherLoadOriginal.apply(this,args);
    const status=$("weather-status")?.textContent||"";
    mobileSfx(status.includes("could not")?"error":"success");
    return result;
  };
  wrappedWeather.__mobileWeatherSound=true;
  window.weatherLoad=wrappedWeather;
}

// Page entry effects are handled by the navigation wrapper above.

const MI_ARCHIVE = [
  {
    id:1,
    name:"The Silent Meridian · 0001",
    region:"Quiet Reach",
    signal:"a low blue pulse",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 1, and its trace number is 1.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a memory fragment"
  },
  {
    id:2,
    name:"A Silent Meridian · 0002",
    region:"Moss Quarter",
    signal:"a ripple crossing dry ground",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 2, and its trace number is 2.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 2.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A distant light answers with one measured flash.",
    reward:"a map trace"
  },
  {
    id:3,
    name:"Beneath the Silent Meridian · 0003",
    region:"Hollow Canopy",
    signal:"a pattern of footprints facing inward",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 3, and its trace number is 3.",
    clue:"A repeated step can open a door, but only once. Fragment index: 3.",
    lesson:"Observation can be a form of movement.",
    response:"The path behind you quietly changes its shape.",
    reward:"a sealed memory"
  },
  {
    id:4,
    name:"Beyond the Silent Meridian · 0004",
    region:"Lantern Expanse",
    signal:"a glow hidden inside a crack",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 4, and its trace number is 4.",
    clue:"The second path is real only after you turn away. Fragment index: 4.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The air grows still, waiting for another choice.",
    reward:"a clearer signal"
  },
  {
    id:5,
    name:"Inside the Silent Meridian · 0005",
    region:"Pale Engine",
    signal:"a door-shaped gap in the air",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 5, and its trace number is 5.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 5.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a changed landmark"
  },
  {
    id:6,
    name:"Under the Silent Meridian · 0006",
    region:"Frostline",
    signal:"a thin thread of silver light",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 6, and its trace number is 6.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 6.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The echo returns with one extra note.",
    reward:"a hidden passage"
  },
  {
    id:7,
    name:"Across the Silent Meridian · 0007",
    region:"Last Horizon",
    signal:"a reflection that arrives late",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 7, and its trace number is 7.",
    clue:"Return to the place where the floor changes colour. Fragment index: 7.",
    lesson:"Observation can be a form of movement.",
    response:"The ground glows for a moment, then settles.",
    reward:"a second chance"
  },
  {
    id:8,
    name:"Behind the Silent Meridian · 0008",
    region:"Glasswater Basin",
    signal:"a door-shaped gap in the air",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 1, and its trace number is 8.",
    clue:"The answer is stored in the order of your choices. Fragment index: 8.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A new mark appears beside your last footprint.",
    reward:"a path that remembers"
  },
  {
    id:9,
    name:"Within the Silent Meridian · 0009",
    region:"Blue Divide",
    signal:"a thin thread of silver light",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 2, and its trace number is 9.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 9.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The observer pauses, then follows at a distance.",
    reward:"an echo token"
  },
  {
    id:10,
    name:"At the edge of the Silent Meridian · 0010",
    region:"Ember Archive",
    signal:"a reflection that arrives late",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 3, and its trace number is 10.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 10.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a stored reflection"
  },
  {
    id:11,
    name:"Where the Silent Meridian · 0011",
    region:"Echo Marsh",
    signal:"a shadow moving against the light",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 4, and its trace number is 11.",
    clue:"Find the only light that does not pulse. Fragment index: 11.",
    lesson:"Observation can be a form of movement.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a new depth"
  },
  {
    id:12,
    name:"Before the Silent Meridian · 0012",
    region:"Last Horizon",
    signal:"a distant bell with no echo",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 5, and its trace number is 12.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 12.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The horizon brightens where your route bends.",
    reward:"a quiet clue"
  },
  {
    id:13,
    name:"After the Silent Meridian · 0013",
    region:"Glasswater Basin",
    signal:"a hum that follows silence",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 6, and its trace number is 13.",
    clue:"The safest route is not always the shortest. Fragment index: 13.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a memory fragment"
  },
  {
    id:14,
    name:"Between the Silent Meridian · 0014",
    region:"Blue Divide",
    signal:"a warm line beneath the stone",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 7, and its trace number is 14.",
    clue:"Your previous route is the map for this one. Fragment index: 14.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A distant light answers with one measured flash.",
    reward:"a map trace"
  },
  {
    id:15,
    name:"Above the Silent Meridian · 0015",
    region:"Ember Archive",
    signal:"a distant bell with no echo",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 1, and its trace number is 15.",
    clue:"Move once, pause once, then listen again. Fragment index: 15.",
    lesson:"Observation can be a form of movement.",
    response:"The path behind you quietly changes its shape.",
    reward:"a sealed memory"
  },
  {
    id:16,
    name:"Below the Silent Meridian · 0016",
    region:"Echo Marsh",
    signal:"a hum that follows silence",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 2, and its trace number is 16.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 16.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The air grows still, waiting for another choice.",
    reward:"a clearer signal"
  },
  {
    id:17,
    name:"The Glass Orchard · 0017",
    region:"Mirror Waste",
    signal:"a warm line beneath the stone",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 3, and its trace number is 17.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 17.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a changed landmark"
  },
  {
    id:18,
    name:"A Glass Orchard · 0018",
    region:"Quiet Reach",
    signal:"a pale mark that shifts position",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 4, and its trace number is 18.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 18.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The echo returns with one extra note.",
    reward:"a hidden passage"
  },
  {
    id:19,
    name:"Beneath the Glass Orchard · 0019",
    region:"Moss Quarter",
    signal:"a small star below the horizon",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 5, and its trace number is 19.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 19.",
    lesson:"Observation can be a form of movement.",
    response:"The ground glows for a moment, then settles.",
    reward:"a second chance"
  },
  {
    id:20,
    name:"Beyond the Glass Orchard · 0020",
    region:"Hollow Canopy",
    signal:"three notes with no source",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 6, and its trace number is 20.",
    clue:"Return to the place where the floor changes colour. Fragment index: 20.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A new mark appears beside your last footprint.",
    reward:"a path that remembers"
  },
  {
    id:21,
    name:"Inside the Glass Orchard · 0021",
    region:"Lantern Expanse",
    signal:"a slow rhythm under the wind",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 7, and its trace number is 21.",
    clue:"The answer is stored in the order of your choices. Fragment index: 21.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The observer pauses, then follows at a distance.",
    reward:"an echo token"
  },
  {
    id:22,
    name:"Under the Glass Orchard · 0022",
    region:"Pale Engine",
    signal:"a small star below the horizon",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 1, and its trace number is 22.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 22.",
    lesson:"Memory is more than a record of where you went.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a stored reflection"
  },
  {
    id:23,
    name:"Across the Glass Orchard · 0023",
    region:"Quiet Reach",
    signal:"three notes with no source",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 2, and its trace number is 23.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 23.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a new depth"
  },
  {
    id:24,
    name:"Behind the Glass Orchard · 0024",
    region:"Moss Quarter",
    signal:"a slow rhythm under the wind",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 3, and its trace number is 24.",
    clue:"Find the only light that does not pulse. Fragment index: 24.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a quiet clue"
  },
  {
    id:25,
    name:"Within the Glass Orchard · 0025",
    region:"Hollow Canopy",
    signal:"a breath behind the wall",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 4, and its trace number is 25.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 25.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A distant light answers with one measured flash.",
    reward:"a memory fragment"
  },
  {
    id:26,
    name:"At the edge of the Glass Orchard · 0026",
    region:"Lantern Expanse",
    signal:"a low blue pulse",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 5, and its trace number is 26.",
    clue:"The safest route is not always the shortest. Fragment index: 26.",
    lesson:"Memory is more than a record of where you went.",
    response:"The path behind you quietly changes its shape.",
    reward:"a map trace"
  },
  {
    id:27,
    name:"Where the Glass Orchard · 0027",
    region:"Pale Engine",
    signal:"a ripple crossing dry ground",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 6, and its trace number is 27.",
    clue:"Your previous route is the map for this one. Fragment index: 27.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The air grows still, waiting for another choice.",
    reward:"a sealed memory"
  },
  {
    id:28,
    name:"Before the Glass Orchard · 0028",
    region:"Frostline",
    signal:"a pattern of footprints facing inward",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 7, and its trace number is 28.",
    clue:"Move once, pause once, then listen again. Fragment index: 28.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a clearer signal"
  },
  {
    id:29,
    name:"After the Glass Orchard · 0029",
    region:"Last Horizon",
    signal:"a low blue pulse",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 1, and its trace number is 29.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 29.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The echo returns with one extra note.",
    reward:"a changed landmark"
  },
  {
    id:30,
    name:"Between the Glass Orchard · 0030",
    region:"Glasswater Basin",
    signal:"a ripple crossing dry ground",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 2, and its trace number is 30.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 30.",
    lesson:"Memory is more than a record of where you went.",
    response:"The ground glows for a moment, then settles.",
    reward:"a new depth"
  },
  {
    id:31,
    name:"Above the Glass Orchard · 0031",
    region:"Blue Divide",
    signal:"a pattern of footprints facing inward",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 3, and its trace number is 31.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 31.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A new mark appears beside your last footprint.",
    reward:"a quiet clue"
  },
  {
    id:32,
    name:"Below the Glass Orchard · 0032",
    region:"Ember Archive",
    signal:"a glow hidden inside a crack",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 4, and its trace number is 32.",
    clue:"A repeated step can open a door, but only once. Fragment index: 32.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a memory fragment"
  },
  {
    id:33,
    name:"The Hollow Stair · 0033",
    region:"Echo Marsh",
    signal:"a door-shaped gap in the air",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 5, and its trace number is 33.",
    clue:"The second path is real only after you turn away. Fragment index: 33.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a map trace"
  },
  {
    id:34,
    name:"A Hollow Stair · 0034",
    region:"Last Horizon",
    signal:"a thin thread of silver light",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 6, and its trace number is 34.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 34.",
    lesson:"Memory is more than a record of where you went.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a sealed memory"
  },
  {
    id:35,
    name:"Beneath the Hollow Stair · 0035",
    region:"Glasswater Basin",
    signal:"a reflection that arrives late",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 7, and its trace number is 35.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 35.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The horizon brightens where your route bends.",
    reward:"a clearer signal"
  },
  {
    id:36,
    name:"Beyond the Hollow Stair · 0036",
    region:"Blue Divide",
    signal:"a door-shaped gap in the air",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 1, and its trace number is 36.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 36.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a changed landmark"
  },
  {
    id:37,
    name:"Inside the Hollow Stair · 0037",
    region:"Ember Archive",
    signal:"a thin thread of silver light",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 2, and its trace number is 37.",
    clue:"Find the only light that does not pulse. Fragment index: 37.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A distant light answers with one measured flash.",
    reward:"a hidden passage"
  },
  {
    id:38,
    name:"Under the Hollow Stair · 0038",
    region:"Echo Marsh",
    signal:"a reflection that arrives late",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 3, and its trace number is 38.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 38.",
    lesson:"Memory is more than a record of where you went.",
    response:"The path behind you quietly changes its shape.",
    reward:"a second chance"
  },
  {
    id:39,
    name:"Across the Hollow Stair · 0039",
    region:"Mirror Waste",
    signal:"a shadow moving against the light",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 4, and its trace number is 39.",
    clue:"The safest route is not always the shortest. Fragment index: 39.",
    lesson:"Silence is information when you learn to listen.",
    response:"The air grows still, waiting for another choice.",
    reward:"a path that remembers"
  },
  {
    id:40,
    name:"Behind the Hollow Stair · 0040",
    region:"Quiet Reach",
    signal:"a distant bell with no echo",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 5, and its trace number is 40.",
    clue:"Your previous route is the map for this one. Fragment index: 40.",
    lesson:"Returning is not the same as repeating.",
    response:"A small opening appears in the wall of darkness.",
    reward:"an echo token"
  },
  {
    id:41,
    name:"Within the Hollow Stair · 0041",
    region:"Moss Quarter",
    signal:"a hum that follows silence",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 6, and its trace number is 41.",
    clue:"Move once, pause once, then listen again. Fragment index: 41.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The echo returns with one extra note.",
    reward:"a stored reflection"
  },
  {
    id:42,
    name:"At the edge of the Hollow Stair · 0042",
    region:"Hollow Canopy",
    signal:"a warm line beneath the stone",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 7, and its trace number is 42.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 42.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The ground glows for a moment, then settles.",
    reward:"a new depth"
  },
  {
    id:43,
    name:"Where the Hollow Stair · 0043",
    region:"Lantern Expanse",
    signal:"a distant bell with no echo",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 1, and its trace number is 43.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 43.",
    lesson:"Silence is information when you learn to listen.",
    response:"A new mark appears beside your last footprint.",
    reward:"a quiet clue"
  },
  {
    id:44,
    name:"Before the Hollow Stair · 0044",
    region:"Pale Engine",
    signal:"a hum that follows silence",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 2, and its trace number is 44.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 44.",
    lesson:"Returning is not the same as repeating.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a memory fragment"
  },
  {
    id:45,
    name:"After the Hollow Stair · 0045",
    region:"Quiet Reach",
    signal:"a warm line beneath the stone",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 3, and its trace number is 45.",
    clue:"A repeated step can open a door, but only once. Fragment index: 45.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a map trace"
  },
  {
    id:46,
    name:"Between the Hollow Stair · 0046",
    region:"Moss Quarter",
    signal:"a pale mark that shifts position",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 4, and its trace number is 46.",
    clue:"The second path is real only after you turn away. Fragment index: 46.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a sealed memory"
  },
  {
    id:47,
    name:"Above the Hollow Stair · 0047",
    region:"Hollow Canopy",
    signal:"a small star below the horizon",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 5, and its trace number is 47.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 47.",
    lesson:"Silence is information when you learn to listen.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a clearer signal"
  },
  {
    id:48,
    name:"Below the Hollow Stair · 0048",
    region:"Lantern Expanse",
    signal:"three notes with no source",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 6, and its trace number is 48.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 48.",
    lesson:"Returning is not the same as repeating.",
    response:"A distant light answers with one measured flash.",
    reward:"a changed landmark"
  },
  {
    id:49,
    name:"The Blue Archive · 0049",
    region:"Pale Engine",
    signal:"a slow rhythm under the wind",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 7, and its trace number is 49.",
    clue:"Return to the place where the floor changes colour. Fragment index: 49.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The path behind you quietly changes its shape.",
    reward:"a hidden passage"
  },
  {
    id:50,
    name:"A Blue Archive · 0050",
    region:"Frostline",
    signal:"a small star below the horizon",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 1, and its trace number is 50.",
    clue:"The answer is stored in the order of your choices. Fragment index: 50.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The air grows still, waiting for another choice.",
    reward:"a second chance"
  },
  {
    id:51,
    name:"Beneath the Blue Archive · 0051",
    region:"Last Horizon",
    signal:"three notes with no source",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 2, and its trace number is 51.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 51.",
    lesson:"Silence is information when you learn to listen.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a path that remembers"
  },
  {
    id:52,
    name:"Beyond the Blue Archive · 0052",
    region:"Glasswater Basin",
    signal:"a slow rhythm under the wind",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 3, and its trace number is 52.",
    clue:"The safest route is not always the shortest. Fragment index: 52.",
    lesson:"Returning is not the same as repeating.",
    response:"The echo returns with one extra note.",
    reward:"an echo token"
  },
  {
    id:53,
    name:"Inside the Blue Archive · 0053",
    region:"Blue Divide",
    signal:"a breath behind the wall",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 4, and its trace number is 53.",
    clue:"Your previous route is the map for this one. Fragment index: 53.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The ground glows for a moment, then settles.",
    reward:"a stored reflection"
  },
  {
    id:54,
    name:"Under the Blue Archive · 0054",
    region:"Ember Archive",
    signal:"a low blue pulse",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 5, and its trace number is 54.",
    clue:"Move once, pause once, then listen again. Fragment index: 54.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A new mark appears beside your last footprint.",
    reward:"a new depth"
  },
  {
    id:55,
    name:"Across the Blue Archive · 0055",
    region:"Echo Marsh",
    signal:"a ripple crossing dry ground",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 6, and its trace number is 55.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 55.",
    lesson:"Silence is information when you learn to listen.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a quiet clue"
  },
  {
    id:56,
    name:"Behind the Blue Archive · 0056",
    region:"Last Horizon",
    signal:"a pattern of footprints facing inward",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 7, and its trace number is 56.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 56.",
    lesson:"Returning is not the same as repeating.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a memory fragment"
  },
  {
    id:57,
    name:"Within the Blue Archive · 0057",
    region:"Glasswater Basin",
    signal:"a low blue pulse",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 1, and its trace number is 57.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 57.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a map trace"
  },
  {
    id:58,
    name:"At the edge of the Blue Archive · 0058",
    region:"Blue Divide",
    signal:"a ripple crossing dry ground",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 2, and its trace number is 58.",
    clue:"A repeated step can open a door, but only once. Fragment index: 58.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The horizon brightens where your route bends.",
    reward:"a sealed memory"
  },
  {
    id:59,
    name:"Where the Blue Archive · 0059",
    region:"Ember Archive",
    signal:"a pattern of footprints facing inward",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 3, and its trace number is 59.",
    clue:"The second path is real only after you turn away. Fragment index: 59.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"an echo token"
  },
  {
    id:60,
    name:"Before the Blue Archive · 0060",
    region:"Echo Marsh",
    signal:"a glow hidden inside a crack",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 4, and its trace number is 60.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 60.",
    lesson:"Observation can be a form of movement.",
    response:"A distant light answers with one measured flash.",
    reward:"a stored reflection"
  },
  {
    id:61,
    name:"After the Blue Archive · 0061",
    region:"Mirror Waste",
    signal:"a door-shaped gap in the air",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 5, and its trace number is 61.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 61.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The path behind you quietly changes its shape.",
    reward:"a new depth"
  },
  {
    id:62,
    name:"Between the Blue Archive · 0062",
    region:"Quiet Reach",
    signal:"a thin thread of silver light",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 6, and its trace number is 62.",
    clue:"Return to the place where the floor changes colour. Fragment index: 62.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The air grows still, waiting for another choice.",
    reward:"a quiet clue"
  },
  {
    id:63,
    name:"Above the Blue Archive · 0063",
    region:"Moss Quarter",
    signal:"a reflection that arrives late",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 7, and its trace number is 63.",
    clue:"The answer is stored in the order of your choices. Fragment index: 63.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a memory fragment"
  },
  {
    id:64,
    name:"Below the Blue Archive · 0064",
    region:"Hollow Canopy",
    signal:"a door-shaped gap in the air",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 1, and its trace number is 64.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 64.",
    lesson:"Observation can be a form of movement.",
    response:"The echo returns with one extra note.",
    reward:"a map trace"
  },
  {
    id:65,
    name:"The Ashen Bridge · 0065",
    region:"Lantern Expanse",
    signal:"a thin thread of silver light",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 2, and its trace number is 65.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 65.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The ground glows for a moment, then settles.",
    reward:"a sealed memory"
  },
  {
    id:66,
    name:"A Ashen Bridge · 0066",
    region:"Pale Engine",
    signal:"a reflection that arrives late",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 3, and its trace number is 66.",
    clue:"Find the only light that does not pulse. Fragment index: 66.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A new mark appears beside your last footprint.",
    reward:"a clearer signal"
  },
  {
    id:67,
    name:"Beneath the Ashen Bridge · 0067",
    region:"Quiet Reach",
    signal:"a shadow moving against the light",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 4, and its trace number is 67.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 67.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a changed landmark"
  },
  {
    id:68,
    name:"Beyond the Ashen Bridge · 0068",
    region:"Moss Quarter",
    signal:"a distant bell with no echo",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 5, and its trace number is 68.",
    clue:"The safest route is not always the shortest. Fragment index: 68.",
    lesson:"Observation can be a form of movement.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a hidden passage"
  },
  {
    id:69,
    name:"Inside the Ashen Bridge · 0069",
    region:"Hollow Canopy",
    signal:"a hum that follows silence",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 6, and its trace number is 69.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 69.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a second chance"
  },
  {
    id:70,
    name:"Under the Ashen Bridge · 0070",
    region:"Lantern Expanse",
    signal:"a warm line beneath the stone",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 7, and its trace number is 70.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 70.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a path that remembers"
  },
  {
    id:71,
    name:"Across the Ashen Bridge · 0071",
    region:"Pale Engine",
    signal:"a distant bell with no echo",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 1, and its trace number is 71.",
    clue:"A repeated step can open a door, but only once. Fragment index: 71.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A distant light answers with one measured flash.",
    reward:"an echo token"
  },
  {
    id:72,
    name:"Behind the Ashen Bridge · 0072",
    region:"Frostline",
    signal:"a hum that follows silence",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 2, and its trace number is 72.",
    clue:"The second path is real only after you turn away. Fragment index: 72.",
    lesson:"Observation can be a form of movement.",
    response:"The path behind you quietly changes its shape.",
    reward:"a stored reflection"
  },
  {
    id:73,
    name:"Within the Ashen Bridge · 0073",
    region:"Last Horizon",
    signal:"a warm line beneath the stone",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 3, and its trace number is 73.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 73.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The air grows still, waiting for another choice.",
    reward:"a new depth"
  },
  {
    id:74,
    name:"At the edge of the Ashen Bridge · 0074",
    region:"Glasswater Basin",
    signal:"a pale mark that shifts position",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 4, and its trace number is 74.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 74.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a quiet clue"
  },
  {
    id:75,
    name:"Where the Ashen Bridge · 0075",
    region:"Blue Divide",
    signal:"a small star below the horizon",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 5, and its trace number is 75.",
    clue:"Return to the place where the floor changes colour. Fragment index: 75.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The echo returns with one extra note.",
    reward:"a memory fragment"
  },
  {
    id:76,
    name:"Before the Ashen Bridge · 0076",
    region:"Ember Archive",
    signal:"three notes with no source",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 6, and its trace number is 76.",
    clue:"The answer is stored in the order of your choices. Fragment index: 76.",
    lesson:"Observation can be a form of movement.",
    response:"The ground glows for a moment, then settles.",
    reward:"a map trace"
  },
  {
    id:77,
    name:"After the Ashen Bridge · 0077",
    region:"Echo Marsh",
    signal:"a slow rhythm under the wind",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 7, and its trace number is 77.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 77.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A new mark appears beside your last footprint.",
    reward:"a sealed memory"
  },
  {
    id:78,
    name:"Between the Ashen Bridge · 0078",
    region:"Last Horizon",
    signal:"a small star below the horizon",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 1, and its trace number is 78.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 78.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a clearer signal"
  },
  {
    id:79,
    name:"Above the Ashen Bridge · 0079",
    region:"Glasswater Basin",
    signal:"three notes with no source",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 2, and its trace number is 79.",
    clue:"Find the only light that does not pulse. Fragment index: 79.",
    lesson:"Memory is more than a record of where you went.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a changed landmark"
  },
  {
    id:80,
    name:"Below the Ashen Bridge · 0080",
    region:"Blue Divide",
    signal:"a slow rhythm under the wind",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 3, and its trace number is 80.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 80.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a hidden passage"
  },
  {
    id:81,
    name:"The Mirror Field · 0081",
    region:"Ember Archive",
    signal:"a breath behind the wall",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 4, and its trace number is 81.",
    clue:"The safest route is not always the shortest. Fragment index: 81.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The horizon brightens where your route bends.",
    reward:"a second chance"
  },
  {
    id:82,
    name:"A Mirror Field · 0082",
    region:"Echo Marsh",
    signal:"a low blue pulse",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 5, and its trace number is 82.",
    clue:"Your previous route is the map for this one. Fragment index: 82.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a path that remembers"
  },
  {
    id:83,
    name:"Beneath the Mirror Field · 0083",
    region:"Mirror Waste",
    signal:"a ripple crossing dry ground",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 6, and its trace number is 83.",
    clue:"Move once, pause once, then listen again. Fragment index: 83.",
    lesson:"Memory is more than a record of where you went.",
    response:"A distant light answers with one measured flash.",
    reward:"an echo token"
  },
  {
    id:84,
    name:"Beyond the Mirror Field · 0084",
    region:"Quiet Reach",
    signal:"a pattern of footprints facing inward",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 7, and its trace number is 84.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 84.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The path behind you quietly changes its shape.",
    reward:"a stored reflection"
  },
  {
    id:85,
    name:"Inside the Mirror Field · 0085",
    region:"Moss Quarter",
    signal:"a low blue pulse",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 1, and its trace number is 85.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 85.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The air grows still, waiting for another choice.",
    reward:"a new depth"
  },
  {
    id:86,
    name:"Under the Mirror Field · 0086",
    region:"Hollow Canopy",
    signal:"a ripple crossing dry ground",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 2, and its trace number is 86.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 86.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a quiet clue"
  },
  {
    id:87,
    name:"Across the Mirror Field · 0087",
    region:"Lantern Expanse",
    signal:"a pattern of footprints facing inward",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 3, and its trace number is 87.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 87.",
    lesson:"Memory is more than a record of where you went.",
    response:"The echo returns with one extra note.",
    reward:"a memory fragment"
  },
  {
    id:88,
    name:"Behind the Mirror Field · 0088",
    region:"Pale Engine",
    signal:"a glow hidden inside a crack",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 4, and its trace number is 88.",
    clue:"Return to the place where the floor changes colour. Fragment index: 88.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The ground glows for a moment, then settles.",
    reward:"a second chance"
  },
  {
    id:89,
    name:"Within the Mirror Field · 0089",
    region:"Quiet Reach",
    signal:"a door-shaped gap in the air",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 5, and its trace number is 89.",
    clue:"The answer is stored in the order of your choices. Fragment index: 89.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A new mark appears beside your last footprint.",
    reward:"a path that remembers"
  },
  {
    id:90,
    name:"At the edge of the Mirror Field · 0090",
    region:"Moss Quarter",
    signal:"a thin thread of silver light",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 6, and its trace number is 90.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 90.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The observer pauses, then follows at a distance.",
    reward:"an echo token"
  },
  {
    id:91,
    name:"Where the Mirror Field · 0091",
    region:"Hollow Canopy",
    signal:"a reflection that arrives late",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 7, and its trace number is 91.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 91.",
    lesson:"Memory is more than a record of where you went.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a stored reflection"
  },
  {
    id:92,
    name:"Before the Mirror Field · 0092",
    region:"Lantern Expanse",
    signal:"a door-shaped gap in the air",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 1, and its trace number is 92.",
    clue:"Find the only light that does not pulse. Fragment index: 92.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a new depth"
  },
  {
    id:93,
    name:"After the Mirror Field · 0093",
    region:"Pale Engine",
    signal:"a thin thread of silver light",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 2, and its trace number is 93.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 93.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a quiet clue"
  },
  {
    id:94,
    name:"Between the Mirror Field · 0094",
    region:"Frostline",
    signal:"a reflection that arrives late",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 3, and its trace number is 94.",
    clue:"The safest route is not always the shortest. Fragment index: 94.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A distant light answers with one measured flash.",
    reward:"a memory fragment"
  },
  {
    id:95,
    name:"Above the Mirror Field · 0095",
    region:"Last Horizon",
    signal:"a shadow moving against the light",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 4, and its trace number is 95.",
    clue:"Your previous route is the map for this one. Fragment index: 95.",
    lesson:"Memory is more than a record of where you went.",
    response:"The path behind you quietly changes its shape.",
    reward:"a map trace"
  },
  {
    id:96,
    name:"Below the Mirror Field · 0096",
    region:"Glasswater Basin",
    signal:"a distant bell with no echo",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 5, and its trace number is 96.",
    clue:"Move once, pause once, then listen again. Fragment index: 96.",
    lesson:"Silence is information when you learn to listen.",
    response:"The air grows still, waiting for another choice.",
    reward:"a sealed memory"
  },
  {
    id:97,
    name:"The Sleeping Engine · 0097",
    region:"Blue Divide",
    signal:"a hum that follows silence",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 6, and its trace number is 97.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 97.",
    lesson:"Returning is not the same as repeating.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a clearer signal"
  },
  {
    id:98,
    name:"A Sleeping Engine · 0098",
    region:"Ember Archive",
    signal:"a warm line beneath the stone",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 7, and its trace number is 98.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 98.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The echo returns with one extra note.",
    reward:"a changed landmark"
  },
  {
    id:99,
    name:"Beneath the Sleeping Engine · 0099",
    region:"Echo Marsh",
    signal:"a distant bell with no echo",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 1, and its trace number is 99.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 99.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The ground glows for a moment, then settles.",
    reward:"a hidden passage"
  },
  {
    id:100,
    name:"Beyond the Sleeping Engine · 0100",
    region:"Last Horizon",
    signal:"a hum that follows silence",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 2, and its trace number is 100.",
    clue:"A repeated step can open a door, but only once. Fragment index: 100.",
    lesson:"Silence is information when you learn to listen.",
    response:"A new mark appears beside your last footprint.",
    reward:"a second chance"
  },
  {
    id:101,
    name:"Inside the Sleeping Engine · 0101",
    region:"Glasswater Basin",
    signal:"a warm line beneath the stone",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 3, and its trace number is 101.",
    clue:"The second path is real only after you turn away. Fragment index: 101.",
    lesson:"Returning is not the same as repeating.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a path that remembers"
  },
  {
    id:102,
    name:"Under the Sleeping Engine · 0102",
    region:"Blue Divide",
    signal:"a pale mark that shifts position",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 4, and its trace number is 102.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 102.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"an echo token"
  },
  {
    id:103,
    name:"Across the Sleeping Engine · 0103",
    region:"Ember Archive",
    signal:"a small star below the horizon",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 5, and its trace number is 103.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 103.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a stored reflection"
  },
  {
    id:104,
    name:"Behind the Sleeping Engine · 0104",
    region:"Echo Marsh",
    signal:"three notes with no source",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 6, and its trace number is 104.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 104.",
    lesson:"Silence is information when you learn to listen.",
    response:"The horizon brightens where your route bends.",
    reward:"a new depth"
  },
  {
    id:105,
    name:"Within the Sleeping Engine · 0105",
    region:"Mirror Waste",
    signal:"a slow rhythm under the wind",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 7, and its trace number is 105.",
    clue:"Find the only light that does not pulse. Fragment index: 105.",
    lesson:"Returning is not the same as repeating.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a quiet clue"
  },
  {
    id:106,
    name:"At the edge of the Sleeping Engine · 0106",
    region:"Quiet Reach",
    signal:"a small star below the horizon",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 1, and its trace number is 106.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 106.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A distant light answers with one measured flash.",
    reward:"a memory fragment"
  },
  {
    id:107,
    name:"Where the Sleeping Engine · 0107",
    region:"Moss Quarter",
    signal:"three notes with no source",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 2, and its trace number is 107.",
    clue:"The safest route is not always the shortest. Fragment index: 107.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The path behind you quietly changes its shape.",
    reward:"a map trace"
  },
  {
    id:108,
    name:"Before the Sleeping Engine · 0108",
    region:"Hollow Canopy",
    signal:"a slow rhythm under the wind",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 3, and its trace number is 108.",
    clue:"Your previous route is the map for this one. Fragment index: 108.",
    lesson:"Silence is information when you learn to listen.",
    response:"The air grows still, waiting for another choice.",
    reward:"a sealed memory"
  },
  {
    id:109,
    name:"After the Sleeping Engine · 0109",
    region:"Lantern Expanse",
    signal:"a breath behind the wall",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 4, and its trace number is 109.",
    clue:"Move once, pause once, then listen again. Fragment index: 109.",
    lesson:"Returning is not the same as repeating.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a clearer signal"
  },
  {
    id:110,
    name:"Between the Sleeping Engine · 0110",
    region:"Pale Engine",
    signal:"a low blue pulse",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 5, and its trace number is 110.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 110.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The echo returns with one extra note.",
    reward:"a changed landmark"
  },
  {
    id:111,
    name:"Above the Sleeping Engine · 0111",
    region:"Quiet Reach",
    signal:"a ripple crossing dry ground",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 6, and its trace number is 111.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 111.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The ground glows for a moment, then settles.",
    reward:"a hidden passage"
  },
  {
    id:112,
    name:"Below the Sleeping Engine · 0112",
    region:"Moss Quarter",
    signal:"a pattern of footprints facing inward",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 7, and its trace number is 112.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 112.",
    lesson:"Silence is information when you learn to listen.",
    response:"A new mark appears beside your last footprint.",
    reward:"a second chance"
  },
  {
    id:113,
    name:"The Distant Choir · 0113",
    region:"Hollow Canopy",
    signal:"a low blue pulse",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 1, and its trace number is 113.",
    clue:"A repeated step can open a door, but only once. Fragment index: 113.",
    lesson:"Returning is not the same as repeating.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a path that remembers"
  },
  {
    id:114,
    name:"A Distant Choir · 0114",
    region:"Lantern Expanse",
    signal:"a ripple crossing dry ground",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 2, and its trace number is 114.",
    clue:"The second path is real only after you turn away. Fragment index: 114.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"an echo token"
  },
  {
    id:115,
    name:"Beneath the Distant Choir · 0115",
    region:"Pale Engine",
    signal:"a pattern of footprints facing inward",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 3, and its trace number is 115.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 115.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a stored reflection"
  },
  {
    id:116,
    name:"Beyond the Distant Choir · 0116",
    region:"Frostline",
    signal:"a glow hidden inside a crack",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 4, and its trace number is 116.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 116.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a new depth"
  },
  {
    id:117,
    name:"Inside the Distant Choir · 0117",
    region:"Last Horizon",
    signal:"a door-shaped gap in the air",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 5, and its trace number is 117.",
    clue:"Return to the place where the floor changes colour. Fragment index: 117.",
    lesson:"Observation can be a form of movement.",
    response:"A distant light answers with one measured flash.",
    reward:"a changed landmark"
  },
  {
    id:118,
    name:"Under the Distant Choir · 0118",
    region:"Glasswater Basin",
    signal:"a thin thread of silver light",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 6, and its trace number is 118.",
    clue:"The answer is stored in the order of your choices. Fragment index: 118.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The path behind you quietly changes its shape.",
    reward:"a hidden passage"
  },
  {
    id:119,
    name:"Across the Distant Choir · 0119",
    region:"Blue Divide",
    signal:"a reflection that arrives late",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 7, and its trace number is 119.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 119.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The air grows still, waiting for another choice.",
    reward:"a second chance"
  },
  {
    id:120,
    name:"Behind the Distant Choir · 0120",
    region:"Ember Archive",
    signal:"a door-shaped gap in the air",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 1, and its trace number is 120.",
    clue:"The safest route is not always the shortest. Fragment index: 120.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a path that remembers"
  },
  {
    id:121,
    name:"Within the Distant Choir · 0121",
    region:"Echo Marsh",
    signal:"a thin thread of silver light",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 2, and its trace number is 121.",
    clue:"Your previous route is the map for this one. Fragment index: 121.",
    lesson:"Observation can be a form of movement.",
    response:"The echo returns with one extra note.",
    reward:"an echo token"
  },
  {
    id:122,
    name:"At the edge of the Distant Choir · 0122",
    region:"Last Horizon",
    signal:"a reflection that arrives late",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 3, and its trace number is 122.",
    clue:"Move once, pause once, then listen again. Fragment index: 122.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The ground glows for a moment, then settles.",
    reward:"a stored reflection"
  },
  {
    id:123,
    name:"Where the Distant Choir · 0123",
    region:"Glasswater Basin",
    signal:"a shadow moving against the light",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 4, and its trace number is 123.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 123.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A new mark appears beside your last footprint.",
    reward:"a new depth"
  },
  {
    id:124,
    name:"Before the Distant Choir · 0124",
    region:"Blue Divide",
    signal:"a distant bell with no echo",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 5, and its trace number is 124.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 124.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a quiet clue"
  },
  {
    id:125,
    name:"After the Distant Choir · 0125",
    region:"Ember Archive",
    signal:"a hum that follows silence",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 6, and its trace number is 125.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 125.",
    lesson:"Observation can be a form of movement.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a memory fragment"
  },
  {
    id:126,
    name:"Between the Distant Choir · 0126",
    region:"Echo Marsh",
    signal:"a warm line beneath the stone",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 7, and its trace number is 126.",
    clue:"A repeated step can open a door, but only once. Fragment index: 126.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a map trace"
  },
  {
    id:127,
    name:"Above the Distant Choir · 0127",
    region:"Mirror Waste",
    signal:"a distant bell with no echo",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 1, and its trace number is 127.",
    clue:"The second path is real only after you turn away. Fragment index: 127.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The horizon brightens where your route bends.",
    reward:"a sealed memory"
  },
  {
    id:128,
    name:"Below the Distant Choir · 0128",
    region:"Quiet Reach",
    signal:"a hum that follows silence",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 2, and its trace number is 128.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 128.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a clearer signal"
  },
  {
    id:129,
    name:"The Pale Garden · 0129",
    region:"Moss Quarter",
    signal:"a warm line beneath the stone",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 3, and its trace number is 129.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 129.",
    lesson:"Observation can be a form of movement.",
    response:"A distant light answers with one measured flash.",
    reward:"a changed landmark"
  },
  {
    id:130,
    name:"A Pale Garden · 0130",
    region:"Hollow Canopy",
    signal:"a pale mark that shifts position",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 4, and its trace number is 130.",
    clue:"Return to the place where the floor changes colour. Fragment index: 130.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The path behind you quietly changes its shape.",
    reward:"a hidden passage"
  },
  {
    id:131,
    name:"Beneath the Pale Garden · 0131",
    region:"Lantern Expanse",
    signal:"a small star below the horizon",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 5, and its trace number is 131.",
    clue:"The answer is stored in the order of your choices. Fragment index: 131.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The air grows still, waiting for another choice.",
    reward:"a second chance"
  },
  {
    id:132,
    name:"Beyond the Pale Garden · 0132",
    region:"Pale Engine",
    signal:"three notes with no source",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 6, and its trace number is 132.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 132.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a path that remembers"
  },
  {
    id:133,
    name:"Inside the Pale Garden · 0133",
    region:"Quiet Reach",
    signal:"a slow rhythm under the wind",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 7, and its trace number is 133.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 133.",
    lesson:"Observation can be a form of movement.",
    response:"The echo returns with one extra note.",
    reward:"an echo token"
  },
  {
    id:134,
    name:"Under the Pale Garden · 0134",
    region:"Moss Quarter",
    signal:"a small star below the horizon",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 1, and its trace number is 134.",
    clue:"Find the only light that does not pulse. Fragment index: 134.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The ground glows for a moment, then settles.",
    reward:"a stored reflection"
  },
  {
    id:135,
    name:"Across the Pale Garden · 0135",
    region:"Hollow Canopy",
    signal:"three notes with no source",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 2, and its trace number is 135.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 135.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A new mark appears beside your last footprint.",
    reward:"a new depth"
  },
  {
    id:136,
    name:"Behind the Pale Garden · 0136",
    region:"Lantern Expanse",
    signal:"a slow rhythm under the wind",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 3, and its trace number is 136.",
    clue:"The safest route is not always the shortest. Fragment index: 136.",
    lesson:"Memory is more than a record of where you went.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a quiet clue"
  },
  {
    id:137,
    name:"Within the Pale Garden · 0137",
    region:"Pale Engine",
    signal:"a breath behind the wall",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 4, and its trace number is 137.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 137.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a memory fragment"
  },
  {
    id:138,
    name:"At the edge of the Pale Garden · 0138",
    region:"Frostline",
    signal:"a low blue pulse",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 5, and its trace number is 138.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 138.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a map trace"
  },
  {
    id:139,
    name:"Where the Pale Garden · 0139",
    region:"Last Horizon",
    signal:"a ripple crossing dry ground",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 6, and its trace number is 139.",
    clue:"A repeated step can open a door, but only once. Fragment index: 139.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a sealed memory"
  },
  {
    id:140,
    name:"Before the Pale Garden · 0140",
    region:"Glasswater Basin",
    signal:"a pattern of footprints facing inward",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 7, and its trace number is 140.",
    clue:"The second path is real only after you turn away. Fragment index: 140.",
    lesson:"Memory is more than a record of where you went.",
    response:"A distant light answers with one measured flash.",
    reward:"a clearer signal"
  },
  {
    id:141,
    name:"After the Pale Garden · 0141",
    region:"Blue Divide",
    signal:"a low blue pulse",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 1, and its trace number is 141.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 141.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The path behind you quietly changes its shape.",
    reward:"a changed landmark"
  },
  {
    id:142,
    name:"Between the Pale Garden · 0142",
    region:"Ember Archive",
    signal:"a ripple crossing dry ground",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 2, and its trace number is 142.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 142.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The air grows still, waiting for another choice.",
    reward:"a hidden passage"
  },
  {
    id:143,
    name:"Above the Pale Garden · 0143",
    region:"Echo Marsh",
    signal:"a pattern of footprints facing inward",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 3, and its trace number is 143.",
    clue:"Return to the place where the floor changes colour. Fragment index: 143.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a second chance"
  },
  {
    id:144,
    name:"Below the Pale Garden · 0144",
    region:"Last Horizon",
    signal:"a glow hidden inside a crack",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 4, and its trace number is 144.",
    clue:"The answer is stored in the order of your choices. Fragment index: 144.",
    lesson:"Memory is more than a record of where you went.",
    response:"The echo returns with one extra note.",
    reward:"a path that remembers"
  },
  {
    id:145,
    name:"The Forgotten Door · 0145",
    region:"Glasswater Basin",
    signal:"a door-shaped gap in the air",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 5, and its trace number is 145.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 145.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The ground glows for a moment, then settles.",
    reward:"an echo token"
  },
  {
    id:146,
    name:"A Forgotten Door · 0146",
    region:"Blue Divide",
    signal:"a thin thread of silver light",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 6, and its trace number is 146.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 146.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A new mark appears beside your last footprint.",
    reward:"a sealed memory"
  },
  {
    id:147,
    name:"Beneath the Forgotten Door · 0147",
    region:"Ember Archive",
    signal:"a reflection that arrives late",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 7, and its trace number is 147.",
    clue:"Find the only light that does not pulse. Fragment index: 147.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a clearer signal"
  },
  {
    id:148,
    name:"Beyond the Forgotten Door · 0148",
    region:"Echo Marsh",
    signal:"a door-shaped gap in the air",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 1, and its trace number is 148.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 148.",
    lesson:"Memory is more than a record of where you went.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a changed landmark"
  },
  {
    id:149,
    name:"Inside the Forgotten Door · 0149",
    region:"Mirror Waste",
    signal:"a thin thread of silver light",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 2, and its trace number is 149.",
    clue:"The safest route is not always the shortest. Fragment index: 149.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a hidden passage"
  },
  {
    id:150,
    name:"Under the Forgotten Door · 0150",
    region:"Quiet Reach",
    signal:"a reflection that arrives late",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 3, and its trace number is 150.",
    clue:"Your previous route is the map for this one. Fragment index: 150.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The horizon brightens where your route bends.",
    reward:"a second chance"
  },
  {
    id:151,
    name:"Across the Forgotten Door · 0151",
    region:"Moss Quarter",
    signal:"a shadow moving against the light",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 4, and its trace number is 151.",
    clue:"Move once, pause once, then listen again. Fragment index: 151.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a path that remembers"
  },
  {
    id:152,
    name:"Behind the Forgotten Door · 0152",
    region:"Hollow Canopy",
    signal:"a distant bell with no echo",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 5, and its trace number is 152.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 152.",
    lesson:"Memory is more than a record of where you went.",
    response:"A distant light answers with one measured flash.",
    reward:"an echo token"
  },
  {
    id:153,
    name:"Within the Forgotten Door · 0153",
    region:"Lantern Expanse",
    signal:"a hum that follows silence",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 6, and its trace number is 153.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 153.",
    lesson:"Silence is information when you learn to listen.",
    response:"The path behind you quietly changes its shape.",
    reward:"a stored reflection"
  },
  {
    id:154,
    name:"At the edge of the Forgotten Door · 0154",
    region:"Pale Engine",
    signal:"a warm line beneath the stone",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 7, and its trace number is 154.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 154.",
    lesson:"Returning is not the same as repeating.",
    response:"The air grows still, waiting for another choice.",
    reward:"a new depth"
  },
  {
    id:155,
    name:"Where the Forgotten Door · 0155",
    region:"Quiet Reach",
    signal:"a distant bell with no echo",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 1, and its trace number is 155.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 155.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a quiet clue"
  },
  {
    id:156,
    name:"Before the Forgotten Door · 0156",
    region:"Moss Quarter",
    signal:"a hum that follows silence",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 2, and its trace number is 156.",
    clue:"Return to the place where the floor changes colour. Fragment index: 156.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The echo returns with one extra note.",
    reward:"a memory fragment"
  },
  {
    id:157,
    name:"After the Forgotten Door · 0157",
    region:"Hollow Canopy",
    signal:"a warm line beneath the stone",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 3, and its trace number is 157.",
    clue:"The answer is stored in the order of your choices. Fragment index: 157.",
    lesson:"Silence is information when you learn to listen.",
    response:"The ground glows for a moment, then settles.",
    reward:"a map trace"
  },
  {
    id:158,
    name:"Between the Forgotten Door · 0158",
    region:"Lantern Expanse",
    signal:"a pale mark that shifts position",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 4, and its trace number is 158.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 158.",
    lesson:"Returning is not the same as repeating.",
    response:"A new mark appears beside your last footprint.",
    reward:"a sealed memory"
  },
  {
    id:159,
    name:"Above the Forgotten Door · 0159",
    region:"Pale Engine",
    signal:"a small star below the horizon",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 5, and its trace number is 159.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 159.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a clearer signal"
  },
  {
    id:160,
    name:"Below the Forgotten Door · 0160",
    region:"Frostline",
    signal:"three notes with no source",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 6, and its trace number is 160.",
    clue:"Find the only light that does not pulse. Fragment index: 160.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a changed landmark"
  },
  {
    id:161,
    name:"The Wandering Signal · 0161",
    region:"Last Horizon",
    signal:"a slow rhythm under the wind",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 7, and its trace number is 161.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 161.",
    lesson:"Silence is information when you learn to listen.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a hidden passage"
  },
  {
    id:162,
    name:"A Wandering Signal · 0162",
    region:"Glasswater Basin",
    signal:"a small star below the horizon",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 1, and its trace number is 162.",
    clue:"The safest route is not always the shortest. Fragment index: 162.",
    lesson:"Returning is not the same as repeating.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a second chance"
  },
  {
    id:163,
    name:"Beneath the Wandering Signal · 0163",
    region:"Blue Divide",
    signal:"three notes with no source",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 2, and its trace number is 163.",
    clue:"Your previous route is the map for this one. Fragment index: 163.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A distant light answers with one measured flash.",
    reward:"a path that remembers"
  },
  {
    id:164,
    name:"Beyond the Wandering Signal · 0164",
    region:"Ember Archive",
    signal:"a slow rhythm under the wind",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 3, and its trace number is 164.",
    clue:"Move once, pause once, then listen again. Fragment index: 164.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The path behind you quietly changes its shape.",
    reward:"an echo token"
  },
  {
    id:165,
    name:"Inside the Wandering Signal · 0165",
    region:"Echo Marsh",
    signal:"a breath behind the wall",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 4, and its trace number is 165.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 165.",
    lesson:"Silence is information when you learn to listen.",
    response:"The air grows still, waiting for another choice.",
    reward:"a stored reflection"
  },
  {
    id:166,
    name:"Under the Wandering Signal · 0166",
    region:"Last Horizon",
    signal:"a low blue pulse",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 5, and its trace number is 166.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 166.",
    lesson:"Returning is not the same as repeating.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a new depth"
  },
  {
    id:167,
    name:"Across the Wandering Signal · 0167",
    region:"Glasswater Basin",
    signal:"a ripple crossing dry ground",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 6, and its trace number is 167.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 167.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The echo returns with one extra note.",
    reward:"a quiet clue"
  },
  {
    id:168,
    name:"Behind the Wandering Signal · 0168",
    region:"Blue Divide",
    signal:"a pattern of footprints facing inward",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 7, and its trace number is 168.",
    clue:"A repeated step can open a door, but only once. Fragment index: 168.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The ground glows for a moment, then settles.",
    reward:"a memory fragment"
  },
  {
    id:169,
    name:"Within the Wandering Signal · 0169",
    region:"Ember Archive",
    signal:"a low blue pulse",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 1, and its trace number is 169.",
    clue:"The second path is real only after you turn away. Fragment index: 169.",
    lesson:"Silence is information when you learn to listen.",
    response:"A new mark appears beside your last footprint.",
    reward:"a map trace"
  },
  {
    id:170,
    name:"At the edge of the Wandering Signal · 0170",
    region:"Echo Marsh",
    signal:"a ripple crossing dry ground",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 2, and its trace number is 170.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 170.",
    lesson:"Returning is not the same as repeating.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a sealed memory"
  },
  {
    id:171,
    name:"Where the Wandering Signal · 0171",
    region:"Mirror Waste",
    signal:"a pattern of footprints facing inward",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 3, and its trace number is 171.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 171.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a clearer signal"
  },
  {
    id:172,
    name:"Before the Wandering Signal · 0172",
    region:"Quiet Reach",
    signal:"a glow hidden inside a crack",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 4, and its trace number is 172.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 172.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a changed landmark"
  },
  {
    id:173,
    name:"After the Wandering Signal · 0173",
    region:"Moss Quarter",
    signal:"a door-shaped gap in the air",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 5, and its trace number is 173.",
    clue:"Find the only light that does not pulse. Fragment index: 173.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The horizon brightens where your route bends.",
    reward:"a hidden passage"
  },
  {
    id:174,
    name:"Between the Wandering Signal · 0174",
    region:"Hollow Canopy",
    signal:"a thin thread of silver light",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 6, and its trace number is 174.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 174.",
    lesson:"Observation can be a form of movement.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a second chance"
  },
  {
    id:175,
    name:"Above the Wandering Signal · 0175",
    region:"Lantern Expanse",
    signal:"a reflection that arrives late",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 7, and its trace number is 175.",
    clue:"The safest route is not always the shortest. Fragment index: 175.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A distant light answers with one measured flash.",
    reward:"a memory fragment"
  },
  {
    id:176,
    name:"Below the Wandering Signal · 0176",
    region:"Pale Engine",
    signal:"a door-shaped gap in the air",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 1, and its trace number is 176.",
    clue:"Your previous route is the map for this one. Fragment index: 176.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The path behind you quietly changes its shape.",
    reward:"a map trace"
  },
  {
    id:177,
    name:"The Quiet Machine · 0177",
    region:"Quiet Reach",
    signal:"a thin thread of silver light",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 2, and its trace number is 177.",
    clue:"Move once, pause once, then listen again. Fragment index: 177.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The air grows still, waiting for another choice.",
    reward:"a sealed memory"
  },
  {
    id:178,
    name:"A Quiet Machine · 0178",
    region:"Moss Quarter",
    signal:"a reflection that arrives late",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 3, and its trace number is 178.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 178.",
    lesson:"Observation can be a form of movement.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a clearer signal"
  },
  {
    id:179,
    name:"Beneath the Quiet Machine · 0179",
    region:"Hollow Canopy",
    signal:"a shadow moving against the light",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 4, and its trace number is 179.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 179.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The echo returns with one extra note.",
    reward:"a changed landmark"
  },
  {
    id:180,
    name:"Beyond the Quiet Machine · 0180",
    region:"Lantern Expanse",
    signal:"a distant bell with no echo",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 5, and its trace number is 180.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 180.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The ground glows for a moment, then settles.",
    reward:"a hidden passage"
  },
  {
    id:181,
    name:"Inside the Quiet Machine · 0181",
    region:"Pale Engine",
    signal:"a hum that follows silence",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 6, and its trace number is 181.",
    clue:"A repeated step can open a door, but only once. Fragment index: 181.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A new mark appears beside your last footprint.",
    reward:"a second chance"
  },
  {
    id:182,
    name:"Under the Quiet Machine · 0182",
    region:"Frostline",
    signal:"a warm line beneath the stone",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 7, and its trace number is 182.",
    clue:"The second path is real only after you turn away. Fragment index: 182.",
    lesson:"Observation can be a form of movement.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a path that remembers"
  },
  {
    id:183,
    name:"Across the Quiet Machine · 0183",
    region:"Last Horizon",
    signal:"a distant bell with no echo",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 1, and its trace number is 183.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 183.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"an echo token"
  },
  {
    id:184,
    name:"Behind the Quiet Machine · 0184",
    region:"Glasswater Basin",
    signal:"a hum that follows silence",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 2, and its trace number is 184.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 184.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a stored reflection"
  },
  {
    id:185,
    name:"Within the Quiet Machine · 0185",
    region:"Blue Divide",
    signal:"a warm line beneath the stone",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 3, and its trace number is 185.",
    clue:"Return to the place where the floor changes colour. Fragment index: 185.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a new depth"
  },
  {
    id:186,
    name:"At the edge of the Quiet Machine · 0186",
    region:"Ember Archive",
    signal:"a pale mark that shifts position",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 4, and its trace number is 186.",
    clue:"The answer is stored in the order of your choices. Fragment index: 186.",
    lesson:"Observation can be a form of movement.",
    response:"A distant light answers with one measured flash.",
    reward:"a quiet clue"
  },
  {
    id:187,
    name:"Where the Quiet Machine · 0187",
    region:"Echo Marsh",
    signal:"a small star below the horizon",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 5, and its trace number is 187.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 187.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The path behind you quietly changes its shape.",
    reward:"a memory fragment"
  },
  {
    id:188,
    name:"Before the Quiet Machine · 0188",
    region:"Last Horizon",
    signal:"three notes with no source",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 6, and its trace number is 188.",
    clue:"The safest route is not always the shortest. Fragment index: 188.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The air grows still, waiting for another choice.",
    reward:"a map trace"
  },
  {
    id:189,
    name:"After the Quiet Machine · 0189",
    region:"Glasswater Basin",
    signal:"a slow rhythm under the wind",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 7, and its trace number is 189.",
    clue:"Your previous route is the map for this one. Fragment index: 189.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a sealed memory"
  },
  {
    id:190,
    name:"Between the Quiet Machine · 0190",
    region:"Blue Divide",
    signal:"a small star below the horizon",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 1, and its trace number is 190.",
    clue:"Move once, pause once, then listen again. Fragment index: 190.",
    lesson:"Observation can be a form of movement.",
    response:"The echo returns with one extra note.",
    reward:"a clearer signal"
  },
  {
    id:191,
    name:"Above the Quiet Machine · 0191",
    region:"Ember Archive",
    signal:"three notes with no source",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 2, and its trace number is 191.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 191.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The ground glows for a moment, then settles.",
    reward:"a changed landmark"
  },
  {
    id:192,
    name:"Below the Quiet Machine · 0192",
    region:"Echo Marsh",
    signal:"a slow rhythm under the wind",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 3, and its trace number is 192.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 192.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A new mark appears beside your last footprint.",
    reward:"a hidden passage"
  },
  {
    id:193,
    name:"The Silver Ravine · 0193",
    region:"Mirror Waste",
    signal:"a breath behind the wall",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 4, and its trace number is 193.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 193.",
    lesson:"Memory is more than a record of where you went.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a second chance"
  },
  {
    id:194,
    name:"A Silver Ravine · 0194",
    region:"Quiet Reach",
    signal:"a low blue pulse",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 5, and its trace number is 194.",
    clue:"A repeated step can open a door, but only once. Fragment index: 194.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a path that remembers"
  },
  {
    id:195,
    name:"Beneath the Silver Ravine · 0195",
    region:"Moss Quarter",
    signal:"a ripple crossing dry ground",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 6, and its trace number is 195.",
    clue:"The second path is real only after you turn away. Fragment index: 195.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"an echo token"
  },
  {
    id:196,
    name:"Beyond the Silver Ravine · 0196",
    region:"Hollow Canopy",
    signal:"a pattern of footprints facing inward",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 7, and its trace number is 196.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 196.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The horizon brightens where your route bends.",
    reward:"a stored reflection"
  },
  {
    id:197,
    name:"Inside the Silver Ravine · 0197",
    region:"Lantern Expanse",
    signal:"a low blue pulse",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 1, and its trace number is 197.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 197.",
    lesson:"Memory is more than a record of where you went.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a new depth"
  },
  {
    id:198,
    name:"Under the Silver Ravine · 0198",
    region:"Pale Engine",
    signal:"a ripple crossing dry ground",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 2, and its trace number is 198.",
    clue:"Return to the place where the floor changes colour. Fragment index: 198.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A distant light answers with one measured flash.",
    reward:"a quiet clue"
  },
  {
    id:199,
    name:"Across the Silver Ravine · 0199",
    region:"Quiet Reach",
    signal:"a pattern of footprints facing inward",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 3, and its trace number is 199.",
    clue:"The answer is stored in the order of your choices. Fragment index: 199.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The path behind you quietly changes its shape.",
    reward:"a memory fragment"
  },
  {
    id:200,
    name:"Behind the Silver Ravine · 0200",
    region:"Moss Quarter",
    signal:"a glow hidden inside a crack",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 4, and its trace number is 200.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 200.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The air grows still, waiting for another choice.",
    reward:"a map trace"
  },
  {
    id:201,
    name:"Within the Silver Ravine · 0201",
    region:"Hollow Canopy",
    signal:"a door-shaped gap in the air",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 5, and its trace number is 201.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 201.",
    lesson:"Memory is more than a record of where you went.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a sealed memory"
  },
  {
    id:202,
    name:"At the edge of the Silver Ravine · 0202",
    region:"Lantern Expanse",
    signal:"a thin thread of silver light",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 6, and its trace number is 202.",
    clue:"Find the only light that does not pulse. Fragment index: 202.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The echo returns with one extra note.",
    reward:"a clearer signal"
  },
  {
    id:203,
    name:"Where the Silver Ravine · 0203",
    region:"Pale Engine",
    signal:"a reflection that arrives late",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 7, and its trace number is 203.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 203.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The ground glows for a moment, then settles.",
    reward:"a changed landmark"
  },
  {
    id:204,
    name:"Before the Silver Ravine · 0204",
    region:"Frostline",
    signal:"a door-shaped gap in the air",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 1, and its trace number is 204.",
    clue:"The safest route is not always the shortest. Fragment index: 204.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A new mark appears beside your last footprint.",
    reward:"a new depth"
  },
  {
    id:205,
    name:"After the Silver Ravine · 0205",
    region:"Last Horizon",
    signal:"a thin thread of silver light",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 2, and its trace number is 205.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 205.",
    lesson:"Memory is more than a record of where you went.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a quiet clue"
  },
  {
    id:206,
    name:"Between the Silver Ravine · 0206",
    region:"Glasswater Basin",
    signal:"a reflection that arrives late",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 3, and its trace number is 206.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 206.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a memory fragment"
  },
  {
    id:207,
    name:"Above the Silver Ravine · 0207",
    region:"Blue Divide",
    signal:"a shadow moving against the light",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 4, and its trace number is 207.",
    clue:"A repeated step can open a door, but only once. Fragment index: 207.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a map trace"
  },
  {
    id:208,
    name:"Below the Silver Ravine · 0208",
    region:"Ember Archive",
    signal:"a distant bell with no echo",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 5, and its trace number is 208.",
    clue:"The second path is real only after you turn away. Fragment index: 208.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a sealed memory"
  },
  {
    id:209,
    name:"The Last Lighthouse · 0209",
    region:"Echo Marsh",
    signal:"a hum that follows silence",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 6, and its trace number is 209.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 209.",
    lesson:"Memory is more than a record of where you went.",
    response:"A distant light answers with one measured flash.",
    reward:"a clearer signal"
  },
  {
    id:210,
    name:"A Last Lighthouse · 0210",
    region:"Last Horizon",
    signal:"a warm line beneath the stone",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 7, and its trace number is 210.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 210.",
    lesson:"Silence is information when you learn to listen.",
    response:"The path behind you quietly changes its shape.",
    reward:"a changed landmark"
  },
  {
    id:211,
    name:"Beneath the Last Lighthouse · 0211",
    region:"Glasswater Basin",
    signal:"a distant bell with no echo",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 1, and its trace number is 211.",
    clue:"Return to the place where the floor changes colour. Fragment index: 211.",
    lesson:"Returning is not the same as repeating.",
    response:"The air grows still, waiting for another choice.",
    reward:"a hidden passage"
  },
  {
    id:212,
    name:"Beyond the Last Lighthouse · 0212",
    region:"Blue Divide",
    signal:"a hum that follows silence",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 2, and its trace number is 212.",
    clue:"The answer is stored in the order of your choices. Fragment index: 212.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a second chance"
  },
  {
    id:213,
    name:"Inside the Last Lighthouse · 0213",
    region:"Ember Archive",
    signal:"a warm line beneath the stone",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 3, and its trace number is 213.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 213.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The echo returns with one extra note.",
    reward:"a path that remembers"
  },
  {
    id:214,
    name:"Under the Last Lighthouse · 0214",
    region:"Echo Marsh",
    signal:"a pale mark that shifts position",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 4, and its trace number is 214.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 214.",
    lesson:"Silence is information when you learn to listen.",
    response:"The ground glows for a moment, then settles.",
    reward:"an echo token"
  },
  {
    id:215,
    name:"Across the Last Lighthouse · 0215",
    region:"Mirror Waste",
    signal:"a small star below the horizon",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 5, and its trace number is 215.",
    clue:"Find the only light that does not pulse. Fragment index: 215.",
    lesson:"Returning is not the same as repeating.",
    response:"A new mark appears beside your last footprint.",
    reward:"a stored reflection"
  },
  {
    id:216,
    name:"Behind the Last Lighthouse · 0216",
    region:"Quiet Reach",
    signal:"three notes with no source",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 6, and its trace number is 216.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 216.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a new depth"
  },
  {
    id:217,
    name:"Within the Last Lighthouse · 0217",
    region:"Moss Quarter",
    signal:"a slow rhythm under the wind",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 7, and its trace number is 217.",
    clue:"The safest route is not always the shortest. Fragment index: 217.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a quiet clue"
  },
  {
    id:218,
    name:"At the edge of the Last Lighthouse · 0218",
    region:"Hollow Canopy",
    signal:"a small star below the horizon",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 1, and its trace number is 218.",
    clue:"Your previous route is the map for this one. Fragment index: 218.",
    lesson:"Silence is information when you learn to listen.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a memory fragment"
  },
  {
    id:219,
    name:"Where the Last Lighthouse · 0219",
    region:"Lantern Expanse",
    signal:"three notes with no source",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 2, and its trace number is 219.",
    clue:"Move once, pause once, then listen again. Fragment index: 219.",
    lesson:"Returning is not the same as repeating.",
    response:"The horizon brightens where your route bends.",
    reward:"a map trace"
  },
  {
    id:220,
    name:"Before the Last Lighthouse · 0220",
    region:"Pale Engine",
    signal:"a slow rhythm under the wind",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 3, and its trace number is 220.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 220.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a sealed memory"
  },
  {
    id:221,
    name:"After the Last Lighthouse · 0221",
    region:"Quiet Reach",
    signal:"a breath behind the wall",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 4, and its trace number is 221.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 221.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A distant light answers with one measured flash.",
    reward:"a clearer signal"
  },
  {
    id:222,
    name:"Between the Last Lighthouse · 0222",
    region:"Moss Quarter",
    signal:"a low blue pulse",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 5, and its trace number is 222.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 222.",
    lesson:"Silence is information when you learn to listen.",
    response:"The path behind you quietly changes its shape.",
    reward:"a changed landmark"
  },
  {
    id:223,
    name:"Above the Last Lighthouse · 0223",
    region:"Hollow Canopy",
    signal:"a ripple crossing dry ground",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 6, and its trace number is 223.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 223.",
    lesson:"Returning is not the same as repeating.",
    response:"The air grows still, waiting for another choice.",
    reward:"a hidden passage"
  },
  {
    id:224,
    name:"Below the Last Lighthouse · 0224",
    region:"Lantern Expanse",
    signal:"a pattern of footprints facing inward",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 7, and its trace number is 224.",
    clue:"Return to the place where the floor changes colour. Fragment index: 224.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a second chance"
  },
  {
    id:225,
    name:"The Paper Moon · 0225",
    region:"Pale Engine",
    signal:"a low blue pulse",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 1, and its trace number is 225.",
    clue:"The answer is stored in the order of your choices. Fragment index: 225.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The echo returns with one extra note.",
    reward:"a path that remembers"
  },
  {
    id:226,
    name:"A Paper Moon · 0226",
    region:"Frostline",
    signal:"a ripple crossing dry ground",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 2, and its trace number is 226.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 226.",
    lesson:"Silence is information when you learn to listen.",
    response:"The ground glows for a moment, then settles.",
    reward:"an echo token"
  },
  {
    id:227,
    name:"Beneath the Paper Moon · 0227",
    region:"Last Horizon",
    signal:"a pattern of footprints facing inward",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 3, and its trace number is 227.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 227.",
    lesson:"Returning is not the same as repeating.",
    response:"A new mark appears beside your last footprint.",
    reward:"a stored reflection"
  },
  {
    id:228,
    name:"Beyond the Paper Moon · 0228",
    region:"Glasswater Basin",
    signal:"a glow hidden inside a crack",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 4, and its trace number is 228.",
    clue:"Find the only light that does not pulse. Fragment index: 228.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a new depth"
  },
  {
    id:229,
    name:"Inside the Paper Moon · 0229",
    region:"Blue Divide",
    signal:"a door-shaped gap in the air",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 5, and its trace number is 229.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 229.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a quiet clue"
  },
  {
    id:230,
    name:"Under the Paper Moon · 0230",
    region:"Ember Archive",
    signal:"a thin thread of silver light",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 6, and its trace number is 230.",
    clue:"The safest route is not always the shortest. Fragment index: 230.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a memory fragment"
  },
  {
    id:231,
    name:"Across the Paper Moon · 0231",
    region:"Echo Marsh",
    signal:"a reflection that arrives late",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 7, and its trace number is 231.",
    clue:"Your previous route is the map for this one. Fragment index: 231.",
    lesson:"Observation can be a form of movement.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a map trace"
  },
  {
    id:232,
    name:"Behind the Paper Moon · 0232",
    region:"Last Horizon",
    signal:"a door-shaped gap in the air",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 1, and its trace number is 232.",
    clue:"Move once, pause once, then listen again. Fragment index: 232.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A distant light answers with one measured flash.",
    reward:"a sealed memory"
  },
  {
    id:233,
    name:"Within the Paper Moon · 0233",
    region:"Glasswater Basin",
    signal:"a thin thread of silver light",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 2, and its trace number is 233.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 233.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The path behind you quietly changes its shape.",
    reward:"an echo token"
  },
  {
    id:234,
    name:"At the edge of the Paper Moon · 0234",
    region:"Blue Divide",
    signal:"a reflection that arrives late",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 3, and its trace number is 234.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 234.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The air grows still, waiting for another choice.",
    reward:"a stored reflection"
  },
  {
    id:235,
    name:"Where the Paper Moon · 0235",
    region:"Ember Archive",
    signal:"a shadow moving against the light",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 4, and its trace number is 235.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 235.",
    lesson:"Observation can be a form of movement.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a new depth"
  },
  {
    id:236,
    name:"Before the Paper Moon · 0236",
    region:"Echo Marsh",
    signal:"a distant bell with no echo",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 5, and its trace number is 236.",
    clue:"A repeated step can open a door, but only once. Fragment index: 236.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The echo returns with one extra note.",
    reward:"a quiet clue"
  },
  {
    id:237,
    name:"After the Paper Moon · 0237",
    region:"Mirror Waste",
    signal:"a hum that follows silence",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 6, and its trace number is 237.",
    clue:"The second path is real only after you turn away. Fragment index: 237.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The ground glows for a moment, then settles.",
    reward:"a memory fragment"
  },
  {
    id:238,
    name:"Between the Paper Moon · 0238",
    region:"Quiet Reach",
    signal:"a warm line beneath the stone",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 7, and its trace number is 238.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 238.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A new mark appears beside your last footprint.",
    reward:"a map trace"
  },
  {
    id:239,
    name:"Above the Paper Moon · 0239",
    region:"Moss Quarter",
    signal:"a distant bell with no echo",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 1, and its trace number is 239.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 239.",
    lesson:"Observation can be a form of movement.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a sealed memory"
  },
  {
    id:240,
    name:"Below the Paper Moon · 0240",
    region:"Hollow Canopy",
    signal:"a hum that follows silence",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 2, and its trace number is 240.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 240.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a clearer signal"
  },
  {
    id:241,
    name:"The Frozen River · 0241",
    region:"Lantern Expanse",
    signal:"a warm line beneath the stone",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 3, and its trace number is 241.",
    clue:"Find the only light that does not pulse. Fragment index: 241.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a changed landmark"
  },
  {
    id:242,
    name:"A Frozen River · 0242",
    region:"Pale Engine",
    signal:"a pale mark that shifts position",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 4, and its trace number is 242.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 242.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The horizon brightens where your route bends.",
    reward:"a hidden passage"
  },
  {
    id:243,
    name:"Beneath the Frozen River · 0243",
    region:"Quiet Reach",
    signal:"a small star below the horizon",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 5, and its trace number is 243.",
    clue:"The safest route is not always the shortest. Fragment index: 243.",
    lesson:"Observation can be a form of movement.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a second chance"
  },
  {
    id:244,
    name:"Beyond the Frozen River · 0244",
    region:"Moss Quarter",
    signal:"three notes with no source",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 6, and its trace number is 244.",
    clue:"Your previous route is the map for this one. Fragment index: 244.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A distant light answers with one measured flash.",
    reward:"a path that remembers"
  },
  {
    id:245,
    name:"Inside the Frozen River · 0245",
    region:"Hollow Canopy",
    signal:"a slow rhythm under the wind",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 7, and its trace number is 245.",
    clue:"Move once, pause once, then listen again. Fragment index: 245.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The path behind you quietly changes its shape.",
    reward:"an echo token"
  },
  {
    id:246,
    name:"Under the Frozen River · 0246",
    region:"Lantern Expanse",
    signal:"a small star below the horizon",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 1, and its trace number is 246.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 246.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The air grows still, waiting for another choice.",
    reward:"a stored reflection"
  },
  {
    id:247,
    name:"Across the Frozen River · 0247",
    region:"Pale Engine",
    signal:"three notes with no source",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 2, and its trace number is 247.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 247.",
    lesson:"Observation can be a form of movement.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a new depth"
  },
  {
    id:248,
    name:"Behind the Frozen River · 0248",
    region:"Frostline",
    signal:"a slow rhythm under the wind",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 3, and its trace number is 248.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 248.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The echo returns with one extra note.",
    reward:"a quiet clue"
  },
  {
    id:249,
    name:"Within the Frozen River · 0249",
    region:"Last Horizon",
    signal:"a breath behind the wall",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 4, and its trace number is 249.",
    clue:"A repeated step can open a door, but only once. Fragment index: 249.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The ground glows for a moment, then settles.",
    reward:"a memory fragment"
  },
  {
    id:250,
    name:"At the edge of the Frozen River · 0250",
    region:"Glasswater Basin",
    signal:"a low blue pulse",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 5, and its trace number is 250.",
    clue:"The second path is real only after you turn away. Fragment index: 250.",
    lesson:"Memory is more than a record of where you went.",
    response:"A new mark appears beside your last footprint.",
    reward:"a map trace"
  },
  {
    id:251,
    name:"Where the Frozen River · 0251",
    region:"Blue Divide",
    signal:"a ripple crossing dry ground",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 6, and its trace number is 251.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 251.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a sealed memory"
  },
  {
    id:252,
    name:"Before the Frozen River · 0252",
    region:"Ember Archive",
    signal:"a pattern of footprints facing inward",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 7, and its trace number is 252.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 252.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a clearer signal"
  },
  {
    id:253,
    name:"After the Frozen River · 0253",
    region:"Echo Marsh",
    signal:"a low blue pulse",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 1, and its trace number is 253.",
    clue:"Return to the place where the floor changes colour. Fragment index: 253.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a changed landmark"
  },
  {
    id:254,
    name:"Between the Frozen River · 0254",
    region:"Last Horizon",
    signal:"a ripple crossing dry ground",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 2, and its trace number is 254.",
    clue:"The answer is stored in the order of your choices. Fragment index: 254.",
    lesson:"Memory is more than a record of where you went.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a hidden passage"
  },
  {
    id:255,
    name:"Above the Frozen River · 0255",
    region:"Glasswater Basin",
    signal:"a pattern of footprints facing inward",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 3, and its trace number is 255.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 255.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A distant light answers with one measured flash.",
    reward:"a second chance"
  },
  {
    id:256,
    name:"Below the Frozen River · 0256",
    region:"Blue Divide",
    signal:"a glow hidden inside a crack",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 4, and its trace number is 256.",
    clue:"The safest route is not always the shortest. Fragment index: 256.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The path behind you quietly changes its shape.",
    reward:"a path that remembers"
  },
  {
    id:257,
    name:"The Lantern Maze · 0257",
    region:"Ember Archive",
    signal:"a door-shaped gap in the air",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 5, and its trace number is 257.",
    clue:"Your previous route is the map for this one. Fragment index: 257.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The air grows still, waiting for another choice.",
    reward:"an echo token"
  },
  {
    id:258,
    name:"A Lantern Maze · 0258",
    region:"Echo Marsh",
    signal:"a thin thread of silver light",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 6, and its trace number is 258.",
    clue:"Move once, pause once, then listen again. Fragment index: 258.",
    lesson:"Memory is more than a record of where you went.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a stored reflection"
  },
  {
    id:259,
    name:"Beneath the Lantern Maze · 0259",
    region:"Mirror Waste",
    signal:"a reflection that arrives late",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 7, and its trace number is 259.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 259.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The echo returns with one extra note.",
    reward:"a new depth"
  },
  {
    id:260,
    name:"Beyond the Lantern Maze · 0260",
    region:"Quiet Reach",
    signal:"a door-shaped gap in the air",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 1, and its trace number is 260.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 260.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The ground glows for a moment, then settles.",
    reward:"a quiet clue"
  },
  {
    id:261,
    name:"Inside the Lantern Maze · 0261",
    region:"Moss Quarter",
    signal:"a thin thread of silver light",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 2, and its trace number is 261.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 261.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A new mark appears beside your last footprint.",
    reward:"a memory fragment"
  },
  {
    id:262,
    name:"Under the Lantern Maze · 0262",
    region:"Hollow Canopy",
    signal:"a reflection that arrives late",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 3, and its trace number is 262.",
    clue:"A repeated step can open a door, but only once. Fragment index: 262.",
    lesson:"Memory is more than a record of where you went.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a second chance"
  },
  {
    id:263,
    name:"Across the Lantern Maze · 0263",
    region:"Lantern Expanse",
    signal:"a shadow moving against the light",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 4, and its trace number is 263.",
    clue:"The second path is real only after you turn away. Fragment index: 263.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a path that remembers"
  },
  {
    id:264,
    name:"Behind the Lantern Maze · 0264",
    region:"Pale Engine",
    signal:"a distant bell with no echo",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 5, and its trace number is 264.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 264.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"an echo token"
  },
  {
    id:265,
    name:"Within the Lantern Maze · 0265",
    region:"Quiet Reach",
    signal:"a hum that follows silence",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 6, and its trace number is 265.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 265.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The horizon brightens where your route bends.",
    reward:"a stored reflection"
  },
  {
    id:266,
    name:"At the edge of the Lantern Maze · 0266",
    region:"Moss Quarter",
    signal:"a warm line beneath the stone",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 7, and its trace number is 266.",
    clue:"Return to the place where the floor changes colour. Fragment index: 266.",
    lesson:"Memory is more than a record of where you went.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a new depth"
  },
  {
    id:267,
    name:"Where the Lantern Maze · 0267",
    region:"Hollow Canopy",
    signal:"a distant bell with no echo",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 1, and its trace number is 267.",
    clue:"The answer is stored in the order of your choices. Fragment index: 267.",
    lesson:"Silence is information when you learn to listen.",
    response:"A distant light answers with one measured flash.",
    reward:"a quiet clue"
  },
  {
    id:268,
    name:"Before the Lantern Maze · 0268",
    region:"Lantern Expanse",
    signal:"a hum that follows silence",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 2, and its trace number is 268.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 268.",
    lesson:"Returning is not the same as repeating.",
    response:"The path behind you quietly changes its shape.",
    reward:"a memory fragment"
  },
  {
    id:269,
    name:"After the Lantern Maze · 0269",
    region:"Pale Engine",
    signal:"a warm line beneath the stone",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 3, and its trace number is 269.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 269.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The air grows still, waiting for another choice.",
    reward:"a map trace"
  },
  {
    id:270,
    name:"Between the Lantern Maze · 0270",
    region:"Frostline",
    signal:"a pale mark that shifts position",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 4, and its trace number is 270.",
    clue:"Find the only light that does not pulse. Fragment index: 270.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a sealed memory"
  },
  {
    id:271,
    name:"Above the Lantern Maze · 0271",
    region:"Last Horizon",
    signal:"a small star below the horizon",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 5, and its trace number is 271.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 271.",
    lesson:"Silence is information when you learn to listen.",
    response:"The echo returns with one extra note.",
    reward:"a clearer signal"
  },
  {
    id:272,
    name:"Below the Lantern Maze · 0272",
    region:"Glasswater Basin",
    signal:"three notes with no source",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 6, and its trace number is 272.",
    clue:"The safest route is not always the shortest. Fragment index: 272.",
    lesson:"Returning is not the same as repeating.",
    response:"The ground glows for a moment, then settles.",
    reward:"a changed landmark"
  },
  {
    id:273,
    name:"The Echo Chamber · 0273",
    region:"Blue Divide",
    signal:"a slow rhythm under the wind",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 7, and its trace number is 273.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 273.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A new mark appears beside your last footprint.",
    reward:"a hidden passage"
  },
  {
    id:274,
    name:"A Echo Chamber · 0274",
    region:"Ember Archive",
    signal:"a small star below the horizon",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 1, and its trace number is 274.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 274.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a second chance"
  },
  {
    id:275,
    name:"Beneath the Echo Chamber · 0275",
    region:"Echo Marsh",
    signal:"three notes with no source",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 2, and its trace number is 275.",
    clue:"A repeated step can open a door, but only once. Fragment index: 275.",
    lesson:"Silence is information when you learn to listen.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a path that remembers"
  },
  {
    id:276,
    name:"Beyond the Echo Chamber · 0276",
    region:"Last Horizon",
    signal:"a slow rhythm under the wind",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 3, and its trace number is 276.",
    clue:"The second path is real only after you turn away. Fragment index: 276.",
    lesson:"Returning is not the same as repeating.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"an echo token"
  },
  {
    id:277,
    name:"Inside the Echo Chamber · 0277",
    region:"Glasswater Basin",
    signal:"a breath behind the wall",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 4, and its trace number is 277.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 277.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a stored reflection"
  },
  {
    id:278,
    name:"Under the Echo Chamber · 0278",
    region:"Blue Divide",
    signal:"a low blue pulse",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 5, and its trace number is 278.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 278.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A distant light answers with one measured flash.",
    reward:"a new depth"
  },
  {
    id:279,
    name:"Across the Echo Chamber · 0279",
    region:"Ember Archive",
    signal:"a ripple crossing dry ground",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 6, and its trace number is 279.",
    clue:"Return to the place where the floor changes colour. Fragment index: 279.",
    lesson:"Silence is information when you learn to listen.",
    response:"The path behind you quietly changes its shape.",
    reward:"a quiet clue"
  },
  {
    id:280,
    name:"Behind the Echo Chamber · 0280",
    region:"Echo Marsh",
    signal:"a pattern of footprints facing inward",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 7, and its trace number is 280.",
    clue:"The answer is stored in the order of your choices. Fragment index: 280.",
    lesson:"Returning is not the same as repeating.",
    response:"The air grows still, waiting for another choice.",
    reward:"a memory fragment"
  },
  {
    id:281,
    name:"Within the Echo Chamber · 0281",
    region:"Mirror Waste",
    signal:"a low blue pulse",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 1, and its trace number is 281.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 281.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a map trace"
  },
  {
    id:282,
    name:"At the edge of the Echo Chamber · 0282",
    region:"Quiet Reach",
    signal:"a ripple crossing dry ground",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 2, and its trace number is 282.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 282.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The echo returns with one extra note.",
    reward:"a sealed memory"
  },
  {
    id:283,
    name:"Where the Echo Chamber · 0283",
    region:"Moss Quarter",
    signal:"a pattern of footprints facing inward",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 3, and its trace number is 283.",
    clue:"Find the only light that does not pulse. Fragment index: 283.",
    lesson:"Silence is information when you learn to listen.",
    response:"The ground glows for a moment, then settles.",
    reward:"a clearer signal"
  },
  {
    id:284,
    name:"Before the Echo Chamber · 0284",
    region:"Hollow Canopy",
    signal:"a glow hidden inside a crack",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 4, and its trace number is 284.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 284.",
    lesson:"Returning is not the same as repeating.",
    response:"A new mark appears beside your last footprint.",
    reward:"a changed landmark"
  },
  {
    id:285,
    name:"After the Echo Chamber · 0285",
    region:"Lantern Expanse",
    signal:"a door-shaped gap in the air",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 5, and its trace number is 285.",
    clue:"The safest route is not always the shortest. Fragment index: 285.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a hidden passage"
  },
  {
    id:286,
    name:"Between the Echo Chamber · 0286",
    region:"Pale Engine",
    signal:"a thin thread of silver light",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 6, and its trace number is 286.",
    clue:"Your previous route is the map for this one. Fragment index: 286.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a second chance"
  },
  {
    id:287,
    name:"Above the Echo Chamber · 0287",
    region:"Quiet Reach",
    signal:"a reflection that arrives late",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 7, and its trace number is 287.",
    clue:"Move once, pause once, then listen again. Fragment index: 287.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a path that remembers"
  },
  {
    id:288,
    name:"Below the Echo Chamber · 0288",
    region:"Moss Quarter",
    signal:"a door-shaped gap in the air",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 1, and its trace number is 288.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 288.",
    lesson:"Observation can be a form of movement.",
    response:"The horizon brightens where your route bends.",
    reward:"an echo token"
  },
  {
    id:289,
    name:"The Broken Compass · 0289",
    region:"Hollow Canopy",
    signal:"a thin thread of silver light",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 2, and its trace number is 289.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 289.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a stored reflection"
  },
  {
    id:290,
    name:"A Broken Compass · 0290",
    region:"Lantern Expanse",
    signal:"a reflection that arrives late",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 3, and its trace number is 290.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 290.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A distant light answers with one measured flash.",
    reward:"a new depth"
  },
  {
    id:291,
    name:"Beneath the Broken Compass · 0291",
    region:"Pale Engine",
    signal:"a shadow moving against the light",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 4, and its trace number is 291.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 291.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The path behind you quietly changes its shape.",
    reward:"a changed landmark"
  },
  {
    id:292,
    name:"Beyond the Broken Compass · 0292",
    region:"Frostline",
    signal:"a distant bell with no echo",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 5, and its trace number is 292.",
    clue:"Return to the place where the floor changes colour. Fragment index: 292.",
    lesson:"Observation can be a form of movement.",
    response:"The air grows still, waiting for another choice.",
    reward:"a hidden passage"
  },
  {
    id:293,
    name:"Inside the Broken Compass · 0293",
    region:"Last Horizon",
    signal:"a hum that follows silence",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 6, and its trace number is 293.",
    clue:"The answer is stored in the order of your choices. Fragment index: 293.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a second chance"
  },
  {
    id:294,
    name:"Under the Broken Compass · 0294",
    region:"Glasswater Basin",
    signal:"a warm line beneath the stone",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 7, and its trace number is 294.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 294.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The echo returns with one extra note.",
    reward:"a path that remembers"
  },
  {
    id:295,
    name:"Across the Broken Compass · 0295",
    region:"Blue Divide",
    signal:"a distant bell with no echo",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 1, and its trace number is 295.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 295.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The ground glows for a moment, then settles.",
    reward:"an echo token"
  },
  {
    id:296,
    name:"Behind the Broken Compass · 0296",
    region:"Ember Archive",
    signal:"a hum that follows silence",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 2, and its trace number is 296.",
    clue:"Find the only light that does not pulse. Fragment index: 296.",
    lesson:"Observation can be a form of movement.",
    response:"A new mark appears beside your last footprint.",
    reward:"a stored reflection"
  },
  {
    id:297,
    name:"Within the Broken Compass · 0297",
    region:"Echo Marsh",
    signal:"a warm line beneath the stone",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 3, and its trace number is 297.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 297.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a new depth"
  },
  {
    id:298,
    name:"At the edge of the Broken Compass · 0298",
    region:"Last Horizon",
    signal:"a pale mark that shifts position",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 4, and its trace number is 298.",
    clue:"The safest route is not always the shortest. Fragment index: 298.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a quiet clue"
  },
  {
    id:299,
    name:"Where the Broken Compass · 0299",
    region:"Glasswater Basin",
    signal:"a small star below the horizon",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 5, and its trace number is 299.",
    clue:"Your previous route is the map for this one. Fragment index: 299.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a memory fragment"
  },
  {
    id:300,
    name:"Before the Broken Compass · 0300",
    region:"Blue Divide",
    signal:"three notes with no source",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 6, and its trace number is 300.",
    clue:"Move once, pause once, then listen again. Fragment index: 300.",
    lesson:"Observation can be a form of movement.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a map trace"
  },
  {
    id:301,
    name:"After the Broken Compass · 0301",
    region:"Ember Archive",
    signal:"a slow rhythm under the wind",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 7, and its trace number is 301.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 301.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A distant light answers with one measured flash.",
    reward:"a sealed memory"
  },
  {
    id:302,
    name:"Between the Broken Compass · 0302",
    region:"Echo Marsh",
    signal:"a small star below the horizon",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 1, and its trace number is 302.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 302.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The path behind you quietly changes its shape.",
    reward:"a clearer signal"
  },
  {
    id:303,
    name:"Above the Broken Compass · 0303",
    region:"Mirror Waste",
    signal:"three notes with no source",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 2, and its trace number is 303.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 303.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The air grows still, waiting for another choice.",
    reward:"a changed landmark"
  },
  {
    id:304,
    name:"Below the Broken Compass · 0304",
    region:"Quiet Reach",
    signal:"a slow rhythm under the wind",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 3, and its trace number is 304.",
    clue:"A repeated step can open a door, but only once. Fragment index: 304.",
    lesson:"Observation can be a form of movement.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a hidden passage"
  },
  {
    id:305,
    name:"The Hidden Shore · 0305",
    region:"Moss Quarter",
    signal:"a breath behind the wall",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 4, and its trace number is 305.",
    clue:"The second path is real only after you turn away. Fragment index: 305.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The echo returns with one extra note.",
    reward:"a second chance"
  },
  {
    id:306,
    name:"A Hidden Shore · 0306",
    region:"Hollow Canopy",
    signal:"a low blue pulse",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 5, and its trace number is 306.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 306.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The ground glows for a moment, then settles.",
    reward:"a path that remembers"
  },
  {
    id:307,
    name:"Beneath the Hidden Shore · 0307",
    region:"Lantern Expanse",
    signal:"a ripple crossing dry ground",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 6, and its trace number is 307.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 307.",
    lesson:"Memory is more than a record of where you went.",
    response:"A new mark appears beside your last footprint.",
    reward:"an echo token"
  },
  {
    id:308,
    name:"Beyond the Hidden Shore · 0308",
    region:"Pale Engine",
    signal:"a pattern of footprints facing inward",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 7, and its trace number is 308.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 308.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a stored reflection"
  },
  {
    id:309,
    name:"Inside the Hidden Shore · 0309",
    region:"Quiet Reach",
    signal:"a low blue pulse",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 1, and its trace number is 309.",
    clue:"Find the only light that does not pulse. Fragment index: 309.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a new depth"
  },
  {
    id:310,
    name:"Under the Hidden Shore · 0310",
    region:"Moss Quarter",
    signal:"a ripple crossing dry ground",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 2, and its trace number is 310.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 310.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a quiet clue"
  },
  {
    id:311,
    name:"Across the Hidden Shore · 0311",
    region:"Hollow Canopy",
    signal:"a pattern of footprints facing inward",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 3, and its trace number is 311.",
    clue:"The safest route is not always the shortest. Fragment index: 311.",
    lesson:"Memory is more than a record of where you went.",
    response:"The horizon brightens where your route bends.",
    reward:"a memory fragment"
  },
  {
    id:312,
    name:"Behind the Hidden Shore · 0312",
    region:"Lantern Expanse",
    signal:"a glow hidden inside a crack",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 4, and its trace number is 312.",
    clue:"Your previous route is the map for this one. Fragment index: 312.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a map trace"
  },
  {
    id:313,
    name:"Within the Hidden Shore · 0313",
    region:"Pale Engine",
    signal:"a door-shaped gap in the air",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 5, and its trace number is 313.",
    clue:"Move once, pause once, then listen again. Fragment index: 313.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A distant light answers with one measured flash.",
    reward:"a sealed memory"
  },
  {
    id:314,
    name:"At the edge of the Hidden Shore · 0314",
    region:"Frostline",
    signal:"a thin thread of silver light",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 6, and its trace number is 314.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 314.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The path behind you quietly changes its shape.",
    reward:"a clearer signal"
  },
  {
    id:315,
    name:"Where the Hidden Shore · 0315",
    region:"Last Horizon",
    signal:"a reflection that arrives late",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 7, and its trace number is 315.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 315.",
    lesson:"Memory is more than a record of where you went.",
    response:"The air grows still, waiting for another choice.",
    reward:"a changed landmark"
  },
  {
    id:316,
    name:"Before the Hidden Shore · 0316",
    region:"Glasswater Basin",
    signal:"a door-shaped gap in the air",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 1, and its trace number is 316.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 316.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a hidden passage"
  },
  {
    id:317,
    name:"After the Hidden Shore · 0317",
    region:"Blue Divide",
    signal:"a thin thread of silver light",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 2, and its trace number is 317.",
    clue:"A repeated step can open a door, but only once. Fragment index: 317.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The echo returns with one extra note.",
    reward:"a second chance"
  },
  {
    id:318,
    name:"Between the Hidden Shore · 0318",
    region:"Ember Archive",
    signal:"a reflection that arrives late",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 3, and its trace number is 318.",
    clue:"The second path is real only after you turn away. Fragment index: 318.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The ground glows for a moment, then settles.",
    reward:"a path that remembers"
  },
  {
    id:319,
    name:"Above the Hidden Shore · 0319",
    region:"Echo Marsh",
    signal:"a shadow moving against the light",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 4, and its trace number is 319.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 319.",
    lesson:"Memory is more than a record of where you went.",
    response:"A new mark appears beside your last footprint.",
    reward:"an echo token"
  },
  {
    id:320,
    name:"Below the Hidden Shore · 0320",
    region:"Last Horizon",
    signal:"a distant bell with no echo",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 5, and its trace number is 320.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 320.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a sealed memory"
  },
  {
    id:321,
    name:"The Velvet Storm · 0321",
    region:"Glasswater Basin",
    signal:"a hum that follows silence",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 6, and its trace number is 321.",
    clue:"Return to the place where the floor changes colour. Fragment index: 321.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a clearer signal"
  },
  {
    id:322,
    name:"A Velvet Storm · 0322",
    region:"Blue Divide",
    signal:"a warm line beneath the stone",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 7, and its trace number is 322.",
    clue:"The answer is stored in the order of your choices. Fragment index: 322.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a changed landmark"
  },
  {
    id:323,
    name:"Beneath the Velvet Storm · 0323",
    region:"Ember Archive",
    signal:"a distant bell with no echo",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 1, and its trace number is 323.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 323.",
    lesson:"Memory is more than a record of where you went.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a hidden passage"
  },
  {
    id:324,
    name:"Beyond the Velvet Storm · 0324",
    region:"Echo Marsh",
    signal:"a hum that follows silence",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 2, and its trace number is 324.",
    clue:"The safest route is not always the shortest. Fragment index: 324.",
    lesson:"Silence is information when you learn to listen.",
    response:"A distant light answers with one measured flash.",
    reward:"a second chance"
  },
  {
    id:325,
    name:"Inside the Velvet Storm · 0325",
    region:"Mirror Waste",
    signal:"a warm line beneath the stone",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 3, and its trace number is 325.",
    clue:"Your previous route is the map for this one. Fragment index: 325.",
    lesson:"Returning is not the same as repeating.",
    response:"The path behind you quietly changes its shape.",
    reward:"a path that remembers"
  },
  {
    id:326,
    name:"Under the Velvet Storm · 0326",
    region:"Quiet Reach",
    signal:"a pale mark that shifts position",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 4, and its trace number is 326.",
    clue:"Move once, pause once, then listen again. Fragment index: 326.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The air grows still, waiting for another choice.",
    reward:"an echo token"
  },
  {
    id:327,
    name:"Across the Velvet Storm · 0327",
    region:"Moss Quarter",
    signal:"a small star below the horizon",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 5, and its trace number is 327.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 327.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a stored reflection"
  },
  {
    id:328,
    name:"Behind the Velvet Storm · 0328",
    region:"Hollow Canopy",
    signal:"three notes with no source",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 6, and its trace number is 328.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 328.",
    lesson:"Silence is information when you learn to listen.",
    response:"The echo returns with one extra note.",
    reward:"a new depth"
  },
  {
    id:329,
    name:"Within the Velvet Storm · 0329",
    region:"Lantern Expanse",
    signal:"a slow rhythm under the wind",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 7, and its trace number is 329.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 329.",
    lesson:"Returning is not the same as repeating.",
    response:"The ground glows for a moment, then settles.",
    reward:"a quiet clue"
  },
  {
    id:330,
    name:"At the edge of the Velvet Storm · 0330",
    region:"Pale Engine",
    signal:"a small star below the horizon",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 1, and its trace number is 330.",
    clue:"A repeated step can open a door, but only once. Fragment index: 330.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A new mark appears beside your last footprint.",
    reward:"a memory fragment"
  },
  {
    id:331,
    name:"Where the Velvet Storm · 0331",
    region:"Quiet Reach",
    signal:"three notes with no source",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 2, and its trace number is 331.",
    clue:"The second path is real only after you turn away. Fragment index: 331.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a map trace"
  },
  {
    id:332,
    name:"Before the Velvet Storm · 0332",
    region:"Moss Quarter",
    signal:"a slow rhythm under the wind",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 3, and its trace number is 332.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 332.",
    lesson:"Silence is information when you learn to listen.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a sealed memory"
  },
  {
    id:333,
    name:"After the Velvet Storm · 0333",
    region:"Hollow Canopy",
    signal:"a breath behind the wall",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 4, and its trace number is 333.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 333.",
    lesson:"Returning is not the same as repeating.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a clearer signal"
  },
  {
    id:334,
    name:"Between the Velvet Storm · 0334",
    region:"Lantern Expanse",
    signal:"a low blue pulse",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 5, and its trace number is 334.",
    clue:"Return to the place where the floor changes colour. Fragment index: 334.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The horizon brightens where your route bends.",
    reward:"a changed landmark"
  },
  {
    id:335,
    name:"Above the Velvet Storm · 0335",
    region:"Pale Engine",
    signal:"a ripple crossing dry ground",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 6, and its trace number is 335.",
    clue:"The answer is stored in the order of your choices. Fragment index: 335.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a hidden passage"
  },
  {
    id:336,
    name:"Below the Velvet Storm · 0336",
    region:"Frostline",
    signal:"a pattern of footprints facing inward",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 7, and its trace number is 336.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 336.",
    lesson:"Silence is information when you learn to listen.",
    response:"A distant light answers with one measured flash.",
    reward:"a second chance"
  },
  {
    id:337,
    name:"The Clockwork Nest · 0337",
    region:"Last Horizon",
    signal:"a low blue pulse",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 1, and its trace number is 337.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 337.",
    lesson:"Returning is not the same as repeating.",
    response:"The path behind you quietly changes its shape.",
    reward:"a path that remembers"
  },
  {
    id:338,
    name:"A Clockwork Nest · 0338",
    region:"Glasswater Basin",
    signal:"a ripple crossing dry ground",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 2, and its trace number is 338.",
    clue:"Find the only light that does not pulse. Fragment index: 338.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The air grows still, waiting for another choice.",
    reward:"an echo token"
  },
  {
    id:339,
    name:"Beneath the Clockwork Nest · 0339",
    region:"Blue Divide",
    signal:"a pattern of footprints facing inward",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 3, and its trace number is 339.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 339.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a stored reflection"
  },
  {
    id:340,
    name:"Beyond the Clockwork Nest · 0340",
    region:"Ember Archive",
    signal:"a glow hidden inside a crack",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 4, and its trace number is 340.",
    clue:"The safest route is not always the shortest. Fragment index: 340.",
    lesson:"Silence is information when you learn to listen.",
    response:"The echo returns with one extra note.",
    reward:"a new depth"
  },
  {
    id:341,
    name:"Inside the Clockwork Nest · 0341",
    region:"Echo Marsh",
    signal:"a door-shaped gap in the air",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 5, and its trace number is 341.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 341.",
    lesson:"Returning is not the same as repeating.",
    response:"The ground glows for a moment, then settles.",
    reward:"a quiet clue"
  },
  {
    id:342,
    name:"Under the Clockwork Nest · 0342",
    region:"Last Horizon",
    signal:"a thin thread of silver light",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 6, and its trace number is 342.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 342.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A new mark appears beside your last footprint.",
    reward:"a memory fragment"
  },
  {
    id:343,
    name:"Across the Clockwork Nest · 0343",
    region:"Glasswater Basin",
    signal:"a reflection that arrives late",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 7, and its trace number is 343.",
    clue:"A repeated step can open a door, but only once. Fragment index: 343.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a map trace"
  },
  {
    id:344,
    name:"Behind the Clockwork Nest · 0344",
    region:"Blue Divide",
    signal:"a door-shaped gap in the air",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 1, and its trace number is 344.",
    clue:"The second path is real only after you turn away. Fragment index: 344.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a sealed memory"
  },
  {
    id:345,
    name:"Within the Clockwork Nest · 0345",
    region:"Ember Archive",
    signal:"a thin thread of silver light",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 2, and its trace number is 345.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 345.",
    lesson:"Observation can be a form of movement.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a clearer signal"
  },
  {
    id:346,
    name:"At the edge of the Clockwork Nest · 0346",
    region:"Echo Marsh",
    signal:"a reflection that arrives late",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 3, and its trace number is 346.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 346.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a changed landmark"
  },
  {
    id:347,
    name:"Where the Clockwork Nest · 0347",
    region:"Mirror Waste",
    signal:"a shadow moving against the light",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 4, and its trace number is 347.",
    clue:"Return to the place where the floor changes colour. Fragment index: 347.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A distant light answers with one measured flash.",
    reward:"a hidden passage"
  },
  {
    id:348,
    name:"Before the Clockwork Nest · 0348",
    region:"Quiet Reach",
    signal:"a distant bell with no echo",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 5, and its trace number is 348.",
    clue:"The answer is stored in the order of your choices. Fragment index: 348.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The path behind you quietly changes its shape.",
    reward:"a second chance"
  },
  {
    id:349,
    name:"After the Clockwork Nest · 0349",
    region:"Moss Quarter",
    signal:"a hum that follows silence",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 6, and its trace number is 349.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 349.",
    lesson:"Observation can be a form of movement.",
    response:"The air grows still, waiting for another choice.",
    reward:"a memory fragment"
  },
  {
    id:350,
    name:"Between the Clockwork Nest · 0350",
    region:"Hollow Canopy",
    signal:"a warm line beneath the stone",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 7, and its trace number is 350.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 350.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a map trace"
  },
  {
    id:351,
    name:"Above the Clockwork Nest · 0351",
    region:"Lantern Expanse",
    signal:"a distant bell with no echo",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 1, and its trace number is 351.",
    clue:"Find the only light that does not pulse. Fragment index: 351.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The echo returns with one extra note.",
    reward:"a sealed memory"
  },
  {
    id:352,
    name:"Below the Clockwork Nest · 0352",
    region:"Pale Engine",
    signal:"a hum that follows silence",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 2, and its trace number is 352.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 352.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The ground glows for a moment, then settles.",
    reward:"a clearer signal"
  },
  {
    id:353,
    name:"The Empty Theatre · 0353",
    region:"Quiet Reach",
    signal:"a warm line beneath the stone",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 3, and its trace number is 353.",
    clue:"The safest route is not always the shortest. Fragment index: 353.",
    lesson:"Observation can be a form of movement.",
    response:"A new mark appears beside your last footprint.",
    reward:"a changed landmark"
  },
  {
    id:354,
    name:"A Empty Theatre · 0354",
    region:"Moss Quarter",
    signal:"a pale mark that shifts position",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 4, and its trace number is 354.",
    clue:"Your previous route is the map for this one. Fragment index: 354.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a hidden passage"
  },
  {
    id:355,
    name:"Beneath the Empty Theatre · 0355",
    region:"Hollow Canopy",
    signal:"a small star below the horizon",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 5, and its trace number is 355.",
    clue:"Move once, pause once, then listen again. Fragment index: 355.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a second chance"
  },
  {
    id:356,
    name:"Beyond the Empty Theatre · 0356",
    region:"Lantern Expanse",
    signal:"three notes with no source",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 6, and its trace number is 356.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 356.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a path that remembers"
  },
  {
    id:357,
    name:"Inside the Empty Theatre · 0357",
    region:"Pale Engine",
    signal:"a slow rhythm under the wind",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 7, and its trace number is 357.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 357.",
    lesson:"Observation can be a form of movement.",
    response:"The horizon brightens where your route bends.",
    reward:"an echo token"
  },
  {
    id:358,
    name:"Under the Empty Theatre · 0358",
    region:"Frostline",
    signal:"a small star below the horizon",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 1, and its trace number is 358.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 358.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a stored reflection"
  },
  {
    id:359,
    name:"Across the Empty Theatre · 0359",
    region:"Last Horizon",
    signal:"three notes with no source",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 2, and its trace number is 359.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 359.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A distant light answers with one measured flash.",
    reward:"a new depth"
  },
  {
    id:360,
    name:"Behind the Empty Theatre · 0360",
    region:"Glasswater Basin",
    signal:"a slow rhythm under the wind",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 3, and its trace number is 360.",
    clue:"Return to the place where the floor changes colour. Fragment index: 360.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The path behind you quietly changes its shape.",
    reward:"a quiet clue"
  },
  {
    id:361,
    name:"Within the Empty Theatre · 0361",
    region:"Blue Divide",
    signal:"a breath behind the wall",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 4, and its trace number is 361.",
    clue:"The answer is stored in the order of your choices. Fragment index: 361.",
    lesson:"Observation can be a form of movement.",
    response:"The air grows still, waiting for another choice.",
    reward:"a memory fragment"
  },
  {
    id:362,
    name:"At the edge of the Empty Theatre · 0362",
    region:"Ember Archive",
    signal:"a low blue pulse",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 5, and its trace number is 362.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 362.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a map trace"
  },
  {
    id:363,
    name:"Where the Empty Theatre · 0363",
    region:"Echo Marsh",
    signal:"a ripple crossing dry ground",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 6, and its trace number is 363.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 363.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The echo returns with one extra note.",
    reward:"a sealed memory"
  },
  {
    id:364,
    name:"Before the Empty Theatre · 0364",
    region:"Last Horizon",
    signal:"a pattern of footprints facing inward",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 7, and its trace number is 364.",
    clue:"Find the only light that does not pulse. Fragment index: 364.",
    lesson:"Memory is more than a record of where you went.",
    response:"The ground glows for a moment, then settles.",
    reward:"a clearer signal"
  },
  {
    id:365,
    name:"After the Empty Theatre · 0365",
    region:"Glasswater Basin",
    signal:"a low blue pulse",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 1, and its trace number is 365.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 365.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A new mark appears beside your last footprint.",
    reward:"a changed landmark"
  },
  {
    id:366,
    name:"Between the Empty Theatre · 0366",
    region:"Blue Divide",
    signal:"a ripple crossing dry ground",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 2, and its trace number is 366.",
    clue:"The safest route is not always the shortest. Fragment index: 366.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a hidden passage"
  },
  {
    id:367,
    name:"Above the Empty Theatre · 0367",
    region:"Ember Archive",
    signal:"a pattern of footprints facing inward",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 3, and its trace number is 367.",
    clue:"Your previous route is the map for this one. Fragment index: 367.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a second chance"
  },
  {
    id:368,
    name:"Below the Empty Theatre · 0368",
    region:"Echo Marsh",
    signal:"a glow hidden inside a crack",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 4, and its trace number is 368.",
    clue:"Move once, pause once, then listen again. Fragment index: 368.",
    lesson:"Memory is more than a record of where you went.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a path that remembers"
  },
  {
    id:369,
    name:"The Moss Cathedral · 0369",
    region:"Mirror Waste",
    signal:"a door-shaped gap in the air",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 5, and its trace number is 369.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 369.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"an echo token"
  },
  {
    id:370,
    name:"A Moss Cathedral · 0370",
    region:"Quiet Reach",
    signal:"a thin thread of silver light",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 6, and its trace number is 370.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 370.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A distant light answers with one measured flash.",
    reward:"a stored reflection"
  },
  {
    id:371,
    name:"Beneath the Moss Cathedral · 0371",
    region:"Moss Quarter",
    signal:"a reflection that arrives late",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 7, and its trace number is 371.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 371.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The path behind you quietly changes its shape.",
    reward:"a new depth"
  },
  {
    id:372,
    name:"Beyond the Moss Cathedral · 0372",
    region:"Hollow Canopy",
    signal:"a door-shaped gap in the air",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 1, and its trace number is 372.",
    clue:"A repeated step can open a door, but only once. Fragment index: 372.",
    lesson:"Memory is more than a record of where you went.",
    response:"The air grows still, waiting for another choice.",
    reward:"a quiet clue"
  },
  {
    id:373,
    name:"Inside the Moss Cathedral · 0373",
    region:"Lantern Expanse",
    signal:"a thin thread of silver light",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 2, and its trace number is 373.",
    clue:"The second path is real only after you turn away. Fragment index: 373.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a memory fragment"
  },
  {
    id:374,
    name:"Under the Moss Cathedral · 0374",
    region:"Pale Engine",
    signal:"a reflection that arrives late",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 3, and its trace number is 374.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 374.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The echo returns with one extra note.",
    reward:"a map trace"
  },
  {
    id:375,
    name:"Across the Moss Cathedral · 0375",
    region:"Quiet Reach",
    signal:"a shadow moving against the light",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 4, and its trace number is 375.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 375.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The ground glows for a moment, then settles.",
    reward:"a sealed memory"
  },
  {
    id:376,
    name:"Behind the Moss Cathedral · 0376",
    region:"Moss Quarter",
    signal:"a distant bell with no echo",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 5, and its trace number is 376.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 376.",
    lesson:"Memory is more than a record of where you went.",
    response:"A new mark appears beside your last footprint.",
    reward:"a clearer signal"
  },
  {
    id:377,
    name:"Within the Moss Cathedral · 0377",
    region:"Hollow Canopy",
    signal:"a hum that follows silence",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 6, and its trace number is 377.",
    clue:"Find the only light that does not pulse. Fragment index: 377.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a changed landmark"
  },
  {
    id:378,
    name:"At the edge of the Moss Cathedral · 0378",
    region:"Lantern Expanse",
    signal:"a warm line beneath the stone",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 7, and its trace number is 378.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 378.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a new depth"
  },
  {
    id:379,
    name:"Where the Moss Cathedral · 0379",
    region:"Pale Engine",
    signal:"a distant bell with no echo",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 1, and its trace number is 379.",
    clue:"The safest route is not always the shortest. Fragment index: 379.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a quiet clue"
  },
  {
    id:380,
    name:"Before the Moss Cathedral · 0380",
    region:"Frostline",
    signal:"a hum that follows silence",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 2, and its trace number is 380.",
    clue:"Your previous route is the map for this one. Fragment index: 380.",
    lesson:"Memory is more than a record of where you went.",
    response:"The horizon brightens where your route bends.",
    reward:"a memory fragment"
  },
  {
    id:381,
    name:"After the Moss Cathedral · 0381",
    region:"Last Horizon",
    signal:"a warm line beneath the stone",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 3, and its trace number is 381.",
    clue:"Move once, pause once, then listen again. Fragment index: 381.",
    lesson:"Silence is information when you learn to listen.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a map trace"
  },
  {
    id:382,
    name:"Between the Moss Cathedral · 0382",
    region:"Glasswater Basin",
    signal:"a pale mark that shifts position",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 4, and its trace number is 382.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 382.",
    lesson:"Returning is not the same as repeating.",
    response:"A distant light answers with one measured flash.",
    reward:"a sealed memory"
  },
  {
    id:383,
    name:"Above the Moss Cathedral · 0383",
    region:"Blue Divide",
    signal:"a small star below the horizon",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 5, and its trace number is 383.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 383.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The path behind you quietly changes its shape.",
    reward:"a clearer signal"
  },
  {
    id:384,
    name:"Below the Moss Cathedral · 0384",
    region:"Ember Archive",
    signal:"three notes with no source",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 6, and its trace number is 384.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 384.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The air grows still, waiting for another choice.",
    reward:"a changed landmark"
  },
  {
    id:385,
    name:"The Fading Map · 0385",
    region:"Echo Marsh",
    signal:"a slow rhythm under the wind",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 7, and its trace number is 385.",
    clue:"A repeated step can open a door, but only once. Fragment index: 385.",
    lesson:"Silence is information when you learn to listen.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a hidden passage"
  },
  {
    id:386,
    name:"A Fading Map · 0386",
    region:"Last Horizon",
    signal:"a small star below the horizon",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 1, and its trace number is 386.",
    clue:"The second path is real only after you turn away. Fragment index: 386.",
    lesson:"Returning is not the same as repeating.",
    response:"The echo returns with one extra note.",
    reward:"a second chance"
  },
  {
    id:387,
    name:"Beneath the Fading Map · 0387",
    region:"Glasswater Basin",
    signal:"three notes with no source",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 2, and its trace number is 387.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 387.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The ground glows for a moment, then settles.",
    reward:"a path that remembers"
  },
  {
    id:388,
    name:"Beyond the Fading Map · 0388",
    region:"Blue Divide",
    signal:"a slow rhythm under the wind",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 3, and its trace number is 388.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 388.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A new mark appears beside your last footprint.",
    reward:"an echo token"
  },
  {
    id:389,
    name:"Inside the Fading Map · 0389",
    region:"Ember Archive",
    signal:"a breath behind the wall",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 4, and its trace number is 389.",
    clue:"Return to the place where the floor changes colour. Fragment index: 389.",
    lesson:"Silence is information when you learn to listen.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a stored reflection"
  },
  {
    id:390,
    name:"Under the Fading Map · 0390",
    region:"Echo Marsh",
    signal:"a low blue pulse",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 5, and its trace number is 390.",
    clue:"The answer is stored in the order of your choices. Fragment index: 390.",
    lesson:"Returning is not the same as repeating.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a new depth"
  },
  {
    id:391,
    name:"Across the Fading Map · 0391",
    region:"Mirror Waste",
    signal:"a ripple crossing dry ground",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 6, and its trace number is 391.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 391.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a quiet clue"
  },
  {
    id:392,
    name:"Behind the Fading Map · 0392",
    region:"Quiet Reach",
    signal:"a pattern of footprints facing inward",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 7, and its trace number is 392.",
    clue:"The safest route is not always the shortest. Fragment index: 392.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a memory fragment"
  },
  {
    id:393,
    name:"Within the Fading Map · 0393",
    region:"Moss Quarter",
    signal:"a low blue pulse",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 1, and its trace number is 393.",
    clue:"Your previous route is the map for this one. Fragment index: 393.",
    lesson:"Silence is information when you learn to listen.",
    response:"A distant light answers with one measured flash.",
    reward:"a map trace"
  },
  {
    id:394,
    name:"At the edge of the Fading Map · 0394",
    region:"Hollow Canopy",
    signal:"a ripple crossing dry ground",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 2, and its trace number is 394.",
    clue:"Move once, pause once, then listen again. Fragment index: 394.",
    lesson:"Returning is not the same as repeating.",
    response:"The path behind you quietly changes its shape.",
    reward:"a sealed memory"
  },
  {
    id:395,
    name:"Where the Fading Map · 0395",
    region:"Lantern Expanse",
    signal:"a pattern of footprints facing inward",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 3, and its trace number is 395.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 395.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The air grows still, waiting for another choice.",
    reward:"a clearer signal"
  },
  {
    id:396,
    name:"Before the Fading Map · 0396",
    region:"Pale Engine",
    signal:"a glow hidden inside a crack",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 4, and its trace number is 396.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 396.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a changed landmark"
  },
  {
    id:397,
    name:"After the Fading Map · 0397",
    region:"Quiet Reach",
    signal:"a door-shaped gap in the air",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 5, and its trace number is 397.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 397.",
    lesson:"Silence is information when you learn to listen.",
    response:"The echo returns with one extra note.",
    reward:"a hidden passage"
  },
  {
    id:398,
    name:"Between the Fading Map · 0398",
    region:"Moss Quarter",
    signal:"a thin thread of silver light",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 6, and its trace number is 398.",
    clue:"A repeated step can open a door, but only once. Fragment index: 398.",
    lesson:"Returning is not the same as repeating.",
    response:"The ground glows for a moment, then settles.",
    reward:"a second chance"
  },
  {
    id:399,
    name:"Above the Fading Map · 0399",
    region:"Hollow Canopy",
    signal:"a reflection that arrives late",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 7, and its trace number is 399.",
    clue:"The second path is real only after you turn away. Fragment index: 399.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A new mark appears beside your last footprint.",
    reward:"a path that remembers"
  },
  {
    id:400,
    name:"Below the Fading Map · 0400",
    region:"Lantern Expanse",
    signal:"a door-shaped gap in the air",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 1, and its trace number is 400.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 400.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The observer pauses, then follows at a distance.",
    reward:"an echo token"
  },
  {
    id:401,
    name:"The Copper Forest · 0401",
    region:"Pale Engine",
    signal:"a thin thread of silver light",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 2, and its trace number is 401.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 401.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a stored reflection"
  },
  {
    id:402,
    name:"A Copper Forest · 0402",
    region:"Frostline",
    signal:"a reflection that arrives late",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 3, and its trace number is 402.",
    clue:"Return to the place where the floor changes colour. Fragment index: 402.",
    lesson:"Observation can be a form of movement.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a new depth"
  },
  {
    id:403,
    name:"Beneath the Copper Forest · 0403",
    region:"Last Horizon",
    signal:"a shadow moving against the light",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 4, and its trace number is 403.",
    clue:"The answer is stored in the order of your choices. Fragment index: 403.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The horizon brightens where your route bends.",
    reward:"a quiet clue"
  },
  {
    id:404,
    name:"Beyond the Copper Forest · 0404",
    region:"Glasswater Basin",
    signal:"a distant bell with no echo",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 5, and its trace number is 404.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 404.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a memory fragment"
  },
  {
    id:405,
    name:"Inside the Copper Forest · 0405",
    region:"Blue Divide",
    signal:"a hum that follows silence",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 6, and its trace number is 405.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 405.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A distant light answers with one measured flash.",
    reward:"a map trace"
  },
  {
    id:406,
    name:"Under the Copper Forest · 0406",
    region:"Ember Archive",
    signal:"a warm line beneath the stone",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 7, and its trace number is 406.",
    clue:"Find the only light that does not pulse. Fragment index: 406.",
    lesson:"Observation can be a form of movement.",
    response:"The path behind you quietly changes its shape.",
    reward:"a sealed memory"
  },
  {
    id:407,
    name:"Across the Copper Forest · 0407",
    region:"Echo Marsh",
    signal:"a distant bell with no echo",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 1, and its trace number is 407.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 407.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The air grows still, waiting for another choice.",
    reward:"an echo token"
  },
  {
    id:408,
    name:"Behind the Copper Forest · 0408",
    region:"Last Horizon",
    signal:"a hum that follows silence",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 2, and its trace number is 408.",
    clue:"The safest route is not always the shortest. Fragment index: 408.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a stored reflection"
  },
  {
    id:409,
    name:"Within the Copper Forest · 0409",
    region:"Glasswater Basin",
    signal:"a warm line beneath the stone",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 3, and its trace number is 409.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 409.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The echo returns with one extra note.",
    reward:"a new depth"
  },
  {
    id:410,
    name:"At the edge of the Copper Forest · 0410",
    region:"Blue Divide",
    signal:"a pale mark that shifts position",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 4, and its trace number is 410.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 410.",
    lesson:"Observation can be a form of movement.",
    response:"The ground glows for a moment, then settles.",
    reward:"a quiet clue"
  },
  {
    id:411,
    name:"Where the Copper Forest · 0411",
    region:"Ember Archive",
    signal:"a small star below the horizon",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 5, and its trace number is 411.",
    clue:"A repeated step can open a door, but only once. Fragment index: 411.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A new mark appears beside your last footprint.",
    reward:"a memory fragment"
  },
  {
    id:412,
    name:"Before the Copper Forest · 0412",
    region:"Echo Marsh",
    signal:"three notes with no source",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 6, and its trace number is 412.",
    clue:"The second path is real only after you turn away. Fragment index: 412.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a map trace"
  },
  {
    id:413,
    name:"After the Copper Forest · 0413",
    region:"Mirror Waste",
    signal:"a slow rhythm under the wind",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 7, and its trace number is 413.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 413.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a sealed memory"
  },
  {
    id:414,
    name:"Between the Copper Forest · 0414",
    region:"Quiet Reach",
    signal:"a small star below the horizon",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 1, and its trace number is 414.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 414.",
    lesson:"Observation can be a form of movement.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a clearer signal"
  },
  {
    id:415,
    name:"Above the Copper Forest · 0415",
    region:"Moss Quarter",
    signal:"three notes with no source",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 2, and its trace number is 415.",
    clue:"Return to the place where the floor changes colour. Fragment index: 415.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a changed landmark"
  },
  {
    id:416,
    name:"Below the Copper Forest · 0416",
    region:"Hollow Canopy",
    signal:"a slow rhythm under the wind",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 3, and its trace number is 416.",
    clue:"The answer is stored in the order of your choices. Fragment index: 416.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A distant light answers with one measured flash.",
    reward:"a hidden passage"
  },
  {
    id:417,
    name:"The Shallow Sky · 0417",
    region:"Lantern Expanse",
    signal:"a breath behind the wall",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 4, and its trace number is 417.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 417.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The path behind you quietly changes its shape.",
    reward:"a second chance"
  },
  {
    id:418,
    name:"A Shallow Sky · 0418",
    region:"Pale Engine",
    signal:"a low blue pulse",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 5, and its trace number is 418.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 418.",
    lesson:"Observation can be a form of movement.",
    response:"The air grows still, waiting for another choice.",
    reward:"a path that remembers"
  },
  {
    id:419,
    name:"Beneath the Shallow Sky · 0419",
    region:"Quiet Reach",
    signal:"a ripple crossing dry ground",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 6, and its trace number is 419.",
    clue:"Find the only light that does not pulse. Fragment index: 419.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A small opening appears in the wall of darkness.",
    reward:"an echo token"
  },
  {
    id:420,
    name:"Beyond the Shallow Sky · 0420",
    region:"Moss Quarter",
    signal:"a pattern of footprints facing inward",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 7, and its trace number is 420.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 420.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The echo returns with one extra note.",
    reward:"a stored reflection"
  },
  {
    id:421,
    name:"Inside the Shallow Sky · 0421",
    region:"Hollow Canopy",
    signal:"a low blue pulse",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 1, and its trace number is 421.",
    clue:"The safest route is not always the shortest. Fragment index: 421.",
    lesson:"Memory is more than a record of where you went.",
    response:"The ground glows for a moment, then settles.",
    reward:"a new depth"
  },
  {
    id:422,
    name:"Under the Shallow Sky · 0422",
    region:"Lantern Expanse",
    signal:"a ripple crossing dry ground",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 2, and its trace number is 422.",
    clue:"Your previous route is the map for this one. Fragment index: 422.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A new mark appears beside your last footprint.",
    reward:"a quiet clue"
  },
  {
    id:423,
    name:"Across the Shallow Sky · 0423",
    region:"Pale Engine",
    signal:"a pattern of footprints facing inward",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 3, and its trace number is 423.",
    clue:"Move once, pause once, then listen again. Fragment index: 423.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a memory fragment"
  },
  {
    id:424,
    name:"Behind the Shallow Sky · 0424",
    region:"Frostline",
    signal:"a glow hidden inside a crack",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 4, and its trace number is 424.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 424.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a map trace"
  },
  {
    id:425,
    name:"Within the Shallow Sky · 0425",
    region:"Last Horizon",
    signal:"a door-shaped gap in the air",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 5, and its trace number is 425.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 425.",
    lesson:"Memory is more than a record of where you went.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a sealed memory"
  },
  {
    id:426,
    name:"At the edge of the Shallow Sky · 0426",
    region:"Glasswater Basin",
    signal:"a thin thread of silver light",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 6, and its trace number is 426.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 426.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The horizon brightens where your route bends.",
    reward:"a clearer signal"
  },
  {
    id:427,
    name:"Where the Shallow Sky · 0427",
    region:"Blue Divide",
    signal:"a reflection that arrives late",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 7, and its trace number is 427.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 427.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a changed landmark"
  },
  {
    id:428,
    name:"Before the Shallow Sky · 0428",
    region:"Ember Archive",
    signal:"a door-shaped gap in the air",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 1, and its trace number is 428.",
    clue:"Return to the place where the floor changes colour. Fragment index: 428.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A distant light answers with one measured flash.",
    reward:"a hidden passage"
  },
  {
    id:429,
    name:"After the Shallow Sky · 0429",
    region:"Echo Marsh",
    signal:"a thin thread of silver light",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 2, and its trace number is 429.",
    clue:"The answer is stored in the order of your choices. Fragment index: 429.",
    lesson:"Memory is more than a record of where you went.",
    response:"The path behind you quietly changes its shape.",
    reward:"a second chance"
  },
  {
    id:430,
    name:"Between the Shallow Sky · 0430",
    region:"Last Horizon",
    signal:"a reflection that arrives late",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 3, and its trace number is 430.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 430.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The air grows still, waiting for another choice.",
    reward:"a path that remembers"
  },
  {
    id:431,
    name:"Above the Shallow Sky · 0431",
    region:"Glasswater Basin",
    signal:"a shadow moving against the light",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 4, and its trace number is 431.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 431.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A small opening appears in the wall of darkness.",
    reward:"an echo token"
  },
  {
    id:432,
    name:"Below the Shallow Sky · 0432",
    region:"Blue Divide",
    signal:"a distant bell with no echo",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 5, and its trace number is 432.",
    clue:"Find the only light that does not pulse. Fragment index: 432.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The echo returns with one extra note.",
    reward:"a stored reflection"
  },
  {
    id:433,
    name:"The Lost Observatory · 0433",
    region:"Ember Archive",
    signal:"a hum that follows silence",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 6, and its trace number is 433.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 433.",
    lesson:"Memory is more than a record of where you went.",
    response:"The ground glows for a moment, then settles.",
    reward:"a new depth"
  },
  {
    id:434,
    name:"A Lost Observatory · 0434",
    region:"Echo Marsh",
    signal:"a warm line beneath the stone",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 7, and its trace number is 434.",
    clue:"The safest route is not always the shortest. Fragment index: 434.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A new mark appears beside your last footprint.",
    reward:"a quiet clue"
  },
  {
    id:435,
    name:"Beneath the Lost Observatory · 0435",
    region:"Mirror Waste",
    signal:"a distant bell with no echo",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 1, and its trace number is 435.",
    clue:"Your previous route is the map for this one. Fragment index: 435.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a memory fragment"
  },
  {
    id:436,
    name:"Beyond the Lost Observatory · 0436",
    region:"Quiet Reach",
    signal:"a hum that follows silence",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 2, and its trace number is 436.",
    clue:"Move once, pause once, then listen again. Fragment index: 436.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a second chance"
  },
  {
    id:437,
    name:"Inside the Lost Observatory · 0437",
    region:"Moss Quarter",
    signal:"a warm line beneath the stone",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 3, and its trace number is 437.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 437.",
    lesson:"Memory is more than a record of where you went.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a path that remembers"
  },
  {
    id:438,
    name:"Under the Lost Observatory · 0438",
    region:"Hollow Canopy",
    signal:"a pale mark that shifts position",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 4, and its trace number is 438.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 438.",
    lesson:"Silence is information when you learn to listen.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"an echo token"
  },
  {
    id:439,
    name:"Across the Lost Observatory · 0439",
    region:"Lantern Expanse",
    signal:"a small star below the horizon",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 5, and its trace number is 439.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 439.",
    lesson:"Returning is not the same as repeating.",
    response:"A distant light answers with one measured flash.",
    reward:"a stored reflection"
  },
  {
    id:440,
    name:"Behind the Lost Observatory · 0440",
    region:"Pale Engine",
    signal:"three notes with no source",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 6, and its trace number is 440.",
    clue:"A repeated step can open a door, but only once. Fragment index: 440.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The path behind you quietly changes its shape.",
    reward:"a new depth"
  },
  {
    id:441,
    name:"Within the Lost Observatory · 0441",
    region:"Quiet Reach",
    signal:"a slow rhythm under the wind",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 7, and its trace number is 441.",
    clue:"The second path is real only after you turn away. Fragment index: 441.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The air grows still, waiting for another choice.",
    reward:"a quiet clue"
  },
  {
    id:442,
    name:"At the edge of the Lost Observatory · 0442",
    region:"Moss Quarter",
    signal:"a small star below the horizon",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 1, and its trace number is 442.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 442.",
    lesson:"Silence is information when you learn to listen.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a memory fragment"
  },
  {
    id:443,
    name:"Where the Lost Observatory · 0443",
    region:"Hollow Canopy",
    signal:"three notes with no source",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 2, and its trace number is 443.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 443.",
    lesson:"Returning is not the same as repeating.",
    response:"The echo returns with one extra note.",
    reward:"a map trace"
  },
  {
    id:444,
    name:"Before the Lost Observatory · 0444",
    region:"Lantern Expanse",
    signal:"a slow rhythm under the wind",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 3, and its trace number is 444.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 444.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The ground glows for a moment, then settles.",
    reward:"a sealed memory"
  },
  {
    id:445,
    name:"After the Lost Observatory · 0445",
    region:"Pale Engine",
    signal:"a breath behind the wall",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 4, and its trace number is 445.",
    clue:"Find the only light that does not pulse. Fragment index: 445.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A new mark appears beside your last footprint.",
    reward:"a clearer signal"
  },
  {
    id:446,
    name:"Between the Lost Observatory · 0446",
    region:"Frostline",
    signal:"a low blue pulse",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 5, and its trace number is 446.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 446.",
    lesson:"Silence is information when you learn to listen.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a changed landmark"
  },
  {
    id:447,
    name:"Above the Lost Observatory · 0447",
    region:"Last Horizon",
    signal:"a ripple crossing dry ground",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 6, and its trace number is 447.",
    clue:"The safest route is not always the shortest. Fragment index: 447.",
    lesson:"Returning is not the same as repeating.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a hidden passage"
  },
  {
    id:448,
    name:"Below the Lost Observatory · 0448",
    region:"Glasswater Basin",
    signal:"a pattern of footprints facing inward",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 7, and its trace number is 448.",
    clue:"Your previous route is the map for this one. Fragment index: 448.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a second chance"
  },
  {
    id:449,
    name:"The Moonlit Well · 0449",
    region:"Blue Divide",
    signal:"a low blue pulse",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 1, and its trace number is 449.",
    clue:"Move once, pause once, then listen again. Fragment index: 449.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The horizon brightens where your route bends.",
    reward:"a path that remembers"
  },
  {
    id:450,
    name:"A Moonlit Well · 0450",
    region:"Ember Archive",
    signal:"a ripple crossing dry ground",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 2, and its trace number is 450.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 450.",
    lesson:"Silence is information when you learn to listen.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"an echo token"
  },
  {
    id:451,
    name:"Beneath the Moonlit Well · 0451",
    region:"Echo Marsh",
    signal:"a pattern of footprints facing inward",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 3, and its trace number is 451.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 451.",
    lesson:"Returning is not the same as repeating.",
    response:"A distant light answers with one measured flash.",
    reward:"a stored reflection"
  },
  {
    id:452,
    name:"Beyond the Moonlit Well · 0452",
    region:"Last Horizon",
    signal:"a glow hidden inside a crack",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 4, and its trace number is 452.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 452.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The path behind you quietly changes its shape.",
    reward:"a new depth"
  },
  {
    id:453,
    name:"Inside the Moonlit Well · 0453",
    region:"Glasswater Basin",
    signal:"a door-shaped gap in the air",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 5, and its trace number is 453.",
    clue:"A repeated step can open a door, but only once. Fragment index: 453.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The air grows still, waiting for another choice.",
    reward:"a quiet clue"
  },
  {
    id:454,
    name:"Under the Moonlit Well · 0454",
    region:"Blue Divide",
    signal:"a thin thread of silver light",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 6, and its trace number is 454.",
    clue:"The second path is real only after you turn away. Fragment index: 454.",
    lesson:"Silence is information when you learn to listen.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a memory fragment"
  },
  {
    id:455,
    name:"Across the Moonlit Well · 0455",
    region:"Ember Archive",
    signal:"a reflection that arrives late",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 7, and its trace number is 455.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 455.",
    lesson:"Returning is not the same as repeating.",
    response:"The echo returns with one extra note.",
    reward:"a map trace"
  },
  {
    id:456,
    name:"Behind the Moonlit Well · 0456",
    region:"Echo Marsh",
    signal:"a door-shaped gap in the air",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 1, and its trace number is 456.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 456.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The ground glows for a moment, then settles.",
    reward:"a sealed memory"
  },
  {
    id:457,
    name:"Within the Moonlit Well · 0457",
    region:"Mirror Waste",
    signal:"a thin thread of silver light",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 2, and its trace number is 457.",
    clue:"Return to the place where the floor changes colour. Fragment index: 457.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A new mark appears beside your last footprint.",
    reward:"a clearer signal"
  },
  {
    id:458,
    name:"At the edge of the Moonlit Well · 0458",
    region:"Quiet Reach",
    signal:"a reflection that arrives late",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 3, and its trace number is 458.",
    clue:"The answer is stored in the order of your choices. Fragment index: 458.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a changed landmark"
  },
  {
    id:459,
    name:"Where the Moonlit Well · 0459",
    region:"Moss Quarter",
    signal:"a shadow moving against the light",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 4, and its trace number is 459.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 459.",
    lesson:"Observation can be a form of movement.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a hidden passage"
  },
  {
    id:460,
    name:"Before the Moonlit Well · 0460",
    region:"Hollow Canopy",
    signal:"a distant bell with no echo",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 5, and its trace number is 460.",
    clue:"The safest route is not always the shortest. Fragment index: 460.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a second chance"
  },
  {
    id:461,
    name:"After the Moonlit Well · 0461",
    region:"Lantern Expanse",
    signal:"a hum that follows silence",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 6, and its trace number is 461.",
    clue:"Your previous route is the map for this one. Fragment index: 461.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a path that remembers"
  },
  {
    id:462,
    name:"Between the Moonlit Well · 0462",
    region:"Pale Engine",
    signal:"a warm line beneath the stone",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 7, and its trace number is 462.",
    clue:"Move once, pause once, then listen again. Fragment index: 462.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A distant light answers with one measured flash.",
    reward:"an echo token"
  },
  {
    id:463,
    name:"Above the Moonlit Well · 0463",
    region:"Quiet Reach",
    signal:"a distant bell with no echo",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 1, and its trace number is 463.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 463.",
    lesson:"Observation can be a form of movement.",
    response:"The path behind you quietly changes its shape.",
    reward:"a stored reflection"
  },
  {
    id:464,
    name:"Below the Moonlit Well · 0464",
    region:"Moss Quarter",
    signal:"a hum that follows silence",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 2, and its trace number is 464.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 464.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The air grows still, waiting for another choice.",
    reward:"a new depth"
  },
  {
    id:465,
    name:"The Crimson Passage · 0465",
    region:"Hollow Canopy",
    signal:"a warm line beneath the stone",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 3, and its trace number is 465.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 465.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a changed landmark"
  },
  {
    id:466,
    name:"A Crimson Passage · 0466",
    region:"Lantern Expanse",
    signal:"a pale mark that shifts position",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 4, and its trace number is 466.",
    clue:"A repeated step can open a door, but only once. Fragment index: 466.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The echo returns with one extra note.",
    reward:"a hidden passage"
  },
  {
    id:467,
    name:"Beneath the Crimson Passage · 0467",
    region:"Pale Engine",
    signal:"a small star below the horizon",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 5, and its trace number is 467.",
    clue:"The second path is real only after you turn away. Fragment index: 467.",
    lesson:"Observation can be a form of movement.",
    response:"The ground glows for a moment, then settles.",
    reward:"a second chance"
  },
  {
    id:468,
    name:"Beyond the Crimson Passage · 0468",
    region:"Frostline",
    signal:"three notes with no source",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 6, and its trace number is 468.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 468.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A new mark appears beside your last footprint.",
    reward:"a path that remembers"
  },
  {
    id:469,
    name:"Inside the Crimson Passage · 0469",
    region:"Last Horizon",
    signal:"a slow rhythm under the wind",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 7, and its trace number is 469.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 469.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The observer pauses, then follows at a distance.",
    reward:"an echo token"
  },
  {
    id:470,
    name:"Under the Crimson Passage · 0470",
    region:"Glasswater Basin",
    signal:"a small star below the horizon",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 1, and its trace number is 470.",
    clue:"Return to the place where the floor changes colour. Fragment index: 470.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a stored reflection"
  },
  {
    id:471,
    name:"Across the Crimson Passage · 0471",
    region:"Blue Divide",
    signal:"three notes with no source",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 2, and its trace number is 471.",
    clue:"The answer is stored in the order of your choices. Fragment index: 471.",
    lesson:"Observation can be a form of movement.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a new depth"
  },
  {
    id:472,
    name:"Behind the Crimson Passage · 0472",
    region:"Ember Archive",
    signal:"a slow rhythm under the wind",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 3, and its trace number is 472.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 472.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The horizon brightens where your route bends.",
    reward:"a quiet clue"
  },
  {
    id:473,
    name:"Within the Crimson Passage · 0473",
    region:"Echo Marsh",
    signal:"a breath behind the wall",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 4, and its trace number is 473.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 473.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a memory fragment"
  },
  {
    id:474,
    name:"At the edge of the Crimson Passage · 0474",
    region:"Last Horizon",
    signal:"a low blue pulse",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 5, and its trace number is 474.",
    clue:"Find the only light that does not pulse. Fragment index: 474.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A distant light answers with one measured flash.",
    reward:"a map trace"
  },
  {
    id:475,
    name:"Where the Crimson Passage · 0475",
    region:"Glasswater Basin",
    signal:"a ripple crossing dry ground",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 6, and its trace number is 475.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 475.",
    lesson:"Observation can be a form of movement.",
    response:"The path behind you quietly changes its shape.",
    reward:"a sealed memory"
  },
  {
    id:476,
    name:"Before the Crimson Passage · 0476",
    region:"Blue Divide",
    signal:"a pattern of footprints facing inward",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 7, and its trace number is 476.",
    clue:"The safest route is not always the shortest. Fragment index: 476.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The air grows still, waiting for another choice.",
    reward:"a clearer signal"
  },
  {
    id:477,
    name:"After the Crimson Passage · 0477",
    region:"Ember Archive",
    signal:"a low blue pulse",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 1, and its trace number is 477.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 477.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a changed landmark"
  },
  {
    id:478,
    name:"Between the Crimson Passage · 0478",
    region:"Echo Marsh",
    signal:"a ripple crossing dry ground",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 2, and its trace number is 478.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 478.",
    lesson:"Memory is more than a record of where you went.",
    response:"The echo returns with one extra note.",
    reward:"a hidden passage"
  },
  {
    id:479,
    name:"Above the Crimson Passage · 0479",
    region:"Mirror Waste",
    signal:"a pattern of footprints facing inward",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 3, and its trace number is 479.",
    clue:"A repeated step can open a door, but only once. Fragment index: 479.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The ground glows for a moment, then settles.",
    reward:"a second chance"
  },
  {
    id:480,
    name:"Below the Crimson Passage · 0480",
    region:"Quiet Reach",
    signal:"a glow hidden inside a crack",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 4, and its trace number is 480.",
    clue:"The second path is real only after you turn away. Fragment index: 480.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A new mark appears beside your last footprint.",
    reward:"a path that remembers"
  },
  {
    id:481,
    name:"The Winter Library · 0481",
    region:"Moss Quarter",
    signal:"a door-shaped gap in the air",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 5, and its trace number is 481.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 481.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The observer pauses, then follows at a distance.",
    reward:"an echo token"
  },
  {
    id:482,
    name:"A Winter Library · 0482",
    region:"Hollow Canopy",
    signal:"a thin thread of silver light",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 6, and its trace number is 482.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 482.",
    lesson:"Memory is more than a record of where you went.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a stored reflection"
  },
  {
    id:483,
    name:"Beneath the Winter Library · 0483",
    region:"Lantern Expanse",
    signal:"a reflection that arrives late",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 7, and its trace number is 483.",
    clue:"Return to the place where the floor changes colour. Fragment index: 483.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a new depth"
  },
  {
    id:484,
    name:"Beyond the Winter Library · 0484",
    region:"Pale Engine",
    signal:"a door-shaped gap in the air",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 1, and its trace number is 484.",
    clue:"The answer is stored in the order of your choices. Fragment index: 484.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a quiet clue"
  },
  {
    id:485,
    name:"Inside the Winter Library · 0485",
    region:"Quiet Reach",
    signal:"a thin thread of silver light",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 2, and its trace number is 485.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 485.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A distant light answers with one measured flash.",
    reward:"a memory fragment"
  },
  {
    id:486,
    name:"Under the Winter Library · 0486",
    region:"Moss Quarter",
    signal:"a reflection that arrives late",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 3, and its trace number is 486.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 486.",
    lesson:"Memory is more than a record of where you went.",
    response:"The path behind you quietly changes its shape.",
    reward:"a map trace"
  },
  {
    id:487,
    name:"Across the Winter Library · 0487",
    region:"Hollow Canopy",
    signal:"a shadow moving against the light",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 4, and its trace number is 487.",
    clue:"Find the only light that does not pulse. Fragment index: 487.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The air grows still, waiting for another choice.",
    reward:"a sealed memory"
  },
  {
    id:488,
    name:"Behind the Winter Library · 0488",
    region:"Lantern Expanse",
    signal:"a distant bell with no echo",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 5, and its trace number is 488.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 488.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a clearer signal"
  },
  {
    id:489,
    name:"Within the Winter Library · 0489",
    region:"Pale Engine",
    signal:"a hum that follows silence",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 6, and its trace number is 489.",
    clue:"The safest route is not always the shortest. Fragment index: 489.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The echo returns with one extra note.",
    reward:"a changed landmark"
  },
  {
    id:490,
    name:"At the edge of the Winter Library · 0490",
    region:"Frostline",
    signal:"a warm line beneath the stone",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 7, and its trace number is 490.",
    clue:"Your previous route is the map for this one. Fragment index: 490.",
    lesson:"Memory is more than a record of where you went.",
    response:"The ground glows for a moment, then settles.",
    reward:"a hidden passage"
  },
  {
    id:491,
    name:"Where the Winter Library · 0491",
    region:"Last Horizon",
    signal:"a distant bell with no echo",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 1, and its trace number is 491.",
    clue:"Move once, pause once, then listen again. Fragment index: 491.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A new mark appears beside your last footprint.",
    reward:"a second chance"
  },
  {
    id:492,
    name:"Before the Winter Library · 0492",
    region:"Glasswater Basin",
    signal:"a hum that follows silence",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 2, and its trace number is 492.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 492.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a path that remembers"
  },
  {
    id:493,
    name:"After the Winter Library · 0493",
    region:"Blue Divide",
    signal:"a warm line beneath the stone",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 3, and its trace number is 493.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 493.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"an echo token"
  },
  {
    id:494,
    name:"Between the Winter Library · 0494",
    region:"Ember Archive",
    signal:"a pale mark that shifts position",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 4, and its trace number is 494.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 494.",
    lesson:"Memory is more than a record of where you went.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a sealed memory"
  },
  {
    id:495,
    name:"Above the Winter Library · 0495",
    region:"Echo Marsh",
    signal:"a small star below the horizon",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 5, and its trace number is 495.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 495.",
    lesson:"Silence is information when you learn to listen.",
    response:"The horizon brightens where your route bends.",
    reward:"a clearer signal"
  },
  {
    id:496,
    name:"Below the Winter Library · 0496",
    region:"Last Horizon",
    signal:"three notes with no source",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 6, and its trace number is 496.",
    clue:"Return to the place where the floor changes colour. Fragment index: 496.",
    lesson:"Returning is not the same as repeating.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a changed landmark"
  },
  {
    id:497,
    name:"The Obsidian Pool · 0497",
    region:"Glasswater Basin",
    signal:"a slow rhythm under the wind",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 7, and its trace number is 497.",
    clue:"The answer is stored in the order of your choices. Fragment index: 497.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A distant light answers with one measured flash.",
    reward:"a hidden passage"
  },
  {
    id:498,
    name:"A Obsidian Pool · 0498",
    region:"Blue Divide",
    signal:"a small star below the horizon",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 1, and its trace number is 498.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 498.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The path behind you quietly changes its shape.",
    reward:"a second chance"
  },
  {
    id:499,
    name:"Beneath the Obsidian Pool · 0499",
    region:"Ember Archive",
    signal:"three notes with no source",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 2, and its trace number is 499.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 499.",
    lesson:"Silence is information when you learn to listen.",
    response:"The air grows still, waiting for another choice.",
    reward:"a path that remembers"
  },
  {
    id:500,
    name:"Beyond the Obsidian Pool · 0500",
    region:"Echo Marsh",
    signal:"a slow rhythm under the wind",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 3, and its trace number is 500.",
    clue:"Find the only light that does not pulse. Fragment index: 500.",
    lesson:"Returning is not the same as repeating.",
    response:"A small opening appears in the wall of darkness.",
    reward:"an echo token"
  },
  {
    id:501,
    name:"Inside the Obsidian Pool · 0501",
    region:"Mirror Waste",
    signal:"a breath behind the wall",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 4, and its trace number is 501.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 501.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The echo returns with one extra note.",
    reward:"a stored reflection"
  },
  {
    id:502,
    name:"Under the Obsidian Pool · 0502",
    region:"Quiet Reach",
    signal:"a low blue pulse",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 5, and its trace number is 502.",
    clue:"The safest route is not always the shortest. Fragment index: 502.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The ground glows for a moment, then settles.",
    reward:"a new depth"
  },
  {
    id:503,
    name:"Across the Obsidian Pool · 0503",
    region:"Moss Quarter",
    signal:"a ripple crossing dry ground",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 6, and its trace number is 503.",
    clue:"Your previous route is the map for this one. Fragment index: 503.",
    lesson:"Silence is information when you learn to listen.",
    response:"A new mark appears beside your last footprint.",
    reward:"a quiet clue"
  },
  {
    id:504,
    name:"Behind the Obsidian Pool · 0504",
    region:"Hollow Canopy",
    signal:"a pattern of footprints facing inward",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 7, and its trace number is 504.",
    clue:"Move once, pause once, then listen again. Fragment index: 504.",
    lesson:"Returning is not the same as repeating.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a memory fragment"
  },
  {
    id:505,
    name:"Within the Obsidian Pool · 0505",
    region:"Lantern Expanse",
    signal:"a low blue pulse",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 1, and its trace number is 505.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 505.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a map trace"
  },
  {
    id:506,
    name:"At the edge of the Obsidian Pool · 0506",
    region:"Pale Engine",
    signal:"a ripple crossing dry ground",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 2, and its trace number is 506.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 506.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a sealed memory"
  },
  {
    id:507,
    name:"Where the Obsidian Pool · 0507",
    region:"Quiet Reach",
    signal:"a pattern of footprints facing inward",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 3, and its trace number is 507.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 507.",
    lesson:"Silence is information when you learn to listen.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a clearer signal"
  },
  {
    id:508,
    name:"Before the Obsidian Pool · 0508",
    region:"Moss Quarter",
    signal:"a glow hidden inside a crack",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 4, and its trace number is 508.",
    clue:"A repeated step can open a door, but only once. Fragment index: 508.",
    lesson:"Returning is not the same as repeating.",
    response:"A distant light answers with one measured flash.",
    reward:"a changed landmark"
  },
  {
    id:509,
    name:"After the Obsidian Pool · 0509",
    region:"Hollow Canopy",
    signal:"a door-shaped gap in the air",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 5, and its trace number is 509.",
    clue:"The second path is real only after you turn away. Fragment index: 509.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The path behind you quietly changes its shape.",
    reward:"a hidden passage"
  },
  {
    id:510,
    name:"Between the Obsidian Pool · 0510",
    region:"Lantern Expanse",
    signal:"a thin thread of silver light",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 6, and its trace number is 510.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 510.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The air grows still, waiting for another choice.",
    reward:"a second chance"
  },
  {
    id:511,
    name:"Above the Obsidian Pool · 0511",
    region:"Pale Engine",
    signal:"a reflection that arrives late",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 7, and its trace number is 511.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 511.",
    lesson:"Silence is information when you learn to listen.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a path that remembers"
  },
  {
    id:512,
    name:"Below the Obsidian Pool · 0512",
    region:"Frostline",
    signal:"a door-shaped gap in the air",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 1, and its trace number is 512.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 512.",
    lesson:"Returning is not the same as repeating.",
    response:"The echo returns with one extra note.",
    reward:"an echo token"
  },
  {
    id:513,
    name:"The Soft Thunder · 0513",
    region:"Last Horizon",
    signal:"a thin thread of silver light",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 2, and its trace number is 513.",
    clue:"Find the only light that does not pulse. Fragment index: 513.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The ground glows for a moment, then settles.",
    reward:"a stored reflection"
  },
  {
    id:514,
    name:"A Soft Thunder · 0514",
    region:"Glasswater Basin",
    signal:"a reflection that arrives late",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 3, and its trace number is 514.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 514.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A new mark appears beside your last footprint.",
    reward:"a new depth"
  },
  {
    id:515,
    name:"Beneath the Soft Thunder · 0515",
    region:"Blue Divide",
    signal:"a shadow moving against the light",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 4, and its trace number is 515.",
    clue:"The safest route is not always the shortest. Fragment index: 515.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a quiet clue"
  },
  {
    id:516,
    name:"Beyond the Soft Thunder · 0516",
    region:"Ember Archive",
    signal:"a distant bell with no echo",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 5, and its trace number is 516.",
    clue:"Your previous route is the map for this one. Fragment index: 516.",
    lesson:"Observation can be a form of movement.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a memory fragment"
  },
  {
    id:517,
    name:"Inside the Soft Thunder · 0517",
    region:"Echo Marsh",
    signal:"a hum that follows silence",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 6, and its trace number is 517.",
    clue:"Move once, pause once, then listen again. Fragment index: 517.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a map trace"
  },
  {
    id:518,
    name:"Under the Soft Thunder · 0518",
    region:"Last Horizon",
    signal:"a warm line beneath the stone",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 7, and its trace number is 518.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 518.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The horizon brightens where your route bends.",
    reward:"a sealed memory"
  },
  {
    id:519,
    name:"Across the Soft Thunder · 0519",
    region:"Glasswater Basin",
    signal:"a distant bell with no echo",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 1, and its trace number is 519.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 519.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a clearer signal"
  },
  {
    id:520,
    name:"Behind the Soft Thunder · 0520",
    region:"Blue Divide",
    signal:"a hum that follows silence",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 2, and its trace number is 520.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 520.",
    lesson:"Observation can be a form of movement.",
    response:"A distant light answers with one measured flash.",
    reward:"a changed landmark"
  },
  {
    id:521,
    name:"Within the Soft Thunder · 0521",
    region:"Ember Archive",
    signal:"a warm line beneath the stone",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 3, and its trace number is 521.",
    clue:"A repeated step can open a door, but only once. Fragment index: 521.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The path behind you quietly changes its shape.",
    reward:"a hidden passage"
  },
  {
    id:522,
    name:"At the edge of the Soft Thunder · 0522",
    region:"Echo Marsh",
    signal:"a pale mark that shifts position",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 4, and its trace number is 522.",
    clue:"The second path is real only after you turn away. Fragment index: 522.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The air grows still, waiting for another choice.",
    reward:"a second chance"
  },
  {
    id:523,
    name:"Where the Soft Thunder · 0523",
    region:"Mirror Waste",
    signal:"a small star below the horizon",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 5, and its trace number is 523.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 523.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a memory fragment"
  },
  {
    id:524,
    name:"Before the Soft Thunder · 0524",
    region:"Quiet Reach",
    signal:"three notes with no source",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 6, and its trace number is 524.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 524.",
    lesson:"Observation can be a form of movement.",
    response:"The echo returns with one extra note.",
    reward:"a map trace"
  },
  {
    id:525,
    name:"After the Soft Thunder · 0525",
    region:"Moss Quarter",
    signal:"a slow rhythm under the wind",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 7, and its trace number is 525.",
    clue:"Return to the place where the floor changes colour. Fragment index: 525.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The ground glows for a moment, then settles.",
    reward:"a sealed memory"
  },
  {
    id:526,
    name:"Between the Soft Thunder · 0526",
    region:"Hollow Canopy",
    signal:"a small star below the horizon",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 1, and its trace number is 526.",
    clue:"The answer is stored in the order of your choices. Fragment index: 526.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A new mark appears beside your last footprint.",
    reward:"a clearer signal"
  },
  {
    id:527,
    name:"Above the Soft Thunder · 0527",
    region:"Lantern Expanse",
    signal:"three notes with no source",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 2, and its trace number is 527.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 527.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a changed landmark"
  },
  {
    id:528,
    name:"Below the Soft Thunder · 0528",
    region:"Pale Engine",
    signal:"a slow rhythm under the wind",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 3, and its trace number is 528.",
    clue:"The safest route is not always the shortest. Fragment index: 528.",
    lesson:"Observation can be a form of movement.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a hidden passage"
  },
  {
    id:529,
    name:"The Amber Corridor · 0529",
    region:"Quiet Reach",
    signal:"a breath behind the wall",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 4, and its trace number is 529.",
    clue:"Your previous route is the map for this one. Fragment index: 529.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a second chance"
  },
  {
    id:530,
    name:"A Amber Corridor · 0530",
    region:"Moss Quarter",
    signal:"a low blue pulse",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 5, and its trace number is 530.",
    clue:"Move once, pause once, then listen again. Fragment index: 530.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a path that remembers"
  },
  {
    id:531,
    name:"Beneath the Amber Corridor · 0531",
    region:"Hollow Canopy",
    signal:"a ripple crossing dry ground",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 6, and its trace number is 531.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 531.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A distant light answers with one measured flash.",
    reward:"an echo token"
  },
  {
    id:532,
    name:"Beyond the Amber Corridor · 0532",
    region:"Lantern Expanse",
    signal:"a pattern of footprints facing inward",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 7, and its trace number is 532.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 532.",
    lesson:"Observation can be a form of movement.",
    response:"The path behind you quietly changes its shape.",
    reward:"a stored reflection"
  },
  {
    id:533,
    name:"Inside the Amber Corridor · 0533",
    region:"Pale Engine",
    signal:"a low blue pulse",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 1, and its trace number is 533.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 533.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The air grows still, waiting for another choice.",
    reward:"a new depth"
  },
  {
    id:534,
    name:"Under the Amber Corridor · 0534",
    region:"Frostline",
    signal:"a ripple crossing dry ground",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 2, and its trace number is 534.",
    clue:"A repeated step can open a door, but only once. Fragment index: 534.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a quiet clue"
  },
  {
    id:535,
    name:"Across the Amber Corridor · 0535",
    region:"Last Horizon",
    signal:"a pattern of footprints facing inward",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 3, and its trace number is 535.",
    clue:"The second path is real only after you turn away. Fragment index: 535.",
    lesson:"Memory is more than a record of where you went.",
    response:"The echo returns with one extra note.",
    reward:"a memory fragment"
  },
  {
    id:536,
    name:"Behind the Amber Corridor · 0536",
    region:"Glasswater Basin",
    signal:"a glow hidden inside a crack",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 4, and its trace number is 536.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 536.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The ground glows for a moment, then settles.",
    reward:"a map trace"
  },
  {
    id:537,
    name:"Within the Amber Corridor · 0537",
    region:"Blue Divide",
    signal:"a door-shaped gap in the air",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 5, and its trace number is 537.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 537.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A new mark appears beside your last footprint.",
    reward:"a sealed memory"
  },
  {
    id:538,
    name:"At the edge of the Amber Corridor · 0538",
    region:"Ember Archive",
    signal:"a thin thread of silver light",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 6, and its trace number is 538.",
    clue:"Return to the place where the floor changes colour. Fragment index: 538.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a clearer signal"
  },
  {
    id:539,
    name:"Where the Amber Corridor · 0539",
    region:"Echo Marsh",
    signal:"a reflection that arrives late",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 7, and its trace number is 539.",
    clue:"The answer is stored in the order of your choices. Fragment index: 539.",
    lesson:"Memory is more than a record of where you went.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a changed landmark"
  },
  {
    id:540,
    name:"Before the Amber Corridor · 0540",
    region:"Last Horizon",
    signal:"a door-shaped gap in the air",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 1, and its trace number is 540.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 540.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a hidden passage"
  },
  {
    id:541,
    name:"After the Amber Corridor · 0541",
    region:"Glasswater Basin",
    signal:"a thin thread of silver light",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 2, and its trace number is 541.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 541.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The horizon brightens where your route bends.",
    reward:"a second chance"
  },
  {
    id:542,
    name:"Between the Amber Corridor · 0542",
    region:"Blue Divide",
    signal:"a reflection that arrives late",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 3, and its trace number is 542.",
    clue:"Find the only light that does not pulse. Fragment index: 542.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a path that remembers"
  },
  {
    id:543,
    name:"Above the Amber Corridor · 0543",
    region:"Ember Archive",
    signal:"a shadow moving against the light",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 4, and its trace number is 543.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 543.",
    lesson:"Memory is more than a record of where you went.",
    response:"A distant light answers with one measured flash.",
    reward:"an echo token"
  },
  {
    id:544,
    name:"Below the Amber Corridor · 0544",
    region:"Echo Marsh",
    signal:"a distant bell with no echo",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 5, and its trace number is 544.",
    clue:"The safest route is not always the shortest. Fragment index: 544.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The path behind you quietly changes its shape.",
    reward:"a stored reflection"
  },
  {
    id:545,
    name:"The Cloud Vault · 0545",
    region:"Mirror Waste",
    signal:"a hum that follows silence",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 6, and its trace number is 545.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 545.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The air grows still, waiting for another choice.",
    reward:"a new depth"
  },
  {
    id:546,
    name:"A Cloud Vault · 0546",
    region:"Quiet Reach",
    signal:"a warm line beneath the stone",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 7, and its trace number is 546.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 546.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a quiet clue"
  },
  {
    id:547,
    name:"Beneath the Cloud Vault · 0547",
    region:"Moss Quarter",
    signal:"a distant bell with no echo",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 1, and its trace number is 547.",
    clue:"A repeated step can open a door, but only once. Fragment index: 547.",
    lesson:"Memory is more than a record of where you went.",
    response:"The echo returns with one extra note.",
    reward:"a memory fragment"
  },
  {
    id:548,
    name:"Beyond the Cloud Vault · 0548",
    region:"Hollow Canopy",
    signal:"a hum that follows silence",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 2, and its trace number is 548.",
    clue:"The second path is real only after you turn away. Fragment index: 548.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The ground glows for a moment, then settles.",
    reward:"a map trace"
  },
  {
    id:549,
    name:"Inside the Cloud Vault · 0549",
    region:"Lantern Expanse",
    signal:"a warm line beneath the stone",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 3, and its trace number is 549.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 549.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A new mark appears beside your last footprint.",
    reward:"a sealed memory"
  },
  {
    id:550,
    name:"Under the Cloud Vault · 0550",
    region:"Pale Engine",
    signal:"a pale mark that shifts position",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 4, and its trace number is 550.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 550.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a clearer signal"
  },
  {
    id:551,
    name:"Across the Cloud Vault · 0551",
    region:"Quiet Reach",
    signal:"a small star below the horizon",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 5, and its trace number is 551.",
    clue:"Return to the place where the floor changes colour. Fragment index: 551.",
    lesson:"Memory is more than a record of where you went.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a changed landmark"
  },
  {
    id:552,
    name:"Behind the Cloud Vault · 0552",
    region:"Moss Quarter",
    signal:"three notes with no source",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 6, and its trace number is 552.",
    clue:"The answer is stored in the order of your choices. Fragment index: 552.",
    lesson:"Silence is information when you learn to listen.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a new depth"
  },
  {
    id:553,
    name:"Within the Cloud Vault · 0553",
    region:"Hollow Canopy",
    signal:"a slow rhythm under the wind",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 7, and its trace number is 553.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 553.",
    lesson:"Returning is not the same as repeating.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a quiet clue"
  },
  {
    id:554,
    name:"At the edge of the Cloud Vault · 0554",
    region:"Lantern Expanse",
    signal:"a small star below the horizon",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 1, and its trace number is 554.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 554.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A distant light answers with one measured flash.",
    reward:"a memory fragment"
  },
  {
    id:555,
    name:"Where the Cloud Vault · 0555",
    region:"Pale Engine",
    signal:"three notes with no source",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 2, and its trace number is 555.",
    clue:"Find the only light that does not pulse. Fragment index: 555.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The path behind you quietly changes its shape.",
    reward:"a map trace"
  },
  {
    id:556,
    name:"Before the Cloud Vault · 0556",
    region:"Frostline",
    signal:"a slow rhythm under the wind",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 3, and its trace number is 556.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 556.",
    lesson:"Silence is information when you learn to listen.",
    response:"The air grows still, waiting for another choice.",
    reward:"a sealed memory"
  },
  {
    id:557,
    name:"After the Cloud Vault · 0557",
    region:"Last Horizon",
    signal:"a breath behind the wall",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 4, and its trace number is 557.",
    clue:"The safest route is not always the shortest. Fragment index: 557.",
    lesson:"Returning is not the same as repeating.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a clearer signal"
  },
  {
    id:558,
    name:"Between the Cloud Vault · 0558",
    region:"Glasswater Basin",
    signal:"a low blue pulse",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 5, and its trace number is 558.",
    clue:"Your previous route is the map for this one. Fragment index: 558.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The echo returns with one extra note.",
    reward:"a changed landmark"
  },
  {
    id:559,
    name:"Above the Cloud Vault · 0559",
    region:"Blue Divide",
    signal:"a ripple crossing dry ground",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 6, and its trace number is 559.",
    clue:"Move once, pause once, then listen again. Fragment index: 559.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The ground glows for a moment, then settles.",
    reward:"a hidden passage"
  },
  {
    id:560,
    name:"Below the Cloud Vault · 0560",
    region:"Ember Archive",
    signal:"a pattern of footprints facing inward",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 7, and its trace number is 560.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 560.",
    lesson:"Silence is information when you learn to listen.",
    response:"A new mark appears beside your last footprint.",
    reward:"a second chance"
  },
  {
    id:561,
    name:"The Drifting City · 0561",
    region:"Echo Marsh",
    signal:"a low blue pulse",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 1, and its trace number is 561.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 561.",
    lesson:"Returning is not the same as repeating.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a path that remembers"
  },
  {
    id:562,
    name:"A Drifting City · 0562",
    region:"Last Horizon",
    signal:"a ripple crossing dry ground",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 2, and its trace number is 562.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 562.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"an echo token"
  },
  {
    id:563,
    name:"Beneath the Drifting City · 0563",
    region:"Glasswater Basin",
    signal:"a pattern of footprints facing inward",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 3, and its trace number is 563.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 563.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a stored reflection"
  },
  {
    id:564,
    name:"Beyond the Drifting City · 0564",
    region:"Blue Divide",
    signal:"a glow hidden inside a crack",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 4, and its trace number is 564.",
    clue:"Return to the place where the floor changes colour. Fragment index: 564.",
    lesson:"Silence is information when you learn to listen.",
    response:"The horizon brightens where your route bends.",
    reward:"a new depth"
  },
  {
    id:565,
    name:"Inside the Drifting City · 0565",
    region:"Ember Archive",
    signal:"a door-shaped gap in the air",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 5, and its trace number is 565.",
    clue:"The answer is stored in the order of your choices. Fragment index: 565.",
    lesson:"Returning is not the same as repeating.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a quiet clue"
  },
  {
    id:566,
    name:"Under the Drifting City · 0566",
    region:"Echo Marsh",
    signal:"a thin thread of silver light",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 6, and its trace number is 566.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 566.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A distant light answers with one measured flash.",
    reward:"a memory fragment"
  },
  {
    id:567,
    name:"Across the Drifting City · 0567",
    region:"Mirror Waste",
    signal:"a reflection that arrives late",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 7, and its trace number is 567.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 567.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The path behind you quietly changes its shape.",
    reward:"a map trace"
  },
  {
    id:568,
    name:"Behind the Drifting City · 0568",
    region:"Quiet Reach",
    signal:"a door-shaped gap in the air",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 1, and its trace number is 568.",
    clue:"Find the only light that does not pulse. Fragment index: 568.",
    lesson:"Silence is information when you learn to listen.",
    response:"The air grows still, waiting for another choice.",
    reward:"a sealed memory"
  },
  {
    id:569,
    name:"Within the Drifting City · 0569",
    region:"Moss Quarter",
    signal:"a thin thread of silver light",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 2, and its trace number is 569.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 569.",
    lesson:"Returning is not the same as repeating.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a clearer signal"
  },
  {
    id:570,
    name:"At the edge of the Drifting City · 0570",
    region:"Hollow Canopy",
    signal:"a reflection that arrives late",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 3, and its trace number is 570.",
    clue:"The safest route is not always the shortest. Fragment index: 570.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The echo returns with one extra note.",
    reward:"a changed landmark"
  },
  {
    id:571,
    name:"Where the Drifting City · 0571",
    region:"Lantern Expanse",
    signal:"a shadow moving against the light",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 4, and its trace number is 571.",
    clue:"Your previous route is the map for this one. Fragment index: 571.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The ground glows for a moment, then settles.",
    reward:"a hidden passage"
  },
  {
    id:572,
    name:"Before the Drifting City · 0572",
    region:"Pale Engine",
    signal:"a distant bell with no echo",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 5, and its trace number is 572.",
    clue:"Move once, pause once, then listen again. Fragment index: 572.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A new mark appears beside your last footprint.",
    reward:"a second chance"
  },
  {
    id:573,
    name:"After the Drifting City · 0573",
    region:"Quiet Reach",
    signal:"a hum that follows silence",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 6, and its trace number is 573.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 573.",
    lesson:"Observation can be a form of movement.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a path that remembers"
  },
  {
    id:574,
    name:"Between the Drifting City · 0574",
    region:"Moss Quarter",
    signal:"a warm line beneath the stone",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 7, and its trace number is 574.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 574.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"an echo token"
  },
  {
    id:575,
    name:"Above the Drifting City · 0575",
    region:"Hollow Canopy",
    signal:"a distant bell with no echo",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 1, and its trace number is 575.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 575.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a stored reflection"
  },
  {
    id:576,
    name:"Below the Drifting City · 0576",
    region:"Lantern Expanse",
    signal:"a hum that follows silence",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 2, and its trace number is 576.",
    clue:"A repeated step can open a door, but only once. Fragment index: 576.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a new depth"
  },
  {
    id:577,
    name:"The Ivory Tunnel · 0577",
    region:"Pale Engine",
    signal:"a warm line beneath the stone",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 3, and its trace number is 577.",
    clue:"The second path is real only after you turn away. Fragment index: 577.",
    lesson:"Observation can be a form of movement.",
    response:"A distant light answers with one measured flash.",
    reward:"a quiet clue"
  },
  {
    id:578,
    name:"A Ivory Tunnel · 0578",
    region:"Frostline",
    signal:"a pale mark that shifts position",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 4, and its trace number is 578.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 578.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The path behind you quietly changes its shape.",
    reward:"a memory fragment"
  },
  {
    id:579,
    name:"Beneath the Ivory Tunnel · 0579",
    region:"Last Horizon",
    signal:"a small star below the horizon",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 5, and its trace number is 579.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 579.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The air grows still, waiting for another choice.",
    reward:"a map trace"
  },
  {
    id:580,
    name:"Beyond the Ivory Tunnel · 0580",
    region:"Glasswater Basin",
    signal:"three notes with no source",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 6, and its trace number is 580.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 580.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a sealed memory"
  },
  {
    id:581,
    name:"Inside the Ivory Tunnel · 0581",
    region:"Blue Divide",
    signal:"a slow rhythm under the wind",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 7, and its trace number is 581.",
    clue:"Find the only light that does not pulse. Fragment index: 581.",
    lesson:"Observation can be a form of movement.",
    response:"The echo returns with one extra note.",
    reward:"an echo token"
  },
  {
    id:582,
    name:"Under the Ivory Tunnel · 0582",
    region:"Ember Archive",
    signal:"a small star below the horizon",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 1, and its trace number is 582.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 582.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The ground glows for a moment, then settles.",
    reward:"a stored reflection"
  },
  {
    id:583,
    name:"Across the Ivory Tunnel · 0583",
    region:"Echo Marsh",
    signal:"three notes with no source",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 2, and its trace number is 583.",
    clue:"The safest route is not always the shortest. Fragment index: 583.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A new mark appears beside your last footprint.",
    reward:"a new depth"
  },
  {
    id:584,
    name:"Behind the Ivory Tunnel · 0584",
    region:"Last Horizon",
    signal:"a slow rhythm under the wind",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 3, and its trace number is 584.",
    clue:"Your previous route is the map for this one. Fragment index: 584.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a quiet clue"
  },
  {
    id:585,
    name:"Within the Ivory Tunnel · 0585",
    region:"Glasswater Basin",
    signal:"a breath behind the wall",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 4, and its trace number is 585.",
    clue:"Move once, pause once, then listen again. Fragment index: 585.",
    lesson:"Observation can be a form of movement.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a memory fragment"
  },
  {
    id:586,
    name:"At the edge of the Ivory Tunnel · 0586",
    region:"Blue Divide",
    signal:"a low blue pulse",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 5, and its trace number is 586.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 586.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a map trace"
  },
  {
    id:587,
    name:"Where the Ivory Tunnel · 0587",
    region:"Ember Archive",
    signal:"a ripple crossing dry ground",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 6, and its trace number is 587.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 587.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The horizon brightens where your route bends.",
    reward:"a sealed memory"
  },
  {
    id:588,
    name:"Before the Ivory Tunnel · 0588",
    region:"Echo Marsh",
    signal:"a pattern of footprints facing inward",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 7, and its trace number is 588.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 588.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a clearer signal"
  },
  {
    id:589,
    name:"After the Ivory Tunnel · 0589",
    region:"Mirror Waste",
    signal:"a low blue pulse",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 1, and its trace number is 589.",
    clue:"A repeated step can open a door, but only once. Fragment index: 589.",
    lesson:"Observation can be a form of movement.",
    response:"A distant light answers with one measured flash.",
    reward:"a changed landmark"
  },
  {
    id:590,
    name:"Between the Ivory Tunnel · 0590",
    region:"Quiet Reach",
    signal:"a ripple crossing dry ground",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 2, and its trace number is 590.",
    clue:"The second path is real only after you turn away. Fragment index: 590.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The path behind you quietly changes its shape.",
    reward:"a hidden passage"
  },
  {
    id:591,
    name:"Above the Ivory Tunnel · 0591",
    region:"Moss Quarter",
    signal:"a pattern of footprints facing inward",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 3, and its trace number is 591.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 591.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The air grows still, waiting for another choice.",
    reward:"a second chance"
  },
  {
    id:592,
    name:"Below the Ivory Tunnel · 0592",
    region:"Hollow Canopy",
    signal:"a glow hidden inside a crack",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 4, and its trace number is 592.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 592.",
    lesson:"Memory is more than a record of where you went.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a path that remembers"
  },
  {
    id:593,
    name:"The Cinder Meadow · 0593",
    region:"Lantern Expanse",
    signal:"a door-shaped gap in the air",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 5, and its trace number is 593.",
    clue:"Return to the place where the floor changes colour. Fragment index: 593.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The echo returns with one extra note.",
    reward:"an echo token"
  },
  {
    id:594,
    name:"A Cinder Meadow · 0594",
    region:"Pale Engine",
    signal:"a thin thread of silver light",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 6, and its trace number is 594.",
    clue:"The answer is stored in the order of your choices. Fragment index: 594.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The ground glows for a moment, then settles.",
    reward:"a stored reflection"
  },
  {
    id:595,
    name:"Beneath the Cinder Meadow · 0595",
    region:"Quiet Reach",
    signal:"a reflection that arrives late",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 7, and its trace number is 595.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 595.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A new mark appears beside your last footprint.",
    reward:"a new depth"
  },
  {
    id:596,
    name:"Beyond the Cinder Meadow · 0596",
    region:"Moss Quarter",
    signal:"a door-shaped gap in the air",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 1, and its trace number is 596.",
    clue:"The safest route is not always the shortest. Fragment index: 596.",
    lesson:"Memory is more than a record of where you went.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a quiet clue"
  },
  {
    id:597,
    name:"Inside the Cinder Meadow · 0597",
    region:"Hollow Canopy",
    signal:"a thin thread of silver light",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 2, and its trace number is 597.",
    clue:"Your previous route is the map for this one. Fragment index: 597.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a memory fragment"
  },
  {
    id:598,
    name:"Under the Cinder Meadow · 0598",
    region:"Lantern Expanse",
    signal:"a reflection that arrives late",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 3, and its trace number is 598.",
    clue:"Move once, pause once, then listen again. Fragment index: 598.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a map trace"
  },
  {
    id:599,
    name:"Across the Cinder Meadow · 0599",
    region:"Pale Engine",
    signal:"a shadow moving against the light",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 4, and its trace number is 599.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 599.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a sealed memory"
  },
  {
    id:600,
    name:"Behind the Cinder Meadow · 0600",
    region:"Frostline",
    signal:"a distant bell with no echo",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 5, and its trace number is 600.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 600.",
    lesson:"Memory is more than a record of where you went.",
    response:"A distant light answers with one measured flash.",
    reward:"a clearer signal"
  },
  {
    id:601,
    name:"Within the Cinder Meadow · 0601",
    region:"Last Horizon",
    signal:"a hum that follows silence",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 6, and its trace number is 601.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 601.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The path behind you quietly changes its shape.",
    reward:"a changed landmark"
  },
  {
    id:602,
    name:"At the edge of the Cinder Meadow · 0602",
    region:"Glasswater Basin",
    signal:"a warm line beneath the stone",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 7, and its trace number is 602.",
    clue:"A repeated step can open a door, but only once. Fragment index: 602.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The air grows still, waiting for another choice.",
    reward:"a hidden passage"
  },
  {
    id:603,
    name:"Where the Cinder Meadow · 0603",
    region:"Blue Divide",
    signal:"a distant bell with no echo",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 1, and its trace number is 603.",
    clue:"The second path is real only after you turn away. Fragment index: 603.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a second chance"
  },
  {
    id:604,
    name:"Before the Cinder Meadow · 0604",
    region:"Ember Archive",
    signal:"a hum that follows silence",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 2, and its trace number is 604.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 604.",
    lesson:"Memory is more than a record of where you went.",
    response:"The echo returns with one extra note.",
    reward:"a path that remembers"
  },
  {
    id:605,
    name:"After the Cinder Meadow · 0605",
    region:"Echo Marsh",
    signal:"a warm line beneath the stone",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 3, and its trace number is 605.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 605.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The ground glows for a moment, then settles.",
    reward:"an echo token"
  },
  {
    id:606,
    name:"Between the Cinder Meadow · 0606",
    region:"Last Horizon",
    signal:"a pale mark that shifts position",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 4, and its trace number is 606.",
    clue:"Return to the place where the floor changes colour. Fragment index: 606.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A new mark appears beside your last footprint.",
    reward:"a stored reflection"
  },
  {
    id:607,
    name:"Above the Cinder Meadow · 0607",
    region:"Glasswater Basin",
    signal:"a small star below the horizon",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 5, and its trace number is 607.",
    clue:"The answer is stored in the order of your choices. Fragment index: 607.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a new depth"
  },
  {
    id:608,
    name:"Below the Cinder Meadow · 0608",
    region:"Blue Divide",
    signal:"three notes with no source",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 6, and its trace number is 608.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 608.",
    lesson:"Memory is more than a record of where you went.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a quiet clue"
  },
  {
    id:609,
    name:"The Sapphire Gate · 0609",
    region:"Ember Archive",
    signal:"a slow rhythm under the wind",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 7, and its trace number is 609.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 609.",
    lesson:"Silence is information when you learn to listen.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a memory fragment"
  },
  {
    id:610,
    name:"A Sapphire Gate · 0610",
    region:"Echo Marsh",
    signal:"a small star below the horizon",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 1, and its trace number is 610.",
    clue:"Find the only light that does not pulse. Fragment index: 610.",
    lesson:"Returning is not the same as repeating.",
    response:"The horizon brightens where your route bends.",
    reward:"a second chance"
  },
  {
    id:611,
    name:"Beneath the Sapphire Gate · 0611",
    region:"Mirror Waste",
    signal:"three notes with no source",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 2, and its trace number is 611.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 611.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a path that remembers"
  },
  {
    id:612,
    name:"Beyond the Sapphire Gate · 0612",
    region:"Quiet Reach",
    signal:"a slow rhythm under the wind",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 3, and its trace number is 612.",
    clue:"The safest route is not always the shortest. Fragment index: 612.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A distant light answers with one measured flash.",
    reward:"an echo token"
  },
  {
    id:613,
    name:"Inside the Sapphire Gate · 0613",
    region:"Moss Quarter",
    signal:"a breath behind the wall",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 4, and its trace number is 613.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 613.",
    lesson:"Silence is information when you learn to listen.",
    response:"The path behind you quietly changes its shape.",
    reward:"a stored reflection"
  },
  {
    id:614,
    name:"Under the Sapphire Gate · 0614",
    region:"Hollow Canopy",
    signal:"a low blue pulse",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 5, and its trace number is 614.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 614.",
    lesson:"Returning is not the same as repeating.",
    response:"The air grows still, waiting for another choice.",
    reward:"a new depth"
  },
  {
    id:615,
    name:"Across the Sapphire Gate · 0615",
    region:"Lantern Expanse",
    signal:"a ripple crossing dry ground",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 6, and its trace number is 615.",
    clue:"A repeated step can open a door, but only once. Fragment index: 615.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a quiet clue"
  },
  {
    id:616,
    name:"Behind the Sapphire Gate · 0616",
    region:"Pale Engine",
    signal:"a pattern of footprints facing inward",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 7, and its trace number is 616.",
    clue:"The second path is real only after you turn away. Fragment index: 616.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The echo returns with one extra note.",
    reward:"a memory fragment"
  },
  {
    id:617,
    name:"Within the Sapphire Gate · 0617",
    region:"Quiet Reach",
    signal:"a low blue pulse",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 1, and its trace number is 617.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 617.",
    lesson:"Silence is information when you learn to listen.",
    response:"The ground glows for a moment, then settles.",
    reward:"a map trace"
  },
  {
    id:618,
    name:"At the edge of the Sapphire Gate · 0618",
    region:"Moss Quarter",
    signal:"a ripple crossing dry ground",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 2, and its trace number is 618.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 618.",
    lesson:"Returning is not the same as repeating.",
    response:"A new mark appears beside your last footprint.",
    reward:"a sealed memory"
  },
  {
    id:619,
    name:"Where the Sapphire Gate · 0619",
    region:"Hollow Canopy",
    signal:"a pattern of footprints facing inward",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 3, and its trace number is 619.",
    clue:"Return to the place where the floor changes colour. Fragment index: 619.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a clearer signal"
  },
  {
    id:620,
    name:"Before the Sapphire Gate · 0620",
    region:"Lantern Expanse",
    signal:"a glow hidden inside a crack",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 4, and its trace number is 620.",
    clue:"The answer is stored in the order of your choices. Fragment index: 620.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a changed landmark"
  },
  {
    id:621,
    name:"After the Sapphire Gate · 0621",
    region:"Pale Engine",
    signal:"a door-shaped gap in the air",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 5, and its trace number is 621.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 621.",
    lesson:"Silence is information when you learn to listen.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a hidden passage"
  },
  {
    id:622,
    name:"Between the Sapphire Gate · 0622",
    region:"Frostline",
    signal:"a thin thread of silver light",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 6, and its trace number is 622.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 622.",
    lesson:"Returning is not the same as repeating.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a second chance"
  },
  {
    id:623,
    name:"Above the Sapphire Gate · 0623",
    region:"Last Horizon",
    signal:"a reflection that arrives late",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 7, and its trace number is 623.",
    clue:"Find the only light that does not pulse. Fragment index: 623.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A distant light answers with one measured flash.",
    reward:"a path that remembers"
  },
  {
    id:624,
    name:"Below the Sapphire Gate · 0624",
    region:"Glasswater Basin",
    signal:"a door-shaped gap in the air",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 1, and its trace number is 624.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 624.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The path behind you quietly changes its shape.",
    reward:"an echo token"
  },
  {
    id:625,
    name:"The Unknown Coast · 0625",
    region:"Blue Divide",
    signal:"a thin thread of silver light",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 2, and its trace number is 625.",
    clue:"The safest route is not always the shortest. Fragment index: 625.",
    lesson:"Silence is information when you learn to listen.",
    response:"The air grows still, waiting for another choice.",
    reward:"a stored reflection"
  },
  {
    id:626,
    name:"A Unknown Coast · 0626",
    region:"Ember Archive",
    signal:"a reflection that arrives late",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 3, and its trace number is 626.",
    clue:"Your previous route is the map for this one. Fragment index: 626.",
    lesson:"Returning is not the same as repeating.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a new depth"
  },
  {
    id:627,
    name:"Beneath the Unknown Coast · 0627",
    region:"Echo Marsh",
    signal:"a shadow moving against the light",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 4, and its trace number is 627.",
    clue:"Move once, pause once, then listen again. Fragment index: 627.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The echo returns with one extra note.",
    reward:"a quiet clue"
  },
  {
    id:628,
    name:"Beyond the Unknown Coast · 0628",
    region:"Last Horizon",
    signal:"a distant bell with no echo",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 5, and its trace number is 628.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 628.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The ground glows for a moment, then settles.",
    reward:"a memory fragment"
  },
  {
    id:629,
    name:"Inside the Unknown Coast · 0629",
    region:"Glasswater Basin",
    signal:"a hum that follows silence",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 6, and its trace number is 629.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 629.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A new mark appears beside your last footprint.",
    reward:"a map trace"
  },
  {
    id:630,
    name:"Under the Unknown Coast · 0630",
    region:"Blue Divide",
    signal:"a warm line beneath the stone",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 7, and its trace number is 630.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 630.",
    lesson:"Observation can be a form of movement.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a sealed memory"
  },
  {
    id:631,
    name:"Across the Unknown Coast · 0631",
    region:"Ember Archive",
    signal:"a distant bell with no echo",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 1, and its trace number is 631.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 631.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a clearer signal"
  },
  {
    id:632,
    name:"Behind the Unknown Coast · 0632",
    region:"Echo Marsh",
    signal:"a hum that follows silence",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 2, and its trace number is 632.",
    clue:"Return to the place where the floor changes colour. Fragment index: 632.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a changed landmark"
  },
  {
    id:633,
    name:"Within the Unknown Coast · 0633",
    region:"Mirror Waste",
    signal:"a warm line beneath the stone",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 3, and its trace number is 633.",
    clue:"The answer is stored in the order of your choices. Fragment index: 633.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The horizon brightens where your route bends.",
    reward:"a hidden passage"
  },
  {
    id:634,
    name:"At the edge of the Unknown Coast · 0634",
    region:"Quiet Reach",
    signal:"a pale mark that shifts position",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 4, and its trace number is 634.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 634.",
    lesson:"Observation can be a form of movement.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a second chance"
  },
  {
    id:635,
    name:"Where the Unknown Coast · 0635",
    region:"Moss Quarter",
    signal:"a small star below the horizon",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 5, and its trace number is 635.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 635.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A distant light answers with one measured flash.",
    reward:"a path that remembers"
  },
  {
    id:636,
    name:"Before the Unknown Coast · 0636",
    region:"Hollow Canopy",
    signal:"three notes with no source",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 6, and its trace number is 636.",
    clue:"Find the only light that does not pulse. Fragment index: 636.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The path behind you quietly changes its shape.",
    reward:"an echo token"
  },
  {
    id:637,
    name:"After the Unknown Coast · 0637",
    region:"Lantern Expanse",
    signal:"a slow rhythm under the wind",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 7, and its trace number is 637.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 637.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The air grows still, waiting for another choice.",
    reward:"a stored reflection"
  },
  {
    id:638,
    name:"Between the Unknown Coast · 0638",
    region:"Pale Engine",
    signal:"a small star below the horizon",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 1, and its trace number is 638.",
    clue:"The safest route is not always the shortest. Fragment index: 638.",
    lesson:"Observation can be a form of movement.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a new depth"
  },
  {
    id:639,
    name:"Above the Unknown Coast · 0639",
    region:"Quiet Reach",
    signal:"three notes with no source",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 2, and its trace number is 639.",
    clue:"Your previous route is the map for this one. Fragment index: 639.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The echo returns with one extra note.",
    reward:"a changed landmark"
  },
  {
    id:640,
    name:"Below the Unknown Coast · 0640",
    region:"Moss Quarter",
    signal:"a slow rhythm under the wind",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 3, and its trace number is 640.",
    clue:"Move once, pause once, then listen again. Fragment index: 640.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The ground glows for a moment, then settles.",
    reward:"a hidden passage"
  },
  {
    id:641,
    name:"The Silent Meridian · 0641",
    region:"Hollow Canopy",
    signal:"a breath behind the wall",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 4, and its trace number is 641.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 641.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A new mark appears beside your last footprint.",
    reward:"a second chance"
  },
  {
    id:642,
    name:"A Silent Meridian · 0642",
    region:"Lantern Expanse",
    signal:"a low blue pulse",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 5, and its trace number is 642.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 642.",
    lesson:"Observation can be a form of movement.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a path that remembers"
  },
  {
    id:643,
    name:"Beneath the Silent Meridian · 0643",
    region:"Pale Engine",
    signal:"a ripple crossing dry ground",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 6, and its trace number is 643.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 643.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"an echo token"
  },
  {
    id:644,
    name:"Beyond the Silent Meridian · 0644",
    region:"Frostline",
    signal:"a pattern of footprints facing inward",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 7, and its trace number is 644.",
    clue:"A repeated step can open a door, but only once. Fragment index: 644.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a stored reflection"
  },
  {
    id:645,
    name:"Inside the Silent Meridian · 0645",
    region:"Last Horizon",
    signal:"a low blue pulse",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 1, and its trace number is 645.",
    clue:"The second path is real only after you turn away. Fragment index: 645.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a new depth"
  },
  {
    id:646,
    name:"Under the Silent Meridian · 0646",
    region:"Glasswater Basin",
    signal:"a ripple crossing dry ground",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 2, and its trace number is 646.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 646.",
    lesson:"Observation can be a form of movement.",
    response:"A distant light answers with one measured flash.",
    reward:"a quiet clue"
  },
  {
    id:647,
    name:"Across the Silent Meridian · 0647",
    region:"Blue Divide",
    signal:"a pattern of footprints facing inward",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 3, and its trace number is 647.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 647.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The path behind you quietly changes its shape.",
    reward:"a memory fragment"
  },
  {
    id:648,
    name:"Behind the Silent Meridian · 0648",
    region:"Ember Archive",
    signal:"a glow hidden inside a crack",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 4, and its trace number is 648.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 648.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The air grows still, waiting for another choice.",
    reward:"a map trace"
  },
  {
    id:649,
    name:"Within the Silent Meridian · 0649",
    region:"Echo Marsh",
    signal:"a door-shaped gap in the air",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 5, and its trace number is 649.",
    clue:"Find the only light that does not pulse. Fragment index: 649.",
    lesson:"Memory is more than a record of where you went.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a sealed memory"
  },
  {
    id:650,
    name:"At the edge of the Silent Meridian · 0650",
    region:"Last Horizon",
    signal:"a thin thread of silver light",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 6, and its trace number is 650.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 650.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The echo returns with one extra note.",
    reward:"a clearer signal"
  },
  {
    id:651,
    name:"Where the Silent Meridian · 0651",
    region:"Glasswater Basin",
    signal:"a reflection that arrives late",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 7, and its trace number is 651.",
    clue:"The safest route is not always the shortest. Fragment index: 651.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The ground glows for a moment, then settles.",
    reward:"a changed landmark"
  },
  {
    id:652,
    name:"Before the Silent Meridian · 0652",
    region:"Blue Divide",
    signal:"a door-shaped gap in the air",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 1, and its trace number is 652.",
    clue:"Your previous route is the map for this one. Fragment index: 652.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A new mark appears beside your last footprint.",
    reward:"a hidden passage"
  },
  {
    id:653,
    name:"After the Silent Meridian · 0653",
    region:"Ember Archive",
    signal:"a thin thread of silver light",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 2, and its trace number is 653.",
    clue:"Move once, pause once, then listen again. Fragment index: 653.",
    lesson:"Memory is more than a record of where you went.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a second chance"
  },
  {
    id:654,
    name:"Between the Silent Meridian · 0654",
    region:"Echo Marsh",
    signal:"a reflection that arrives late",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 3, and its trace number is 654.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 654.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a path that remembers"
  },
  {
    id:655,
    name:"Above the Silent Meridian · 0655",
    region:"Mirror Waste",
    signal:"a shadow moving against the light",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 4, and its trace number is 655.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 655.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"an echo token"
  },
  {
    id:656,
    name:"Below the Silent Meridian · 0656",
    region:"Quiet Reach",
    signal:"a distant bell with no echo",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 5, and its trace number is 656.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 656.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The horizon brightens where your route bends.",
    reward:"a stored reflection"
  },
  {
    id:657,
    name:"The Glass Orchard · 0657",
    region:"Moss Quarter",
    signal:"a hum that follows silence",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 6, and its trace number is 657.",
    clue:"A repeated step can open a door, but only once. Fragment index: 657.",
    lesson:"Memory is more than a record of where you went.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a new depth"
  },
  {
    id:658,
    name:"A Glass Orchard · 0658",
    region:"Hollow Canopy",
    signal:"a warm line beneath the stone",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 7, and its trace number is 658.",
    clue:"The second path is real only after you turn away. Fragment index: 658.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A distant light answers with one measured flash.",
    reward:"a quiet clue"
  },
  {
    id:659,
    name:"Beneath the Glass Orchard · 0659",
    region:"Lantern Expanse",
    signal:"a distant bell with no echo",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 1, and its trace number is 659.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 659.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The path behind you quietly changes its shape.",
    reward:"a memory fragment"
  },
  {
    id:660,
    name:"Beyond the Glass Orchard · 0660",
    region:"Pale Engine",
    signal:"a hum that follows silence",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 2, and its trace number is 660.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 660.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The air grows still, waiting for another choice.",
    reward:"a map trace"
  },
  {
    id:661,
    name:"Inside the Glass Orchard · 0661",
    region:"Quiet Reach",
    signal:"a warm line beneath the stone",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 3, and its trace number is 661.",
    clue:"Return to the place where the floor changes colour. Fragment index: 661.",
    lesson:"Memory is more than a record of where you went.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a sealed memory"
  },
  {
    id:662,
    name:"Under the Glass Orchard · 0662",
    region:"Moss Quarter",
    signal:"a pale mark that shifts position",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 4, and its trace number is 662.",
    clue:"The answer is stored in the order of your choices. Fragment index: 662.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The echo returns with one extra note.",
    reward:"a clearer signal"
  },
  {
    id:663,
    name:"Across the Glass Orchard · 0663",
    region:"Hollow Canopy",
    signal:"a small star below the horizon",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 5, and its trace number is 663.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 663.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The ground glows for a moment, then settles.",
    reward:"a changed landmark"
  },
  {
    id:664,
    name:"Behind the Glass Orchard · 0664",
    region:"Lantern Expanse",
    signal:"three notes with no source",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 6, and its trace number is 664.",
    clue:"The safest route is not always the shortest. Fragment index: 664.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A new mark appears beside your last footprint.",
    reward:"a hidden passage"
  },
  {
    id:665,
    name:"Within the Glass Orchard · 0665",
    region:"Pale Engine",
    signal:"a slow rhythm under the wind",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 7, and its trace number is 665.",
    clue:"Your previous route is the map for this one. Fragment index: 665.",
    lesson:"Memory is more than a record of where you went.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a second chance"
  },
  {
    id:666,
    name:"At the edge of the Glass Orchard · 0666",
    region:"Frostline",
    signal:"a small star below the horizon",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 1, and its trace number is 666.",
    clue:"Move once, pause once, then listen again. Fragment index: 666.",
    lesson:"Silence is information when you learn to listen.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a path that remembers"
  },
  {
    id:667,
    name:"Where the Glass Orchard · 0667",
    region:"Last Horizon",
    signal:"three notes with no source",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 2, and its trace number is 667.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 667.",
    lesson:"Returning is not the same as repeating.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"an echo token"
  },
  {
    id:668,
    name:"Before the Glass Orchard · 0668",
    region:"Glasswater Basin",
    signal:"a slow rhythm under the wind",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 3, and its trace number is 668.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 668.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a sealed memory"
  },
  {
    id:669,
    name:"After the Glass Orchard · 0669",
    region:"Blue Divide",
    signal:"a breath behind the wall",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 4, and its trace number is 669.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 669.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A distant light answers with one measured flash.",
    reward:"a clearer signal"
  },
  {
    id:670,
    name:"Between the Glass Orchard · 0670",
    region:"Ember Archive",
    signal:"a low blue pulse",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 5, and its trace number is 670.",
    clue:"A repeated step can open a door, but only once. Fragment index: 670.",
    lesson:"Silence is information when you learn to listen.",
    response:"The path behind you quietly changes its shape.",
    reward:"a changed landmark"
  },
  {
    id:671,
    name:"Above the Glass Orchard · 0671",
    region:"Echo Marsh",
    signal:"a ripple crossing dry ground",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 6, and its trace number is 671.",
    clue:"The second path is real only after you turn away. Fragment index: 671.",
    lesson:"Returning is not the same as repeating.",
    response:"The air grows still, waiting for another choice.",
    reward:"a hidden passage"
  },
  {
    id:672,
    name:"Below the Glass Orchard · 0672",
    region:"Last Horizon",
    signal:"a pattern of footprints facing inward",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 7, and its trace number is 672.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 672.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a second chance"
  },
  {
    id:673,
    name:"The Hollow Stair · 0673",
    region:"Glasswater Basin",
    signal:"a low blue pulse",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 1, and its trace number is 673.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 673.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The echo returns with one extra note.",
    reward:"a path that remembers"
  },
  {
    id:674,
    name:"A Hollow Stair · 0674",
    region:"Blue Divide",
    signal:"a ripple crossing dry ground",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 2, and its trace number is 674.",
    clue:"Return to the place where the floor changes colour. Fragment index: 674.",
    lesson:"Silence is information when you learn to listen.",
    response:"The ground glows for a moment, then settles.",
    reward:"an echo token"
  },
  {
    id:675,
    name:"Beneath the Hollow Stair · 0675",
    region:"Ember Archive",
    signal:"a pattern of footprints facing inward",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 3, and its trace number is 675.",
    clue:"The answer is stored in the order of your choices. Fragment index: 675.",
    lesson:"Returning is not the same as repeating.",
    response:"A new mark appears beside your last footprint.",
    reward:"a stored reflection"
  },
  {
    id:676,
    name:"Beyond the Hollow Stair · 0676",
    region:"Echo Marsh",
    signal:"a glow hidden inside a crack",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 4, and its trace number is 676.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 676.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a new depth"
  },
  {
    id:677,
    name:"Inside the Hollow Stair · 0677",
    region:"Mirror Waste",
    signal:"a door-shaped gap in the air",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 5, and its trace number is 677.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 677.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a quiet clue"
  },
  {
    id:678,
    name:"Under the Hollow Stair · 0678",
    region:"Quiet Reach",
    signal:"a thin thread of silver light",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 6, and its trace number is 678.",
    clue:"Find the only light that does not pulse. Fragment index: 678.",
    lesson:"Silence is information when you learn to listen.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a memory fragment"
  },
  {
    id:679,
    name:"Across the Hollow Stair · 0679",
    region:"Moss Quarter",
    signal:"a reflection that arrives late",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 7, and its trace number is 679.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 679.",
    lesson:"Returning is not the same as repeating.",
    response:"The horizon brightens where your route bends.",
    reward:"a map trace"
  },
  {
    id:680,
    name:"Behind the Hollow Stair · 0680",
    region:"Hollow Canopy",
    signal:"a door-shaped gap in the air",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 1, and its trace number is 680.",
    clue:"The safest route is not always the shortest. Fragment index: 680.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a sealed memory"
  },
  {
    id:681,
    name:"Within the Hollow Stair · 0681",
    region:"Lantern Expanse",
    signal:"a thin thread of silver light",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 2, and its trace number is 681.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 681.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A distant light answers with one measured flash.",
    reward:"a clearer signal"
  },
  {
    id:682,
    name:"At the edge of the Hollow Stair · 0682",
    region:"Pale Engine",
    signal:"a reflection that arrives late",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 3, and its trace number is 682.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 682.",
    lesson:"Silence is information when you learn to listen.",
    response:"The path behind you quietly changes its shape.",
    reward:"a changed landmark"
  },
  {
    id:683,
    name:"Where the Hollow Stair · 0683",
    region:"Quiet Reach",
    signal:"a shadow moving against the light",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 4, and its trace number is 683.",
    clue:"A repeated step can open a door, but only once. Fragment index: 683.",
    lesson:"Returning is not the same as repeating.",
    response:"The air grows still, waiting for another choice.",
    reward:"a hidden passage"
  },
  {
    id:684,
    name:"Before the Hollow Stair · 0684",
    region:"Moss Quarter",
    signal:"a distant bell with no echo",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 5, and its trace number is 684.",
    clue:"The second path is real only after you turn away. Fragment index: 684.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a second chance"
  },
  {
    id:685,
    name:"After the Hollow Stair · 0685",
    region:"Hollow Canopy",
    signal:"a hum that follows silence",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 6, and its trace number is 685.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 685.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The echo returns with one extra note.",
    reward:"a path that remembers"
  },
  {
    id:686,
    name:"Between the Hollow Stair · 0686",
    region:"Lantern Expanse",
    signal:"a warm line beneath the stone",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 7, and its trace number is 686.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 686.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The ground glows for a moment, then settles.",
    reward:"an echo token"
  },
  {
    id:687,
    name:"Above the Hollow Stair · 0687",
    region:"Pale Engine",
    signal:"a distant bell with no echo",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 1, and its trace number is 687.",
    clue:"Return to the place where the floor changes colour. Fragment index: 687.",
    lesson:"Observation can be a form of movement.",
    response:"A new mark appears beside your last footprint.",
    reward:"a stored reflection"
  },
  {
    id:688,
    name:"Below the Hollow Stair · 0688",
    region:"Frostline",
    signal:"a hum that follows silence",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 2, and its trace number is 688.",
    clue:"The answer is stored in the order of your choices. Fragment index: 688.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a new depth"
  },
  {
    id:689,
    name:"The Blue Archive · 0689",
    region:"Last Horizon",
    signal:"a warm line beneath the stone",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 3, and its trace number is 689.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 689.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a quiet clue"
  },
  {
    id:690,
    name:"A Blue Archive · 0690",
    region:"Glasswater Basin",
    signal:"a pale mark that shifts position",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 4, and its trace number is 690.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 690.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a memory fragment"
  },
  {
    id:691,
    name:"Beneath the Blue Archive · 0691",
    region:"Blue Divide",
    signal:"a small star below the horizon",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 5, and its trace number is 691.",
    clue:"Find the only light that does not pulse. Fragment index: 691.",
    lesson:"Observation can be a form of movement.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a map trace"
  },
  {
    id:692,
    name:"Beyond the Blue Archive · 0692",
    region:"Ember Archive",
    signal:"three notes with no source",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 6, and its trace number is 692.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 692.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A distant light answers with one measured flash.",
    reward:"a sealed memory"
  },
  {
    id:693,
    name:"Inside the Blue Archive · 0693",
    region:"Echo Marsh",
    signal:"a slow rhythm under the wind",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 7, and its trace number is 693.",
    clue:"The safest route is not always the shortest. Fragment index: 693.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The path behind you quietly changes its shape.",
    reward:"a clearer signal"
  },
  {
    id:694,
    name:"Under the Blue Archive · 0694",
    region:"Last Horizon",
    signal:"a small star below the horizon",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 1, and its trace number is 694.",
    clue:"Your previous route is the map for this one. Fragment index: 694.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The air grows still, waiting for another choice.",
    reward:"a changed landmark"
  },
  {
    id:695,
    name:"Across the Blue Archive · 0695",
    region:"Glasswater Basin",
    signal:"three notes with no source",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 2, and its trace number is 695.",
    clue:"Move once, pause once, then listen again. Fragment index: 695.",
    lesson:"Observation can be a form of movement.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a hidden passage"
  },
  {
    id:696,
    name:"Behind the Blue Archive · 0696",
    region:"Blue Divide",
    signal:"a slow rhythm under the wind",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 3, and its trace number is 696.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 696.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The echo returns with one extra note.",
    reward:"a second chance"
  },
  {
    id:697,
    name:"Within the Blue Archive · 0697",
    region:"Ember Archive",
    signal:"a breath behind the wall",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 4, and its trace number is 697.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 697.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The ground glows for a moment, then settles.",
    reward:"a memory fragment"
  },
  {
    id:698,
    name:"At the edge of the Blue Archive · 0698",
    region:"Echo Marsh",
    signal:"a low blue pulse",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 5, and its trace number is 698.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 698.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A new mark appears beside your last footprint.",
    reward:"a map trace"
  },
  {
    id:699,
    name:"Where the Blue Archive · 0699",
    region:"Mirror Waste",
    signal:"a ripple crossing dry ground",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 6, and its trace number is 699.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 699.",
    lesson:"Observation can be a form of movement.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a sealed memory"
  },
  {
    id:700,
    name:"Before the Blue Archive · 0700",
    region:"Quiet Reach",
    signal:"a pattern of footprints facing inward",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 7, and its trace number is 700.",
    clue:"Return to the place where the floor changes colour. Fragment index: 700.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a clearer signal"
  },
  {
    id:701,
    name:"After the Blue Archive · 0701",
    region:"Moss Quarter",
    signal:"a low blue pulse",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 1, and its trace number is 701.",
    clue:"The answer is stored in the order of your choices. Fragment index: 701.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a changed landmark"
  },
  {
    id:702,
    name:"Between the Blue Archive · 0702",
    region:"Hollow Canopy",
    signal:"a ripple crossing dry ground",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 2, and its trace number is 702.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 702.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The horizon brightens where your route bends.",
    reward:"a hidden passage"
  },
  {
    id:703,
    name:"Above the Blue Archive · 0703",
    region:"Lantern Expanse",
    signal:"a pattern of footprints facing inward",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 3, and its trace number is 703.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 703.",
    lesson:"Observation can be a form of movement.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a second chance"
  },
  {
    id:704,
    name:"Below the Blue Archive · 0704",
    region:"Pale Engine",
    signal:"a glow hidden inside a crack",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 4, and its trace number is 704.",
    clue:"Find the only light that does not pulse. Fragment index: 704.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A distant light answers with one measured flash.",
    reward:"a path that remembers"
  },
  {
    id:705,
    name:"The Ashen Bridge · 0705",
    region:"Quiet Reach",
    signal:"a door-shaped gap in the air",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 5, and its trace number is 705.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 705.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The path behind you quietly changes its shape.",
    reward:"an echo token"
  },
  {
    id:706,
    name:"A Ashen Bridge · 0706",
    region:"Moss Quarter",
    signal:"a thin thread of silver light",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 6, and its trace number is 706.",
    clue:"The safest route is not always the shortest. Fragment index: 706.",
    lesson:"Memory is more than a record of where you went.",
    response:"The air grows still, waiting for another choice.",
    reward:"a stored reflection"
  },
  {
    id:707,
    name:"Beneath the Ashen Bridge · 0707",
    region:"Hollow Canopy",
    signal:"a reflection that arrives late",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 7, and its trace number is 707.",
    clue:"Your previous route is the map for this one. Fragment index: 707.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a new depth"
  },
  {
    id:708,
    name:"Beyond the Ashen Bridge · 0708",
    region:"Lantern Expanse",
    signal:"a door-shaped gap in the air",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 1, and its trace number is 708.",
    clue:"Move once, pause once, then listen again. Fragment index: 708.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The echo returns with one extra note.",
    reward:"a quiet clue"
  },
  {
    id:709,
    name:"Inside the Ashen Bridge · 0709",
    region:"Pale Engine",
    signal:"a thin thread of silver light",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 2, and its trace number is 709.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 709.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The ground glows for a moment, then settles.",
    reward:"a memory fragment"
  },
  {
    id:710,
    name:"Under the Ashen Bridge · 0710",
    region:"Frostline",
    signal:"a reflection that arrives late",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 3, and its trace number is 710.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 710.",
    lesson:"Memory is more than a record of where you went.",
    response:"A new mark appears beside your last footprint.",
    reward:"a map trace"
  },
  {
    id:711,
    name:"Across the Ashen Bridge · 0711",
    region:"Last Horizon",
    signal:"a shadow moving against the light",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 4, and its trace number is 711.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 711.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a sealed memory"
  },
  {
    id:712,
    name:"Behind the Ashen Bridge · 0712",
    region:"Glasswater Basin",
    signal:"a distant bell with no echo",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 5, and its trace number is 712.",
    clue:"A repeated step can open a door, but only once. Fragment index: 712.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a clearer signal"
  },
  {
    id:713,
    name:"Within the Ashen Bridge · 0713",
    region:"Blue Divide",
    signal:"a hum that follows silence",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 6, and its trace number is 713.",
    clue:"The second path is real only after you turn away. Fragment index: 713.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a changed landmark"
  },
  {
    id:714,
    name:"At the edge of the Ashen Bridge · 0714",
    region:"Ember Archive",
    signal:"a warm line beneath the stone",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 7, and its trace number is 714.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 714.",
    lesson:"Memory is more than a record of where you went.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a hidden passage"
  },
  {
    id:715,
    name:"Where the Ashen Bridge · 0715",
    region:"Echo Marsh",
    signal:"a distant bell with no echo",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 1, and its trace number is 715.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 715.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A distant light answers with one measured flash.",
    reward:"a second chance"
  },
  {
    id:716,
    name:"Before the Ashen Bridge · 0716",
    region:"Last Horizon",
    signal:"a hum that follows silence",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 2, and its trace number is 716.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 716.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The path behind you quietly changes its shape.",
    reward:"a path that remembers"
  },
  {
    id:717,
    name:"After the Ashen Bridge · 0717",
    region:"Glasswater Basin",
    signal:"a warm line beneath the stone",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 3, and its trace number is 717.",
    clue:"Find the only light that does not pulse. Fragment index: 717.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The air grows still, waiting for another choice.",
    reward:"an echo token"
  },
  {
    id:718,
    name:"Between the Ashen Bridge · 0718",
    region:"Blue Divide",
    signal:"a pale mark that shifts position",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 4, and its trace number is 718.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 718.",
    lesson:"Memory is more than a record of where you went.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a stored reflection"
  },
  {
    id:719,
    name:"Above the Ashen Bridge · 0719",
    region:"Ember Archive",
    signal:"a small star below the horizon",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 5, and its trace number is 719.",
    clue:"The safest route is not always the shortest. Fragment index: 719.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The echo returns with one extra note.",
    reward:"a new depth"
  },
  {
    id:720,
    name:"Below the Ashen Bridge · 0720",
    region:"Echo Marsh",
    signal:"three notes with no source",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 6, and its trace number is 720.",
    clue:"Your previous route is the map for this one. Fragment index: 720.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The ground glows for a moment, then settles.",
    reward:"a quiet clue"
  },
  {
    id:721,
    name:"The Mirror Field · 0721",
    region:"Mirror Waste",
    signal:"a slow rhythm under the wind",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 7, and its trace number is 721.",
    clue:"Move once, pause once, then listen again. Fragment index: 721.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A new mark appears beside your last footprint.",
    reward:"a memory fragment"
  },
  {
    id:722,
    name:"A Mirror Field · 0722",
    region:"Quiet Reach",
    signal:"a small star below the horizon",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 1, and its trace number is 722.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 722.",
    lesson:"Memory is more than a record of where you went.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a map trace"
  },
  {
    id:723,
    name:"Beneath the Mirror Field · 0723",
    region:"Moss Quarter",
    signal:"three notes with no source",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 2, and its trace number is 723.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 723.",
    lesson:"Silence is information when you learn to listen.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a sealed memory"
  },
  {
    id:724,
    name:"Beyond the Mirror Field · 0724",
    region:"Hollow Canopy",
    signal:"a slow rhythm under the wind",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 3, and its trace number is 724.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 724.",
    lesson:"Returning is not the same as repeating.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a clearer signal"
  },
  {
    id:725,
    name:"Inside the Mirror Field · 0725",
    region:"Lantern Expanse",
    signal:"a breath behind the wall",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 4, and its trace number is 725.",
    clue:"A repeated step can open a door, but only once. Fragment index: 725.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The horizon brightens where your route bends.",
    reward:"a changed landmark"
  },
  {
    id:726,
    name:"Under the Mirror Field · 0726",
    region:"Pale Engine",
    signal:"a low blue pulse",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 5, and its trace number is 726.",
    clue:"The second path is real only after you turn away. Fragment index: 726.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a new depth"
  },
  {
    id:727,
    name:"Across the Mirror Field · 0727",
    region:"Quiet Reach",
    signal:"a ripple crossing dry ground",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 6, and its trace number is 727.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 727.",
    lesson:"Silence is information when you learn to listen.",
    response:"A distant light answers with one measured flash.",
    reward:"a quiet clue"
  },
  {
    id:728,
    name:"Behind the Mirror Field · 0728",
    region:"Moss Quarter",
    signal:"a pattern of footprints facing inward",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 7, and its trace number is 728.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 728.",
    lesson:"Returning is not the same as repeating.",
    response:"The path behind you quietly changes its shape.",
    reward:"a memory fragment"
  },
  {
    id:729,
    name:"Within the Mirror Field · 0729",
    region:"Hollow Canopy",
    signal:"a low blue pulse",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 1, and its trace number is 729.",
    clue:"Return to the place where the floor changes colour. Fragment index: 729.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The air grows still, waiting for another choice.",
    reward:"a map trace"
  },
  {
    id:730,
    name:"At the edge of the Mirror Field · 0730",
    region:"Lantern Expanse",
    signal:"a ripple crossing dry ground",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 2, and its trace number is 730.",
    clue:"The answer is stored in the order of your choices. Fragment index: 730.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a sealed memory"
  },
  {
    id:731,
    name:"Where the Mirror Field · 0731",
    region:"Pale Engine",
    signal:"a pattern of footprints facing inward",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 3, and its trace number is 731.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 731.",
    lesson:"Silence is information when you learn to listen.",
    response:"The echo returns with one extra note.",
    reward:"a clearer signal"
  },
  {
    id:732,
    name:"Before the Mirror Field · 0732",
    region:"Frostline",
    signal:"a glow hidden inside a crack",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 4, and its trace number is 732.",
    clue:"The safest route is not always the shortest. Fragment index: 732.",
    lesson:"Returning is not the same as repeating.",
    response:"The ground glows for a moment, then settles.",
    reward:"a changed landmark"
  },
  {
    id:733,
    name:"After the Mirror Field · 0733",
    region:"Last Horizon",
    signal:"a door-shaped gap in the air",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 5, and its trace number is 733.",
    clue:"Your previous route is the map for this one. Fragment index: 733.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A new mark appears beside your last footprint.",
    reward:"a hidden passage"
  },
  {
    id:734,
    name:"Between the Mirror Field · 0734",
    region:"Glasswater Basin",
    signal:"a thin thread of silver light",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 6, and its trace number is 734.",
    clue:"Move once, pause once, then listen again. Fragment index: 734.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a second chance"
  },
  {
    id:735,
    name:"Above the Mirror Field · 0735",
    region:"Blue Divide",
    signal:"a reflection that arrives late",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 7, and its trace number is 735.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 735.",
    lesson:"Silence is information when you learn to listen.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a path that remembers"
  },
  {
    id:736,
    name:"Below the Mirror Field · 0736",
    region:"Ember Archive",
    signal:"a door-shaped gap in the air",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 1, and its trace number is 736.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 736.",
    lesson:"Returning is not the same as repeating.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"an echo token"
  },
  {
    id:737,
    name:"The Sleeping Engine · 0737",
    region:"Echo Marsh",
    signal:"a thin thread of silver light",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 2, and its trace number is 737.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 737.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a stored reflection"
  },
  {
    id:738,
    name:"A Sleeping Engine · 0738",
    region:"Last Horizon",
    signal:"a reflection that arrives late",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 3, and its trace number is 738.",
    clue:"A repeated step can open a door, but only once. Fragment index: 738.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A distant light answers with one measured flash.",
    reward:"a new depth"
  },
  {
    id:739,
    name:"Beneath the Sleeping Engine · 0739",
    region:"Glasswater Basin",
    signal:"a shadow moving against the light",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 4, and its trace number is 739.",
    clue:"The second path is real only after you turn away. Fragment index: 739.",
    lesson:"Silence is information when you learn to listen.",
    response:"The path behind you quietly changes its shape.",
    reward:"a quiet clue"
  },
  {
    id:740,
    name:"Beyond the Sleeping Engine · 0740",
    region:"Blue Divide",
    signal:"a distant bell with no echo",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 5, and its trace number is 740.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 740.",
    lesson:"Returning is not the same as repeating.",
    response:"The air grows still, waiting for another choice.",
    reward:"a memory fragment"
  },
  {
    id:741,
    name:"Inside the Sleeping Engine · 0741",
    region:"Ember Archive",
    signal:"a hum that follows silence",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 6, and its trace number is 741.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 741.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a map trace"
  },
  {
    id:742,
    name:"Under the Sleeping Engine · 0742",
    region:"Echo Marsh",
    signal:"a warm line beneath the stone",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 7, and its trace number is 742.",
    clue:"Return to the place where the floor changes colour. Fragment index: 742.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The echo returns with one extra note.",
    reward:"a sealed memory"
  },
  {
    id:743,
    name:"Across the Sleeping Engine · 0743",
    region:"Mirror Waste",
    signal:"a distant bell with no echo",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 1, and its trace number is 743.",
    clue:"The answer is stored in the order of your choices. Fragment index: 743.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The ground glows for a moment, then settles.",
    reward:"a clearer signal"
  },
  {
    id:744,
    name:"Behind the Sleeping Engine · 0744",
    region:"Quiet Reach",
    signal:"a hum that follows silence",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 2, and its trace number is 744.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 744.",
    lesson:"Observation can be a form of movement.",
    response:"A new mark appears beside your last footprint.",
    reward:"a changed landmark"
  },
  {
    id:745,
    name:"Within the Sleeping Engine · 0745",
    region:"Moss Quarter",
    signal:"a warm line beneath the stone",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 3, and its trace number is 745.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 745.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a hidden passage"
  },
  {
    id:746,
    name:"At the edge of the Sleeping Engine · 0746",
    region:"Hollow Canopy",
    signal:"a pale mark that shifts position",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 4, and its trace number is 746.",
    clue:"Find the only light that does not pulse. Fragment index: 746.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a second chance"
  },
  {
    id:747,
    name:"Where the Sleeping Engine · 0747",
    region:"Lantern Expanse",
    signal:"a small star below the horizon",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 5, and its trace number is 747.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 747.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a path that remembers"
  },
  {
    id:748,
    name:"Before the Sleeping Engine · 0748",
    region:"Pale Engine",
    signal:"three notes with no source",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 6, and its trace number is 748.",
    clue:"The safest route is not always the shortest. Fragment index: 748.",
    lesson:"Observation can be a form of movement.",
    response:"The horizon brightens where your route bends.",
    reward:"an echo token"
  },
  {
    id:749,
    name:"After the Sleeping Engine · 0749",
    region:"Quiet Reach",
    signal:"a slow rhythm under the wind",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 7, and its trace number is 749.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 749.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a stored reflection"
  },
  {
    id:750,
    name:"Between the Sleeping Engine · 0750",
    region:"Moss Quarter",
    signal:"a small star below the horizon",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 1, and its trace number is 750.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 750.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A distant light answers with one measured flash.",
    reward:"a new depth"
  },
  {
    id:751,
    name:"Above the Sleeping Engine · 0751",
    region:"Hollow Canopy",
    signal:"three notes with no source",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 2, and its trace number is 751.",
    clue:"A repeated step can open a door, but only once. Fragment index: 751.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The path behind you quietly changes its shape.",
    reward:"a quiet clue"
  },
  {
    id:752,
    name:"Below the Sleeping Engine · 0752",
    region:"Lantern Expanse",
    signal:"a slow rhythm under the wind",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 3, and its trace number is 752.",
    clue:"The second path is real only after you turn away. Fragment index: 752.",
    lesson:"Observation can be a form of movement.",
    response:"The air grows still, waiting for another choice.",
    reward:"a memory fragment"
  },
  {
    id:753,
    name:"The Distant Choir · 0753",
    region:"Pale Engine",
    signal:"a breath behind the wall",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 4, and its trace number is 753.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 753.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a map trace"
  },
  {
    id:754,
    name:"A Distant Choir · 0754",
    region:"Frostline",
    signal:"a low blue pulse",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 5, and its trace number is 754.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 754.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The echo returns with one extra note.",
    reward:"a sealed memory"
  },
  {
    id:755,
    name:"Beneath the Distant Choir · 0755",
    region:"Last Horizon",
    signal:"a ripple crossing dry ground",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 6, and its trace number is 755.",
    clue:"Return to the place where the floor changes colour. Fragment index: 755.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The ground glows for a moment, then settles.",
    reward:"an echo token"
  },
  {
    id:756,
    name:"Beyond the Distant Choir · 0756",
    region:"Glasswater Basin",
    signal:"a pattern of footprints facing inward",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 7, and its trace number is 756.",
    clue:"The answer is stored in the order of your choices. Fragment index: 756.",
    lesson:"Observation can be a form of movement.",
    response:"A new mark appears beside your last footprint.",
    reward:"a stored reflection"
  },
  {
    id:757,
    name:"Inside the Distant Choir · 0757",
    region:"Blue Divide",
    signal:"a low blue pulse",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 1, and its trace number is 757.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 757.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a new depth"
  },
  {
    id:758,
    name:"Under the Distant Choir · 0758",
    region:"Ember Archive",
    signal:"a ripple crossing dry ground",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 2, and its trace number is 758.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 758.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a quiet clue"
  },
  {
    id:759,
    name:"Across the Distant Choir · 0759",
    region:"Echo Marsh",
    signal:"a pattern of footprints facing inward",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 3, and its trace number is 759.",
    clue:"Find the only light that does not pulse. Fragment index: 759.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a memory fragment"
  },
  {
    id:760,
    name:"Behind the Distant Choir · 0760",
    region:"Last Horizon",
    signal:"a glow hidden inside a crack",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 4, and its trace number is 760.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 760.",
    lesson:"Observation can be a form of movement.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a map trace"
  },
  {
    id:761,
    name:"Within the Distant Choir · 0761",
    region:"Glasswater Basin",
    signal:"a door-shaped gap in the air",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 5, and its trace number is 761.",
    clue:"The safest route is not always the shortest. Fragment index: 761.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A distant light answers with one measured flash.",
    reward:"a sealed memory"
  },
  {
    id:762,
    name:"At the edge of the Distant Choir · 0762",
    region:"Blue Divide",
    signal:"a thin thread of silver light",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 6, and its trace number is 762.",
    clue:"Your previous route is the map for this one. Fragment index: 762.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The path behind you quietly changes its shape.",
    reward:"a clearer signal"
  },
  {
    id:763,
    name:"Where the Distant Choir · 0763",
    region:"Ember Archive",
    signal:"a reflection that arrives late",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 7, and its trace number is 763.",
    clue:"Move once, pause once, then listen again. Fragment index: 763.",
    lesson:"Memory is more than a record of where you went.",
    response:"The air grows still, waiting for another choice.",
    reward:"a changed landmark"
  },
  {
    id:764,
    name:"Before the Distant Choir · 0764",
    region:"Echo Marsh",
    signal:"a door-shaped gap in the air",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 1, and its trace number is 764.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 764.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a hidden passage"
  },
  {
    id:765,
    name:"After the Distant Choir · 0765",
    region:"Mirror Waste",
    signal:"a thin thread of silver light",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 2, and its trace number is 765.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 765.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The echo returns with one extra note.",
    reward:"a second chance"
  },
  {
    id:766,
    name:"Between the Distant Choir · 0766",
    region:"Quiet Reach",
    signal:"a reflection that arrives late",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 3, and its trace number is 766.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 766.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The ground glows for a moment, then settles.",
    reward:"a path that remembers"
  },
  {
    id:767,
    name:"Above the Distant Choir · 0767",
    region:"Moss Quarter",
    signal:"a shadow moving against the light",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 4, and its trace number is 767.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 767.",
    lesson:"Memory is more than a record of where you went.",
    response:"A new mark appears beside your last footprint.",
    reward:"an echo token"
  },
  {
    id:768,
    name:"Below the Distant Choir · 0768",
    region:"Hollow Canopy",
    signal:"a distant bell with no echo",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 5, and its trace number is 768.",
    clue:"Return to the place where the floor changes colour. Fragment index: 768.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a stored reflection"
  },
  {
    id:769,
    name:"The Pale Garden · 0769",
    region:"Lantern Expanse",
    signal:"a hum that follows silence",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 6, and its trace number is 769.",
    clue:"The answer is stored in the order of your choices. Fragment index: 769.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a new depth"
  },
  {
    id:770,
    name:"A Pale Garden · 0770",
    region:"Pale Engine",
    signal:"a warm line beneath the stone",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 7, and its trace number is 770.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 770.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a quiet clue"
  },
  {
    id:771,
    name:"Beneath the Pale Garden · 0771",
    region:"Quiet Reach",
    signal:"a distant bell with no echo",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 1, and its trace number is 771.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 771.",
    lesson:"Memory is more than a record of where you went.",
    response:"The horizon brightens where your route bends.",
    reward:"a memory fragment"
  },
  {
    id:772,
    name:"Beyond the Pale Garden · 0772",
    region:"Moss Quarter",
    signal:"a hum that follows silence",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 2, and its trace number is 772.",
    clue:"Find the only light that does not pulse. Fragment index: 772.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a map trace"
  },
  {
    id:773,
    name:"Inside the Pale Garden · 0773",
    region:"Hollow Canopy",
    signal:"a warm line beneath the stone",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 3, and its trace number is 773.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 773.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A distant light answers with one measured flash.",
    reward:"a sealed memory"
  },
  {
    id:774,
    name:"Under the Pale Garden · 0774",
    region:"Lantern Expanse",
    signal:"a pale mark that shifts position",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 4, and its trace number is 774.",
    clue:"The safest route is not always the shortest. Fragment index: 774.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The path behind you quietly changes its shape.",
    reward:"a clearer signal"
  },
  {
    id:775,
    name:"Across the Pale Garden · 0775",
    region:"Pale Engine",
    signal:"a small star below the horizon",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 5, and its trace number is 775.",
    clue:"Your previous route is the map for this one. Fragment index: 775.",
    lesson:"Memory is more than a record of where you went.",
    response:"The air grows still, waiting for another choice.",
    reward:"a changed landmark"
  },
  {
    id:776,
    name:"Behind the Pale Garden · 0776",
    region:"Frostline",
    signal:"three notes with no source",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 6, and its trace number is 776.",
    clue:"Move once, pause once, then listen again. Fragment index: 776.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a hidden passage"
  },
  {
    id:777,
    name:"Within the Pale Garden · 0777",
    region:"Last Horizon",
    signal:"a slow rhythm under the wind",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 7, and its trace number is 777.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 777.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The echo returns with one extra note.",
    reward:"a second chance"
  },
  {
    id:778,
    name:"At the edge of the Pale Garden · 0778",
    region:"Glasswater Basin",
    signal:"a small star below the horizon",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 1, and its trace number is 778.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 778.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The ground glows for a moment, then settles.",
    reward:"a path that remembers"
  },
  {
    id:779,
    name:"Where the Pale Garden · 0779",
    region:"Blue Divide",
    signal:"three notes with no source",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 2, and its trace number is 779.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 779.",
    lesson:"Memory is more than a record of where you went.",
    response:"A new mark appears beside your last footprint.",
    reward:"an echo token"
  },
  {
    id:780,
    name:"Before the Pale Garden · 0780",
    region:"Ember Archive",
    signal:"a slow rhythm under the wind",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 3, and its trace number is 780.",
    clue:"A repeated step can open a door, but only once. Fragment index: 780.",
    lesson:"Silence is information when you learn to listen.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a stored reflection"
  },
  {
    id:781,
    name:"After the Pale Garden · 0781",
    region:"Echo Marsh",
    signal:"a breath behind the wall",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 4, and its trace number is 781.",
    clue:"The second path is real only after you turn away. Fragment index: 781.",
    lesson:"Returning is not the same as repeating.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a new depth"
  },
  {
    id:782,
    name:"Between the Pale Garden · 0782",
    region:"Last Horizon",
    signal:"a low blue pulse",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 5, and its trace number is 782.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 782.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a quiet clue"
  },
  {
    id:783,
    name:"Above the Pale Garden · 0783",
    region:"Glasswater Basin",
    signal:"a ripple crossing dry ground",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 6, and its trace number is 783.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 783.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a memory fragment"
  },
  {
    id:784,
    name:"Below the Pale Garden · 0784",
    region:"Blue Divide",
    signal:"a pattern of footprints facing inward",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 7, and its trace number is 784.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 784.",
    lesson:"Silence is information when you learn to listen.",
    response:"A distant light answers with one measured flash.",
    reward:"a second chance"
  },
  {
    id:785,
    name:"The Forgotten Door · 0785",
    region:"Ember Archive",
    signal:"a low blue pulse",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 1, and its trace number is 785.",
    clue:"Find the only light that does not pulse. Fragment index: 785.",
    lesson:"Returning is not the same as repeating.",
    response:"The path behind you quietly changes its shape.",
    reward:"a path that remembers"
  },
  {
    id:786,
    name:"A Forgotten Door · 0786",
    region:"Echo Marsh",
    signal:"a ripple crossing dry ground",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 2, and its trace number is 786.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 786.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The air grows still, waiting for another choice.",
    reward:"an echo token"
  },
  {
    id:787,
    name:"Beneath the Forgotten Door · 0787",
    region:"Mirror Waste",
    signal:"a pattern of footprints facing inward",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 3, and its trace number is 787.",
    clue:"The safest route is not always the shortest. Fragment index: 787.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a stored reflection"
  },
  {
    id:788,
    name:"Beyond the Forgotten Door · 0788",
    region:"Quiet Reach",
    signal:"a glow hidden inside a crack",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 4, and its trace number is 788.",
    clue:"Your previous route is the map for this one. Fragment index: 788.",
    lesson:"Silence is information when you learn to listen.",
    response:"The echo returns with one extra note.",
    reward:"a new depth"
  },
  {
    id:789,
    name:"Inside the Forgotten Door · 0789",
    region:"Moss Quarter",
    signal:"a door-shaped gap in the air",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 5, and its trace number is 789.",
    clue:"Move once, pause once, then listen again. Fragment index: 789.",
    lesson:"Returning is not the same as repeating.",
    response:"The ground glows for a moment, then settles.",
    reward:"a quiet clue"
  },
  {
    id:790,
    name:"Under the Forgotten Door · 0790",
    region:"Hollow Canopy",
    signal:"a thin thread of silver light",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 6, and its trace number is 790.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 790.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A new mark appears beside your last footprint.",
    reward:"a memory fragment"
  },
  {
    id:791,
    name:"Across the Forgotten Door · 0791",
    region:"Lantern Expanse",
    signal:"a reflection that arrives late",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 7, and its trace number is 791.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 791.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a map trace"
  },
  {
    id:792,
    name:"Behind the Forgotten Door · 0792",
    region:"Pale Engine",
    signal:"a door-shaped gap in the air",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 1, and its trace number is 792.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 792.",
    lesson:"Silence is information when you learn to listen.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a sealed memory"
  },
  {
    id:793,
    name:"Within the Forgotten Door · 0793",
    region:"Quiet Reach",
    signal:"a thin thread of silver light",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 2, and its trace number is 793.",
    clue:"A repeated step can open a door, but only once. Fragment index: 793.",
    lesson:"Returning is not the same as repeating.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a clearer signal"
  },
  {
    id:794,
    name:"At the edge of the Forgotten Door · 0794",
    region:"Moss Quarter",
    signal:"a reflection that arrives late",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 3, and its trace number is 794.",
    clue:"The second path is real only after you turn away. Fragment index: 794.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The horizon brightens where your route bends.",
    reward:"a changed landmark"
  },
  {
    id:795,
    name:"Where the Forgotten Door · 0795",
    region:"Hollow Canopy",
    signal:"a shadow moving against the light",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 4, and its trace number is 795.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 795.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a hidden passage"
  },
  {
    id:796,
    name:"Before the Forgotten Door · 0796",
    region:"Lantern Expanse",
    signal:"a distant bell with no echo",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 5, and its trace number is 796.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 796.",
    lesson:"Silence is information when you learn to listen.",
    response:"A distant light answers with one measured flash.",
    reward:"a second chance"
  },
  {
    id:797,
    name:"After the Forgotten Door · 0797",
    region:"Pale Engine",
    signal:"a hum that follows silence",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 6, and its trace number is 797.",
    clue:"Return to the place where the floor changes colour. Fragment index: 797.",
    lesson:"Returning is not the same as repeating.",
    response:"The path behind you quietly changes its shape.",
    reward:"a path that remembers"
  },
  {
    id:798,
    name:"Between the Forgotten Door · 0798",
    region:"Frostline",
    signal:"a warm line beneath the stone",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 7, and its trace number is 798.",
    clue:"The answer is stored in the order of your choices. Fragment index: 798.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The air grows still, waiting for another choice.",
    reward:"an echo token"
  },
  {
    id:799,
    name:"Above the Forgotten Door · 0799",
    region:"Last Horizon",
    signal:"a distant bell with no echo",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 1, and its trace number is 799.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 799.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a stored reflection"
  },
  {
    id:800,
    name:"Below the Forgotten Door · 0800",
    region:"Glasswater Basin",
    signal:"a hum that follows silence",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 2, and its trace number is 800.",
    clue:"The safest route is not always the shortest. Fragment index: 800.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The echo returns with one extra note.",
    reward:"a new depth"
  },
  {
    id:801,
    name:"The Wandering Signal · 0801",
    region:"Blue Divide",
    signal:"a warm line beneath the stone",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 3, and its trace number is 801.",
    clue:"Your previous route is the map for this one. Fragment index: 801.",
    lesson:"Observation can be a form of movement.",
    response:"The ground glows for a moment, then settles.",
    reward:"a quiet clue"
  },
  {
    id:802,
    name:"A Wandering Signal · 0802",
    region:"Ember Archive",
    signal:"a pale mark that shifts position",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 4, and its trace number is 802.",
    clue:"Move once, pause once, then listen again. Fragment index: 802.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A new mark appears beside your last footprint.",
    reward:"a memory fragment"
  },
  {
    id:803,
    name:"Beneath the Wandering Signal · 0803",
    region:"Echo Marsh",
    signal:"a small star below the horizon",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 5, and its trace number is 803.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 803.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a map trace"
  },
  {
    id:804,
    name:"Beyond the Wandering Signal · 0804",
    region:"Last Horizon",
    signal:"three notes with no source",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 6, and its trace number is 804.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 804.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a sealed memory"
  },
  {
    id:805,
    name:"Inside the Wandering Signal · 0805",
    region:"Glasswater Basin",
    signal:"a slow rhythm under the wind",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 7, and its trace number is 805.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 805.",
    lesson:"Observation can be a form of movement.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a clearer signal"
  },
  {
    id:806,
    name:"Under the Wandering Signal · 0806",
    region:"Blue Divide",
    signal:"a small star below the horizon",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 1, and its trace number is 806.",
    clue:"A repeated step can open a door, but only once. Fragment index: 806.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a changed landmark"
  },
  {
    id:807,
    name:"Across the Wandering Signal · 0807",
    region:"Ember Archive",
    signal:"three notes with no source",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 2, and its trace number is 807.",
    clue:"The second path is real only after you turn away. Fragment index: 807.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A distant light answers with one measured flash.",
    reward:"a hidden passage"
  },
  {
    id:808,
    name:"Behind the Wandering Signal · 0808",
    region:"Echo Marsh",
    signal:"a slow rhythm under the wind",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 3, and its trace number is 808.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 808.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The path behind you quietly changes its shape.",
    reward:"a second chance"
  },
  {
    id:809,
    name:"Within the Wandering Signal · 0809",
    region:"Mirror Waste",
    signal:"a breath behind the wall",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 4, and its trace number is 809.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 809.",
    lesson:"Observation can be a form of movement.",
    response:"The air grows still, waiting for another choice.",
    reward:"a path that remembers"
  },
  {
    id:810,
    name:"At the edge of the Wandering Signal · 0810",
    region:"Quiet Reach",
    signal:"a low blue pulse",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 5, and its trace number is 810.",
    clue:"Return to the place where the floor changes colour. Fragment index: 810.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A small opening appears in the wall of darkness.",
    reward:"an echo token"
  },
  {
    id:811,
    name:"Where the Wandering Signal · 0811",
    region:"Moss Quarter",
    signal:"a ripple crossing dry ground",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 6, and its trace number is 811.",
    clue:"The answer is stored in the order of your choices. Fragment index: 811.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The echo returns with one extra note.",
    reward:"a stored reflection"
  },
  {
    id:812,
    name:"Before the Wandering Signal · 0812",
    region:"Hollow Canopy",
    signal:"a pattern of footprints facing inward",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 7, and its trace number is 812.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 812.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The ground glows for a moment, then settles.",
    reward:"a new depth"
  },
  {
    id:813,
    name:"After the Wandering Signal · 0813",
    region:"Lantern Expanse",
    signal:"a low blue pulse",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 1, and its trace number is 813.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 813.",
    lesson:"Observation can be a form of movement.",
    response:"A new mark appears beside your last footprint.",
    reward:"a changed landmark"
  },
  {
    id:814,
    name:"Between the Wandering Signal · 0814",
    region:"Pale Engine",
    signal:"a ripple crossing dry ground",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 2, and its trace number is 814.",
    clue:"Find the only light that does not pulse. Fragment index: 814.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a hidden passage"
  },
  {
    id:815,
    name:"Above the Wandering Signal · 0815",
    region:"Quiet Reach",
    signal:"a pattern of footprints facing inward",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 3, and its trace number is 815.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 815.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a second chance"
  },
  {
    id:816,
    name:"Below the Wandering Signal · 0816",
    region:"Moss Quarter",
    signal:"a glow hidden inside a crack",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 4, and its trace number is 816.",
    clue:"The safest route is not always the shortest. Fragment index: 816.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a path that remembers"
  },
  {
    id:817,
    name:"The Quiet Machine · 0817",
    region:"Hollow Canopy",
    signal:"a door-shaped gap in the air",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 5, and its trace number is 817.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 817.",
    lesson:"Observation can be a form of movement.",
    response:"The horizon brightens where your route bends.",
    reward:"an echo token"
  },
  {
    id:818,
    name:"A Quiet Machine · 0818",
    region:"Lantern Expanse",
    signal:"a thin thread of silver light",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 6, and its trace number is 818.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 818.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a stored reflection"
  },
  {
    id:819,
    name:"Beneath the Quiet Machine · 0819",
    region:"Pale Engine",
    signal:"a reflection that arrives late",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 7, and its trace number is 819.",
    clue:"A repeated step can open a door, but only once. Fragment index: 819.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A distant light answers with one measured flash.",
    reward:"a new depth"
  },
  {
    id:820,
    name:"Beyond the Quiet Machine · 0820",
    region:"Frostline",
    signal:"a door-shaped gap in the air",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 1, and its trace number is 820.",
    clue:"The second path is real only after you turn away. Fragment index: 820.",
    lesson:"Memory is more than a record of where you went.",
    response:"The path behind you quietly changes its shape.",
    reward:"a quiet clue"
  },
  {
    id:821,
    name:"Inside the Quiet Machine · 0821",
    region:"Last Horizon",
    signal:"a thin thread of silver light",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 2, and its trace number is 821.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 821.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The air grows still, waiting for another choice.",
    reward:"a memory fragment"
  },
  {
    id:822,
    name:"Under the Quiet Machine · 0822",
    region:"Glasswater Basin",
    signal:"a reflection that arrives late",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 3, and its trace number is 822.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 822.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a map trace"
  },
  {
    id:823,
    name:"Across the Quiet Machine · 0823",
    region:"Blue Divide",
    signal:"a shadow moving against the light",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 4, and its trace number is 823.",
    clue:"Return to the place where the floor changes colour. Fragment index: 823.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The echo returns with one extra note.",
    reward:"a sealed memory"
  },
  {
    id:824,
    name:"Behind the Quiet Machine · 0824",
    region:"Ember Archive",
    signal:"a distant bell with no echo",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 5, and its trace number is 824.",
    clue:"The answer is stored in the order of your choices. Fragment index: 824.",
    lesson:"Memory is more than a record of where you went.",
    response:"The ground glows for a moment, then settles.",
    reward:"a clearer signal"
  },
  {
    id:825,
    name:"Within the Quiet Machine · 0825",
    region:"Echo Marsh",
    signal:"a hum that follows silence",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 6, and its trace number is 825.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 825.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A new mark appears beside your last footprint.",
    reward:"a changed landmark"
  },
  {
    id:826,
    name:"At the edge of the Quiet Machine · 0826",
    region:"Last Horizon",
    signal:"a warm line beneath the stone",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 7, and its trace number is 826.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 826.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a hidden passage"
  },
  {
    id:827,
    name:"Where the Quiet Machine · 0827",
    region:"Glasswater Basin",
    signal:"a distant bell with no echo",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 1, and its trace number is 827.",
    clue:"Find the only light that does not pulse. Fragment index: 827.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a second chance"
  },
  {
    id:828,
    name:"Before the Quiet Machine · 0828",
    region:"Blue Divide",
    signal:"a hum that follows silence",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 2, and its trace number is 828.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 828.",
    lesson:"Memory is more than a record of where you went.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a path that remembers"
  },
  {
    id:829,
    name:"After the Quiet Machine · 0829",
    region:"Ember Archive",
    signal:"a warm line beneath the stone",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 3, and its trace number is 829.",
    clue:"The safest route is not always the shortest. Fragment index: 829.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"an echo token"
  },
  {
    id:830,
    name:"Between the Quiet Machine · 0830",
    region:"Echo Marsh",
    signal:"a pale mark that shifts position",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 4, and its trace number is 830.",
    clue:"Your previous route is the map for this one. Fragment index: 830.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A distant light answers with one measured flash.",
    reward:"a stored reflection"
  },
  {
    id:831,
    name:"Above the Quiet Machine · 0831",
    region:"Mirror Waste",
    signal:"a small star below the horizon",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 5, and its trace number is 831.",
    clue:"Move once, pause once, then listen again. Fragment index: 831.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The path behind you quietly changes its shape.",
    reward:"a new depth"
  },
  {
    id:832,
    name:"Below the Quiet Machine · 0832",
    region:"Quiet Reach",
    signal:"three notes with no source",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 6, and its trace number is 832.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 832.",
    lesson:"Memory is more than a record of where you went.",
    response:"The air grows still, waiting for another choice.",
    reward:"a quiet clue"
  },
  {
    id:833,
    name:"The Silver Ravine · 0833",
    region:"Moss Quarter",
    signal:"a slow rhythm under the wind",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 7, and its trace number is 833.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 833.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a memory fragment"
  },
  {
    id:834,
    name:"A Silver Ravine · 0834",
    region:"Hollow Canopy",
    signal:"a small star below the horizon",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 1, and its trace number is 834.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 834.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The echo returns with one extra note.",
    reward:"a map trace"
  },
  {
    id:835,
    name:"Beneath the Silver Ravine · 0835",
    region:"Lantern Expanse",
    signal:"three notes with no source",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 2, and its trace number is 835.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 835.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The ground glows for a moment, then settles.",
    reward:"a sealed memory"
  },
  {
    id:836,
    name:"Beyond the Silver Ravine · 0836",
    region:"Pale Engine",
    signal:"a slow rhythm under the wind",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 3, and its trace number is 836.",
    clue:"Return to the place where the floor changes colour. Fragment index: 836.",
    lesson:"Memory is more than a record of where you went.",
    response:"A new mark appears beside your last footprint.",
    reward:"a clearer signal"
  },
  {
    id:837,
    name:"Inside the Silver Ravine · 0837",
    region:"Quiet Reach",
    signal:"a breath behind the wall",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 4, and its trace number is 837.",
    clue:"The answer is stored in the order of your choices. Fragment index: 837.",
    lesson:"Silence is information when you learn to listen.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a changed landmark"
  },
  {
    id:838,
    name:"Under the Silver Ravine · 0838",
    region:"Moss Quarter",
    signal:"a low blue pulse",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 5, and its trace number is 838.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 838.",
    lesson:"Returning is not the same as repeating.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a hidden passage"
  },
  {
    id:839,
    name:"Across the Silver Ravine · 0839",
    region:"Hollow Canopy",
    signal:"a ripple crossing dry ground",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 6, and its trace number is 839.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 839.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a second chance"
  },
  {
    id:840,
    name:"Behind the Silver Ravine · 0840",
    region:"Lantern Expanse",
    signal:"a pattern of footprints facing inward",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 7, and its trace number is 840.",
    clue:"Find the only light that does not pulse. Fragment index: 840.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The horizon brightens where your route bends.",
    reward:"a path that remembers"
  },
  {
    id:841,
    name:"Within the Silver Ravine · 0841",
    region:"Pale Engine",
    signal:"a low blue pulse",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 1, and its trace number is 841.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 841.",
    lesson:"Silence is information when you learn to listen.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"an echo token"
  },
  {
    id:842,
    name:"At the edge of the Silver Ravine · 0842",
    region:"Frostline",
    signal:"a ripple crossing dry ground",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 2, and its trace number is 842.",
    clue:"The safest route is not always the shortest. Fragment index: 842.",
    lesson:"Returning is not the same as repeating.",
    response:"A distant light answers with one measured flash.",
    reward:"a sealed memory"
  },
  {
    id:843,
    name:"Where the Silver Ravine · 0843",
    region:"Last Horizon",
    signal:"a pattern of footprints facing inward",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 3, and its trace number is 843.",
    clue:"Your previous route is the map for this one. Fragment index: 843.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The path behind you quietly changes its shape.",
    reward:"a clearer signal"
  },
  {
    id:844,
    name:"Before the Silver Ravine · 0844",
    region:"Glasswater Basin",
    signal:"a glow hidden inside a crack",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 4, and its trace number is 844.",
    clue:"Move once, pause once, then listen again. Fragment index: 844.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The air grows still, waiting for another choice.",
    reward:"a changed landmark"
  },
  {
    id:845,
    name:"After the Silver Ravine · 0845",
    region:"Blue Divide",
    signal:"a door-shaped gap in the air",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 5, and its trace number is 845.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 845.",
    lesson:"Silence is information when you learn to listen.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a hidden passage"
  },
  {
    id:846,
    name:"Between the Silver Ravine · 0846",
    region:"Ember Archive",
    signal:"a thin thread of silver light",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 6, and its trace number is 846.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 846.",
    lesson:"Returning is not the same as repeating.",
    response:"The echo returns with one extra note.",
    reward:"a second chance"
  },
  {
    id:847,
    name:"Above the Silver Ravine · 0847",
    region:"Echo Marsh",
    signal:"a reflection that arrives late",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 7, and its trace number is 847.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 847.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The ground glows for a moment, then settles.",
    reward:"a path that remembers"
  },
  {
    id:848,
    name:"Below the Silver Ravine · 0848",
    region:"Last Horizon",
    signal:"a door-shaped gap in the air",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 1, and its trace number is 848.",
    clue:"A repeated step can open a door, but only once. Fragment index: 848.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A new mark appears beside your last footprint.",
    reward:"an echo token"
  },
  {
    id:849,
    name:"The Last Lighthouse · 0849",
    region:"Glasswater Basin",
    signal:"a thin thread of silver light",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 2, and its trace number is 849.",
    clue:"The second path is real only after you turn away. Fragment index: 849.",
    lesson:"Silence is information when you learn to listen.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a stored reflection"
  },
  {
    id:850,
    name:"A Last Lighthouse · 0850",
    region:"Blue Divide",
    signal:"a reflection that arrives late",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 3, and its trace number is 850.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 850.",
    lesson:"Returning is not the same as repeating.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a new depth"
  },
  {
    id:851,
    name:"Beneath the Last Lighthouse · 0851",
    region:"Ember Archive",
    signal:"a shadow moving against the light",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 4, and its trace number is 851.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 851.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a quiet clue"
  },
  {
    id:852,
    name:"Beyond the Last Lighthouse · 0852",
    region:"Echo Marsh",
    signal:"a distant bell with no echo",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 5, and its trace number is 852.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 852.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a memory fragment"
  },
  {
    id:853,
    name:"Inside the Last Lighthouse · 0853",
    region:"Mirror Waste",
    signal:"a hum that follows silence",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 6, and its trace number is 853.",
    clue:"Find the only light that does not pulse. Fragment index: 853.",
    lesson:"Silence is information when you learn to listen.",
    response:"A distant light answers with one measured flash.",
    reward:"a map trace"
  },
  {
    id:854,
    name:"Under the Last Lighthouse · 0854",
    region:"Quiet Reach",
    signal:"a warm line beneath the stone",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 7, and its trace number is 854.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 854.",
    lesson:"Returning is not the same as repeating.",
    response:"The path behind you quietly changes its shape.",
    reward:"a sealed memory"
  },
  {
    id:855,
    name:"Across the Last Lighthouse · 0855",
    region:"Moss Quarter",
    signal:"a distant bell with no echo",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 1, and its trace number is 855.",
    clue:"The safest route is not always the shortest. Fragment index: 855.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The air grows still, waiting for another choice.",
    reward:"a clearer signal"
  },
  {
    id:856,
    name:"Behind the Last Lighthouse · 0856",
    region:"Hollow Canopy",
    signal:"a hum that follows silence",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 2, and its trace number is 856.",
    clue:"Your previous route is the map for this one. Fragment index: 856.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a changed landmark"
  },
  {
    id:857,
    name:"Within the Last Lighthouse · 0857",
    region:"Lantern Expanse",
    signal:"a warm line beneath the stone",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 3, and its trace number is 857.",
    clue:"Move once, pause once, then listen again. Fragment index: 857.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The echo returns with one extra note.",
    reward:"a hidden passage"
  },
  {
    id:858,
    name:"At the edge of the Last Lighthouse · 0858",
    region:"Pale Engine",
    signal:"a pale mark that shifts position",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 4, and its trace number is 858.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 858.",
    lesson:"Observation can be a form of movement.",
    response:"The ground glows for a moment, then settles.",
    reward:"a second chance"
  },
  {
    id:859,
    name:"Where the Last Lighthouse · 0859",
    region:"Quiet Reach",
    signal:"a small star below the horizon",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 5, and its trace number is 859.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 859.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A new mark appears beside your last footprint.",
    reward:"a path that remembers"
  },
  {
    id:860,
    name:"Before the Last Lighthouse · 0860",
    region:"Moss Quarter",
    signal:"three notes with no source",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 6, and its trace number is 860.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 860.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The observer pauses, then follows at a distance.",
    reward:"an echo token"
  },
  {
    id:861,
    name:"After the Last Lighthouse · 0861",
    region:"Hollow Canopy",
    signal:"a slow rhythm under the wind",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 7, and its trace number is 861.",
    clue:"A repeated step can open a door, but only once. Fragment index: 861.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a stored reflection"
  },
  {
    id:862,
    name:"Between the Last Lighthouse · 0862",
    region:"Lantern Expanse",
    signal:"a small star below the horizon",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 1, and its trace number is 862.",
    clue:"The second path is real only after you turn away. Fragment index: 862.",
    lesson:"Observation can be a form of movement.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a new depth"
  },
  {
    id:863,
    name:"Above the Last Lighthouse · 0863",
    region:"Pale Engine",
    signal:"three notes with no source",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 2, and its trace number is 863.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 863.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The horizon brightens where your route bends.",
    reward:"a quiet clue"
  },
  {
    id:864,
    name:"Below the Last Lighthouse · 0864",
    region:"Frostline",
    signal:"a slow rhythm under the wind",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 3, and its trace number is 864.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 864.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a memory fragment"
  },
  {
    id:865,
    name:"The Paper Moon · 0865",
    region:"Last Horizon",
    signal:"a breath behind the wall",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 4, and its trace number is 865.",
    clue:"Return to the place where the floor changes colour. Fragment index: 865.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A distant light answers with one measured flash.",
    reward:"a map trace"
  },
  {
    id:866,
    name:"A Paper Moon · 0866",
    region:"Glasswater Basin",
    signal:"a low blue pulse",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 5, and its trace number is 866.",
    clue:"The answer is stored in the order of your choices. Fragment index: 866.",
    lesson:"Observation can be a form of movement.",
    response:"The path behind you quietly changes its shape.",
    reward:"a sealed memory"
  },
  {
    id:867,
    name:"Beneath the Paper Moon · 0867",
    region:"Blue Divide",
    signal:"a ripple crossing dry ground",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 6, and its trace number is 867.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 867.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The air grows still, waiting for another choice.",
    reward:"a clearer signal"
  },
  {
    id:868,
    name:"Beyond the Paper Moon · 0868",
    region:"Ember Archive",
    signal:"a pattern of footprints facing inward",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 7, and its trace number is 868.",
    clue:"The safest route is not always the shortest. Fragment index: 868.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a changed landmark"
  },
  {
    id:869,
    name:"Inside the Paper Moon · 0869",
    region:"Echo Marsh",
    signal:"a low blue pulse",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 1, and its trace number is 869.",
    clue:"Your previous route is the map for this one. Fragment index: 869.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The echo returns with one extra note.",
    reward:"a hidden passage"
  },
  {
    id:870,
    name:"Under the Paper Moon · 0870",
    region:"Last Horizon",
    signal:"a ripple crossing dry ground",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 2, and its trace number is 870.",
    clue:"Move once, pause once, then listen again. Fragment index: 870.",
    lesson:"Observation can be a form of movement.",
    response:"The ground glows for a moment, then settles.",
    reward:"a second chance"
  },
  {
    id:871,
    name:"Across the Paper Moon · 0871",
    region:"Glasswater Basin",
    signal:"a pattern of footprints facing inward",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 3, and its trace number is 871.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 871.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A new mark appears beside your last footprint.",
    reward:"a memory fragment"
  },
  {
    id:872,
    name:"Behind the Paper Moon · 0872",
    region:"Blue Divide",
    signal:"a glow hidden inside a crack",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 4, and its trace number is 872.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 872.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a map trace"
  },
  {
    id:873,
    name:"Within the Paper Moon · 0873",
    region:"Ember Archive",
    signal:"a door-shaped gap in the air",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 5, and its trace number is 873.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 873.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a sealed memory"
  },
  {
    id:874,
    name:"At the edge of the Paper Moon · 0874",
    region:"Echo Marsh",
    signal:"a thin thread of silver light",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 6, and its trace number is 874.",
    clue:"A repeated step can open a door, but only once. Fragment index: 874.",
    lesson:"Observation can be a form of movement.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a clearer signal"
  },
  {
    id:875,
    name:"Where the Paper Moon · 0875",
    region:"Mirror Waste",
    signal:"a reflection that arrives late",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 7, and its trace number is 875.",
    clue:"The second path is real only after you turn away. Fragment index: 875.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a changed landmark"
  },
  {
    id:876,
    name:"Before the Paper Moon · 0876",
    region:"Quiet Reach",
    signal:"a door-shaped gap in the air",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 1, and its trace number is 876.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 876.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A distant light answers with one measured flash.",
    reward:"a hidden passage"
  },
  {
    id:877,
    name:"After the Paper Moon · 0877",
    region:"Moss Quarter",
    signal:"a thin thread of silver light",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 2, and its trace number is 877.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 877.",
    lesson:"Memory is more than a record of where you went.",
    response:"The path behind you quietly changes its shape.",
    reward:"a second chance"
  },
  {
    id:878,
    name:"Between the Paper Moon · 0878",
    region:"Hollow Canopy",
    signal:"a reflection that arrives late",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 3, and its trace number is 878.",
    clue:"Return to the place where the floor changes colour. Fragment index: 878.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The air grows still, waiting for another choice.",
    reward:"a path that remembers"
  },
  {
    id:879,
    name:"Above the Paper Moon · 0879",
    region:"Lantern Expanse",
    signal:"a shadow moving against the light",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 4, and its trace number is 879.",
    clue:"The answer is stored in the order of your choices. Fragment index: 879.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A small opening appears in the wall of darkness.",
    reward:"an echo token"
  },
  {
    id:880,
    name:"Below the Paper Moon · 0880",
    region:"Pale Engine",
    signal:"a distant bell with no echo",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 5, and its trace number is 880.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 880.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The echo returns with one extra note.",
    reward:"a stored reflection"
  },
  {
    id:881,
    name:"The Frozen River · 0881",
    region:"Quiet Reach",
    signal:"a hum that follows silence",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 6, and its trace number is 881.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 881.",
    lesson:"Memory is more than a record of where you went.",
    response:"The ground glows for a moment, then settles.",
    reward:"a new depth"
  },
  {
    id:882,
    name:"A Frozen River · 0882",
    region:"Moss Quarter",
    signal:"a warm line beneath the stone",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 7, and its trace number is 882.",
    clue:"Find the only light that does not pulse. Fragment index: 882.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A new mark appears beside your last footprint.",
    reward:"a quiet clue"
  },
  {
    id:883,
    name:"Beneath the Frozen River · 0883",
    region:"Hollow Canopy",
    signal:"a distant bell with no echo",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 1, and its trace number is 883.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 883.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a memory fragment"
  },
  {
    id:884,
    name:"Beyond the Frozen River · 0884",
    region:"Lantern Expanse",
    signal:"a hum that follows silence",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 2, and its trace number is 884.",
    clue:"The safest route is not always the shortest. Fragment index: 884.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a map trace"
  },
  {
    id:885,
    name:"Inside the Frozen River · 0885",
    region:"Pale Engine",
    signal:"a warm line beneath the stone",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 3, and its trace number is 885.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 885.",
    lesson:"Memory is more than a record of where you went.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a sealed memory"
  },
  {
    id:886,
    name:"Under the Frozen River · 0886",
    region:"Frostline",
    signal:"a pale mark that shifts position",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 4, and its trace number is 886.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 886.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The horizon brightens where your route bends.",
    reward:"a clearer signal"
  },
  {
    id:887,
    name:"Across the Frozen River · 0887",
    region:"Last Horizon",
    signal:"a small star below the horizon",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 5, and its trace number is 887.",
    clue:"A repeated step can open a door, but only once. Fragment index: 887.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a changed landmark"
  },
  {
    id:888,
    name:"Behind the Frozen River · 0888",
    region:"Glasswater Basin",
    signal:"three notes with no source",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 6, and its trace number is 888.",
    clue:"The second path is real only after you turn away. Fragment index: 888.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A distant light answers with one measured flash.",
    reward:"a hidden passage"
  },
  {
    id:889,
    name:"Within the Frozen River · 0889",
    region:"Blue Divide",
    signal:"a slow rhythm under the wind",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 7, and its trace number is 889.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 889.",
    lesson:"Memory is more than a record of where you went.",
    response:"The path behind you quietly changes its shape.",
    reward:"a second chance"
  },
  {
    id:890,
    name:"At the edge of the Frozen River · 0890",
    region:"Ember Archive",
    signal:"a small star below the horizon",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 1, and its trace number is 890.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 890.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The air grows still, waiting for another choice.",
    reward:"a path that remembers"
  },
  {
    id:891,
    name:"Where the Frozen River · 0891",
    region:"Echo Marsh",
    signal:"three notes with no source",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 2, and its trace number is 891.",
    clue:"Return to the place where the floor changes colour. Fragment index: 891.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A small opening appears in the wall of darkness.",
    reward:"an echo token"
  },
  {
    id:892,
    name:"Before the Frozen River · 0892",
    region:"Last Horizon",
    signal:"a slow rhythm under the wind",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 3, and its trace number is 892.",
    clue:"The answer is stored in the order of your choices. Fragment index: 892.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The echo returns with one extra note.",
    reward:"a stored reflection"
  },
  {
    id:893,
    name:"After the Frozen River · 0893",
    region:"Glasswater Basin",
    signal:"a breath behind the wall",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 4, and its trace number is 893.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 893.",
    lesson:"Memory is more than a record of where you went.",
    response:"The ground glows for a moment, then settles.",
    reward:"a new depth"
  },
  {
    id:894,
    name:"Between the Frozen River · 0894",
    region:"Blue Divide",
    signal:"a low blue pulse",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 5, and its trace number is 894.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 894.",
    lesson:"Silence is information when you learn to listen.",
    response:"A new mark appears beside your last footprint.",
    reward:"a quiet clue"
  },
  {
    id:895,
    name:"Above the Frozen River · 0895",
    region:"Ember Archive",
    signal:"a ripple crossing dry ground",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 6, and its trace number is 895.",
    clue:"Find the only light that does not pulse. Fragment index: 895.",
    lesson:"Returning is not the same as repeating.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a memory fragment"
  },
  {
    id:896,
    name:"Below the Frozen River · 0896",
    region:"Echo Marsh",
    signal:"a pattern of footprints facing inward",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 7, and its trace number is 896.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 896.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a map trace"
  },
  {
    id:897,
    name:"The Lantern Maze · 0897",
    region:"Mirror Waste",
    signal:"a low blue pulse",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 1, and its trace number is 897.",
    clue:"The safest route is not always the shortest. Fragment index: 897.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a sealed memory"
  },
  {
    id:898,
    name:"A Lantern Maze · 0898",
    region:"Quiet Reach",
    signal:"a ripple crossing dry ground",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 2, and its trace number is 898.",
    clue:"Your previous route is the map for this one. Fragment index: 898.",
    lesson:"Silence is information when you learn to listen.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a clearer signal"
  },
  {
    id:899,
    name:"Beneath the Lantern Maze · 0899",
    region:"Moss Quarter",
    signal:"a pattern of footprints facing inward",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 3, and its trace number is 899.",
    clue:"Move once, pause once, then listen again. Fragment index: 899.",
    lesson:"Returning is not the same as repeating.",
    response:"A distant light answers with one measured flash.",
    reward:"a changed landmark"
  },
  {
    id:900,
    name:"Beyond the Lantern Maze · 0900",
    region:"Hollow Canopy",
    signal:"a glow hidden inside a crack",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 4, and its trace number is 900.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 900.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The path behind you quietly changes its shape.",
    reward:"a new depth"
  },
  {
    id:901,
    name:"Inside the Lantern Maze · 0901",
    region:"Lantern Expanse",
    signal:"a door-shaped gap in the air",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 5, and its trace number is 901.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 901.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The air grows still, waiting for another choice.",
    reward:"a quiet clue"
  },
  {
    id:902,
    name:"Under the Lantern Maze · 0902",
    region:"Pale Engine",
    signal:"a thin thread of silver light",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 6, and its trace number is 902.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 902.",
    lesson:"Silence is information when you learn to listen.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a memory fragment"
  },
  {
    id:903,
    name:"Across the Lantern Maze · 0903",
    region:"Quiet Reach",
    signal:"a reflection that arrives late",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 7, and its trace number is 903.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 903.",
    lesson:"Returning is not the same as repeating.",
    response:"The echo returns with one extra note.",
    reward:"a map trace"
  },
  {
    id:904,
    name:"Behind the Lantern Maze · 0904",
    region:"Moss Quarter",
    signal:"a door-shaped gap in the air",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 1, and its trace number is 904.",
    clue:"Return to the place where the floor changes colour. Fragment index: 904.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The ground glows for a moment, then settles.",
    reward:"a sealed memory"
  },
  {
    id:905,
    name:"Within the Lantern Maze · 0905",
    region:"Hollow Canopy",
    signal:"a thin thread of silver light",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 2, and its trace number is 905.",
    clue:"The answer is stored in the order of your choices. Fragment index: 905.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A new mark appears beside your last footprint.",
    reward:"a clearer signal"
  },
  {
    id:906,
    name:"At the edge of the Lantern Maze · 0906",
    region:"Lantern Expanse",
    signal:"a reflection that arrives late",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 3, and its trace number is 906.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 906.",
    lesson:"Silence is information when you learn to listen.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a changed landmark"
  },
  {
    id:907,
    name:"Where the Lantern Maze · 0907",
    region:"Pale Engine",
    signal:"a shadow moving against the light",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 4, and its trace number is 907.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 907.",
    lesson:"Returning is not the same as repeating.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a hidden passage"
  },
  {
    id:908,
    name:"Before the Lantern Maze · 0908",
    region:"Frostline",
    signal:"a distant bell with no echo",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 5, and its trace number is 908.",
    clue:"Find the only light that does not pulse. Fragment index: 908.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a second chance"
  },
  {
    id:909,
    name:"After the Lantern Maze · 0909",
    region:"Last Horizon",
    signal:"a hum that follows silence",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 6, and its trace number is 909.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 909.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The horizon brightens where your route bends.",
    reward:"a path that remembers"
  },
  {
    id:910,
    name:"Between the Lantern Maze · 0910",
    region:"Glasswater Basin",
    signal:"a warm line beneath the stone",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 7, and its trace number is 910.",
    clue:"The safest route is not always the shortest. Fragment index: 910.",
    lesson:"Silence is information when you learn to listen.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"an echo token"
  },
  {
    id:911,
    name:"Above the Lantern Maze · 0911",
    region:"Blue Divide",
    signal:"a distant bell with no echo",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 1, and its trace number is 911.",
    clue:"Your previous route is the map for this one. Fragment index: 911.",
    lesson:"Returning is not the same as repeating.",
    response:"A distant light answers with one measured flash.",
    reward:"a stored reflection"
  },
  {
    id:912,
    name:"Below the Lantern Maze · 0912",
    region:"Ember Archive",
    signal:"a hum that follows silence",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 2, and its trace number is 912.",
    clue:"Move once, pause once, then listen again. Fragment index: 912.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The path behind you quietly changes its shape.",
    reward:"a new depth"
  },
  {
    id:913,
    name:"The Echo Chamber · 0913",
    region:"Echo Marsh",
    signal:"a warm line beneath the stone",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 3, and its trace number is 913.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 913.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The air grows still, waiting for another choice.",
    reward:"a quiet clue"
  },
  {
    id:914,
    name:"A Echo Chamber · 0914",
    region:"Last Horizon",
    signal:"a pale mark that shifts position",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 4, and its trace number is 914.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 914.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a memory fragment"
  },
  {
    id:915,
    name:"Beneath the Echo Chamber · 0915",
    region:"Glasswater Basin",
    signal:"a small star below the horizon",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 5, and its trace number is 915.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 915.",
    lesson:"Observation can be a form of movement.",
    response:"The echo returns with one extra note.",
    reward:"a map trace"
  },
  {
    id:916,
    name:"Beyond the Echo Chamber · 0916",
    region:"Blue Divide",
    signal:"three notes with no source",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 6, and its trace number is 916.",
    clue:"A repeated step can open a door, but only once. Fragment index: 916.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The ground glows for a moment, then settles.",
    reward:"a sealed memory"
  },
  {
    id:917,
    name:"Inside the Echo Chamber · 0917",
    region:"Ember Archive",
    signal:"a slow rhythm under the wind",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 7, and its trace number is 917.",
    clue:"The second path is real only after you turn away. Fragment index: 917.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A new mark appears beside your last footprint.",
    reward:"a clearer signal"
  },
  {
    id:918,
    name:"Under the Echo Chamber · 0918",
    region:"Echo Marsh",
    signal:"a small star below the horizon",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 1, and its trace number is 918.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 918.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a changed landmark"
  },
  {
    id:919,
    name:"Across the Echo Chamber · 0919",
    region:"Mirror Waste",
    signal:"three notes with no source",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 2, and its trace number is 919.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 919.",
    lesson:"Observation can be a form of movement.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a hidden passage"
  },
  {
    id:920,
    name:"Behind the Echo Chamber · 0920",
    region:"Quiet Reach",
    signal:"a slow rhythm under the wind",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 3, and its trace number is 920.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 920.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a second chance"
  },
  {
    id:921,
    name:"Within the Echo Chamber · 0921",
    region:"Moss Quarter",
    signal:"a breath behind the wall",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 4, and its trace number is 921.",
    clue:"Find the only light that does not pulse. Fragment index: 921.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a path that remembers"
  },
  {
    id:922,
    name:"At the edge of the Echo Chamber · 0922",
    region:"Hollow Canopy",
    signal:"a low blue pulse",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 5, and its trace number is 922.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 922.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A distant light answers with one measured flash.",
    reward:"an echo token"
  },
  {
    id:923,
    name:"Where the Echo Chamber · 0923",
    region:"Lantern Expanse",
    signal:"a ripple crossing dry ground",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 6, and its trace number is 923.",
    clue:"The safest route is not always the shortest. Fragment index: 923.",
    lesson:"Observation can be a form of movement.",
    response:"The path behind you quietly changes its shape.",
    reward:"a stored reflection"
  },
  {
    id:924,
    name:"Before the Echo Chamber · 0924",
    region:"Pale Engine",
    signal:"a pattern of footprints facing inward",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 7, and its trace number is 924.",
    clue:"Your previous route is the map for this one. Fragment index: 924.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The air grows still, waiting for another choice.",
    reward:"a new depth"
  },
  {
    id:925,
    name:"After the Echo Chamber · 0925",
    region:"Quiet Reach",
    signal:"a low blue pulse",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 1, and its trace number is 925.",
    clue:"Move once, pause once, then listen again. Fragment index: 925.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a quiet clue"
  },
  {
    id:926,
    name:"Between the Echo Chamber · 0926",
    region:"Moss Quarter",
    signal:"a ripple crossing dry ground",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 2, and its trace number is 926.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 926.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The echo returns with one extra note.",
    reward:"a memory fragment"
  },
  {
    id:927,
    name:"Above the Echo Chamber · 0927",
    region:"Hollow Canopy",
    signal:"a pattern of footprints facing inward",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 3, and its trace number is 927.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 927.",
    lesson:"Observation can be a form of movement.",
    response:"The ground glows for a moment, then settles.",
    reward:"a map trace"
  },
  {
    id:928,
    name:"Below the Echo Chamber · 0928",
    region:"Lantern Expanse",
    signal:"a glow hidden inside a crack",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 4, and its trace number is 928.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 928.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A new mark appears beside your last footprint.",
    reward:"a sealed memory"
  },
  {
    id:929,
    name:"The Broken Compass · 0929",
    region:"Pale Engine",
    signal:"a door-shaped gap in the air",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 5, and its trace number is 929.",
    clue:"A repeated step can open a door, but only once. Fragment index: 929.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The observer pauses, then follows at a distance.",
    reward:"an echo token"
  },
  {
    id:930,
    name:"A Broken Compass · 0930",
    region:"Frostline",
    signal:"a thin thread of silver light",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 6, and its trace number is 930.",
    clue:"The second path is real only after you turn away. Fragment index: 930.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a stored reflection"
  },
  {
    id:931,
    name:"Beneath the Broken Compass · 0931",
    region:"Last Horizon",
    signal:"a reflection that arrives late",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 7, and its trace number is 931.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 931.",
    lesson:"Observation can be a form of movement.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a new depth"
  },
  {
    id:932,
    name:"Beyond the Broken Compass · 0932",
    region:"Glasswater Basin",
    signal:"a door-shaped gap in the air",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 1, and its trace number is 932.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 932.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The horizon brightens where your route bends.",
    reward:"a quiet clue"
  },
  {
    id:933,
    name:"Inside the Broken Compass · 0933",
    region:"Blue Divide",
    signal:"a thin thread of silver light",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 2, and its trace number is 933.",
    clue:"Return to the place where the floor changes colour. Fragment index: 933.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a memory fragment"
  },
  {
    id:934,
    name:"Under the Broken Compass · 0934",
    region:"Ember Archive",
    signal:"a reflection that arrives late",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 3, and its trace number is 934.",
    clue:"The answer is stored in the order of your choices. Fragment index: 934.",
    lesson:"Memory is more than a record of where you went.",
    response:"A distant light answers with one measured flash.",
    reward:"a map trace"
  },
  {
    id:935,
    name:"Across the Broken Compass · 0935",
    region:"Echo Marsh",
    signal:"a shadow moving against the light",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 4, and its trace number is 935.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 935.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The path behind you quietly changes its shape.",
    reward:"a sealed memory"
  },
  {
    id:936,
    name:"Behind the Broken Compass · 0936",
    region:"Last Horizon",
    signal:"a distant bell with no echo",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 5, and its trace number is 936.",
    clue:"The safest route is not always the shortest. Fragment index: 936.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The air grows still, waiting for another choice.",
    reward:"a clearer signal"
  },
  {
    id:937,
    name:"Within the Broken Compass · 0937",
    region:"Glasswater Basin",
    signal:"a hum that follows silence",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 6, and its trace number is 937.",
    clue:"Your previous route is the map for this one. Fragment index: 937.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a changed landmark"
  },
  {
    id:938,
    name:"At the edge of the Broken Compass · 0938",
    region:"Blue Divide",
    signal:"a warm line beneath the stone",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 7, and its trace number is 938.",
    clue:"Move once, pause once, then listen again. Fragment index: 938.",
    lesson:"Memory is more than a record of where you went.",
    response:"The echo returns with one extra note.",
    reward:"a hidden passage"
  },
  {
    id:939,
    name:"Where the Broken Compass · 0939",
    region:"Ember Archive",
    signal:"a distant bell with no echo",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 1, and its trace number is 939.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 939.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The ground glows for a moment, then settles.",
    reward:"a second chance"
  },
  {
    id:940,
    name:"Before the Broken Compass · 0940",
    region:"Echo Marsh",
    signal:"a hum that follows silence",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 2, and its trace number is 940.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 940.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A new mark appears beside your last footprint.",
    reward:"a path that remembers"
  },
  {
    id:941,
    name:"After the Broken Compass · 0941",
    region:"Mirror Waste",
    signal:"a warm line beneath the stone",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 3, and its trace number is 941.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 941.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The observer pauses, then follows at a distance.",
    reward:"an echo token"
  },
  {
    id:942,
    name:"Between the Broken Compass · 0942",
    region:"Quiet Reach",
    signal:"a pale mark that shifts position",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 4, and its trace number is 942.",
    clue:"A repeated step can open a door, but only once. Fragment index: 942.",
    lesson:"Memory is more than a record of where you went.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a stored reflection"
  },
  {
    id:943,
    name:"Above the Broken Compass · 0943",
    region:"Moss Quarter",
    signal:"a small star below the horizon",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 5, and its trace number is 943.",
    clue:"The second path is real only after you turn away. Fragment index: 943.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a new depth"
  },
  {
    id:944,
    name:"Below the Broken Compass · 0944",
    region:"Hollow Canopy",
    signal:"three notes with no source",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 6, and its trace number is 944.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 944.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a quiet clue"
  },
  {
    id:945,
    name:"The Hidden Shore · 0945",
    region:"Lantern Expanse",
    signal:"a slow rhythm under the wind",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 7, and its trace number is 945.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 945.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A distant light answers with one measured flash.",
    reward:"a memory fragment"
  },
  {
    id:946,
    name:"A Hidden Shore · 0946",
    region:"Pale Engine",
    signal:"a small star below the horizon",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 1, and its trace number is 946.",
    clue:"Return to the place where the floor changes colour. Fragment index: 946.",
    lesson:"Memory is more than a record of where you went.",
    response:"The path behind you quietly changes its shape.",
    reward:"a map trace"
  },
  {
    id:947,
    name:"Beneath the Hidden Shore · 0947",
    region:"Quiet Reach",
    signal:"three notes with no source",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 2, and its trace number is 947.",
    clue:"The answer is stored in the order of your choices. Fragment index: 947.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The air grows still, waiting for another choice.",
    reward:"a sealed memory"
  },
  {
    id:948,
    name:"Beyond the Hidden Shore · 0948",
    region:"Moss Quarter",
    signal:"a slow rhythm under the wind",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 3, and its trace number is 948.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 948.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a clearer signal"
  },
  {
    id:949,
    name:"Inside the Hidden Shore · 0949",
    region:"Hollow Canopy",
    signal:"a breath behind the wall",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 4, and its trace number is 949.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 949.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The echo returns with one extra note.",
    reward:"a changed landmark"
  },
  {
    id:950,
    name:"Under the Hidden Shore · 0950",
    region:"Lantern Expanse",
    signal:"a low blue pulse",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 5, and its trace number is 950.",
    clue:"Find the only light that does not pulse. Fragment index: 950.",
    lesson:"Memory is more than a record of where you went.",
    response:"The ground glows for a moment, then settles.",
    reward:"a hidden passage"
  },
  {
    id:951,
    name:"Across the Hidden Shore · 0951",
    region:"Pale Engine",
    signal:"a ripple crossing dry ground",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 6, and its trace number is 951.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 951.",
    lesson:"Silence is information when you learn to listen.",
    response:"A new mark appears beside your last footprint.",
    reward:"a second chance"
  },
  {
    id:952,
    name:"Behind the Hidden Shore · 0952",
    region:"Frostline",
    signal:"a pattern of footprints facing inward",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 7, and its trace number is 952.",
    clue:"The safest route is not always the shortest. Fragment index: 952.",
    lesson:"Returning is not the same as repeating.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a path that remembers"
  },
  {
    id:953,
    name:"Within the Hidden Shore · 0953",
    region:"Last Horizon",
    signal:"a low blue pulse",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 1, and its trace number is 953.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 953.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"an echo token"
  },
  {
    id:954,
    name:"At the edge of the Hidden Shore · 0954",
    region:"Glasswater Basin",
    signal:"a ripple crossing dry ground",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 2, and its trace number is 954.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 954.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a stored reflection"
  },
  {
    id:955,
    name:"Where the Hidden Shore · 0955",
    region:"Blue Divide",
    signal:"a pattern of footprints facing inward",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 3, and its trace number is 955.",
    clue:"A repeated step can open a door, but only once. Fragment index: 955.",
    lesson:"Silence is information when you learn to listen.",
    response:"The horizon brightens where your route bends.",
    reward:"a new depth"
  },
  {
    id:956,
    name:"Before the Hidden Shore · 0956",
    region:"Ember Archive",
    signal:"a glow hidden inside a crack",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 4, and its trace number is 956.",
    clue:"The second path is real only after you turn away. Fragment index: 956.",
    lesson:"Returning is not the same as repeating.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a quiet clue"
  },
  {
    id:957,
    name:"After the Hidden Shore · 0957",
    region:"Echo Marsh",
    signal:"a door-shaped gap in the air",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 5, and its trace number is 957.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 957.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A distant light answers with one measured flash.",
    reward:"a memory fragment"
  },
  {
    id:958,
    name:"Between the Hidden Shore · 0958",
    region:"Last Horizon",
    signal:"a thin thread of silver light",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 6, and its trace number is 958.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 958.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The path behind you quietly changes its shape.",
    reward:"a second chance"
  },
  {
    id:959,
    name:"Above the Hidden Shore · 0959",
    region:"Glasswater Basin",
    signal:"a reflection that arrives late",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 7, and its trace number is 959.",
    clue:"Return to the place where the floor changes colour. Fragment index: 959.",
    lesson:"Silence is information when you learn to listen.",
    response:"The air grows still, waiting for another choice.",
    reward:"a path that remembers"
  },
  {
    id:960,
    name:"Below the Hidden Shore · 0960",
    region:"Blue Divide",
    signal:"a door-shaped gap in the air",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 1, and its trace number is 960.",
    clue:"The answer is stored in the order of your choices. Fragment index: 960.",
    lesson:"Returning is not the same as repeating.",
    response:"A small opening appears in the wall of darkness.",
    reward:"an echo token"
  },
  {
    id:961,
    name:"The Velvet Storm · 0961",
    region:"Ember Archive",
    signal:"a thin thread of silver light",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 2, and its trace number is 961.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 961.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The echo returns with one extra note.",
    reward:"a stored reflection"
  },
  {
    id:962,
    name:"A Velvet Storm · 0962",
    region:"Echo Marsh",
    signal:"a reflection that arrives late",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 3, and its trace number is 962.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 962.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The ground glows for a moment, then settles.",
    reward:"a new depth"
  },
  {
    id:963,
    name:"Beneath the Velvet Storm · 0963",
    region:"Mirror Waste",
    signal:"a shadow moving against the light",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 4, and its trace number is 963.",
    clue:"Find the only light that does not pulse. Fragment index: 963.",
    lesson:"Silence is information when you learn to listen.",
    response:"A new mark appears beside your last footprint.",
    reward:"a quiet clue"
  },
  {
    id:964,
    name:"Beyond the Velvet Storm · 0964",
    region:"Quiet Reach",
    signal:"a distant bell with no echo",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 5, and its trace number is 964.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 964.",
    lesson:"Returning is not the same as repeating.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a memory fragment"
  },
  {
    id:965,
    name:"Inside the Velvet Storm · 0965",
    region:"Moss Quarter",
    signal:"a hum that follows silence",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 6, and its trace number is 965.",
    clue:"The safest route is not always the shortest. Fragment index: 965.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a map trace"
  },
  {
    id:966,
    name:"Under the Velvet Storm · 0966",
    region:"Hollow Canopy",
    signal:"a warm line beneath the stone",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 7, and its trace number is 966.",
    clue:"Your previous route is the map for this one. Fragment index: 966.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a sealed memory"
  },
  {
    id:967,
    name:"Across the Velvet Storm · 0967",
    region:"Lantern Expanse",
    signal:"a distant bell with no echo",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 1, and its trace number is 967.",
    clue:"Move once, pause once, then listen again. Fragment index: 967.",
    lesson:"Silence is information when you learn to listen.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a clearer signal"
  },
  {
    id:968,
    name:"Behind the Velvet Storm · 0968",
    region:"Pale Engine",
    signal:"a hum that follows silence",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 2, and its trace number is 968.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 968.",
    lesson:"Returning is not the same as repeating.",
    response:"A distant light answers with one measured flash.",
    reward:"a changed landmark"
  },
  {
    id:969,
    name:"Within the Velvet Storm · 0969",
    region:"Quiet Reach",
    signal:"a warm line beneath the stone",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 3, and its trace number is 969.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 969.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The path behind you quietly changes its shape.",
    reward:"a hidden passage"
  },
  {
    id:970,
    name:"At the edge of the Velvet Storm · 0970",
    region:"Moss Quarter",
    signal:"a pale mark that shifts position",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 4, and its trace number is 970.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 970.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The air grows still, waiting for another choice.",
    reward:"a second chance"
  },
  {
    id:971,
    name:"Where the Velvet Storm · 0971",
    region:"Hollow Canopy",
    signal:"a small star below the horizon",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 5, and its trace number is 971.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 971.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a path that remembers"
  },
  {
    id:972,
    name:"Before the Velvet Storm · 0972",
    region:"Lantern Expanse",
    signal:"three notes with no source",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 6, and its trace number is 972.",
    clue:"Return to the place where the floor changes colour. Fragment index: 972.",
    lesson:"Observation can be a form of movement.",
    response:"The echo returns with one extra note.",
    reward:"an echo token"
  },
  {
    id:973,
    name:"After the Velvet Storm · 0973",
    region:"Pale Engine",
    signal:"a slow rhythm under the wind",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 7, and its trace number is 973.",
    clue:"The answer is stored in the order of your choices. Fragment index: 973.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The ground glows for a moment, then settles.",
    reward:"a stored reflection"
  },
  {
    id:974,
    name:"Between the Velvet Storm · 0974",
    region:"Frostline",
    signal:"a small star below the horizon",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 1, and its trace number is 974.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 974.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A new mark appears beside your last footprint.",
    reward:"a new depth"
  },
  {
    id:975,
    name:"Above the Velvet Storm · 0975",
    region:"Last Horizon",
    signal:"three notes with no source",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 2, and its trace number is 975.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 975.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a quiet clue"
  },
  {
    id:976,
    name:"Below the Velvet Storm · 0976",
    region:"Glasswater Basin",
    signal:"a slow rhythm under the wind",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 3, and its trace number is 976.",
    clue:"Find the only light that does not pulse. Fragment index: 976.",
    lesson:"Observation can be a form of movement.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a memory fragment"
  },
  {
    id:977,
    name:"The Clockwork Nest · 0977",
    region:"Blue Divide",
    signal:"a breath behind the wall",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 4, and its trace number is 977.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 977.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a map trace"
  },
  {
    id:978,
    name:"A Clockwork Nest · 0978",
    region:"Ember Archive",
    signal:"a low blue pulse",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 5, and its trace number is 978.",
    clue:"The safest route is not always the shortest. Fragment index: 978.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The horizon brightens where your route bends.",
    reward:"a sealed memory"
  },
  {
    id:979,
    name:"Beneath the Clockwork Nest · 0979",
    region:"Echo Marsh",
    signal:"a ripple crossing dry ground",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 6, and its trace number is 979.",
    clue:"Your previous route is the map for this one. Fragment index: 979.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a clearer signal"
  },
  {
    id:980,
    name:"Beyond the Clockwork Nest · 0980",
    region:"Last Horizon",
    signal:"a pattern of footprints facing inward",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 7, and its trace number is 980.",
    clue:"Move once, pause once, then listen again. Fragment index: 980.",
    lesson:"Observation can be a form of movement.",
    response:"A distant light answers with one measured flash.",
    reward:"a changed landmark"
  },
  {
    id:981,
    name:"Inside the Clockwork Nest · 0981",
    region:"Glasswater Basin",
    signal:"a low blue pulse",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 1, and its trace number is 981.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 981.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The path behind you quietly changes its shape.",
    reward:"a hidden passage"
  },
  {
    id:982,
    name:"Under the Clockwork Nest · 0982",
    region:"Blue Divide",
    signal:"a ripple crossing dry ground",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 2, and its trace number is 982.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 982.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The air grows still, waiting for another choice.",
    reward:"a second chance"
  },
  {
    id:983,
    name:"Across the Clockwork Nest · 0983",
    region:"Ember Archive",
    signal:"a pattern of footprints facing inward",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 3, and its trace number is 983.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 983.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a path that remembers"
  },
  {
    id:984,
    name:"Behind the Clockwork Nest · 0984",
    region:"Echo Marsh",
    signal:"a glow hidden inside a crack",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 4, and its trace number is 984.",
    clue:"A repeated step can open a door, but only once. Fragment index: 984.",
    lesson:"Observation can be a form of movement.",
    response:"The echo returns with one extra note.",
    reward:"an echo token"
  },
  {
    id:985,
    name:"Within the Clockwork Nest · 0985",
    region:"Mirror Waste",
    signal:"a door-shaped gap in the air",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 5, and its trace number is 985.",
    clue:"The second path is real only after you turn away. Fragment index: 985.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The ground glows for a moment, then settles.",
    reward:"a stored reflection"
  },
  {
    id:986,
    name:"At the edge of the Clockwork Nest · 0986",
    region:"Quiet Reach",
    signal:"a thin thread of silver light",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 6, and its trace number is 986.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 986.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A new mark appears beside your last footprint.",
    reward:"a new depth"
  },
  {
    id:987,
    name:"Where the Clockwork Nest · 0987",
    region:"Moss Quarter",
    signal:"a reflection that arrives late",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 7, and its trace number is 987.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 987.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a changed landmark"
  },
  {
    id:988,
    name:"Before the Clockwork Nest · 0988",
    region:"Hollow Canopy",
    signal:"a door-shaped gap in the air",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 1, and its trace number is 988.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 988.",
    lesson:"Observation can be a form of movement.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a hidden passage"
  },
  {
    id:989,
    name:"After the Clockwork Nest · 0989",
    region:"Lantern Expanse",
    signal:"a thin thread of silver light",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 2, and its trace number is 989.",
    clue:"Find the only light that does not pulse. Fragment index: 989.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a second chance"
  },
  {
    id:990,
    name:"Between the Clockwork Nest · 0990",
    region:"Pale Engine",
    signal:"a reflection that arrives late",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 3, and its trace number is 990.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 990.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a path that remembers"
  },
  {
    id:991,
    name:"Above the Clockwork Nest · 0991",
    region:"Quiet Reach",
    signal:"a shadow moving against the light",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 4, and its trace number is 991.",
    clue:"The safest route is not always the shortest. Fragment index: 991.",
    lesson:"Memory is more than a record of where you went.",
    response:"A distant light answers with one measured flash.",
    reward:"an echo token"
  },
  {
    id:992,
    name:"Below the Clockwork Nest · 0992",
    region:"Moss Quarter",
    signal:"a distant bell with no echo",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 5, and its trace number is 992.",
    clue:"Your previous route is the map for this one. Fragment index: 992.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The path behind you quietly changes its shape.",
    reward:"a stored reflection"
  },
  {
    id:993,
    name:"The Empty Theatre · 0993",
    region:"Hollow Canopy",
    signal:"a hum that follows silence",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 6, and its trace number is 993.",
    clue:"Move once, pause once, then listen again. Fragment index: 993.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The air grows still, waiting for another choice.",
    reward:"a new depth"
  },
  {
    id:994,
    name:"A Empty Theatre · 0994",
    region:"Lantern Expanse",
    signal:"a warm line beneath the stone",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 7, and its trace number is 994.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 994.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a quiet clue"
  },
  {
    id:995,
    name:"Beneath the Empty Theatre · 0995",
    region:"Pale Engine",
    signal:"a distant bell with no echo",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 1, and its trace number is 995.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 995.",
    lesson:"Memory is more than a record of where you went.",
    response:"The echo returns with one extra note.",
    reward:"a memory fragment"
  },
  {
    id:996,
    name:"Beyond the Empty Theatre · 0996",
    region:"Frostline",
    signal:"a hum that follows silence",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 2, and its trace number is 996.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 996.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The ground glows for a moment, then settles.",
    reward:"a map trace"
  },
  {
    id:997,
    name:"Inside the Empty Theatre · 0997",
    region:"Last Horizon",
    signal:"a warm line beneath the stone",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 3, and its trace number is 997.",
    clue:"A repeated step can open a door, but only once. Fragment index: 997.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A new mark appears beside your last footprint.",
    reward:"a sealed memory"
  },
  {
    id:998,
    name:"Under the Empty Theatre · 0998",
    region:"Glasswater Basin",
    signal:"a pale mark that shifts position",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 4, and its trace number is 998.",
    clue:"The second path is real only after you turn away. Fragment index: 998.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a clearer signal"
  },
  {
    id:999,
    name:"Across the Empty Theatre · 0999",
    region:"Blue Divide",
    signal:"a small star below the horizon",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 5, and its trace number is 999.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 999.",
    lesson:"Memory is more than a record of where you went.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a changed landmark"
  },
  {
    id:1000,
    name:"Behind the Empty Theatre · 1000",
    region:"Ember Archive",
    signal:"three notes with no source",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 6, and its trace number is 1000.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 1000.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a hidden passage"
  },
  {
    id:1001,
    name:"Within the Empty Theatre · 1001",
    region:"Echo Marsh",
    signal:"a slow rhythm under the wind",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 7, and its trace number is 1001.",
    clue:"Return to the place where the floor changes colour. Fragment index: 1001.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The horizon brightens where your route bends.",
    reward:"a second chance"
  },
  {
    id:1002,
    name:"At the edge of the Empty Theatre · 1002",
    region:"Last Horizon",
    signal:"a small star below the horizon",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 1, and its trace number is 1002.",
    clue:"The answer is stored in the order of your choices. Fragment index: 1002.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a path that remembers"
  },
  {
    id:1003,
    name:"Where the Empty Theatre · 1003",
    region:"Glasswater Basin",
    signal:"three notes with no source",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 2, and its trace number is 1003.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1003.",
    lesson:"Memory is more than a record of where you went.",
    response:"A distant light answers with one measured flash.",
    reward:"an echo token"
  },
  {
    id:1004,
    name:"Before the Empty Theatre · 1004",
    region:"Blue Divide",
    signal:"a slow rhythm under the wind",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 3, and its trace number is 1004.",
    clue:"The safest route is not always the shortest. Fragment index: 1004.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The path behind you quietly changes its shape.",
    reward:"a stored reflection"
  },
  {
    id:1005,
    name:"After the Empty Theatre · 1005",
    region:"Ember Archive",
    signal:"a breath behind the wall",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 4, and its trace number is 1005.",
    clue:"Your previous route is the map for this one. Fragment index: 1005.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The air grows still, waiting for another choice.",
    reward:"a new depth"
  },
  {
    id:1006,
    name:"Between the Empty Theatre · 1006",
    region:"Echo Marsh",
    signal:"a low blue pulse",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 5, and its trace number is 1006.",
    clue:"Move once, pause once, then listen again. Fragment index: 1006.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a quiet clue"
  },
  {
    id:1007,
    name:"Above the Empty Theatre · 1007",
    region:"Mirror Waste",
    signal:"a ripple crossing dry ground",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 6, and its trace number is 1007.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 1007.",
    lesson:"Memory is more than a record of where you went.",
    response:"The echo returns with one extra note.",
    reward:"a memory fragment"
  },
  {
    id:1008,
    name:"Below the Empty Theatre · 1008",
    region:"Quiet Reach",
    signal:"a pattern of footprints facing inward",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 7, and its trace number is 1008.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1008.",
    lesson:"Silence is information when you learn to listen.",
    response:"The ground glows for a moment, then settles.",
    reward:"a map trace"
  },
  {
    id:1009,
    name:"The Moss Cathedral · 1009",
    region:"Moss Quarter",
    signal:"a low blue pulse",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 1, and its trace number is 1009.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 1009.",
    lesson:"Returning is not the same as repeating.",
    response:"A new mark appears beside your last footprint.",
    reward:"a sealed memory"
  },
  {
    id:1010,
    name:"A Moss Cathedral · 1010",
    region:"Hollow Canopy",
    signal:"a ripple crossing dry ground",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 2, and its trace number is 1010.",
    clue:"A repeated step can open a door, but only once. Fragment index: 1010.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a clearer signal"
  },
  {
    id:1011,
    name:"Beneath the Moss Cathedral · 1011",
    region:"Lantern Expanse",
    signal:"a pattern of footprints facing inward",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 3, and its trace number is 1011.",
    clue:"The second path is real only after you turn away. Fragment index: 1011.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a changed landmark"
  },
  {
    id:1012,
    name:"Beyond the Moss Cathedral · 1012",
    region:"Pale Engine",
    signal:"a glow hidden inside a crack",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 4, and its trace number is 1012.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 1012.",
    lesson:"Silence is information when you learn to listen.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a hidden passage"
  },
  {
    id:1013,
    name:"Inside the Moss Cathedral · 1013",
    region:"Quiet Reach",
    signal:"a door-shaped gap in the air",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 5, and its trace number is 1013.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 1013.",
    lesson:"Returning is not the same as repeating.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a second chance"
  },
  {
    id:1014,
    name:"Under the Moss Cathedral · 1014",
    region:"Moss Quarter",
    signal:"a thin thread of silver light",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 6, and its trace number is 1014.",
    clue:"Return to the place where the floor changes colour. Fragment index: 1014.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A distant light answers with one measured flash.",
    reward:"a path that remembers"
  },
  {
    id:1015,
    name:"Across the Moss Cathedral · 1015",
    region:"Hollow Canopy",
    signal:"a reflection that arrives late",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 7, and its trace number is 1015.",
    clue:"The answer is stored in the order of your choices. Fragment index: 1015.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The path behind you quietly changes its shape.",
    reward:"an echo token"
  },
  {
    id:1016,
    name:"Behind the Moss Cathedral · 1016",
    region:"Lantern Expanse",
    signal:"a door-shaped gap in the air",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 1, and its trace number is 1016.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1016.",
    lesson:"Silence is information when you learn to listen.",
    response:"The air grows still, waiting for another choice.",
    reward:"a sealed memory"
  },
  {
    id:1017,
    name:"Within the Moss Cathedral · 1017",
    region:"Pale Engine",
    signal:"a thin thread of silver light",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 2, and its trace number is 1017.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 1017.",
    lesson:"Returning is not the same as repeating.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a clearer signal"
  },
  {
    id:1018,
    name:"At the edge of the Moss Cathedral · 1018",
    region:"Frostline",
    signal:"a reflection that arrives late",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 3, and its trace number is 1018.",
    clue:"Find the only light that does not pulse. Fragment index: 1018.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The echo returns with one extra note.",
    reward:"a changed landmark"
  },
  {
    id:1019,
    name:"Where the Moss Cathedral · 1019",
    region:"Last Horizon",
    signal:"a shadow moving against the light",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 4, and its trace number is 1019.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 1019.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The ground glows for a moment, then settles.",
    reward:"a hidden passage"
  },
  {
    id:1020,
    name:"Before the Moss Cathedral · 1020",
    region:"Glasswater Basin",
    signal:"a distant bell with no echo",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 5, and its trace number is 1020.",
    clue:"The safest route is not always the shortest. Fragment index: 1020.",
    lesson:"Silence is information when you learn to listen.",
    response:"A new mark appears beside your last footprint.",
    reward:"a second chance"
  },
  {
    id:1021,
    name:"After the Moss Cathedral · 1021",
    region:"Blue Divide",
    signal:"a hum that follows silence",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 6, and its trace number is 1021.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1021.",
    lesson:"Returning is not the same as repeating.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a path that remembers"
  },
  {
    id:1022,
    name:"Between the Moss Cathedral · 1022",
    region:"Ember Archive",
    signal:"a warm line beneath the stone",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 7, and its trace number is 1022.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 1022.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"an echo token"
  },
  {
    id:1023,
    name:"Above the Moss Cathedral · 1023",
    region:"Echo Marsh",
    signal:"a distant bell with no echo",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 1, and its trace number is 1023.",
    clue:"A repeated step can open a door, but only once. Fragment index: 1023.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a stored reflection"
  },
  {
    id:1024,
    name:"Below the Moss Cathedral · 1024",
    region:"Last Horizon",
    signal:"a hum that follows silence",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 2, and its trace number is 1024.",
    clue:"The second path is real only after you turn away. Fragment index: 1024.",
    lesson:"Silence is information when you learn to listen.",
    response:"The horizon brightens where your route bends.",
    reward:"a new depth"
  },
  {
    id:1025,
    name:"The Fading Map · 1025",
    region:"Glasswater Basin",
    signal:"a warm line beneath the stone",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 3, and its trace number is 1025.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 1025.",
    lesson:"Returning is not the same as repeating.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a quiet clue"
  },
  {
    id:1026,
    name:"A Fading Map · 1026",
    region:"Blue Divide",
    signal:"a pale mark that shifts position",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 4, and its trace number is 1026.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 1026.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A distant light answers with one measured flash.",
    reward:"a memory fragment"
  },
  {
    id:1027,
    name:"Beneath the Fading Map · 1027",
    region:"Ember Archive",
    signal:"a small star below the horizon",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 5, and its trace number is 1027.",
    clue:"Return to the place where the floor changes colour. Fragment index: 1027.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The path behind you quietly changes its shape.",
    reward:"a map trace"
  },
  {
    id:1028,
    name:"Beyond the Fading Map · 1028",
    region:"Echo Marsh",
    signal:"three notes with no source",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 6, and its trace number is 1028.",
    clue:"The answer is stored in the order of your choices. Fragment index: 1028.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The air grows still, waiting for another choice.",
    reward:"a sealed memory"
  },
  {
    id:1029,
    name:"Inside the Fading Map · 1029",
    region:"Mirror Waste",
    signal:"a slow rhythm under the wind",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 7, and its trace number is 1029.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1029.",
    lesson:"Observation can be a form of movement.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a clearer signal"
  },
  {
    id:1030,
    name:"Under the Fading Map · 1030",
    region:"Quiet Reach",
    signal:"a small star below the horizon",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 1, and its trace number is 1030.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 1030.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The echo returns with one extra note.",
    reward:"a changed landmark"
  },
  {
    id:1031,
    name:"Across the Fading Map · 1031",
    region:"Moss Quarter",
    signal:"three notes with no source",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 2, and its trace number is 1031.",
    clue:"Find the only light that does not pulse. Fragment index: 1031.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The ground glows for a moment, then settles.",
    reward:"a hidden passage"
  },
  {
    id:1032,
    name:"Behind the Fading Map · 1032",
    region:"Hollow Canopy",
    signal:"a slow rhythm under the wind",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 3, and its trace number is 1032.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 1032.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A new mark appears beside your last footprint.",
    reward:"a second chance"
  },
  {
    id:1033,
    name:"Within the Fading Map · 1033",
    region:"Lantern Expanse",
    signal:"a breath behind the wall",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 4, and its trace number is 1033.",
    clue:"The safest route is not always the shortest. Fragment index: 1033.",
    lesson:"Observation can be a form of movement.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a path that remembers"
  },
  {
    id:1034,
    name:"At the edge of the Fading Map · 1034",
    region:"Pale Engine",
    signal:"a low blue pulse",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 5, and its trace number is 1034.",
    clue:"Your previous route is the map for this one. Fragment index: 1034.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"an echo token"
  },
  {
    id:1035,
    name:"Where the Fading Map · 1035",
    region:"Quiet Reach",
    signal:"a ripple crossing dry ground",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 6, and its trace number is 1035.",
    clue:"Move once, pause once, then listen again. Fragment index: 1035.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a stored reflection"
  },
  {
    id:1036,
    name:"Before the Fading Map · 1036",
    region:"Moss Quarter",
    signal:"a pattern of footprints facing inward",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 7, and its trace number is 1036.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 1036.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a new depth"
  },
  {
    id:1037,
    name:"After the Fading Map · 1037",
    region:"Hollow Canopy",
    signal:"a low blue pulse",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 1, and its trace number is 1037.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1037.",
    lesson:"Observation can be a form of movement.",
    response:"A distant light answers with one measured flash.",
    reward:"a quiet clue"
  },
  {
    id:1038,
    name:"Between the Fading Map · 1038",
    region:"Lantern Expanse",
    signal:"a ripple crossing dry ground",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 2, and its trace number is 1038.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 1038.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The path behind you quietly changes its shape.",
    reward:"a memory fragment"
  },
  {
    id:1039,
    name:"Above the Fading Map · 1039",
    region:"Pale Engine",
    signal:"a pattern of footprints facing inward",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 3, and its trace number is 1039.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 1039.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The air grows still, waiting for another choice.",
    reward:"a map trace"
  },
  {
    id:1040,
    name:"Below the Fading Map · 1040",
    region:"Frostline",
    signal:"a glow hidden inside a crack",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 4, and its trace number is 1040.",
    clue:"Return to the place where the floor changes colour. Fragment index: 1040.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a sealed memory"
  },
  {
    id:1041,
    name:"The Copper Forest · 1041",
    region:"Last Horizon",
    signal:"a door-shaped gap in the air",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 5, and its trace number is 1041.",
    clue:"The answer is stored in the order of your choices. Fragment index: 1041.",
    lesson:"Observation can be a form of movement.",
    response:"The echo returns with one extra note.",
    reward:"a clearer signal"
  },
  {
    id:1042,
    name:"A Copper Forest · 1042",
    region:"Glasswater Basin",
    signal:"a thin thread of silver light",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 6, and its trace number is 1042.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1042.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The ground glows for a moment, then settles.",
    reward:"a changed landmark"
  },
  {
    id:1043,
    name:"Beneath the Copper Forest · 1043",
    region:"Blue Divide",
    signal:"a reflection that arrives late",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 7, and its trace number is 1043.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 1043.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A new mark appears beside your last footprint.",
    reward:"a hidden passage"
  },
  {
    id:1044,
    name:"Beyond the Copper Forest · 1044",
    region:"Ember Archive",
    signal:"a door-shaped gap in the air",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 1, and its trace number is 1044.",
    clue:"Find the only light that does not pulse. Fragment index: 1044.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a second chance"
  },
  {
    id:1045,
    name:"Inside the Copper Forest · 1045",
    region:"Echo Marsh",
    signal:"a thin thread of silver light",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 2, and its trace number is 1045.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 1045.",
    lesson:"Observation can be a form of movement.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a memory fragment"
  },
  {
    id:1046,
    name:"Under the Copper Forest · 1046",
    region:"Last Horizon",
    signal:"a reflection that arrives late",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 3, and its trace number is 1046.",
    clue:"The safest route is not always the shortest. Fragment index: 1046.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a map trace"
  },
  {
    id:1047,
    name:"Across the Copper Forest · 1047",
    region:"Glasswater Basin",
    signal:"a shadow moving against the light",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 4, and its trace number is 1047.",
    clue:"Your previous route is the map for this one. Fragment index: 1047.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The horizon brightens where your route bends.",
    reward:"a sealed memory"
  },
  {
    id:1048,
    name:"Behind the Copper Forest · 1048",
    region:"Blue Divide",
    signal:"a distant bell with no echo",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 5, and its trace number is 1048.",
    clue:"Move once, pause once, then listen again. Fragment index: 1048.",
    lesson:"Memory is more than a record of where you went.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a clearer signal"
  },
  {
    id:1049,
    name:"Within the Copper Forest · 1049",
    region:"Ember Archive",
    signal:"a hum that follows silence",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 6, and its trace number is 1049.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 1049.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A distant light answers with one measured flash.",
    reward:"a changed landmark"
  },
  {
    id:1050,
    name:"At the edge of the Copper Forest · 1050",
    region:"Echo Marsh",
    signal:"a warm line beneath the stone",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 7, and its trace number is 1050.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1050.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The path behind you quietly changes its shape.",
    reward:"a hidden passage"
  },
  {
    id:1051,
    name:"Where the Copper Forest · 1051",
    region:"Mirror Waste",
    signal:"a distant bell with no echo",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 1, and its trace number is 1051.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 1051.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The air grows still, waiting for another choice.",
    reward:"a second chance"
  },
  {
    id:1052,
    name:"Before the Copper Forest · 1052",
    region:"Quiet Reach",
    signal:"a hum that follows silence",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 2, and its trace number is 1052.",
    clue:"A repeated step can open a door, but only once. Fragment index: 1052.",
    lesson:"Memory is more than a record of where you went.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a path that remembers"
  },
  {
    id:1053,
    name:"After the Copper Forest · 1053",
    region:"Moss Quarter",
    signal:"a warm line beneath the stone",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 3, and its trace number is 1053.",
    clue:"The second path is real only after you turn away. Fragment index: 1053.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The echo returns with one extra note.",
    reward:"an echo token"
  },
  {
    id:1054,
    name:"Between the Copper Forest · 1054",
    region:"Hollow Canopy",
    signal:"a pale mark that shifts position",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 4, and its trace number is 1054.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 1054.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The ground glows for a moment, then settles.",
    reward:"a stored reflection"
  },
  {
    id:1055,
    name:"Above the Copper Forest · 1055",
    region:"Lantern Expanse",
    signal:"a small star below the horizon",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 5, and its trace number is 1055.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1055.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A new mark appears beside your last footprint.",
    reward:"a new depth"
  },
  {
    id:1056,
    name:"Below the Copper Forest · 1056",
    region:"Pale Engine",
    signal:"three notes with no source",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 6, and its trace number is 1056.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 1056.",
    lesson:"Memory is more than a record of where you went.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a quiet clue"
  },
  {
    id:1057,
    name:"The Shallow Sky · 1057",
    region:"Quiet Reach",
    signal:"a slow rhythm under the wind",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 7, and its trace number is 1057.",
    clue:"Find the only light that does not pulse. Fragment index: 1057.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a memory fragment"
  },
  {
    id:1058,
    name:"A Shallow Sky · 1058",
    region:"Moss Quarter",
    signal:"a small star below the horizon",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 1, and its trace number is 1058.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 1058.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a map trace"
  },
  {
    id:1059,
    name:"Beneath the Shallow Sky · 1059",
    region:"Hollow Canopy",
    signal:"three notes with no source",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 2, and its trace number is 1059.",
    clue:"The safest route is not always the shortest. Fragment index: 1059.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a sealed memory"
  },
  {
    id:1060,
    name:"Beyond the Shallow Sky · 1060",
    region:"Lantern Expanse",
    signal:"a slow rhythm under the wind",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 3, and its trace number is 1060.",
    clue:"Your previous route is the map for this one. Fragment index: 1060.",
    lesson:"Memory is more than a record of where you went.",
    response:"A distant light answers with one measured flash.",
    reward:"a clearer signal"
  },
  {
    id:1061,
    name:"Inside the Shallow Sky · 1061",
    region:"Pale Engine",
    signal:"a breath behind the wall",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 4, and its trace number is 1061.",
    clue:"Move once, pause once, then listen again. Fragment index: 1061.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The path behind you quietly changes its shape.",
    reward:"a changed landmark"
  },
  {
    id:1062,
    name:"Under the Shallow Sky · 1062",
    region:"Frostline",
    signal:"a low blue pulse",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 5, and its trace number is 1062.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 1062.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The air grows still, waiting for another choice.",
    reward:"a hidden passage"
  },
  {
    id:1063,
    name:"Across the Shallow Sky · 1063",
    region:"Last Horizon",
    signal:"a ripple crossing dry ground",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 6, and its trace number is 1063.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1063.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a second chance"
  },
  {
    id:1064,
    name:"Behind the Shallow Sky · 1064",
    region:"Glasswater Basin",
    signal:"a pattern of footprints facing inward",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 7, and its trace number is 1064.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 1064.",
    lesson:"Memory is more than a record of where you went.",
    response:"The echo returns with one extra note.",
    reward:"a path that remembers"
  },
  {
    id:1065,
    name:"Within the Shallow Sky · 1065",
    region:"Blue Divide",
    signal:"a low blue pulse",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 1, and its trace number is 1065.",
    clue:"A repeated step can open a door, but only once. Fragment index: 1065.",
    lesson:"Silence is information when you learn to listen.",
    response:"The ground glows for a moment, then settles.",
    reward:"an echo token"
  },
  {
    id:1066,
    name:"At the edge of the Shallow Sky · 1066",
    region:"Ember Archive",
    signal:"a ripple crossing dry ground",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 2, and its trace number is 1066.",
    clue:"The second path is real only after you turn away. Fragment index: 1066.",
    lesson:"Returning is not the same as repeating.",
    response:"A new mark appears beside your last footprint.",
    reward:"a stored reflection"
  },
  {
    id:1067,
    name:"Where the Shallow Sky · 1067",
    region:"Echo Marsh",
    signal:"a pattern of footprints facing inward",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 3, and its trace number is 1067.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 1067.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a new depth"
  },
  {
    id:1068,
    name:"Before the Shallow Sky · 1068",
    region:"Last Horizon",
    signal:"a glow hidden inside a crack",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 4, and its trace number is 1068.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 1068.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a quiet clue"
  },
  {
    id:1069,
    name:"After the Shallow Sky · 1069",
    region:"Glasswater Basin",
    signal:"a door-shaped gap in the air",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 5, and its trace number is 1069.",
    clue:"Return to the place where the floor changes colour. Fragment index: 1069.",
    lesson:"Silence is information when you learn to listen.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a memory fragment"
  },
  {
    id:1070,
    name:"Between the Shallow Sky · 1070",
    region:"Blue Divide",
    signal:"a thin thread of silver light",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 6, and its trace number is 1070.",
    clue:"The answer is stored in the order of your choices. Fragment index: 1070.",
    lesson:"Returning is not the same as repeating.",
    response:"The horizon brightens where your route bends.",
    reward:"a map trace"
  },
  {
    id:1071,
    name:"Above the Shallow Sky · 1071",
    region:"Ember Archive",
    signal:"a reflection that arrives late",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 7, and its trace number is 1071.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1071.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a sealed memory"
  },
  {
    id:1072,
    name:"Below the Shallow Sky · 1072",
    region:"Echo Marsh",
    signal:"a door-shaped gap in the air",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 1, and its trace number is 1072.",
    clue:"The safest route is not always the shortest. Fragment index: 1072.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A distant light answers with one measured flash.",
    reward:"a clearer signal"
  },
  {
    id:1073,
    name:"The Lost Observatory · 1073",
    region:"Mirror Waste",
    signal:"a thin thread of silver light",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 2, and its trace number is 1073.",
    clue:"Your previous route is the map for this one. Fragment index: 1073.",
    lesson:"Silence is information when you learn to listen.",
    response:"The path behind you quietly changes its shape.",
    reward:"a changed landmark"
  },
  {
    id:1074,
    name:"A Lost Observatory · 1074",
    region:"Quiet Reach",
    signal:"a reflection that arrives late",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 3, and its trace number is 1074.",
    clue:"Move once, pause once, then listen again. Fragment index: 1074.",
    lesson:"Returning is not the same as repeating.",
    response:"The air grows still, waiting for another choice.",
    reward:"a new depth"
  },
  {
    id:1075,
    name:"Beneath the Lost Observatory · 1075",
    region:"Moss Quarter",
    signal:"a shadow moving against the light",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 4, and its trace number is 1075.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 1075.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a quiet clue"
  },
  {
    id:1076,
    name:"Beyond the Lost Observatory · 1076",
    region:"Hollow Canopy",
    signal:"a distant bell with no echo",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 5, and its trace number is 1076.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1076.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The echo returns with one extra note.",
    reward:"a memory fragment"
  },
  {
    id:1077,
    name:"Inside the Lost Observatory · 1077",
    region:"Lantern Expanse",
    signal:"a hum that follows silence",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 6, and its trace number is 1077.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 1077.",
    lesson:"Silence is information when you learn to listen.",
    response:"The ground glows for a moment, then settles.",
    reward:"a map trace"
  },
  {
    id:1078,
    name:"Under the Lost Observatory · 1078",
    region:"Pale Engine",
    signal:"a warm line beneath the stone",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 7, and its trace number is 1078.",
    clue:"A repeated step can open a door, but only once. Fragment index: 1078.",
    lesson:"Returning is not the same as repeating.",
    response:"A new mark appears beside your last footprint.",
    reward:"a sealed memory"
  },
  {
    id:1079,
    name:"Across the Lost Observatory · 1079",
    region:"Quiet Reach",
    signal:"a distant bell with no echo",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 1, and its trace number is 1079.",
    clue:"The second path is real only after you turn away. Fragment index: 1079.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a clearer signal"
  },
  {
    id:1080,
    name:"Behind the Lost Observatory · 1080",
    region:"Moss Quarter",
    signal:"a hum that follows silence",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 2, and its trace number is 1080.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 1080.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a changed landmark"
  },
  {
    id:1081,
    name:"Within the Lost Observatory · 1081",
    region:"Hollow Canopy",
    signal:"a warm line beneath the stone",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 3, and its trace number is 1081.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 1081.",
    lesson:"Silence is information when you learn to listen.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a hidden passage"
  },
  {
    id:1082,
    name:"At the edge of the Lost Observatory · 1082",
    region:"Lantern Expanse",
    signal:"a pale mark that shifts position",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 4, and its trace number is 1082.",
    clue:"Return to the place where the floor changes colour. Fragment index: 1082.",
    lesson:"Returning is not the same as repeating.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a second chance"
  },
  {
    id:1083,
    name:"Where the Lost Observatory · 1083",
    region:"Pale Engine",
    signal:"a small star below the horizon",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 5, and its trace number is 1083.",
    clue:"The answer is stored in the order of your choices. Fragment index: 1083.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A distant light answers with one measured flash.",
    reward:"a path that remembers"
  },
  {
    id:1084,
    name:"Before the Lost Observatory · 1084",
    region:"Frostline",
    signal:"three notes with no source",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 6, and its trace number is 1084.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1084.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The path behind you quietly changes its shape.",
    reward:"an echo token"
  },
  {
    id:1085,
    name:"After the Lost Observatory · 1085",
    region:"Last Horizon",
    signal:"a slow rhythm under the wind",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 7, and its trace number is 1085.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 1085.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The air grows still, waiting for another choice.",
    reward:"a stored reflection"
  },
  {
    id:1086,
    name:"Between the Lost Observatory · 1086",
    region:"Glasswater Basin",
    signal:"a small star below the horizon",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 1, and its trace number is 1086.",
    clue:"Find the only light that does not pulse. Fragment index: 1086.",
    lesson:"Observation can be a form of movement.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a new depth"
  },
  {
    id:1087,
    name:"Above the Lost Observatory · 1087",
    region:"Blue Divide",
    signal:"three notes with no source",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 2, and its trace number is 1087.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 1087.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The echo returns with one extra note.",
    reward:"a quiet clue"
  },
  {
    id:1088,
    name:"Below the Lost Observatory · 1088",
    region:"Ember Archive",
    signal:"a slow rhythm under the wind",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 3, and its trace number is 1088.",
    clue:"The safest route is not always the shortest. Fragment index: 1088.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The ground glows for a moment, then settles.",
    reward:"a memory fragment"
  },
  {
    id:1089,
    name:"The Moonlit Well · 1089",
    region:"Echo Marsh",
    signal:"a breath behind the wall",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 4, and its trace number is 1089.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1089.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A new mark appears beside your last footprint.",
    reward:"a map trace"
  },
  {
    id:1090,
    name:"A Moonlit Well · 1090",
    region:"Last Horizon",
    signal:"a low blue pulse",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 5, and its trace number is 1090.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 1090.",
    lesson:"Observation can be a form of movement.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a sealed memory"
  },
  {
    id:1091,
    name:"Beneath the Moonlit Well · 1091",
    region:"Glasswater Basin",
    signal:"a ripple crossing dry ground",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 6, and its trace number is 1091.",
    clue:"A repeated step can open a door, but only once. Fragment index: 1091.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a clearer signal"
  },
  {
    id:1092,
    name:"Beyond the Moonlit Well · 1092",
    region:"Blue Divide",
    signal:"a pattern of footprints facing inward",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 7, and its trace number is 1092.",
    clue:"The second path is real only after you turn away. Fragment index: 1092.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a changed landmark"
  },
  {
    id:1093,
    name:"Inside the Moonlit Well · 1093",
    region:"Ember Archive",
    signal:"a low blue pulse",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 1, and its trace number is 1093.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 1093.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The horizon brightens where your route bends.",
    reward:"a hidden passage"
  },
  {
    id:1094,
    name:"Under the Moonlit Well · 1094",
    region:"Echo Marsh",
    signal:"a ripple crossing dry ground",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 2, and its trace number is 1094.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 1094.",
    lesson:"Observation can be a form of movement.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a second chance"
  },
  {
    id:1095,
    name:"Across the Moonlit Well · 1095",
    region:"Mirror Waste",
    signal:"a pattern of footprints facing inward",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 3, and its trace number is 1095.",
    clue:"Return to the place where the floor changes colour. Fragment index: 1095.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A distant light answers with one measured flash.",
    reward:"a path that remembers"
  },
  {
    id:1096,
    name:"Behind the Moonlit Well · 1096",
    region:"Quiet Reach",
    signal:"a glow hidden inside a crack",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 4, and its trace number is 1096.",
    clue:"The answer is stored in the order of your choices. Fragment index: 1096.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The path behind you quietly changes its shape.",
    reward:"an echo token"
  },
  {
    id:1097,
    name:"Within the Moonlit Well · 1097",
    region:"Moss Quarter",
    signal:"a door-shaped gap in the air",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 5, and its trace number is 1097.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1097.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The air grows still, waiting for another choice.",
    reward:"a stored reflection"
  },
  {
    id:1098,
    name:"At the edge of the Moonlit Well · 1098",
    region:"Hollow Canopy",
    signal:"a thin thread of silver light",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 6, and its trace number is 1098.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 1098.",
    lesson:"Observation can be a form of movement.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a new depth"
  },
  {
    id:1099,
    name:"Where the Moonlit Well · 1099",
    region:"Lantern Expanse",
    signal:"a reflection that arrives late",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 7, and its trace number is 1099.",
    clue:"Find the only light that does not pulse. Fragment index: 1099.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The echo returns with one extra note.",
    reward:"a quiet clue"
  },
  {
    id:1100,
    name:"Before the Moonlit Well · 1100",
    region:"Pale Engine",
    signal:"a door-shaped gap in the air",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 1, and its trace number is 1100.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 1100.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The ground glows for a moment, then settles.",
    reward:"a memory fragment"
  },
  {
    id:1101,
    name:"After the Moonlit Well · 1101",
    region:"Quiet Reach",
    signal:"a thin thread of silver light",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 2, and its trace number is 1101.",
    clue:"The safest route is not always the shortest. Fragment index: 1101.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A new mark appears beside your last footprint.",
    reward:"a map trace"
  },
  {
    id:1102,
    name:"Between the Moonlit Well · 1102",
    region:"Moss Quarter",
    signal:"a reflection that arrives late",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 3, and its trace number is 1102.",
    clue:"Your previous route is the map for this one. Fragment index: 1102.",
    lesson:"Observation can be a form of movement.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a sealed memory"
  },
  {
    id:1103,
    name:"Above the Moonlit Well · 1103",
    region:"Hollow Canopy",
    signal:"a shadow moving against the light",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 4, and its trace number is 1103.",
    clue:"Move once, pause once, then listen again. Fragment index: 1103.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"an echo token"
  },
  {
    id:1104,
    name:"Below the Moonlit Well · 1104",
    region:"Lantern Expanse",
    signal:"a distant bell with no echo",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 5, and its trace number is 1104.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 1104.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a stored reflection"
  },
  {
    id:1105,
    name:"The Crimson Passage · 1105",
    region:"Pale Engine",
    signal:"a hum that follows silence",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 6, and its trace number is 1105.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1105.",
    lesson:"Memory is more than a record of where you went.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a new depth"
  },
  {
    id:1106,
    name:"A Crimson Passage · 1106",
    region:"Frostline",
    signal:"a warm line beneath the stone",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 7, and its trace number is 1106.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 1106.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A distant light answers with one measured flash.",
    reward:"a quiet clue"
  },
  {
    id:1107,
    name:"Beneath the Crimson Passage · 1107",
    region:"Last Horizon",
    signal:"a distant bell with no echo",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 1, and its trace number is 1107.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 1107.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The path behind you quietly changes its shape.",
    reward:"a memory fragment"
  },
  {
    id:1108,
    name:"Beyond the Crimson Passage · 1108",
    region:"Glasswater Basin",
    signal:"a hum that follows silence",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 2, and its trace number is 1108.",
    clue:"Return to the place where the floor changes colour. Fragment index: 1108.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The air grows still, waiting for another choice.",
    reward:"a map trace"
  },
  {
    id:1109,
    name:"Inside the Crimson Passage · 1109",
    region:"Blue Divide",
    signal:"a warm line beneath the stone",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 3, and its trace number is 1109.",
    clue:"The answer is stored in the order of your choices. Fragment index: 1109.",
    lesson:"Memory is more than a record of where you went.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a sealed memory"
  },
  {
    id:1110,
    name:"Under the Crimson Passage · 1110",
    region:"Ember Archive",
    signal:"a pale mark that shifts position",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 4, and its trace number is 1110.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1110.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The echo returns with one extra note.",
    reward:"a clearer signal"
  },
  {
    id:1111,
    name:"Across the Crimson Passage · 1111",
    region:"Echo Marsh",
    signal:"a small star below the horizon",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 5, and its trace number is 1111.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 1111.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The ground glows for a moment, then settles.",
    reward:"a changed landmark"
  },
  {
    id:1112,
    name:"Behind the Crimson Passage · 1112",
    region:"Last Horizon",
    signal:"three notes with no source",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 6, and its trace number is 1112.",
    clue:"Find the only light that does not pulse. Fragment index: 1112.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A new mark appears beside your last footprint.",
    reward:"a hidden passage"
  },
  {
    id:1113,
    name:"Within the Crimson Passage · 1113",
    region:"Glasswater Basin",
    signal:"a slow rhythm under the wind",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 7, and its trace number is 1113.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 1113.",
    lesson:"Memory is more than a record of where you went.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a second chance"
  },
  {
    id:1114,
    name:"At the edge of the Crimson Passage · 1114",
    region:"Blue Divide",
    signal:"a small star below the horizon",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 1, and its trace number is 1114.",
    clue:"The safest route is not always the shortest. Fragment index: 1114.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a path that remembers"
  },
  {
    id:1115,
    name:"Where the Crimson Passage · 1115",
    region:"Ember Archive",
    signal:"three notes with no source",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 2, and its trace number is 1115.",
    clue:"Your previous route is the map for this one. Fragment index: 1115.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"an echo token"
  },
  {
    id:1116,
    name:"Before the Crimson Passage · 1116",
    region:"Echo Marsh",
    signal:"a slow rhythm under the wind",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 3, and its trace number is 1116.",
    clue:"Move once, pause once, then listen again. Fragment index: 1116.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The horizon brightens where your route bends.",
    reward:"a stored reflection"
  },
  {
    id:1117,
    name:"After the Crimson Passage · 1117",
    region:"Mirror Waste",
    signal:"a breath behind the wall",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 4, and its trace number is 1117.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 1117.",
    lesson:"Memory is more than a record of where you went.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a new depth"
  },
  {
    id:1118,
    name:"Between the Crimson Passage · 1118",
    region:"Quiet Reach",
    signal:"a low blue pulse",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 5, and its trace number is 1118.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1118.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A distant light answers with one measured flash.",
    reward:"a quiet clue"
  },
  {
    id:1119,
    name:"Above the Crimson Passage · 1119",
    region:"Moss Quarter",
    signal:"a ripple crossing dry ground",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 6, and its trace number is 1119.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 1119.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The path behind you quietly changes its shape.",
    reward:"a memory fragment"
  },
  {
    id:1120,
    name:"Below the Crimson Passage · 1120",
    region:"Hollow Canopy",
    signal:"a pattern of footprints facing inward",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 7, and its trace number is 1120.",
    clue:"A repeated step can open a door, but only once. Fragment index: 1120.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The air grows still, waiting for another choice.",
    reward:"a map trace"
  },
  {
    id:1121,
    name:"The Winter Library · 1121",
    region:"Lantern Expanse",
    signal:"a low blue pulse",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 1, and its trace number is 1121.",
    clue:"The second path is real only after you turn away. Fragment index: 1121.",
    lesson:"Memory is more than a record of where you went.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a sealed memory"
  },
  {
    id:1122,
    name:"A Winter Library · 1122",
    region:"Pale Engine",
    signal:"a ripple crossing dry ground",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 2, and its trace number is 1122.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 1122.",
    lesson:"Silence is information when you learn to listen.",
    response:"The echo returns with one extra note.",
    reward:"a clearer signal"
  },
  {
    id:1123,
    name:"Beneath the Winter Library · 1123",
    region:"Quiet Reach",
    signal:"a pattern of footprints facing inward",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 3, and its trace number is 1123.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1123.",
    lesson:"Returning is not the same as repeating.",
    response:"The ground glows for a moment, then settles.",
    reward:"a changed landmark"
  },
  {
    id:1124,
    name:"Beyond the Winter Library · 1124",
    region:"Moss Quarter",
    signal:"a glow hidden inside a crack",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 4, and its trace number is 1124.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 1124.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A new mark appears beside your last footprint.",
    reward:"a hidden passage"
  },
  {
    id:1125,
    name:"Inside the Winter Library · 1125",
    region:"Hollow Canopy",
    signal:"a door-shaped gap in the air",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 5, and its trace number is 1125.",
    clue:"Find the only light that does not pulse. Fragment index: 1125.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a second chance"
  },
  {
    id:1126,
    name:"Under the Winter Library · 1126",
    region:"Lantern Expanse",
    signal:"a thin thread of silver light",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 6, and its trace number is 1126.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 1126.",
    lesson:"Silence is information when you learn to listen.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a path that remembers"
  },
  {
    id:1127,
    name:"Across the Winter Library · 1127",
    region:"Pale Engine",
    signal:"a reflection that arrives late",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 7, and its trace number is 1127.",
    clue:"The safest route is not always the shortest. Fragment index: 1127.",
    lesson:"Returning is not the same as repeating.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"an echo token"
  },
  {
    id:1128,
    name:"Behind the Winter Library · 1128",
    region:"Frostline",
    signal:"a door-shaped gap in the air",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 1, and its trace number is 1128.",
    clue:"Your previous route is the map for this one. Fragment index: 1128.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a stored reflection"
  },
  {
    id:1129,
    name:"Within the Winter Library · 1129",
    region:"Last Horizon",
    signal:"a thin thread of silver light",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 2, and its trace number is 1129.",
    clue:"Move once, pause once, then listen again. Fragment index: 1129.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A distant light answers with one measured flash.",
    reward:"a new depth"
  },
  {
    id:1130,
    name:"At the edge of the Winter Library · 1130",
    region:"Glasswater Basin",
    signal:"a reflection that arrives late",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 3, and its trace number is 1130.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 1130.",
    lesson:"Silence is information when you learn to listen.",
    response:"The path behind you quietly changes its shape.",
    reward:"a quiet clue"
  },
  {
    id:1131,
    name:"Where the Winter Library · 1131",
    region:"Blue Divide",
    signal:"a shadow moving against the light",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 4, and its trace number is 1131.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1131.",
    lesson:"Returning is not the same as repeating.",
    response:"The air grows still, waiting for another choice.",
    reward:"a memory fragment"
  },
  {
    id:1132,
    name:"Before the Winter Library · 1132",
    region:"Ember Archive",
    signal:"a distant bell with no echo",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 5, and its trace number is 1132.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 1132.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a second chance"
  },
  {
    id:1133,
    name:"After the Winter Library · 1133",
    region:"Echo Marsh",
    signal:"a hum that follows silence",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 6, and its trace number is 1133.",
    clue:"A repeated step can open a door, but only once. Fragment index: 1133.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The echo returns with one extra note.",
    reward:"a path that remembers"
  },
  {
    id:1134,
    name:"Between the Winter Library · 1134",
    region:"Last Horizon",
    signal:"a warm line beneath the stone",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 7, and its trace number is 1134.",
    clue:"The second path is real only after you turn away. Fragment index: 1134.",
    lesson:"Silence is information when you learn to listen.",
    response:"The ground glows for a moment, then settles.",
    reward:"an echo token"
  },
  {
    id:1135,
    name:"Above the Winter Library · 1135",
    region:"Glasswater Basin",
    signal:"a distant bell with no echo",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 1, and its trace number is 1135.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 1135.",
    lesson:"Returning is not the same as repeating.",
    response:"A new mark appears beside your last footprint.",
    reward:"a stored reflection"
  },
  {
    id:1136,
    name:"Below the Winter Library · 1136",
    region:"Blue Divide",
    signal:"a hum that follows silence",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 2, and its trace number is 1136.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 1136.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a new depth"
  },
  {
    id:1137,
    name:"The Obsidian Pool · 1137",
    region:"Ember Archive",
    signal:"a warm line beneath the stone",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 3, and its trace number is 1137.",
    clue:"Return to the place where the floor changes colour. Fragment index: 1137.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a quiet clue"
  },
  {
    id:1138,
    name:"A Obsidian Pool · 1138",
    region:"Echo Marsh",
    signal:"a pale mark that shifts position",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 4, and its trace number is 1138.",
    clue:"The answer is stored in the order of your choices. Fragment index: 1138.",
    lesson:"Silence is information when you learn to listen.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a memory fragment"
  },
  {
    id:1139,
    name:"Beneath the Obsidian Pool · 1139",
    region:"Mirror Waste",
    signal:"a small star below the horizon",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 5, and its trace number is 1139.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1139.",
    lesson:"Returning is not the same as repeating.",
    response:"The horizon brightens where your route bends.",
    reward:"a map trace"
  },
  {
    id:1140,
    name:"Beyond the Obsidian Pool · 1140",
    region:"Quiet Reach",
    signal:"three notes with no source",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 6, and its trace number is 1140.",
    clue:"The safest route is not always the shortest. Fragment index: 1140.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a sealed memory"
  },
  {
    id:1141,
    name:"Inside the Obsidian Pool · 1141",
    region:"Moss Quarter",
    signal:"a slow rhythm under the wind",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 7, and its trace number is 1141.",
    clue:"Your previous route is the map for this one. Fragment index: 1141.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A distant light answers with one measured flash.",
    reward:"a clearer signal"
  },
  {
    id:1142,
    name:"Under the Obsidian Pool · 1142",
    region:"Hollow Canopy",
    signal:"a small star below the horizon",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 1, and its trace number is 1142.",
    clue:"Move once, pause once, then listen again. Fragment index: 1142.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The path behind you quietly changes its shape.",
    reward:"a changed landmark"
  },
  {
    id:1143,
    name:"Across the Obsidian Pool · 1143",
    region:"Lantern Expanse",
    signal:"three notes with no source",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 2, and its trace number is 1143.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 1143.",
    lesson:"Observation can be a form of movement.",
    response:"The air grows still, waiting for another choice.",
    reward:"a hidden passage"
  },
  {
    id:1144,
    name:"Behind the Obsidian Pool · 1144",
    region:"Pale Engine",
    signal:"a slow rhythm under the wind",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 3, and its trace number is 1144.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1144.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a second chance"
  },
  {
    id:1145,
    name:"Within the Obsidian Pool · 1145",
    region:"Quiet Reach",
    signal:"a breath behind the wall",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 4, and its trace number is 1145.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 1145.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The echo returns with one extra note.",
    reward:"a path that remembers"
  },
  {
    id:1146,
    name:"At the edge of the Obsidian Pool · 1146",
    region:"Moss Quarter",
    signal:"a low blue pulse",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 5, and its trace number is 1146.",
    clue:"A repeated step can open a door, but only once. Fragment index: 1146.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The ground glows for a moment, then settles.",
    reward:"an echo token"
  },
  {
    id:1147,
    name:"Where the Obsidian Pool · 1147",
    region:"Hollow Canopy",
    signal:"a ripple crossing dry ground",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 6, and its trace number is 1147.",
    clue:"The second path is real only after you turn away. Fragment index: 1147.",
    lesson:"Observation can be a form of movement.",
    response:"A new mark appears beside your last footprint.",
    reward:"a stored reflection"
  },
  {
    id:1148,
    name:"Before the Obsidian Pool · 1148",
    region:"Lantern Expanse",
    signal:"a pattern of footprints facing inward",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 7, and its trace number is 1148.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 1148.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a new depth"
  },
  {
    id:1149,
    name:"After the Obsidian Pool · 1149",
    region:"Pale Engine",
    signal:"a low blue pulse",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 1, and its trace number is 1149.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 1149.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a quiet clue"
  },
  {
    id:1150,
    name:"Between the Obsidian Pool · 1150",
    region:"Frostline",
    signal:"a ripple crossing dry ground",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 2, and its trace number is 1150.",
    clue:"Return to the place where the floor changes colour. Fragment index: 1150.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a memory fragment"
  },
  {
    id:1151,
    name:"Above the Obsidian Pool · 1151",
    region:"Last Horizon",
    signal:"a pattern of footprints facing inward",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 3, and its trace number is 1151.",
    clue:"The answer is stored in the order of your choices. Fragment index: 1151.",
    lesson:"Observation can be a form of movement.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a map trace"
  },
  {
    id:1152,
    name:"Below the Obsidian Pool · 1152",
    region:"Glasswater Basin",
    signal:"a glow hidden inside a crack",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 4, and its trace number is 1152.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1152.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"A distant light answers with one measured flash.",
    reward:"a sealed memory"
  },
  {
    id:1153,
    name:"The Soft Thunder · 1153",
    region:"Blue Divide",
    signal:"a door-shaped gap in the air",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 5, and its trace number is 1153.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 1153.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The path behind you quietly changes its shape.",
    reward:"a clearer signal"
  },
  {
    id:1154,
    name:"A Soft Thunder · 1154",
    region:"Ember Archive",
    signal:"a thin thread of silver light",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 6, and its trace number is 1154.",
    clue:"Find the only light that does not pulse. Fragment index: 1154.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The air grows still, waiting for another choice.",
    reward:"a changed landmark"
  },
  {
    id:1155,
    name:"Beneath the Soft Thunder · 1155",
    region:"Echo Marsh",
    signal:"a reflection that arrives late",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 7, and its trace number is 1155.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 1155.",
    lesson:"Observation can be a form of movement.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a hidden passage"
  },
  {
    id:1156,
    name:"Beyond the Soft Thunder · 1156",
    region:"Last Horizon",
    signal:"a door-shaped gap in the air",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 1, and its trace number is 1156.",
    clue:"The safest route is not always the shortest. Fragment index: 1156.",
    lesson:"Every shortcut leaves a trace behind.",
    response:"The echo returns with one extra note.",
    reward:"a second chance"
  },
  {
    id:1157,
    name:"Inside the Soft Thunder · 1157",
    region:"Glasswater Basin",
    signal:"a thin thread of silver light",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 2, and its trace number is 1157.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1157.",
    lesson:"Curiosity changes what becomes visible.",
    response:"The ground glows for a moment, then settles.",
    reward:"a path that remembers"
  },
  {
    id:1158,
    name:"Under the Soft Thunder · 1158",
    region:"Blue Divide",
    signal:"a reflection that arrives late",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 3, and its trace number is 1158.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 1158.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"A new mark appears beside your last footprint.",
    reward:"an echo token"
  },
  {
    id:1159,
    name:"Across the Soft Thunder · 1159",
    region:"Ember Archive",
    signal:"a shadow moving against the light",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 4, and its trace number is 1159.",
    clue:"A repeated step can open a door, but only once. Fragment index: 1159.",
    lesson:"Observation can be a form of movement.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a stored reflection"
  },
  {
    id:1160,
    name:"Behind the Soft Thunder · 1160",
    region:"Echo Marsh",
    signal:"a distant bell with no echo",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 5, and its trace number is 1160.",
    clue:"The second path is real only after you turn away. Fragment index: 1160.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a new depth"
  },
  {
    id:1161,
    name:"Within the Soft Thunder · 1161",
    region:"Mirror Waste",
    signal:"a hum that follows silence",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 6, and its trace number is 1161.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 1161.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a changed landmark"
  },
  {
    id:1162,
    name:"At the edge of the Soft Thunder · 1162",
    region:"Quiet Reach",
    signal:"a warm line beneath the stone",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 7, and its trace number is 1162.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 1162.",
    lesson:"Memory is more than a record of where you went.",
    response:"The horizon brightens where your route bends.",
    reward:"a hidden passage"
  },
  {
    id:1163,
    name:"Where the Soft Thunder · 1163",
    region:"Moss Quarter",
    signal:"a distant bell with no echo",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 1, and its trace number is 1163.",
    clue:"Return to the place where the floor changes colour. Fragment index: 1163.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a second chance"
  },
  {
    id:1164,
    name:"Before the Soft Thunder · 1164",
    region:"Hollow Canopy",
    signal:"a hum that follows silence",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 2, and its trace number is 1164.",
    clue:"The answer is stored in the order of your choices. Fragment index: 1164.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"A distant light answers with one measured flash.",
    reward:"a path that remembers"
  },
  {
    id:1165,
    name:"After the Soft Thunder · 1165",
    region:"Lantern Expanse",
    signal:"a warm line beneath the stone",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 3, and its trace number is 1165.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1165.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The path behind you quietly changes its shape.",
    reward:"an echo token"
  },
  {
    id:1166,
    name:"Between the Soft Thunder · 1166",
    region:"Pale Engine",
    signal:"a pale mark that shifts position",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 4, and its trace number is 1166.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 1166.",
    lesson:"Memory is more than a record of where you went.",
    response:"The air grows still, waiting for another choice.",
    reward:"a stored reflection"
  },
  {
    id:1167,
    name:"Above the Soft Thunder · 1167",
    region:"Quiet Reach",
    signal:"a small star below the horizon",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 5, and its trace number is 1167.",
    clue:"Find the only light that does not pulse. Fragment index: 1167.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a new depth"
  },
  {
    id:1168,
    name:"Below the Soft Thunder · 1168",
    region:"Moss Quarter",
    signal:"three notes with no source",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 6, and its trace number is 1168.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 1168.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The echo returns with one extra note.",
    reward:"a quiet clue"
  },
  {
    id:1169,
    name:"The Amber Corridor · 1169",
    region:"Hollow Canopy",
    signal:"a slow rhythm under the wind",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 7, and its trace number is 1169.",
    clue:"The safest route is not always the shortest. Fragment index: 1169.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The ground glows for a moment, then settles.",
    reward:"a memory fragment"
  },
  {
    id:1170,
    name:"A Amber Corridor · 1170",
    region:"Lantern Expanse",
    signal:"a small star below the horizon",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 1, and its trace number is 1170.",
    clue:"Your previous route is the map for this one. Fragment index: 1170.",
    lesson:"Memory is more than a record of where you went.",
    response:"A new mark appears beside your last footprint.",
    reward:"a map trace"
  },
  {
    id:1171,
    name:"Beneath the Amber Corridor · 1171",
    region:"Pale Engine",
    signal:"three notes with no source",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 2, and its trace number is 1171.",
    clue:"Move once, pause once, then listen again. Fragment index: 1171.",
    lesson:"The world adapts, but it does not always understand.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a sealed memory"
  },
  {
    id:1172,
    name:"Beyond the Amber Corridor · 1172",
    region:"Frostline",
    signal:"a slow rhythm under the wind",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 3, and its trace number is 1172.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 1172.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a clearer signal"
  },
  {
    id:1173,
    name:"Inside the Amber Corridor · 1173",
    region:"Last Horizon",
    signal:"a breath behind the wall",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 4, and its trace number is 1173.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1173.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a changed landmark"
  },
  {
    id:1174,
    name:"Under the Amber Corridor · 1174",
    region:"Glasswater Basin",
    signal:"a low blue pulse",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 5, and its trace number is 1174.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 1174.",
    lesson:"Memory is more than a record of where you went.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a hidden passage"
  },
  {
    id:1175,
    name:"Across the Amber Corridor · 1175",
    region:"Blue Divide",
    signal:"a ripple crossing dry ground",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 6, and its trace number is 1175.",
    clue:"Follow the signal that grows quieter as you approach. Fragment index: 1175.",
    lesson:"The world adapts, but it does not always understand.",
    response:"A distant light answers with one measured flash.",
    reward:"a second chance"
  },
  {
    id:1176,
    name:"Behind the Amber Corridor · 1176",
    region:"Ember Archive",
    signal:"a pattern of footprints facing inward",
    observation:"A distant observer is trying to predict your next move. Its recorded depth is 7, and its trace number is 1176.",
    clue:"Return to the place where the floor changes colour. Fragment index: 1176.",
    lesson:"A choice is still meaningful when nobody explains it.",
    response:"The path behind you quietly changes its shape.",
    reward:"a path that remembers"
  },
  {
    id:1177,
    name:"Within the Amber Corridor · 1177",
    region:"Echo Marsh",
    signal:"a low blue pulse",
    observation:"The nearest path grows brighter after a careful pause. Its recorded depth is 1, and its trace number is 1177.",
    clue:"The answer is stored in the order of your choices. Fragment index: 1177.",
    lesson:"Patience can reveal a route that speed overlooks.",
    response:"The air grows still, waiting for another choice.",
    reward:"an echo token"
  },
  {
    id:1178,
    name:"At the edge of the Amber Corridor · 1178",
    region:"Last Horizon",
    signal:"a ripple crossing dry ground",
    observation:"Something here is learning the difference between patience and fear. Its recorded depth is 2, and its trace number is 1178.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1178.",
    lesson:"Memory is more than a record of where you went.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a stored reflection"
  },
  {
    id:1179,
    name:"Where the Amber Corridor · 1179",
    region:"Glasswater Basin",
    signal:"a pattern of footprints facing inward",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 3, and its trace number is 1179.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 1179.",
    lesson:"Silence is information when you learn to listen.",
    response:"The echo returns with one extra note.",
    reward:"a new depth"
  },
  {
    id:1180,
    name:"Before the Amber Corridor · 1180",
    region:"Blue Divide",
    signal:"a glow hidden inside a crack",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 4, and its trace number is 1180.",
    clue:"Find the only light that does not pulse. Fragment index: 1180.",
    lesson:"Returning is not the same as repeating.",
    response:"The ground glows for a moment, then settles.",
    reward:"a quiet clue"
  },
  {
    id:1181,
    name:"After the Amber Corridor · 1181",
    region:"Ember Archive",
    signal:"a door-shaped gap in the air",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 5, and its trace number is 1181.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 1181.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A new mark appears beside your last footprint.",
    reward:"a memory fragment"
  },
  {
    id:1182,
    name:"Between the Amber Corridor · 1182",
    region:"Echo Marsh",
    signal:"a thin thread of silver light",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 6, and its trace number is 1182.",
    clue:"The safest route is not always the shortest. Fragment index: 1182.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a map trace"
  },
  {
    id:1183,
    name:"Above the Amber Corridor · 1183",
    region:"Mirror Waste",
    signal:"a reflection that arrives late",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 7, and its trace number is 1183.",
    clue:"Your previous route is the map for this one. Fragment index: 1183.",
    lesson:"Silence is information when you learn to listen.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a sealed memory"
  },
  {
    id:1184,
    name:"Below the Amber Corridor · 1184",
    region:"Quiet Reach",
    signal:"a door-shaped gap in the air",
    observation:"The room seems larger when you explore its edges. Its recorded depth is 1, and its trace number is 1184.",
    clue:"Move once, pause once, then listen again. Fragment index: 1184.",
    lesson:"Returning is not the same as repeating.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"a clearer signal"
  },
  {
    id:1185,
    name:"The Cloud Vault · 1185",
    region:"Moss Quarter",
    signal:"a thin thread of silver light",
    observation:"The world leaves this clue where your attention usually wanders. Its recorded depth is 2, and its trace number is 1185.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 1185.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The horizon brightens where your route bends.",
    reward:"a changed landmark"
  },
  {
    id:1186,
    name:"A Cloud Vault · 1186",
    region:"Hollow Canopy",
    signal:"a reflection that arrives late",
    observation:"The stones rearrange themselves around your favourite direction. Its recorded depth is 3, and its trace number is 1186.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1186.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a hidden passage"
  },
  {
    id:1187,
    name:"Beneath the Cloud Vault · 1187",
    region:"Lantern Expanse",
    signal:"a shadow moving against the light",
    observation:"It keeps a record of the direction you chose last. Its recorded depth is 4, and its trace number is 1187.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 1187.",
    lesson:"Silence is information when you learn to listen.",
    response:"A distant light answers with one measured flash.",
    reward:"a second chance"
  },
  {
    id:1188,
    name:"Beyond the Cloud Vault · 1188",
    region:"Pale Engine",
    signal:"a distant bell with no echo",
    observation:"The floor remembers the weight of repeated footsteps. Its recorded depth is 5, and its trace number is 1188.",
    clue:"A repeated step can open a door, but only once. Fragment index: 1188.",
    lesson:"Returning is not the same as repeating.",
    response:"The path behind you quietly changes its shape.",
    reward:"a path that remembers"
  },
  {
    id:1189,
    name:"Inside the Cloud Vault · 1189",
    region:"Quiet Reach",
    signal:"a hum that follows silence",
    observation:"A quiet presence copies your habits without copying your shape. Its recorded depth is 6, and its trace number is 1189.",
    clue:"The second path is real only after you turn away. Fragment index: 1189.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The air grows still, waiting for another choice.",
    reward:"an echo token"
  },
  {
    id:1190,
    name:"Under the Cloud Vault · 1190",
    region:"Moss Quarter",
    signal:"a warm line beneath the stone",
    observation:"A mark appears only after you have passed it twice. Its recorded depth is 7, and its trace number is 1190.",
    clue:"Do not confuse a reflection with an entrance. Fragment index: 1190.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"A small opening appears in the wall of darkness.",
    reward:"a sealed memory"
  },
  {
    id:1191,
    name:"Across the Cloud Vault · 1191",
    region:"Hollow Canopy",
    signal:"a distant bell with no echo",
    observation:"The air repeats a pattern you made without noticing. Its recorded depth is 1, and its trace number is 1191.",
    clue:"Two matching symbols are hiding one difference. Fragment index: 1191.",
    lesson:"Silence is information when you learn to listen.",
    response:"The echo returns with one extra note.",
    reward:"a clearer signal"
  },
  {
    id:1192,
    name:"Behind the Cloud Vault · 1192",
    region:"Lantern Expanse",
    signal:"a hum that follows silence",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 2, and its trace number is 1192.",
    clue:"Wait for the echo to finish before choosing. Fragment index: 1192.",
    lesson:"Returning is not the same as repeating.",
    response:"The ground glows for a moment, then settles.",
    reward:"a changed landmark"
  },
  {
    id:1193,
    name:"Within the Cloud Vault · 1193",
    region:"Pale Engine",
    signal:"a warm line beneath the stone",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 3, and its trace number is 1193.",
    clue:"Find the only light that does not pulse. Fragment index: 1193.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"A new mark appears beside your last footprint.",
    reward:"a hidden passage"
  },
  {
    id:1194,
    name:"At the edge of the Cloud Vault · 1194",
    region:"Frostline",
    signal:"a pale mark that shifts position",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 4, and its trace number is 1194.",
    clue:"The edge of the room is part of the puzzle. Fragment index: 1194.",
    lesson:"Some doors open only after you stop forcing them.",
    response:"The observer pauses, then follows at a distance.",
    reward:"a second chance"
  },
  {
    id:1195,
    name:"Where the Cloud Vault · 1195",
    region:"Last Horizon",
    signal:"a small star below the horizon",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 5, and its trace number is 1195.",
    clue:"The safest route is not always the shortest. Fragment index: 1195.",
    lesson:"Silence is information when you learn to listen.",
    response:"The room rearranges its shadows into a new pattern.",
    reward:"a path that remembers"
  },
  {
    id:1196,
    name:"Before the Cloud Vault · 1196",
    region:"Glasswater Basin",
    signal:"three notes with no source",
    observation:"An invisible current bends toward the route you avoid. Its recorded depth is 6, and its trace number is 1196.",
    clue:"Your previous route is the map for this one. Fragment index: 1196.",
    lesson:"Returning is not the same as repeating.",
    response:"A thin line of light points toward an unvisited place.",
    reward:"an echo token"
  },
  {
    id:1197,
    name:"After the Cloud Vault · 1197",
    region:"Blue Divide",
    signal:"a slow rhythm under the wind",
    observation:"The place changes slightly whenever you stop watching it. Its recorded depth is 7, and its trace number is 1197.",
    clue:"Move once, pause once, then listen again. Fragment index: 1197.",
    lesson:"Patterns are useful, but they can become traps.",
    response:"The signal shifts to the side, as if making room for you.",
    reward:"a stored reflection"
  },
  {
    id:1198,
    name:"Between the Cloud Vault · 1198",
    region:"Ember Archive",
    signal:"a small star below the horizon",
    observation:"An old shape returns, but one detail has been replaced. Its recorded depth is 1, and its trace number is 1198.",
    clue:"Look for the mark that does not match its neighbours. Fragment index: 1198.",
    lesson:"Curiosity changes what becomes visible.",
    response:"A distant light answers with one measured flash.",
    reward:"a new depth"
  },
  {
    id:1199,
    name:"Above the Cloud Vault · 1199",
    region:"Echo Marsh",
    signal:"three notes with no source",
    observation:"The horizon moves when you choose not to look at it. Its recorded depth is 2, and its trace number is 1199.",
    clue:"Count the spaces between the lights, not the lights themselves. Fragment index: 1199.",
    lesson:"An unfamiliar path can carry a familiar answer.",
    response:"The path behind you quietly changes its shape.",
    reward:"a quiet clue"
  },
  {
    id:1200,
    name:"Below the Cloud Vault · 1200",
    region:"Last Horizon",
    signal:"a slow rhythm under the wind",
    observation:"The silence changes pitch after every new decision. Its recorded depth is 3, and its trace number is 1200.",
    clue:"The world reveals its pattern to patient explorers. Fragment index: 1200.",
    lesson:"Observation can be a form of movement.",
    response:"The air grows still, waiting for another choice.",
    reward:"a memory fragment"
  }
];

// ====================== MIMESIS WORLD ENGINE ======================
const MI_KEY = "mobile_mimesis_world_v1";
const MI = {
  running:false, frame:0, tick:0, gridW:18, gridH:13, tile:50,
  x:8, y:6, facing:{x:0,y:1}, map:[], objects:[], visited:{},
  memories:[], fragments:0, depth:1, steps:0, scans:0, listens:0,
  choices:0, repeated:0, cautious:0, bold:0, pattern:0, lastMove:"",
  adaptation:0, profile:"UNREAD", seed:73421, modal:null, lastInteract:0,
  particles:[], lastTime:0, canvas:null, ctx:null
};
const MI_BIOMES = [
  {name:"THE QUIET REACH",ground:"#172b39",accent:"#6ad6c4",sky:"#111d31"},
  {name:"GLASSWATER BASIN",ground:"#193444",accent:"#83d8ed",sky:"#10243a"},
  {name:"THE HOLLOW CANOPY",ground:"#233a34",accent:"#a2d99c",sky:"#152c2c"},
  {name:"EMBER ARCHIVE",ground:"#49302c",accent:"#ffb078",sky:"#2a1d2d"},
  {name:"THE PALE ENGINE",ground:"#30334a",accent:"#c0b8ff",sky:"#171b35"},
  {name:"THE MIRROR WASTE",ground:"#3c3548",accent:"#e4b8ed",sky:"#201c36"},
  {name:"THE LAST HORIZON",ground:"#293c50",accent:"#b8e9ff",sky:"#101b34"}
];
const MI_TILES = {floor:0,wall:1,water:2,glow:3,gate:4,shard:5,echo:6,rift:7};
const MI_COLORS = ["#172b39","#26354b","#1b3d48","#31505a","#39425c","#40384d"];
const MI_LINES = [
 "The air changes when you turn away.",
 "Something beneath the floor is counting.",
 "A path has appeared where you hesitated.",
 "The silence seems arranged around your footsteps.",
 "The distant light moves only when you do.",
 "A familiar shape waits at the edge of sight.",
 "The world has kept the shape of your last decision.",
 "A quiet pulse travels through the stones."
];
function miRand(){
  MI.seed=(MI.seed*1664525+1013904223)>>>0;
  return MI.seed/4294967296;
}
function miPick(list){return list[Math.floor(miRand()*list.length)];}
function miEl(id){return document.getElementById(id);}
function miText(id,value){const e=miEl(id);if(e)e.textContent=value;}
function miLog(message){
  const entry={message,time:Date.now(),depth:MI.depth};
  MI.memories.unshift(entry);
  MI.memories=MI.memories.slice(0,40);
  const box=miEl("mi-log");
  if(box){box.innerHTML="";MI.memories.slice(0,7).forEach(m=>{const d=document.createElement("div");d.textContent="D"+m.depth+" · "+m.message;box.appendChild(d);});}
  miStats();
}
function miStats(){
  miText("mi-level",String(MI.depth).padStart(2,"0"));
  miText("mi-memories",MI.memories.length);
  miText("mi-fragments",MI.fragments);
  const read=Math.min(99,Math.round(MI.adaptation));
  miText("mi-instinct",read+"%");
  const bar=miEl("mi-adapt-bar");if(bar)bar.style.width=read+"%";
  const b=MI_BIOMES[(MI.depth-1)%MI_BIOMES.length];
  miText("mi-biome",b.name);
  miText("mi-world-state",MI.profile==="UNREAD"?"OBSERVING":MI.profile);
}
function miLoad(){
  try{
    const raw=localStorage.getItem(MI_KEY);
    if(!raw)return false;
    const d=JSON.parse(raw);
    if(!d||d.version!==1)return false;
    ["x","y","fragments","depth","steps","scans","listens","choices","repeated","cautious","bold","pattern","adaptation","seed"].forEach(k=>{if(Number.isFinite(d[k]))MI[k]=d[k];});
    MI.memories=Array.isArray(d.memories)?d.memories.slice(0,40):[];
    MI.visited=d.visited&&typeof d.visited==="object"?d.visited:{};
    MI.profile=d.profile||"UNREAD";
    return true;
  }catch(e){return false;}
}
function miSave(){
  const d={version:1,x:MI.x,y:MI.y,fragments:MI.fragments,depth:MI.depth,steps:MI.steps,scans:MI.scans,listens:MI.listens,choices:MI.choices,repeated:MI.repeated,cautious:MI.cautious,bold:MI.bold,pattern:MI.pattern,adaptation:MI.adaptation,seed:MI.seed,memories:MI.memories,visited:MI.visited,profile:MI.profile};
  try{localStorage.setItem(MI_KEY,JSON.stringify(d));miText("mi-response","World saved on this device. It will remember your path.");miLog("The world sealed a copy of this moment.");}
  catch(e){miText("mi-response","This browser could not save the world. Your current session is still active.");}
}
function miStart(){
  if(!MI.canvas){MI.canvas=miEl("mi-canvas");if(!MI.canvas)return;MI.ctx=MI.canvas.getContext("2d");}
  const loaded=miLoad();
  if(!MI.map.length)miBuildWorld();
  MI.running=true;
  miStats();miDraw();
  if(!MI._loop){MI._loop=true;requestAnimationFrame(miLoop);}
  if(!MI._keys){MI._keys=true;window.addEventListener("keydown",miKeyDown);}
  if(!MI._touch){MI._touch=true;MI.canvas.addEventListener("pointerdown",miPointer);}
  if(!MI._welcome){MI._welcome=true;miLog(loaded?"You returned. The world remembers your earlier route.":"You entered a place that has no name yet.");}
}
function miBuildWorld(){
  const w=MI.gridW,h=MI.gridH;
  MI.map=Array.from({length:h},(_,y)=>Array.from({length:w},(_,x)=>{
    if(x===0||y===0||x===w-1||y===h-1)return MI_TILES.wall;
    const r=miRand();
    if(r<.10)return MI_TILES.wall;
    if(r<.16)return MI_TILES.water;
    if(r<.19)return MI_TILES.glow;
    return MI_TILES.floor;
  }));
  MI.map[MI.y][MI.x]=MI_TILES.floor;
  MI.objects=[];
  const kinds=["shard","echo","gate","rift"];
  for(let i=0;i<13;i++){
    let x=1+Math.floor(miRand()*(w-2)),y=1+Math.floor(miRand()*(h-2));
    if(MI.map[y][x]===MI_TILES.wall|| (x===MI.x&&y===MI.y)){i--;continue;}
    const kind=miPick(kinds);
    MI.map[y][x]=MI_TILES[ kind ];
    MI.objects.push({x,y,kind,used:false,id:MI.objects.length});
  }
  MI.visited[MI.depth+":"+MI.x+":"+MI.y]=true;
}
function miLoop(t){
  if(!MI._loop)return;
  if(MI.running){MI.frame++;if(t-MI.lastTime>45){MI.lastTime=t;miDraw();}}
  requestAnimationFrame(miLoop);
}
function miDraw(){
  if(!MI.ctx||!MI.running)return;
  const c=MI.ctx,w=c.canvas.width,h=c.canvas.height;
  const tw=w/MI.gridW,th=h/MI.gridH;
  const biome=MI_BIOMES[(MI.depth-1)%MI_BIOMES.length];
  c.clearRect(0,0,w,h);
  const grad=c.createLinearGradient(0,0,w,h);grad.addColorStop(0,biome.sky);grad.addColorStop(1,"#080d1b");c.fillStyle=grad;c.fillRect(0,0,w,h);
  for(let y=0;y<MI.gridH;y++)for(let x=0;x<MI.gridW;x++){
    const t=MI.map[y][x],px=x*tw,py=y*th;
    if(t===MI_TILES.wall){c.fillStyle="#0a1020";c.fillRect(px,py,tw,th);c.fillStyle="#26324b";c.fillRect(px+2,py+2,tw-4,th-4);}
    else{
      c.fillStyle=(x+y)%2?biome.ground:"#1c293b";c.fillRect(px,py,tw,th);
      c.strokeStyle="#ffffff0a";c.strokeRect(px,py,tw,th);
      if(t===MI_TILES.water){c.fillStyle="#2c8ba077";c.fillRect(px+3,py+5,tw-6,th-10);c.strokeStyle="#8be8f055";c.beginPath();c.moveTo(px+7,py+th/2);c.lineTo(px+tw-7,py+th/2);c.stroke();}
      if(t===MI_TILES.glow){c.fillStyle=biome.accent+"55";c.beginPath();c.arc(px+tw/2,py+th/2,tw*.23,0,Math.PI*2);c.fill();}
      if(t===MI_TILES.shard){c.fillStyle="#a9f7ef";c.beginPath();c.moveTo(px+tw/2,py+9);c.lineTo(px+tw-10,py+th/2);c.lineTo(px+tw/2,py+th-9);c.lineTo(px+10,py+th/2);c.closePath();c.fill();}
      if(t===MI_TILES.echo){c.strokeStyle="#c8a9ff";c.lineWidth=3;c.beginPath();c.arc(px+tw/2,py+th/2,tw*.22+Math.sin(MI.frame/12)*3,0,Math.PI*2);c.stroke();}
      if(t===MI_TILES.gate){c.strokeStyle="#ffd38b";c.lineWidth=4;c.strokeRect(px+tw*.3,py+th*.16,tw*.4,th*.68);}
      if(t===MI_TILES.rift){c.fillStyle="#a56bdf88";c.beginPath();c.ellipse(px+tw/2,py+th/2,tw*.18,th*.38,Math.sin(MI.frame/25)*.2,0,Math.PI*2);c.fill();}
    }
  }
  // The observer is a moving light that reacts to the player's movement profile.
  const ox=(MI.gridW-2-MI.x*.38)*tw,oy=(MI.y*.55+1)*th;
  c.fillStyle="#b9a4ff22";c.beginPath();c.arc(ox,oy,25+Math.sin(MI.frame/8)*5,0,Math.PI*2);c.fill();
  c.fillStyle="#d8caff";c.beginPath();c.arc(ox,oy,5,0,Math.PI*2);c.fill();
  // Player marker.
  const px=MI.x*tw+tw/2,py=MI.y*th+th/2;
  c.fillStyle=biome.accent+"44";c.beginPath();c.arc(px,py,tw*.42,0,Math.PI*2);c.fill();
  c.fillStyle="#f4ffff";c.beginPath();c.arc(px,py,tw*.19,0,Math.PI*2);c.fill();
  c.strokeStyle="#ffffff";c.lineWidth=2;c.beginPath();c.moveTo(px,py);c.lineTo(px+MI.facing.x*tw*.35,py+MI.facing.y*th*.35);c.stroke();
  // Soft drifting motes.
  for(let i=0;i<18;i++){const xx=(i*97+MI.frame*.32)%w,yy=(i*53+Math.sin(MI.frame/20+i)*18)%h;c.fillStyle="#dceaff33";c.fillRect(xx,yy,2,2);}
}
function miKeyDown(e){
  if(!MI.running||!miEl("mimesis-page")||miEl("mimesis-page").classList.contains("hidden"))return;
  const k=e.key.toLowerCase();
  if(["arrowup","w"].includes(k)){e.preventDefault();miMove(0,-1);}
  else if(["arrowdown","s"].includes(k)){e.preventDefault();miMove(0,1);}
  else if(["arrowleft","a"].includes(k)){e.preventDefault();miMove(-1,0);}
  else if(["arrowright","d"].includes(k)){e.preventDefault();miMove(1,0);}
  else if(k===" "||k==="e"){e.preventDefault();miInteract();}
}
function miPointer(e){
  if(!MI.running)return;
  const r=MI.canvas.getBoundingClientRect(),x=(e.clientX-r.left)/r.width*MI.gridW,y=(e.clientY-r.top)/r.height*MI.gridH;
  const dx=x-(MI.x+.5),dy=y-(MI.y+.5);
  if(Math.abs(dx)+Math.abs(dy)<1.1){miInteract();return;}
  if(Math.abs(dx)>Math.abs(dy))miMove(Math.sign(dx),0);else miMove(0,Math.sign(dy));
}
function miMove(dx,dy){
  if(!MI.running)miStart();
  if(!MI.running)return;
  MI.facing={x:dx,y:dy};
  const nx=MI.x+dx,ny=MI.y+dy;
  if(nx<1||ny<1||nx>=MI.gridW-1||ny>=MI.gridH-1||MI.map[ny][nx]===MI_TILES.wall){
    MI.cautious++;MI.adaptation=Math.min(99,MI.adaptation+.35);
    miText("mi-hint","A boundary. The world noticed your hesitation.");
    if(MI.cautious%3===0)miLog("You tested the edge instead of crossing it.");
    miReact();return;
  }
  MI.x=nx;MI.y=ny;MI.steps++;
  const move=dx+","+dy;
  if(move===MI.lastMove)MI.repeated++;else MI.pattern=Math.max(0,MI.pattern-1);
  MI.lastMove=move;
  if(MI.steps%5===0)MI.adaptation=Math.min(99,MI.adaptation+1.2);
  const key=MI.depth+":"+nx+":"+ny;
  if(!MI.visited[key]){MI.visited[key]=true;MI.bold++;MI.adaptation=Math.min(99,MI.adaptation+.7);}
  const tile=MI.map[ny][nx];
  if(tile===MI_TILES.water){MI.cautious++;miText("mi-hint","Cold water records the direction you chose.");}
  else if(tile===MI_TILES.glow){MI.fragments++;MI.map[ny][nx]=MI_TILES.floor;miLog("A quiet light folded itself into a memory fragment.");}
  const obj=MI.objects.find(o=>o.x===nx&&o.y===ny&&!o.used);
  if(obj){MI.lastInteract=obj.id;miText("mi-hint","Something is close. Tap ✦ to understand it.");}
  miReact();miStats();miDraw();
}
function miReact(){
  const explorer=MI.bold>MI.cautious+2;
  const careful=MI.cautious>MI.bold+2;
  const repetitive=MI.repeated>5;
  MI.profile=explorer?"CURIOUS":careful?"CAUTIOUS":repetitive?"PATTERN-SEEKER":"UNREAD";
  let msg;
  if(explorer)msg="New paths brighten ahead of you. The world is rewarding exploration.";
  else if(careful)msg="The edges grow quieter. The world is learning where you hesitate.";
  else if(repetitive)msg="A familiar pattern returns in a different place. It is copying your rhythm.";
  else msg=miPick(MI_LINES);
  miText("mi-response",msg);miStats();
}
function miInteract(){
  if(!MI.running)miStart();
  const obj=MI.objects.find(o=>o.x===MI.x&&o.y===MI.y&&!o.used)||
    MI.objects.find(o=>!o.used&&Math.abs(o.x-MI.x)+Math.abs(o.y-MI.y)===1);
  if(!obj){miText("mi-hint","Nothing answers here. Try a glowing mark or a strange shape.");return;}
  obj.used=true;
  if(obj.kind==="shard"){MI.fragments++;miLog("You recovered a fragment the world tried to hide.");miShowFragment();}
  else if(obj.kind==="echo"){MI.listens++;MI.adaptation=Math.min(99,MI.adaptation+3);miEcho();}
  else if(obj.kind==="gate"){miGate();}
  else if(obj.kind==="rift"){miRift();}
  MI.map[obj.y][obj.x]=MI_TILES.floor;miStats();miDraw();
}
function miShowFragment(){
  const item=MI_ARCHIVE[(MI.fragments*37+MI.depth*19+MI.seed)%MI_ARCHIVE.length];
  miModal("MEMORY FRAGMENT",`<p><b>${miSafe(item.name)}</b></p><p>${miSafe(item.observation)}</p><p><i>${miSafe(item.clue)}</i></p><button class="mi-close" onclick="miClose()">KEEP MEMORY</button>`);
}
function miEcho(){
  const line=miPick(MI_LINES);
  miModal("AN ECHO ANSWERS",`<p>${miSafe(line)}</p><p>It repeats a sound you made earlier, but the timing is wrong.</p><button class="mi-close" onclick="miClose()">LISTEN AGAIN LATER</button>`);
  miLog("An echo returned a sound from somewhere behind you.");
}
function miGate(){
  MI.choices++;
  const title=MI.profile==="CURIOUS"?"THE OPENING":"THE NARROW DOOR";
  miModal(title,`<p>A gate has formed from the paths you have taken. It is not locked. It is waiting for a decision.</p>
   <button class="mi-choice" onclick="miChoose('enter')">STEP THROUGH — accept an unknown place</button>
   <button class="mi-choice" onclick="miChoose('study')">STUDY THE FRAME — learn its pattern</button>
   <button class="mi-choice" onclick="miChoose('leave')">WALK AWAY — keep this place unchanged</button>`);
}
function miChoose(choice){
  miClose();MI.choices++;
  if(choice==="enter"){MI.depth++;MI.x=2;MI.y=2;miBuildWorld();MI.fragments++;miLog("You crossed into depth "+MI.depth+". The world changed its rules.");}
  else if(choice==="study"){MI.pattern+=2;MI.adaptation=Math.min(99,MI.adaptation+6);miLog("You studied the gate instead of using it. A hidden mark appeared.");}
  else{MI.cautious+=2;miLog("You left the gate behind. It will remember that.");}
  miReact();miStats();miDraw();miSave();
}
function miRift(){
  MI.choices++;
  miModal("THE MIRROR RIFT",`<p>The rift shows a version of this room with one detail changed. The world is testing whether you notice.</p>
   <button class="mi-choice" onclick="miRiftChoice('near')">FOLLOW THE NEAREST LIGHT</button>
   <button class="mi-choice" onclick="miRiftChoice('far')">FOLLOW THE DISTANT LIGHT</button>`);
}
function miRiftChoice(choice){
  miClose();
  if(choice==="near"){MI.fragments++;MI.adaptation=Math.min(99,MI.adaptation+4);miLog("You trusted the nearest signal and found a memory.");}
  else{MI.depth++;MI.log=MI.memories;miLog("You followed the distant signal. The next depth opened early.");}
  MI.x=2;MI.y=2;miBuildWorld();miStats();miDraw();
}
function miModal(title,body){
  const modal=miEl("mi-modal"),content=miEl("mi-modal-content");if(!modal||!content)return;
  content.innerHTML=`<h3>${title}</h3>${body}`;modal.classList.add("open");
}
function miClose(){const m=miEl("mi-modal");if(m)m.classList.remove("open");}
function miSafe(v){return String(v).replace(/[&<>"']/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));}
function miScan(){
  if(!MI.running)miStart();MI.scans++;MI.adaptation=Math.min(99,MI.adaptation+2);
  const nearby=MI.objects.filter(o=>!o.used&&Math.abs(o.x-MI.x)+Math.abs(o.y-MI.y)<=4);
  if(nearby.length){const o=nearby[0];miText("mi-response",`A ${o.kind} signal is ${Math.abs(o.x-MI.x)+Math.abs(o.y-MI.y)} steps away. Its pulse matches your recent movement.`);}
  else miText("mi-response","No object nearby. The scan reveals faint tracks that were not here before.");
  miLog("You scanned the area. The world recorded your curiosity.");miStats();
}
function miRest(){
  if(!MI.running)miStart();MI.listens++;MI.adaptation=Math.min(99,MI.adaptation+1.5);
  const msg=MI.repeated>4?"The silence repeats your movement rhythm.":"Beneath the wind, a slow pulse answers.";
  miText("mi-response",msg);miLog("You stopped moving and listened. The world did not.");miReact();
}
function miJournal(){
  const rows=MI.memories.length?MI.memories.map(m=>`<p>DEPTH ${m.depth} · ${miSafe(m.message)}</p>`).join(""):"<p>No memories yet. Explore to create some.</p>";
  miModal("MEMORY LOG",rows+'<button class="mi-close" onclick="miClose()">CLOSE LOG</button>');
}
function miSafeRestart(){
  MI.x=8;MI.y=6;MI.depth=1;MI.fragments=0;MI.steps=0;MI.scans=0;MI.listens=0;MI.choices=0;MI.repeated=0;MI.cautious=0;MI.bold=0;MI.pattern=0;MI.adaptation=0;MI.memories=[];MI.visited={};MI.profile="UNREAD";MI.seed=73421;
  try{localStorage.removeItem(MI_KEY);}catch(e){}
  miBuildWorld();miLog("A new world opened. Nothing has learned you yet.");miStats();miDraw();
}
document.addEventListener("visibilitychange",()=>{if(document.hidden&&MI.running)miSave();});

// Keep the MIMESIS simulation paused whenever another app page is shown.
const miOriginalShowPage = window.showPage;
window.showPage = function(id){
  if(id !== "mimesis-page") MI.running = false;
  return miOriginalShowPage.apply(this, arguments);
};
</script>

<script>
/* EXPERIENCE SETTINGS: persistent, defensive and independent from app features. */
(function(){
 const key='mobile_app_experience_v2';
 let prefs={motion:true,sound:true,glow:true};
 try{prefs={...prefs,...JSON.parse(localStorage.getItem(key)||'{}')}}catch(e){}
 window.mobileSetPreference=function(name,value){
  if(!(name in prefs))return;
  prefs[name]=!!value;
  try{localStorage.setItem(key,JSON.stringify(prefs))}catch(e){}
  apply();
 };
 function apply(){
  document.body.classList.toggle('mobile-no-motion',!prefs.motion);
  document.body.classList.toggle('mobile-no-glow',!prefs.glow);
  document.documentElement.dataset.mobileSound=prefs.sound?'on':'off';
  ['motion','sound','glow'].forEach(k=>{const el=document.getElementById('pref-'+k);if(el)el.checked=!!prefs[k]});
 }
 window.mobileResetPreferences=function(){prefs={motion:true,sound:true,glow:true};try{localStorage.removeItem(key)}catch(e){}apply()};
 const oldShow=window.showPage;
 if(typeof oldShow==='function'){
  window.showPage=function(id){const result=oldShow.apply(this,arguments);if(id==='settings-page')setTimeout(apply,0);return result};
 }
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',apply,{once:true});else apply();
})();
</script>

</body>
</html>
"""


# Render the existing mobile.app interface inside a controlled iframe.
app_markup = json.dumps(APP).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
launcher = f"""
<div id="mobile-app-frame-root" style="width:100%;min-height:1000px;overflow:visible"></div>
<script>
(function() {{
  const root = document.getElementById("mobile-app-frame-root");
  if (!root) return;
  const frame = document.createElement("iframe");
  frame.title = "mobile.app";
  frame.setAttribute("scrolling", "yes");
  frame.setAttribute("sandbox", "allow-scripts allow-same-origin allow-forms allow-downloads");
  frame.style.cssText = "display:block;width:100%;height:1000px;border:0;background:transparent;";
  frame.srcdoc = {app_markup};
  root.appendChild(frame);
}})();
</script>
"""
st.html(launcher, unsafe_allow_javascript=True)
