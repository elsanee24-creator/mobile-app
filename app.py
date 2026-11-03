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
    <button class="row-tile" onclick="logout()"><span class="emoji">🚪</span><b>Logout</b><span style="margin-left:auto">›</span></button>
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
<script>
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
    try { localStorage.setItem(key, JSON.stringify(value)); }
    catch (e) {}
  }
};

let userName = store.get("mobile_name", "Guest");
let appPin = store.get("mobile_pin", "");
let isGuest = false;

let calcExpression = "";
let secretNumber = 0;
let guessCount = 0;
let guessFinished = false;

let typingTimer = null;
let typingStartTime = 0;
let typingStarted = false;
let typingDuration = 60;
let typingParagraph = "";

let flappyTimer = null;
let flappyRunning = false;
let flappyBird = null;
let flappyPipes = [];
let flappyScore = 0;
let flappyLastTime = 0;

let snakeFrame = null;
let snakeRunning = false;
let snakeBody = [];
let snakeFood = null;
let snakeDir = {x:1,y:0};
let snakeNextDir = {x:1,y:0};
let snakePoints = 0;
let snakeLastTime = 0;
let snakeAccumulator = 0;
let snakeStep = 115;
let snakeTouchStart = null;

let raceFrame = null;
let raceRunning = false;
let raceLastTime = 0;
let raceElapsed = 0;
let raceScore = 0;
let racePlayerLane = 1;
let racePlayerX = 0;
let raceTraffic = [];
let raceSpawnTimer = 0;
let raceRoadOffset = 0;
let raceTouchStart = null;

const typingParagraphs = [
  "Success comes from small efforts repeated every single day. Stay focused, keep learning, and never stop improving.",
  "Technology has changed the way people communicate, learn, and solve problems. It helps us connect with the world.",
  "A good habit can make a big difference in life. Practice regularly and give yourself time to improve.",
  "Learning something new requires patience and consistency. Every mistake is an opportunity to understand something better.",
  "The future belongs to people who keep learning and adapting. Work hard, stay curious, and believe in your progress.",
  "Reading improves knowledge, vocabulary, and imagination. Even a few minutes of reading every day can be useful.",
  "Time is valuable, so use it wisely. Set clear goals and take small steps towards achieving them.",
  "Computers are useful machines that help people perform many tasks. They are used in education, business, science, and communication."
];

/* CLOCK */
function updateClock() {
  const now = new Date();
  const time = now.toLocaleTimeString([], {
    hour: "2-digit",
    minute: "2-digit",
    second: "2-digit"
  });
  const date = now.toLocaleDateString([], {
    weekday: "short",
    day: "numeric",
    month: "short",
    year: "numeric"
  });

  if ($("clock-time")) $("clock-time").textContent = time;
  if ($("clock-date")) $("clock-date").textContent = date;

  const seconds = now.getSeconds();
  const minutes = now.getMinutes();
  const hours = now.getHours() % 12;

  const secondHand = $("second-hand");
  const minuteHand = $("minute-hand");
  const hourHand = $("hour-hand");

  if (secondHand) secondHand.style.transform =
    `rotate(${seconds * 6}deg)`;
  if (minuteHand) minuteHand.style.transform =
    `rotate(${minutes * 6 + seconds * 0.1}deg)`;
  if (hourHand) hourHand.style.transform =
    `rotate(${hours * 30 + minutes * 0.5}deg)`;
}

updateClock();
setInterval(updateClock, 1000);

/* NAVIGATION */
const pages = [
  "login-page",
  "home-page",
  "calculator-page",
  "password-page",
  "notes-page",
  "settings-page",
  "about-page",
  "games-page",
  "guess-page",
  "typing-page",
  "flappy-page",
  "snake-page",
  "pin-page",
  "racing-page"
];

function stopTyping() {
  if (typingTimer) clearInterval(typingTimer);
  typingTimer = null;
  typingStarted = false;
}

function stopFlappy() {
  flappyRunning = false;
  if (flappyTimer) cancelAnimationFrame(flappyTimer);
  flappyTimer = null;
}

function stopSnake() {
  snakeRunning = false;
  if (snakeFrame) cancelAnimationFrame(snakeFrame);
  snakeFrame = null;
}

function stopRacing() {
  raceRunning = false;
  if (raceFrame) cancelAnimationFrame(raceFrame);
  raceFrame = null;
}

