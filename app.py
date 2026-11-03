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
}

:root {
    --bg: #071b17;
    --panel: #102b25;
    --panel2: #16382f;
    --green: #62e6a4;
    --gold: #e8c77b;
    --text: #f4f4e9;
    --muted: #a9c1b6;
    --line: #315348;
}

body {
    margin: 0;
    padding: 16px 10px;
    min-height: 100vh;
    color: var(--text);
    font-family: Arial, sans-serif;

    background:
        radial-gradient(
            ellipse at 12% 10%,
            rgba(39, 135, 96, .48),
            transparent 36%
        ),
        radial-gradient(
            ellipse at 90% 85%,
            rgba(190, 145, 65, .20),
            transparent 32%
        ),
        radial-gradient(
            ellipse at 55% 45%,
            rgba(24, 85, 68, .25),
            transparent 50%
        ),
        linear-gradient(
            145deg,
            #020b09,
            #09231c 48%,
            #101d19
        );

    background-attachment: fixed;
}

#phone {
    max-width: 440px;
    min-height: 720px;
    margin: auto;
    padding: 17px;

    border: 1px solid rgba(145, 205, 175, .38);
    border-radius: 34px;

    background:
        linear-gradient(
            145deg,
            rgba(20, 55, 44, .97),
            rgba(5, 20, 17, .98)
        );

    box-shadow:
        0 25px 75px rgba(0,0,0,.55),
        0 0 35px rgba(66, 190, 133, .10),
        inset 0 0 30px rgba(255,255,255,.025);

    overflow: hidden;
}

.topline {
    display: flex;
    justify-content: space-between;
    align-items: center;
    color: var(--muted);
    font-size: 12px;
    margin-bottom: 18px;
}

.brand {
    font-size: 13px;
    letter-spacing: 3px;
    color: var(--gold);
    font-weight: bold;
}

#clock {
    font-size: 14px;
    font-weight: bold;
    color: var(--green);
    letter-spacing: 1px;
}

.screen {
    display: none;
    animation: appear .22s ease;
}

.screen.active {
    display: block;
}

@keyframes appear {
    from {
        opacity: 0;
        transform: translateY(7px);
    }
    to {
        opacity: 1;
        transform: none;
    }
}

.logo {
    width: 68px;
    height: 68px;
    margin: 20px auto 15px;
    border-radius: 22px;

    display: grid;
    place-items: center;

    font-size: 35px;
    font-weight: bold;
    color: #09251b;

    background: linear-gradient(
        135deg,
        #a5f4c8,
        #d7bd79
    );

    box-shadow: 0 8px 30px #62e6a433;
}

.center {
    text-align: center;
    padding: 38px 8px;
}

h1 {
    font-size: 27px;
    margin: 12px 0 7px;
}

h2 {
    font-size: 20px;
    margin: 10px 0 16px;
}

p {
    color: var(--muted);
    line-height: 1.5;
}

input,
textarea {
    width: 100%;
    padding: 14px;
    margin: 8px 0;

    border-radius: 13px;
    border: 1px solid var(--line);

    background: #071a15;
    color: var(--text);

    outline: none;
    font-size: 15px;
}

input:focus,
textarea:focus {
    border-color: var(--green);
    box-shadow: 0 0 0 2px rgba(98,230,164,.10);
}

textarea {
    resize: vertical;
}

button {
    border: 0;
    border-radius: 13px;
    padding: 13px 15px;

    font-size: 14px;
    font-weight: bold;
    cursor: pointer;

    transition: transform .12s, filter .12s;
}

button:active {
    transform: scale(.97);
    filter: brightness(1.15);
}

.primary {
    width: 100%;
    background: linear-gradient(
        110deg,
        #62e6a4,
        #b8d78c
    );

    color: #092219;
    margin-top: 10px;
}

.secondary {
    width: 100%;
    background: #18372e;
    color: var(--text);
    border: 1px solid #45695b;
    margin-top: 9px;
}

.back {
    background: #18372e;
    color: var(--green);
    padding: 9px 13px;
}

.header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 8px 0 20px;
}

.header h2 {
    margin: 0;
}

.card {
    background: linear-gradient(
        145deg,
        #17382f,
        #0d241e
    );

    border: 1px solid var(--line);
    border-radius: 19px;
    padding: 17px;
    margin: 12px 0;
}

.grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

.tile {
    min-height: 105px;

    background: linear-gradient(
        145deg,
        #1b4034,
        #10271f
    );

    border: 1px solid #31594a;
    color: var(--text);

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 9px;

    padding: 12px 5px;
}

.tile span:first-child {
    font-size: 25px;
}

.tile span:last-child {
    font-size: 12px;
}

/* GAMING HUB FEATURE CARD */

.gaming-feature {
    width: 100%;
    min-height: 145px;
    margin-top: 15px;
    padding: 18px;

    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 17px;

    text-align: left;

    border-radius: 22px;
    border: 1px solid rgba(115, 220, 169, .45);

    color: var(--text);

    background:
        radial-gradient(
            circle at 15% 15%,
            rgba(98,230,164,.25),
            transparent 55%
        ),
        linear-gradient(
            125deg,
            #174b39,
            #10271f 75%
        );

    box-shadow:
        0 10px 28px rgba(0,0,0,.22),
        inset 0 0 20px rgba(255,255,255,.025);
}

.gaming-icon {
    width: 76px;
    height: 76px;
    flex-shrink: 0;

    display: grid;
    place-items: center;

    border-radius: 23px;
    font-size: 39px;

    background: linear-gradient(
        145deg,
        #a5f4c8,
        #d7bd79
    );

    box-shadow: 0 6px 25px rgba(98,230,164,.20);
}

.gaming-info strong {
    display: block;
    font-size: 19px;
    margin-bottom: 6px;
}

.gaming-info small {
    display: block;
    color: #b8d4c6;
    font-size: 12px;
    line-height: 1.5;
}

/* SETTINGS AND ABOUT ROWS */

