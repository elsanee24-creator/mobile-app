import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="mobile.app",
    page_icon="📱",
    layout="centered"
)

APP = r"""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<style>
*{box-sizing:border-box}
:root{
 --bg:#071b17;--panel:#102b25;--panel2:#16382f;
 --green:#62e6a4;--gold:#e8c77b;--text:#f4f4e9;
 --muted:#a9c1b6;--line:#315348;
}
body{
 margin:0;padding:16px 10px;min-height:100vh;
 background:
 radial-gradient(ellipse at 15% 5%,#24634b 0,transparent 35%),
 radial-gradient(ellipse at 90% 90%,#594a25 0,transparent 30%),
 linear-gradient(145deg,#04110f,#0b2821 55%,#101d19);
 color:var(--text);font-family:Arial,sans-serif;
}
#phone{
 max-width:440px;min-height:720px;margin:auto;padding:17px;
 border:1px solid #527568;border-radius:34px;
 background:linear-gradient(160deg,rgba(16,43,37,.97),rgba(5,20,17,.98));
 box-shadow:0 25px 70px #0009,inset 0 0 25px #ffffff08;
 overflow:hidden;
}
.topline{display:flex;justify-content:space-between;align-items:center;
 color:var(--muted);font-size:12px;margin-bottom:18px}
.brand{font-size:13px;letter-spacing:3px;color:var(--gold);font-weight:bold}
.screen{display:none;animation:appear .22s ease}
.screen.active{display:block}
@keyframes appear{from{opacity:0;transform:translateY(7px)}to{opacity:1;transform:none}}
.logo{
 width:68px;height:68px;margin:20px auto 15px;border-radius:22px;
 display:grid;place-items:center;font-size:35px;font-weight:bold;
 color:#09251b;background:linear-gradient(135deg,#a5f4c8,#d7bd79);
 box-shadow:0 8px 30px #62e6a433;
}
.center{text-align:center;padding:38px 8px}
h1{font-size:27px;margin:12px 0 7px}
h2{font-size:20px;margin:10px 0 16px}
p{color:var(--muted);line-height:1.5}
input,textarea{
 width:100%;padding:14px;margin:8px 0;border-radius:13px;
 border:1px solid var(--line);background:#071a15;color:var(--text);
 outline:none;font-size:15px;
}
textarea{resize:vertical}
button{
 border:0;border-radius:13px;padding:13px 15px;
 font-size:14px;font-weight:bold;cursor:pointer;
 transition:transform .12s,filter .12s;
}
button:active{transform:scale(.97);filter:brightness(1.15)}
.primary{width:100%;background:linear-gradient(110deg,#62e6a4,#b8d78c);
 color:#092219;margin-top:10px}
.secondary{width:100%;background:#18372e;color:var(--text);
 border:1px solid #45695b;margin-top:9px}
.back{background:#18372e;color:var(--green);padding:9px 13px}
.header{display:flex;align-items:center;gap:12px;margin:8px 0 20px}
.header h2{margin:0}
.card{
 background:linear-gradient(145deg,#17382f,#0d241e);
 border:1px solid var(--line);border-radius:19px;padding:17px;margin:12px 0;
}
.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.tile{
 min-height:105px;background:linear-gradient(145deg,#1b4034,#10271f);
 border:1px solid #31594a;color:var(--text);display:flex;
 flex-direction:column;align-items:center;justify-content:center;gap:9px;
 padding:12px 5px;
}
.tile span:first-child{font-size:25px}
.tile span:last-child{font-size:12px}
.gamegrid{display:grid;grid-template-columns:repeat(2,1fr);gap:11px}
.gamecard{
 min-height:100px;background:linear-gradient(145deg,#1a4234,#10271f);
 color:var(--text);border:1px solid #426454;display:flex;
 flex-direction:column;align-items:center;justify-content:center;gap:8px;
}
.gamecard span:first-child{font-size:27px}
.display{
 background:#061510;border:1px solid var(--line);border-radius:15px;
 padding:20px;text-align:right;font-size:29px;min-height:75px;
 overflow-wrap:anywhere;margin-bottom:12px;
}
.calcgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.calcgrid button{background:#1c3a30;color:white;padding:17px 4px;font-size:17px}
.calcgrid .op{background:#9c7b3f;color:#fff}
.calcgrid .special{background:#31584a}
.calcgrid .equal{background:#68dba0;color:#092219}
.calcgrid .zero{grid-column:span 2}
.output{padding:15px;background:#071a15;border:1px solid var(--line);
 border-radius:12px;overflow-wrap:anywhere;margin:12px 0}
.option{display:flex;align-items:center;gap:10px;margin:12px 0;color:var(--muted)}
.option input{width:auto;margin:0}
.stats{display:flex;justify-content:space-around;gap:8px;text-align:center}
.stats strong{display:block;color:var(--gold);font-size:20px}
canvas{
 width:100%;display:block;background:#8bd8dc;border-radius:15px;
 border:1px solid #527568;touch-action:manipulation;
}
#snakeCanvas{background:#102e25;touch-action:none}
.message{text-align:center;min-height:24px;color:var(--gold)}
.footer{text-align:center;color:#79998a;font-size:11px;margin:22px 0 5px}
.hidden{display:none!important}
@media(max-width:380px){
 body{padding:5px}#phone{padding:13px;border-radius:25px}
 .grid{gap:7px}.tile{min-height:95px}
}
</style>
</head>
<body>
<div id="phone">
 <div class="topline">
  <span class="brand">MOBILE.APP</span>
  <span id="clock">--:--</span>
 </div>

 <!-- LOGIN -->
 <section id="login" class="screen active">
  <div class="center">
   <div class="logo">M</div>
   <h1>Welcome Back</h1>
   <p>Your personal mobile experience</p>
   <input id="username" placeholder="Enter your name" autocomplete="off">
   <button class="primary" onclick="loginUser()">Login</button>
   <button class="secondary" onclick="guestLogin()">Explore as Guest</button>
  </div>
 </section>

 <!-- PIN LOCK -->
 <section id="lock" class="screen">
  <div class="center">
   <div class="logo">M</div>
   <h1>App Locked</h1>
   <p>Enter your PIN to continue</p>
   <input id="unlockPin" type="password" inputmode="numeric" placeholder="Enter PIN">
   <button class="primary" onclick="unlockApp()">Unlock</button>
   <p id="lockError" class="message"></p>
  </div>
 </section>

 <!-- HOME -->
 <section id="home" class="screen">
  <h1 id="welcomeName">Hello!</h1>
  <p>Your personal space. Everything in one place.</p>
  <h2>Your Apps</h2>
  <div class="grid">
   <button class="tile" onclick="showPage('calculator')"><span>🧮</span><span>Calculator</span></button>
   <button class="tile" onclick="showPage('passwordPage')"><span>🔐</span><span>Password Generator</span></button>
   <button class="tile" onclick="showPage('notesPage')"><span>📝</span><span>Notes</span></button>
   <button class="tile" onclick="showPage('gaming')"><span>🎮</span><span>Gaming Hub</span></button>
   <button class="tile" onclick="showPage('settingsPage')"><span>⚙️</span><span>Settings</span></button>
   <button class="tile" onclick="showPage('aboutPage')"><span>✨</span><span>About</span></button>
  </div>
  <button class="secondary" onclick="logout()">Logout</button>
 </section>

 <!-- CALCULATOR -->
 <section id="calculator" class="screen">
  <div class="header"><button class="back" onclick="showPage('home')">← Back</button><h2>Calculator</h2></div>
  <div class="card">
   <div id="calcDisplay" class="display">0</div>
   <div class="calcgrid">
    <button class="special" onclick="clearCalc()">AC</button>
    <button class="special" onclick="deleteCalc()">DEL</button>
    <button class="special" onclick="appendCalc('%')">%</button>
    <button class="op" onclick="appendCalc('/')">÷</button>
    <button onclick="appendCalc('7')">7</button><button onclick="appendCalc('8')">8</button><button onclick="appendCalc('9')">9</button><button class="op" onclick="appendCalc('*')">×</button>
    <button onclick="appendCalc('4')">4</button><button onclick="appendCalc('5')">5</button><button onclick="appendCalc('6')">6</button><button class="op" onclick="appendCalc('-')">−</button>
    <button onclick="appendCalc('1')">1</button><button onclick="appendCalc('2')">2</button><button onclick="appendCalc('3')">3</button><button class="op" onclick="appendCalc('+')">+</button>
    <button class="zero" onclick="appendCalc('0')">0</button><button onclick="appendCalc('.')">.</button><button class="equal" onclick="calculateResult()">=</button>
   </div>
  </div>
 </section>

 <!-- PASSWORD GENERATOR -->
 <section id="passwordPage" class="screen">
  <div class="header"><button class="back" onclick="showPage('home')">← Back</button><h2>Password Generator</h2></div>
  <div class="card">
   <p>Create a random password.</p>
   <div id="passwordOutput" class="output">Your password will appear here</div>
   <label>Password length</label>
   <input id="passwordLength" type="number" min="4" max="64" value="16">
   <label class="option"><input id="includeNumbers" type="checkbox" checked> Include numbers</label>
   <label class="option"><input id="includeSymbols" type="checkbox" checked> Include symbols</label>
   <button class="primary" onclick="generatePassword()">Generate Password</button>
   <button class="secondary" onclick="copyPassword()">Copy Password</button>
  </div>
 </section>

 <!-- NOTES -->
 <section id="notesPage" class="screen">
  <div class="header"><button class="back" onclick="showPage('home')">← Back</button><h2>My Notes</h2></div>
  <div class="card">
   <input id="noteTitle" placeholder="Note title">
   <textarea id="noteText" rows="4" placeholder="Write your note..."></textarea>
   <button class="primary" onclick="saveNote()">Save Note</button>
   <div id="notesList"></div>
  </div>
 </section>

 <!-- SETTINGS -->
 <section id="settingsPage" class="screen">
  <div class="header"><button class="back" onclick="showPage('home')">← Back</button><h2>Settings</h2></div>
  <div class="card">
   <label>Display name</label><input id="displayName" placeholder="Your name">
   <label class="option"><input id="lightModeToggle" type="checkbox"> Light Mode</label>
   <label class="option"><input id="hapticToggle" type="checkbox"> Haptic Feedback</label>
   <label>App PIN (leave blank to keep current PIN)</label>
   <input id="newPin" type="password" inputmode="numeric" placeholder="Set a PIN">
   <button class="primary" onclick="saveSettings()">Save Settings</button>
   <p id="settingsMessage" class="message"></p>
  </div>
 </section>

 <!-- ABOUT -->
 <section id="aboutPage" class="screen">
  <div class="header"><button class="back" onclick="showPage('home')">← Back</button><h2>About</h2></div>
  <div class="card center"><div class="logo">M</div><h2>mobile.app</h2><p>Your personal collection of useful tools and games.</p><p>Version 1.0</p></div>
 </section>

 <!-- GAMING HUB -->
 <section id="gaming" class="screen">
  <div class="header"><button class="back" onclick="showPage('home')">← Back</button><h2>Gaming Hub</h2></div>
  <div class="gamegrid">
   <button class="gamecard" onclick="resetGuessGame();showPage('guessPage')"><span>🔢</span><span>Number Guessing</span></button>
   <button class="gamecard" onclick="showPage('typingPage')"><span>⌨️</span><span>Typing Speed</span></button>
   <button class="gamecard" onclick="showPage('flappyPage')"><span>🐦</span><span>Flappy Bird</span></button>
   <button class="gamecard" onclick="showPage('snakePage')"><span>🐍</span><span>Snake</span></button>
  </div>
 </section>

 <!-- NUMBER GUESSING -->
 <section id="guessPage" class="screen">
  <div class="header"><button class="back" onclick="showPage('gaming')">← Back</button><h2>Number Guessing</h2></div>
  <div class="card">
   <p>Guess a number between 1 and 100. You have 10 chances.</p>
   <input id="guessInput" type="number" min="1" max="100" placeholder="Your guess">
   <button class="primary" onclick="makeGuess()">Submit Guess</button>
   <p id="guessMessage" class="message"></p>
   <p id="guessAttempts" class="message">Attempts remaining: 10</p>
   <button class="secondary" onclick="resetGuessGame()">Restart Game</button>
  </div>
 </section>

 <!-- TYPING SPEED -->
 <section id="typingPage" class="screen">
  <div class="header"><button class="back" onclick="showPage('gaming')">← Back</button><h2>Typing Speed</h2></div>
  <div class="card">
   <p id="typingText" class="output">Press Start to begin your typing test.</p>
   <textarea id="typingInput" rows="4" placeholder="Type the text here..." disabled></textarea>
   <div class="stats">
    <div>Time<strong id="typingTime">60</strong></div>
    <div>WPM<strong id="typingWpm">0</strong></div>
    <div>Accuracy<strong id="typingAccuracy">100%</strong></div>
   </div>
   <button class="primary" onclick="startTypingGame()">Start Typing Test</button>
   <p id="typingMessage" class="message"></p>
  </div>
 </section>

 <!-- FLAPPY BIRD -->
 <section id="flappyPage" class="screen">
  <div class="header"><button class="back" onclick="stopFlappy();showPage('gaming')">← Back</button><h2>Flappy Bird</h2></div>
  <div class="card">
   <div class="message">Score: <strong id="flappyScore">0</strong></div>
   <canvas id="flappyCanvas" width="360" height="480"></canvas>
   <button class="primary" onclick="startFlappyGame()">Start / Restart</button>
   <p id="flappyMessage" class="message">Tap the game area to fly.</p>
  </div>
 </section>

 <!-- SNAKE -->
 <section id="snakePage" class="screen">
  <div class="header"><button class="back" onclick="stopSnake();showPage('gaming')">← Back</button><h2>Snake</h2></div>
  <div class="card">
   <div class="message">Score: <strong id="snakeScore">0</strong></div>
   <canvas id="snakeCanvas" width="360" height="360"></canvas>
   <p id="snakeMessage" class="message">Swipe or use arrow keys.</p>
   <button class="primary" onclick="startSnakeGame()">Start / Restart</button>
  </div>
 </section>

 <div class="footer">MOBILE.APP • YOUR PERSONAL SPACE</div>
</div>

<script>
"""
// APP JAVASCRIPT

