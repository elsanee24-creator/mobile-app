
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
}

body {
    font-family: Arial, sans-serif;
    background: #061b18;
    color: white;
}

:root {
    --bg: #061b18;
    --panel: #0c2924;
    --accent: #00ff9d;
    --text: #ffffff;
    --muted: #a6c8bb;
}

body.blue {
    --bg: #071426;
    --panel: #102744;
    --accent: #39aaff;
}

body.purple {
    --bg: #180d29;
    --panel: #2c1944;
    --accent: #c084fc;
}

body.light {
    --bg: #edf4f2;
    --panel: #ffffff;
    --accent: #008c65;
    --text: #13251f;
    --muted: #52665d;
}

body.dark {
    --bg: #090909;
    --panel: #191919;
    --accent: #dddddd;
}

.app {
    min-height: 100vh;
    padding: 20px;
    background:
        radial-gradient(circle at 15% 10%, #00ff9d20, transparent 35%),
        radial-gradient(circle at 90% 85%, #00bfff20, transparent 35%),
        var(--bg);
    color: var(--text);
}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 25px;
}

.logo {
    font-size: 25px;
    font-weight: bold;
    color: var(--accent);
    letter-spacing: 1px;
}

.theme-select {
    background: var(--panel);
    color: var(--text);
    border: 1px solid var(--accent);
    border-radius: 10px;
    padding: 9px;
    outline: none;
}

.panel {
    background: var(--panel);
    border: 1px solid #ffffff20;
    border-radius: 20px;
    padding: 20px;
    margin-bottom: 18px;
    box-shadow: 0 8px 30px #00000025;
}

button {
    border: none;
    border-radius: 12px;
    padding: 13px;
    background: var(--accent);
    color: #061b18;
    font-weight: bold;
    cursor: pointer;
    font-size: 15px;
}

input {
    width: 100%;
    padding: 14px;
    margin: 9px 0;
    border-radius: 11px;
    border: 1px solid #ffffff30;
    background: var(--bg);
    color: var(--text);
    outline: none;
}

button:active {
    transform: scale(.97);
}

.hidden {
    display: none !important;
}

.clock-circle {
    width: 210px;
    height: 210px;
    border-radius: 50%;
    border: 3px solid var(--accent);
    box-shadow:
        0 0 15px var(--accent),
        inset 0 0 20px #00ff9d20;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 25px auto;
}

.clock-time {
    font-size: 32px;
    font-weight: bold;
    color: var(--accent);
}

.clock-date {
    font-size: 13px;
    margin-top: 10px;
    color: var(--muted);
}

.center {
    text-align: center;
}

.full {
    width: 100%;
    margin-top: 10px;
}

.grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 12px;
}

.app-button {
    min-height: 100px;
    font-size: 17px;
    background: var(--panel);
    color: var(--text);
    border: 1px solid var(--accent);
}

.message {
    margin-top: 12px;
    color: var(--accent);
    text-align: center;
    min-height: 20px;
}

</style>
</head>

<body>
<div class="app" id="mainApp">

<div class="header">
    <div class="logo">mobile.app</div>

    <select class="theme-select" id="themeSelect">
        <option value="green">Green Neon</option>
        <option value="blue">Blue</option>
        <option value="purple">Purple</option>
        <option value="light">Light</option>
        <option value="dark">Dark</option>
    </select>
</div>

<div id="loginScreen" class="center">

    <div class="panel">
        <h2>Welcome 👋</h2>
        <p style="color:var(--muted);margin-top:8px">
            Your personal mini application
        </p>

        <div class="clock-circle">
            <div class="clock-time" id="clockTime">
                --:--:--
            </div>
            <div class="clock-date" id="clockDate">
                Loading date...
            </div>
        </div>

        <h3>Login</h3>

        <input
            id="username"
            type="text"
            placeholder="Enter your username"
        >

        <input
            id="password"
            type="password"
            placeholder="Enter your password"
        >

        <button class="full" onclick="login()">
            Login
        </button>

        <button class="full" onclick="guestLogin()">
            Continue as Guest
        </button>

        <div class="message" id="loginMessage"></div>
    </div>