.home-row {
    width: 100%;
    min-height: 54px;
    margin-top: 9px;
    padding: 13px 15px;

    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 12px;

    background: linear-gradient(
        110deg,
        #17382f,
        #10271f
    );

    color: var(--text);
    border: 1px solid var(--line);
    text-align: left;
}

.home-row span:first-child {
    font-size: 20px;
}

/* GAME MENU */

.gamegrid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 11px;
}

.gamecard {
    min-height: 100px;

    background: linear-gradient(
        145deg,
        #1a4234,
        #10271f
    );

    color: var(--text);
    border: 1px solid #426454;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
}

.gamecard span:first-child {
    font-size: 27px;
}

/* CALCULATOR */

.display {
    background: #061510;
    border: 1px solid var(--line);
    border-radius: 15px;

    padding: 20px;
    text-align: right;
    font-size: 29px;
    min-height: 75px;

    overflow-wrap: anywhere;
    margin-bottom: 12px;
}

.calcgrid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 8px;
}

.calcgrid button {
    background: #1c3a30;
    color: white;
    padding: 17px 4px;
    font-size: 17px;
}

.calcgrid .op {
    background: #9c7b3f;
    color: #fff;
}

.calcgrid .special {
    background: #31584a;
}

.calcgrid .equal {
    background: #68dba0;
    color: #092219;
}

.calcgrid .zero {
    grid-column: span 2;
}

.output {
    padding: 15px;
    background: #071a15;
    border: 1px solid var(--line);
    border-radius: 12px;
    overflow-wrap: anywhere;
    margin: 12px 0;
}

.option {
    display: flex;
    align-items: center;
    gap: 10px;
    margin: 12px 0;
    color: var(--muted);
}

.option input {
    width: auto;
    margin: 0;
}

.stats {
    display: flex;
    justify-content: space-around;
    gap: 8px;
    text-align: center;
}

.stats strong {
    display: block;
    color: var(--gold);
    font-size: 20px;
}

canvas {
    width: 100%;
    display: block;
    background: #8bd8dc;
    border-radius: 15px;
    border: 1px solid #527568;
    touch-action: manipulation;
}

#snakeCanvas {
    background: #102e25;
    touch-action: none;
}

.message {
    text-align: center;
    min-height: 24px;
    color: var(--gold);
}

.footer {
    text-align: center;
    color: #79998a;
    font-size: 11px;
    margin: 22px 0 5px;
}

.hidden {
    display: none !important;
}

@media(max-width:380px) {
    body {
        padding: 5px;
    }

    #phone {
        padding: 13px;
        border-radius: 25px;
    }

    .grid {
        gap: 7px;
    }

    .tile {
        min-height: 95px;
    }
}
</style>
</head>

