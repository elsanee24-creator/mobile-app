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
 --mint:#65f5c1;
 --aqua:#35d8e8;
 --blue:#668cff;
 --violet:#a77bff;
 --gold:#ffd477;
 --ink:#102b35;
 --paper:#f2fff9;
 --muted:#b9d9d5;
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
 margin:0 auto;padding:10px;
 border-radius:38px;
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

/* INDIVIDUAL PAGE THEMES */
.screen:has(#login-page:not(.hidden)),
.screen:has(#pin-page:not(.hidden)){
 background:
 radial-gradient(circle at 15% 10%,#40e9c766,transparent 40%),
 linear-gradient(145deg,#123e4b,#183c61 55%,#44316e);
}

.screen:has(#home-page:not(.hidden)){
 background:
 radial-gradient(circle at 90% 5%,#ffb75a66,transparent 35%),
 linear-gradient(145deg,#193b50,#254b67 50%,#51416e);
}

.screen:has(#calculator-page:not(.hidden)){
 background:
 radial-gradient(circle at 90% 10%,#ffcf6c55,transparent 38%),
 linear-gradient(145deg,#47304c,#713e55 55%,#a15b55);
}

.screen:has(#password-page:not(.hidden)){
 background:
 radial-gradient(circle at 90% 5%,#64e7ff55,transparent 38%),
 linear-gradient(145deg,#123d57,#176b80 55%,#315b83);
}

.screen:has(#notes-page:not(.hidden)){
 background:
 radial-gradient(circle at 90% 5%,#ffe49a55,transparent 38%),
 linear-gradient(145deg,#493c2d,#75543c 55%,#986d4d);
}

.screen:has(#games-page:not(.hidden)),
.screen:has(#guess-page:not(.hidden)),
.screen:has(#typing-page:not(.hidden)){
 background:
 radial-gradient(circle at 90% 5%,#c77bff55,transparent 38%),
 linear-gradient(145deg,#30265a,#49346e 55%,#743e75);
}

.screen:has(#flappy-page:not(.hidden)){
 background:
 radial-gradient(circle at 90% 5%,#ffe08b55,transparent 38%),
 linear-gradient(145deg,#15516c,#267d9b 55%,#55a9a5);
}

.screen:has(#snake-page:not(.hidden)){
 background:
 radial-gradient(circle at 90% 5%,#a4ff7750,transparent 38%),
 linear-gradient(145deg,#102f28,#15543d 55%,#28704c);
}

.screen:has(#settings-page:not(.hidden)){
 background:
 radial-gradient(circle at 90% 5%,#ff9fc855,transparent 38%),
 linear-gradient(145deg,#482c51,#754267 55%,#a45c70);
}

.screen:has(#about-page:not(.hidden)){
 background:
 radial-gradient(circle at 90% 5%,#ffe58a55,transparent 38%),
 linear-gradient(145deg,#51402c,#80603d 55%,#9d8050);
}

.topbar{
 display:flex;justify-content:space-between;align-items:center;
 color:#eafffa;font-size:12px;margin:2px 4px 20px;
}

.brand{font-weight:900;letter-spacing:2px;font-size:17px}

.pill{
 padding:7px 11px;border-radius:30px;
 background:#ffffff20;border:1px solid #ffffff35;
 color:#eafffa;font-size:11px;
}

h1,h2,h3,p{margin-top:0}
h1{font-size:30px;line-height:1.1;margin-bottom:9px}
h2{font-size:21px;margin-bottom:8px}
p{color:#c5e3e2;line-height:1.5;font-size:13px}

button{
 border:0;cursor:pointer;font-weight:800;
 font-size:13px;color:#12323a;
}

.primary{
 width:100%;padding:15px;border-radius:16px;
 background:linear-gradient(100deg,var(--mint),var(--aqua),#9bceff);
 box-shadow:0 8px 22px #36e4ca45;
}

.secondary{
 width:100%;padding:14px;border-radius:16px;
 color:#effffb;background:#ffffff16;
 border:1px solid #ffffff38;
}

.login-wrap{
 min-height:690px;display:flex;flex-direction:column;
 align-items:center;justify-content:center;text-align:center;
 padding:12px 5px;
}

.clock-panel{
 width:100%;display:flex;align-items:center;justify-content:center;
 gap:20px;margin:0 auto 25px;padding:20px 12px;
 border-radius:25px;
 background:linear-gradient(135deg,#ffffff20,#ffffff09);
 border:1px solid #ffffff40;
 box-shadow:0 12px 35px #071b3740;
}

.clock-face{
 width:116px;height:116px;position:relative;flex-shrink:0;
 border-radius:50%;
 background:radial-gradient(circle at 35% 25%,#fff,#d7fff1 55%,#91d9d0);
 border:5px solid #f5fffc;
 box-shadow:0 0 0 5px #70f5c155,0 8px 25px #061b3a70;
}

.clock-face:before{
 content:"";position:absolute;inset:8px;border-radius:50%;
 border:1px solid #7aa9a2;
}

.clock-face .number{
 position:absolute;color:#24515a;font-size:10px;font-weight:900;
 transform:translate(-50%,-50%);
}

.hand{
 position:absolute;left:50%;bottom:50%;
 transform-origin:50% 100%;border-radius:8px;
}

.hour-hand{width:5px;height:29px;background:#244c62}
.minute-hand{width:3px;height:39px;background:#287c86}
.second-hand{width:2px;height:43px;background:#ed8b65}

.clock-pin{
 position:absolute;width:9px;height:9px;border-radius:50%;
 background:#e89a58;left:50%;top:50%;transform:translate(-50%,-50%);
}

.time-info{text-align:left;min-width:0}
.digital-time{font-size:25px;font-weight:900;color:#fff;letter-spacing:1px}
.digital-date{font-size:11px;color:#c9e9e5;margin-top:7px;line-height:1.5}

.login-title{
 font-size:34px;font-weight:900;letter-spacing:1px;
 background:linear-gradient(90deg,#a5ffe1,#8ceaff,#d8b4ff,#ffe1a1);
 -webkit-background-clip:text;background-clip:text;color:transparent;
}

.login-sub{max-width:290px;margin:8px auto 25px}
.login-actions{width:100%;max-width:310px;display:grid;gap:12px}
.section{margin:18px 0}

.card{
 padding:15px;border-radius:20px;
 background:linear-gradient(135deg,#ffffff20,#ffffff0c);
 border:1px solid #ffffff35;
 box-shadow:0 8px 24px #081b3440;
}

.tile-grid{
 display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:9px;
}

.tile{
 min-height:104px;padding:13px 7px;border-radius:18px;
 background:linear-gradient(145deg,#ffffff28,#ffffff0c);
 border:1px solid #ffffff35;text-align:center;
 display:flex;flex-direction:column;align-items:center;justify-content:center;
 gap:8px;color:#f4fffd;
}

.tile .emoji{font-size:27px}
.tile span:last-child{font-size:11px;font-weight:800}

.wide-tile{
 width:100%;display:flex;align-items:center;gap:15px;
 padding:18px;border-radius:20px;text-align:left;
 color:white;background:linear-gradient(110deg,#19b99b,#318fc6,#7565d9);
 border:1px solid #ffffff60;box-shadow:0 10px 25px #081b3440;
}

.wide-icon{font-size:37px}
.wide-title{font-size:18px;font-weight:900;margin-bottom:5px}
.wide-desc{font-size:11px;color:#effffb;line-height:1.45}

.row-tile{
 width:100%;display:flex;align-items:center;gap:12px;
 padding:14px 16px;margin-top:10px;border-radius:16px;
 text-align:left;color:#f2fffc;
 background:#ffffff16;border:1px solid #ffffff30;
}

.row-tile .emoji{font-size:22px}

.page-head{display:flex;align-items:center;gap:12px;margin:6px 0 18px}

.back{
 padding:10px 13px;border-radius:12px;color:#effffb;
 background:#ffffff1c;border:1px solid #ffffff35;
}

.field{
 width:100%;padding:13px;border-radius:13px;
 border:1px solid #ffffff55;background:#ffffffed;
 color:#183a42;font-size:14px;margin:5px 0 12px;
}

.output{
 padding:14px;border-radius:14px;background:#ffffffed;
 color:#183a42;overflow-wrap:anywhere;margin:10px 0;
}

.calc-display{
 background:#eafff7;color:#173b42;border-radius:15px;
 padding:18px;text-align:right;font-size:27px;font-weight:900;
 min-height:65px;margin-bottom:10px;overflow-wrap:anywhere;
}

.calc-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:7px}

.calc-key{
 padding:17px 3px;border-radius:13px;
 background:#f2fff9;color:#173b42;font-size:16px;
}

.calc-key.op{background:#ffd477}
.calc-key.equal{background:#65f5c1}
.calc-key.clear{background:#ffb8a8}

.game-canvas{
 width:100%;display:block;border-radius:17px;
 background:linear-gradient(#6bd8ff,#b8f1ff);
 border:2px solid #ffffff55;
 touch-action:none;
}

.small-note{font-size:11px;color:#c3e2df}
.hidden{display:none!important}

/* SNAKE — COMPACT PHONE-FRIENDLY LAYOUT */
#snake-page{
 touch-action:none;
 overscroll-behavior:none;
}

#snake-page .page-head{margin-bottom:8px}
#snake-page .card{
 padding:10px;
 background:linear-gradient(145deg,#ffffff19,#ffffff08);
 border-color:#aaffbb55;
}

#snake-page .card>p:first-child{
 margin-bottom:8px;
 font-size:11px;
}

#snake-canvas{
 width:min(100%,288px);
 height:auto;
 aspect-ratio:1/1;
 margin:0 auto 8px;
 border-radius:13px;
 background:linear-gradient(145deg,#092b25,#124c38);
 border:2px solid #8cffb855;
 touch-action:none;
}

#snake-controls{
 display:grid;
 grid-template-columns:repeat(3,1fr);
 gap:6px;
 max-width:225px;
 margin:5px auto 8px;
}

#snake-controls button{
 min-height:42px;
 padding:7px;
 border-radius:12px;
 font-size:19px;
 background:linear-gradient(145deg,#d9ffe9,#8af0b7);
 color:#17432f;
 box-shadow:0 4px 10px #061b1644;
}

#snake-controls .empty-control{
 visibility:hidden;
}

#snake-page .primary{
 padding:11px;
 margin-top:4px;
}

#snake-page #snake-score{
 margin:8px 0 0;
 text-align:center;
 font-weight:800;
 color:#c9ffdc;
}

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
</style>
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
    <button class="tile" onclick="openPage('calculator-page')">
     <span class="emoji">🧮</span><span>Calculator</span>
    </button>
    <button class="tile" onclick="openPage('password-page')">
     <span class="emoji">🔐</span><span>Password</span>
    </button>
    <button class="tile" onclick="openPage('notes-page')">
     <span class="emoji">📝</span><span>Notes</span>
    </button>
   </div>

   <div class="section">
    <button class="wide-tile" onclick="openPage('games-page')">
     <span class="wide-icon">🧩</span>
     <span>
      <div class="wide-title">Gaming Hub</div>
      <div class="wide-desc">Play, challenge yourself and enjoy your mini-games collection.</div>
     </span>
     <span style="margin-left:auto;font-size:23px">›</span>
    </button>
   </div>

   <div class="section">
    <button class="row-tile" onclick="openPage('settings-page')">
     <span class="emoji">⚙️</span><b>Settings</b><span style="margin-left:auto">›</span>
    </button>
    <button class="row-tile" onclick="openPage('about-page')">
     <span class="emoji">✨</span><b>About</b><span style="margin-left:auto">›</span>
    </button>
   </div>
  </section>

  <section id="calculator-page" class="hidden">
   <div class="page-head">
    <button class="back" onclick="goHome()">‹ Back</button>
    <h2>Calculator</h2>
   </div>

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
   <div class="page-head">
    <button class="back" onclick="goHome()">‹ Back</button>
    <h2>Password Generator</h2>
   </div>

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
   <div class="page-head">
    <button class="back" onclick="goHome()">‹ Back</button>
    <h2>My Notes</h2>
   </div>

   <div class="card">
    <input class="field" id="note-title" placeholder="Note title">
    <textarea class="field" id="note-body" rows="5" placeholder="Write your note..."></textarea>
    <button class="primary" onclick="saveNote()">SAVE NOTE</button>
    <div id="notes-list" style="margin-top:15px"></div>
   </div>
  </section>

  <section id="games-page" class="hidden">
   <div class="page-head">
    <button class="back" onclick="goHome()">‹ Back</button>
    <h2>Gaming Hub</h2>
   </div>

   <p>Choose a game and enjoy your break.</p>

   <div class="tile-grid">
    <button class="tile" onclick="openPage('guess-page')">
     <span class="emoji">🔢</span><span>Number Guess</span>
    </button>
    <button class="tile" onclick="openPage('typing-page')">
     <span class="emoji">⌨️</span><span>Typing Speed</span>
    </button>
    <button class="tile" onclick="openPage('flappy-page')">
     <span class="emoji">🐦</span><span>Flappy Bird</span>
    </button>
    <button class="tile" onclick="openPage('snake-page')">
     <span class="emoji">🐍</span><span>Snake</span>
    </button>
   </div>
  </section>

  <section id="guess-page" class="hidden">
   <div class="page-head">
    <button class="back" onclick="openPage('games-page')">‹ Games</button>
    <h2>Number Guess</h2>
   </div>

   <div class="card">
    <p>Guess the secret number from 1 to 100. You have 10 chances.</p>
    <input class="field" id="guess-input" type="number" min="1" max="100" placeholder="Your guess">
    <button class="primary" onclick="makeGuess()">GUESS</button>
    <p id="guess-message">10 chances remaining.</p>
    <button class="secondary" onclick="resetGuess()">RESTART GAME</button>
   </div>
  </section>

  <section id="typing-page" class="hidden">
   <div class="page-head">
    <button class="back" onclick="openPage('games-page')">‹ Games</button>
    <h2>Typing Speed</h2>
   </div>

   <div class="card">
    <p id="typing-sentence">Small steps every day create big progress.</p>
    <textarea class="field" id="typing-input" rows="4" placeholder="Start typing the sentence..."></textarea>
    <button class="primary" onclick="startTyping()">START / RESET</button>
    <p id="typing-result">Timer: 0 seconds</p>
   </div>
  </section>

  <section id="flappy-page" class="hidden">
   <div class="page-head">
    <button class="back" onclick="openPage('games-page')">‹ Games</button>
    <h2>Flappy Bird</h2>
   </div>

   <div class="card">
    <p>Tap the game area to flap and avoid the obstacles.</p>
    <canvas id="flappy-canvas" class="game-canvas" width="360" height="460"></canvas>
    <button class="primary" onclick="startFlappy()">PLAY / RESTART</button>
    <p id="flappy-score">Score: 0</p>
   </div>
  </section>

  <section id="snake-page" class="hidden">
   <div class="page-head">
    <button class="back" onclick="openPage('games-page')">‹ Games</button>
    <h2>Snake</h2>
   </div>

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

  <section id="settings-page" class="hidden">
   <div class="page-head">
    <button class="back" onclick="goHome()">‹ Back</button>
    <h2>Settings</h2>
   </div>

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
   <div class="page-head">
    <button class="back" onclick="goHome()">‹ Back</button>
    <h2>About</h2>
   </div>

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

<script>
"""
APP += r"""
// ===============================
// MOBILE.APP — MAIN JAVASCRIPT
// ===============================

const $ = id => document.getElementById(id);

const store = {
 get(key, fallback){
  try{
   const value=localStorage.getItem(key);
   return value===null?fallback:JSON.parse(value);
  }catch(e){return fallback;}
 },
 set(key,value){
  try{localStorage.setItem(key,JSON.stringify(value));}catch(e){}
 }
};

let userName=store.get("mobile_name","Guest");
let appPin=store.get("mobile_pin","");
let isGuest=false;
let calcExpression="";
let secretNumber=0,guessCount=0,guessFinished=false;
let typingStarted=false,typingStartTime=0,typingTimer=null;

let flappyTimer=null;
let flappyRunning=false;
let flappyBird=null;
let flappyPipes=[];
let flappyScore=0;

let snakeFrame=null;
let snakeRunning=false;
let snakeBody=[];
let snakeFood=null;
let snakeDir={x:1,y:0};
let snakeNextDir={x:1,y:0};
let snakePoints=0;
let snakeLastTime=0;
let snakeAccumulator=0;
let snakeStep=115;
let snakeTouchStart=null;


// CLOCK
function updateClock(){
 const now=new Date();
 const h=now.getHours(),m=now.getMinutes(),s=now.getSeconds();

 const hour=(h%12)*30+m*.5;
 const minute=m*6+s*.1;
 const second=s*6;

 if($("hour-hand"))
  $("hour-hand").style.transform=`translateX(-50%) rotate(${hour}deg)`;

 if($("minute-hand"))
  $("minute-hand").style.transform=`translateX(-50%) rotate(${minute}deg)`;

 if($("second-hand"))
  $("second-hand").style.transform=`translateX(-50%) rotate(${second}deg)`;

 const time=now.toLocaleTimeString([],{
  hour:"2-digit",minute:"2-digit",second:"2-digit"
 });

 if($("digital-time"))$("digital-time").textContent=time;

 if($("top-time"))
  $("top-time").textContent=now.toLocaleTimeString([],{
   hour:"2-digit",minute:"2-digit"
  });

 if($("digital-date"))
  $("digital-date").textContent=now.toLocaleDateString([],{
   weekday:"long",day:"numeric",month:"long",year:"numeric"
  });
}

updateClock();
setInterval(updateClock,1000);


// PAGE NAVIGATION
const pages=[
 "login-page","home-page","calculator-page","password-page",
 "notes-page","games-page","guess-page","typing-page",
 "flappy-page","snake-page","settings-page","about-page","pin-page"
];

function stopFlappy(){
 if(flappyTimer){
  clearInterval(flappyTimer);
  flappyTimer=null;
 }
 flappyRunning=false;
}

function stopSnake(){
 if(snakeFrame!==null){
  cancelAnimationFrame(snakeFrame);
  snakeFrame=null;
 }
 snakeRunning=false;
}

function stopTyping(){
 if(typingTimer){
  clearInterval(typingTimer);
  typingTimer=null;
 }
}

function showPage(id){
 stopFlappy();
 stopSnake();
 stopTyping();

 pages.forEach(page=>{
  const el=$(page);
  if(el)el.classList.toggle("hidden",page!==id);
 });

 if(id==="notes-page")renderNotes();

 if(id==="settings-page"){
  $("setting-name").value=store.get("mobile_name","Guest");
  $("setting-pin").value="";
 }

 if(id==="flappy-page")drawFlappy();
 if(id==="snake-page")drawSnake();
}

function openPage(id){showPage(id);}

function goHome(){
 if(appPin&&!isGuest){
  showPage("pin-page");
  return;
 }
 showPage("home-page");
}


// LOGIN
function login(){
 isGuest=false;
 if(appPin){
  showPage("pin-page");
  return;
 }
 enterHome();
}

function guestLogin(){
 isGuest=true;
 userName="Guest";
 enterHome();
}

function enterHome(){
 $("welcome-name").textContent="Hello, "+userName+"!";
 showPage("home-page");
}

function unlockApp(){
 const entered=$("pin-entry").value;

 if(entered===appPin){
  $("pin-entry").value="";
  $("pin-message").textContent="";
  enterHome();
 }else{
  $("pin-message").textContent="Incorrect PIN. Try again.";
 }
}


// CALCULATOR
function calcUpdate(){
 $("calc-display").textContent=calcExpression||"0";
}

function calcInput(value){
 if(calcExpression.length>35)return;
 calcExpression+=value;
 calcUpdate();
}

function calcClear(){
 calcExpression="";
 calcUpdate();
}

function calcBack(){
 calcExpression=calcExpression.slice(0,-1);
 calcUpdate();
}

function calcResult(){
 try{
  if(!calcExpression||!/^[0-9+\-*/%.() ]+$/.test(calcExpression))
   throw Error();

  const result=Function('"use strict";return ('+calcExpression+')')();

  if(!Number.isFinite(result))throw Error();

  calcExpression=String(Number(result.toFixed(10)));
 }catch(e){
  calcExpression="Error";
 }

 calcUpdate();
}


// PASSWORD GENERATOR
function generatePassword(){
 let length=parseInt($("pass-length").value,10);

 if(!Number.isFinite(length))length=16;

 length=Math.max(6,Math.min(40,length));

 const chars="ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz23456789!@#$%&*?";
 let result="";

 const random=new Uint32Array(length);

 if(window.crypto&&crypto.getRandomValues)
  crypto.getRandomValues(random);
 else
  for(let i=0;i<length;i++)
   random[i]=Math.floor(Math.random()*100000);

 for(let i=0;i<length;i++)
  result+=chars[random[i]%chars.length];

 $("password-output").textContent=result;
}

async function copyPassword(){
 const value=$("password-output").textContent;

 if(!value||value==="Your password appears here.")return;

 try{
  await navigator.clipboard.writeText(value);
  $("password-output").textContent=value+"  ✓ Copied";
 }catch(e){
  $("password-output").textContent=value+"  (Select to copy)";
 }
}


// NOTES
function getNotes(){
 return store.get("mobile_notes",[]);
}

function saveNote(){
 const title=$("note-title").value.trim();
 const body=$("note-body").value.trim();

 if(!title&&!body)return;

 const notes=getNotes();

 notes.unshift({
  id:Date.now(),
  title:title||"Untitled",
  body
 });

 store.set("mobile_notes",notes);

 $("note-title").value="";
 $("note-body").value="";

 renderNotes();
}

function renderNotes(){
 const notes=getNotes();

 $("notes-list").innerHTML="";

 if(!notes.length){
  $("notes-list").innerHTML=
   '<p class="small-note">No notes yet. Create your first note.</p>';
  return;
 }

 notes.forEach(note=>{
  const card=document.createElement("div");
  card.className="card";
  card.style.marginBottom="10px";

  const heading=document.createElement("h3");
  heading.textContent=note.title;

  const content=document.createElement("p");
  content.textContent=note.body;

  const remove=document.createElement("button");
  remove.className="secondary";
  remove.textContent="DELETE";

  remove.onclick=()=>{
   store.set(
    "mobile_notes",
    getNotes().filter(n=>n.id!==note.id)
   );
   renderNotes();
  };

  card.append(heading,content,remove);
  $("notes-list").appendChild(card);
 });
}


// SETTINGS
function saveSettings(){
 const name=$("setting-name").value.trim()||"Guest";
 const pin=$("setting-pin").value.trim();

 if(pin&&!/^\d{4,8}$/.test(pin)){
  alert("PIN must contain 4 to 8 digits.");
  return;
 }

 userName=name;
 appPin=pin;

 store.set("mobile_name",name);
 store.set("mobile_pin",pin);

 $("welcome-name").textContent="Hello, "+userName+"!";

 alert("Settings saved successfully.");
 goHome();
}


// NUMBER GUESSING GAME
function resetGuess(){
 secretNumber=Math.floor(Math.random()*100)+1;
 guessCount=0;
 guessFinished=false;

 $("guess-input").value="";
 $("guess-message").textContent=
  "10 chances remaining. Guess from 1 to 100.";
}

function makeGuess(){
 if(guessFinished)return;

 const guess=Number($("guess-input").value);

 if(!Number.isInteger(guess)||guess<1||guess>100){
  $("guess-message").textContent="Enter a number from 1 to 100.";
  return;
 }

 guessCount++;

 const remaining=10-guessCount;

 if(guess===secretNumber){
  $("guess-message").textContent=
   "🎉 Correct! You guessed it in "+guessCount+" attempts.";
  guessFinished=true;
 }else if(guessCount>=10){
  $("guess-message").textContent=
   "Game over! The number was "+secretNumber+".";
  guessFinished=true;
 }else{
  $("guess-message").textContent=
   (guess<secretNumber?"Too low! Try higher.":"Too high! Try lower.")+
   " "+remaining+" chances left.";
 }

 $("guess-input").value="";
}


// TYPING SPEED
const typingText="Small steps every day create big progress.";

function startTyping(){
 stopTyping();

 typingStarted=false;
 typingStartTime=0;

 $("typing-input").value="";
 $("typing-result").textContent="Start typing the sentence above.";

 $("typing-input").focus();

 $("typing-input").oninput=()=>{
  const value=$("typing-input").value;

  if(!typingStarted&&value.length>0){
   typingStarted=true;
   typingStartTime=Date.now();

   typingTimer=setInterval(()=>{
    const elapsed=Math.floor((Date.now()-typingStartTime)/1000);
    $("typing-result").textContent="Time: "+elapsed+" seconds";
   },500);
  }

  if(value===typingText){
   const elapsed=Math.max(1,(Date.now()-typingStartTime)/1000);
   const words=typingText.split(/\s+/).length;
   const wpm=Math.round(words/(elapsed/60));

   stopTyping();

   $("typing-result").textContent=
    "Completed! "+wpm+" words per minute · "+
    Math.round(elapsed)+" seconds.";
  }
 };
}


// FLAPPY BIRD
const fc=$("flappy-canvas");
const fx=fc.getContext("2d");

function drawFlappy(){
 const w=fc.width,h=fc.height;

 const sky=fx.createLinearGradient(0,0,0,h);
 sky.addColorStop(0,"#51c9f5");
 sky.addColorStop(1,"#d3f7ff");

 fx.fillStyle=sky;
 fx.fillRect(0,0,w,h);

 // Clouds
 fx.fillStyle="#ffffff99";

 [[55,65,20],[175,105,27],[285,55,23]].forEach(([x,y,r])=>{
  fx.beginPath();
  fx.arc(x,y,r,0,Math.PI*2);
  fx.arc(x+r,y-8,r*.8,0,Math.PI*2);
  fx.arc(x+r*2,y,r,0,Math.PI*2);
  fx.fill();
 });

 // Ground
 fx.fillStyle="#75d68b";
 fx.fillRect(0,h-35,w,35);

 fx.fillStyle="#3eae74";
 fx.fillRect(0,h-35,w,7);

 // Bird
 if(flappyBird){
  const x=flappyBird.x;
  const y=flappyBird.y;

  fx.save();

  fx.translate(x,y);
  fx.rotate(Math.max(-.45,Math.min(.65,flappyBird.velocity*.055)));

  // Body
  fx.fillStyle="#ffd447";
  fx.beginPath();
  fx.ellipse(0,0,16,12,0,0,Math.PI*2);
  fx.fill();

  // Wing
  const wing=Math.sin(Date.now()/65)*4;

  fx.fillStyle="#f3a928";
  fx.beginPath();
  fx.ellipse(-5,wing,9,5,-.3,0,Math.PI*2);
  fx.fill();

  // Tail
  fx.fillStyle="#ed9c30";
  fx.beginPath();
  fx.moveTo(-13,-2);
  fx.lineTo(-21,-8);
  fx.lineTo(-19,2);
  fx.closePath();
  fx.fill();

  // Eye
  fx.fillStyle="#ffffff";
  fx.beginPath();
  fx.arc(7,-6,5,0,Math.PI*2);
  fx.fill();

  fx.fillStyle="#172c42";
  fx.beginPath();
  fx.arc(9,-6,2.2,0,Math.PI*2);
  fx.fill();

  // Beak
  fx.fillStyle="#f07836";
  fx.beginPath();
  fx.moveTo(14,-1);
  fx.lineTo(25,3);
  fx.lineTo(14,6);
  fx.closePath();
  fx.fill();

  fx.restore();
 }

 // Pipes
 flappyPipes.forEach(p=>{
  const gradient=fx.createLinearGradient(p.x,0,p.x+48,0);

  gradient.addColorStop(0,"#168b77");
  gradient.addColorStop(.5,"#43d5a1");
  gradient.addColorStop(1,"#137b70");

  fx.fillStyle=gradient;

  fx.fillRect(p.x,0,48,p.top);
  fx.fillRect(p.x,p.top-12,48,12);

  fx.fillRect(p.x,p.bottom,48,h-p.bottom-35);
  fx.fillRect(p.x,p.bottom,48,12);
 });

 if(!flappyRunning){
  fx.fillStyle="#174b61";
  fx.textAlign="center";
  fx.font="bold 19px Arial";
  fx.fillText("Tap PLAY to start",w/2,h/2);
 }
}

function startFlappy(){
 stopFlappy();

 flappyBird={
  x:80,
  y:200,
  velocity:0
 };

 flappyPipes=[];
 flappyScore=0;

 $("flappy-score").textContent="Score: 0";

 flappyRunning=true;

 let frame=0;

 flappyTimer=setInterval(()=>{
  if(!flappyRunning)return;

  frame++;

  // Harder gravity
  flappyBird.velocity+=.45;
  flappyBird.y+=flappyBird.velocity;

  // More frequent pipes and smaller gaps
  if(frame%78===0){
   const top=65+Math.random()*145;

   flappyPipes.push({
    x:fc.width,
    top,
    bottom:top+105,
    passed:false
   });
  }

  flappyPipes.forEach(p=>{
   p.x-=3.4;

   if(!p.passed&&p.x+48<flappyBird.x){
    p.passed=true;
    flappyScore++;
    $("flappy-score").textContent="Score: "+flappyScore;
   }

   const overlaps=
    flappyBird.x+11>p.x&&
    flappyBird.x-11<p.x+48;

   const hitsPipe=
    flappyBird.y-11<p.top||
    flappyBird.y+11>p.bottom;

   if(overlaps&&hitsPipe)endFlappy();
  });

  flappyPipes=flappyPipes.filter(p=>p.x>-55);

  if(flappyBird.y>fc.height-48||flappyBird.y<10)
   endFlappy();

  drawFlappy();

 },25);
}

function flap(){
 if(!flappyRunning)return;
 flappyBird.velocity=-6.8;
}

function endFlappy(){
 if(!flappyRunning)return;

 stopFlappy();
 drawFlappy();

 $("flappy-score").textContent=
  "Game over! Score: "+flappyScore;
}

fc.addEventListener("pointerdown",flap);


// SNAKE — SMOOTH ANIMATION
const sc=$("snake-canvas");
const sx=sc.getContext("2d");

const cell=20;
const gridSize=14;

function newSnakeFood(){
 let point;

 do{
  point={
   x:Math.floor(Math.random()*gridSize),
   y:Math.floor(Math.random()*gridSize)
  };
 }while(
  snakeBody.some(p=>p.x===point.x&&p.y===point.y)
 );

 return point;
}

function drawSnake(){
 const w=sc.width;
 const h=sc.height;

 const bg=sx.createLinearGradient(0,0,w,h);

 bg.addColorStop(0,"#092b25");
 bg.addColorStop(1,"#174b38");

 sx.fillStyle=bg;
 sx.fillRect(0,0,w,h);

 // Grid
 sx.strokeStyle="#ffffff12";
 sx.lineWidth=1;

 for(let i=0;i<=gridSize;i++){
  sx.beginPath();
  sx.moveTo(i*cell,0);
  sx.lineTo(i*cell,h);
  sx.stroke();

  sx.beginPath();
  sx.moveTo(0,i*cell);
  sx.lineTo(w,i*cell);
  sx.stroke();
 }

 // Food
 if(snakeFood){
  sx.shadowColor="#ffb347";
  sx.shadowBlur=16;
  sx.fillStyle="#ffb347";

  sx.beginPath();
  sx.arc(
   snakeFood.x*cell+10,
   snakeFood.y*cell+10,
   7,0,Math.PI*2
  );
  sx.fill();

  sx.shadowBlur=0;
 }

 // Snake
 snakeBody.forEach((p,i)=>{
  sx.fillStyle=i===0?"#b5ff9c":"#43d99b";

  sx.beginPath();
  sx.roundRect(
   p.x*cell+2,
   p.y*cell+2,
   cell-4,
   cell-4,
   6
  );
  sx.fill();

  if(i===0){
   sx.fillStyle="#173c2a";

   sx.beginPath();
   sx.arc(p.x*cell+7,p.y*cell+8,1.8,0,Math.PI*2);
   sx.arc(p.x*cell+13,p.y*cell+8,1.8,0,Math.PI*2);
   sx.fill();
  }
 });

 if(!snakeRunning){
  sx.fillStyle="#ffffff";
  sx.textAlign="center";
  sx.font="bold 16px Arial";
  sx.fillText("Press PLAY to start",w/2,h/2);
 }
}

function stopSnake(){
 if(snakeFrame!==null){
  cancelAnimationFrame(snakeFrame);
  snakeFrame=null;
 }

 snakeRunning=false;
}

function snakeMove(){
 snakeDir={...snakeNextDir};

 const head={
  x:snakeBody[0].x+snakeDir.x,
  y:snakeBody[0].y+snakeDir.y
 };

 const eating=
  head.x===snakeFood.x&&
  head.y===snakeFood.y;

 const bodyToCheck=eating
  ?snakeBody
  :snakeBody.slice(0,-1);

 if(
  head.x<0||
  head.y<0||
  head.x>=gridSize||
  head.y>=gridSize||
  bodyToCheck.some(p=>p.x===head.x&&p.y===head.y)
 ){
  stopSnake();

  $("snake-score").textContent=
   "Game over! Score: "+snakePoints;

  drawSnake();
  return;
 }

 snakeBody.unshift(head);

 if(eating){
  snakePoints++;
  snakeFood=newSnakeFood();

  $("snake-score").textContent="Score: "+snakePoints;

  snakeStep=Math.max(65,115-snakePoints*3);
 }else{
  snakeBody.pop();
 }

 drawSnake();
}

function snakeAnimation(timestamp){
 if(!snakeRunning)return;

 if(!snakeLastTime)snakeLastTime=timestamp;

 const delta=Math.min(timestamp-snakeLastTime,50);

 snakeLastTime=timestamp;
 snakeAccumulator+=delta;

 while(snakeAccumulator>=snakeStep&&snakeRunning){
  snakeAccumulator-=snakeStep;
  snakeMove();
 }

 if(snakeRunning){
  snakeFrame=requestAnimationFrame(snakeAnimation);
 }
}

function startSnake(){
 stopSnake();

 snakeBody=[
  {x:5,y:7},
  {x:4,y:7},
  {x:3,y:7}
 ];

 snakeDir={x:1,y:0};
 snakeNextDir={x:1,y:0};

 snakeFood=newSnakeFood();
 snakePoints=0;

 snakeStep=115;
 snakeAccumulator=0;
 snakeLastTime=0;

 snakeRunning=true;

 $("snake-score").textContent="Score: 0";

 drawSnake();

 snakeFrame=requestAnimationFrame(snakeAnimation);
}

function snakeDirection(x,y){
 if(!snakeRunning)return;

 if(x===-snakeDir.x&&y===-snakeDir.y)return;

 snakeNextDir={x,y};
}


// SNAKE TOUCH CONTROLS
sc.addEventListener("touchstart",e=>{
 const t=e.touches[0];

 snakeTouchStart={
  x:t.clientX,
  y:t.clientY
 };
},{passive:true});

sc.addEventListener("touchmove",e=>{
 if(snakeTouchStart)e.preventDefault();
},{passive:false});

sc.addEventListener("touchend",e=>{
 if(!snakeTouchStart)return;

 const t=e.changedTouches[0];

 const dx=t.clientX-snakeTouchStart.x;
 const dy=t.clientY-snakeTouchStart.y;

 if(Math.max(Math.abs(dx),Math.abs(dy))>20){
  if(Math.abs(dx)>Math.abs(dy)){
   snakeDirection(dx>0?1:-1,0);
  }else{
   snakeDirection(0,dy>0?1:-1);
  }
 }

 snakeTouchStart=null;
},{passive:true});


// KEYBOARD CONTROLS
document.addEventListener("keydown",e=>{
 if(!$("snake-page").classList.contains("hidden")){
  if(e.key==="ArrowUp")snakeDirection(0,-1);
  if(e.key==="ArrowDown")snakeDirection(0,1);
  if(e.key==="ArrowLeft")snakeDirection(-1,0);
  if(e.key==="ArrowRight")snakeDirection(1,0);
 }
});


// INITIALIZE
function initializeApp(){
 resetGuess();
 drawFlappy();
 drawSnake();
 renderNotes();
 showPage("login-page");
}

initializeApp();

</script>
</body>
</html>
"""

components.html(APP, height=950, scrolling=True)