function showPage(pageId) {
  stopTyping();
  stopFlappy();
  stopSnake();
  stopRacing();

  pages.forEach(id => {
    const page = $(id);
    if (page) page.classList.toggle("hidden", id !== pageId);
  });

  if (pageId === "notes-page") renderNotes();
  if (pageId === "settings-page") loadSettings();
  if (pageId === "guess-page") resetGuess();
  if (pageId === "typing-page") prepareTyping();
  if (pageId === "flappy-page") drawFlappy();
  if (pageId === "snake-page") drawSnake();
  if (pageId === "racing-page") drawRacing();

  window.scrollTo({top:0, behavior:"smooth"});
}

function openPage(pageId) {
  showPage(pageId);
}

function enterHome() {
  if ($("welcome-name")) {
    $("welcome-name").textContent = isGuest ? "Guest" : userName;
  }
  showPage("home-page");
}

function login() {
  if (appPin) {
    showPage("pin-page");
    if ($("pin-entry")) $("pin-entry").focus();
  } else {
    isGuest = false;
    enterHome();
  }
}

function loginAsGuest() {
  isGuest = true;
  enterHome();
}

function unlockApp() {
  const entered = $("pin-entry")?.value || "";
  if (entered === appPin) {
    isGuest = false;
    if ($("pin-entry")) $("pin-entry").value = "";
    if ($("pin-message")) $("pin-message").textContent = "";
    enterHome();
  } else {
    if ($("pin-message")) {
      $("pin-message").textContent = "Incorrect PIN. Try again.";
    }
  }
}

/* LOGOUT BUTTON */
function addLogoutButton() {
  const home = $("home-page");
  if (!home || $("mobile-logout-button")) return;

  const button = document.createElement("button");
  button.id = "mobile-logout-button";
  button.className = "secondary";
  button.textContent = "LOG OUT";
  button.style.cssText =
    "width:100%;margin-top:16px;padding:13px;border-radius:14px;";

  button.onclick = logout;
  home.appendChild(button);
}

function logout() {
  isGuest = false;
  userName = store.get("mobile_name", "Guest");

  stopTyping();
  stopFlappy();
  stopSnake();
  stopRacing();

  if ($("pin-entry")) $("pin-entry").value = "";
  if ($("pin-message")) $("pin-message").textContent = "";

  showPage("login-page");
}

/* CALCULATOR */
function calculatorPress(value) {
  const display = $("calc-display");
  if (!display) return;

  if (value === "AC") {
    calcExpression = "";
  } else if (value === "DEL") {
    calcExpression = calcExpression.slice(0, -1);
  } else if (value === "=") {
    try {
      if (!/^[0-9+\-*/().%\s]+$/.test(calcExpression)) {
        throw Error("Invalid");
      }

      const result = Function('"use strict";return (' +
        calcExpression + ')')();

      if (!Number.isFinite(result)) throw Error("Invalid");
      calcExpression = String(Number(result.toFixed(8)));
    } catch (e) {
      calcExpression = "";
      display.value = "Error";
      return;
    }
  } else {
    calcExpression += value;
  }

  display.value = calcExpression;
}

/* PASSWORD GENERATOR */
function generatePassword() {
  const lengthInput = $("password-length");
  const output = $("password-result");
  if (!output) return;

  let length = Number(lengthInput?.value || 12);
  length = Math.max(4, Math.min(40, length));

  const chars =
    "ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz23456789!@#$%&*";

  let result = "";
  const randomValues = new Uint32Array(length);

  if (window.crypto?.getRandomValues) {
    crypto.getRandomValues(randomValues);
    for (let i = 0; i < length; i++) {
      result += chars[randomValues[i] % chars.length];
    }
  } else {
    for (let i = 0; i < length; i++) {
      result += chars[Math.floor(Math.random() * chars.length)];
    }
  }

  output.value = result;
}

function copyPassword() {
  const output = $("password-result");
  if (!output?.value) return;

  navigator.clipboard?.writeText(output.value)
    .then(() => alert("Password copied!"))
    .catch(() => {
      output.select();
      document.execCommand("copy");
      alert("Password copied!");
    });
}