<body>
<div id="phone">

    <div class="topline">
        <span class="brand">MOBILE.APP</span>
        <span id="clock">--:--:--</span>
    </div>

    <!-- LOGIN -->
    <section id="login" class="screen active">
        <div class="center">

            <div class="clock-display">
                <div class="clock-face">◷</div>
                <div id="loginClock" class="login-clock">--:--:--</div>
                <div id="loginDate" class="login-date">Loading date...</div>
            </div>

            <h1>Welcome Back</h1>
            <p>Your personal mobile experience</p>

            <input
                id="username"
                placeholder="Enter your name"
                autocomplete="off"
            >

            <button class="primary" onclick="loginUser()">
                Login
            </button>

            <button class="secondary" onclick="guestLogin()">
                Explore as Guest
            </button>

        </div>
    </section>

    <!-- PIN LOCK -->
    <section id="lock" class="screen">
        <div class="center">

            <div class="logo">M</div>

            <h1>App Locked</h1>
            <p>Enter your PIN to continue</p>

            <input
                id="unlockPin"
                type="password"
                inputmode="numeric"
                placeholder="Enter PIN"
            >

            <button class="primary" onclick="unlockApp()">
                Unlock
            </button>

            <p id="lockError" class="message"></p>
        </div>
    </section>

    <!-- HOME -->
    <section id="home" class="screen">

        <h1 id="welcomeName">Hello!</h1>
        <p>Your personal space. Everything in one place.</p>

        <h2>Your Apps</h2>

        <div class="grid">

            <button class="tile" onclick="showPage('calculator')">
                <span>🧮</span>
                <span>Calculator</span>
            </button>

            <button class="tile" onclick="showPage('passwordPage')">
                <span>🔐</span>
                <span>Password Generator</span>
            </button>

            <button class="tile" onclick="showPage('notesPage')">
                <span>📝</span>
                <span>Notes</span>
            </button>

        </div>

        <button
            class="gaming-feature"
            onclick="showPage('gaming')"
        >
            <span class="gaming-icon">🧩</span>

            <span class="gaming-info">
                <strong>Gaming Hub</strong>
                <small>
                    Explore games, challenge yourself and have fun.
                </small>
            </span>
        </button>

        <button
            class="home-row"
            onclick="showPage('settingsPage')"
        >
            <span>⚙️</span>
            <span>Settings</span>
        </button>

        <button
            class="home-row"
            onclick="showPage('aboutPage')"
        >
            <span>✨</span>
            <span>About</span>
        </button>

        <button class="secondary" onclick="logout()">
            Logout
        </button>

    </section>

    <!-- CALCULATOR -->
    <section id="calculator" class="screen">

        <div class="header">
            <button class="back" onclick="showPage('home')">
                ← Back
            </button>
            <h2>Calculator</h2>
        </div>

        <div class="card">
            <div id="calcDisplay" class="display">0</div>

            <div class="calcgrid">

                <button class="special" onclick="clearCalc()">AC</button>
                <button class="special" onclick="deleteCalc()">DEL</button>
                <button class="special" onclick="appendCalc('%')">%</button>
                <button class="op" onclick="appendCalc('/')">÷</button>

                <button onclick="appendCalc('7')">7</button>
                <button onclick="appendCalc('8')">8</button>
                <button onclick="appendCalc('9')">9</button>
                <button class="op" onclick="appendCalc('*')">×</button>

                <button onclick="appendCalc('4')">4</button>
                <button onclick="appendCalc('5')">5</button>
                <button onclick="appendCalc('6')">6</button>
                <button class="op" onclick="appendCalc('-')">−</button>

                <button onclick="appendCalc('1')">1</button>
                <button onclick="appendCalc('2')">2</button>
                <button onclick="appendCalc('3')">3</button>
                <button class="op" onclick="appendCalc('+')">+</button>

                <button class="zero" onclick="appendCalc('0')">0</button>
                <button onclick="appendCalc('.')">.</button>
                <button class="equal" onclick="calculateResult()">=</button>

            </div>
        </div>
    </section>

    <!-- PASSWORD GENERATOR -->
    <section id="passwordPage" class="screen">

        <div class="header">
            <button class="back" onclick="showPage('home')">
                ← Back
            </button>
            <h2>Password Generator</h2>
        </div>

        <div class="card">

            <p>Create a random password.</p>

            <div id="passwordOutput" class="output">
                Your password will appear here
            </div>

            <label>Password length</label>
            <input
                id="passwordLength"
                type="number"
                min="4"
                max="64"
                value="16"
            >

            <label class="option">
                <input id="includeNumbers" type="checkbox" checked>
                Include numbers
            </label>

            <label class="option">
                <input id="includeSymbols" type="checkbox" checked>
                Include symbols
            </label>

            <button class="primary" onclick="generatePassword()">
                Generate Password
            </button>

            <button class="secondary" onclick="copyPassword()">
                Copy Password
            </button>

        </div>
    </section>

    <!-- NOTES -->
    <section id="notesPage" class="screen">

        <div class="header">
            <button class="back" onclick="showPage('home')">
                ← Back
            </button>
            <h2>My Notes</h2>
        </div>

        <div class="card">

            <input id="noteTitle" placeholder="Note title">

            <textarea
                id="noteText"
                rows="4"
                placeholder="Write your note..."
            ></textarea>

            <button class="primary" onclick="saveNote()">
                Save Note
            </button>

            <div id="notesList"></div>

        </div>
    </section>

    <!-- SETTINGS -->
    <section id="settingsPage" class="screen">

        <div class="header">
            <button class="back" onclick="showPage('home')">
                ← Back
            </button>
            <h2>Settings</h2>
        </div>

        <div class="card">

            <label>Display name</label>
            <input id="displayName" placeholder="Your name">

            <label class="option">
                <input id="lightModeToggle" type="checkbox">
                Light Mode
            </label>

            <label class="option">
                <input id="hapticToggle" type="checkbox">
                Haptic Feedback
            </label>

            <label>
                App PIN (leave blank to keep current PIN)
            </label>

            <input
                id="newPin"
                type="password"
                inputmode="numeric"
                placeholder="Set a PIN"
            >

            <button class="primary" onclick="saveSettings()">
                Save Settings
            </button>

            <p id="settingsMessage" class="message"></p>

        </div>
    </section>

    <!-- ABOUT -->
    <section id="aboutPage" class="screen">

        <div class="header">
            <button class="back" onclick="showPage('home')">
                ← Back
            </button>
            <h2>About</h2>
        </div>

        <div class="card center">

            <div class="logo">M</div>

            <h2>mobile.app</h2>

            <p>
                Your personal collection of useful tools and games.
            </p>

            <p>Version 1.0</p>

        </div>
    </section>

    <!-- GAMING HUB -->
    <section id="gaming" class="screen">

        <div class="header">
            <button class="back" onclick="showPage('home')">
                ← Back
            </button>
            <h2>Gaming Hub</h2>
        </div>

        <div class="gamegrid">

            <button
                class="gamecard"
                onclick="resetGuessGame();showPage('guessPage')"
            >
                <span>🔢</span>
                <span>Number Guessing</span>
            </button>

            <button
                class="gamecard"
                onclick="showPage('typingPage')"
            >
                <span>⌨️</span>
                <span>Typing Speed</span>
            </button>

            <button
                class="gamecard"
                onclick="showPage('flappyPage')"
            >
                <span>🐦</span>
                <span>Flappy Bird</span>
            </button>

            <button
                class="gamecard"
                onclick="showPage('snakePage')"
            >
                <span>🐍</span>
                <span>Snake</span>
            </button>

        </div>
    </section>

    <!-- NUMBER GUESSING -->
    <section id="guessPage" class="screen">

        <div class="header">
            <button class="back" onclick="showPage('gaming')">
                ← Back
            </button>
            <h2>Number Guessing</h2>
        </div>

        <div class="card">

            <p>
                Guess a number between 1 and 100.
                You have 10 chances.
            </p>

            <input
                id="guessInput"
                type="number"
                min="1"
                max="100"
                placeholder="Your guess"
            >

            <button class="primary" onclick="makeGuess()">
                Submit Guess
            </button>

            <p id="guessMessage" class="message"></p>

            <p id="guessAttempts" class="message">
                Attempts remaining: 10
            </p>

            <button class="secondary" onclick="resetGuessGame()">
                Restart Game
            </button>

        </div>
    </section>

    <!-- TYPING SPEED -->
    <section id="typingPage" class="screen">

        <div class="header">
            <button class="back" onclick="showPage('gaming')">
                ← Back
            </button>
            <h2>Typing Speed</h2>
        </div>

        <div class="card">

            <p id="typingText" class="output">
                Press Start to begin your typing test.
            </p>

            <textarea
                id="typingInput"
                rows="4"
                placeholder="Type the text here..."
                disabled
            ></textarea>

            <div class="stats">

        // APP JAVASCRIPT

const $ = (id) => document.getElementById(id);

let settings = {
    name: "",
    lightMode: false,
    haptics: true,
    pin: ""
};

let currentUser = "";
let calcValue = "0";

let guessNumber = 0;
let guessRemaining = 10;
let guessFinished = false;

let typingTimer = null;
let typingSeconds = 60;
let typingStarted = false;

function loadSettings() {
    try {
        const saved = localStorage.getItem("mobileAppSettings");

        if (saved) {
            settings = {
                ...settings,
                ...JSON.parse(saved)
            };
        }
    } catch (error) {
        console.error("Settings could not be loaded:", error);
    }
}

