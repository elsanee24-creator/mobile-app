
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
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* { box-sizing:border-box; }

html,body {
    margin:0;
    padding:0;
    width:100%;
    min-height:100%;
    font-family:Arial,sans-serif;
    background:#020805;
    color:white;
}

button {
    font-family:Arial,sans-serif;
    cursor:pointer;
    -webkit-tap-highlight-color:transparent;
}

#app {
    width:100%;
    max-width:460px;
    min-height:850px;
    margin:auto;
    padding:20px 14px 35px;
    background:linear-gradient(155deg,#081b10,#020805);
    color:white;
    position:relative;
    overflow:hidden;
}

.page { display:none; }
.page.active { display:block; }

.logo {
    text-align:center;
    color:#55ff91;
    font-size:27px;
    font-weight:900;
    margin:15px 0 28px;
    letter-spacing:1px;
}

.subtitle {
    text-align:center;
    color:#c6e9d0;
    font-size:14px;
}

/* LOGIN */
#login {
    min-height:810px;
    display:none;
    align-items:center;
    justify-content:center;
    flex-direction:column;
    padding:20px;
}
#login.active { display:flex; }

.login-logo {
    color:#55ff91;
    font-size:35px;
    font-weight:900;
    margin-bottom:12px;
}

.login-sub {
    color:#b9d9c4;
    margin-bottom:35px;
    text-align:center;
}

.login-btn {
    width:190px;
    height:65px;
    border-radius:18px;
    border:2px solid #55ff91;
    background:#123c24;
    color:#fff;
    font-size:21px;
    font-weight:bold;
    box-shadow:0 0 20px #20d96855;
}

/* HOME */
.home-grid {
    display:grid;
    grid-template-columns:repeat(3,minmax(0,1fr));
    gap:9px;
    width:100%;
    margin-top:45px;
}

.home-card {
    aspect-ratio:1 / 1;
    min-width:0;
    border:2px solid #25d968;
    border-radius:17px;
    background:linear-gradient(145deg,#164329,#081b10);
    color:#65ff9c;
    display:flex;
    flex-direction:column;
    align-items:center;
    justify-content:center;
    gap:9px;
    font-weight:bold;
    font-size:12px;
    padding:5px;
    text-align:center;
    overflow-wrap:anywhere;
}

.home-icon { font-size:29px; }

.logout {
    margin-top:45px;
    width:100%;
    height:48px;
    background:#15281c;
    border:1px solid #55ff91;
    border-radius:12px;
    color:#55ff91;
    font-weight:bold;
}

/* COMMON */
.back {
    width:100%;
    height:47px;
    margin-top:22px;
    background:#102b1c;
    color:#55ff91;
    border:1px solid #20d968;
    border-radius:12px;
    font-weight:bold;
}

.heading {
    color:#55ff91;
    text-align:center;
    font-size:23px;
    margin:15px 0 20px;
}

/* CALCULATOR */
#calculator {
    background:#101820;
    border-radius:20px;
    padding:14px;
    border:1px solid #53616c;
}

.calc-display {
    width:100%;
    min-height:105px;
    padding:20px 12px;
    margin-bottom:15px;
    border-radius:13px;
    background:#edf1f4;
    color:#18222b;
    display:flex;
    align-items:center;
    justify-content:flex-end;
    font-size:35px;
    font-weight:bold;
    overflow-wrap:anywhere;
    word-break:break-all;
    text-align:right;
}

.calc-grid {
    display:grid;
    grid-template-columns:repeat(4,minmax(0,1fr));
    gap:9px;
}

.calc-key {
    width:100%;
    min-width:0;
    height:65px;
    border-radius:14px;
    border:0;
    background:#f1f3f5;
    color:#1c252c;
    font-size:21px;
    font-weight:bold;
    box-shadow:0 3px 0 #aab2b8;
}

.calc-key.operator {
    background:#ff9638;
    color:white;
    box-shadow:0 3px 0 #c96b1d;
}

.calc-key.equal {
    background:#ff7e1f;
    color:white;
    box-shadow:0 3px 0 #b9560d;
}

