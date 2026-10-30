
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
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-tap-highlight-color: transparent;
}

:root {
    --bg1: #061c18;
    --bg2: #0b3027;
    --card: rgba(15, 65, 51, .75);
    --accent: #39ff9c;
    --accent2: #00c878;
    --text: #f2fff8;
    --muted: #a8cbb9;
    --border: rgba(57,255,156,.22);
}

body {
    min-height: 100vh;
    font-family: Arial, sans-serif;
    color: var(--text);
    background:
        radial-gradient(circle at 15% 10%, #14543e, transparent 40%),
        linear-gradient(145deg, var(--bg1), var(--bg2));
    transition: background .45s ease, color .3s ease;
    overflow-x: hidden;
}

body.theme-blue {
    --bg1:#07172e;
    --bg2:#102f59;
    --card:rgba(18,54,94,.78);
    --accent:#54c8ff;
    --accent2:#278cff;
    --text:#f2f9ff;
    --muted:#b2cce4;
    --border:rgba(84,200,255,.25);
}

body.theme-purple {
    --bg1:#1b1030;
    --bg2:#382052;
    --card:rgba(66,39,94,.78);
    --accent:#d59aff;
    --accent2:#a45bff;
    --text:#fff8ff;
    --muted:#d0b9e3;
    --border:rgba(213,154,255,.25);
}

body.theme-light {
    --bg1:#e9fff4;
    --bg2:#ccefe0;
    --card:rgba(255,255,255,.85);
    --accent:#078b58;
    --accent2:#10b978;
    --text:#123b2c;
    --muted:#557565;
    --border:rgba(0,130,80,.2);
}

body.theme-dark {
    --bg1:#101114;
    --bg2:#202329;
    --card:rgba(43,46,53,.85);
    --accent:#eeeeee;
    --accent2:#aaaaaa;
    --text:#ffffff;
    --muted:#b8bbc2;
    --border:rgba(255,255,255,.15);
}

#app {
    width:100%;
    max-width:520px;
    min-height:100vh;
    margin:auto;
    padding:18px 15px 30px;
    animation: appEnter .7s ease;
}

@keyframes appEnter {
    from { opacity:0; transform:translateY(15px); }
    to { opacity:1; transform:translateY(0); }
}

@keyframes fadeIn {
    from { opacity:0; transform:translateY(12px); }
    to { opacity:1; transform:translateY(0); }
}

@keyframes glow {
    0%,100% { box-shadow:0 0 8px var(--border); }
    50% { box-shadow:0 0 22px var(--accent); }
}

@keyframes spin {
    to { transform:rotate(360deg); }
}

@keyframes pulse {
    0%,100% { transform:scale(1); }
    50% { transform:scale(1.06); }
}

@keyframes pop {
    0% { transform:scale(.92); opacity:.5; }
    100% { transform:scale(1); opacity:1; }
}

.header {
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin-bottom:24px;
}

.logo {
    font-size:25px;
    font-weight:900;
    letter-spacing:-1px;
}

.logo span {
    color:var(--accent);
    text-shadow:0 0 15px var(--accent);
}

.theme-control {
    background:var(--card);
    color:var(--text);
    border:1px solid var(--border);
    padding:9px 10px;
    border-radius:12px;
    font-size:12px;
    outline:none;
}

.screen {
    display:none;
    animation:fadeIn .4s ease;
}

.screen.active {
    display:block;
}

.card {
    background:var(--card);
    border:1px solid var(--border);
    border-radius:20px;
    padding:20px;
    box-shadow:0 8px 30px rgba(0,0,0,.12);
    backdrop-filter:blur(12px);
    margin-bottom:16px;
    transition:transform .25s, box-shadow .25s;
}

.card:hover {
    box-shadow:0 0 18px var(--border);
}

h1 {
    font-size:27px;
    margin-bottom:10px;
}

h2 {
    font-size:21px;
    margin-bottom:12px;
}

p {
    color:var(--muted);
    line-height:1.5;
}

.primary-btn, .secondary-btn {
    width:100%;
    border:0;
    border-radius:14px;
    padding:14px;
    font-size:15px;
    font-weight:bold;
    cursor:pointer;
    transition:transform .18s, filter .2s, box-shadow .2s;
}

.primary-btn {
    color:#042719;
    background:linear-gradient(120deg,var(--accent),var(--accent2));
    box-shadow:0 0 14px var(--border);
}

