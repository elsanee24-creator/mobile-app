# ============================================================
#                     PART 1
#              APP SETUP & DESIGN SYSTEM
# ============================================================
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

html,body{
 margin:0;
 width:100%;
 height:100%;
 min-height:0;
 overflow:hidden;
 font-family:Arial,sans-serif;
 background:#172b35;
 color:#fff;
}

button,input,textarea{font:inherit}
button{cursor:pointer;border:0;color:white}

#app{
 height:100dvh;
 width:100%;
 max-width:650px;
 margin:auto;
 padding:5px 9px 10px;
 overflow:hidden;
 border-radius:42px;
 background:
 radial-gradient(ellipse at 15% 10%,#416b60 0,transparent 42%),
 radial-gradient(ellipse at 90% 85%,#a77b48 0,transparent 38%),
 linear-gradient(145deg,#173c3b,#244d50 55%,#66503d);
 position:relative;
 display:flex;
 flex-direction:column;
}

.screen{
 flex:1 1 0%;
 height:0;
 min-height:0;
 max-height:100%;
 width:100%;
 overflow-y:auto;
 overflow-x:hidden;
 overscroll-behavior-y:contain;
 -webkit-overflow-scrolling:touch;
 touch-action:pan-y;
 border:1px solid #ffffff35;
 border-radius:34px;
 padding:48px 15px calc(110px + env(safe-area-inset-bottom));
 background:#ffffff0c;
 backdrop-filter:blur(18px);
 box-shadow:0 15px 50px #0003;
 scrollbar-width:none;
}

.screen::-webkit-scrollbar{display:none}
.hidden{display:none!important}

h1,h2,h3,p{margin-top:0}
h1{font-size:27px}
h2{font-size:22px}
.muted{color:#d2ded8;font-size:13px}

.clock{
 text-align:center;
 padding:18px 5px 22px;
}

.clock-icon{font-size:28px}

#time{
 font-size:39px;
 font-weight:800;
 letter-spacing:2px;
 margin:5px;
}

#date{
 color:#e0e8df;
 font-size:13px;
}

.input{
 width:100%;
 padding:14px;
 border:1px solid #ffffff35;
 border-radius:13px;
 background:#183b3b;
 color:white;
 margin:7px 0;
 outline:none;
}

.input:focus,
.notes-title:focus,
.notes-content:focus{
 border-color:#e5c58d;
 box-shadow:0 0 0 2px #e5c58d25;
}

.btn{
 padding:13px 15px;
 border-radius:13px;
 background:linear-gradient(110deg,#b58b55,#80623d);
 font-weight:bold;
 margin:5px 0;
 width:100%;
 box-shadow:0 5px 18px #0003;
 transition:transform .15s,filter .15s;
}

.btn:active{transform:scale(.97);filter:brightness(1.15)}

.btn.secondary{
 background:#ffffff16;
 border:1px solid #ffffff35;
}

.btn.small{
 width:auto;
 padding:10px 15px;
}

.row{
 display:flex;
 gap:9px;
}

.row>*{
 flex:1;
 min-width:0;
}

.card{
 padding:15px;
 border:1px solid #ffffff30;
 background:#ffffff12;
 border-radius:17px;
 margin:10px 0;
}

.home-grid{
 display:grid;
 grid-template-columns:1fr 1fr;
 gap:10px;
}

.home-tile{
 min-height:83px;
 border-radius:17px;
 padding:13px;
 background:linear-gradient(135deg,#527a6a,#315b55);
 border:1px solid #ffffff35;
 text-align:left;
}

.home-tile b{
 display:block;
 margin-top:8px;
}

.hub{
 grid-column:1/-1;
 min-height:105px;
 background:linear-gradient(120deg,#9b754a,#526d55);
}

.bigicon{font-size:27px}

.back{
 background:#ffffff20;
 padding:9px 13px;
 border-radius:10px;
 margin-bottom:12px;
}

.game-area{
 border-radius:18px;
 overflow:hidden;
 position:relative;
 border:1px solid #ffffff35;
}

canvas{
 display:block;
 width:100%;
 height:auto;
 touch-action:none;
}

.game-controls{
 display:flex;
 justify-content:center;
 gap:10px;
 flex-wrap:wrap;
 margin-top:12px;
}

.game-controls button{
 background:#ffffff20;
 border:1px solid #ffffff35;
 padding:12px 18px;
 border-radius:12px;
}

/* Individual screen backgrounds */

#login{
 background:
 radial-gradient(ellipse at 50% 10%,#a17a4b 0,transparent 45%),
 linear-gradient(145deg,#244b45,#173536 65%,#55432f);
}

#home{
 background:
 radial-gradient(ellipse at 90% 5%,#b28a55 0,transparent 40%),
 linear-gradient(145deg,#315b4e,#24443d);
}

#calculator{
 background:linear-gradient(145deg,#3c5264,#243a4a 60%,#6d5843);
}

#passwordPage{
 background:linear-gradient(145deg,#4c3e60,#352d4c 60%,#73533e);
}

#notesPage{
 background:
 radial-gradient(ellipse at 10% 5%,#96714c 0,transparent 40%),
 linear-gradient(145deg,#4c493b,#354d48);
}

#settingsPage{
 background:linear-gradient(145deg,#385b68,#29434d 60%,#66533e);
}

#aboutPage{
 background:linear-gradient(145deg,#66513d,#465d51 65%,#344d53);
}

#gaming{
 background:
 radial-gradient(ellipse at 85% 5%,#a77a4b 0,transparent 42%),
 linear-gradient(145deg,#344d42,#263c43);
}

#guessPage{
 background:linear-gradient(145deg,#3d536c,#293c56 60%,#70543d);
}

#typingPage{
 background:linear-gradient(145deg,#514466,#34344f 60%,#73543e);
}

#flappyPage{
 background:linear-gradient(145deg,#b3a06d,#6e987f 60%,#527b83);
 color:#173d3c;
}

#snakePage{
 background:linear-gradient(145deg,#315b50,#24443d 60%,#80633f);
}

/* Calculator */

#calcDisplay{
 width:100%;
 font-size:30px;
 text-align:right;
 padding:17px;
 border-radius:14px;
 border:1px solid #ffffff30;
 background:#263d49;
 color:white;
 margin-bottom:10px;
}

.calc-grid{
 display:grid;
 grid-template-columns:repeat(4,1fr);
 gap:8px;
}

.calc-grid button{
 height:58px;
 border-radius:14px;
 background:linear-gradient(145deg,#526d79,#304b58);
 font-size:19px;
}

.calc-grid button.op{
 background:linear-gradient(145deg,#a47b50,#745537);
}

.calc-grid button.eq{
 background:linear-gradient(145deg,#398c78,#286b60);
}

.calc-grid button.clear{
 background:#a64e50;
}

/* Loading */

#loading{
 position:absolute;
 inset:5px;
 z-index:20;
 border-radius:23px;
 background:#193a38f5;
 display:flex;
 flex-direction:column;
 align-items:center;
 justify-content:center;
}

.spinner{
 width:54px;
 height:54px;
 border:4px solid #ffffff25;
 border-top-color:#e5c58d;
 border-radius:50%;
 animation:spin .8s linear infinite;
}

@keyframes spin{to{transform:rotate(360deg)}}

.bar{
 height:5px;
 width:190px;
 background:#ffffff22;
 border-radius:8px;
 margin-top:20px;
 overflow:hidden;
}

.bar:after{
 content:"";
 display:block;
 height:100%;
 width:0;
 background:#e5c58d;
 animation:load 2s linear forwards;
}

@keyframes load{to{width:100%}}

/* Fingerprint button */

.fingerprint-wrap{
 display:flex;
 justify-content:center;
 align-items:center;
 margin:12px auto 5px;
}

.fingerprint-btn{
 width:66px;
 height:66px;
 border-radius:50%;
 display:flex;
 align-items:center;
 justify-content:center;
 background:linear-gradient(145deg,#537568,#294c47);
 border:1px solid #e5c58d88;
 box-shadow:0 0 15px #e5c58d30;
 color:#f0d6a8;
 padding:0;
}

.fingerprint-btn:active{transform:scale(.94)}

.fingerprint-btn svg{
 width:36px;
 height:36px;
 stroke:#f0d6a8;
}

/* Notes */

#notesPage{
 padding-bottom:calc(110px + env(safe-area-inset-bottom));
}

.notes-heading{
 display:flex;
 justify-content:space-between;
 align-items:center;
 position:sticky;
 top:-48px;
 z-index:3;
 background:#414a3bed;
 padding:8px 0;
}

.notes-editor{
 background:#ffffff12;
 border:1px solid #ffffff30;
 border-radius:18px;
 padding:11px;
 margin:7px 0 12px;
}

.notes-title{
 width:100%;
 padding:11px;
 border-radius:11px;
 border:1px solid #ffffff30;
 background:#30443e;
 color:white;
 outline:none;
 margin:5px 0 8px;
}

.notes-content{
 width:100%;
 min-height:88px;
 max-height:150px;
 resize:vertical;
 padding:11px;
 border-radius:11px;
 border:1px solid #ffffff30;
 background:#30443e;
 color:white;
 outline:none;
}

.notes-list{
 display:flex;
 flex-direction:column;
 gap:9px;
 padding-bottom:24px;
}

.note-card{
 background:linear-gradient(135deg,#ffffff1c,#ffffff09);
 border:1px solid #ffffff30;
 border-radius:15px;
 padding:12px;
 overflow-wrap:anywhere;
}

.note-card h3{
 margin:0 0 7px;
 font-size:17px;
}

.note-card p{
 white-space:pre-wrap;
 color:#e0e8df;
 font-size:13px;
 margin:0 0 10px;
 max-height:120px;
 overflow-y:auto;
}

.note-meta{
 font-size:11px;
 color:#d0d9ce;
 margin-bottom:10px;
}

.note-actions{
 display:flex;
 gap:8px;
}

.note-actions button{
 flex:1;
 min-height:44px;
 padding:9px;
 border-radius:10px;
 background:#ffffff20;
 border:1px solid #ffffff30;
 font-weight:bold;
}

.note-actions .delete-note{
 background:#a64e5055;
 border:1px solid #ff9a9a88;
 color:#fff;
}

.notes-empty{
 text-align:center;
 padding:18px 12px;
 border:1px dashed #ffffff40;
 border-radius:15px;
 color:#e0e8df;
}

.notes-message{
 min-height:17px;
 color:#e5c58d;
 font-size:12px;
 margin-top:5px;
}

#notesPage h3{margin-bottom:7px}
#settingsPage,#aboutPage{padding-bottom:calc(110px + env(safe-area-inset-bottom))}

@media(max-height:700px){
 .screen{padding-top:48px}
 .clock{padding:8px 4px 12px}
 #time{font-size:32px}
 .home-tile{min-height:68px}
 .btn{padding:11px}
 .fingerprint-btn{width:58px;height:58px}
}

@media(max-width:380px){
 #app{padding:3px 7px 8px}
 .screen{padding-left:11px;padding-right:11px;border-radius:26px}
 h1{font-size:24px}
 .clock{padding:9px 4px 12px}
 #time{font-size:33px}
 .input{padding:12px}
 .home-tile{padding:10px}
}

/* Phone frame details */

#app:before{
 content:"";
 position:absolute;
 top:8px;
 left:50%;
 transform:translateX(-50%);
 width:104px;
 height:27px;
 border-radius:18px;
 background:#28302c;
 border:1px solid #69716a;
 z-index:30;
 box-shadow:0 2px 10px #0005;
 pointer-events:none;
}

#app:after{
 content:"";
 position:absolute;
 top:18px;
 left:calc(50% + 31px);
 width:7px;
 height:7px;
 border-radius:50%;
 background:#435e62;
 box-shadow:inset 0 0 3px #a4c4bd;
 z-index:31;
 pointer-events:none;
}

/* Settings */

.setting-row{
 display:flex;
 align-items:center;
 justify-content:space-between;
 gap:12px;
 padding:12px 0;
 border-bottom:1px solid #ffffff22;
}

.setting-row:last-child{border-bottom:0}

.setting-row small{
 display:block;
 color:#d2ded8;
 margin-top:3px;
}

.toggle{
 width:48px;
 height:27px;
 border-radius:20px;
 background:#536078;
 position:relative;
 flex:none;
}

.toggle:after{
 content:"";
 position:absolute;
 width:21px;
 height:21px;
 left:3px;
 top:3px;
 border-radius:50%;
 background:white;
 transition:.2s;
}

.toggle.on{background:#398c78}
.toggle.on:after{left:24px}

/* App lock */

#lockOverlay{
 position:absolute;
 inset:5px;
 z-index:50;
 border-radius:23px;
 background:#24423df5;
 display:none;
 align-items:center;
 justify-content:center;
 padding:24px;
}

#lockOverlay.active{display:flex}

.lock-box{
 width:100%;
 max-width:330px;
 text-align:center;
 padding:22px;
 border:1px solid #ffffff35;
 border-radius:20px;
 background:#ffffff12;
}

#lockOverlay input{
 letter-spacing:8px;
 text-align:center;
 font-size:22px;
}

#lockMessage{
 min-height:20px;
 color:#ffb0a9;
 font-size:12px;
}

/* Responsive scrolling */

html,body{
 height:100%;
 min-height:0;
 overflow:hidden;
 touch-action:pan-y;
}

#app{
 height:100dvh;
 min-height:0;
 max-height:none;
 overflow:hidden;
 display:flex;
 flex-direction:column;
}

.screen:not(#login){
 flex:1 1 0%;
 height:0;
 min-height:0;
 max-height:100%;
 overflow-y:auto!important;
 overflow-x:hidden!important;
 -webkit-overflow-scrolling:touch;
 overscroll-behavior-y:contain;
 touch-action:pan-y!important;
 scrollbar-width:none;
}

.screen:not(#login)::-webkit-scrollbar{display:none}

#login{
 overflow:hidden!important;
 touch-action:none!important;
}

body.light-mode #app{
 background:linear-gradient(145deg,#e8e0cc,#d3e2d8);
}

body.light-mode .screen{
 color:#263b39;
 border-color:#ffffff;
}

body.light-mode .muted,
body.light-mode #date{
 color:#52665d;
}

body.light-mode .card,
body.light-mode .home-tile{
 background:#ffffffd9;
 border-color:#d7dfd2;
 color:#263b39;
}

body.light-mode .input,
body.light-mode .notes-title,
body.light-mode .notes-content{
 background:#f4f2e9;
 color:#263b39;
 border-color:#d5d9c9;
}

body.light-mode .notes-heading{
 background:#e4e9dc;
}

body.light-mode .back{
 background:#dce6d9;
 color:#263b39;
}
</style>
</head>

<body>

    </section>

                <button onclick="appendCalc('9')">9</button>
                <button onclick="appendCalc('*')" class="calc-operator">×</button>

                <button onclick="appendCalc('4')">4</button>
                <button onclick="appendCalc('5')">5</button>
                <button onclick="appendCalc('6')">6</button>
                <button onclick="appendCalc('-')" class="calc-operator">−</button>

                <button onclick="appendCalc('1')">1</button>
                <button onclick="appendCalc('2')">2</button>
                <button onclick="appendCalc('3')">3</button>
                <button onclick="appendCalc('+')" class="calc-operator">+</button>

                <button onclick="appendCalc('0')" class="calc-zero">0</button>
                <button onclick="appendCalc('.')">.</button>
                <button onclick="calculateResult()" class="calc-equal">=</button>

            </div>
        </div>

    </section>

    

            
            <textarea
                id="typingInput"
                placeholder="Start typing here..."
                rows="5"
            ></textarea>

            <div class="typing-stats">
                <p>Time: <span id="typingTime">60</span>s</p>
                <p>WPM: <span id="typingWpm">0</span></p>
                <p>Accuracy: <span id="typingAccuracy">100</span>%</p>
            </div>

            <button class="primary-btn" onclick="startTypingGame()">
                Start Typing Test
            </button>

        </div>

    </section>

    
<!-- =========================================================
                     PART 2
              MOBILE.APP — APP STRUCTURE
     ========================================================= -->

<div id="app">

    <!-- APP LOCK SCREEN -->
    <div id="lockOverlay" class="screen hidden">
        <div class="lock-card">
            <div class="app-logo">M</div>
            <h2>App Locked</h2>
            <p>Enter your PIN to continue</p>

            <input
                type="password"
                id="unlockPin"
                placeholder="Enter PIN"
                inputmode="numeric"
            >

            <button class="primary-btn" onclick="unlockApp()">
                Unlock
            </button>

            <p id="lockError" class="error-message"></p>
        </div>
    </div>

    <!-- LOGIN SCREEN -->
    <section id="login" class="screen">
        <div class="login-content">
            <div class="app-logo">M</div>

            <h1>Welcome Back</h1>
            <p>Your personal mobile experience</p>

            <input
                type="text"
                id="username"
                placeholder="Enter your name"
                autocomplete="off"
            >

            <button class="primary-btn" onclick="loginUser()">
                Login
            </button>

            <button class="secondary-btn" onclick="loginAsGuest()">
                Explore as Guest
            </button>
        </div>
    </section>

    <!-- HOME SCREEN -->
    <section id="home" class="screen hidden">

        <header class="top-header">
            <div>
                <p class="small-label">WELCOME TO</p>
                <h1 id="homeTitle">mobile.app</h1>
                <p id="welcomeName">Hello!</p>
            </div>

            <div class="header-clock" id="clock">
                --:--
            </div>
        </header>

        <div class="home-section">
            <h2>Your Apps</h2>

            <div class="app-grid">

                <button class="app-card" onclick="showPage('calculator')">
                    <span class="app-icon">🧮</span>
                    <span>Calculator</span>
                </button>

                <button class="app-card" onclick="showPage('passwordPage')">
                    <span class="app-icon">🔐</span>
                    <span>Password Generator</span>
                </button>

                <button class="app-card" onclick="showPage('notesPage')">
                    <span class="app-icon">📝</span>
                    <span>Notes</span>
                </button>

                <button class="app-card" onclick="showPage('gaming')">
                    <span class="app-icon">🎮</span>
                    <span>Gaming Hub</span>
                </button>

                <button class="app-card" onclick="showPage('settingsPage')">
                    <span class="app-icon">⚙️</span>
                    <span>Settings</span>
                </button>

                <button class="app-card" onclick="showPage('aboutPage')">
                    <span class="app-icon">✨</span>
                    <span>About</span>
                </button>

            </div>
        </div>

        <button class="back" onclick="goLogin()">
            Logout
        </button>

    </section>

    <!-- CALCULATOR SCREEN -->
    <section id="calculator" class="screen hidden">

        <div class="page-header">
            <button class="back" onclick="showPage('home')">← Back</button>
            <h2>Calculator</h2>
        </div>

        <div class="calculator-container">

            <div id="calcDisplay" class="calculator-display">
                0
            </div>

            <div class="calculator-grid">

                <button onclick="clearCalc()" class="calc-special">AC</button>
                <button onclick="deleteCalc()" class="calc-special">DEL</button>
                <button onclick="appendCalc('%')" class="calc-special">%</button>
                <button onclick="appendCalc('/')" class="calc-operator">÷</button>

                <button onclick="appendCalc('7')">7</button>
                <button onclick="appendCalc('8')">8</button>
                <button onclick="appendCalc('9')">9</button>
                <button onclick="appendCalc('*')" class="calc-operator">×</button>

                <button onclick="appendCalc('4')">4</button>
                <button onclick="appendCalc('5')">5</button>
                <button onclick="appendCalc('6')">6</button>
                <button onclick="appendCalc('-')" class="calc-operator">−</button>

                <button onclick="appendCalc('1')">1</button>
                <button onclick="appendCalc('2')">2</button>
                <button onclick="appendCalc('3')">3</button>
                <button onclick="appendCalc('+')" class="calc-operator">+</button>

                <button onclick="appendCalc('0')" class="calc-zero">0</button>
                <button onclick="appendCalc('.')">.</button>
                <button onclick="calculateResult()" class="calc-equal">=</button>

            </div>
        </div>

    </section>

    <!-- PASSWORD GENERATOR SCREEN -->
    <section id="passwordPage" class="screen hidden">

        <div class="page-header">
            <button class="back" onclick="showPage('home')">← Back</button>
            <h2>Password Generator</h2>
        </div>

        <div class="content-card">

            <p>Generate a secure password</p>

            <div id="passwordOutput" class="password-output">
                Your password will appear here
            </div>

            <label for="passwordLength">
                Password Length
            </label>

            <input
                type="number"
                id="passwordLength"
                min="4"
                max="64"
                value="16"
            >

            <label class="setting-option">
                <input type="checkbox" id="includeNumbers" checked>
                Include Numbers
            </label>

            <label class="setting-option">
                <input type="checkbox" id="includeSymbols" checked>
                Include Symbols
            </label>

            <button class="primary-btn" onclick="generatePassword()">
                Generate Password
            </button>

            <button class="secondary-btn" onclick="copyPassword()">
                Copy Password
            </button>

        </div>

    </section>

    <!-- NOTES SCREEN -->
    <section id="notesPage" class="screen hidden">

        <div class="page-header">
            <button class="back" onclick="showPage('home')">← Back</button>
            <h2>My Notes</h2>
        </div>

        <div class="content-card">

            <input
                type="text"
                id="noteTitle"
                placeholder="Note title"
            >

            <textarea
                id="noteText"
                placeholder="Write your note here..."
                rows="5"
            ></textarea>

            <button class="primary-btn" onclick="saveNote()">
                Save Note
            </button>

            <div id="notesList"></div>

        </div>

    </section>

    <!-- SETTINGS SCREEN -->
    <section id="settingsPage" class="screen hidden">

        <div class="page-header">
            <button class="back" onclick="showPage('home')">← Back</button>
            <h2>Settings</h2>
        </div>

        <div class="content-card">

            <label for="displayName">Display Name</label>
            <input
                type="text"
                id="displayName"
                placeholder="Your name"
            >

            <label class="setting-option">
                <input type="checkbox" id="lightModeToggle">
                Light Mode
            </label>

            <label class="setting-option">
                <input type="checkbox" id="hapticToggle">
                Haptic Feedback
            </label>

            <label for="newPin">App PIN</label>
            <input
                type="password"
                id="newPin"
                placeholder="Set a PIN"
                inputmode="numeric"
            >

            <button class="primary-btn" onclick="saveSettings()">
                Save Settings
            </button>

        </div>

    </section>

    <!-- ABOUT SCREEN -->
    <section id="aboutPage" class="screen hidden">

        <div class="page-header">
            <button class="back" onclick="showPage('home')">← Back</button>
            <h2>About</h2>
        </div>

        <div class="content-card about-content">
            <div class="app-logo">M</div>
            <h2>mobile.app</h2>
            <p>Your personal collection of useful tools and games.</p>
            <p>Version 1.0</p>
        </div>

    </section>

    <!-- GAMING HUB -->
    <section id="gaming" class="screen hidden">

        <div class="page-header">
            <button class="back" onclick="showPage('home')">← Back</button>
            <h2>Gaming Hub</h2>
        </div>

        <div class="game-grid">

            <button class="game-card" onclick="showPage('guessPage')">
                <span class="game-icon">🔢</span>
                <span>Number Guessing</span>
            </button>

            <button class="game-card" onclick="showPage('typingPage')">
                <span class="game-icon">⌨️</span>
                <span>Typing Speed</span>
            </button>

            <button class="game-card" onclick="showPage('flappyPage')">
                <span class="game-icon">🐦</span>
                <span>Flappy Bird</span>
            </button>

            <button class="game-card" onclick="showPage('snakePage')">
                <span class="game-icon">🐍</span>
                <span>Snake</span>
            </button>

        </div>

    </section>

    <!-- NUMBER GUESSING GAME -->
    <section id="guessPage" class="screen hidden">

        <div class="page-header">
            <button class="back" onclick="showPage('gaming')">← Back</button>
            <h2>Number Guessing</h2>
        </div>

        <div class="content-card game-content">

            <p>Guess a number between 1 and 100.</p>

            <input
                type="number"
                id="guessInput"
                placeholder="Enter your guess"
                min="1"
                max="100"
            >

            <button class="primary-btn" onclick="makeGuess()">
                Submit Guess
            </button>

            <p id="guessMessage"></p>
            <p id="guessAttempts">Attempts remaining: 10</p>

            <button class="secondary-btn" onclick="resetGuessGame()">
                Restart Game
            </button>

        </div>

    </section>

    <!-- TYPING SPEED GAME -->
    <section id="typingPage" class="screen hidden">

        <div class="page-header">
            <button class="back" onclick="showPage('gaming')">← Back</button>
            <h2>Typing Speed</h2>
        </div>

        <div class="content-card game-content">

            <div id="typingText" class="typing-text"></div>

            <textarea
                id="typingInput"
                placeholder="Start typing here..."
                rows="5"
            ></textarea>

            <div class="typing-stats">
                <p>Time: <span id="typingTime">60</span>s</p>
                <p>WPM: <span id="typingWpm">0</span></p>
                <p>Accuracy: <span id="typingAccuracy">100</span>%</p>
            </div>

            <button class="primary-btn" onclick="startTypingGame()">
                Start Typing Test
            </button>

        </div>

    </section>

    <!-- FLAPPY BIRD GAME -->
    <section id="flappyPage" class="screen hidden">

        <div class="page-header">
            <button class="back" onclick="showPage('gaming')">← Back</button>
            <h2>Flappy Bird</h2>
        </div>

        <div class="game-content">
            <div class="game-score">
                Score: <span id="flappyScore">0</span>
            </div>

            <canvas
                id="flappyCanvas"
                width="360"
                height="480"
            ></canvas>

            <button class="primary-btn" onclick="startFlappyGame()">
                Start Game
            </button>

            <p id="flappyMessage">
                Tap the screen to fly!
            </p>
        </div>

    </section>

    <!-- SNAKE GAME -->
    <section id="snakePage" class="screen hidden">

        <div class="page-header">
            <button class="back" onclick="showPage('gaming')">← Back</button>
            <h2>Snake</h2>
        </div>

        <div class="game-content">

            <div class="game-score">
                Score: <span id="snakeScore">0</span>
            </div>

            <canvas
                id="snakeCanvas"
                width="360"
                height="360"
            ></canvas>

            <p id="snakeMessage">
                Swipe or use WASD / Arrow keys.
            </p>

            <button class="primary-btn" onclick="startSnakeGame()">
                Start Game
            </button>

        </div>

    </section>

</div>

<!-- PART 2 ENDS HERE: NEXT PART CONTINUES WITH JAVASCRIPT -->
<!-- ========================================================= -->

<!-- =========================================================
                     PART 3
          JAVASCRIPT — APP CORE & NAVIGATION
     ========================================================= -->

<script>

// ============================================================
// APP STORAGE & GLOBAL SETTINGS
// ============================================================

const APP_STORAGE = {
    name: "mobileAppName",
    theme: "mobileAppTheme",
    haptics: "mobileAppHaptics",
    pin: "mobileAppPin",
    notes: "mobileAppNotes"
};

let currentUser = "";
let currentPage = "login";
let appLocked = false;

let appSettings = {
    name: localStorage.getItem(APP_STORAGE.name) || "mobile.app",
    theme: localStorage.getItem(APP_STORAGE.theme) || "dark",
    haptics: localStorage.getItem(APP_STORAGE.haptics) !== "false",
    pin: localStorage.getItem(APP_STORAGE.pin) || ""
};

// ============================================================
// BASIC DOM HELPERS
// ============================================================

function getElement(id) {
    return document.getElementById(id);
}

function setText(id, value) {
    const element = getElement(id);
    if (element) element.textContent = value;
}

function getValue(id) {
    const element = getElement(id);
    return element ? element.value : "";
}

// ============================================================
// HAPTIC FEEDBACK
// ============================================================

function vibrateDevice(duration = 25) {
    if (!appSettings.haptics) return;

    if (typeof navigator.vibrate === "function") {
        navigator.vibrate(duration);
    }
}

// ============================================================
// THEME MANAGEMENT
// ============================================================

function applyTheme() {
    document.body.classList.toggle(
        "light-mode",
        appSettings.theme === "light"
    );

    const toggle = getElement("lightModeToggle");

    if (toggle) {
        toggle.checked = appSettings.theme === "light";
    }
}

// ============================================================
// APP INITIALIZATION
// ============================================================

function initializeApp() {
    appSettings.name =
        localStorage.getItem(APP_STORAGE.name) || "mobile.app";

    appSettings.theme =
        localStorage.getItem(APP_STORAGE.theme) || "dark";

    appSettings.haptics =
        localStorage.getItem(APP_STORAGE.haptics) !== "false";

    appSettings.pin =
        localStorage.getItem(APP_STORAGE.pin) || "";

    applyTheme();
    updateClock();
    loadNotes();
    updateSettingsInputs();

    const loading = getElement("loadingScreen");

    if (loading) {
        loading.classList.add("hidden");
    }

    if (appSettings.pin) {
        appLocked = true;
        showOnlyScreen("lockOverlay");
    } else {
        showOnlyScreen("login");
    }

    setInterval(updateClock, 1000);
}

// ============================================================
// SCREEN NAVIGATION
// ============================================================

function showOnlyScreen(screenId) {
    document.querySelectorAll(".screen").forEach(screen => {
        screen.classList.add("hidden");
    });

    const target = getElement(screenId);

    if (!target) {
        console.error("Screen not found:", screenId);
        return;
    }

    target.classList.remove("hidden");
    currentPage = screenId;

    window.scrollTo(0, 0);
}

function showPage(pageId) {
    if (appLocked) return;

    const target = getElement(pageId);

    if (!target) {
        console.error("Page not found:", pageId);
        return;
    }

    showOnlyScreen(pageId);

    if (pageId === "notesPage") {
        loadNotes();
    }

    if (pageId === "settingsPage") {
        updateSettingsInputs();
    }

    if (pageId === "guessPage") {
        resetGuessGame();
    }

    if (pageId === "typingPage") {
        prepareTypingGame();
    }

    vibrateDevice();
}

// ============================================================
// LOGIN & GUEST ACCESS
// ============================================================

function loginUser() {
    const input = getValue("username").trim();

    if (!input) {
        alert("Please enter your name.");
        return;
    }

    currentUser = input;

    setText("welcomeName", "Hello, " + currentUser + "!");

    const displayName = getElement("displayName");

    if (displayName) {
        displayName.value = currentUser;
    }

    showPage("home");
    vibrateDevice(40);
}

function loginAsGuest() {
    currentUser = "Guest";

    setText("welcomeName", "Hello, Guest!");

    showPage("home");
    vibrateDevice(40);
}

function goLogin() {
    currentUser = "";
    showOnlyScreen("login");

    const username = getElement("username");

    if (username) {
        username.value = "";
    }
}

// ============================================================
// APP LOCK & PIN
// ============================================================

function unlockApp() {
    const enteredPin = getValue("unlockPin");
    const savedPin = localStorage.getItem(APP_STORAGE.pin) || "";

    if (savedPin && enteredPin === savedPin) {
        appLocked = false;

        const pinInput = getElement("unlockPin");

        if (pinInput) {
            pinInput.value = "";
        }

        setText("lockError", "");
        showOnlyScreen("login");
        vibrateDevice(50);

    } else {
        setText("lockError", "Incorrect PIN. Try again.");
        vibrateDevice(100);
    }
}

// ============================================================
// CLOCK
// ============================================================

function updateClock() {
    const clock = getElement("clock");

    if (!clock) return;

    clock.textContent = new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });
}

// ============================================================
// CALCULATOR
// ============================================================

let calcExpression = "";

function updateCalcDisplay() {
    const display = getElement("calcDisplay");

    if (display) {
        display.textContent = calcExpression || "0";
    }
}

function appendCalc(value) {
    if (!/^[0-9+\-*/%.]$/.test(value)) return;

    calcExpression += value;

    updateCalcDisplay();
    vibrateDevice(15);
}

function clearCalc() {
    calcExpression = "";
    updateCalcDisplay();
    vibrateDevice();
}

function deleteCalc() {
    calcExpression = calcExpression.slice(0, -1);
    updateCalcDisplay();
    vibrateDevice();
}

function calculateResult() {
    if (!calcExpression) return;

    if (!/^[0-9+\-*/%.() ]+$/.test(calcExpression)) {
        calcExpression = "";
        updateCalcDisplay();
        return;
    }

    try {
        const result = Function(
            '"use strict"; return (' + calcExpression + ')'
        )();

        if (!Number.isFinite(result)) {
            throw new Error("Invalid calculation");
        }

        calcExpression = String(
            Number(result.toPrecision(12))
        );

        updateCalcDisplay();
        vibrateDevice(35);

    } catch (error) {
        calcExpression = "";
        setText("calcDisplay", "Error");
    }
}

// ============================================================
// END OF PART 3
// PART 4 WILL CONTINUE INSIDE THIS SAME SCRIPT
// ============================================================
// ============================================================
//                     PART 4
//          PASSWORD GENERATOR, NOTES & SETTINGS
// ============================================================

// ============================================================
// PASSWORD GENERATOR
// ============================================================

function generatePassword() {
    const lengthInput = getElement("passwordLength");
    const numbersInput = getElement("includeNumbers");
    const symbolsInput = getElement("includeSymbols");

    const output = getElement("passwordOutput");

    if (!lengthInput || !output) return;

    const length = Math.max(
        4,
        Math.min(64, Number(lengthInput.value) || 16)
    );

    lengthInput.value = length;

    const letters =
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";

    const numbers = "0123456789";
    const symbols = "!@#$%^&*()-_=+[]{}?";

    let characters = letters;

    if (numbersInput && numbersInput.checked) {
        characters += numbers;
    }

    if (symbolsInput && symbolsInput.checked) {
        characters += symbols;
    }

    const randomValues = new Uint32Array(length);

    crypto.getRandomValues(randomValues);

    let password = "";

    for (let i = 0; i < length; i++) {
        password += characters[
            randomValues[i] % characters.length
        ];
    }

    output.textContent = password;

    vibrateDevice(30);
}

async function copyPassword() {
    const output = getElement("passwordOutput");

    if (!output) return;

    const password = output.textContent.trim();

    if (
        !password ||
        password === "Your password will appear here"
    ) {
        alert("Generate a password first.");
        return;
    }

    try {
        await navigator.clipboard.writeText(password);
        alert("Password copied!");
        vibrateDevice(35);

    } catch (error) {
        alert("Copy is unavailable in this browser.");
    }
}

// ============================================================
// NOTES STORAGE
// ============================================================

let notes = [];
let editingNoteId = null;

function loadNotes() {
    try {
        const savedNotes = localStorage.getItem(
            APP_STORAGE.notes
        );

        notes = savedNotes ? JSON.parse(savedNotes) : [];

        if (!Array.isArray(notes)) {
            notes = [];
        }

    } catch (error) {
        console.error("Notes loading error:", error);
        notes = [];
    }

    renderNotes();
}

function saveNotesToStorage() {
    try {
        localStorage.setItem(
            APP_STORAGE.notes,
            JSON.stringify(notes)
        );

    } catch (error) {
        alert("Unable to save notes on this device.");
    }
}

// ============================================================
// SAVE OR UPDATE NOTE
// ============================================================

function saveNote() {
    const titleInput = getElement("noteTitle");
    const textInput = getElement("noteText");

    if (!titleInput || !textInput) return;

    const title = titleInput.value.trim();
    const content = textInput.value.trim();

    if (!title && !content) {
        alert("Write something before saving.");
        return;
    }

    if (editingNoteId !== null) {
        const existingNote = notes.find(
            note => note.id === editingNoteId
        );

        if (existingNote) {
            existingNote.title = title || "Untitled";
            existingNote.content = content;
            existingNote.updatedAt = Date.now();
        }

    } else {
        notes.unshift({
            id: Date.now() + Math.random(),
            title: title || "Untitled",
            content: content,
            createdAt: Date.now(),
            updatedAt: Date.now()
        });
    }

    saveNotesToStorage();

    titleInput.value = "";
    textInput.value = "";

    editingNoteId = null;

    const saveButton = document.querySelector(
        "#notesPage .primary-btn"
    );

    if (saveButton) {
        saveButton.textContent = "Save Note";
    }

    renderNotes();
    vibrateDevice(35);
}

// ============================================================
// DISPLAY NOTES
// ============================================================

function renderNotes() {
    const container = getElement("notesList");

    if (!container) return;

    container.innerHTML = "";

    if (notes.length === 0) {
        const emptyMessage = document.createElement("p");

        emptyMessage.textContent = "No notes yet. Create your first note.";

        container.appendChild(emptyMessage);
        return;
    }

    notes.forEach(note => {
        const card = document.createElement("div");

        card.className = "note-card";

        const title = document.createElement("h3");
        title.textContent = note.title || "Untitled";

        const content = document.createElement("p");
        content.textContent = note.content || "";

        const editButton = document.createElement("button");
        editButton.className = "secondary-btn";
        editButton.textContent = "Edit";

        editButton.addEventListener("click", () => {
            editNote(note.id);
        });

        const deleteButton = document.createElement("button");
        deleteButton.className = "secondary-btn";
        deleteButton.textContent = "Delete";

        deleteButton.addEventListener("click", () => {
            deleteNote(note.id);
        });

        card.appendChild(title);
        card.appendChild(content);
        card.appendChild(editButton);
        card.appendChild(deleteButton);

        container.appendChild(card);
    });
}

// ============================================================
// EDIT NOTE
// ============================================================

function editNote(id) {
    const note = notes.find(item => item.id === id);

    if (!note) return;

    const titleInput = getElement("noteTitle");
    const textInput = getElement("noteText");

    if (!titleInput || !textInput) return;

    titleInput.value = note.title || "";
    textInput.value = note.content || "";

    editingNoteId = id;

    const saveButton = document.querySelector(
        "#notesPage .primary-btn"
    );

    if (saveButton) {
        saveButton.textContent = "Update Note";
    }

    titleInput.focus();

    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
}

// ============================================================
// DELETE NOTE
// ============================================================

function deleteNote(id) {
    const confirmed = confirm(
        "Are you sure you want to delete this note?"
    );

    if (!confirmed) return;

    notes = notes.filter(note => note.id !== id);

    if (editingNoteId === id) {
        editingNoteId = null;

        const titleInput = getElement("noteTitle");
        const textInput = getElement("noteText");

        if (titleInput) titleInput.value = "";
        if (textInput) textInput.value = "";
    }

    saveNotesToStorage();
    renderNotes();

    vibrateDevice(40);
}

// ============================================================
// SETTINGS INPUTS
// ============================================================

function updateSettingsInputs() {
    const nameInput = getElement("displayName");
    const lightToggle = getElement("lightModeToggle");
    const hapticToggle = getElement("hapticToggle");

    if (nameInput) {
        nameInput.value = appSettings.name;
    }

    if (lightToggle) {
        lightToggle.checked = appSettings.theme === "light";
    }

    if (hapticToggle) {
        hapticToggle.checked = appSettings.haptics;
    }
}

// ============================================================
// SAVE SETTINGS
// ============================================================

function saveSettings() {
    const nameInput = getElement("displayName");
    const lightToggle = getElement("lightModeToggle");
    const hapticToggle = getElement("hapticToggle");
    const pinInput = getElement("newPin");

    const newName = nameInput
        ? nameInput.value.trim()
        : appSettings.name;

    appSettings.name = newName || "mobile.app";

    appSettings.theme =
        lightToggle && lightToggle.checked
            ? "light"
            : "dark";

    appSettings.haptics =
        hapticToggle ? hapticToggle.checked : true;

    if (pinInput && pinInput.value.trim()) {
        const newPin = pinInput.value.trim();

        if (!/^\d{4,8}$/.test(newPin)) {
            alert("PIN must contain 4 to 8 digits.");
            return;
        }

        appSettings.pin = newPin;

        localStorage.setItem(
            APP_STORAGE.pin,
            newPin
        );

        pinInput.value = "";
    }

    localStorage.setItem(
        APP_STORAGE.name,
        appSettings.name
    );

    localStorage.setItem(
        APP_STORAGE.theme,
        appSettings.theme
    );

    localStorage.setItem(
        APP_STORAGE.haptics,
        String(appSettings.haptics)
    );

    applyTheme();

    const homeTitle = getElement("homeTitle");

    if (homeTitle) {
        homeTitle.textContent = appSettings.name;
    }

    alert("Settings saved successfully!");

    vibrateDevice(40);
}

// ============================================================
// END OF PART 4
// PART 5 CONTINUES INSIDE THE SAME SCRIPT
// ============================================================
// ============================================================
//                     PART 5
//          NUMBER GUESSING & TYPING SPEED GAME
// ============================================================


// ============================================================
// NUMBER GUESSING GAME
// ============================================================

let secretNumber = 0;
let guessAttempts = 10;
let guessGameOver = false;

function resetGuessGame() {
    secretNumber = Math.floor(Math.random() * 100) + 1;
    guessAttempts = 10;
    guessGameOver = false;

    const input = getElement("guessInput");

    if (input) {
        input.value = "";
        input.disabled = false;
    }

    setText(
        "guessMessage",
        "Guess a number between 1 and 100."
    );

    setText(
        "guessAttempts",
        "Attempts remaining: 10"
    );
}

function makeGuess() {
    if (guessGameOver) return;

    const input = getElement("guessInput");

    if (!input) return;

    const guess = Number(input.value);

    if (
        !Number.isInteger(guess) ||
        guess < 1 ||
        guess > 100
    ) {
        setText(
            "guessMessage",
            "Enter a valid number between 1 and 100."
        );
        return;
    }

    guessAttempts--;

    if (guess === secretNumber) {
        setText(
            "guessMessage",
            "🎉 Correct! You guessed the number!"
        );

        guessGameOver = true;
        input.disabled = true;

    } else if (guessAttempts <= 0) {
        setText(
            "guessMessage",
            "Game over! The number was " + secretNumber + "."
        );

        guessGameOver = true;
        input.disabled = true;

    } else if (guess < secretNumber) {
        setText(
            "guessMessage",
            "Too low! Try a higher number."
        );

    } else {
        setText(
            "guessMessage",
            "Too high! Try a lower number."
        );
    }

    setText(
        "guessAttempts",
        "Attempts remaining: " + guessAttempts
    );

    input.value = "";

    vibrateDevice(30);
}


// ============================================================
// TYPING SPEED GAME — DATA & STATE
// ============================================================

const typingParagraphs = [
    "Technology has changed the way people communicate, learn, and work. Modern devices help us complete everyday tasks more efficiently. Learning new skills can open many opportunities for the future.",

    "Success is not achieved in a single day. It requires patience, practice, consistency, and a willingness to learn from mistakes. Small improvements made regularly can lead to meaningful progress.",

    "The world of computers is constantly evolving. New ideas and inventions help people solve problems and explore possibilities. Creativity and curiosity are important parts of learning."
];

let typingTextContent = "";
let typingStarted = false;
let typingFinished = false;
let typingTimeLeft = 60;
let typingTimer = null;


// ============================================================
// PREPARE TYPING GAME
// ============================================================

function prepareTypingGame() {
    clearInterval(typingTimer);

    typingStarted = false;
    typingFinished = false;
    typingTimeLeft = 60;

    typingTextContent =
        typingParagraphs[
            Math.floor(Math.random() * typingParagraphs.length)
        ];

    const input = getElement("typingInput");

    if (input) {
        input.value = "";
        input.disabled = false;
    }

    setText("typingText", typingTextContent);
    setText("typingTime", "60");
    setText("typingWpm", "0");
    setText("typingAccuracy", "100");

    const startButton = document.querySelector(
        "#typingPage .primary-btn"
    );

    if (startButton) {
        startButton.disabled = false;
        startButton.textContent = "Start Typing Test";
    }
}


// ============================================================
// START TYPING GAME
// ============================================================

function startTypingGame() {
    if (typingStarted || typingFinished) {
        if (typingFinished) {
            prepareTypingGame();
        }

        return;
    }

    const input = getElement("typingInput");

    if (!input) return;

    typingStarted = true;
    input.focus();

    const startButton = document.querySelector(
        "#typingPage .primary-btn"
    );

    if (startButton) {
        startButton.disabled = true;
        startButton.textContent = "Test Running...";
    }

    clearInterval(typingTimer);

    typingTimer = setInterval(() => {
        typingTimeLeft--;

        setText("typingTime", String(typingTimeLeft));

        updateTypingStats();

        if (typingTimeLeft <= 0) {
            finishTypingGame();
        }

    }, 1000);
}


// ============================================================
// UPDATE TYPING STATISTICS
// ============================================================

function updateTypingStats() {
    const input = getElement("typingInput");

    if (!input) return;

    const typedText = input.value;

    const elapsedTime = Math.max(
        1,
        60 - typingTimeLeft
    );

    const correctCharacters = typedText
        .split("")
        .filter((character, index) => {
            return character === typingTextContent[index];
        }).length;

    const accuracy = typedText.length === 0
        ? 100
        : Math.round(
            (correctCharacters / typedText.length) * 100
        );

    const wordsTyped = typedText.trim()
        ? typedText.trim().split(/\s+/).length
        : 0;

    const wpm = Math.round(
        wordsTyped / (elapsedTime / 60)
    );

    setText("typingWpm", String(wpm));
    setText("typingAccuracy", String(accuracy));

    if (
        typedText.length >= typingTextContent.length
    ) {
        finishTypingGame();
    }
}


// ============================================================
// FINISH TYPING GAME
// ============================================================

function finishTypingGame() {
    if (typingFinished) return;

    typingFinished = true;
    typingStarted = false;

    clearInterval(typingTimer);

    const input = getElement("typingInput");

    if (input) {
        input.disabled = true;
    }

    const startButton = document.querySelector(
        "#typingPage .primary-btn"
    );

    if (startButton) {
        startButton.disabled = false;
        startButton.textContent = "Try Again";
    }

    setText(
        "typingTime",
        String(typingTimeLeft)
    );

    updateTypingStats();

    vibrateDevice(50);
}


// ============================================================
// TYPING INPUT EVENT
// ============================================================

const typingInputElement = getElement("typingInput");

if (typingInputElement) {
    typingInputElement.addEventListener("input", () => {
        if (!typingStarted && !typingFinished) {
            startTypingGame();
        }

        if (typingStarted) {
            updateTypingStats();
        }
    });
}


// ============================================================
// END OF PART 5
// PART 6 CONTINUES INSIDE THE SAME SCRIPT
// ============================================================
// ============================================================
//                     PART 6
//              FLAPPY BIRD GAME ENGINE
// ============================================================

// ============================================================
// CANVAS & GAME SETTINGS
// ============================================================

const flappyCanvas = getElement("flappyCanvas");
const flappyCtx = flappyCanvas
    ? flappyCanvas.getContext("2d")
    : null;

const FLAPPY_WIDTH = 360;
const FLAPPY_HEIGHT = 480;

let flappyAnimation = null;
let flappyRunning = false;
let flappyGameOver = false;

let flappyBird = {
    x: 85,
    y: 220,
    velocity: 0,
    radius: 14,
    rotation: 0
};

let flappyPipes = [];
let flappyScore = 0;
let flappyLastTime = 0;
let flappySpawnTimer = 0;

const FLAPPY_GRAVITY = 1250;
const FLAPPY_FLAP_POWER = -390;

const FLAPPY_INITIAL_SPEED = 145;
const FLAPPY_MAX_SPEED = 255;

const FLAPPY_INITIAL_GAP = 170;
const FLAPPY_MIN_GAP = 112;


// ============================================================
// DIFFICULTY SYSTEM
// ============================================================

function getFlappyDifficulty() {
    const level = Math.floor(flappyScore / 5);

    const speed = Math.min(
        FLAPPY_MAX_SPEED,
        FLAPPY_INITIAL_SPEED + level * 12
    );

    const gap = Math.max(
        FLAPPY_MIN_GAP,
        FLAPPY_INITIAL_GAP - level * 8
    );

    const spawnDistance = Math.max(
        175,
        230 - level * 5
    );

    return {
        speed,
        gap,
        spawnDistance
    };
}


// ============================================================
// RESET GAME
// ============================================================

function resetFlappyGame() {
    flappyBird = {
        x: 85,
        y: 220,
        velocity: 0,
        radius: 14,
        rotation: 0
    };

    flappyPipes = [];
    flappyScore = 0;
    flappySpawnTimer = 0;
    flappyLastTime = 0;

    flappyRunning = false;
    flappyGameOver = false;

    setText("flappyScore", "0");
    setText("flappyMessage", "Tap Start, then tap to fly!");

    drawFlappy();
}


// ============================================================
// CREATE PIPE
// ============================================================

function createFlappyPipe() {
    const difficulty = getFlappyDifficulty();

    const margin = 65;
    const availableHeight =
        FLAPPY_HEIGHT - difficulty.gap - margin * 2;

    const topHeight =
        margin + Math.random() * availableHeight;

    flappyPipes.push({
        x: FLAPPY_WIDTH + 10,
        top: topHeight,
        gap: difficulty.gap,
        passed: false
    });
}


// ============================================================
// DRAW BACKGROUND
// ============================================================

function drawFlappyBackground() {
    const gradient = flappyCtx.createLinearGradient(
        0, 0, 0, FLAPPY_HEIGHT
    );

    gradient.addColorStop(0, "#8bd9c0");
    gradient.addColorStop(0.65, "#d6edbd");
    gradient.addColorStop(1, "#f1d99b");

    flappyCtx.fillStyle = gradient;

    flappyCtx.fillRect(
        0, 0, FLAPPY_WIDTH, FLAPPY_HEIGHT
    );

    // Soft clouds
    flappyCtx.fillStyle = "rgba(255,255,255,0.65)";

    [
        [65, 90, 25],
        [245, 125, 32],
        [175, 55, 19]
    ].forEach(([x, y, r]) => {
        flappyCtx.beginPath();
        flappyCtx.arc(x, y, r, 0, Math.PI * 2);
        flappyCtx.arc(x + r, y + 5, r * 0.8, 0, Math.PI * 2);
        flappyCtx.arc(x - r, y + 7, r * 0.7, 0, Math.PI * 2);
        flappyCtx.fill();
    });

    // Ground
    flappyCtx.fillStyle = "#9cbd6c";
    flappyCtx.fillRect(
        0, FLAPPY_HEIGHT - 24,
        FLAPPY_WIDTH, 24
    );

    flappyCtx.fillStyle = "#658b48";
    flappyCtx.fillRect(
        0, FLAPPY_HEIGHT - 24,
        FLAPPY_WIDTH, 5
    );
}


// ============================================================
// DRAW BIRD CHARACTER
// ============================================================

function drawFlappyBird() {
    flappyCtx.save();

    flappyCtx.translate(
        flappyBird.x,
        flappyBird.y
    );

    flappyCtx.rotate(flappyBird.rotation);

    // Tail
    flappyCtx.fillStyle = "#d68a32";

    flappyCtx.beginPath();
    flappyCtx.moveTo(-12, 2);
    flappyCtx.lineTo(-25, -7);
    flappyCtx.lineTo(-22, 8);
    flappyCtx.closePath();
    flappyCtx.fill();

    // Body
    flappyCtx.fillStyle = "#f6b84a";

    flappyCtx.beginPath();
    flappyCtx.ellipse(
        0, 0, 18, 14,
        0, 0, Math.PI * 2
    );
    flappyCtx.fill();

    // Wing
    flappyCtx.fillStyle = "#e89b36";

    flappyCtx.beginPath();
    flappyCtx.ellipse(
        -4, 5, 9, 6,
        -0.25, 0, Math.PI * 2
    );
    flappyCtx.fill();

    // Eye
    flappyCtx.fillStyle = "#ffffff";

    flappyCtx.beginPath();
    flappyCtx.arc(8, -6, 5, 0, Math.PI * 2);
    flappyCtx.fill();

    flappyCtx.fillStyle = "#27352b";

    flappyCtx.beginPath();
    flappyCtx.arc(10, -6, 2, 0, Math.PI * 2);
    flappyCtx.fill();

    // Beak
    flappyCtx.fillStyle = "#ef713c";

    flappyCtx.beginPath();
    flappyCtx.moveTo(14, 0);
    flappyCtx.lineTo(25, 4);
    flappyCtx.lineTo(14, 8);
    flappyCtx.closePath();
    flappyCtx.fill();

    flappyCtx.restore();
}


// ============================================================
// DRAW PIPES
// ============================================================

function drawFlappyPipes() {
    flappyPipes.forEach(pipe => {
        const bottomY = pipe.top + pipe.gap;

        flappyCtx.fillStyle = "#438d61";
        flappyCtx.strokeStyle = "#276746";
        flappyCtx.lineWidth = 3;

        // Top pipe
        flappyCtx.fillRect(
            pipe.x, 0, 48, pipe.top
        );

        flappyCtx.strokeRect(
            pipe.x, -2, 48, pipe.top + 2
        );

        flappyCtx.fillStyle = "#65b67a";

        flappyCtx.fillRect(
            pipe.x - 5,
            pipe.top - 17,
            58,
            17
        );

        // Bottom pipe
        flappyCtx.fillStyle = "#438d61";

        flappyCtx.fillRect(
            pipe.x,
            bottomY,
            48,
            FLAPPY_HEIGHT - bottomY
        );

        flappyCtx.strokeRect(
            pipe.x,
            bottomY,
            48,
            FLAPPY_HEIGHT - bottomY
        );

        flappyCtx.fillStyle = "#65b67a";

        flappyCtx.fillRect(
            pipe.x - 5,
            bottomY,
            58,
            17
        );
    });
}


// ============================================================
// COLLISION DETECTION
// ============================================================

function checkFlappyCollision() {
    const bird = flappyBird;

    if (
        bird.y - bird.radius <= 0 ||
        bird.y + bird.radius >= FLAPPY_HEIGHT - 24
    ) {
        return true;
    }

    for (const pipe of flappyPipes) {
        const overlapsX =
            bird.x + bird.radius > pipe.x &&
            bird.x - bird.radius < pipe.x + 48;

        const hitsPipe =
            bird.y - bird.radius < pipe.top ||
            bird.y + bird.radius > pipe.top + pipe.gap;

        if (overlapsX && hitsPipe) {
            return true;
        }
    }

    return false;
}


// ============================================================
// UPDATE GAME
// ============================================================

function updateFlappy(deltaTime) {
    if (!flappyRunning) return;

    const difficulty = getFlappyDifficulty();

    flappyBird.velocity += FLAPPY_GRAVITY * deltaTime;

    flappyBird.y +=
        flappyBird.velocity * deltaTime;

    flappyBird.rotation = Math.max(
        -0.45,
        Math.min(0.9, flappyBird.velocity / 500)
    );

    flappySpawnTimer +=
        difficulty.speed * deltaTime;

    if (
        flappySpawnTimer >= difficulty.spawnDistance
    ) {
        createFlappyPipe();
        flappySpawnTimer = 0;
    }

    flappyPipes.forEach(pipe => {
        pipe.x -= difficulty.speed * deltaTime;

        if (
            !pipe.passed &&
            pipe.x + 48 < flappyBird.x
        ) {
            pipe.passed = true;
            flappyScore++;

            setText(
                "flappyScore",
                String(flappyScore)
            );

            vibrateDevice(15);
        }
    });

    flappyPipes = flappyPipes.filter(
        pipe => pipe.x > -60
    );

    if (checkFlappyCollision()) {
        endFlappyGame();
    }
}


// ============================================================
// DRAW GAME
// ============================================================

function drawFlappy() {
    if (!flappyCtx) return;

    drawFlappyBackground();
    drawFlappyPipes();
    drawFlappyBird();

    if (!flappyRunning && !flappyGameOver) {
        flappyCtx.fillStyle = "rgba(30,60,45,0.75)";
        flappyCtx.font = "bold 19px Arial";
        flappyCtx.textAlign = "center";

        flappyCtx.fillText(
            "READY?",
            FLAPPY_WIDTH / 2,
            185
        );
    }

    if (flappyGameOver) {
        flappyCtx.fillStyle = "rgba(30,45,35,0.65)";

        flappyCtx.fillRect(
            35, 175, 290, 105
        );

        flappyCtx.fillStyle = "#ffffff";
        flappyCtx.textAlign = "center";
        flappyCtx.font = "bold 25px Arial";

        flappyCtx.fillText(
            "GAME OVER",
            FLAPPY_WIDTH / 2,
            218
        );

        flappyCtx.font = "17px Arial";

        flappyCtx.fillText(
            "Score: " + flappyScore,
            FLAPPY_WIDTH / 2,
            249
        );
    }
}


// ============================================================
// ANIMATION LOOP
// ============================================================

function flappyLoop(timestamp) {
    if (!flappyRunning) return;

    if (!flappyLastTime) {
        flappyLastTime = timestamp;
    }

    const deltaTime = Math.min(
        (timestamp - flappyLastTime) / 1000,
        0.035
    );

    flappyLastTime = timestamp;

    updateFlappy(deltaTime);
    drawFlappy();

    if (flappyRunning) {
        flappyAnimation =
            requestAnimationFrame(flappyLoop);
    }
}


// ============================================================
// FLAP / TAP CONTROL
// ============================================================

function flapBird(event) {
    if (event) {
        event.preventDefault();
    }

    if (!flappyRunning || flappyGameOver) return;

    flappyBird.velocity = FLAPPY_FLAP_POWER;

    vibrateDevice(15);
}


// ============================================================
// START GAME
// ============================================================

function startFlappyGame() {
    if (!flappyCanvas || !flappyCtx) return;

    if (flappyAnimation) {
        cancelAnimationFrame(flappyAnimation);
    }

    resetFlappyGame();

    flappyRunning = true;
    flappyGameOver = false;

    setText("flappyMessage", "Tap anywhere on the game to fly!");

    flappyLastTime = 0;

    flappyAnimation =
        requestAnimationFrame(flappyLoop);

    vibrateDevice(30);
}


// ============================================================
// END GAME
// ============================================================

function endFlappyGame() {
    if (flappyGameOver) return;

    flappyRunning = false;
    flappyGameOver = true;

    if (flappyAnimation) {
        cancelAnimationFrame(flappyAnimation);
        flappyAnimation = null;
    }

    setText(
        "flappyMessage",
        "Game over! Tap Start Game to play again."
    );

    drawFlappy();

    vibrateDevice(100);
}


// ============================================================
// CANVAS TOUCH & MOUSE INPUT
// ============================================================

if (flappyCanvas) {
    flappyCanvas.addEventListener(
        "pointerdown",
        event => {
            if (!flappyRunning) return;

            flapBird(event);
        },
        { passive: false }
    );
}


// ============================================================
// INITIAL DRAW
// ============================================================

drawFlappy();


// ============================================================
// END OF PART 6
// PART 7 CONTINUES INSIDE THE SAME SCRIPT
// ============================================================
// ============================================================
//                     PART 7
//             PREMIUM SNAKE GAME ENGINE
// ============================================================

// ============================================================
// CANVAS & GAME CONFIGURATION
// ============================================================

const snakeCanvas = getElement("snakeCanvas");
const snakeCtx = snakeCanvas
    ? snakeCanvas.getContext("2d")
    : null;

const SNAKE_SIZE = 360;
const SNAKE_GRID = 20;
const SNAKE_CELL = SNAKE_SIZE / SNAKE_GRID;

const SNAKE_INITIAL_SPEED = 115;
const SNAKE_MIN_SPEED = 65;

let snakeBody = [];
let snakeDirection = { x: 1, y: 0 };
let snakeNextDirection = { x: 1, y: 0 };

let snakeFood = { x: 10, y: 10 };

let snakeScore = 0;
let snakeRunning = false;
let snakeGameOver = false;
let snakeGrowth = 0;

let snakeTimer = null;
let snakeLastMove = 0;
let snakeTouchStart = null;


// ============================================================
// RESET SNAKE GAME
// ============================================================

function resetSnakeGame() {
    clearInterval(snakeTimer);

    snakeBody = [
        { x: 8, y: 10 },
        { x: 7, y: 10 },
        { x: 6, y: 10 }
    ];

    snakeDirection = { x: 1, y: 0 };
    snakeNextDirection = { x: 1, y: 0 };

    snakeScore = 0;
    snakeGrowth = 0;

    snakeRunning = false;
    snakeGameOver = false;

    snakeLastMove = 0;
    snakeTouchStart = null;

    createSnakeFood();

    setText("snakeScore", "0");
    setText(
        "snakeMessage",
        "Swipe or use WASD / Arrow keys."
    );

    drawSnake();
}


// ============================================================
// CREATE APPLE
// ============================================================

function createSnakeFood() {
    let position;
    let attempts = 0;

    do {
        position = {
            x: Math.floor(Math.random() * SNAKE_GRID),
            y: Math.floor(Math.random() * SNAKE_GRID)
        };

        attempts++;

    } while (
        snakeBody.some(
            segment =>
                segment.x === position.x &&
                segment.y === position.y
        ) &&
        attempts < 1000
    );

    snakeFood = position;

    if (
        snakeBody.length >= SNAKE_GRID * SNAKE_GRID
    ) {
        endSnakeGame(true);
    }
}


// ============================================================
// SNAKE DIFFICULTY
// ============================================================

function getSnakeSpeed() {
    return Math.max(
        SNAKE_MIN_SPEED,
        SNAKE_INITIAL_SPEED - Math.floor(snakeScore / 3) * 5
    );
}


// ============================================================
// DIRECTION CONTROL
// ============================================================

function changeSnakeDirection(x, y) {
    if (!snakeRunning || snakeGameOver) return;

    // Prevent reversing directly into the snake's body.
    if (
        x === -snakeDirection.x &&
        y === -snakeDirection.y
    ) {
        return;
    }

    // Keep direction changes valid.
    if (
        x !== 0 && y !== 0
    ) {
        return;
    }

    snakeNextDirection = { x, y };
}


// ============================================================
// KEYBOARD CONTROLS
// ============================================================

document.addEventListener("keydown", event => {
    if (currentPage !== "snakePage") return;

    const key = event.key.toLowerCase();

    const directions = {
        arrowup: { x: 0, y: -1 },
        w: { x: 0, y: -1 },

        arrowdown: { x: 0, y: 1 },
        s: { x: 0, y: 1 },

        arrowleft: { x: -1, y: 0 },
        a: { x: -1, y: 0 },

        arrowright: { x: 1, y: 0 },
        d: { x: 1, y: 0 }
    };

    const direction = directions[key];

    if (!direction || !snakeRunning) return;

    event.preventDefault();

    changeSnakeDirection(
        direction.x,
        direction.y
    );
});


// ============================================================
// MOBILE SWIPE CONTROLS
// ============================================================

if (snakeCanvas) {

    snakeCanvas.style.touchAction = "none";

    snakeCanvas.addEventListener(
        "pointerdown",
        event => {
            if (!snakeRunning) return;

            snakeTouchStart = {
                x: event.clientX,
                y: event.clientY
            };
        },
        { passive: true }
    );

    snakeCanvas.addEventListener(
        "pointerup",
        event => {
            if (!snakeTouchStart || !snakeRunning) {
                snakeTouchStart = null;
                return;
            }

            const deltaX =
                event.clientX - snakeTouchStart.x;

            const deltaY =
                event.clientY - snakeTouchStart.y;

            const threshold = 12;

            if (
                Math.abs(deltaX) < threshold &&
                Math.abs(deltaY) < threshold
            ) {
                snakeTouchStart = null;
                return;
            }

            if (Math.abs(deltaX) > Math.abs(deltaY)) {
                changeSnakeDirection(
                    deltaX > 0 ? 1 : -1,
                    0
                );
            } else {
                changeSnakeDirection(
                    0,
                    deltaY > 0 ? 1 : -1
                );
            }

            snakeTouchStart = null;
        },
        { passive: true }
    );

    snakeCanvas.addEventListener(
        "pointercancel",
        () => {
            snakeTouchStart = null;
        }
    );
}


// ============================================================
// MOVE SNAKE
// ============================================================

function moveSnake() {
    if (!snakeRunning || snakeGameOver) return;

    snakeDirection = {
        x: snakeNextDirection.x,
        y: snakeNextDirection.y
    };

    const head = {
        x: snakeBody[0].x + snakeDirection.x,
        y: snakeBody[0].y + snakeDirection.y
    };

    // Wall collision.
    if (
        head.x < 0 ||
        head.y < 0 ||
        head.x >= SNAKE_GRID ||
        head.y >= SNAKE_GRID
    ) {
        endSnakeGame();
        return;
    }

    const eatingApple =
        head.x === snakeFood.x &&
        head.y === snakeFood.y;

    // The tail moves away unless the snake is growing.
    const bodyToCheck = eatingApple
        ? snakeBody
        : snakeBody.slice(0, -1);

    const collision = bodyToCheck.some(
        segment =>
            segment.x === head.x &&
            segment.y === head.y
    );

    if (collision) {
        endSnakeGame();
        return;
    }

    snakeBody.unshift(head);

    if (eatingApple) {
        // Keep the tail in place: snake grows by one segment.
        snakeGrowth++;

        snakeScore++;

        setText(
            "snakeScore",
            String(snakeScore)
        );

        createSnakeFood();

        vibrateDevice(35);

    } else {
        snakeBody.pop();
    }

    drawSnake();
}


// ============================================================
// DRAW SNAKE BACKGROUND
// ============================================================

function drawSnakeBackground() {
    const gradient = snakeCtx.createLinearGradient(
        0, 0, SNAKE_SIZE, SNAKE_SIZE
    );

    gradient.addColorStop(0, "#e7f4d9");
    gradient.addColorStop(1, "#c3dfbd");

    snakeCtx.fillStyle = gradient;

    snakeCtx.fillRect(
        0, 0, SNAKE_SIZE, SNAKE_SIZE
    );

    // Subtle grid.
    snakeCtx.strokeStyle = "rgba(65,110,75,0.10)";
    snakeCtx.lineWidth = 1;

    for (let i = 0; i <= SNAKE_GRID; i++) {
        const position = i * SNAKE_CELL;

        snakeCtx.beginPath();
        snakeCtx.moveTo(position, 0);
        snakeCtx.lineTo(position, SNAKE_SIZE);
        snakeCtx.stroke();

        snakeCtx.beginPath();
        snakeCtx.moveTo(0, position);
        snakeCtx.lineTo(SNAKE_SIZE, position);
        snakeCtx.stroke();
    }
}


// ============================================================
// DRAW APPLE
// ============================================================

function drawSnakeFood() {
    const x =
        snakeFood.x * SNAKE_CELL + SNAKE_CELL / 2;

    const y =
        snakeFood.y * SNAKE_CELL + SNAKE_CELL / 2;

    snakeCtx.fillStyle = "#e74b48";

    snakeCtx.beginPath();

    snakeCtx.arc(
        x, y, SNAKE_CELL * 0.38,
        0, Math.PI * 2
    );

    snakeCtx.fill();

    // Apple highlight.
    snakeCtx.fillStyle = "rgba(255,255,255,0.55)";

    snakeCtx.beginPath();

    snakeCtx.arc(
        x - 4, y - 4, 3,
        0, Math.PI * 2
    );

    snakeCtx.fill();

    // Stem.
    snakeCtx.strokeStyle = "#76502e";
    snakeCtx.lineWidth = 2;

    snakeCtx.beginPath();
    snakeCtx.moveTo(x, y - 7);
    snakeCtx.lineTo(x + 2, y - 11);
    snakeCtx.stroke();

    // Leaf.
    snakeCtx.fillStyle = "#378b50";

    snakeCtx.beginPath();
    snakeCtx.ellipse(
        x + 5, y - 10, 4, 2,
        -0.4, 0, Math.PI * 2
    );

    snakeCtx.fill();
}


// ============================================================
// DRAW SNAKE BODY
// ============================================================

function drawSnakeBody() {
    snakeBody.forEach((segment, index) => {
        const padding = 2;

        const x =
            segment.x * SNAKE_CELL + padding;

        const y =
            segment.y * SNAKE_CELL + padding;

        const size =
            SNAKE_CELL - padding * 2;

        const gradient = snakeCtx.createLinearGradient(
            x, y, x + size, y + size
        );

        if (index === 0) {
            gradient.addColorStop(0, "#16845a");
            gradient.addColorStop(1, "#07583e");
        } else {
            gradient.addColorStop(0, "#43ad78");
            gradient.addColorStop(1, "#16845a");
        }

        snakeCtx.fillStyle = gradient;

        snakeCtx.beginPath();

        snakeCtx.roundRect(
            x, y, size, size, 5
        );

        snakeCtx.fill();
    });

    drawSnakeEyes();
}


// ============================================================
// DRAW SNAKE EYES
// ============================================================

function drawSnakeEyes() {
    if (!snakeBody.length) return;

    const head = snakeBody[0];

    const centerX =
        head.x * SNAKE_CELL + SNAKE_CELL / 2;

    const centerY =
        head.y * SNAKE_CELL + SNAKE_CELL / 2;

    let eye1;
    let eye2;

    if (snakeDirection.x === 1) {
        eye1 = [centerX + 4, centerY - 4];
        eye2 = [centerX + 4, centerY + 4];

    } else if (snakeDirection.x === -1) {
        eye1 = [centerX - 4, centerY - 4];
        eye2 = [centerX - 4, centerY + 4];

    } else if (snakeDirection.y === -1) {
        eye1 = [centerX - 4, centerY - 4];
        eye2 = [centerX + 4, centerY - 4];

    } else {
        eye1 = [centerX - 4, centerY + 4];
        eye2 = [centerX + 4, centerY + 4];
    }

    snakeCtx.fillStyle = "#ffffff";

    [eye1, eye2].forEach(eye => {
        snakeCtx.beginPath();

        snakeCtx.arc(
            eye[0], eye[1], 2,
            0, Math.PI * 2
        );

        snakeCtx.fill();
    });
}


// ============================================================
// DRAW COMPLETE SNAKE GAME
// ============================================================

function drawSnake() {
    if (!snakeCtx) return;

    drawSnakeBackground();
    drawSnakeFood();
    drawSnakeBody();

    if (!snakeRunning && !snakeGameOver) {
        snakeCtx.fillStyle = "rgba(15,65,45,0.75)";
        snakeCtx.font = "bold 18px Arial";
        snakeCtx.textAlign = "center";

        snakeCtx.fillText(
            "PRESS START",
            SNAKE_SIZE / 2,
            25
        );
    }

    if (snakeGameOver) {
        snakeCtx.fillStyle = "rgba(15,45,32,0.75)";

        snakeCtx.fillRect(
            35, 135, 290, 90
        );

        snakeCtx.fillStyle = "#ffffff";
        snakeCtx.textAlign = "center";
        snakeCtx.font = "bold 24px Arial";

        snakeCtx.fillText(
            "GAME OVER",
            SNAKE_SIZE / 2,
            175
        );

        snakeCtx.font = "17px Arial";

        snakeCtx.fillText(
            "Score: " + snakeScore,
            SNAKE_SIZE / 2,
            204
        );
    }
}


// ============================================================
// END SNAKE GAME
// ============================================================

function endSnakeGame(won = false) {
    snakeRunning = false;
    snakeGameOver = true;

    clearInterval(snakeTimer);
    snakeTimer = null;

    setText(
        "snakeMessage",
        won
            ? "🏆 You filled the entire board!"
            : "Game over! Your score: " + snakeScore
    );

    drawSnake();

    vibrateDevice(100);
}


// ============================================================
// START SNAKE GAME
// ============================================================

function startSnakeGame() {
    if (!snakeCanvas || !snakeCtx) return;

    resetSnakeGame();

    snakeRunning = true;
    snakeGameOver = false;

    setText(
        "snakeMessage",
        "Swipe or use WASD / Arrow keys."
    );

    snakeLastMove = performance.now();

    snakeTimer = setInterval(() => {
        if (!snakeRunning) return;

        const now = performance.now();
        const speed = getSnakeSpeed();

        if (now - snakeLastMove >= speed) {
            snakeLastMove = now;
            moveSnake();
        }

    }, 8);

    vibrateDevice(30);
}


// ============================================================
// INITIAL SNAKE DRAW
// ============================================================

drawSnake();


// ============================================================
// END OF PART 7
// PART 8 WILL FINISH THE APP SCRIPT
// ============================================================
// ============================================================
//                     PART 8
//          FINAL INITIALIZATION & EVENT LISTENERS
// ============================================================


// ============================================================
// INITIALIZE APP AFTER ALL FUNCTIONS ARE DEFINED
// ============================================================

function startMobileApp() {
    initializeApp();

    // Initial calculator display
    updateCalcDisplay();

    // Initial game displays
    resetGuessGame();
    prepareTypingGame();
    resetFlappyGame();
    resetSnakeGame();

    // Restore saved settings
    updateSettingsInputs();

    // Set the app title
    const homeTitle = getElement("homeTitle");

    if (homeTitle) {
        homeTitle.textContent = appSettings.name;
    }
}


// ============================================================
// KEYBOARD SUPPORT FOR CALCULATOR
// ============================================================

document.addEventListener("keydown", event => {
    if (currentPage !== "calculator") return;

    const key = event.key;

    if (/^[0-9.]$/.test(key)) {
        appendCalc(key);
        return;
    }

    if (["+", "-", "*", "/", "%"].includes(key)) {
        appendCalc(key);
        return;
    }

    if (key === "Enter" || key === "=") {
        event.preventDefault();
        calculateResult();
        return;
    }

    if (key === "Backspace") {
        deleteCalc();
        return;
    }

    if (key === "Escape") {
        clearCalc();
    }
});


// ============================================================
// NUMBER GUESSING ENTER KEY SUPPORT
// ============================================================

const guessInputElement = getElement("guessInput");

if (guessInputElement) {
    guessInputElement.addEventListener("keydown", event => {
        if (event.key === "Enter") {
            event.preventDefault();
            makeGuess();
        }
    });
}


// ============================================================
// END OF PART 7
// PART 8 WILL FINISH THE APP SCRIPT
// ============================================================


// ============================================================
//                     PART 8
//          FINAL INITIALIZATION & EVENT LISTENERS
// ============================================================


// ============================================================
// INITIALIZE APP AFTER ALL FUNCTIONS ARE DEFINED
// ============================================================

function startMobileApp() {
    initializeApp();

    updateCalcDisplay();

    resetGuessGame();
    prepareTypingGame();
    resetFlappyGame();
    resetSnakeGame();

    updateSettingsInputs();

    const homeTitle = getElement("homeTitle");

    if (homeTitle) {
        homeTitle.textContent = appSettings.name;
    }
}


// ============================================================
// KEYBOARD SUPPORT FOR CALCULATOR
// ============================================================

document.addEventListener("keydown", event => {

    if (currentPage !== "calculator") return;

    const key = event.key;

    if (/^[0-9.]$/.test(key)) {
        appendCalc(key);
        return;
    }

    if (["+", "-", "*", "/", "%"].includes(key)) {
        appendCalc(key);
        return;
    }

    if (key === "Enter" || key === "=") {
        event.preventDefault();
        calculateResult();
        return;
    }

    if (key === "Backspace") {
        deleteCalc();
        return;
    }

    if (key === "Escape") {
        clearCalc();
    }
});


// ============================================================
// NUMBER GUESSING ENTER KEY SUPPORT
// ============================================================

const guessInputElement = getElement("guessInput");

if (guessInputElement) {

    guessInputElement.addEventListener("keydown", event => {

        if (event.key === "Enter") {
            event.preventDefault();
            makeGuess();
        }

    });

}


// ============================================================
// LIGHT MODE CHANGE
// ============================================================

const lightModeElement = getElement("lightModeToggle");

if (lightModeElement) {

    lightModeElement.addEventListener("change", () => {

        appSettings.theme = lightModeElement.checked
            ? "light"
            : "dark";

        applyTheme();

    });

}


// ============================================================
// HAPTIC SETTING CHANGE
// ============================================================

const hapticElement = getElement("hapticToggle");

if (hapticElement) {

    hapticElement.addEventListener("change", () => {

        appSettings.haptics = hapticElement.checked;

    });

}


// ============================================================
// INITIALIZE WHEN DOCUMENT IS READY
// ============================================================

if (document.readyState === "loading") {

    document.addEventListener(
        "DOMContentLoaded",
        startMobileApp,
        { once: true }
    );

} else {

    startMobileApp();

}


// ============================================================
// APP SCRIPT COMPLETED
// ============================================================

</script>

</body>
</html>
"""


# ============================================================
# STREAMLIT APP DISPLAY
# ============================================================

components.html(
    APP,
    height=900,
    scrolling=True
)