.calc-key:active { transform:scale(.96); }

/* GUESS GAME */
#guess {
    background:linear-gradient(145deg,#25115c,#153b8d,#071a49);
    border-radius:20px;
    min-height:700px;
    padding:16px;
    border:1px solid #7885ff;
    box-shadow:0 0 22px #554dff33;
}

.guess-title {
    text-align:center;
    color:#d9d5ff;
    font-size:24px;
    font-weight:900;
    margin:15px 0;
}

.guess-info {
    text-align:center;
    color:#d5ddff;
    font-size:15px;
    margin:15px 0;
}

.guess-card {
    background:#101f56aa;
    border:1px solid #8290ff;
    border-radius:16px;
    padding:17px;
    text-align:center;
    margin:20px 0;
}

#guessInput {
    width:100%;
    height:58px;
    border-radius:13px;
    border:2px solid #a4aaff;
    background:#f5f5ff;
    color:#20204a;
    text-align:center;
    font-size:23px;
    font-weight:bold;
}

.guess-submit,.new-game {
    width:100%;
    height:55px;
    border:0;
    border-radius:13px;
    margin-top:14px;
    background:linear-gradient(90deg,#8b5cf6,#3679ff);
    color:white;
    font-size:17px;
    font-weight:bold;
}

.guess-message {
    min-height:45px;
    text-align:center;
    color:white;
    font-weight:bold;
    margin-top:18px;
    font-size:17px;
}

/* FLAPPY BIRD */
#flappy {
    background:#061b2d;
    border-radius:20px;
    padding:12px;
    border:1px solid #28b9ff;
}

#birdCanvas {
    width:100%;
    height:auto;
    display:block;
    border:2px solid #5acbff;
    border-radius:13px;
    background:#63c9ff;
    touch-action:manipulation;
}

.jump-btn {
    width:100%;
    height:60px;
    margin-top:13px;
    border:2px solid #27d968;
    border-radius:15px;
    background:#123b25;
    color:#65ff9b;
    font-size:22px;
    font-weight:bold;
}

.game-hint {
    color:#b8eaff;
    text-align:center;
    font-size:13px;
    margin:12px 0 5px;
}

@media(max-width:350px) {
    #app { padding-left:9px; padding-right:9px; }
    .home-grid { gap:5px; }
    .home-card { font-size:10px; border-radius:12px; }
    .home-icon { font-size:24px; }
    .calc-grid { gap:6px; }
    .calc-key { height:57px; font-size:18px; }
}
</style>
</head>

<body>
<div id="app">

<!-- LOGIN -->
<section id="login" class="page active">
    <div class="login-logo">📱 mobile.app</div>
    <div class="login-sub">Your little world of useful tools</div>
    <button class="login-btn" onclick="go('home')">LOGIN</button>
</section>

<!-- HOME -->
<section id="home" class="page">
    <div class="logo">📱 mobile.app</div>
    <div class="subtitle">Choose your tool</div>

    <div class="home-grid">
        <button class="home-card" onclick="go('calculator')">
            <span class="home-icon">🧮</span>
            <span>Calculator</span>
        </button>

        <button class="home-card" onclick="go('guess')">
            <span class="home-icon">🎮</span>
            <span>Number Guessing</span>
        </button>

        <button class="home-card" onclick="go('flappy')">
            <span class="home-icon">🐦</span>
            <span>Flappy Bird</span>
        </button>
    </div>

    <button class="logout" onclick="go('login')">LOG OUT</button>
</section>

