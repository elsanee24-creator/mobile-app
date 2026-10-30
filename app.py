
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
    -webkit-tap-highlight-color: transparent;
}

:root {
    --bg: #07150e;
    --panel: #10251a;
    --card: #183526;
    --text: #f1fff5;
    --muted: #a2b9a9;
    --accent: #39ff88;
    --accent2: #13bd68;
    --border: rgba(57,255,136,.22);
}

body[data-theme="blue"] {
    --bg:#071222;
    --panel:#10243b;
    --card:#193653;
    --text:#eff7ff;
    --muted:#a5bad0;
    --accent:#42baff;
    --accent2:#247ee8;
    --border:rgba(66,186,255,.25);
}

body[data-theme="purple"] {
    --bg:#160d24;
    --panel:#28183c;
    --card:#392450;
    --text:#fff4ff;
    --muted:#c1a9d1;
    --accent:#d58aff;
    --accent2:#984de0;
    --border:rgba(213,138,255,.25);
}

body[data-theme="light"] {
    --bg:#edf5ef;
    --panel:#ffffff;
    --card:#f0f5f1;
    --text:#15251a;
    --muted:#66776b;
    --accent:#159c55;
    --accent2:#087a40;
    --border:rgba(20,120,60,.2);
}

body[data-theme="dark"] {
    --bg:#08090c;
    --panel:#15171c;
    --card:#22252d;
    --text:#f5f5f5;
    --muted:#a5a7ae;
    --accent:#eeeeee;
    --accent2:#a9a9a9;
    --border:rgba(255,255,255,.13);
}

body {
    margin:0;
    padding:12px 5px;
    background:var(--bg);
    color:var(--text);
    font-family:Arial, sans-serif;
    transition:background .25s,color .25s;
}

#phone {
    width:100%;
    max-width:430px;
    min-height:850px;
    margin:auto;
    padding:15px;
    border:2px solid var(--border);
    border-radius:35px;
    background:var(--panel);
    box-shadow:0 15px 45px rgba(0,0,0,.25);
    overflow:hidden;
    position:relative;
}

.topbar {
    display:flex;
    justify-content:space-between;
    align-items:center;
    gap:8px;
    margin-bottom:25px;
}

.logo {
    font-size:21px;
    font-weight:900;
    letter-spacing:-1px;
}

.logo span {
    color:var(--accent);
}

select,input {
    background:var(--card);
    color:var(--text);
    border:1px solid var(--border);
    border-radius:12px;
    padding:11px;
    outline:none;
    font-size:14px;
    max-width:100%;
}

select {
    width:125px;
}

.screen {
    display:none;
    animation:appear .25s ease;
}

.screen.active {
    display:block;
}

@keyframes appear {
    from {opacity:0;transform:translateY(8px)}
    to {opacity:1;transform:translateY(0)}
}

h1 {
    font-size:29px;
    margin:10px 0;
}

h2 {
    font-size:22px;
    margin:8px 0 15px;
}

p {
    color:var(--muted);
    line-height:1.5;
}

.card {
    background:var(--card);
    border:1px solid var(--border);
    padding:17px;
    border-radius:19px;
    margin:12px 0;
}

button {
    cursor:pointer;
    border:0;
    border-radius:14px;
    padding:14px;
    font-size:15px;
    font-weight:bold;
    color:var(--text);
    background:var(--card);
    transition:transform .15s,opacity .15s;
}

button:active {
    transform:scale(.96);
}

.primary {
    color:#06150b;
    background:var(--accent);
    width:100%;
    box-shadow:0 5px 18px rgba(0,0,0,.12);
}

.secondary {
    border:1px solid var(--border);
    width:100%;
}

.back {
    padding:9px 13px;
    margin-bottom:15px;
}

.menu-grid {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:12px;
    margin-top:20px;
}

.menu-btn {
    min-height:115px;
    text-align:left;
    padding:17px;
    border:1px solid var(--border);
    background:var(--card);
}

.menu-btn .emoji {
    display:block;
    font-size:29px;
    margin-bottom:12px;
}

.menu-btn small {
    display:block;
    color:var(--muted);
    margin-top:5px;
    font-weight:normal;
}

input {
    width:100%;
    margin:8px 0;
}

.loading {
    display:none;
    text-align:center;
    padding:25px 5px;
}