const $ = id => document.getElementById(id);
const screens = document.querySelectorAll(".screen");

let settings = {};
let currentUser = "Guest";
let calcValue = "0";

function loadSettings(){
    try {
        settings = JSON.parse(localStorage.getItem("mobileSettings") || "{}");
    } catch(e) {
        settings = {};
    }
}

function saveLocalSettings(){
    localStorage.setItem("mobileSettings", JSON.stringify(settings));
}

function showPage(id){
    screens.forEach(s => s.classList.remove("active"));
    $(id).classList.add("active");

    if(id !== "flappyPage") stopFlappy();
    if(id !== "snakePage") stopSnake();
}

function updateClock(){
    $("clock").textContent = new Date().toLocaleTimeString([], {
        hour:"2-digit", minute:"2-digit"
    });
}

function loginUser(){
    const name = $("username").value.trim();
    if(!name){
        $("username").focus();
        return;
    }
    currentUser = name;
    continueLogin();
}

function guestLogin(){
    currentUser = "Guest";
    continueLogin();
}

function continueLogin(){
    if(settings.pin){
        $("lockError").textContent = "";
        $("unlockPin").value = "";
        showPage("lock");
    } else {
        enterHome();
    }
}

function unlockApp(){
    if($("unlockPin").value === settings.pin){
        $("lockError").textContent = "";
        enterHome();
    } else {
        $("lockError").textContent = "Incorrect PIN. Try again.";
        $("unlockPin").value = "";
    }
}

