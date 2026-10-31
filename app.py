
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
html,body{
    margin:0;padding:0;width:100%;height:100%;
    overflow:hidden;font-family:Arial,sans-serif;
    background:#08091b;color:#fff;
}
.app{
    width:100%;max-width:410px;
    height:calc(100dvh - 12px);
    min-height:0;margin:6px auto;
    overflow:hidden;position:relative;
    border:1px solid #514b83;border-radius:25px;
    background:
      radial-gradient(ellipse at 15% 15%,#512b85 0,transparent 42%),
      radial-gradient(ellipse at 90% 45%,#075b83 0,transparent 40%),
      linear-gradient(145deg,#10102b,#080d22 65%,#101a37);
    box-shadow:0 0 35px #5b3b9a55;
}
.screen{
    display:none;height:100%;padding:15px;
    overflow-y:auto;overscroll-behavior:contain;
    scrollbar-width:none;
}
.screen::-webkit-scrollbar{display:none}
.screen.active{display:block}
.glass{
    background:#ffffff12;border:1px solid #ffffff25;
    border-radius:18px;padding:14px;
    backdrop-filter:blur(12px);
}
h1,h2,h3{margin-top:0}
h1{font-size:25px}
h2{font-size:21px}
.muted{color:#b7b7d7;font-size:12px}
input,select{
    width:100%;padding:11px;margin:6px 0;
    border-radius:12px;border:1px solid #ffffff35;
    background:#ffffff12;color:white;font-size:14px;
    outline:none;
}
input::placeholder{color:#aaa}
button{
    border:0;border-radius:12px;padding:11px;
    background:linear-gradient(110deg,#6c42dd,#08a9ce);
    color:white;font-weight:bold;font-size:13px;
    cursor:pointer;
}
button:active{transform:scale(.97)}
.primary{width:100%;margin:5px 0}
.secondary{background:#ffffff18;border:1px solid #ffffff25}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:9px}
.tile{
    min-height:82px;text-align:left;padding:11px;
    background:#ffffff12;border:1px solid #ffffff20;
    border-radius:16px;color:white;font-size:12px;
}
.tile span{display:block;font-size:23px;margin-bottom:5px}
.top{display:flex;justify-content:space-between;align-items:center}
.back{background:#ffffff17;padding:8px 12px}
.clockrow{display:flex;align-items:center;gap:14px;margin:8px 0 18px}
.clockicon{font-size:51px;color:#69e5ff}
#time{font-size:35px;font-weight:bold;letter-spacing:1px}
#date{font-size:12px;color:#b7b7d7}
.fingerprint{
    width:55px;height:55px;border-radius:50%;
    border:1px solid #7beaff;background:#ffffff12;
    display:block;margin:12px auto;font-size:27px;
}
#calcDisplay{
    width:100%;height:60px;font-size:25px;text-align:right;
    background:#ffffff14;color:white;
}
.calcgrid{display:grid;grid-template-columns:repeat(4,1fr);gap:7px}
.calcgrid button{height:49px;font-size:18px}
#gameCanvas{
    width:100%;background:#07162a;
    border:1px solid #ffffff35;border-radius:14px;
    touch-action:none;
}
.controls{
    display:grid;grid-template-columns:repeat(3,1fr);
    gap:7px;margin:9px auto;max-width:220px
}
.controls button{font-size:19px}
.center{text-align:center}
.stat{display:flex;justify-content:space-between;margin:8px 0}
.small{font-size:11px;color:#b7b7d7}
#guessMessage{min-height:22px}

/* LOGIN LOADING */
#loadingScreen{
    display:none;position:absolute;inset:0;z-index:50;
    background:
      radial-gradient(ellipse at 50% 40%,#30206b,#080d22 70%);
    align-items:center;justify-content:center;
    flex-direction:column;text-align:center;
}
#loadingScreen.show{display:flex}
.loader{
    width:72px;height:72px;border-radius:50%;
    border:4px solid #ffffff20;
    border-top-color:#65eaff;
    border-right-color:#8b62ff;
    animation:spin .8s linear infinite;
    box-shadow:0 0 25px #36cfff55;
}
@keyframes spin{to{transform:rotate(360deg)}}
.loadingTitle{
    margin-top:24px;font-size:21px;font-weight:bold;
    letter-spacing:1px;
}
.loadingText{color:#aebce0;font-size:12px;margin-top:9px}
.progress{
    width:190px;height:5px;background:#ffffff20;
    border-radius:10px;margin-top:22px;overflow:hidden;
}
.progressBar{
    height:100%;width:0%;
    background:linear-gradient(90deg,#8054ff,#55eaff);
    border-radius:10px;
    animation:progress 2s linear forwards;
}
@keyframes progress{to{width:100%}}
#app.fadeIn{animation:enter .35s ease}
@keyframes enter{
    from{opacity:.2;transform:scale(.985)}
    to{opacity:1;transform:scale(1)}
}
</style>
</head>
<body>
<div class="app" id="app">

<!-- LOGIN -->
<section class="screen active" id="login">
    <div class="clockrow">
        <div class="clockicon">◷</div>
        <div>
            <div id="time">00:00:00</div>
            <div id="date">Loading date...</div>
        </div>
    </div>

    <div style="margin-top:24px">
        <div class="center">
            <div style="font-size:43px">✦</div>
            <h1>mobile.app</h1>
            <p class="muted">Your personal digital space</p>
        </div>
        <div class="glass">
            <input id="username" placeholder="Username">
            <input id="password" type="password" placeholder="Password">
            <button class="primary" onclick="loginUser()">LOGIN</button>
            <button class="primary secondary" onclick="guestLogin()">CONTINUE AS GUEST</button>
            <button class="fingerprint" onclick="fingerprintLogin()" title="Demo fingerprint">♧</button>
            <p class="small center">Fingerprint button is a demo shortcut.</p>
        </div>
    </div>
</section>

<!-- HOME -->
<section class="screen" id="home">
    <div class="top">
        <div><p class="muted">WELCOME TO</p><h1>mobile.app ✦</h1></div>
        <button class="back" onclick="goLogin()">Exit</button>
    </div>
    <div class="glass" style="margin:12px 0">
        <h2 id="welcome">Hello!</h2>
        <p class="muted">Choose an application to continue.</p>
    </div>
    <div class="grid">
        <button class="tile" onclick="openApp('calculator')"><span>🧮</span>Calculator</button>
        <button class="tile" onclick="openApp('passwordgen')"><span>🔐</span>Password Generator</button>
        <button class="tile" style="min-height:105px" onclick="openApp('gaming')"><span style="font-size:34px">🧩</span>Gaming Hub</button>
    </div>
    <div class="glass" style="margin-top:12px">
        <div class="top"><b>Appearance</b>
        <select id="theme" onchange="changeTheme()" style="width:125px;margin:0">
            <option value="cosmic">Cosmic</option>
            <option value="blue">Blue</option>
            <option value="purple">Purple</option>
            <option value="light">Light</option>
            <option value="dark">Dark</option>
        </select></div>
    </div>
</section>

<!-- GAMING HUB -->
<section class="screen" id="gaming">
    <div class="top"><h2>🧩 Gaming Hub</h2><button class="back" onclick="goHome()">Back</button></div>
    <div class="glass" style="padding:18px;margin:12px 0">
        <div class="center" style="font-size:38px">🧩</div>
        <h2 class="center">Gaming Zone</h2>
        <p class="muted center">Choose your game and have fun!</p>
    </div>
    <div class="grid">
        <button class="tile" onclick="openApp('flappy')"><span>🐦</span>Flappy Bird</button>
        <button class="tile" onclick="openApp('guess')"><span>🔢</span>Number Guess</button>
        <button class="tile" onclick="openApp('snake')"><span>🐍</span>Snake.io</button>
    </div>
</section>

<!-- CALCULATOR -->
<section class="screen" id="calculator">
    <div class="top"><h2>🧮 Calculator</h2><button class="back" onclick="goHome()">Back</button></div>
    <input id="calcDisplay" readonly placeholder="0">
    <div class="calcgrid">
        <button class="secondary" onclick="clearCalc()">C</button>
        <button class="secondary" onclick="calcAdd('(')">(</button>
        <button class="secondary" onclick="calcAdd(')')">)</button>
        <button onclick="calcAdd('/')">÷</button>
        <button class="secondary" onclick="calcAdd('7')">7</button>
        <button class="secondary" onclick="calcAdd('8')">8</button>
        <button class="secondary" onclick="calcAdd('9')">9</button>
        <button onclick="calcAdd('*')">×</button>
        <button class="secondary" onclick="calcAdd('4')">4</button>
        <button class="secondary" onclick="calcAdd('5')">5</button>
        <button class="secondary" onclick="calcAdd('6')">6</button>
        <button onclick="calcAdd('-')">−</button>
        <button class="secondary" onclick="calcAdd('1')">1</button>
        <button class="secondary" onclick="calcAdd('2')">2</button>
        <button class="secondary" onclick="calcAdd('3')">3</button>
        <button onclick="calcAdd('+')">+</button>
        <button class="secondary" onclick="calcAdd('0')">0</button>
        <button class="secondary" onclick="calcAdd('.')">.</button>
        <button class="secondary" onclick="calcBack()">⌫</button>
        <button onclick="calculate()">=</button>
    </div>
</section>

<!-- PASSWORD GENERATOR -->
<section class="screen" id="passwordgen">
    <div class="top"><h2>🔐 Password Generator</h2><button class="back" onclick="goHome()">Back</button></div>
    <div class="glass">
        <label>Password length</label>
        <input id="passLength" type="number" min="4" max="40" value="16">
        <button class="primary" onclick="generatePassword()">GENERATE PASSWORD</button>
        <input id="generatedPass" readonly placeholder="Your password appears here">
        <button class="primary secondary" onclick="copyPassword()">COPY PASSWORD</button>
    </div>
</section>

<!-- NUMBER GUESS -->
<section class="screen" id="guess">
    <div class="top"><h2>🔢 Number Guess</h2><button class="back" onclick="backToHub()">Back</button></div>
    <div class="glass center">
        <h3>Guess the number!</h3>
        <p class="muted">Choose a number between 1 and 100.</p>
        <input id="guessInput" type="number" placeholder="Enter your guess">
        <button class="primary" onclick="checkGuess()">CHECK</button>
        <p id="guessMessage"></p>
        <p id="guessCount" class="muted">Attempts: 0</p>
        <button class="secondary" onclick="resetGuess()">New Game</button>
    </div>
</section>

<!-- FLAPPY BIRD -->
<section class="screen" id="flappy">
    <div class="top"><h2>🐦 Flappy Bird</h2><button class="back" onclick="backToHub()">Back</button></div>
    <p class="muted center">Tap the game to fly.</p>
    <canvas id="birdCanvas" width="340" height="420" style="width:100%;background:#102d4a;border-radius:15px"></canvas>
    <button class="primary" onclick="startBird()">START / RESTART</button>
    <p class="center" id="birdScore">Score: 0</p>
</section>

<!-- SNAKE -->
<section class="screen" id="snake">
    <div class="top"><h2>🐍 Snake.io</h2><button class="back" onclick="backToHub()">Back</button></div>
    <div class="stat"><b>Score: <span id="snakeScore">0</span></b><b>🏆 Best: <span id="snakeBest">0</span></b></div>
    <canvas id="gameCanvas" width="360" height="360"></canvas>
    <button class="primary" onclick="startSnake()">START / RESTART</button>
    <div class="controls">
        <span></span><button class="secondary" onclick="setDir(0,-1)">▲</button><span></span>
        <button class="secondary" onclick="setDir(-1,0)">◀</button>
        <button class="secondary" onclick="setDir(0,1)">▼</button>
        <button class="secondary" onclick="setDir(1,0)">▶</button>
    </div>
    <p class="small center">Swipe or use arrow buttons to move.</p>
</section>

<!-- LOADING OVERLAY -->
<div id="loadingScreen">
    <div class="loader"></div>
    <div class="loadingTitle">mobile.app</div>
    <div class="loadingText" id="loadingText">Initializing mobile.app...</div>
    <div class="progress"><div class="progressBar" id="progressBar"></div></div>
</div>

</div>

<script>
function showScreen(id){
    document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));
    document.getElementById(id).classList.add('active');
}
let loading=false;
function enterWithLoading(name){
    if(loading)return;
    loading=true;
    const overlay=document.getElementById('loadingScreen');
    const bar=document.getElementById('progressBar');
    const text=document.getElementById('loadingText');

    bar.style.animation='none';
    void bar.offsetWidth;
    bar.style.animation='progress 2s linear forwards';
    text.textContent='Initializing mobile.app...';
    overlay.classList.add('show');

    setTimeout(()=>{
        document.getElementById('welcome').textContent='Hello, '+name+'!';
        showScreen('home');
        overlay.classList.remove('show');
        document.getElementById('app').classList.remove('fadeIn');
        void document.getElementById('app').offsetWidth;
        document.getElementById('app').classList.add('fadeIn');
        loading=false;
    },2000);
}
function loginUser(){
    let name=document.getElementById('username').value.trim();
    let pass=document.getElementById('password').value;
    if(!name||!pass){alert('Enter username and password.');return;}
    enterWithLoading(name);
}
function guestLogin(){enterWithLoading('Guest')}
function fingerprintLogin(){enterWithLoading('Guest')}
function goHome(){stopSnake();stopBird();showScreen('home')}
function goLogin(){stopSnake();stopBird();showScreen('login')}
function backToHub(){stopSnake();stopBird();showScreen('gaming')}
function openApp(id){
    showScreen(id);
    if(id==='snake')drawSnake();
    if(id==='flappy')drawBird();
}
function changeTheme(){
    let t=document.getElementById('theme').value;
    let app=document.getElementById('app');
    let themes={
        cosmic:'radial-gradient(ellipse at 15% 15%,#512b85,transparent 42%),radial-gradient(ellipse at 90% 45%,#075b83,transparent 40%),linear-gradient(145deg,#10102b,#080d22 65%,#101a37)',
        blue:'linear-gradient(145deg,#061d43,#075b83,#10102b)',
        purple:'linear-gradient(145deg,#210d40,#632d87,#140d2c)',
        light:'linear-gradient(145deg,#e4eaff,#c5d8ff,#f1e9ff)',
        dark:'linear-gradient(145deg,#080808,#20202b,#101018)'
    };
    app.style.background=themes[t];
    app.style.color=t==='light'?'#18203a':'white';
}
function updateClock(){
    let d=new Date();
    document.getElementById('time').textContent=
        d.toLocaleTimeString([], {hour:'2-digit',minute:'2-digit',second:'2-digit'});
    document.getElementById('date').textContent=
        d.toLocaleDateString([], {weekday:'long',day:'numeric',month:'long',year:'numeric'});
}
updateClock();setInterval(updateClock,1000);

// CALCULATOR
function calcAdd(v){document.getElementById('calcDisplay').value+=v}
function clearCalc(){document.getElementById('calcDisplay').value=''}
function calcBack(){let x=document.getElementById('calcDisplay');x.value=x.value.slice(0,-1)}
function calculate(){
    let x=document.getElementById('calcDisplay');
    try{
        if(!/^[0-9+\-*/(). ]+$/.test(x.value))throw Error();
        let result=Function('"use strict";return ('+x.value+')')();
        if(!Number.isFinite(result))throw Error();
        x.value=result;
    }catch(e){x.value='Error'}
}

// PASSWORD GENERATOR
function generatePassword(){
    let n=Math.max(4,Math.min(40,Number(document.getElementById('passLength').value)||16));
    let chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&*?';
    let p='';
    for(let i=0;i<n;i++)p+=chars[Math.floor(Math.random()*chars.length)];
    document.getElementById('generatedPass').value=p;
}
function copyPassword(){
    let p=document.getElementById('generatedPass').value;
    if(p)navigator.clipboard?.writeText(p).then(()=>alert('Copied!')).catch(()=>alert('Copy not supported'));
}

// NUMBER GUESS
let secret=Math.floor(Math.random()*100)+1,attempts=0;
function checkGuess(){
    let v=Number(document.getElementById('guessInput').value);
    let m=document.getElementById('guessMessage');
    if(!v||v<1||v>100){m.textContent='Enter a number from 1 to 100.';return}
    attempts++;
    if(v===secret)m.textContent='🎉 Correct! You won!';
    else m.textContent=v<secret?'Try a higher number!':'Try a lower number!';
    document.getElementById('guessCount').textContent='Attempts: '+attempts;
}
function resetGuess(){
    secret=Math.floor(Math.random()*100)+1;attempts=0;
    document.getElementById('guessInput').value='';
    document.getElementById('guessMessage').textContent='';
    document.getElementById('guessCount').textContent='Attempts: 0';
}

// FLAPPY BIRD
const bc=document.getElementById('birdCanvas'),bctx=bc.getContext('2d');
let bird={y:180,v:0},pipes=[],birdScore=0,birdRun=false,birdRAF;
function drawBird(){
    bctx.clearRect(0,0,340,420);
    bctx.fillStyle='#102d4a';bctx.fillRect(0,0,340,420);
    bctx.fillStyle='#46d8ff';
    bctx.beginPath();bctx.arc(90,bird.y,13,0,Math.PI*2);bctx.fill();
    bctx.fillStyle='#ffdf64';
    pipes.forEach(p=>{
        bctx.fillRect(p.x,0,48,p.top);
        bctx.fillRect(p.x,p.top+115,48,420);
    });
    bctx.fillStyle='white';bctx.font='20px Arial';
    bctx.fillText('Score: '+birdScore,12,28);
}
function startBird(){
    stopBird();bird.y=180;bird.v=0;pipes=[];birdScore=0;birdRun=true;
    pipes.push({x:350,top:100,scored:false});
    birdLoop();
}
function stopBird(){birdRun=false;cancelAnimationFrame(birdRAF)}
function birdLoop(){
    if(!birdRun)return;
    bird.v+=.35;bird.y+=bird.v;
    if(Math.random()<.012)pipes.push({x:350,top:50+Math.random()*180,scored:false});
    pipes.forEach(p=>{
        p.x-=2.3;
        if(!p.scored&&p.x<90){p.scored=true;birdScore++}
        if(p.x<103&&p.x+48>77&&(bird.y<p.top||bird.y>p.top+115))birdRun=false;
    });
    pipes=pipes.filter(p=>p.x>-55);
    if(bird.y>410||bird.y<0)birdRun=false;
    drawBird();
    document.getElementById('birdScore').textContent='Score: '+birdScore;
    if(birdRun)birdRAF=requestAnimationFrame(birdLoop);
    else {bctx.fillStyle='white';bctx.font='24px Arial';bctx.fillText('Game Over',110,210)}
}
bc.addEventListener('pointerdown',()=>{if(birdRun)bird.v=-5});

// SNAKE.IO
const sc=document.getElementById('gameCanvas'),ctx=sc.getContext('2d');
const CELL=18,GRID=20;
let snake=[],food={},dir={x:1,y:0},nextDir={x:1,y:0};
let snakeScore=0,snakeRunning=false,snakeRAF=0,lastStep=0;
let best=Number(localStorage.getItem('snakeBest')||0);
document.getElementById('snakeBest').textContent=best;
function newFood(){
    food={x:Math.floor(Math.random()*GRID),y:Math.floor(Math.random()*GRID)};
    if(snake.some(s=>s.x===food.x&&s.y===food.y))newFood();
}
function drawSnake(){
    ctx.clearRect(0,0,360,360);
    ctx.fillStyle='#07162a';ctx.fillRect(0,0,360,360);
    ctx.strokeStyle='#ffffff0c';
    for(let i=0;i<=360;i+=CELL){
        ctx.beginPath();ctx.moveTo(i,0);ctx.lineTo(i,360);ctx.stroke();
        ctx.beginPath();ctx.moveTo(0,i);ctx.lineTo(360,i);ctx.stroke();
    }
    ctx.shadowColor='#ff254e';ctx.shadowBlur=15;
    ctx.fillStyle='#ff254e';
    ctx.beginPath();ctx.arc(food.x*CELL+9,food.y*CELL+9,7,0,Math.PI*2);ctx.fill();
    ctx.shadowBlur=0;
    ctx.fillStyle='#66ef9b';
    ctx.fillRect(food.x*CELL+10,food.y*CELL,3,6);
    snake.forEach((s,i)=>{
        let g=ctx.createLinearGradient(s.x*CELL,s.y*CELL,s.x*CELL+CELL,s.y*CELL+CELL);
        g.addColorStop(0,i===0?'#8cf5ff':'#268cff');
        g.addColorStop(1,'#0752c7');
        ctx.fillStyle=g;ctx.shadowColor='#168bff';ctx.shadowBlur=i===0?12:5;
        ctx.beginPath();ctx.roundRect(s.x*CELL+1,s.y*CELL+1,CELL-2,CELL-2,6);ctx.fill();
    });
    ctx.shadowBlur=0;
    if(snake.length){
        ctx.fillStyle='white';
        ctx.beginPath();ctx.arc(snake[0].x*CELL+6,snake[0].y*CELL+6,2,0,Math.PI*2);ctx.fill();
        ctx.beginPath();ctx.arc(snake[0].x*CELL+13,snake[0].y*CELL+6,2,0,Math.PI*2);ctx.fill();
    }
}
function startSnake(){
    cancelAnimationFrame(snakeRAF);
    snake=[{x:8,y:10},{x:7,y:10},{x:6,y:10}];
    dir={x:1,y:0};nextDir={x:1,y:0};
    snakeScore=0;snakeRunning=true;lastStep=0;
    document.getElementById('snakeScore').textContent=0;
    newFood();drawSnake();
    snakeRAF=requestAnimationFrame(snakeLoop);
}
function stopSnake(){snakeRunning=false;cancelAnimationFrame(snakeRAF)}
function setDir(x,y){
    if(x===-dir.x&&y===-dir.y)return;
    nextDir={x,y};
}
function snakeLoop(t){
    if(!snakeRunning)return;
    let speed=Math.max(65,125-snakeScore*2);
    if(t-lastStep>speed){
        lastStep=t;dir=nextDir;
        let head={x:snake[0].x+dir.x,y:snake[0].y+dir.y};
        let eating=head.x===food.x&&head.y===food.y;
        if(head.x<0||head.x>=GRID||head.y<0||head.y>=GRID||
           snake.slice(0,eating?snake.length:snake.length-1).some(s=>s.x===head.x&&s.y===head.y)){
            endSnake();return;
        }
        snake.unshift(head);
        if(eating){
            snakeScore+=5;
            document.getElementById('snakeScore').textContent=snakeScore;
            if(snakeScore>best){
                best=snakeScore;localStorage.setItem('snakeBest',best);
                document.getElementById('snakeBest').textContent=best;
            }
            newFood();
        }else snake.pop();
        drawSnake();
    }
    snakeRAF=requestAnimationFrame(snakeLoop);
}
function endSnake(){
    snakeRunning=false;
    drawSnake();
    ctx.fillStyle='#0009';ctx.fillRect(0,135,360,90);
    ctx.fillStyle='white';ctx.textAlign='center';
    ctx.font='bold 25px Arial';ctx.fillText('GAME OVER',180,177);
    ctx.font='15px Arial';ctx.fillText('Score: '+snakeScore+'  •  Press Restart',180,205);
    ctx.textAlign='left';
}
let touchX=0,touchY=0;
sc.addEventListener('touchstart',e=>{
    touchX=e.touches[0].clientX;touchY=e.touches[0].clientY;
},{passive:true});
sc.addEventListener('touchend',e=>{
    let dx=e.changedTouches[0].clientX-touchX;
    let dy=e.changedTouches[0].clientY-touchY;
    if(Math.abs(dx)>Math.abs(dy))setDir(dx>0?1:-1,0);
    else if(Math.abs(dy)>0)setDir(0,dy>0?1:-1);
},{passive:true});
document.addEventListener('keydown',e=>{
    if(!document.getElementById('snake').classList.contains('active'))return;
    if(e.key==='ArrowUp')setDir(0,-1);
    if(e.key==='ArrowDown')setDir(0,1);
    if(e.key==='ArrowLeft')setDir(-1,0);
    if(e.key==='ArrowRight')setDir(1,0);
});
</script>
</body>
</html>
"""

components.html(APP, height=720, scrolling=False)