/* NOTES */
function renderNotes() {
  const list = $("notes-list");
  if (!list) return;

  list.innerHTML = "";
  const notes = store.get("mobile_notes", []);

  if (!notes.length) {
    list.innerHTML =
      '<p style="opacity:.65;text-align:center">No notes yet.</p>';
    return;
  }

  notes.forEach((note, index) => {
    const card = document.createElement("div");
    card.className = "card";
    card.style.marginBottom = "10px";

    const content = document.createElement("p");
    content.textContent = note;
    content.style.whiteSpace = "pre-wrap";

    const remove = document.createElement("button");
    remove.className = "secondary";
    remove.textContent = "DELETE";
    remove.onclick = () => {
      const updated = store.get("mobile_notes", []);
      updated.splice(index, 1);
      store.set("mobile_notes", updated);
      renderNotes();
    };

    card.appendChild(content);
    card.appendChild(remove);
    list.appendChild(card);
  });
}

function addNote() {
  const input = $("note-input");
  if (!input || !input.value.trim()) return;

  const notes = store.get("mobile_notes", []);
  notes.unshift(input.value.trim());
  store.set("mobile_notes", notes);

  input.value = "";
  renderNotes();
}

/* SETTINGS */
function loadSettings() {
  if ($("setting-name")) {
    $("setting-name").value = store.get("mobile_name", "Guest");
  }
  if ($("setting-pin")) {
    $("setting-pin").value = store.get("mobile_pin", "");
  }
}

function saveSettings() {
  const name = $("setting-name")?.value.trim() || "Guest";
  const pin = $("setting-pin")?.value.trim() || "";

  if (pin && !/^\d{4,8}$/.test(pin)) {
    alert("PIN must contain 4 to 8 digits.");
    return;
  }

  userName = name;
  appPin = pin;

  store.set("mobile_name", userName);
  store.set("mobile_pin", appPin);

  alert("Settings saved successfully!");
  enterHome();
}

/* NUMBER GUESSING GAME */
function resetGuess() {
  secretNumber = Math.floor(Math.random() * 100) + 1;
  guessCount = 0;
  guessFinished = false;

  if ($("guess-result")) {
    $("guess-result").textContent =
      "Guess a number between 1 and 100.";
  }
  if ($("guess-input")) $("guess-input").value = "";
  if ($("guess-count")) $("guess-count").textContent = "Chances: 10";
}

function makeGuess() {
  if (guessFinished) return;

  const input = $("guess-input");
  const result = $("guess-result");
  if (!input || !result) return;

  const guess = Number(input.value);

  if (!Number.isInteger(guess) || guess < 1 || guess > 100) {
    result.textContent = "Enter a number from 1 to 100.";
    return;
  }

  guessCount++;
  const remaining = 10 - guessCount;

  if (guess === secretNumber) {
    result.textContent =
      "Correct! You guessed the number in " + guessCount + " tries.";
    guessFinished = true;
  } else if (remaining <= 0) {
    result.textContent =
      "Game over! The number was " + secretNumber + ".";
    guessFinished = true;
  } else {
    result.textContent = guess < secretNumber
      ? "Too low! Try a higher number."
      : "Too high! Try a lower number.";
  }

  if ($("guess-count")) {
    $("guess-count").textContent =
      guessFinished ? "Game finished" : "Chances: " + remaining;
  }

  input.value = "";
}

/* TYPING SPEED GAME */
function prepareTyping() {
  stopTyping();

  const sentence = $("typing-sentence");
  const input = $("typing-input");
  const result = $("typing-result");

  if (sentence) sentence.textContent =
    "Press START / RESET to begin a new 60-second test.";
  if (input) {
    input.value = "";
    input.disabled = true;
  }
  if (result) result.textContent = "Timer: 60 seconds";
}

function startTyping() {
  stopTyping();

  const sentence = $("typing-sentence");
  const input = $("typing-input");
  const result = $("typing-result");
  if (!sentence || !input || !result) return;

  let choices = typingParagraphs.filter(p => p !== typingParagraph);
  if (!choices.length) choices = typingParagraphs;

  typingParagraph =
    choices[Math.floor(Math.random() * choices.length)];

  sentence.textContent = typingParagraph;
  input.value = "";
  input.disabled = false;
  input.focus();

  typingStarted = true;
  typingStartTime = Date.now();

  let secondsLeft = 60;
  result.textContent = "Time left: 60 seconds";

  typingTimer = setInterval(() => {
    const elapsed = Math.floor((Date.now() - typingStartTime) / 1000);
    secondsLeft = Math.max(0, 60 - elapsed);

    result.textContent = "Time left: " + secondsLeft + " seconds";

    if (secondsLeft <= 0) {
      finishTyping();
    }
  }, 200);
}