</div>

<div id="homeScreen" class="hidden">

    <div class="panel center">
        <h2 id="welcomeText">Welcome!</h2>
        <p style="color:var(--muted);margin-top:8px">
            Select an application
        </p>
    </div>

    <div class="grid">

        <button class="app-button" onclick="openApp('calculator')">
            🧮<br>Calculator
        </button>

        <button class="app-button" onclick="openApp('guess')">
            🎯<br>Number Guess
        </button>

        <button class="app-button" onclick="openApp('password')">
            🔐<br>Password Generator
        </button>

        <button class="app-button" onclick="openApp('flappy')">
            🐦<br>Flappy Bird
        </button>

    </div>

    <button class="full" onclick="logout()">
        Logout
    </button>

</div>

<script>
let currentUser = "Guest";
let currentApp = "";

function updateClock() {
    const now = new Date();

    document.getElementById("clockTime").textContent =
        now.toLocaleTimeString("en-US", {
            hour: "2-digit",
            minute: "2-digit",
            second: "2-digit"
        });

    document.getElementById("clockDate").textContent =
        now.toLocaleDateString("en-US", {
            weekday: "long",
            day: "numeric",
            month: "long",
            year: "numeric"
        });
}

updateClock();
setInterval(updateClock, 1000);

document.getElementById("themeSelect").addEventListener("change", function() {
    document.body.className = this.value;
});

function login() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value;

    const message = document.getElementById("loginMessage");

    if (username === "" || password === "") {
        message.textContent = "Please enter username and password.";
        return;
    }

    currentUser = username;
    showHome();
}

function guestLogin() {
    currentUser = "Guest";
    showHome();
}

function showHome() {
    document.getElementById("loginScreen").classList.add("hidden");
    document.getElementById("homeScreen").classList.remove("hidden");

    document.getElementById("welcomeText").textContent =
        "Welcome, " + currentUser + "!";
}

function logout() {
    document.getElementById("homeScreen").classList.add("hidden");
    document.getElementById("loginScreen").classList.remove("hidden");

    document.getElementById("username").value = "";
    document.getElementById("password").value = "";
    document.getElementById("loginMessage").textContent = "";

    currentUser = "Guest";
}

function openApp(name) {
    currentApp = name;

    document.getElementById("homeScreen").classList.add("hidden");

    const screen = document.getElementById(name + "Screen");

    if (screen) {
        screen.classList.remove("hidden");
    }
}

function goHome() {
    document.querySelectorAll(".tool-screen").forEach(function(screen) {
        screen.classList.add("hidden");
    });

    document.getElementById("homeScreen").classList.remove("hidden");

    currentApp = "";
}
</script>

<!-- CALCULATOR -->
<div id="calculatorScreen" class="tool-screen hidden">

    <div class="panel">
        <h2>🧮 Calculator</h2>

        <input id="calcDisplay" type="text"
        placeholder="Enter calculation" readonly>

        <div class="grid">
            <button onclick="calcPress('7')">7</button>
            <button onclick="calcPress('8')">8</button>
            <button onclick="calcPress('9')">9</button>
            <button onclick="calcPress('/')">÷</button>

            <button onclick="calcPress('4')">4</button>
            <button onclick="calcPress('5')">5</button>
            <button onclick="calcPress('6')">6</button>
            <button onclick="calcPress('*')">×</button>

            <button onclick="calcPress('1')">1</button>
            <button onclick="calcPress('2')">2</button>
            <button onclick="calcPress('3')">3</button>
            <button onclick="calcPress('-')">−</button>

            <button onclick="calcPress('0')">0</button>
            <button onclick="calcPress('.')">.</button>
            <button onclick="calculate()">=</button>
            <button onclick="calcPress('+')">+</button>
        </div>

        <button class="full" onclick="clearCalc()">Clear</button>
        <button class="full" onclick="goHome()">Back to Home</button>

        <div class="message" id="calcMessage"></div>
    </div>
</div>

