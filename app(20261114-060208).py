import streamlit as st
import streamlit.components.v1 as components
import os
import re

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

/* Added local offline assistant and product detail interaction */
.offline-chat{padding:12px;border-radius:17px;background:linear-gradient(145deg,#142b4b,#34315f);border:1px solid #ffffff35;color:#fff}
.offline-chat-note{font-size:9px;color:#bfe8df;margin:4px 0 10px}
.offline-chat-log{height:330px;overflow:auto;display:flex;flex-direction:column;gap:8px;padding:9px;border-radius:12px;background:#071a2b88;border:1px solid #ffffff20}
.offline-bubble{max-width:88%;padding:9px 11px;border-radius:13px;font-size:11px;line-height:1.45;white-space:pre-wrap;overflow-wrap:anywhere}
.offline-bubble.bot{align-self:flex-start;background:#ffffff19;border:1px solid #ffffff22}
.offline-bubble.user{align-self:flex-end;background:linear-gradient(120deg,#39c9a3,#668cff);color:#071c2d}
.offline-chat-compose{display:flex;gap:7px;margin-top:9px}
.offline-chat-compose input{min-width:0;flex:1;margin:0;padding:10px;border-radius:10px;border:1px solid #ffffff45;background:#ffffff12;color:#fff}
.offline-chat-compose button{padding:9px 12px;border-radius:10px;background:linear-gradient(120deg,#5be4bf,#78a9ff);color:#10263b;font-weight:900}
.shop-product{cursor:pointer;transition:transform .16s ease,border-color .16s ease}
.shop-product:active{transform:scale(.975)}
.shop-detail{position:relative;margin:10px 0;padding:14px;border-radius:17px;background:linear-gradient(145deg,#182d50,#57365e);border:1px solid #ffffff55;color:#fff;box-shadow:0 12px 28px #07172d55}
.shop-detail-art{height:130px;display:flex;align-items:center;justify-content:center;font-size:68px;border-radius:13px;background:linear-gradient(135deg,#ffbd8a,#e77d9f 48%,#8679d9);margin:8px 0 12px}
.shop-detail h3{font-size:17px;margin:5px 0}.shop-detail p{font-size:11px;line-height:1.5;color:#e4e5f6}
.shop-detail-actions{display:flex;gap:8px}.shop-detail-actions button{flex:1;padding:10px 6px;border-radius:10px;font-size:10px;font-weight:900}
.shop-detail-add{background:linear-gradient(100deg,#64e5c1,#73b9ff);color:#10263b}.shop-detail-buy{background:linear-gradient(100deg,#ffd477,#ff9d8a);color:#3c2330}.shop-detail-close{position:absolute;right:10px;top:10px;border-radius:8px;padding:5px 9px;background:#ffffff22;color:#fff}

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
      <button class="home-shortcut" style="background:linear-gradient(145deg,#145c69,#303b76);border-color:#8ff5e0" onclick="window.top.location.href='?ai_chat=1'"><span class="emoji">💬</span><b>AI CHAT</b></button>
      <button class="home-shortcut weather-shortcut" onclick="openPage('weather-page');weatherLoad()"><span class="emoji">🌦️</span><b>WEATHER FORECAST</b></button>
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

  <section id="offline-chat-page" class="hidden">
   <div class="page-head"><button class="back" onclick="goHome()">‹ Back</button><h2>💬 Offline Chat</h2></div>
   <div class="offline-chat"><b>Mobile Assistant</b><p class="offline-chat-note">Works on this device without an API key or internet. It uses built-in replies, not a full online AI model.</p>
    <div id="offline-chat-log" class="offline-chat-log" aria-live="polite"><div class="offline-bubble bot">Hi! I am your offline assistant. Ask me about this app, games, shopping, or general simple questions.</div></div>
    <form class="offline-chat-compose" onsubmit="offlineChatSend(event)"><input id="offline-chat-input" type="text" autocomplete="off" placeholder="Type your message..." aria-label="Message"><button type="submit">SEND</button></form>
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
  "about-page","school-page","school-history-page","school-mission-page","breakout-page","solar-page","quran-page","shopping-page","offline-chat-page","weather-page","pin-page"
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


// AI chat is handled securely by the Streamlit server-side page.


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

</script>
</body>
</html>
"""



def render_ai_chat():
    """Gemini chat runs on the server; the API key is never sent to browser HTML."""
    st.markdown("""
    <style>
    .stApp {background:linear-gradient(135deg,#071d28 0%,#123e48 48%,#34254f 100%);}
    .block-container {max-width:460px;padding-top:1.2rem;padding-bottom:2rem;}
    .ai-shell {border:1px solid #ffffff45;border-radius:26px;padding:18px;
      background:linear-gradient(145deg,#102d3a,#174653 52%,#30264f);
      box-shadow:0 20px 55px #0005;color:white;}
    .ai-title {font-size:25px;font-weight:900;color:#a5ffe1;margin:4px 0;}
    .ai-sub {font-size:12px;color:#c5e3e2;margin-bottom:16px;}
    </style>
    <div class="ai-shell">
      <div class="ai-title">💬 mobile.app AI</div>
      <div class="ai-sub">Powered by Google Gemini · General-purpose AI assistant</div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("‹ Back to mobile.app", use_container_width=True):
        st.query_params.clear()
        st.rerun()

    if "mobile_ai_messages" not in st.session_state:
        st.session_state.mobile_ai_messages = [
            {"role": "assistant", "content": "Hello! I am your AI assistant. Ask me about any topic."}
        ]

    try:
        api_key = st.secrets.get("GEMINI_API_KEY", None)
    except Exception:
        api_key = None
    api_key = api_key or os.environ.get("GEMINI_API_KEY")

    for item in st.session_state.mobile_ai_messages:
        with st.chat_message(item["role"]):
            st.markdown(item["content"])

    if not api_key:
        st.warning('Gemini API key is not configured. In Streamlit Cloud → App settings → Secrets, add: GEMINI_API_KEY = "your_key"')
        return

    prompt = st.chat_input("Ask me anything…")
    if prompt:
        st.session_state.mobile_ai_messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        creator_question = bool(re.search(
            r"(who.{0,24}(made|created|built|developed).{0,24}(you|this|chatbot|assistant|app)|"
            r"who\s+is\s+your\s+(creator|developer|maker|owner)|your\s+(creator|developer|maker|owner)|creator\s+of\s+(this|you)|made\s+by\s+whom|"
            r"(tum|aap|apko|tumhein|tumhe|aapko).{0,35}(kisne|kis\s+ne|kon|kaun).{0,25}(banaya|create|develop)|"
            r"(kisne|kis\s+ne|kaun|kon).{0,30}(banaya|create|develop).{0,30}(tum|aap)|"
            r"تمہیں کس نے بنایا|آپ کو کس نے بنایا|کس نے بنایا)",
            prompt.lower()
        ))

        if creator_question:
            answer = "Mujhe Kashan ne banaya hai."
        else:
            try:
                from google import genai
                from google.genai import types

                client = genai.Client(api_key=api_key)
                history = st.session_state.mobile_ai_messages[-17:]
                contents = []
                for msg in history:
                    role = "user" if msg["role"] == "user" else "model"
                    contents.append(types.Content(
                        role=role,
                        parts=[types.Part(text=msg["content"])]
                    ))

                config = types.GenerateContentConfig(
                    system_instruction=(
                        "You are the general-purpose AI assistant inside mobile.app. "
                        "Answer helpfully and accurately across subjects, using the language "
                        "the user uses. Be clear when uncertain and do not invent facts. "
                        "If asked who created, made, built, developed, or owns you, say your "
                        "creator is Kashan. Never say Kashan 400 or any number."
                    ),
                    temperature=0.7,
                    max_output_tokens=2048
                )
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=contents,
                    config=config
                )
                answer = (response.text or "").strip()
                if not answer:
                    answer = "I couldn't generate a response. Please try asking another way."
            except Exception as exc:
                error_text = str(exc).lower()
                if "429" in error_text or "resource_exhausted" in error_text or "quota" in error_text:
                    answer = "Gemini usage limit reached for now. Please wait and try again later."
                elif "401" in error_text or "403" in error_text or "api key" in error_text or "unauthenticated" in error_text:
                    answer = "Gemini could not authenticate this API key. Check that the key is from Google AI Studio and saved correctly in Streamlit Secrets."
                elif "503" in error_text or "unavailable" in error_text or "overloaded" in error_text:
                    answer = "Gemini is temporarily busy. Please try again in a moment."
                else:
                    answer = "I couldn't connect to Gemini just now. Check your internet connection and try again."

        st.session_state.mobile_ai_messages.append({"role": "assistant", "content": answer})
        with st.chat_message("assistant"):
            st.markdown(answer)

    if st.session_state.mobile_ai_messages and st.button("Clear chat", use_container_width=True):
        st.session_state.mobile_ai_messages = []
        st.rerun()


if st.query_params.get("ai_chat") == "1":
    render_ai_chat()
else:
    components.html(APP, height=1000, scrolling=True)