function enterHome(){
    $("welcomeName").textContent = "Hello, " + (settings.name || currentUser) + "!";
    showPage("home");
}

function logout(){
    currentUser = "Guest";
    $("username").value = "";
    if(settings.pin){
        $("unlockPin").value = "";
        showPage("lock");
    } else {
        showPage("login");
    }
}

// CALCULATOR
function updateCalc(){
    $("calcDisplay").textContent = calcValue;
}

function appendCalc(value){
    if(calcValue === "0" && "0123456789.".includes(value)){
        calcValue = value;
    } else {
        calcValue += value;
    }
    updateCalc();
}

function clearCalc(){
    calcValue = "0";
    updateCalc();
}

function deleteCalc(){
    calcValue = calcValue.length > 1 ? calcValue.slice(0,-1) : "0";
    updateCalc();
}

function calculateResult(){
    try {
        const expression = calcValue.replace(/%/g, "/100");
        if(!/^[0-9+\-*/().\s]+$/.test(expression)) throw Error();
        const result = Function('"use strict";return (' + expression + ')')();
        if(!Number.isFinite(result)) throw Error();
        calcValue = String(Number(result.toFixed(10)));
    } catch(e) {
        calcValue = "Error";
    }
    updateCalc();
}

// PASSWORD GENERATOR
function generatePassword(){
    let length = Math.max(4, Math.min(64, Number($("passwordLength").value) || 16));
    let chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    if($("includeNumbers").checked) chars += "0123456789";
    if($("includeSymbols").checked) chars += "!@#$%^&*()-_=+?";
    let result = "";
    const random = new Uint32Array(length);
    crypto.getRandomValues(random);
    for(let i=0;i<length;i++){
        result += chars[random[i] % chars.length];
    }
    $("passwordOutput").textContent = result;
}