function saveSettingsData() {
    try {
        localStorage.setItem(
            "mobileAppSettings",
            JSON.stringify(settings)
        );
    } catch (error) {
        console.error("Settings could not be saved:", error);
    }
}

function applyTheme() {
    if (settings.lightMode) {
        document.documentElement.style.setProperty("--bg", "#edf5ef");
        document.documentElement.style.setProperty("--panel", "#ffffff");
        document.documentElement.style.setProperty("--panel2", "#e5f0e9");
        document.documentElement.style.setProperty("--green", "#168653");
        document.documentElement.style.setProperty("--gold", "#a77c27");
        document.documentElement.style.setProperty("--text", "#173329");
        document.documentElement.style.setProperty("--muted", "#60796c");
        document.documentElement.style.setProperty("--line", "#c5d9cc");

        document.body.style.background =
            "radial-gradient(ellipse at 12% 10%, #b9e8ce, transparent 40%)," +
            "radial-gradient(ellipse at 90% 85%, #f3dfb1, transparent 35%)," +
            "linear-gradient(145deg, #eaf5ee, #dcece2)";
    } else {
        document.documentElement.style.setProperty("--bg", "#071b17");
        document.documentElement.style.setProperty("--panel", "#102b25");
        document.documentElement.style.setProperty("--panel2", "#16382f");
        document.documentElement.style.setProperty("--green", "#62e6a4");
        document.documentElement.style.setProperty("--gold", "#e8c77b");
        document.documentElement.style.setProperty("--text", "#f4f4e9");
        document.documentElement.style.setProperty("--muted", "#a9c1b6");
        document.documentElement.style.setProperty("--line", "#315348");

        document.body.style.background =
            "radial-gradient(ellipse at 12% 10%, rgba(39,135,96,.48), transparent 36%)," +
            "radial-gradient(ellipse at 90% 85%, rgba(190,145,65,.20), transparent 32%)," +
            "radial-gradient(ellipse at 55% 45%, rgba(24,85,68,.25), transparent 50%)," +
            "linear-gradient(145deg, #020b09, #09231c 48%, #101d19)";
    }
}

function updateClock() {
    const now = new Date();

    const time = now.toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit"
    });

    const date = now.toLocaleDateString([], {
        weekday: "long",
        day: "numeric",
        month: "long",
        year: "numeric"
    });

    if ($("clock")) {
        $("clock").textContent = time;
    }

    if ($("loginClock")) {
        $("loginClock").textContent = time;
    }

    if ($("loginDate")) {
        $("loginDate").textContent = date;
    }
}

function showPage(pageId) {
    document.querySelectorAll(".screen").forEach(screen => {
        screen.classList.remove("active");
    });

    const target = $(pageId);

    if (target) {
        target.classList.add("active");
    }

    if (pageId !== "flappyPage") {
        stopFlappy();
    }

    if (pageId !== "snakePage") {
        stopSnake();
    }

    if (pageId === "flappyPage") {
        drawFlappy();
    }

    if (pageId === "snakePage") {
        drawSnake();
    }

    haptic();
}

function haptic() {
    if (!settings.haptics) return;

    if (navigator.vibrate) {
        navigator.vibrate(15);
    }
}

function loginUser() {
    const name = $("username").value.trim();

    if (!name) {
        alert("Please enter your name.");
        return;
    }

    currentUser = name;
    settings.name = name;
    saveSettingsData();

    if (settings.pin) {
        showPage("lock");
    } else {
        enterHome();
    }
}

function guestLogin() {
    currentUser = "Guest";
    enterHome();
}

function enterHome() {
    $("welcomeName").textContent =
        "Hello, " + (currentUser || settings.name || "Guest") + "!";

    showPage("home");
}

function unlockApp() {
    const enteredPin = $("unlockPin").value;

    if (enteredPin === settings.pin) {
        $("unlockPin").value = "";
        $("lockError").textContent = "";
        enterHome();
    } else {
        $("lockError").textContent = "Incorrect PIN. Try again.";
        $("unlockPin").value = "";
    }
}

function logout() {
    currentUser = "";
    $("username").value = "";
    $("unlockPin").value = "";
    showPage("login");
}

function saveSettings() {
    const name = $("displayName").value.trim();
    const pin = $("newPin").value.trim();

    if (pin && !/^\d{4,8}$/.test(pin)) {
        $("settingsMessage").textContent =
            "PIN must contain 4 to 8 digits.";
        return;
    }

    if (name) {
        settings.name = name;
    }

    settings.lightMode = $("lightModeToggle").checked;
    settings.haptics = $("hapticToggle").checked;

    if (pin) {
        settings.pin = pin;
    }

    saveSettingsData();
    applyTheme();

    $("newPin").value = "";
    $("settingsMessage").textContent = "Settings saved successfully.";

    if (currentUser && currentUser !== "Guest" && name) {
        currentUser = name;
        $("welcomeName").textContent = "Hello, " + name + "!";
    }

    haptic();
}

// CALCULATOR

function appendCalc(value) {
    if (calcValue === "0" && value !== ".") {
        calcValue = value;
    } else {
        calcValue += value;
    }

    $("calcDisplay").textContent = calcValue;
}

function clearCalc() {
    calcValue = "0";
    $("calcDisplay").textContent = calcValue;
}

function deleteCalc() {
    calcValue = calcValue.slice(0, -1);

    if (!calcValue) {
        calcValue = "0";
    }

    $("calcDisplay").textContent = calcValue;
}

function calculateResult() {
    try {
        if (!/^[0-9+\-*/%.() ]+$/.test(calcValue)) {
            throw new Error("Invalid expression");
        }

        const result = Function(
            '"use strict"; return (' + calcValue + ')'
        )();

        if (!Number.isFinite(result)) {
            throw new Error("Invalid result");
        }

        calcValue = String(
            Number.parseFloat(result.toFixed(10))
        );

        $("calcDisplay").textContent = calcValue;

    } catch (error) {
        $("calcDisplay").textContent = "Error";
        calcValue = "0";
    }
}

// PASSWORD GENERATOR