<!-- CALCULATOR -->
<section id="calculator" class="page">
    <div class="heading">CALCULATOR</div>

    <div class="calc-display" id="calcDisplay">0</div>

    <div class="calc-grid">
        <button class="calc-key" onclick="calcPress('AC')">AC</button>
        <button class="calc-key" onclick="calcPress('+/-')">+/−</button>
        <button class="calc-key" onclick="calcPress('%')">%</button>
        <button class="calc-key operator" onclick="calcPress('/')">÷</button>

        <button class="calc-key" onclick="calcPress('7')">7</button>
        <button class="calc-key" onclick="calcPress('8')">8</button>
        <button class="calc-key" onclick="calcPress('9')">9</button>
        <button class="calc-key operator" onclick="calcPress('*')">×</button>

        <button class="calc-key" onclick="calcPress('4')">4</button>
        <button class="calc-key" onclick="calcPress('5')">5</button>
        <button class="calc-key" onclick="calcPress('6')">6</button>
        <button class="calc-key operator" onclick="calcPress('-')">−</button>

        <button class="calc-key" onclick="calcPress('1')">1</button>
        <button class="calc-key" onclick="calcPress('2')">2</button>
        <button class="calc-key" onclick="calcPress('3')">3</button>
        <button class="calc-key operator" onclick="calcPress('+')">+</button>

        <button class="calc-key" onclick="calcPress('DEL')">DEL</button>
        <button class="calc-key" onclick="calcPress('0')">0</button>
        <button class="calc-key" onclick="calcPress('.')">.</button>
        <button class="calc-key equal" onclick="calcPress('=')">=</button>
    </div>

    <button class="back" onclick="go('home')">⬅ BACK TO HOME</button>
</section>

<!-- NUMBER GUESSING -->
<section id="guess" class="page">
    <div class="guess-title">🎮 NUMBER GUESSING</div>

    <div class="guess-info">
        Guess a secret number between 1 and 100!
    </div>

    <div class="guess-card">
        <div style="font-size:45px">🔮</div>
        <div style="color:#dce2ff;font-size:16px;margin:12px 0">
            Your remaining chances
        </div>
        <div id="chances" style="font-size:32px;font-weight:bold;color:#fff">
            10 / 10
        </div>
    </div>

    <input id="guessInput" type="number" min="1" max="100"
           placeholder="Enter your number">

    <button class="guess-submit" id="guessSubmit" onclick="submitGuess()">
        SUBMIT GUESS
    </button>

    <div class="guess-message" id="guessMessage">
        Good luck!
    </div>

    <button class="new-game" onclick="newGame()">↻ NEW GAME</button>
    <button class="back" onclick="go('home')">⬅ BACK TO HOME</button>
</section>

<!-- FLAPPY BIRD -->
<section id="flappy" class="page">
    <div class="heading">🐦 FLAPPY BIRD</div>

    <canvas id="birdCanvas" width="360" height="480"></canvas>

    <button class="jump-btn" id="jumpButton" onclick="jumpBird()">
        ⬆ JUMP
    </button>

    <div class="game-hint">Tap JUMP to fly. Avoid the pipes!</div>

    <button class="back" onclick="go('home')">⬅ BACK TO HOME</button>
</section>

</div>

<script>
/* ---------- NAVIGATION ---------- */
function go(id) {
    document.querySelectorAll('.page').forEach(p => {
        p.classList.remove('active');
    });
    document.getElementById(id).classList.add('active');

    if(id === 'flappy') {
        drawBirdGame();
    }
}

/* ---------- CALCULATOR ---------- */
let calcValue = "0";
let calcFirst = null;
let calcOperator = null;
let calcWaiting = false;

function showCalc() {
    document.getElementById('calcDisplay').textContent = calcValue;
}

function cleanNumber(n) {
    if(!Number.isFinite(n)) return "Error";
    return String(Number(n.toPrecision(11)));
}