function copyPassword(){
    const value = $("passwordOutput").textContent;
    if(!value || value === "Your password will appear here") return;
    if(navigator.clipboard && navigator.clipboard.writeText){
        navigator.clipboard.writeText(value)
            .then(() => alert("Password copied!"))
            .catch(() => alert("Copy is not available in this browser."));
    } else {
        alert("Copy is not available in this browser.");
    }
}

// NOTES
function getNotes(){
    try {
        return JSON.parse(localStorage.getItem("mobileNotes") || "[]");
    } catch(e) {
        return [];
    }
}

function renderNotes(){
    const notes = getNotes();
    $("notesList").innerHTML = "";

    notes.forEach((note,index) => {
        const card = document.createElement("div");
        card.className = "card";

        const title = document.createElement("strong");
        title.textContent = note.title;

        const content = document.createElement("p");
        content.textContent = note.text;

        const remove = document.createElement("button");
        remove.className = "secondary";
        remove.textContent = "Delete";
        remove.onclick = () => deleteNote(index);

        card.append(title,content,remove);
        $("notesList").appendChild(card);
    });
}

function saveNote(){
    const title = $("noteTitle").value.trim();
    const text = $("noteText").value.trim();

    if(!title && !text){
        alert("Write something first.");
        return;
    }

    const notes = getNotes();
    notes.unshift({
        title: title || "Untitled",
        text: text,
        date: Date.now()
    });

    localStorage.setItem("mobileNotes",JSON.stringify(notes));
    $("noteTitle").value = "";
    $("noteText").value = "";
    renderNotes();
}

