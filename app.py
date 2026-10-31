import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Mobile App",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

APP = r"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
<style>
*{box-sizing:border-box}
html,body{margin:0;width:100%;height:100%;overflow:hidden;font-family:Arial,sans-serif;background:#080d20;color:white}
button,input,textarea{font:inherit}
button{cursor:pointer;border:0;color:white}
#app{height:100dvh;width:100%;max-width:650px;margin:auto;padding:3px 9px calc(12px + env(safe-area-inset-bottom));overflow:hidden;border-radius:42px;background:radial-gradient(ellipse at 15% 10%,#35216c 0,transparent 40%),radial-gradient(ellipse at 90% 80%,#075b77 0,transparent 38%),linear-gradient(145deg,#090e24,#15102e 60%,#071c2b);position:relative;display:flex;flex-direction:column}
.screen{height:100%;min-height:0;width:100%;overflow-y:auto;overflow-x:hidden;overscroll-behavior:contain;-webkit-overflow-scrolling:touch;touch-action:pan-y;border:1px solid #ffffff22;border-radius:30px;padding:15px 15px calc(150px + env(safe-area-inset-bottom));background:#ffffff09;backdrop-filter:blur(18px);box-shadow:0 15px 50px #0006;scrollbar-width:none}
.screen::-webkit-scrollbar{display:none}
.hidden{display:none!important}
h1,h2,h3,p{margin-top:0}
h1{font-size:27px}h2{font-size:22px}.muted{color:#b8c5dc;font-size:13px}
.clock{text-align:center;padding:18px 5px 22px}.clock-icon{font-size:28px}
#time{font-size:39px;font-weight:800;letter-spacing:2px;margin:5px}
#date{color:#c5cde0;font-size:13px}
.input{width:100%;padding:14px;border:1px solid #ffffff2c;border-radius:13px;background:#101a35;color:white;margin:7px 0;outline:none}
.btn{padding:13px 15px;border-radius:13px;background:linear-gradient(110deg,#6553e9,#168eae);font-weight:bold;margin:5px 0;width:100%;box-shadow:0 5px 18px #0003}
.btn.secondary{background:#ffffff14;border:1px solid #ffffff22}.btn.small{width:auto;padding:10px 15px}
.row{display:flex;gap:9px}.row>*{flex:1;min-width:0}
.card{padding:15px;border:1px solid #ffffff20;background:#ffffff0c;border-radius:17px;margin:10px 0}
.home-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.home-tile{min-height:83px;border-radius:17px;padding:13px;background:linear-gradient(135deg,#ffffff1b,#ffffff08);border:1px solid #ffffff25;text-align:left}
.home-tile b{display:block;margin-top:8px}
.hub{grid-column:1/-1;min-height:105px;background:linear-gradient(120deg,#493b9b,#087e91)}
.bigicon{font-size:27px}
.back{background:#ffffff16;padding:9px 13px;border-radius:10px;margin-bottom:12px}
.game-area{border-radius:18px;overflow:hidden;position:relative;border:1px solid #ffffff22}
canvas{display:block;width:100%;height:auto;touch-action:none}
.game-controls{display:flex;justify-content:center;gap:10px;flex-wrap:wrap;margin-top:12px}
.game-controls button{background:#ffffff20;border:1px solid #ffffff25;padding:12px 18px;border-radius:12px}
#guessPage{background:linear-gradient(145deg,#142d52,#14203c)}
#flappyPage{background:linear-gradient(180deg,#48b8ed,#a4e4f6 58%,#398f56);color:#102e45}
#snakePage{background:linear-gradient(145deg,#062e36,#071a27)}
#flappyPage .muted{color:#204c60}
#calcDisplay{width:100%;font-size:30px;text-align:right;padding:17px;border-radius:14px;border:1px solid #ffffff25;background:#111a35;color:white;margin-bottom:10px}
.calc-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.calc-grid button{height:58px;border-radius:14px;background:linear-gradient(145deg,#283d70,#182746);font-size:19px}
.calc-grid button.op{background:linear-gradient(145deg,#7849c7,#42328a)}
.calc-grid button.eq{background:linear-gradient(145deg,#05a6b7,#087b91)}
.calc-grid button.clear{background:#a43c66}
#loading{position:absolute;inset:5px;z-index:20;border-radius:23px;background:#090e24f5;display:flex;flex-direction:column;align-items:center;justify-content:center}
.spinner{width:54px;height:54px;border:4px solid #ffffff25;border-top-color:#25d9ed;border-radius:50%;animation:spin .8s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.bar{height:5px;width:190px;background:#ffffff22;border-radius:8px;margin-top:20px;overflow:hidden}
.bar:after{content:"";display:block;height:100%;width:0;background:#24d9ed;animation:load 2s linear forwards}
@keyframes load{to{width:100%}}
.fingerprint-wrap{display:flex;justify-content:center;align-items:center;margin:12px auto 5px}
.fingerprint-btn{width:66px;height:66px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:linear-gradient(145deg,#253d72,#111e3b);border:1px solid #48d8ee88;box-shadow:0 0 15px #24c9e944,inset 0 0 12px #ffffff12;color:#52dff1;padding:0}
.fingerprint-btn:active{transform:scale(.94);box-shadow:0 0 22px #24c9e9aa}
.fingerprint-btn svg{width:36px;height:36px;stroke:#63e5f5}
@media(max-height:700px){.screen{padding:38px 10px calc(42px + env(safe-area-inset-bottom))}.clock{padding:8px 4px 12px}#time{font-size:32px}.home-tile{min-height:68px}.btn{padding:11px}.fingerprint-btn{width:58px;height:58px}}
@media(max-width:380px){#app{padding:10px 7px calc(20px + env(safe-area-inset-bottom))}.screen{padding:38px 11px calc(76px + env(safe-area-inset-bottom));border-radius:26px}h1{font-size:24px}.clock{padding:9px 4px 12px}#time{font-size:33px}.input{padding:12px}.home-tile{padding:10px}}

/* Notes */
#notesPage{background:radial-gradient(ellipse at 10% 5%,#5944a0 0,transparent 40%),radial-gradient(ellipse at 90% 90%,#075b77 0,transparent 40%),linear-gradient(145deg,#151b3b,#102d43)}
.notes-heading{display:flex;justify-content:space-between;align-items:center;position:sticky;top:-10px;z-index:3;background:#172342ed;padding:5px 0 8px}
.notes-editor{background:#ffffff10;border:1px solid #ffffff25;border-radius:18px;padding:11px;margin:7px 0 12px}
.notes-title{width:100%;padding:11px;border-radius:11px;border:1px solid #ffffff25;background:#101a35;color:white;outline:none;margin:5px 0 8px}
.notes-content{width:100%;min-height:88px;max-height:150px;resize:vertical;padding:11px;border-radius:11px;border:1px solid #ffffff25;background:#101a35;color:white;outline:none}
.notes-list{display:flex;flex-direction:column;gap:9px;padding-bottom:16px}
.note-card{background:linear-gradient(135deg,#ffffff19,#ffffff08);border:1px solid #ffffff25;border-radius:15px;padding:12px;overflow-wrap:anywhere}
.note-card h3{margin:0 0 7px;font-size:17px}
.note-card p{white-space:pre-wrap;color:#d5deef;font-size:13px;margin:0 0 10px;max-height:120px;overflow-y:auto}
.note-meta{font-size:11px;color:#aebbd2;margin-bottom:10px}
.note-actions{display:flex;gap:8px}
.note-actions button{flex:1;min-height:44px;padding:9px;border-radius:10px;background:#ffffff18;border:1px solid #ffffff25;font-weight:bold}
.note-actions .delete-note{background:#b735584d;border:1px solid #ff829c88;color:#fff}
.notes-empty{text-align:center;padding:18px 12px;border:1px dashed #ffffff35;border-radius:15px;color:#b8c5dc}
.notes-message{min-height:17px;color:#8ce8d8;font-size:12px;margin-top:5px}
#notesPage h3{margin-bottom:7px}
#notesPage{padding-bottom:calc(180px + env(safe-area-inset-bottom))}
#settingsPage,#aboutPage{padding-bottom:calc(180px + env(safe-area-inset-bottom))}
@media(max-height:700px){.notes-content{min-height:72px} .notes-editor{padding:9px;margin:5px 0 9px}}

/* Compact Snake game only */
#snakePage{padding:10px}
#snakePage .snake-back{margin-bottom:6px}
#snakePage h2{margin-bottom:5px}
#snakePage .snake-description{margin-bottom:7px}
#snakePage .snake-game-area{width:100%;max-width:250px;margin:0 auto;border-radius:14px;overflow:hidden;border:1px solid #ffffff22}
#snakePage .snake-game-area canvas{width:100%;height:auto}
#snakePage .snake-scores{gap:7px;margin:5px 0}
#snakePage .snake-scores .card{padding:7px 10px;margin:3px 0;text-align:center}
#snakePage .snake-scores h2{margin:3px 0 0;font-size:19px}
#snakePage .snake-start{margin:3px 0;padding:9px}
#snakePage .snake-controls{display:flex;flex-direction:column;align-items:center;gap:5px;margin:5px 0 7px}
#snakePage .snake-controls button{width:43px;height:38px;padding:4px;border-radius:10px;background:#ffffff20;border:1px solid #ffffff35;font-size:18px}
#snakePage .snake-controls .horizontal{display:flex;gap:7px}

/* Final polish: lifted rounded phone frame + iPhone-inspired Dynamic Island */
#app:before{content:"";position:absolute;top:8px;left:50%;transform:translateX(-50%);width:104px;height:27px;border-radius:18px;background:#020306;border:1px solid #252833;z-index:30;box-shadow:0 2px 10px #0008;pointer-events:none}
#app:after{content:"";position:absolute;top:18px;left:calc(50% + 31px);width:7px;height:7px;border-radius:50%;background:#101d35;box-shadow:inset 0 0 3px #42618e;z-index:31;pointer-events:none}
.screen{padding-top:48px;padding-bottom:calc(160px + env(safe-area-inset-bottom));border-radius:34px}
#home .home-grid{padding-bottom:12px}
#settingsPage .card,#aboutPage .card{margin-bottom:12px}
.setting-row{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:12px 0;border-bottom:1px solid #ffffff18}
.setting-row:last-child{border-bottom:0}.setting-row small{display:block;color:#b8c5dc;margin-top:3px}
.toggle{width:48px;height:27px;border-radius:20px;background:#536078;position:relative;flex:none}
.toggle:after{content:"";position:absolute;width:21px;height:21px;left:3px;top:3px;border-radius:50%;background:white;transition:.2s}
.toggle.on{background:#13a9a6}.toggle.on:after{left:24px}
#lockOverlay{position:absolute;inset:5px;z-index:50;border-radius:23px;background:#080d20f5;display:none;align-items:center;justify-content:center;padding:24px}
#lockOverlay.active{display:flex}
.lock-box{width:100%;max-width:330px;text-align:center;padding:22px;border:1px solid #ffffff25;border-radius:20px;background:#ffffff10}
#lockOverlay input{letter-spacing:8px;text-align:center;font-size:22px}
#lockMessage{min-height:20px;color:#ff9ca9;font-size:12px}
body.light-mode #app{background:linear-gradient(145deg,#e8f1ff,#d9f4f2)}
body.light-mode .screen{background:#ffffffd9;color:#17233b;border-color:#ffffff}
body.light-mode .muted,body.light-mode #date{color:#52627d}
body.light-mode .card,body.light-mode .home-tile{background:#ffffff;border-color:#d9e2f1;color:#17233b}
body.light-mode .input,body.light-mode .notes-title,body.light-mode .notes-content{background:#f4f7fc;color:#17233b;border-color:#d5deec}
body.light-mode .notes-heading{background:#eaf0fb}
body.light-mode .back{background:#dce6f5;color:#17233b}
</style>
</head>
<body>
<div id="app">
<div id="loading" class="hidden">
 <div class="spinner"></div><h2 style="margin:20px 0 5px">Loading your app</h2>
 <div class="muted">Please wait...</div><div class="bar"></div>
</div>
<div id="lockOverlay">
 <div class="lock-box"><div style="font-size:38px">🔐</div><h2 id="lockTitle">App Locked</h2><p class="muted">Enter your PIN to continue</p>
 <input id="unlockPin" class="input" type="password" inputmode="numeric" maxlength="4" placeholder="••••">
 <button class="btn" onclick="unlockApp()">Unlock</button><div id="lockMessage"></div>
 </div>
</div>

<section id="login" class="screen">
 <div class="clock"><div class="clock-icon">◷</div><div id="time">00:00:00</div><div id="date">Loading date...</div></div>
 <div style="text-align:center;margin-bottom:18px"><h1>Welcome Back</h1><div class="muted">Your personal mobile space</div></div>
 <input id="username" class="input" placeholder="Username" autocomplete="username">
 <input id="password" class="input" type="password" placeholder="Password" autocomplete="current-password">
 <button class="btn" onclick="loginUser()">LOGIN</button>
 <button class="btn secondary" onclick="enterApp('Guest')">Continue as Guest</button>
 <div class="fingerprint-wrap">
  <button class="fingerprint-btn" onclick="enterApp('Guest')" aria-label="Fingerprint demo">
   <svg viewBox="0 0 48 48" fill="none" stroke-width="2.1" stroke-linecap="round">
    <path d="M24 5C14 5 8 12 8 21"/><path d="M24 10C17 10 12 15 12 22"/>
    <path d="M24 15C19 15 16 18 16 23"/><path d="M24 20C21 20 20 22 20 25"/>
    <path d="M24 5C34 5 40 12 40 21"/><path d="M24 10C31 10 36 15 36 22"/>
    <path d="M24 15C29 15 32 18 32 23"/><path d="M24 20C27 20 28 22 28 25"/>
    <path d="M8 25C8 33 12 39 16 43"/><path d="M14 27C14 34 17 39 20 42"/>
    <path d="M34 27C34 34 31 39 28 42"/><path d="M40 25C40 33 36 39 32 43"/>
    <path d="M24 25C24 33 23 39 22 44"/>
   </svg>
  </button>
 </div>
 <p class="muted" style="text-align:center;margin-top:7px">Fingerprint is a demo shortcut.</p>
</section>

<section id="home" class="screen hidden">
 <div style="display:flex;justify-content:space-between;align-items:center">
  <div><div class="muted" id="homeAppName">WELCOME</div><h1 id="welcomeName">Home</h1></div>
  <button class="back" onclick="goLogin()">↪</button>
 </div>
 <div class="card" style="display:flex;justify-content:space-between;align-items:center">
  <div><div class="muted">TODAY</div><b id="homeDate">Loading...</b></div><div style="font-size:29px">◷</div><b id="homeTime">00:00</b>
 </div>
 <div class="home-grid">
  <button class="home-tile" onclick="showPage('calculator')"><span class="bigicon">🧮</span><b>Calculator</b><span class="muted">Quick calculations</span></button>
  <button class="home-tile" onclick="showPage('passwordPage')"><span class="bigicon">🔐</span><b>Password Generator</b><span class="muted">Create passwords</span></button>
  <button class="home-tile" onclick="openNotes()"><span class="bigicon">📝</span><b>Notes</b><span class="muted">Write your thoughts</span></button>
  <button class="home-tile hub" onclick="showPage('gaming')"><span class="bigicon">🧩</span><b>Gaming Hub</b><span class="muted">Play your favourite games</span></button>
  <button class="home-tile" onclick="showPage('settingsPage')"><span class="bigicon">⚙️</span><b>Settings</b><span class="muted">Personalize your app</span></button>
  <button class="home-tile" onclick="showPage('aboutPage')"><span class="bigicon">ℹ️</span><b>About</b><span class="muted">App information</span></button>
 </div>
 <div class="card"><b>✨ Your Space</b><p class="muted" style="margin:7px 0 0">Choose an activity and enjoy.</p></div>
</section>

<section id="calculator" class="screen hidden">
 <button class="back" onclick="showPage('home')">← Back</button><h2>🧮 Calculator</h2>
 <input id="calcDisplay" value="0" readonly><div class="calc-grid" id="calcButtons"></div>
</section>

<section id="passwordPage" class="screen hidden">
 <button class="back" onclick="showPage('home')">← Back</button><h2>🔐 Password Generator</h2>
 <div class="card">
  <label class="muted">Password length</label><input id="passLength" class="input" type="number" min="6" max="32" value="16">
  <label><input id="passUpper" type="checkbox" checked> Uppercase letters</label><br><br>
  <label><input id="passLower" type="checkbox" checked> Lowercase letters</label><br><br>
  <label><input id="passNumbers" type="checkbox" checked> Numbers</label><br><br>
  <label><input id="passSymbols" type="checkbox" checked> Symbols</label>
  <button class="btn" onclick="generatePassword()">Generate Password</button>
  <input id="passOutput" class="input" readonly placeholder="Your password appears here">
  <button class="btn secondary" onclick="copyPassword()">Copy Password</button><div id="passMessage" class="muted"></div>
 </div>
</section>

<section id="notesPage" class="screen hidden">
 <div class="notes-heading">
  <div><button class="back" onclick="showPage('home')">← Back</button><h2>📝 My Notes</h2></div>
  <div style="font-size:28px">✍️</div>
 </div>
 <div class="notes-editor">
  <h3 id="noteEditorHeading">Create a note</h3>
  <input id="noteTitle" class="notes-title" maxlength="80" placeholder="Note title">
  <textarea id="noteContent" class="notes-content" placeholder="Write your note here..."></textarea>
  <button id="saveNoteButton" class="btn" onclick="saveNote()">Save Note</button>
  <button id="cancelEditButton" class="btn secondary hidden" onclick="cancelNoteEdit()">Cancel Edit</button>
  <div id="notesMessage" class="notes-message"></div>
 </div>
 <h3>📚 Saved Notes</h3><div id="notesList" class="notes-list"></div>
</section>

<section id="settingsPage" class="screen hidden">
 <button class="back" onclick="showPage('home')">← Back</button><h2>⚙️ Settings</h2>
 <div class="card">
  <div class="setting-row"><div><b>Light mode</b><small>Switch the app appearance</small></div><button id="themeToggle" class="toggle" onclick="toggleTheme()" aria-label="Toggle light mode"></button></div>
  <div class="setting-row"><div><b>Haptic feedback</b><small>Vibration on supported phones</small></div><button id="hapticToggle" class="toggle on" onclick="toggleHaptics()" aria-label="Toggle haptic feedback"></button></div>
  <div class="setting-row"><div><b>App display name</b><small id="appNameLabel">Mobile.app</small></div><button class="btn small secondary" onclick="changeAppName()">Change</button></div>
 </div>
 <div class="card"><h3>🔐 App Lock</h3><p class="muted">Set a 4-digit PIN for this app on this device.</p>
  <button class="btn" onclick="setAppPin()">Set / Change PIN</button><button class="btn secondary" onclick="lockNow()">Lock Now</button><button class="btn secondary" onclick="removeAppPin()">Turn Off App Lock</button>
  <p class="muted" style="margin:8px 0 0">Note: This is a basic app-level lock, not device-grade security.</p>
 </div>
 <div class="card"><h3>Data</h3><p class="muted">Clear saved notes and app preferences from this device.</p><button class="btn secondary" style="background:#8e3048" onclick="resetAppData()">Reset App Data</button></div>
</section>

<section id="aboutPage" class="screen hidden">
 <button class="back" onclick="showPage('home')">← Back</button><div style="text-align:center;padding:16px 0"><div style="font-size:54px">📱</div><h1 id="aboutAppName">Mobile.app</h1><div class="muted">Your personal mobile space</div></div>
 <div class="card"><div class="setting-row"><b>Version</b><span class="muted">1.0</span></div><div class="setting-row"><b>Created by</b><span class="muted">Kashan</span></div><div class="setting-row"><b>Includes</b><span class="muted">Tools, Notes & Games</span></div></div>
 <p class="muted" style="text-align:center">Made with care. Thanks for using Mobile.app ✨</p>
</section>

<section id="gaming" class="screen hidden">
 <button class="back" onclick="showPage('home')">← Back</button><h2>🧩 Gaming Hub</h2><p class="muted">Choose your game</p>
 <button class="btn" onclick="startGuess()">🔢 Number Guessing</button>
 <button class="btn" onclick="startFlappy()">🐦 Flappy Bird</button>
 <button class="btn" onclick="startSnake()">🐍 Snake.io</button>
</section>

<section id="guessPage" class="screen hidden">
 <button class="back" onclick="showPage('gaming')">← Back</button><h2>🔢 Number Guessing</h2>
 <div class="card">
  <p>Guess a number between <b>1 and 20</b>.</p><h1 id="attempts">Attempts left: 5</h1>
  <input id="guessInput" class="input" type="number" min="1" max="20" placeholder="Enter your guess">
  <button class="btn" onclick="makeGuess()">Submit Guess</button>
  <div id="guessMessage" style="min-height:25px;margin-top:12px"></div>
  <button id="guessAgain" class="btn secondary hidden" onclick="startGuess()">Play Again</button>
 </div>
</section>

<section id="flappyPage" class="screen hidden">
 <button class="back" onclick="stopFlappy();showPage('gaming')">← Back</button><h2>🐦 Flappy Bird</h2>
 <p class="muted">Tap the game or press SPACE to fly.</p>
 <div class="game-area"><canvas id="flappyCanvas" width="360" height="480"></canvas></div>
 <div class="row"><div class="card"><small>Score</small><h2 id="flappyScore">0</h2></div><div class="card"><small>Best</small><h2 id="flappyBest">0</h2></div></div>
 <button class="btn" onclick="flappyStart()">Start / Restart</button><button class="btn secondary" onclick="flap()">FLAP ↑</button>
</section>

<section id="snakePage" class="screen hidden">
 <button class="back snake-back" onclick="stopSnake();showPage('gaming')">← Back</button>
 <h2>🐍 Snake.io</h2><p class="muted snake-description">Eat apples. Avoid the walls and your tail.</p>
 <div class="snake-controls">
  <button onclick="changeDir(0,-1)">▲</button>
  <div class="horizontal"><button onclick="changeDir(-1,0)">◀</button><button onclick="changeDir(0,1)">▼</button><button onclick="changeDir(1,0)">▶</button></div>
 </div>
 <div class="snake-game-area"><canvas id="snakeCanvas" width="360" height="360"></canvas></div>
 <div class="row snake-scores">
  <div class="card"><small>Score</small><h2 id="snakeScore">0</h2></div><div class="card"><small>Best</small><h2 id="snakeBest">0</h2></div>
 </div>
 <button class="btn snake-start" onclick="startSnakeGame()">Start / Restart</button>
</section>
</div>

<script>
const $=id=>document.getElementById(id);
let currentUser="Guest";
const PIN_KEY="mobileAppPin",THEME_KEY="mobileAppLight",HAPTIC_KEY="mobileAppHaptics",APP_NAME_KEY="mobileAppDisplayName";
let hapticsEnabled=localStorage.getItem(HAPTIC_KEY)!=="false";
function applyPreferences(){
 const light=localStorage.getItem(THEME_KEY)==="true";document.body.classList.toggle("light-mode",light);$("themeToggle").classList.toggle("on",light);
 $("hapticToggle").classList.toggle("on",hapticsEnabled);
 const name=localStorage.getItem(APP_NAME_KEY)||"Mobile.app";$("appNameLabel").textContent=name;$("aboutAppName").textContent=name;$("homeAppName").textContent=name.toUpperCase();
}
function buzz(){if(hapticsEnabled&&navigator.vibrate)navigator.vibrate(18)}
function toggleTheme(){const next=!document.body.classList.contains("light-mode");localStorage.setItem(THEME_KEY,String(next));applyPreferences();buzz()}
function toggleHaptics(){hapticsEnabled=!hapticsEnabled;localStorage.setItem(HAPTIC_KEY,String(hapticsEnabled));applyPreferences();buzz()}
function changeAppName(){const current=localStorage.getItem(APP_NAME_KEY)||"Mobile.app";const value=prompt("Enter app display name:",current);if(value&&value.trim()){localStorage.setItem(APP_NAME_KEY,value.trim().slice(0,24));applyPreferences()}}
function setAppPin(){const pin=prompt("Create a 4-digit PIN:");if(!/^\d{4}$/.test(pin||"")){alert("PIN must contain exactly 4 digits.");return}const again=prompt("Confirm your 4-digit PIN:");if(pin!==again){alert("PINs do not match.");return}localStorage.setItem(PIN_KEY,pin);alert("App Lock is now enabled.")}
function unlockApp(){const pin=$("unlockPin").value;if(pin===localStorage.getItem(PIN_KEY)){$("lockOverlay").classList.remove("active");$("unlockPin").value="";$("lockMessage").textContent=""}else{$("lockMessage").textContent="Incorrect PIN. Try again.";$("unlockPin").value=""}}
function lockNow(){if(!localStorage.getItem(PIN_KEY)){alert("Set a PIN first.");return}$("lockTitle").textContent="App Locked";$("lockOverlay").classList.add("active");$("unlockPin").focus()}
function removeAppPin(){if(!localStorage.getItem(PIN_KEY)){alert("App Lock is not enabled.");return}const pin=prompt("Enter your current PIN to turn off App Lock:");if(pin===localStorage.getItem(PIN_KEY)){localStorage.removeItem(PIN_KEY);alert("App Lock turned off.")}else alert("Incorrect PIN.")}
function resetAppData(){if(!confirm("This will delete saved notes and app preferences. Continue?"))return;["mobileAppNotes",PIN_KEY,THEME_KEY,HAPTIC_KEY,APP_NAME_KEY].forEach(k=>localStorage.removeItem(k));hapticsEnabled=true;applyPreferences();alert("App data has been reset.");showPage("home")}
applyPreferences();
if(localStorage.getItem(PIN_KEY)){$("lockOverlay").classList.add("active")};

function updateClock(){
 const d=new Date();
 $("time").textContent=d.toLocaleTimeString();
 $("date").textContent=d.toLocaleDateString(undefined,{weekday:"long",day:"numeric",month:"long",year:"numeric"});
 $("homeTime").textContent=d.toLocaleTimeString([],{hour:"2-digit",minute:"2-digit"});
 $("homeDate").textContent=d.toLocaleDateString([],{weekday:"short",day:"numeric",month:"short"});
}
updateClock();setInterval(updateClock,1000);

function enterApp(name){
 if(localStorage.getItem(PIN_KEY)&&$("lockOverlay").classList.contains("active")){return}
 currentUser=name;$("loading").classList.remove("hidden");
 setTimeout(()=>{$("loading").classList.add("hidden");$("welcomeName").textContent=name;showPage("home")},2000);
}
function loginUser(){
 let u=$("username").value.trim(),p=$("password").value;
 if(!u||!p){alert("Please enter username and password.");return}
 enterApp(u);
}
function goLogin(){showPage("login")}
function showPage(id){
 document.querySelectorAll(".screen").forEach(s=>s.classList.add("hidden"));
 $(id).classList.remove("hidden");$(id).scrollTop=0;buzz();
}

/* Calculator */
const keys=["C","⌫","%","÷","7","8","9","×","4","5","6","−","1","2","3","+","±","0",".","="];
let calc="0",fresh=false;
function renderCalc(){$("calcDisplay").value=calc}
function calcPress(k){
 if(k==="C"){calc="0";fresh=false}
 else if(k==="⌫"){calc=calc.length>1?calc.slice(0,-1):"0"}
 else if(k==="±"){calc=String(-Number(calc))}
 else if(k==="="){
  try{
   let expr=calc.replace(/×/g,"*").replace(/÷/g,"/").replace(/−/g,"-").replace(/%/g,"/100");
   if(!/^[0-9+*/.() -]+$/.test(expr))throw Error();
   let result=Function('"use strict";return ('+expr+')')();
   calc=Number.isFinite(result)?String(Number(result.toFixed(8))):"Error";fresh=true;
  }catch(e){calc="Error";fresh=true}
 }else{
  if(calc==="Error"||fresh){calc="0";fresh=false}
  if("÷×−+".includes(k)){if("÷×−+".includes(calc.slice(-1)))calc=calc.slice(0,-1);calc+=k}
  else if(k==="."){let part=calc.split(/[+−×÷]/).pop();if(!part.includes("."))calc+="."}
  else calc=calc==="0"?k:calc+k;
 }
 renderCalc();
}
$("calcButtons").innerHTML=keys.map(k=>'<button class="'+(k==="="?"eq":k==="C"?"clear":"÷×−+".includes(k)?"op":"")+'" data-key="'+k+'">'+k+'</button>').join("");
$("calcButtons").addEventListener("click",e=>{let b=e.target.closest("button");if(b)calcPress(b.dataset.key)});

/* Password generator */
function generatePassword(){
 let n=Math.max(6,Math.min(32,Number($("passLength").value)||16)),sets=[];
 if($("passUpper").checked)sets.push("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
 if($("passLower").checked)sets.push("abcdefghijklmnopqrstuvwxyz");
 if($("passNumbers").checked)sets.push("0123456789");
 if($("passSymbols").checked)sets.push("!@#$%^&*()-_=+?");
 if(!sets.length){$("passMessage").textContent="Select at least one character type.";return}
 let chars=sets.join(""),out="";
 for(let i=0;i<n;i++)out+=chars[Math.floor(Math.random()*chars.length)];
 $("passOutput").value=out;$("passMessage").textContent="Password generated.";
}
function copyPassword(){
 let v=$("passOutput").value;
 if(!v){$("passMessage").textContent="Generate a password first.";return}
 if(navigator.clipboard&&navigator.clipboard.writeText){
  navigator.clipboard.writeText(v).then(()=>$("passMessage").textContent="Copied!").catch(()=>$("passMessage").textContent="Select and copy the password.");
 }else{$("passOutput").select();$("passMessage").textContent="Select and copy the password."}
}

/* Notes app */
const NOTES_KEY="mobileAppNotes";
let editingNoteId=null;
function getNotes(){
 try{const saved=JSON.parse(localStorage.getItem(NOTES_KEY)||"[]");return Array.isArray(saved)?saved:[]}
 catch(e){return []}
}
function storeNotes(notes){localStorage.setItem(NOTES_KEY,JSON.stringify(notes))}
function openNotes(){clearNoteEditor();renderNotes();showPage("notesPage");$("notesPage").scrollTop=0}
function clearNoteEditor(){
 $("noteTitle").value="";$("noteContent").value="";
 $("noteEditorHeading").textContent="Create a note";
 $("saveNoteButton").textContent="Save Note";
 $("cancelEditButton").classList.add("hidden");
 $("notesMessage").textContent="";editingNoteId=null;
}
function cancelNoteEdit(){clearNoteEditor()}
function saveNote(){
 const title=$("noteTitle").value.trim(),content=$("noteContent").value.trim();
 if(!title&&!content){$("notesMessage").textContent="Write a title or some note content first.";return}
 const notes=getNotes(),now=new Date().toLocaleString();
 if(editingNoteId!==null){
  const index=notes.findIndex(n=>n.id===editingNoteId);
  if(index!==-1){notes[index].title=title||"Untitled";notes[index].content=content;notes[index].updatedAt=now}
  storeNotes(notes);clearNoteEditor();renderNotes();$("notesMessage").textContent="Note updated successfully.";
 }else{
  notes.unshift({id:Date.now().toString()+"_"+Math.random().toString(36).slice(2,8),title:title||"Untitled",content:content,updatedAt:now});
  storeNotes(notes);clearNoteEditor();renderNotes();$("notesMessage").textContent="Note saved successfully.";
 }
}
function editNote(id){
 const note=getNotes().find(n=>n.id===id);if(!note)return;
 editingNoteId=id;$("noteTitle").value=note.title==="Untitled"?"":note.title;
 $("noteContent").value=note.content;$("noteEditorHeading").textContent="Edit note";
 $("saveNoteButton").textContent="Update Note";$("cancelEditButton").classList.remove("hidden");
 $("notesMessage").textContent="";$("noteTitle").focus();
}
function deleteNote(id){
 if(!confirm("Delete this note?"))return;
 storeNotes(getNotes().filter(n=>n.id!==id));
 if(editingNoteId===id)clearNoteEditor();
 renderNotes();
}
function renderNotes(){
 const list=$("notesList");list.replaceChildren();const notes=getNotes();
 if(notes.length===0){
  const empty=document.createElement("div");empty.className="notes-empty";
  empty.textContent="No notes yet. Create your first note above!";list.appendChild(empty);return;
 }
 notes.forEach(note=>{
  const card=document.createElement("div");card.className="note-card";
  const title=document.createElement("h3");title.textContent=note.title||"Untitled";
  const content=document.createElement("p");content.textContent=note.content||"";
  const meta=document.createElement("div");meta.className="note-meta";meta.textContent="Updated: "+(note.updatedAt||"");
  const actions=document.createElement("div");actions.className="note-actions";
  const edit=document.createElement("button");edit.textContent="✏️ Edit";edit.addEventListener("click",()=>editNote(note.id));
  const del=document.createElement("button");del.className="delete-note";del.textContent="🗑 Delete Note";del.setAttribute("aria-label","Delete note: "+(note.title||"Untitled"));del.addEventListener("click",()=>deleteNote(note.id));
  actions.append(edit,del);card.append(title,content,meta,actions);list.appendChild(card);
 });
}

/* Number Guess */
let secret=0,tries=5,guessDone=false;
function startGuess(){
 secret=Math.floor(Math.random()*20)+1;tries=5;guessDone=false;
 $("attempts").textContent="Attempts left: 5";$("guessMessage").textContent="You have five attempts. Good luck!";
 $("guessInput").value="";$("guessInput").disabled=false;$("guessAgain").classList.add("hidden");showPage("guessPage");
}
function makeGuess(){
 if(guessDone)return;
 let v=Number($("guessInput").value);
 if(!Number.isInteger(v)||v<1||v>20){$("guessMessage").textContent="Enter a whole number from 1 to 20.";return}
 tries--;$("attempts").textContent="Attempts left: "+tries;
 if(v===secret){$("guessMessage").textContent="🎉 Correct! You won!";guessDone=true}
 else if(tries===0){$("guessMessage").textContent="Game over! The number was "+secret+".";guessDone=true}
 else $("guessMessage").textContent=v<secret?"Too low! Try a higher number.":"Too high! Try a lower number.";
 if(guessDone){$("guessInput").disabled=true;$("guessAgain").classList.remove("hidden")}
 $("guessInput").value="";
}

/* Flappy Bird */
const fc=$("flappyCanvas"),fx=fc.getContext("2d");
let bird,pipes,flScore,flRunning=false,flOver=true,flFrame=0,flLoop=null;
let flBest=Number(localStorage.getItem("flappyBest")||0);
$("flappyBest").textContent=flBest;
function startFlappy(){showPage("flappyPage");flappyStart()}
function flappyStart(){
 stopFlappy();bird={x:75,y:220,vy:0};pipes=[];flScore=0;flFrame=0;flRunning=true;flOver=false;
 $("flappyScore").textContent="0";pipes.push({x:390,gapY:190,passed:false});
 flLoop=setInterval(flappyTick,1000/60);drawFlappy();
}
function stopFlappy(){if(flLoop)clearInterval(flLoop);flLoop=null;flRunning=false}
function flap(){
 if(!flRunning){if(flOver)flappyStart();return}
 bird.vy=-5.2;
}
function flappyTick(){
 if(!flRunning)return;
 flFrame++;bird.vy+=0.28;bird.y+=bird.vy;
 if(flFrame%105===0)pipes.push({x:370,gapY:95+Math.random()*220,passed:false});
 pipes.forEach(p=>p.x-=2.5);pipes=pipes.filter(p=>p.x>-65);
 for(let p of pipes){
  if(bird.x+13>p.x&&bird.x-13<p.x+48&&(bird.y-11<p.gapY-73||bird.y+11>p.gapY+73))return flappyEnd();
  if(!p.passed&&p.x+48<bird.x){p.passed=true;flScore++;$("flappyScore").textContent=flScore}
 }
 if(bird.y<0||bird.y>fc.height-20)return flappyEnd();
 drawFlappy();
}
function drawFlappy(){
 fx.clearRect(0,0,360,480);
 let sky=fx.createLinearGradient(0,0,0,480);sky.addColorStop(0,"#55c7f4");sky.addColorStop(1,"#d5f6ff");fx.fillStyle=sky;fx.fillRect(0,0,360,480);
 fx.fillStyle="#ffffff99";
 [[55,70],[220,105],[300,55]].forEach(([x,y])=>{fx.beginPath();fx.arc(x,y,19,0,Math.PI*2);fx.arc(x+18,y+4,15,0,Math.PI*2);fx.fill()});
 pipes.forEach(p=>{
  fx.fillStyle="#27964c";fx.fillRect(p.x,0,48,p.gapY-73);fx.fillRect(p.x,p.gapY+73,48,480);
  fx.fillStyle="#176e3c";fx.fillRect(p.x-4,p.gapY-84,56,11);fx.fillRect(p.x-4,p.gapY+73,56,11);
 });
 fx.fillStyle="#e8c34b";fx.beginPath();fx.ellipse(bird.x,bird.y,14,11,0,0,Math.PI*2);fx.fill();
 fx.fillStyle="#fff";fx.beginPath();fx.arc(bird.x+5,bird.y-4,4,0,Math.PI*2);fx.fill();
 fx.fillStyle="#111";fx.beginPath();fx.arc(bird.x+6,bird.y-4,1.8,0,Math.PI*2);fx.fill();
 fx.fillStyle="#ed7839";fx.beginPath();fx.moveTo(bird.x+12,bird.y);fx.lineTo(bird.x+23,bird.y+4);fx.lineTo(bird.x+12,bird.y+7);fx.fill();
 fx.fillStyle="#347b42";fx.fillRect(0,460,360,20);
 if(flOver){fx.fillStyle="#12384c";fx.textAlign="center";fx.font="bold 23px Arial";fx.fillText("Tap START to play",180,250)}
}
function flappyEnd(){
 stopFlappy();flOver=true;
 if(flScore>flBest){flBest=flScore;localStorage.setItem("flappyBest",flBest);$("flappyBest").textContent=flBest}
 drawFlappy();fx.fillStyle="#12384c";fx.textAlign="center";fx.font="bold 24px Arial";fx.fillText("GAME OVER",180,285);
}
fc.addEventListener("pointerdown",flap);
document.addEventListener("keydown",e=>{if(e.code==="Space"&&!$("flappyPage").classList.contains("hidden")){e.preventDefault();flap()}});

/* Snake */
const sc=$("snakeCanvas"),sx=sc.getContext("2d"),CELL=18,GRID=20;
let snake,apple,dir,nextDir,snScore=0,snTimer=null,snRunning=false,snOver=true;
let snBest=Number(localStorage.getItem("snakeBest")||0);
$("snakeBest").textContent=snBest;
function startSnake(){showPage("snakePage");startSnakeGame()}
function stopSnake(){if(snTimer)clearInterval(snTimer);snTimer=null;snRunning=false}
function randomApple(){
 let a;
 do{a={x:Math.floor(Math.random()*GRID),y:Math.floor(Math.random()*GRID)}}
 while(snake.some(s=>s.x===a.x&&s.y===a.y));
 return a;
}
function startSnakeGame(){
 stopSnake();snake=[{x:9,y:10},{x:8,y:10},{x:7,y:10}];
 dir={x:1,y:0};nextDir={x:1,y:0};snScore=0;apple=randomApple();snRunning=true;snOver=false;
 $("snakeScore").textContent="0";drawSnake();snTimer=setInterval(snakeTick,115);
}
function changeDir(x,y){
 if(!snRunning)return;
 if(x===-dir.x&&y===-dir.y)return;
 nextDir={x,y};
}
function snakeTick(){
 if(!snRunning)return;
 dir=nextDir;
 let head={x:snake[0].x+dir.x,y:snake[0].y+dir.y};
 if(head.x<0||head.x>=GRID||head.y<0||head.y>=GRID||snake.some((s,i)=>i<snake.length-1&&s.x===head.x&&s.y===head.y)){snakeEnd();return}
 snake.unshift(head);
 if(head.x===apple.x&&head.y===apple.y){snScore++;$("snakeScore").textContent=snScore;apple=randomApple()}
 else snake.pop();
 drawSnake();
}
function drawSnake(){
 sx.fillStyle="#082c35";sx.fillRect(0,0,360,360);sx.strokeStyle="#ffffff0b";
 for(let i=0;i<=GRID;i++){
  sx.beginPath();sx.moveTo(i*CELL,0);sx.lineTo(i*CELL,360);sx.stroke();
  sx.beginPath();sx.moveTo(0,i*CELL);sx.lineTo(360,i*CELL);sx.stroke();
 }
 if(apple){
  sx.fillStyle="#ff4e59";sx.beginPath();sx.arc(apple.x*CELL+9,apple.y*CELL+9,7,0,Math.PI*2);sx.fill();
 }
 if(snake)snake.forEach((s,i)=>{
  sx.fillStyle=i===0?"#6cecff":"#168ed5";sx.beginPath();sx.roundRect(s.x*CELL+1,s.y*CELL+1,16,16,5);sx.fill();
 });
 if(snOver){sx.fillStyle="#fff";sx.textAlign="center";sx.font="bold 22px Arial";sx.fillText("Press Start to play",180,190)}
}
function snakeEnd(){
 stopSnake();snOver=true;
 if(snScore>snBest){snBest=snScore;localStorage.setItem("snakeBest",snBest);$("snakeBest").textContent=snBest}
 drawSnake();sx.fillStyle="#fff";sx.textAlign="center";sx.font="bold 24px Arial";sx.fillText("GAME OVER",180,225);
}
document.addEventListener("keydown",e=>{
 if($("snakePage").classList.contains("hidden"))return;
 const map={ArrowUp:[0,-1],ArrowDown:[0,1],ArrowLeft:[-1,0],ArrowRight:[1,0]};
 if(map[e.key]){e.preventDefault();changeDir(...map[e.key])}
});
let touchX=0,touchY=0;
sc.addEventListener("touchstart",e=>{touchX=e.changedTouches[0].clientX;touchY=e.changedTouches[0].clientY},{passive:true});
sc.addEventListener("touchend",e=>{
 let dx=e.changedTouches[0].clientX-touchX,dy=e.changedTouches[0].clientY-touchY;
 if(Math.max(Math.abs(dx),Math.abs(dy))<15)return;
 if(Math.abs(dx)>Math.abs(dy))changeDir(dx>0?1:-1,0);else changeDir(0,dy>0?1:-1);
},{passive:true});

drawFlappy();drawSnake();
</script>
</body>
</html>
"""

components.html(APP, height=1080, scrolling=False)