function finishTyping() {
  if (!typingStarted) return;

  const input = $("typing-input");
  const result = $("typing-result");
  if (!input || !result) return;

  typingStarted = false;
  if (typingTimer) clearInterval(typingTimer);
  typingTimer = null;

  const typed = input.value;
  let correct = 0;

  for (let i = 0; i < typed.length; i++) {
    if (typed[i] === typingParagraph[i]) correct++;
  }

  const errors = typed.length - correct;
  const elapsed = Math.min(
    60,
    Math.max(1, (Date.now() - typingStartTime) / 1000)
  );

  const accuracy = typed.length
    ? (correct / typed.length) * 100
    : 0;

  const wpm = (correct / 5) / (elapsed / 60);

  input.disabled = true;

  result.innerHTML =
    "<b>Test finished!</b><br>" +
    "WPM: " + Math.round(wpm) + "<br>" +
    "Accuracy: " + accuracy.toFixed(1) + "%<br>" +
    "Correct characters: " + correct + "<br>" +
    "Errors: " + errors + "<br>" +
    "Time: " + Math.round(elapsed) + " seconds";
}

if ($("typing-input")) {
  $("typing-input").addEventListener("input", () => {
    if (!typingStarted) return;

    if ($("typing-input").value.length >= typingParagraph.length) {
      finishTyping();
    }
  });
}

/* FLAPPY BIRD */
const flappyCanvas = $("flappy-canvas");
const fc = flappyCanvas?.getContext("2d");

function drawFlappy() {
  if (!fc || !flappyCanvas) return;

  fc.clearRect(0, 0, 360, 460);

  const sky = fc.createLinearGradient(0, 0, 0, 460);
  sky.addColorStop(0, "#63c9ff");
  sky.addColorStop(1, "#d6f4ff");
  fc.fillStyle = sky;
  fc.fillRect(0, 0, 360, 460);

  fc.fillStyle = "rgba(255,255,255,.8)";
  [[65,65],[245,105],[145,160]].forEach(([x,y]) => {
    fc.beginPath();
    fc.arc(x,y,20,0,Math.PI*2);
    fc.arc(x+22,y-8,24,0,Math.PI*2);
    fc.arc(x+45,y,18,0,Math.PI*2);
    fc.fill();
  });

  fc.fillStyle = "#65bd53";
  fc.fillRect(0, 425, 360, 35);
  fc.fillStyle = "#d8b66c";
  fc.fillRect(0, 425, 360, 8);

  if (!flappyBird) {
    flappyBird = {x:95,y:210,velocity:0};
    flappyPipes = [];
    flappyScore = 0;
  }

  flappyPipes.forEach(pipe => {
    fc.fillStyle = "#168d37";
    fc.fillRect(pipe.x, 0, 48, pipe.top);
    fc.fillRect(pipe.x-5, pipe.top-18, 58, 18);
    fc.fillRect(pipe.x, pipe.bottom, 48, 425-pipe.bottom);
    fc.fillRect(pipe.x-5, pipe.bottom, 58, 18);
  });

  fc.fillStyle = "#ffd43b";
  fc.beginPath();
  fc.ellipse(flappyBird.x,flappyBird.y,17,13,0,0,Math.PI*2);
  fc.fill();

  fc.fillStyle = "#fff";
  fc.beginPath();
  fc.arc(flappyBird.x+6,flappyBird.y-5,5,0,Math.PI*2);
  fc.fill();

  fc.fillStyle = "#111";
  fc.beginPath();
  fc.arc(flappyBird.x+8,flappyBird.y-5,2,0,Math.PI*2);
  fc.fill();

  fc.fillStyle = "#ff812c";
  fc.beginPath();
  fc.moveTo(flappyBird.x+14,flappyBird.y);
  fc.lineTo(flappyBird.x+27,flappyBird.y+4);
  fc.lineTo(flappyBird.x+14,flappyBird.y+8);
  fc.fill();

  fc.fillStyle = "#172b42";
  fc.font = "bold 24px Arial";
  fc.fillText("Score: " + flappyScore, 12, 32);
}