function deleteNote(index){
    const notes = getNotes();
    notes.splice(index,1);
    localStorage.setItem("mobileNotes",JSON.stringify(notes));
    renderNotes();
}

// SETTINGS
function applyTheme(){
    if(settings.lightMode){
        document.documentElement.style.setProperty("--bg","#e9f3ed");
        document.documentElement.style.setProperty("--panel","#ffffff");
        document.documentElement.style.setProperty("--panel2","#e2eee7");
        document.documentElement.style.setProperty("--text","#18352a");
        document.documentElement.style.setProperty("--muted","#526d60");
        document.body.style.background =
            "linear-gradient(145deg,#d8eadf,#f4eee0)";
        $("phone").style.background =
            "linear-gradient(145deg,#ffffff,#e6f1e9)";
    } else {
        document.documentElement.style.setProperty("--bg","#071b17");
        document.documentElement.style.setProperty("--panel","#102b25");
        document.documentElement.style.setProperty("--panel2","#16382f");
        document.documentElement.style.setProperty("--text","#f4f4e9");
        document.documentElement.style.setProperty("--muted","#a9c1b6");
        document.body.style.background =
            "radial-gradient(ellipse at 15% 5%,#24634b 0,transparent 35%),radial-gradient(ellipse at 90% 90%,#594a25 0,transparent 30%),linear-gradient(145deg,#04110f,#0b2821 55%,#101d19)";
        $("phone").style.background =
            "linear-gradient(160deg,rgba(16,43,37,.97),rgba(5,20,17,.98))";
    }
}

function saveSettings(){
    settings.name = $("displayName").value.trim() || settings.name || currentUser;
    settings.lightMode = $("lightModeToggle").checked;
    settings.haptics = $("hapticToggle").checked;

    const newPin = $("newPin").value.trim();
    if(newPin){
        if(!/^\d{4,8}$/.test(newPin)){
            $("settingsMessage").textContent = "PIN must be 4–8 digits.";
            return;
        }
        settings.pin = newPin;
    }

    saveLocalSettings();
    applyTheme();
    $("settingsMessage").textContent = "Settings saved!";
    $("newPin").value = "";
    $("welcomeName").textContent = "Hello, " + settings.name + "!";
}