<!-- NUMBER GUESS -->
<div id="guessScreen" class="tool-screen hidden">
    <div class="panel center">
        <h2>🎯 Number Guess</h2>

        <p style="margin:15px 0">
            Guess a number between 1 and 100.
        </p>

        <input id="guessInput" type="number"
        placeholder="Enter your guess">

        <button class="full" onclick="checkGuess()">
            Check Guess
        </button>

        <div class="message" id="guessMessage"></div>

        <button class="full" onclick="resetGuess()">
            New Game
        </button>

        <button class="full" onclick="goHome()">
            Back to Home
        </button>
    </div>
</div>

<!-- PASSWORD GENERATOR -->
<div id="passwordScreen" class="tool-screen hidden">
    <div class="panel center">
        <h2>🔐 Password Generator</h2>

        <p style="margin:15px 0">
            Choose password length
        </p>

        <input id="passLength" type="number"
        min="6" max="40" value="12">

        <button class="full" onclick="generatePassword()">
            Generate Password
        </button>

        <input id="generatedPassword"
        placeholder="Your password will appear here"
        readonly>

        <button class="full" onclick="copyPassword()">
            Copy Password
        </button>

        <div class="message" id="passMessage"></div>

        <button class="full" onclick="goHome()">
            Back to Home
        </button>
    </div>
</div>

<!-- FLAPPY BIRD SCREEN -->
<div id="flappyScreen" class="tool-screen hidden">
    <div class="panel center">
        <h2>🐦 Flappy Bird</h2>

        <p style="margin:12px">
            Tap the button to play.
        </p>

        <canvas id="birdCanvas"
        width="320" height="420"
        style="width:100%;max-width:320px;
        background:#80d8ff;border-radius:15px">
        </canvas>

        <button class="full" onclick="birdJump()">
            TAP TO FLY
        </button>

        <div class="message" id="birdMessage">
            Press Start to begin.
        </div>

        <button class="full" onclick="startBird()">
            Start Game
        </button>

        <button class="full" onclick="goHome()">
            Back to Home
        </button>
    </div>
</div>
</div>

<script>
/* CALCULATOR */
let calcExpression = "";

function calcPress(value) {
    calcExpression += value;
    document.getElementById("calcDisplay").value =
        calcExpression;
}

function clearCalc() {
    calcExpression = "";
    document.getElementById("calcDisplay").value = "";
    document.getElementById("calcMessage").textContent = "";
}

function calculate() {
    const display = document.getElementById("calcDisplay");
    const message = document.getElementById("calcMessage");

    try {
        if (!calcExpression ||
            !/^[0-9+*/%.() -]+$/.test(calcExpression)) {
            throw new Error("Invalid expression");
        }

        const result = Function(
            '"use strict"; return (' + calcExpression + ')'
        )();

        if (!Number.isFinite(result)) {
            throw new Error("Invalid result");
        }

        calcExpression = String(result);
        display.value = calcExpression;
        message.textContent = "Calculation complete!";
    } catch (error) {
        message.textContent = "Invalid calculation!";
    }
}

/* NUMBER GUESS */
let secretNumber = Math.floor(Math.random() * 100) + 1;
let guessAttempts = 0;

function checkGuess() {
    const input = document.getElementById("guessInput");
    const message = document.getElementById("guessMessage");
    const guess = Number(input.value);

    if (!input.value || guess < 1 || guess > 100) {
        message.textContent = "Enter a number from 1 to 100.";
        return;
    }

    guessAttempts++;

    if (guess === secretNumber) {
        message.textContent =
            "Correct! You won in " + guessAttempts + " attempts!";
    } else if (guess < secretNumber) {
        message.textContent = "Try a HIGHER number!";
    } else {
        message.textContent = "Try a LOWER number!";
    }
}

function resetGuess() {
    secretNumber = Math.floor(Math.random() * 100) + 1;
    guessAttempts = 0;

    document.getElementById("guessInput").value = "";
    document.getElementById("guessMessage").textContent =
        "New game started!";
}