function generatePassword() {
    let length = Number.parseInt(
        $("passwordLength").value,
        10
    );

    if (!Number.isFinite(length)) {
        length = 16;
    }

    length = Math.max(4, Math.min(64, length));

    const letters =
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    const numbers = "0123456789";
    const symbols = "!@#$%^&*()-_=+[]{}";

    let characters = letters;

    if ($("includeNumbers").checked) {
        characters += numbers;
    }

    if ($("includeSymbols").checked) {
        characters += symbols;
    }

    let password = "";

    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(
            Math.random() * characters.length
        );

        password += characters[randomIndex];
    }

    $("passwordOutput").textContent = password;
    haptic();
}

async function copyPassword() {
    const password = $("passwordOutput").textContent;

    if (!password || password === "Your password will appear here") {
        return;
    }

    try {
        await navigator.clipboard.writeText(password);
        $("passwordOutput").textContent = password + " ✓ Copied";
    } catch (error) {
        $("passwordOutput").textContent =
            password + " (Select and copy manually)";
    }
}

// NOTES

function getNotes() {
    try {
        const notes = JSON.parse(
            localStorage.getItem("mobileAppNotes") || "[]"
        );

        return Array.isArray(notes) ? notes : [];
    } catch (error) {
        return [];
    }
}

function renderNotes() {
    const notes = getNotes();
    const list = $("notesList");

    if (!list) return;

    list.innerHTML = "";

    if (notes.length === 0) {
        list.innerHTML =
            '<p class="message">No notes saved yet.</p>';
        return;
    }

    notes.forEach((note, index) => {
        const card = document.createElement("div");
        card.className = "card";

        const title = document.createElement("strong");
        title.textContent = note.title || "Untitled";

        const content = document.createElement("p");
        content.textContent = note.text || "";

        const remove = document.createElement("button");
        remove.className = "secondary";
        remove.textContent = "Delete";
        remove.onclick = () => deleteNote(index);

        card.appendChild(title);
        card.appendChild(content);
        card.appendChild(remove);

        list.appendChild(card);
    });
}

function saveNote() {
    const title = $("noteTitle").value.trim();
    const text = $("noteText").value.trim();

    if (!title && !text) {
        alert("Write something before saving.");
        return;
    }

    const notes = getNotes();

    notes.unshift({
        title: title || "Untitled",
        text: text,
        date: new Date().toISOString()
    });

    try {
        localStorage.setItem(
            "mobileAppNotes",
            JSON.stringify(notes)
        );

        $("noteTitle").value = "";
        $("noteText").value = "";

        renderNotes();
        haptic();

    } catch (error) {
        alert("Unable to save note on this device.");
    }
}

function deleteNote(index) {
    const notes = getNotes();

    if (index < 0 || index >= notes.length) {
        return;
    }

    notes.splice(index, 1);

    localStorage.setItem(
        "mobileAppNotes",
        JSON.stringify(notes)
    );

    renderNotes();
}

// NUMBER GUESSING GAME

function resetGuessGame() {
    guessNumber = Math.floor(Math.random() * 100) + 1;
    guessRemaining = 10;
    guessFinished = false;

    if ($("guessInput")) {
        $("guessInput").value = "";
    }

    if ($("guessMessage")) {
        $("guessMessage").textContent = "Make your first guess!";
    }

    if ($("guessAttempts")) {
        $("guessAttempts").textContent =
            "Attempts remaining: 10";
    }
}

function makeGuess() {
    if (guessFinished) return;

    const value = Number.parseInt(
        $("guessInput").value,
        10
    );

    if (!Number.isInteger(value) || value < 1 || value > 100) {
        $("guessMessage").textContent =
            "Enter a number from 1 to 100.";
        return;
    }

    guessRemaining--;

    if (value === guessNumber) {
        $("guessMessage").textContent =
            "Correct! You guessed the number!";
        guessFinished = true;
    } else if (guessRemaining === 0) {
        $("guessMessage").textContent =
            "Game over! The number was " + guessNumber + ".";
        guessFinished = true;
    } else if (value < guessNumber) {
        $("guessMessage").textContent = "Too low! Try higher.";
    } else {
        $("guessMessage").textContent = "Too high! Try lower.";
    }

    $("guessAttempts").textContent =
        "Attempts remaining: " + guessRemaining;

    $("guessInput").value = "";
    haptic();
}

// TYPING SPEED GAME

const typingSentences = [
    "Practice makes progress and patience builds success.",
    "Every small step brings you closer to your goal.",
    "Learning something new can be an exciting journey.",
    "Stay focused and keep improving your skills every day."
];

let typingTarget = "";

function startTypingGame() {
    clearInterval(typingTimer);

    typingSeconds = 60;
    typingStarted = true;

    typingTarget = typingSentences[
        Math.floor(Math.random() * typingSentences.length)
    ];

    $("typingText").textContent = typingTarget;
    $("typingInput").value = "";
    $("typingInput").disabled = false;
    $("typingInput").focus();

    $("typingTime").textContent = "60";
    $("typingWpm").textContent = "0";
    $("typingAccuracy").textContent = "100%";
    $("typingMessage").textContent = "Start typing!";

    typingTimer = setInterval(() => {
        typingSeconds--;

        $("typingTime").textContent = typingSeconds;

        updateTypingStats();

        if (typingSeconds <= 0) {
            finishTypingGame();
        }
    }, 1000);
}

function updateTypingStats() {
    if (!typingStarted) return;

    const typed = $("typingInput").value;
    const words = typed.trim()
        ? typed.trim().split(/\s+/).length
        : 0;

    const elapsed = Math.max(1, 60 - typingSeconds);
    const wpm = Math.round(words / (elapsed / 60));

    let correct = 0;

    for (let i = 0; i < typed.length; i++) {
        if (typed[i] === typingTarget[i]) {
            correct++;
        }
    }

    const accuracy = typed.length
        ? Math.round((correct / typed.length) * 100)
        : 100;

    $("typingWpm").textContent = wpm;
    $("typingAccuracy").textContent = accuracy + "%";

    if (typed === typingTarget) {
        finishTypingGame();
    }
}