function calcPress(key) {
    if(key === 'AC') {
        calcValue = "0";
        calcFirst = null;
        calcOperator = null;
        calcWaiting = false;
        showCalc();
        return;
    }

    if(key === 'DEL') {
        if(calcWaiting) return;
        if(calcValue === "Error") {
            calcValue = "0";
        } else {
            calcValue = calcValue.length > 1
                ? calcValue.slice(0,-1) : "0";
        }
        showCalc();
        return;
    }

    if(key === '+/-') {
        if(calcValue !== "Error") {
            calcValue = cleanNumber(-Number(calcValue));
        }
        showCalc();
        return;
    }

    if(key === '%') {
        if(calcValue !== "Error") {
            calcValue = cleanNumber(Number(calcValue)/100);
        }
        showCalc();
        return;
    }

    if("0123456789".includes(key)) {
        if(calcValue === "Error" || calcWaiting || calcValue === "0") {
            calcValue = key;
            calcWaiting = false;
        } else {
            calcValue += key;
        }
        showCalc();
        return;
    }

    if(key === '.') {
        if(calcWaiting || calcValue === "Error") {
            calcValue = "0.";
            calcWaiting = false;
        } else if(!calcValue.includes('.')) {
            calcValue += '.';
        }
        showCalc();
        return;
    }

    if(['+','-','*','/'].includes(key)) {
        if(calcValue === "Error") return;

        let current = Number(calcValue);

        if(calcOperator && !calcWaiting) {
            let result = calculateCalc(
                calcFirst,current,calcOperator
            );
            if(result === null) {
                calcValue = "Cannot divide by zero";
                calcFirst = null;
                calcOperator = null;
                calcWaiting = true;
                showCalc();
                return;
            }
            current = result;
            calcValue = cleanNumber(result);
        }

        calcFirst = current;
        calcOperator = key;
        calcWaiting = true;
        showCalc();
        return;
    }

    if(key === '=' && calcOperator !== null) {
        let result = calculateCalc(
            calcFirst,Number(calcValue),calcOperator
        );

        calcValue = result === null
            ? "Cannot divide by zero"
            : cleanNumber(result);

        calcFirst = null;
        calcOperator = null;
        calcWaiting = true;
        showCalc();
    }
}

function calculateCalc(a,b,op) {
    if(op === '+') return a+b;
    if(op === '-') return a-b;
    if(op === '*') return a*b;
    if(op === '/') return b === 0 ? null : a/b;
}

/* ---------- NUMBER GUESSING ---------- */
let secretNumber = Math.floor(Math.random()*100)+1;
let tries = 0;
let finished = false;

function updateChances() {
    document.getElementById('chances').textContent =
        (10-tries) + " / 10";
}

function submitGuess() {
    if(finished) return;

    const input = document.getElementById('guessInput');
    const guess = Number(input.value);
    const message = document.getElementById('guessMessage');

    if(!input.value || !Number.isInteger(guess) || guess < 1 || guess > 100) {
        message.textContent = "Enter a number from 1 to 100!";
        return;
    }

    tries++;

    if(guess === secretNumber) {
        message.textContent = "Yay! You won !!!!";
        finished = true;
    } else if(tries >= 10) {
        message.textContent = "Oops! You're out of tries";
        finished = true;
    } else if(guess < secretNumber) {
        message.textContent = "Too low! Try higher.";
    } else {
        message.textContent = "Too high! Try lower.";
    }

    updateChances();

    if(finished) {
        document.getElementById('guessSubmit').disabled = true;
        document.getElementById('guessSubmit').style.opacity = ".5";
    }

    input.value = "";
}

function newGame() {
    secretNumber = Math.floor(Math.random()*100)+1;
    tries = 0;
    finished = false;

    document.getElementById('guessMessage').textContent = "Good luck!";
    document.getElementById('guessInput').value = "";
    document.getElementById('guessSubmit').disabled = false;
    document.getElementById('guessSubmit').style.opacity = "1";

    updateChances();
}

/* ---------- FLAPPY BIRD ---------- */
const canvas = document.getElementById('birdCanvas');
const ctx = canvas.getContext('2d');

let bird = {};
let pipes = [];
let birdScore = 0;
let birdFrame = 0;
let birdRunning = false;
let birdStarted = false;

function resetBird() {
    bird = {x:75,y:220,velocity:0,radius:12};
    pipes = [];
    birdScore = 0;
    birdFrame = 0;
    birdRunning = false;
    birdStarted = false;
    drawBirdGame();
}

function jumpBird() {
    if(!birdStarted) {
        birdStarted = true;
        birdRunning = true;
        bird.velocity = -6.5;
    } else if(birdRunning) {
        bird.velocity = -6.5;
    } else {
        resetBird();
        birdStarted = true;
        birdRunning = true;
        bird.velocity = -6.5;
    }
}