/* PASSWORD GENERATOR */
function generatePassword() {
    const length = Number(
        document.getElementById("passLength").value
    );

    const message = document.getElementById("passMessage");

    if (!Number.isInteger(length) || length < 6 || length > 40) {
        message.textContent = "Choose a length from 6 to 40.";
        return;
    }

    const chars =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*";

    let password = "";

    const randomValues = new Uint32Array(length);
    crypto.getRandomValues(randomValues);

    for (let i = 0; i < length; i++) {
        password += chars[randomValues[i] % chars.length];
    }

    document.getElementById("generatedPassword").value =
        password;

    message.textContent = "Password generated!";
}

async function copyPassword() {
    const password =
        document.getElementById("generatedPassword").value;

    const message = document.getElementById("passMessage");

    if (!password) {
        message.textContent = "Generate a password first!";
        return;
    }

    try {
        await navigator.clipboard.writeText(password);
        message.textContent = "Password copied!";
    } catch (error) {
        message.textContent = "Copy unavailable on this browser.";
    }
}

/* FLAPPY BIRD */
const birdCanvas = document.getElementById("birdCanvas");
const birdCtx = birdCanvas.getContext("2d");

let birdY = 200;
let birdVelocity = 0;
let birdScore = 0;
let birdRunning = false;
let birdFrame = 0;
let birdPipes = [];

function drawBird() {
    birdCtx.clearRect(0, 0, 320, 420);

    birdCtx.fillStyle = "#80d8ff";
    birdCtx.fillRect(0, 0, 320, 420);

    birdCtx.fillStyle = "#ffffff";
    birdCtx.font = "bold 24px Arial";
    birdCtx.fillText("Score: " + birdScore, 15, 35);

    birdCtx.fillStyle = "#22aa55";

    birdPipes.forEach(function(pipe) {
        birdCtx.fillRect(pipe.x, 0, 48, pipe.top);
        birdCtx.fillRect(
            pipe.x,
            pipe.top + 125,
            48,
            420 - pipe.top - 125
        );
    });

    birdCtx.fillStyle = "#ffcc33";
    birdCtx.beginPath();
    birdCtx.arc(75, birdY, 15, 0, Math.PI * 2);
    birdCtx.fill();

    birdCtx.fillStyle = "#ffffff";
    birdCtx.beginPath();
    birdCtx.arc(80, birdY - 4, 4, 0, Math.PI * 2);
    birdCtx.fill();
}

function startBird() {
    birdY = 200;
    birdVelocity = 0;
    birdScore = 0;
    birdFrame = 0;
    birdPipes = [];
    birdRunning = true;

    document.getElementById("birdMessage").textContent =
        "Game started! Tap to fly.";

    drawBird();
    requestAnimationFrame(birdLoop);
}

function birdJump() {
    if (!birdRunning) {
        startBird();
    }

    birdVelocity = -6;
}

function birdLoop() {
    if (!birdRunning) return;

    birdFrame++;
    birdVelocity += 0.28;
    birdY += birdVelocity;

    if (birdFrame % 95 === 0) {
        birdPipes.push({
            x: 320,
            top: 60 + Math.random() * 180,
            scored: false
        });
    }

    birdPipes.forEach(function(pipe) {
        pipe.x -= 2;

        if (!pipe.scored && pipe.x + 48 < 75) {
            pipe.scored = true;
            birdScore++;
        }

        const hitX = 75 + 15 > pipe.x &&
                     75 - 15 < pipe.x + 48;

        const hitY = birdY - 15 < pipe.top ||
                     birdY + 15 > pipe.top + 125;

        if (hitX && hitY) {
            birdRunning = false;
        }
    });

    birdPipes = birdPipes.filter(function(pipe) {
        return pipe.x > -60;
    });

    if (birdY < 15 || birdY > 405) {
        birdRunning = false;
    }

    drawBird();

    if (birdRunning) {
        requestAnimationFrame(birdLoop);
    } else {
        document.getElementById("birdMessage").textContent =
            "Game Over! Score: " + birdScore +
            ". Press Start Game to play again.";
    }
}

/* INITIAL SCREEN */
updateClock();
</script>
</div>
</body>
</html>
"""

components.html(APP, height=1050, scrolling=True)





