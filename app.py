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
.tile{min-height:104px;padding:13px 7px;border-radius:18px;background:linear-gradient(145deg,#ffffff28,#ffffff0c);border:1px solid #ffffff35;text-align:center;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;color:#f4fffd}
.tile .emoji{font-size:27px}
.tile span:last-child{font-size:11px;font-weight:800}
.wide-tile{width:100%;display:flex;align-items:center;gap:15px;padding:18px;border-radius:20px;text-align:left;color:white;background:linear-gradient(110deg,#19b99b,#318fc6,#7565d9);border:1px solid #ffffff60;box-shadow:0 10px 25px #081b3440}
.wide-icon{font-size:37px}
.wide-title{font-size:18px;font-weight:900;margin-bottom:5px}
.wide-desc{font-size:11px;color:#effffb;line-height:1.45}
.row-tile{width:100%;display:flex;align-items:center;gap:12px;padding:14px 16px;margin-top:10px;border-radius:16px;text-align:left;color:#f2fffc;background:#ffffff16;border:1px solid #ffffff30}
.row-tile .emoji{font-size:22px}
/* Premium color accents for home-screen buttons only */
#home-page .tile:nth-child(1){background:linear-gradient(145deg,#e5b85c,#a96d28);border-color:#ffe2a0;color:#fff}
#home-page .tile:nth-child(2){background:linear-gradient(145deg,#6e9de8,#3456a5);border-color:#b9d3ff;color:#fff}
#home-page .tile:nth-child(3){background:linear-gradient(145deg,#a987df,#6847a7);border-color:#ddc8ff;color:#fff}
#home-page .wide-tile{background:linear-gradient(110deg,#168d78,#176b91,#4b4c9d);border-color:#a8f5e5}
#home-page .row-tile:nth-of-type(1){background:linear-gradient(110deg,#246b65,#348d80);border-color:#8de2d2}
#home-page .row-tile:nth-of-type(2){background:linear-gradient(110deg,#5a4a91,#8265bd);border-color:#d0baff}
#home-page .school-btn{background:linear-gradient(110deg,#b34b38,#d18b36);border-color:#ffe0a0}
.logout-btn{background:#e53935!important;border-color:#e53935!important;color:#fff!important}
#school-page{position:relative;isolation:isolate;padding:12px;border-radius:22px;overflow:hidden;background-image:linear-gradient(180deg,rgba(10,20,35,.72),rgba(10,20,35,.86)),url("data:image/jpeg;base64,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