function vibrate(){
    if(settings.haptics && navigator.vibrate){
        navigator.vibrate(15);
    }
}

// NUMBER GUESSING
let secretNumber = 0;
let attempts = 10;
let guessFinished = false;

function resetGuessGame(){
    secretNumber = Math.floor(Math.random()*100)+1;
    attempts = 10;
    guessFinished = false;
    $("guessInput").value = "";
    $("guessMessage").textContent = "Game started. Make your first guess!";
    $("guessAttempts").textContent = "Attempts remaining: 10";
}

function makeGuess(){
    if(guessFinished) return;

    const guess = Number($("guessInput").value);
    if(!Number.isInteger(guess) || guess < 1 || guess > 100){
        $("guessMessage").textContent = "Enter a number from 1 to 100.";
        return;
    }

    attempts--;
    if(guess === secretNumber){
        $("guessMessage").textContent = "Correct! You won!";
        guessFinished = true;
    } else if(attempts === 0){
        $("guessMessage").textContent = "Game over! Number was " + secretNumber;
        guessFinished = true;
    } else {
        $("guessMessage").textContent =
            guess < secretNumber ? "Too low! Try higher." : "Too high! Try lower.";
    }

    $("guessAttempts").textContent = "Attempts remaining: " + attempts;
    $("guessInput").value = "";
    vibrate();
}

// TYPING SPEED
const typingSamples = [
    "Learning new things every day helps us improve our skills and confidence.",
    "Technology makes communication and information easier for people around the world.",
    "Practice regularly and stay focused to achieve your goals step by step."
];

let typingTimer = null;
let typingSeconds = 60;
let typingStarted = false;

function startTypingGame(){
    clearInterval(typingTimer);
    typingSeconds = 60;
    typingStarted = true;

    $("typingTime").textContent = "60";
    $("typingWpm").textContent = "0";
    $("typingAccuracy").textContent = "100%";
    $("typingInput").value = "";
    $("typingInput").disabled = false;
    $("typingInput").focus();

    $("typingText").textContent =
        typingSamples[Math.floor(Math.random()*typingSamples.length)];
    $("typingMessage").textContent = "Start typing!";

    $("typingInput").oninput = updateTypingStats;

    typingTimer = setInterval(() => {
        typingSeconds--;
        $("typingTime").textContent = typingSeconds;
        updateTypingStats();

        if(typingSeconds <= 0){
            finishTyping();
        }
    },1000);
}

function updateTypingStats(){
    if(!typingStarted) return;

    const target = $("typingText").textContent;
    const typed = $("typingInput").value;
    let correct = 0;

    for(let i=0;i<typed.length;i++){
        if(typed[i] === target[i]) correct++;
    }

    const elapsed = Math.max(1,60-typingSeconds);
    const wpm = Math.round((typed.trim().split(/\s+/).filter(Boolean).length / elapsed)*60);
    const accuracy = typed.length ? Math.round(correct/typed.length*100) : 100;

    $("typingWpm").textContent = wpm;
    $("typingAccuracy").textContent = accuracy + "%";

    if(typed === target){
        finishTyping();
    }
}

function finishTyping(){
    clearInterval(typingTimer);
    typingStarted = false;
    $("typingInput").disabled = true;
    $("typingMessage").textContent = "Test finished!";
}

// FLAPPY BIRD — SMOOTH ANIMATION
const flappyCanvas = $("flappyCanvas");
const fctx = flappyCanvas.getContext("2d");

let bird = {x:75,y:210,velocity:0};
let pipes = [];
let flappyScore = 0;
let flappyRunning = false;
let flappyFrame = 0;
let lastFlappyTime = 0;