function drawCloud(x,y,s) {
    ctx.fillStyle = "white";
    ctx.beginPath();
    ctx.arc(x,y,17*s,0,Math.PI*2);
    ctx.arc(x+19*s,y-9*s,21*s,0,Math.PI*2);
    ctx.arc(x+42*s,y,16*s,0,Math.PI*2);
    ctx.fill();
}

function drawBirdGame() {
    const sky = ctx.createLinearGradient(0,0,0,480);
    sky.addColorStop(0,"#42b7ff");
    sky.addColorStop(1,"#b9edff");

    ctx.fillStyle = sky;
    ctx.fillRect(0,0,360,480);

    drawCloud(40,90,.8);
    drawCloud(225,140,.7);
    drawCloud(140,45,.5);

    for(const p of pipes) {
        ctx.fillStyle = "#20b84a";
        ctx.fillRect(p.x,0,48,p.top);
        ctx.fillRect(p.x,p.bottom,48,480-p.bottom);

        ctx.fillStyle = "#49e879";
        ctx.fillRect(p.x-4,p.top-12,56,12);
        ctx.fillRect(p.x-4,p.bottom,56,12);
    }

    ctx.fillStyle = "#ffe34a";
    ctx.beginPath();
    ctx.arc(bird.x,bird.y,bird.radius,0,Math.PI*2);
    ctx.fill();

    ctx.fillStyle = "#fff";
    ctx.beginPath();
    ctx.arc(bird.x+4,bird.y-4,3,0,Math.PI*2);
    ctx.fill();

    ctx.fillStyle = "#ff8b32";
    ctx.beginPath();
    ctx.moveTo(bird.x+10,bird.y);
    ctx.lineTo(bird.x+19,bird.y+4);
    ctx.lineTo(bird.x+10,bird.y+7);
    ctx.fill();

    ctx.fillStyle = "#143b65";
    ctx.font = "bold 26px Arial";
    ctx.textAlign = "center";
    ctx.fillText("Score: "+birdScore,180,35);

    if(!birdStarted) {
        ctx.font = "bold 20px Arial";
        ctx.fillText("TAP JUMP TO START",180,250);
    }

    if(birdStarted && !birdRunning) {
        ctx.font = "bold 26px Arial";
        ctx.fillText("GAME OVER",180,220);
        ctx.font = "18px Arial";
        ctx.fillText("Tap JUMP to restart",180,255);
    }
}

function addBirdPipe() {
    const gap = 145;
    const top = 55 + Math.random()*185;
    pipes.push({
        x:360,
        top:top,
        bottom:top+gap,
        scored:false
    });
}

function updateBirdGame() {
    if(birdRunning) {
        birdFrame++;
        bird.velocity += .38;
        bird.y += bird.velocity;

        if(birdFrame % 95 === 0) {
            addBirdPipe();
        }

        for(const p of pipes) {
            p.x -= 2.3;

            if(!p.scored && p.x+48 < bird.x) {
                p.scored = true;
                birdScore++;
            }

            const horizontal =
                bird.x+bird.radius > p.x &&
                bird.x-bird.radius < p.x+48;

            const vertical =
                bird.y-bird.radius < p.top ||
                bird.y+bird.radius > p.bottom;

            if(horizontal && vertical) {
                birdRunning = false;
                break;
            }
        }

        pipes = pipes.filter(p => p.x > -60);

        if(bird.y+bird.radius >= 480 ||
           bird.y-bird.radius <= 0) {
            birdRunning = false;
        }
    }

    drawBirdGame();
    requestAnimationFrame(updateBirdGame);
}

canvas.addEventListener('click',jumpBird);

document.addEventListener('keydown',function(e) {
    if(e.code === "Space" || e.code === "ArrowUp") {
        const flappyPage = document.getElementById('flappy');
        if(flappyPage.classList.contains('active')) {
            e.preventDefault();
            jumpBird();
        }
    }
});

resetBird();
updateBirdGame();
</script>
</body>
</html>
"""

components.html(APP, height=900, scrolling=True)