function startFlappy() {
  stopFlappy();
  if (!fc) return;

  flappyBird = {x:95,y:210,velocity:0};
  flappyPipes = [];
  flappyScore = 0;
  flappyLastTime = 0;
  flappyRunning = true;

  function frame(time) {
    if (!flappyRunning) return;

    const delta = flappyLastTime ? Math.min(2,(time-flappyLastTime)/16.67) : 1;
    flappyLastTime = time;

    flappyBird.velocity += 0.42 * delta;
    flappyBird.y += flappyBird.velocity * delta;

    if (!flappyPipes.length ||
        flappyPipes[flappyPipes.length-1].x < 175) {
      const top = 65 + Math.random()*175;
      flappyPipes.push({
        x:360,
        top,
        bottom:top+112,
        scored:false
      });
    }

    flappyPipes.forEach(pipe => {
      pipe.x -= 2.8 * delta;

      if (!pipe.scored && pipe.x+48 < flappyBird.x) {
        pipe.scored = true;
        flappyScore++;
      }

      const hitX =
        flappyBird.x+14 > pipe.x && flappyBird.x-14 < pipe.x+48;
      const hitY =
        flappyBird.y-12 < pipe.top ||
        flappyBird.y+12 > pipe.bottom;

      if (hitX && hitY) endFlappy();
    });

    flappyPipes = flappyPipes.filter(p => p.x > -65);

    if (flappyBird.y > 413 || flappyBird.y < 0) {
      endFlappy();
    }

    drawFlappy();
    if (flappyRunning) {
      flappyTimer = requestAnimationFrame(frame);
    }
  }

  flappyTimer = requestAnimationFrame(frame);
}

function flap() {
  if (!flappyRunning) {
    startFlappy();
    return;
  }
  flappyBird.velocity = -6.8;
}

function endFlappy() {
  if (!flappyRunning) return;
  stopFlappy();
  drawFlappy();
  if ($("flappy-result")) {
    $("flappy-result").textContent =
      "Game over! Score: " + flappyScore;
  }
}

if (flappyCanvas) {
  flappyCanvas.addEventListener("pointerdown", flap);
}

/* SNAKE */
const snakeCanvas = $("snake-canvas");
const sc = snakeCanvas?.getContext("2d");
const snakeCell = 20;
const snakeGrid = 14;

function randomSnakeFood() {
  let food;
  do {
    food = {
      x:Math.floor(Math.random()*snakeGrid),
      y:Math.floor(Math.random()*snakeGrid)
    };
  } while (snakeBody.some(p => p.x===food.x && p.y===food.y));
  return food;
}

function resetSnake() {
  stopSnake();

  snakeBody = [
    {x:5,y:7},
    {x:4,y:7},
    {x:3,y:7}
  ];

  snakeDir = {x:1,y:0};
  snakeNextDir = {x:1,y:0};
  snakePoints = 0;
  snakeStep = 115;
  snakeAccumulator = 0;
  snakeLastTime = 0;
  snakeFood = randomSnakeFood();

  if ($("snake-result")) $("snake-result").textContent = "Score: 0";
  drawSnake();
}

function drawSnake() {
  if (!sc || !snakeCanvas) return;

  sc.clearRect(0,0,288,288);

  const bg = sc.createLinearGradient(0,0,288,288);
  bg.addColorStop(0,"#03150c");
  bg.addColorStop(1,"#0c321c");
  sc.fillStyle = bg;
  sc.fillRect(0,0,288,288);

  sc.strokeStyle = "rgba(100,255,150,.08)";
  for (let i=0;i<=snakeGrid;i++) {
    sc.beginPath();
    sc.moveTo(i*snakeCell,0);
    sc.lineTo(i*snakeCell,288);
    sc.stroke();

    sc.beginPath();
    sc.moveTo(0,i*snakeCell);
    sc.lineTo(288,i*snakeCell);
    sc.stroke();
  }

  if (snakeFood) {
    sc.fillStyle = "#ff5252";
    sc.beginPath();
    sc.arc(
      snakeFood.x*snakeCell+10,
      snakeFood.y*snakeCell+10,
      7,0,Math.PI*2
    );
    sc.fill();
  }

  snakeBody.forEach((part,index) => {
    sc.fillStyle = index===0 ? "#aaff72" : "#43d878";
    sc.beginPath();
    sc.roundRect(
      part.x*snakeCell+1,
      part.y*snakeCell+1,
      18,18,5
    );
    sc.fill();
  });
}