.spinner {
    width:38px;
    height:38px;
    border:4px solid var(--border);
    border-top-color:var(--accent);
    border-radius:50%;
    margin:10px auto;
    animation:spin .8s linear infinite;
}

@keyframes spin {
    to {transform:rotate(360deg)}
}

.calc-display {
    min-height:85px;
    background:var(--bg);
    border:1px solid var(--border);
    border-radius:16px;
    padding:17px;
    text-align:right;
    font-size:29px;
    overflow-wrap:anywhere;
    margin-bottom:12px;
}

.calc-grid {
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:8px;
}

.calc-grid button {
    min-height:58px;
    font-size:19px;
}

.calc-grid .operator {
    color:var(--accent);
}

.result {
    font-size:19px;
    font-weight:bold;
    color:var(--accent);
    margin:15px 0;
    overflow-wrap:anywhere;
}

.game-info {
    text-align:center;
    font-size:18px;
    font-weight:bold;
    color:var(--accent);
}

#birdCanvas {
    display:block;
    width:100%;
    max-width:360px;
    height:auto;
    margin:12px auto;
    border-radius:15px;
    border:1px solid var(--border);
    touch-action:manipulation;
    background:#65cfff;
}

.check-row {
    display:flex;
    align-items:center;
    gap:8px;
    margin:12px 0;
    color:var(--text);
}

.check-row input {
    width:auto;
    margin:0;
    accent-color:var(--accent);
}

.footer {
    text-align:center;
    color:var(--muted);
    font-size:12px;
    padding:30px 0 10px;
}

</style>
</head>

<body data-theme="green">