.secondary-btn {
    color:var(--text);
    background:var(--card);
    border:1px solid var(--border);
}

.primary-btn:active, .secondary-btn:active, .square-btn:active {
    transform:scale(.94);
}

button {
    font-family:inherit;
}

input, select {
    width:100%;
    padding:13px;
    margin:9px 0;
    border-radius:12px;
    border:1px solid var(--border);
    background:var(--bg1);
    color:var(--text);
    outline:none;
    font-size:15px;
}

input:focus, select:focus {
    box-shadow:0 0 12px var(--border);
    border-color:var(--accent);
}

.dashboard-grid {
    display:grid;
    grid-template-columns:repeat(3,1fr);
    gap:11px;
    margin-top:20px;
}

.square-btn {
    min-width:0;
    aspect-ratio:1/1;
    border:1px solid var(--border);
    border-radius:17px;
    background:var(--card);
    color:var(--text);
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;
    gap:9px;
    font-size:12px;
    font-weight:bold;
    cursor:pointer;
    transition:all .25s ease;
    animation:pop .45s ease;
}

.square-btn:hover {
    transform:translateY(-5px);
    box-shadow:0 0 20px var(--border);
    border-color:var(--accent);
}

.square-icon {
    font-size:29px;
}

.back-btn {
    display:inline-block;
    padding:9px 13px;
    border-radius:10px;
    border:1px solid var(--border);
    background:var(--card);
    color:var(--text);
    margin-bottom:17px;
    cursor:pointer;
}

.loading-area {
    display:none;
    text-align:center;
    padding:25px 10px;
}

.loader {
    width:38px;
    height:38px;
    border:4px solid var(--border);
    border-top-color:var(--accent);
    border-radius:50%;
    animation:spin .8s linear infinite;
    margin:15px auto;
}

.loading-dots {
    display:flex;
    justify-content:center;
    gap:7px;
    margin-top:10px;
}

.loading-dots span {
    width:8px;
    height:8px;
    border-radius:50%;
    background:var(--accent);
    animation:pulse .7s infinite alternate;
}

.loading-dots span:nth-child(2) {
    animation-delay:.2s;
}

.loading-dots span:nth-child(3) {
    animation-delay:.4s;
}

.notice {
    color:var(--accent);
    font-size:13px;
    min-height:20px;
    margin-top:10px;
    text-align:center;
}