function snakeDirection(direction) {
  const directions = {
    up:{x:0,y:-1},
    down:{x:0,y:1},
    left:{x:-1,y:0},
    right:{x:1,y:0}
  };

  const next = directions[direction];
  if (!next) return;

  if (next.x === -snakeDir.x && next.y === -snakeDir.y) return;
  snakeNextDir = next;

  if (!snakeRunning) startSnake();
}

function startSnake() {
  if (snakeRunning) return;
  if (!snakeBody.length) resetSnake();

  snakeRunning = true;
  snakeLastTime = 0;
  snakeAccumulator = 0;

  function frame(time) {
    if (!snakeRunning) return;

    if (!snakeLastTime) snakeLastTime = time;
    const delta = Math.min(100,time-snakeLastTime);
    snakeLastTime = time;
    snakeAccumulator += delta;

    if (snakeAccumulator >= snakeStep) {
      snakeAccumulator = 0;
      moveSnake();
    }

    drawSnake();
    if (snakeRunning) snakeFrame = requestAnimationFrame(frame);
  }

  snakeFrame = requestAnimationFrame(frame);
}

function moveSnake() {
  snakeDir = snakeNextDir;

  const head = {
    x:snakeBody[0].x+snakeDir.x,
    y:snakeBody[0].y+snakeDir.y
  };

  if (
    head.x<0 || head.x>=snakeGrid ||
    head.y<0 || head.y>=snakeGrid ||
    snakeBody.some(p => p.x===head.x && p.y===head.y)
  ) {
    stopSnake();
    if ($("snake-result")) {
      $("snake-result").textContent =
        "Game over! Score: " + snakePoints;
    }
    return;
  }

  snakeBody.unshift(head);

  if (head.x===snakeFood.x && head.y===snakeFood.y) {
    snakePoints++;
    snakeStep = Math.max(65,115-snakePoints*3);
    snakeFood = randomSnakeFood();

    if ($("snake-result")) {
      $("snake-result").textContent = "Score: " + snakePoints;
    }
  } else {
    snakeBody.pop();
  }
}

if (snakeCanvas) {
  snakeCanvas.addEventListener("touchstart", e => {
    const touch = e.touches[0];
    snakeTouchStart = {x:touch.clientX,y:touch.clientY};
  },{passive:true});

  snakeCanvas.addEventListener("touchend", e => {
    if (!snakeTouchStart) return;

    const touch = e.changedTouches[0];
    const dx = touch.clientX-snakeTouchStart.x;
    const dy = touch.clientY-snakeTouchStart.y;

    if (Math.abs(dx)>Math.abs(dy)) {
      snakeDirection(dx>0?"right":"left");
    } else {
      snakeDirection(dy>0?"down":"up");
    }

    snakeTouchStart = null;
  },{passive:true});
}

/* RACING GAME — ADDED TO GAMING HUB */
function createRacingGame() {
  if ($("racing-page")) return;

  const main = document.querySelector("main") ||
               document.querySelector(".screen") ||
               document.body;

  const tileGrid = $("games-page")?.querySelector(".tile-grid");

  if (tileGrid) {
    const tile = document.createElement("button");
    tile.className = "tile";
    tile.innerHTML =
      '<span style="font-size:30px">🏎️</span>' +
      '<b>Racing Game</b>';
    tile.onclick = () => openPage("racing-page");
    tileGrid.appendChild(tile);
  }

  const section = document.createElement("section");
  section.id = "racing-page";
  section.className = "hidden";

  section.innerHTML = `
    <div style="padding:12px 0">
      <button class="back" onclick="openPage('games-page')">
        ‹ Games
      </button>
      <h2 style="text-align:center;margin:12px 0">🏎️ Racing Game</h2>

      <div style="display:flex;justify-content:space-between;
        font-weight:bold;margin:10px 4px">
        <span id="race-score">Distance: 0</span>
        <span id="race-level">Level: 1</span>
      </div>

      <div style="width:100%;display:flex;justify-content:center">
        <canvas id="racing-canvas" width="360" height="520"
          style="width:100%;max-width:360px;height:auto;
          border-radius:18px;touch-action:none;
          display:block;background:#17231b;
          box-shadow:0 8px 25px #0005">
        </canvas>
      </div>

      <p id="race-result" style="text-align:center;font-weight:bold">
        Avoid the traffic and survive!
      </p>

      <button class="primary" id="race-start"
        onclick="startRacing()" style="width:100%">
        START RACING
      </button>

      <p style="text-align:center;font-size:13px;opacity:.75">
        Mobile: swipe left or right. Laptop: use ← → or A / D.
        Your car moves forward automatically.
      </p>
    </div>
  `;

  main.appendChild(section);
}