<div id="phone">

    <div class="topbar">
        <div class="logo">mobile<span>.app</span></div>

        <select id="themeSelect" onchange="changeTheme(this.value)">
            <option value="green">Green Neon</option>
            <option value="blue">Blue</option>
            <option value="purple">Purple</option>
            <option value="light">Light</option>
            <option value="dark">Dark</option>
        </select>
    </div>

    <!-- LOGIN -->
    <section id="login" class="screen active">

        <div style="text-align:center;padding:45px 5px 25px">
            <div style="font-size:65px">📱</div>
            <h1>Welcome to <span style="color:var(--accent)">mobile.app</span></h1>
            <p>Your mini digital world.</p>
        </div>

        <div class="card">
            <h2>Get Started</h2>

            <input id="username" placeholder="Enter your name">

            <button class="primary" onclick="loginUser()">
                Login
            </button>

            <div style="height:10px"></div>

            <button class="secondary" onclick="guestUser()">
                Continue as Guest
            </button>
        </div>

        <div id="loginLoading" class="loading">
            <div class="spinner"></div>
            <b id="loadingText">Please wait...</b>
        </div>

        <div class="footer">Made with creativity ✨</div>
    </section>


    <!-- HOME -->
    <section id="home" class="screen">

        <div class="card">
            <p>Welcome back 👋</p>
            <h1 id="welcomeName">User</h1>
            <p>Your tools are ready.</p>
        </div>

        <h2>Explore Apps</h2>

        <div class="menu-grid">

            <button class="menu-btn" onclick="go('calculator')">
                <span class="emoji">🧮</span>
                Calculator
                <small>Calculate anything</small>
            </button>

            <button class="menu-btn" onclick="go('guess')">
                <span class="emoji">🎯</span>
                Number Guess
                <small>Guess the number</small>
            </button>

            <button class="menu-btn" onclick="go('flappy')">
                <span class="emoji">🐦</span>
                Flappy Bird
                <small>Play the game</small>
            </button>

            <button class="menu-btn" onclick="go('password')">
                <span class="emoji">🔐</span>
                Password Generator
                <small>Create passwords</small>
            </button>

        </div>

        <div class="card" style="margin-top:22px">
            <b>✨ mobile.app</b>
            <p>A collection of useful mini tools in one place.</p>
        </div>

        <button class="secondary" onclick="logoutUser()">Logout</button>

    </section>


    <!-- CALCULATOR -->
    <section id="calculator" class="screen">

        <button class="back" onclick="go('home')">← Back</button>

        <h1>Calculator</h1>
        <p>Simple and quick calculations.</p>

        <div class="calc-display" id="calcDisplay">0</div>

        <div class="calc-grid">

            <button class="operator" onclick="calcClear()">AC</button>
            <button class="operator" onclick="calcBack()">⌫</button>
            <button class="operator" onclick="calcPress('%')">%</button>
            <button class="operator" onclick="calcPress('/')">÷</button>

            <button onclick="calcPress('7')">7</button>
            <button onclick="calcPress('8')">8</button>
            <button onclick="calcPress('9')">9</button>
            <button class="operator" onclick="calcPress('*')">×</button>

            <button onclick="calcPress('4')">4</button>
            <button onclick="calcPress('5')">5</button>
            <button onclick="calcPress('6')">6</button>
            <button class="operator" onclick="calcPress('-')">−</button>

            <button onclick="calcPress('1')">1</button>
            <button onclick="calcPress('2')">2</button>
            <button onclick="calcPress('3')">3</button>
            <button class="operator" onclick="calcPress('+')">+</button>

            <button onclick="calcPress('0')">0</button>
            <button onclick="calcPress('00')">00</button>
            <button onclick="calcPress('.')">.</button>
            <button class="primary" onclick="calculateCalc()">=</button>

        </div>
    </section>


    <!-- NUMBER GUESS -->
    <section id="guess" class="screen">

        <button class="back" onclick="go('home')">← Back</button>

        <h1>Number Guess 🎯</h1>
        <p>Guess a secret number between 1 and 100.</p>

        <div class="card">
            <div class="game-info" id="guessAttempts">
                Attempts left: 10
            </div>

            <input
                id="guessInput"
                type="number"
                min="1"
                max="100"
                placeholder="Enter your guess"
            >

            <button class="primary" onclick="checkGuess()">
                Check Number
            </button>

            <div class="result" id="guessMessage">
                Good luck!
            </div>

            <button class="secondary" onclick="resetGuess()">
                New Game
            </button>
        </div>
    </section>


    <!-- FLAPPY BIRD -->
    <section id="flappy" class="screen">

        <button class="back" onclick="go('home')">← Back</button>

        <h1>Flappy Bird 🐦</h1>
        <p>Tap the game area or press Jump to fly.</p>

        <div class="game-info" id="birdScoreText">
            Score: 0
        </div>

        <canvas id="birdCanvas" width="360" height="480"></canvas>

        <button class="primary" onclick="birdJump()">
            JUMP
        </button>

        <div style="height:10px"></div>

        <button class="secondary" onclick="resetBird()">
            Restart Game
        </button>

    </section>


    <!-- PASSWORD GENERATOR -->
    <section id="password" class="screen">

        <button class="back" onclick="go('home')">← Back</button>

        <h1>Password Generator 🔐</h1>
        <p>Create a random password.</p>

        <div class="card">

            <label>Password Length</label>
            <input
                type="number"
                id="passLength"
                min="8"
                max="32"
                value="16"
            >

            <div class="check-row">
                <input type="checkbox" id="passUpper" checked>
                <label for="passUpper">Uppercase letters (A-Z)</label>
            </div>

            <div class="check-row">
                <input type="checkbox" id="passLower" checked>
                <label for="passLower">Lowercase letters (a-z)</label>
            </div>

            <div class="check-row">
                <input type="checkbox" id="passNumbers" checked>
                <label for="passNumbers">Numbers (0-9)</label>
            </div>

            <div class="check-row">
                <input type="checkbox" id="passSymbols" checked>
                <label for="passSymbols">Symbols (!@#$)</label>
            </div>

            <button class="primary" onclick="generatePassword()">
                Generate Password
            </button>

            <input
                id="passwordOutput"
                readonly
                placeholder="Your password appears here"
            >

            <button class="secondary" onclick="copyPassword()">
                Copy Password
            </button>

            <div class="result" id="passwordMessage"></div>

        </div>
    </section>

    <div class="footer">mobile.app • Your digital space</div>

</div>


<script>

// ===========================
// THEME SYSTEM
// ===========================

function changeTheme(theme) {
    document.body.setAttribute("data-theme", theme);
    document.getElementById("themeSelect").value = theme;

    try {
        localStorage.setItem("mobileAppTheme", theme);
    } catch(e) {}
}

try {
    const savedTheme = localStorage.getItem("mobileAppTheme");

    if(savedTheme) {
        changeTheme(savedTheme);
    }
} catch(e) {}


// ===========================
// SCREEN NAVIGATION
// ===========================

function go(screenId) {
    document.querySelectorAll(".screen").forEach(function(screen) {
        screen.classList.remove("active");
    });

    const target = document.getElementById(screenId);

    if(target) {
        target.classList.add("active");
    }

    if(screenId === "flappy") {
        if(!birdStarted || !birdRunning) {
            resetBird();
        } else {
            startBirdLoop();
            drawBirdGame();
        }
    }
}


// ===========================
// LOGIN AND GUEST
// ===========================

function startLogin(name) {
    document.getElementById("loginLoading").style.display = "block";
    document.getElementById("loadingText").textContent =
        "Preparing your experience...";

    document.querySelectorAll("#login .card button").forEach(function(btn) {
        btn.disabled = true;
        btn.style.opacity = ".5";
    });

    setTimeout(function() {
        document.getElementById("welcomeName").textContent = name;
        document.getElementById("loginLoading").style.display = "none";

        document.querySelectorAll("#login .card button").forEach(function(btn) {
            btn.disabled = false;
            btn.style.opacity = "1";
        });

        go("home");
    }, 1200);
}

function loginUser() {
    const name = document.getElementById("username").value.trim();

    if(!name) {
        alert("Please enter your name.");
        return;
    }

    startLogin(name);
}

function guestUser() {
    startLogin("Guest");
}

function logoutUser() {
    go("login");
}


// ===========================
// CALCULATOR
// ===========================

let calcExpression = "";

function updateCalc() {
    document.getElementById("calcDisplay").textContent =
        calcExpression || "0";
}

function calcPress(value) {
    if(calcExpression.length > 35) return;

    calcExpression += value;
    updateCalc();
}

function calcClear() {
    calcExpression = "";
    updateCalc();
}

function calcBack() {
    calcExpression = calcExpression.slice(0, -1);
    updateCalc();
}

function calculateCalc() {
    if(!calcExpression) return;

    try {
        if(!/^[0-9+\-*/%.() ]+$/.test(calcExpression)) {
            throw new Error("Invalid");
        }

        const result = Function(
            '"use strict"; return (' + calcExpression + ')'
        )();

        if(!Number.isFinite(result)) {
            throw new Error("Invalid");
        }

        calcExpression = String(
            Number(result.toFixed(10))
        );

        updateCalc();

    } catch(e) {
        document.getElementById("calcDisplay").textContent =
            "Error";

        calcExpression = "";
    }
}


// ===========================
// NUMBER GUESSING GAME
// ===========================

let secretNumber = Math.floor(Math.random() * 100) + 1;
let attemptsLeft = 10;
let guessFinished = false;

function resetGuess() {
    secretNumber = Math.floor(Math.random() * 100) + 1;
    attemptsLeft = 10;
    guessFinished = false;

    document.getElementById("guessInput").value = "";
    document.getElementById("guessMessage").textContent = "Good luck!";
    document.getElementById("guessAttempts").textContent =
        "Attempts left: 10";
}

function checkGuess() {
    if(guessFinished) return;

    const input = document.getElementById("guessInput");
    const guess = Number(input.value);
    const message = document.getElementById("guessMessage");

    if(!input.value || !Number.isInteger(guess) || guess < 1 || guess > 100) {
        message.textContent = "Enter a number from 1 to 100.";
        return;
    }

    attemptsLeft--;

    if(guess === secretNumber) {
        message.textContent = "🎉 Correct! You won!";
        guessFinished = true;
    } else if(attemptsLeft <= 0) {
        message.textContent = "Game over! Number was " + secretNumber;
        guessFinished = true;
    } else if(guess < secretNumber) {
        message.textContent = "Too low! Try a higher number.";
    } else {
        message.textContent = "Too high! Try a lower number.";
    }

    document.getElementById("guessAttempts").textContent =
        "Attempts left: " + attemptsLeft;

    input.value = "";
}


// ===========================
// PASSWORD GENERATOR
// ===========================

function secureRandom(max) {
    const values = new Uint32Array(1);
    crypto.getRandomValues(values);
    return values[0] % max;
}

function generatePassword() {
    const length = Number(document.getElementById("passLength").value);

    if(!Number.isInteger(length) || length < 8 || length > 32) {
        document.getElementById("passwordMessage").textContent =
            "Choose a length between 8 and 32.";
        return;
    }

    let groups = [];

    if(document.getElementById("passUpper").checked) {
        groups.push("ABCDEFGHIJKLMNOPQRSTUVWXYZ");
    }

    if(document.getElementById("passLower").checked) {
        groups.push("abcdefghijklmnopqrstuvwxyz");
    }

    if(document.getElementById("passNumbers").checked) {
        groups.push("0123456789");
    }

    if(document.getElementById("passSymbols").checked) {
        groups.push("!@#$%&*?");
    }

    if(groups.length === 0) {
        document.getElementById("passwordMessage").textContent =
            "Select at least one character group.";
        return;
    }

    let allCharacters = groups.join("");
    let password = "";

    // Include at least one character from each selected group.
    groups.forEach(function(group) {
        password += group[secureRandom(group.length)];
    });

    while(password.length < length) {
        password += allCharacters[secureRandom(allCharacters.length)];
    }

    // Shuffle characters.
    let chars = password.split("");

    for(let i = chars.length - 1; i > 0; i--) {
        const j = secureRandom(i + 1);
        [chars[i], chars[j]] = [chars[j], chars[i]];
    }

    password = chars.join("");

    document.getElementById("passwordOutput").value = password;
    document.getElementById("passwordMessage").textContent =
        "Password generated successfully.";
}

async function copyPassword() {
    const output = document.getElementById("passwordOutput");

    if(!output.value) {
        document.getElementById("passwordMessage").textContent =
            "Generate a password first.";
        return;
    }

    try {
        await navigator.clipboard.writeText(output.value);
        document.getElementById("passwordMessage").textContent =
            "Password copied!";
    } catch(e) {
        output.select();
        document.execCommand("copy");
        document.getElementById("passwordMessage").textContent =
            "Copy attempted. Please check the field.";
    }
}


// ===========================
// FLAPPY BIRD ENGINE
// ===========================

const canvas = document.getElementById("birdCanvas");
const ctx = canvas.getContext("2d");

const GAME_WIDTH = 360;
const GAME_HEIGHT = 480;

let bird = {
    x: 78,
    y: 220,
    velocity: 0,
    radius: 13
};

let pipes = [];
let birdScore = 0;
let birdFrame = 0;
let birdRunning = false;
let birdStarted = false;
let birdLoopActive = false;
let birdAnimationId = null;

const birdGravity = 0.38;
const birdJumpPower = -6.5;
const pipeSpeed = 2.3;
const pipeGap = 150;
const pipeWidth = 48;


// Reset game
function resetBird() {
    if(birdAnimationId !== null) {
        cancelAnimationFrame(birdAnimationId);
        birdAnimationId = null;
    }

    bird.x = 78;
    bird.y = 220;
    bird.velocity = 0;

    pipes = [];
    birdScore = 0;
    birdFrame = 0;

    birdRunning = true;
    birdStarted = true;
    birdLoopActive = false;

    document.getElementById("birdScoreText").textContent = "Score: 0";

    drawBirdGame();
    startBirdLoop();
}


// Jump
function birdJump() {
    if(!birdStarted || !birdRunning) {
        resetBird();
    }

    bird.velocity = birdJumpPower;
}


// Create pipes
function addBirdPipe() {
    const top = 55 + Math.random() * 180;

    pipes.push({
        x: GAME_WIDTH,
        top: top,
        bottom: top + pipeGap,
        scored: false
    });
}


// Draw game
function drawBirdGame() {
    ctx.clearRect(0, 0, GAME_WIDTH, GAME_HEIGHT);

    const sky = ctx.createLinearGradient(0, 0, 0, GAME_HEIGHT);
    sky.addColorStop(0, "#65cfff");
    sky.addColorStop(1, "#d8f5ff");

    ctx.fillStyle = sky;
    ctx.fillRect(0, 0, GAME_WIDTH, GAME_HEIGHT);

    // Clouds
    ctx.fillStyle = "rgba(255,255,255,.85)";

    function drawCloud(x, y) {
        ctx.beginPath();
        ctx.arc(x, y, 17, 0, Math.PI * 2);
        ctx.arc(x + 22, y - 8, 23, 0, Math.PI * 2);
        ctx.arc(x + 45, y, 17, 0, Math.PI * 2);
        ctx.fill();
    }

    drawCloud(40, 75);
    drawCloud(235, 140);

    // Pipes
    for(const p of pipes) {
        ctx.fillStyle = "#159447";

        ctx.fillRect(p.x, 0, pipeWidth, p.top);
        ctx.fillRect(
            p.x,
            p.bottom,
            pipeWidth,
            GAME_HEIGHT - p.bottom
        );

        ctx.fillStyle = "#087638";

        ctx.fillRect(p.x - 4, p.top - 12, pipeWidth + 8, 12);
        ctx.fillRect(p.x - 4, p.bottom, pipeWidth + 8, 12);
    }

    // Ground
    ctx.fillStyle = "#d4ad54";
    ctx.fillRect(0, 465, GAME_WIDTH, 15);

    ctx.fillStyle = "#65b945";
    ctx.fillRect(0, 460, GAME_WIDTH, 7);

    // Bird
    ctx.fillStyle = "#ffdf38";

    ctx.beginPath();
    ctx.arc(bird.x, bird.y, bird.radius, 0, Math.PI * 2);
    ctx.fill();

    // Wing
    ctx.fillStyle = "#ffad24";

    ctx.beginPath();
    ctx.ellipse(
        bird.x - 5,
        bird.y + 4,
        7,
        4,
        -.3,
        0,
        Math.PI * 2
    );
    ctx.fill();

    // Eye
    ctx.fillStyle = "#ffffff";

    ctx.beginPath();
    ctx.arc(bird.x + 5, bird.y - 4, 4, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = "#111111";

    ctx.beginPath();
    ctx.arc(bird.x + 6, bird.y - 4, 2, 0, Math.PI * 2);
    ctx.fill();

    // Beak
    ctx.fillStyle = "#ff7a21";

    ctx.beginPath();
    ctx.moveTo(bird.x + 12, bird.y);
    ctx.lineTo(bird.x + 23, bird.y + 4);
    ctx.lineTo(bird.x + 12, bird.y + 7);
    ctx.fill();

    document.getElementById("birdScoreText").textContent =
        "Score: " + birdScore;

    // Game over
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


// Collision detection
function checkBirdCollision(p) {
    const horizontal =
        bird.x + bird.radius > p.x &&
        bird.x - bird.radius < p.x + pipeWidth;

    const vertical =
        bird.y - bird.radius < p.top ||
        bird.y + bird.radius > p.bottom;

    return horizontal && vertical;
}


// Start loop
function startBirdLoop() {
    if(birdLoopActive) return;

    birdLoopActive = true;
    birdAnimationId = requestAnimationFrame(updateBirdGame);
}


// Update game
function updateBirdGame() {
    if(!birdRunning) {
        birdLoopActive = false;
        birdAnimationId = null;
        drawBirdGame();
        return;
    }

    birdFrame++;

    bird.velocity += birdGravity;
    bird.y += bird.velocity;

    if(birdFrame % 95 === 0) {
        addBirdPipe();
    }

    for(const p of pipes) {
        p.x -= pipeSpeed;

        if(!p.scored && p.x + pipeWidth < bird.x) {
            birdScore++;
            p.scored = true;
        }

        if(checkBirdCollision(p)) {
            birdRunning = false;
        }
    }

    pipes = pipes.filter(function(p) {
        return p.x > -60;
    });

    if(
        bird.y + bird.radius > 460 ||
        bird.y - bird.radius < 0
    ) {
        birdRunning = false;
    }

    drawBirdGame();

    if(birdRunning) {
        birdAnimationId = requestAnimationFrame(updateBirdGame);
    } else {
        birdLoopActive = false;
        birdAnimationId = null;
    }
}


// Mobile touch controls
canvas.addEventListener("pointerdown", function(event) {
    event.preventDefault();

    if(document.getElementById("flappy").classList.contains("active")) {
        birdJump();
    }
});


// Keyboard controls
document.addEventListener("keydown", function(event) {
    if(event.code === "Space") {
        if(document.getElementById("flappy").classList.contains("active")) {
            event.preventDefault();
            birdJump();
        }
    }
});


// Initial game display
birdStarted = false;
birdRunning = false;
drawBirdGame();

</script>

</body>
</html>
"""

components.html(APP, height=1050, scrolling=True)

 