@media(max-width:360px) {
    #app { padding:14px 10px; }
    .dashboard-grid { gap:7px; }
    .square-btn { font-size:11px; }
    .square-icon { font-size:25px; }
}
</style>
</head>
"""

<body>
<div id="app">

    <div class="header">
        <div class="logo">mobile<span>.app</span></div>

        <select class="theme-control" id="themeSelect" onchange="changeTheme(this.value)">
            <option value="green">Green Neon</option>
            <option value="blue">Blue</option>
            <option value="purple">Purple</option>
            <option value="light">Light</option>
            <option value="dark">Dark</option>
        </select>
    </div>

    <!-- LOGIN SCREEN -->
    <section id="login" class="screen active">
        <div class="card" style="margin-top:45px;text-align:center;">
            <div style="font-size:55px;margin-bottom:15px;">📱</div>
            <h1>Welcome to mobile.app</h1>
            <p>Your mini digital world.</p>

            <div id="loginForm">
                <input id="username" type="text" placeholder="Enter your name">

                <button class="primary-btn" onclick="loginUser()">
                    Login
                </button>

                <button class="secondary-btn" style="margin-top:10px;"
                    onclick="guestUser()">
                    Continue as Guest
                </button>
            </div>

            <div class="loading-area" id="loginLoading">
                <div class="loader"></div>
                <h3 id="loadingTitle">Processing...</h3>
                <div class="loading-dots">
                    <span></span><span></span><span></span>
                </div>
                <p style="margin-top:12px;">Please wait a moment</p>
            </div>
        </div>
    </section>

    <!-- HOME SCREEN -->
    <section id="home" class="screen">
        <div class="card">
            <h1 id="welcomeTitle">Hello!</h1>
            <p>Choose an application to get started.</p>
        </div>

        <div class="dashboard-grid">

            <button class="square-btn" onclick="go('calculator')">
                <span class="square-icon">🧮</span>
                Calculator
            </button>

            <button class="square-btn" onclick="go('guess')">
                <span class="square-icon">🎯</span>
                Number Guess
            </button>

            <button class="square-btn" onclick="go('flappy')">
                <span class="square-icon">🐦</span>
                Flappy Bird
            </button>

            <button class="square-btn" onclick="go('password')">
                <span class="square-icon">🔐</span>
                Password Generator
            </button>

        </div>

        <div class="card" style="margin-top:20px;text-align:center;">
            <p>Made with creativity ✨</p>
            <button class="secondary-btn" style="margin-top:13px;"
                onclick="logoutUser()">
                Logout
            </button>
        </div>
    </section>

    <!-- CALCULATOR SCREEN -->
    <section id="calculator" class="screen">
        <button class="back-btn" onclick="go('home')">← Home</button>

        <div class="card">
            <h2>🧮 Calculator</h2>

            <input id="calcDisplay" type="text" value="0"
                readonly style="font-size:27px;text-align:right;">

            <div id="calcKeys"
                style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:12px;">

                <button class="secondary-btn" onclick="calcPress('C')">C</button>
                <button class="secondary-btn" onclick="calcPress('(')">(</button>
                <button class="secondary-btn" onclick="calcPress(')')">)</button>
                <button class="secondary-btn" onclick="calcPress('/')">÷</button>

                <button class="secondary-btn" onclick="calcPress('7')">7</button>
                <button class="secondary-btn" onclick="calcPress('8')">8</button>
                <button class="secondary-btn" onclick="calcPress('9')">9</button>
                <button class="secondary-btn" onclick="calcPress('*')">×</button>

                <button class="secondary-btn" onclick="calcPress('4')">4</button>
                <button class="secondary-btn" onclick="calcPress('5')">5</button>
                <button class="secondary-btn" onclick="calcPress('6')">6</button>
                <button class="secondary-btn" onclick="calcPress('-')">−</button>

                <button class="secondary-btn" onclick="calcPress('1')">1</button>
                <button class="secondary-btn" onclick="calcPress('2')">2</button>
                <button class="secondary-btn" onclick="calcPress('3')">3</button>
                <button class="secondary-btn" onclick="calcPress('+')">+</button>

                <button class="secondary-btn" onclick="calcPress('0')">0</button>
                <button class="secondary-btn" onclick="calcPress('.')">.</button>
                <button class="secondary-btn" onclick="calcBack()">⌫</button>
                <button class="primary-btn" onclick="calculateCalc()">=</button>

            </div>
        </div>
    </section>

    <!-- NUMBER GUESS SCREEN -->
    <section id="guess" class="screen">
        <button class="back-btn" onclick="go('home')">← Home</button>

        <div class="card">
            <h2>🎯 Number Guessing</h2>
            <p>Guess a number between 1 and 100.</p>

            <h3 id="triesText" style="margin-top:15px;">
                Attempts left: 10
            </h3>

            <input id="guessInput" type="number"
                placeholder="Enter your guess">

            <button class="primary-btn" onclick="submitGuess()">
                Submit Guess
            </button>

            <div class="notice" id="guessMessage"></div>

            <button class="secondary-btn" style="margin-top:12px;"
                onclick="newGame()">
                New Game
            </button>
        </div>
    </section>

    <!-- FLAPPY BIRD SCREEN -->
    <section id="flappy" class="screen">
        <button class="back-btn" onclick="go('home')">← Home</button>

        <div class="card" style="text-align:center;">
            <h2>🐦 Flappy Bird</h2>
            <p>Tap Jump to fly through the pipes.</p>

            <h3 id="birdScoreText" style="margin:12px;">
                Score: 0
            </h3>

            <canvas id="birdCanvas" width="360" height="480"
                style="width:100%;max-width:360px;border-radius:14px;
                background:#87ceeb;display:block;margin:auto;">
            </canvas>

            <button class="primary-btn" style="margin-top:13px;"
                onclick="birdJump()">
                JUMP
            </button>

            <button class="secondary-btn" style="margin-top:9px;"
                onclick="resetBird()">
                Restart
            </button>
        </div>
    </section>

    <!-- PASSWORD GENERATOR SCREEN -->
    <section id="password" class="screen">
        <button class="back-btn" onclick="go('home')">← Home</button>

        <div class="card">
            <h2>🔐 Password Generator</h2>
            <p>Create a random password on your device.</p>

            <label style="display:block;margin-top:18px;">
                Password Length
            </label>

            <input id="passwordLength" type="number"
                min="8" max="32" value="16">

            <label style="display:block;margin-top:12px;">
                Password Options
            </label>

            <label style="display:block;margin-top:12px;">
                <input type="checkbox" id="useUpper" checked
                    style="width:auto;margin-right:8px;">
                Uppercase letters (A-Z)
            </label>

            <label style="display:block;margin-top:12px;">
                <input type="checkbox" id="useLower" checked
                    style="width:auto;margin-right:8px;">
                Lowercase letters (a-z)
            </label>

            <label style="display:block;margin-top:12px;">
                <input type="checkbox" id="useNumbers" checked
                    style="width:auto;margin-right:8px;">
                Numbers (0-9)
            </label>

            <label style="display:block;margin-top:12px;">
                <input type="checkbox" id="useSymbols" checked
                    style="width:auto;margin-right:8px;">
                Special symbols
            </label>

            <button class="primary-btn" style="margin-top:18px;"
                onclick="generatePassword()">
                Generate Password
            </button>

            <input id="passwordOutput" type="text"
                placeholder="Your password will appear here"
                readonly style="margin-top:15px;text-align:center;">

            <button class="secondary-btn"
                onclick="copyPassword()">
                📋 Copy Password
            </button>

            <div class="notice" id="passwordMessage"></div>
        </div>
    </section>

</div>
</body>
</html>

<script>

// THEME SYSTEM
function changeTheme(theme) {
    document.body.className = "";

    if(theme !== "green") {
        document.body.classList.add("theme-" + theme);
    }

    localStorage.setItem("mobileAppTheme", theme);
}

const savedTheme = localStorage.getItem("mobileAppTheme") || "green";
document.getElementById("themeSelect").value = savedTheme;
changeTheme(savedTheme);


// SCREEN NAVIGATION
function go(id) {
    document.querySelectorAll(".screen").forEach(function(screen) {
        screen.classList.remove("active");
    });

    const target = document.getElementById(id);

    if(target) {
        target.classList.add("active");
    }

    if(id === "flappy") {
        drawBirdGame();
    }
}


// LOGIN AND GUEST PROCESSING
function showProcessing(name) {
    document.getElementById("loginForm").style.display = "none";
    document.getElementById("loginLoading").style.display = "block";
    document.getElementById("loadingTitle").textContent = name;

    setTimeout(function() {
        document.getElementById("loginLoading").style.display = "none";
        document.getElementById("loginForm").style.display = "block";
        go("home");
    }, 1500);
}

function loginUser() {
    const name = document.getElementById("username").value.trim();

    if(!name) {
        alert("Please enter your name.");
        return;
    }

    document.getElementById("welcomeTitle").textContent = "Hello, " + name + "!";
    showProcessing("Logging in...");
}

function guestUser() {
    document.getElementById("welcomeTitle").textContent = "Hello, Guest!";
    showProcessing("Preparing your app...");
}

function logoutUser() {
    document.getElementById("username").value = "";
    go("login");
}


// CALCULATOR
let calcExpression = "";

function updateCalc() {
    document.getElementById("calcDisplay").value =
        calcExpression || "0";
}

function calcPress(value) {
    if(value === "C") {
        calcExpression = "";
    } else {
        calcExpression += value;
    }

    updateCalc();
}

function calcBack() {
    calcExpression = calcExpression.slice(0, -1);
    updateCalc();
}

function calculateCalc() {
    try {
        if(!calcExpression) return;

        if(!/^[0-9+\-*/(). ]+$/.test(calcExpression)) {
            throw new Error("Invalid");
        }

        const result = Function(
            '"use strict"; return (' + calcExpression + ')'
        )();

        if(!Number.isFinite(result)) {
            throw new Error("Invalid");
        }

        calcExpression = String(result);
        updateCalc();

    } catch(error) {
        document.getElementById("calcDisplay").value = "Error";
        calcExpression = "";
    }
}


// NUMBER GUESSING GAME
let secretNumber = Math.floor(Math.random() * 100) + 1;
let triesLeft = 10;
let gameFinished = false;

function updateGuessDisplay() {
    document.getElementById("triesText").textContent =
        "Attempts left: " + triesLeft;
}

function newGame() {
    secretNumber = Math.floor(Math.random() * 100) + 1;
    triesLeft = 10;
    gameFinished = false;

    document.getElementById("guessInput").value = "";
    document.getElementById("guessMessage").textContent = "";

    updateGuessDisplay();
}

function submitGuess() {
    if(gameFinished) return;

    const input = document.getElementById("guessInput");
    const guess = Number(input.value);
    const message = document.getElementById("guessMessage");

    if(input.value.trim() === "" || !Number.isInteger(guess) ||
       guess < 1 || guess > 100) {
        message.textContent = "Enter a number between 1 and 100.";
        return;
    }

    triesLeft--;

    if(guess === secretNumber) {
        message.textContent = "Yay! You won !!!!";
        gameFinished = true;
    } else if(triesLeft === 0) {
        message.textContent = "Oops! You're out of tries. Number was " +
            secretNumber;
        gameFinished = true;
    } else if(guess < secretNumber) {
        message.textContent = "Too low! Try a higher number.";
    } else {
        message.textContent = "Too high! Try a lower number.";
    }

    updateGuessDisplay();
    input.value = "";
}


// PASSWORD GENERATOR
function generatePassword() {
    const lengthInput = document.getElementById("passwordLength");
    let length = Number(lengthInput.value);

    if(!Number.isInteger(length) || length < 8 || length > 32) {
        document.getElementById("passwordMessage").textContent =
            "Choose a length between 8 and 32.";
        return;
    }

    const groups = [];

    if(document.getElementById("useUpper").checked) {
        groups.push("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
    }

    if(document.getElementById("useLower").checked) {
        groups.push("abcdefghijklmnopqrstuvwxyz");
    }

    if(document.getElementById("useNumbers").checked) {
        groups.push("0123456789");
    }

    if(document.getElementById("useSymbols").checked) {
        groups.push("!@#$%&*_-+=?");
    }

    const message = document.getElementById("passwordMessage");
    const output = document.getElementById("passwordOutput");

    if(groups.length === 0) {
        message.textContent = "Select at least one option.";
        output.value = "";
        return;
    }

    const allCharacters = groups.join("");
    const randomValues = new Uint32Array(length);
    crypto.getRandomValues(randomValues);

    let password = "";

    // Include at least one character from every selected group.
    for(let i = 0; i < groups.length; i++) {
        const groupIndex = randomValues[i] % groups[i].length;
        password += groups[i][groupIndex];
    }

    for(let i = groups.length; i < length; i++) {
        password += allCharacters[
            randomValues[i] % allCharacters.length
        ];
    }

    // Shuffle the password.
    let shuffled = password.split("");

    for(let i = shuffled.length - 1; i > 0; i--) {
        const j = randomValues[i] % (i + 1);
        [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }

    output.value = shuffled.join("");
    output.style.animation = "none";
    void output.offsetWidth;
    output.style.animation = "pop .35s ease";

    message.textContent = "New password generated!";
}

async function copyPassword() {
    const output = document.getElementById("passwordOutput");
    const message = document.getElementById("passwordMessage");

    if(!output.value) {
        message.textContent = "Generate a password first.";
        return;
    }

    try {
        await navigator.clipboard.writeText(output.value);
        message.textContent = "Password copied!";
    } catch(error) {
        output.select();
        const copied = document.execCommand("copy");
        message.textContent = copied ?
            "Password copied!" :
            "Copy unavailable. Select and copy manually.";
    }
}


// FLAPPY BIRD VARIABLES
const canvas = document.getElementById("birdCanvas");
const ctx = canvas.getContext("2d");

let bird = {
    x:75,
    y:220,
    velocity:0,
    radius:13
};

let pipes = [];
let birdScore = 0;
let birdFrame = 0;
let birdRunning = false;
let birdStarted = false;
let birdLoopActive = false;

function resetBird() {
    bird.y = 220;
    bird.velocity = 0;

    pipes = [];
    birdScore = 0;
    birdFrame = 0;

    birdRunning = true;
    birdStarted = true;

    document.getElementById("birdScoreText").textContent =
        "Score: 0";

    drawBirdGame();
    startBirdLoop();
}

function birdJump() {
    if(!birdStarted || !birdRunning) {
        resetBird();
    }

    bird.velocity = -6.5;
    drawBirdGame();
}

function drawBirdGame() {
    ctx.clearRect(0, 0, 360, 480);

    const sky = ctx.createLinearGradient(0, 0, 0, 480);
    sky.addColorStop(0, "#71d6ff");
    sky.addColorStop(1, "#d6f5ff");

    ctx.fillStyle = sky;
    ctx.fillRect(0, 0, 360, 480);

    // Clouds
    ctx.fillStyle = "rgba(255,255,255,.8)";

    ctx.beginPath();
    ctx.arc(65, 75, 19, 0, Math.PI*2);
    ctx.arc(88, 75, 25, 0, Math.PI*2);
    ctx.arc(112, 75, 18, 0, Math.PI*2);
    ctx.fill();

    ctx.beginPath();
    ctx.arc(245, 145, 17, 0, Math.PI*2);
    ctx.arc(267, 145, 24, 0, Math.PI*2);
    ctx.arc(289, 145, 17, 0, Math.PI*2);
    ctx.fill();

    // Pipes
    for(const p of pipes) {
        ctx.fillStyle = "#159447";
        ctx.fillRect(p.x, 0, 48, p.top);
        ctx.fillRect(p.x, p.bottom, 48, 480-p.bottom);

        ctx.fillStyle = "#087638";
        ctx.fillRect(p.x-4, p.top-12, 56, 12);
        ctx.fillRect(p.x-4, p.bottom, 56, 12);
    }

    // Bird
    ctx.fillStyle = "#ffdf38";
    ctx.beginPath();
    ctx.arc(bird.x, bird.y, bird.radius, 0, Math.PI*2);
    ctx.fill();

    ctx.fillStyle = "#ffffff";
    ctx.beginPath();
    ctx.arc(bird.x+5, bird.y-4, 4, 0, Math.PI*2);
    ctx.fill();

    ctx.fillStyle = "#111111";
    ctx.beginPath();
    ctx.arc(bird.x+6, bird.y-4, 2, 0, Math.PI*2);
    ctx.fill();

    ctx.fillStyle = "#ff7a21";
    ctx.beginPath();
    ctx.moveTo(bird.x+12, bird.y);
    ctx.lineTo(bird.x+23, bird.y+4);
    ctx.lineTo(bird.x+12, bird.y+7);
    ctx.fill();

    document.getElementById("birdScoreText").textContent =
        "Score: " + birdScore;

    if(birdStarted && !birdRunning) {
        ctx.fillStyle = "rgba(0,0,0,.65)";
        ctx.fillRect(35, 185, 290, 105);

        ctx.fillStyle = "#ffffff";
        ctx.textAlign = "center";
        ctx.font = "bold 26px Arial";
        ctx.fillText("GAME OVER", 180, 220);

        ctx.font = "18px Arial";
        ctx.fillText("Tap JUMP to restart", 180, 255);
    }
}

</script>

function addBirdPipe() {
    const gap = 145;
    const top = 55 + Math.random() * 185;

    pipes.push({
        x:360,
        top:top,
        bottom:top+gap,
        scored:false
    });
}

function startBirdLoop() {
    if(birdLoopActive) return;

    birdLoopActive = true;
    requestAnimationFrame(updateBirdGame);
}

function updateBirdGame() {
    if(!birdRunning) {
        birdLoopActive = false;
        drawBirdGame();
        return;
    }

    birdFrame++;

    bird.velocity += .38;
    bird.y += bird.velocity;

    if(birdFrame % 95 === 0) {
        addBirdPipe();
    }

    for(const p of pipes) {
        p.x -= 2.3;

        if(!p.scored && p.x+48 < bird.x) {
            birdScore++;
            p.scored = true;
        }

        if(
            bird.x + bird.radius > p.x &&
            bird.x - bird.radius < p.x + 48 &&
            (
                bird.y - bird.radius < p.top ||
                bird.y + bird.radius > p.bottom
            )
        ) {
            birdRunning = false;
        }
    }

    pipes = pipes.filter(function(p) {
        return p.x > -60;
    });

    if(
        bird.y + bird.radius > 480 ||
        bird.y - bird.radius < 0
    ) {
        birdRunning = false;
    }

    drawBirdGame();

    if(birdRunning) {
        requestAnimationFrame(updateBirdGame);
    } else {
        birdLoopActive = false;
    }
}

// INITIAL GAME SETUP
resetBird();

</script>
</body>
</html>
"""

components.html(APP, height=1100, scrolling=True)