function drawRacing() {
  const canvas = $("racing-canvas");
  const ctx = canvas?.getContext("2d");
  if (!ctx) return;

  const w = 360, h = 520;
  ctx.clearRect(0,0,w,h);

  ctx.fillStyle = "#17632b";
  ctx.fillRect(0,0,w,h);

  // Road
  const roadX = 42;
  const roadW = 276;
  ctx.fillStyle = "#34383d";
  ctx.fillRect(roadX,0,roadW,h);

  // Road edges
  ctx.fillStyle = "#f5f5f5";
  ctx.fillRect(roadX,0,5,h);
  ctx.fillRect(roadX+roadW-5,0,5,h);

  // Roadside bushes
  for (let y=-40;y<h+40;y+=75) {
    const offset = raceRoadOffset % 75;
    [12,330].forEach(x => {
      ctx.fillStyle = "#0b421b";
      ctx.beginPath();
      ctx.arc(x,y+offset,13,0,Math.PI*2);
      ctx.fill();

      ctx.fillStyle = "#269b42";
      ctx.beginPath();
      ctx.arc(x+5,y+offset-5,8,0,Math.PI*2);
      ctx.fill();
    });
  }

  // Four lanes
  const laneW = roadW/4;
  ctx.strokeStyle = "#f5f0a8";
  ctx.lineWidth = 3;
  ctx.setLineDash([24,22]);

  for (let i=1;i<4;i++) {
    const x = roadX+laneW*i;
    ctx.beginPath();
    ctx.moveTo(x,-60+(raceRoadOffset%46));
    ctx.lineTo(x,h);
    ctx.stroke();
  }
  ctx.setLineDash([]);

  // Traffic
  raceTraffic.forEach(car => {
    drawTrafficVehicle(ctx,roadX+laneW*(car.lane+.5),car.y,car.type,car.color);
  });

  // Player car
  drawTrafficVehicle(
    ctx,
    racePlayerX || roadX+laneW*(racePlayerLane+.5),
    425,
    "player",
    "#39e6ff"
  );

  ctx.fillStyle = "#fff";
  ctx.font = "bold 15px Arial";
  ctx.fillText("🏁", 8, 24);
}

function drawTrafficVehicle(ctx,x,y,type,color) {
  if (type === "bike") {
    ctx.fillStyle = "#111";
    ctx.beginPath();
    ctx.arc(x,y+12,7,0,Math.PI*2);
    ctx.arc(x,y+34,7,0,Math.PI*2);
    ctx.fill();

    ctx.fillStyle = color;
    ctx.fillRect(x-5,y+10,10,25);
    ctx.fillStyle = "#fff";
    ctx.fillRect(x-3,y+8,6,5);
    return;
  }

  ctx.fillStyle = "#101317";
  ctx.beginPath();
  ctx.roundRect(x-17,y-29,34,58,8);
  ctx.fill();

  ctx.fillStyle = color;
  ctx.beginPath();
  ctx.roundRect(x-14,y-27,28,54,7);
  ctx.fill();

  ctx.fillStyle = "#bceaff";
  ctx.fillRect(x-10,y-19,20,12);

  ctx.fillStyle = "#ffe98a";
  ctx.fillRect(x-12,y+19,7,5);
  ctx.fillRect(x+5,y+19,7,5);

  ctx.fillStyle = "#171717";
  ctx.fillRect(x-19,y-17,4,12);
  ctx.fillRect(x+15,y-17,4,12);
  ctx.fillRect(x-19,y+12,4,12);
  ctx.fillRect(x+15,y+12,4,12);
}