function finishTypingGame() {
    clearInterval(typingTimer);
    typingStarted = false;

    $("typingInput").disabled = true;
    $("typingMessage").textContent = "Test completed!";
}

if ($("typingInput")) {
    $("typingInput").addEventListener(
        "input",
        updateTypingStats
    );
}

// PART 3 CONTINUES WITH FLAPPY BIRD, SNAKE AND INITIALIZATION.
// FLAPPY BIRD — IMPROVED GAME

let flappyCanvas = $("flappyCanvas");
let flappyCtx = flappyCanvas.getContext("2d");

let bird = {
    x: 85,
    y: 220,
    velocity: 0,
    radius: 13
};

let flappyPipes = [];
let flappyScore = 0;
let flappyRunning = false;
let flappyOver = false;
let flappyFrame = 0;
let flappyAnimation = null;

const FLAPPY_GRAVITY = 0.38;
const FLAPPY_JUMP = -6.8;
const FLAPPY_GAP = 142;
const FLAPPY_PIPE_WIDTH = 58;

function resetFlappy() {
    bird = {
        x: 85,
        y: 220,
        velocity: 0,
        radius: 13
    };

    flappyPipes = [];
    flappyScore = 0;
    flappyFrame = 0;
    flappyOver = false;

    $("flappyScore").textContent = "0";
    $("flappyMessage").textContent = "Tap the game area to fly.";

    drawFlappy();
}

function drawCloud(ctx, x, y, scale) {
    ctx.save();
    ctx.translate(x, y);
    ctx.scale(scale, scale);

    ctx.fillStyle = "rgba(255,255,255,.75)";
    ctx.beginPath();
    ctx.arc(0, 10, 17, 0, Math.PI * 2);
    ctx.arc(20, 0, 22, 0, Math.PI * 2);
    ctx.arc(43, 10, 17, 0, Math.PI * 2);
    ctx.fill();

    ctx.restore();
}