function drawFlappy(){
    const w = flappyCanvas.width;
    const h = flappyCanvas.height;

    const sky = fctx.createLinearGradient(0,0,0,h);
    sky.addColorStop(0,"#70d5e0");
    sky.addColorStop(1,"#d5f1d5");
    fctx.fillStyle = sky;
    fctx.fillRect(0,0,w,h);

    fctx.fillStyle = "#ffffffaa";
    for(let i=0;i<4;i++){
        const x = (i*110 + 30 - flappyFrame*.25) % (w+70);
        fctx.beginPath();
        fctx.arc(x,70+i%2*40,17,0,Math.PI*2);
        fctx.arc(x+20,70+i%2*40,22,0,Math.PI*2);
        fctx.arc(x+42,70+i%2*40,15,0,Math.PI*2);
        fctx.fill();
    }

    fctx.fillStyle = "#5aab65";
    fctx.fillRect(0,h-28,w,28);

    pipes.forEach(p => {
        fctx.fillStyle = "#278b50";
        fctx.fillRect(p.x,0,48,p.top);
        fctx.fillRect(p.x,p.top+135,48,h-p.top-135-28);
        fctx.fillStyle = "#176d3b";
        fctx.fillRect(p.x-4,p.top-14,56,14);
        fctx.fillRect(p.x-4,p.top+135,56,14);
    });

    fctx.save();
    fctx.translate(bird.x,bird.y);
    fctx.rotate(Math.max(-.4,Math.min(.7,bird.velocity*.06)));
    fctx.fillStyle = "#f6c84a";
    fctx.beginPath();
    fctx.ellipse(0,0,16,12,0,0,Math.PI*2);
    fctx.fill();
    fctx.fillStyle = "#fff";
    fctx.beginPath();
    fctx.arc(7,-5,5,0,Math.PI*2);
    fctx.fill();
    fctx.fillStyle = "#18251b";
    fctx.beginPath();
    fctx.arc(9,-5,2,0,Math.PI*2);
    fctx.fill();
    fctx.fillStyle = "#e9783f";
    fctx.beginPath();
    fctx.moveTo(12,2);
    fctx.lineTo(25,6);
    fctx.lineTo(12,9);
    fctx.fill();
    fctx.restore();
}

function flappyJump(){
    if(!flappyRunning) return;
    bird.velocity = -6.2;
}

function flappyLoop(timestamp){
    if(!flappyRunning) return;

    const delta = Math.min((timestamp-lastFlappyTime)/16.67,2);
    lastFlappyTime = timestamp;
    flappyFrame += delta;

    bird.velocity += .28*delta;
    bird.y += bird.velocity*delta;

    if(flappyFrame % 95 < delta){
        const top = 65 + Math.random()*190;
        pipes.push({x:flappyCanvas.width,top:top,passed:false});
    }

    pipes.forEach(p => {
        p.x -= 2.5*delta;

        if(!p.passed && p.x+48<bird.x){
            p.passed = true;
            flappyScore++;
            $("flappyScore").textContent = flappyScore;
        }

        const hitX = bird.x+12>p.x && bird.x-12<p.x+48;
        const hitY = bird.y-10<p.top || bird.y+10>p.top+135;

        if(hitX && hitY) endFlappy();
    });

    pipes = pipes.filter(p => p.x>-60);

    if(bird.y>flappyCanvas.height-35 || bird.y<0){
        endFlappy();
    }

    drawFlappy();

    if(flappyRunning){
        requestAnimationFrame(flappyLoop);
    }
}

function startFlappyGame(){
    stopFlappy();
    bird = {x:75,y:210,velocity:0};
    pipes = [];
    flappyScore = 0;
    flappyFrame = 0;
    lastFlappyTime = performance.now();
    flappyRunning = true;

    $("flappyScore").textContent = "0";
    $("flappyMessage").textContent = "Tap to fly!";
    drawFlappy();
    requestAnimationFrame(flappyLoop);
}

function endFlappy(){
    if(!flappyRunning) return;
    flappyRunning = false;
    $("flappyMessage").textContent = "Game over! Score: " + flappyScore;
}

function stopFlappy(){
    flappyRunning = false;
}

flappyCanvas.addEventListener("pointerdown",flappyJump);

// SNAKE — SMOOTH GAME LOOP
const snakeCanvas = $("snakeCanvas");
const sctx = snakeCanvas.getContext("2d");

const cell = 18;
const boardSize = 20;

let snake = [];
let food = {};
let snakeDirection = {x:1,y:0};
let nextDirection = {x:1,y:0};
let snakeRunning = false;
let snakeTimer = null;
let snakeScore = 0;

function placeFood(){
    do {
        food = {
            x:Math.floor(Math.random()*boardSize),
            y:Math.floor(Math.random()*boardSize)
        };
    } while(snake.some(p=>p.x===food.x && p.y===food.y));
}