function startRacing() {
  stopRacing();

  raceRunning = true;
  raceLastTime = 0;
  raceElapsed = 0;
  raceScore = 0;
  racePlayerLane = 1;
  racePlayerX = 42+(276/4)*(racePlayerLane+.5);
  raceTraffic = [];
  raceSpawnTimer = 0;
  raceRoadOffset = 0;

  if ($("race-result")) {
    $("race-result").textContent = "Go! Avoid the traffic!";
  }
  if ($("race-start")) $("race-start").textContent = "RESTART";

  function frame(time) {
    if (!raceRunning) return;

    if (!raceLastTime) raceLastTime = time;
    const dt = Math.min(40,time-raceLastTime)/1000;
    raceLastTime = time;

    raceElapsed += dt;
    raceScore = Math.floor(raceElapsed*10);

    const level = 1+Math.floor(raceElapsed/15);
    const speed = 190+Math.min(180,raceElapsed*5);
    const spawnGap = Math.max(.48,1.15-raceElapsed*.012);

    raceRoadOffset += speed*dt;
    raceSpawnTimer += dt;

    const roadX = 42;
    const laneW = 276/4;

    // Smooth player movement
    const targetX = roadX+laneW*(racePlayerLane+.5);
    racePlayerX += (targetX-racePlayerX)*Math.min(1,dt*12);

    // Spawn traffic
    if (raceSpawnTimer >= spawnGap) {
      raceSpawnTimer = 0;

      const lane = Math.floor(Math.random()*4);
      const type = Math.random()<.27 ? "bike" : "car";
      const colors = ["#ff5151","#ffb52e","#a66bff","#f2f2f2","#42d66b"];

      raceTraffic.push({
        lane,
        y:-55,
        type,
        color:colors[Math.floor(Math.random()*colors.length)]
      });
    }

    raceTraffic.forEach(vehicle => {
      vehicle.y += speed*dt;
    });

    raceTraffic = raceTraffic.filter(vehicle => vehicle.y<580);

    // Collision detection
    const playerLane = Math.round(
      (racePlayerX-roadX)/laneW-.5
    );

    const collision = raceTraffic.some(vehicle => {
      const closeY = vehicle.y>385 && vehicle.y<475;
      const sameLane = vehicle.lane===playerLane;
      return closeY && sameLane;
    });

    if (collision) {
      endRacing();
      return;
    }

    if ($("race-score")) {
      $("race-score").textContent = "Distance: " + raceScore;
    }
    if ($("race-level")) {
      $("race-level").textContent = "Level: " + level;
    }

    drawRacing();
    raceFrame = requestAnimationFrame(frame);
  }

  raceFrame = requestAnimationFrame(frame);
}

function endRacing() {
  stopRacing();
  drawRacing();

  if ($("race-result")) {
    $("race-result").textContent =
      "Crash! Distance: " + raceScore + " — Tap RESTART to play again.";
  }
}

function changeRaceLane(direction) {
  if (!raceRunning) return;

  racePlayerLane = Math.max(
    0,
    Math.min(3,racePlayerLane+direction)
  );
}

document.addEventListener("keydown", e => {
  if (!$("racing-page") ||
      $("racing-page").classList.contains("hidden")) return;

  if (["ArrowLeft","ArrowRight","a","A","d","D"].includes(e.key)) {
    e.preventDefault();
  }

  if (e.key==="ArrowLeft" || e.key==="a" || e.key==="A") {
    changeRaceLane(-1);
  }
  if (e.key==="ArrowRight" || e.key==="d" || e.key==="D") {
    changeRaceLane(1);
  }
});

function setupRaceSwipe() {
  const canvas = $("racing-canvas");
  if (!canvas) return;

  canvas.addEventListener("touchstart", e => {
    const touch = e.touches[0];
    raceTouchStart = {x:touch.clientX,y:touch.clientY};
  },{passive:true});

  canvas.addEventListener("touchend", e => {
    if (!raceTouchStart || !raceRunning) return;

    const touch = e.changedTouches[0];
    const dx = touch.clientX-raceTouchStart.x;

    if (Math.abs(dx)>20) {
      changeRaceLane(dx>0?1:-1);
    }

    raceTouchStart = null;
  },{passive:true});
}

/* INITIAL SETUP */
createRacingGame();
addLogoutButton();
setupRaceSwipe();

resetGuess();
drawFlappy();
resetSnake();
renderNotes();
showPage("login-page");

</script>
</body>
</html>
"""

components.html(APP, height=950, scrolling=True)