function drawFlappy() {
    const ctx = flappyCtx;
    const width = flappyCanvas.width;
    const height = flappyCanvas.height;

    const sky = ctx.createLinearGradient(0, 0, 0, height);
    sky.addColorStop(0, "#64c7e9");
    sky.addColorStop(.68, "#b3e7d7");
    sky.addColorStop(1, "#e5edb1");

    ctx.fillStyle = sky;
    ctx.fillRect(0, 0, width, height);

    drawCloud(ctx, 55, 85, .8);
    drawCloud(ctx, 235, 145, .65);
    drawCloud(ctx, 155, 35, .55);

    // Distant hills
    ctx.fillStyle = "#8bcf9d";
    ctx.beginPath();
    ctx.moveTo(0, 370);
    ctx.quadraticCurveTo(80, 300, 165, 370);
    ctx.quadraticCurveTo(260, 300, 360, 365);
    ctx.lineTo(360, 430);
    ctx.lineTo(0, 430);
    ctx.fill();

    // Ground
    ctx.fillStyle = "#83c95c";
    ctx.fillRect(0, 425, width, 55);

    ctx.fillStyle = "#c7e18a";
    ctx.fillRect(0, 425, width, 7);

    // Pipes
    flappyPipes.forEach(pipe => {
        const gradient = ctx.createLinearGradient(
            pipe.x,
            0,
            pipe.x + FLAPPY_PIPE_WIDTH,
            0
        );

        gradient.addColorStop(0, "#168b50");
        gradient.addColorStop(.45, "#4fd77b");
        gradient.addColorStop(1, "#126b42");

        ctx.fillStyle = gradient;

        ctx.fillRect(
            pipe.x,
            0,
            FLAPPY_PIPE_WIDTH,
            pipe.top
        );

        ctx.fillRect(
            pipe.x,
            pipe.top + FLAPPY_GAP,
            FLAPPY_PIPE_WIDTH,
            height - (pipe.top + FLAPPY_GAP) - 55
        );

        ctx.fillStyle = "#0c7041";

        ctx.fillRect(
            pipe.x - 5,
            pipe.top - 18,
            FLAPPY_PIPE_WIDTH + 10,
            18
        );

        ctx.fillRect(
            pipe.x - 5,
            pipe.top + FLAPPY_GAP,
            FLAPPY_PIPE_WIDTH + 10,
            18
        );

        ctx.fillStyle = "rgba(255,255,255,.18)";
        ctx.fillRect(pipe.x + 8, 0, 5, pipe.top);
    });

    // Bird shadow
    ctx.fillStyle = "rgba(0,0,0,.15)";
    ctx.beginPath();
    ctx.ellipse(
        bird.x + 3,
        bird.y + 19,
        13,
        5,
        0,
        0,
        Math.PI * 2
    );
    ctx.fill();

    // Bird body
    ctx.save();
    ctx.translate(bird.x, bird.y);

    const tilt = Math.max(
        -.45,
        Math.min(.65, bird.velocity * .07)
    );

    ctx.rotate(tilt);

    ctx.fillStyle = "#ffcb45";
    ctx.beginPath();
    ctx.ellipse(0, 0, 15, 12, 0, 0, Math.PI * 2);
    ctx.fill();

    // Wing
    ctx.fillStyle = "#f3a928";
    ctx.beginPath();
    ctx.ellipse(-5, 3, 8, 5, -.35, 0, Math.PI * 2);
    ctx.fill();

    // Eye
    ctx.fillStyle = "#fff";
    ctx.beginPath();
    ctx.arc(7, -5, 5, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = "#202b27";
    ctx.beginPath();
    ctx.arc(9, -5, 2, 0, Math.PI * 2);
    ctx.fill();

    // Beak
    ctx.fillStyle = "#f47a35";
    ctx.beginPath();
    ctx.moveTo(12, 1);
    ctx.lineTo(23, 5);
    ctx.lineTo(12, 8);
    ctx.closePath();
    ctx.fill();

    ctx.restore();

    if (!flappyRunning && !flappyOver) {
        ctx.fillStyle = "rgba(4,35,27,.75)";
        ctx.font = "bold 21px Arial";
        ctx.textAlign = "center";
        ctx.fillText("FLAPPY BIRD", width / 2, 235);
    }

    if (flappyOver) {
        ctx.fillStyle = "rgba(3,20,15,.65)";
        ctx.fillRect(0, 0, width, height);

        ctx.fillStyle = "#fff";
        ctx.textAlign = "center";
        ctx.font = "bold 27px Arial";
        ctx.fillText("GAME OVER", width / 2, 220);

        ctx.font = "17px Arial";
        ctx.fillText(
            "Score: " + flappyScore,
            width / 2,
            255
        );
    }
}

function flappyJump() {
    if (!flappyRunning || flappyOver) return;

    bird.velocity = FLAPPY_JUMP;
}

function flappyLoop() {
    if (!flappyRunning) return;

    flappyFrame++;

    bird.velocity += FLAPPY_GRAVITY;
    bird.y += bird.velocity;

    if (flappyFrame % 95 === 0) {
        const top = 65 + Math.random() * 210;

        flappyPipes.push({
            x: flappyCanvas.width,
            top: top,
            scored: false
        });
    }

    flappyPipes.forEach(pipe => {
        pipe.x -= 2.5;

        if (!pipe.scored && pipe.x + FLAPPY_PIPE_WIDTH < bird.x) {
            pipe.scored = true;
            flappyScore++;

            $("flappyScore").textContent = flappyScore;
        }

        const birdLeft = bird.x - bird.radius;
        const birdRight = bird.x + bird.radius;
        const birdTop = bird.y - bird.radius;
        const birdBottom = bird.y + bird.radius;

        const pipeLeft = pipe.x;
        const pipeRight = pipe.x + FLAPPY_PIPE_WIDTH;

        const horizontalCollision =
            birdRight > pipeLeft && birdLeft < pipeRight;

        const outsideGap =
            birdTop < pipe.top ||
            birdBottom > pipe.top + FLAPPY_GAP;

        if (horizontalCollision && outsideGap) {
            endFlappy();
        }
    });

    flappyPipes = flappyPipes.filter(
        pipe => pipe.x + FLAPPY_PIPE_WIDTH > 0
    );

    if (
        bird.y + bird.radius >= 425 ||
        bird.y - bird.radius <= 0
    ) {
        endFlappy();
    }

    drawFlappy();

    if (flappyRunning) {
        flappyAnimation = requestAnimationFrame(flappyLoop);
    }
}

function endFlappy() {
    if (flappyOver) return;

    flappyRunning = false;
    flappyOver = true;

    cancelAnimationFrame(flappyAnimation);

    $("flappyMessage").textContent =
        "Game over! Tap Start / Restart to play again.";

    drawFlappy();
}

function startFlappyGame() {
    stopFlappy();

    resetFlappy();

    flappyRunning = true;
    flappyOver = false;

    $("flappyMessage").textContent =
        "Tap the game area to fly!";

    flappyLoop();
}

function stopFlappy() {
    flappyRunning = false;

    if (flappyAnimation !== null) {
        cancelAnimationFrame(flappyAnimation);
        flappyAnimation = null;
    }
}

flappyCanvas.addEventListener("pointerdown", event => {
    event.preventDefault();

    if (!flappyRunning && !flappyOver) {
        startFlappyGame();
    } else {
        flappyJump();
    }
});

// SNAKE — IMPROVED GAME

const snakeCanvas = $("snakeCanvas");
const snakeCtx = snakeCanvas.getContext("2d");

const SNAKE_SIZE = 20;
const SNAKE_CELL = snakeCanvas.width / SNAKE_SIZE;

let snake = [];
let snakeFood = { x: 10, y: 10 };
let snakeDirection = { x: 1, y: 0 };
let nextSnakeDirection = { x: 1, y: 0 };
let snakeScore = 0;
let snakeRunning = false;
let snakeOver = false;
let snakeTimer = null;

function resetSnake() {
    snake = [
        { x: 8, y: 10 },
        { x: 7, y: 10 },
        { x: 6, y: 10 }
    ];

    snakeDirection = { x: 1, y: 0 };
    nextSnakeDirection = { x: 1, y: 0 };

    snakeScore = 0;
    snakeOver = false;

    $("snakeScore").textContent = "0";
    $("snakeMessage").textContent =
        "Swipe or use arrow keys to move.";

    placeSnakeFood();
    drawSnake();
}

function placeSnakeFood() {
    let validPosition = false;

    while (!validPosition) {
        snakeFood = {
            x: Math.floor(Math.random() * SNAKE_SIZE),
            y: Math.floor(Math.random() * SNAKE_SIZE)
        };

        validPosition = !snake.some(part =>
            part.x === snakeFood.x &&
            part.y === snakeFood.y
        );
    }
}

function drawSnake() {
    const ctx = snakeCtx;
    const width = snakeCanvas.width;
    const height = snakeCanvas.height;

    ctx.clearRect(0, 0, width, height);

    // Background
    const background = ctx.createLinearGradient(
        0,
        0,
        width,
        height
    );

    background.addColorStop(0, "#102d25");
    background.addColorStop(1, "#071b17");

    ctx.fillStyle = background;
    ctx.fillRect(0, 0, width, height);

    // Grid
    ctx.strokeStyle = "rgba(145,210,170,.075)";
    ctx.lineWidth = 1;

    for (let i = 0; i <= SNAKE_SIZE; i++) {
        const position = i * SNAKE_CELL;

        ctx.beginPath();
        ctx.moveTo(position, 0);
        ctx.lineTo(position, height);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(0, position);
        ctx.lineTo(width, position);
        ctx.stroke();
    }

    // Food glow
    const foodX = snakeFood.x * SNAKE_CELL + SNAKE_CELL / 2;
    const foodY = snakeFood.y * SNAKE_CELL + SNAKE_CELL / 2;

    ctx.shadowColor = "#ffbd55";
    ctx.shadowBlur = 15;

    ctx.fillStyle = "#ffbd55";
    ctx.beginPath();
    ctx.arc(
        foodX,
        foodY,
        SNAKE_CELL * .34,
        0,
        Math.PI * 2
    );
    ctx.fill();

    ctx.shadowBlur = 0;

    // Snake
    snake.forEach((part, index) => {
        const x = part.x * SNAKE_CELL;
        const y = part.y * SNAKE_CELL;
        const gap = 1.5;

        const gradient = ctx.createLinearGradient(
            x,
            y,
            x + SNAKE_CELL,
            y + SNAKE_CELL
        );

        if (index === 0) {
            gradient.addColorStop(0, "#b2ffd0");
            gradient.addColorStop(1, "#48d98b");
        } else {
            gradient.addColorStop(0, "#45d88a");
            gradient.addColorStop(1, "#168c5a");
        }

        ctx.fillStyle = gradient;

        ctx.beginPath();
        ctx.roundRect(
            x + gap,
            y + gap,
            SNAKE_CELL - gap * 2,
            SNAKE_CELL - gap * 2,
            index === 0 ? 7 : 5
        );
        ctx.fill();

        if (index === 0) {
            // Snake eyes
            ctx.fillStyle = "#09251b";

            let eyeOne;
            let eyeTwo;

            if (snakeDirection.x === 1) {
                eyeOne = [x + 14, y + 6];
                eyeTwo = [x + 14, y + 14];
            } else if (snakeDirection.x === -1) {
                eyeOne = [x + 6, y + 6];
                eyeTwo = [x + 6, y + 14];
            } else if (snakeDirection.y === -1) {
                eyeOne = [x + 6, y + 6];
                eyeTwo = [x + 14, y + 6];
            } else {
                eyeOne = [x + 6, y + 14];
                eyeTwo = [x + 14, y + 14];
            }

            ctx.beginPath();
            ctx.arc(eyeOne[0], eyeOne[1], 2, 0, Math.PI * 2);
            ctx.arc(eyeTwo[0], eyeTwo[1], 2, 0, Math.PI * 2);
            ctx.fill();
        }
    });

    if (snakeOver) {
        ctx.fillStyle = "rgba(0,0,0,.65)";
        ctx.fillRect(0, 0, width, height);

        ctx.fillStyle = "#fff";
        ctx.textAlign = "center";
        ctx.font = "bold 25px Arial";
        ctx.fillText("GAME OVER", width / 2, height / 2 - 10);

        ctx.font = "16px Arial";
        ctx.fillText(
            "Score: " + snakeScore,
            width / 2,
            height / 2 + 22
        );
    }
}

function setSnakeDirection(x, y) {
    if (
        x === -snakeDirection.x &&
        y === -snakeDirection.y
    ) {
        return;
    }

    nextSnakeDirection = { x, y };
}

function snakeStep() {
    if (!snakeRunning || snakeOver) return;

    snakeDirection = { ...nextSnakeDirection };

    const head = {
        x: snake[0].x + snakeDirection.x,
        y: snake[0].y + snakeDirection.y
    };

    const eating =
        head.x === snakeFood.x &&
        head.y === snakeFood.y;

    const bodyToCheck = eating
        ? snake
        : snake.slice(0, -1);

    const wallCollision =
        head.x < 0 ||
        head.y < 0 ||
        head.x >= SNAKE_SIZE ||
        head.y >= SNAKE_SIZE;

    const bodyCollision = bodyToCheck.some(part =>
        part.x === head.x &&
        part.y === head.y
    );

    if (wallCollision || bodyCollision) {
        endSnake();
        return;
    }

    snake.unshift(head);

    if (eating) {
        snakeScore += 10;

        $("snakeScore").textContent = snakeScore;

        placeSnakeFood();
        haptic();
    } else {
        snake.pop();
    }

    drawSnake();
}

function endSnake() {
    snakeRunning = false;
    snakeOver = true;

    clearInterval(snakeTimer);
    snakeTimer = null;

    $("snakeMessage").textContent =
        "Game over! Tap Start / Restart to play again.";

    drawSnake();
}

function startSnakeGame() {
    stopSnake();
    resetSnake();

    snakeRunning = true;

    $("snakeMessage").textContent =
        "Good luck! Collect the golden food.";

    snakeTimer = setInterval(snakeStep, 115);
}

function stopSnake() {
    snakeRunning = false;

    if (snakeTimer !== null) {
        clearInterval(snakeTimer);
        snakeTimer = null;
    }
}

// SNAKE KEYBOARD CONTROLS

document.addEventListener("keydown", event => {
    if (!$("snakePage").classList.contains("active")) {
        return;
    }

    const keys = {
        ArrowUp: [0, -1],
        ArrowDown: [0, 1],
        ArrowLeft: [-1, 0],
        ArrowRight: [1, 0]
    };

    if (keys[event.key]) {
        event.preventDefault();

        setSnakeDirection(
            keys[event.key][0],
            keys[event.key][1]
        );
    }
});

// SNAKE SWIPE CONTROLS

let snakeTouchStartX = 0;
let snakeTouchStartY = 0;

snakeCanvas.addEventListener("pointerdown", event => {
    snakeTouchStartX = event.clientX;
    snakeTouchStartY = event.clientY;
});

snakeCanvas.addEventListener("pointerup", event => {
    const dx = event.clientX - snakeTouchStartX;
    const dy = event.clientY - snakeTouchStartY;

    if (Math.max(Math.abs(dx), Math.abs(dy)) < 15) {
        return;
    }

    if (Math.abs(dx) > Math.abs(dy)) {
        setSnakeDirection(
            dx > 0 ? 1 : -1,
            0
        );
    } else {
        setSnakeDirection(
            0,
            dy > 0 ? 1 : -1
        );
    }
});

// INITIALIZE APP

function initializeApp() {
    loadSettings();

    if ($("displayName")) {
        $("displayName").value = settings.name || "";
    }

    if ($("lightModeToggle")) {
        $("lightModeToggle").checked = !!settings.lightMode;
    }

    if ($("hapticToggle")) {
        $("hapticToggle").checked = !!settings.haptics;
    }

    applyTheme();

    updateClock();
    setInterval(updateClock, 1000);

    renderNotes();
    resetGuessGame();
    resetFlappy();
    resetSnake();

    if (settings.pin) {
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