function drawSnake(){
    sctx.fillStyle = "#102e25";
    sctx.fillRect(0,0,360,360);

    sctx.strokeStyle = "#1b4537";
    sctx.lineWidth = .5;

    for(let i=0;i<=360;i+=cell){
        sctx.beginPath();
        sctx.moveTo(i,0);
        sctx.lineTo(i,360);
        sctx.stroke();

        sctx.beginPath();
        sctx.moveTo(0,i);
        sctx.lineTo(360,i);
        sctx.stroke();
    }

    sctx.fillStyle = "#e8c77b";
    sctx.beginPath();
    sctx.arc(food.x*cell+9,food.y*cell+9,7,0,Math.PI*2);
    sctx.fill();

    snake.forEach((p,i)=>{
        sctx.fillStyle = i===0 ? "#a5f4c8" : "#45b982";
        sctx.fillRect(p.x*cell+1,p.y*cell+1,cell-2,cell-2);
    });
}

function startSnakeGame(){
    stopSnake();
    snake = [{x:7,y:10},{x:6,y:10},{x:5,y:10}];
    snakeDirection = {x:1,y:0};
    nextDirection = {x:1,y:0};
    snakeScore = 0;

    $("snakeScore").textContent = "0";
    $("snakeMessage").textContent = "Collect the food!";
    placeFood();
    drawSnake();

    snakeRunning = true;
    snakeTimer = setInterval(snakeStep,115);
}

function snakeStep(){
    if(!snakeRunning) return;

    snakeDirection = nextDirection;

    const head = {
        x:snake[0].x+snakeDirection.x,
        y:snake[0].y+snakeDirection.y
    };

    const eating = head.x===food.x && head.y===food.y;
    const body = eating ? snake : snake.slice(0,-1);

    if(
        head.x<0 || head.y<0 ||
        head.x>=boardSize || head.y>=boardSize ||
        body.some(p=>p.x===head.x && p.y===head.y)
    ){
        stopSnake();
        $("snakeMessage").textContent = "Game over! Score: " + snakeScore;
        return;
    }

    snake.unshift(head);

    if(eating){
        snakeScore += 10;
        $("snakeScore").textContent = snakeScore;
        placeFood();
    } else {
        snake.pop();
    }

    drawSnake();
}

function stopSnake(){
    snakeRunning = false;
    if(snakeTimer){
        clearInterval(snakeTimer);
        snakeTimer = null;
    }
}

function changeSnakeDirection(x,y){
    if(x===-snakeDirection.x && y===-snakeDirection.y) return;
    nextDirection = {x:x,y:y};
}

document.addEventListener("keydown",e=>{
    if(!$("snakePage").classList.contains("active")) return;

    if(e.key==="ArrowUp" || e.key.toLowerCase()==="w"){
        e.preventDefault();
        changeSnakeDirection(0,-1);
    }
    if(e.key==="ArrowDown" || e.key.toLowerCase()==="s"){
        e.preventDefault();
        changeSnakeDirection(0,1);
    }
    if(e.key==="ArrowLeft" || e.key.toLowerCase()==="a"){
        e.preventDefault();
        changeSnakeDirection(-1,0);
    }
    if(e.key==="ArrowRight" || e.key.toLowerCase()==="d"){
        e.preventDefault();
        changeSnakeDirection(1,0);
    }
});

let swipeStart = null;

snakeCanvas.addEventListener("pointerdown",e=>{
    swipeStart = {x:e.clientX,y:e.clientY};
});

snakeCanvas.addEventListener("pointerup",e=>{
    if(!swipeStart) return;

    const dx = e.clientX-swipeStart.x;
    const dy = e.clientY-swipeStart.y;

    if(Math.max(Math.abs(dx),Math.abs(dy))>15){
        if(Math.abs(dx)>Math.abs(dy)){
            changeSnakeDirection(dx>0?1:-1,0);
        } else {
            changeSnakeDirection(0,dy>0?1:-1);
        }
    }
    swipeStart = null;
});

// STARTUP
function initializeApp(){
    loadSettings();

    $("displayName").value = settings.name || "";
    $("lightModeToggle").checked = !!settings.lightMode;
    $("hapticToggle").checked = !!settings.haptics;

    applyTheme();
    updateClock();
    renderNotes();
    resetGuessGame();
    drawFlappy();
    drawSnake();

    setInterval(updateClock,1000);

    if(settings.pin){
        showPage("lock");
    } else {
        showPage("login");
    }
}

initializeApp();
</script>
</body>
</html>
"""

components.html(APP, height=950, scrolling=True)
