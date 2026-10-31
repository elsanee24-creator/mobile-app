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
body{margin:0;background:#07110d;color:white;font-family:Arial,sans-serif}
.app{max-width:500px;margin:auto;padding:18px;min-height:100vh;
background:linear-gradient(145deg,#07110d,#10251b)}
header{display:flex;justify-content:space-between;align-items:center;margin-bottom:22px}
.logo{font-size:23px;font-weight:bold;color:#43ff9b}
.panel{background:#13271d;border:1px solid #28543c;border-radius:18px;
padding:20px;margin:14px 0;box-shadow:0 0 15px #00ff7715}
h2{text-align:center;color:#50ffa4}
button{border:0;border-radius:12px;padding:14px;margin:6px 0;
width:100%;background:#20d879;color:#06150d;font-weight:bold;font-size:16px}
button:active{transform:scale(.98)}
input,select{width:100%;padding:13px;border-radius:10px;border:1px solid #43845d;
background:#071a10;color:white;margin:8px 0;font-size:16px}
.secondary{background:#244b35;color:white}
.hidden{display:none!important}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.clock{text-align:center;color:#7dffb5;font-size:24px;font-weight:bold}
.date{text-align:center;color:#a6cdb5;margin-top:5px}
.output{background:#07150e;padding:15px;border-radius:10px;overflow-wrap:anywhere}
canvas{width:100%;background:#07150e;border:1px solid #36704b;border-radius:12px}
.score{text-align:center;font-size:20px;color:#65ffad;margin:10px}
.small{text-align:center;color:#a8cbb5;font-size:13px}
.theme-light{background:#eaf5ee!important;color:#10251b!important}
.theme-light .panel{background:#fff;color:#10251b}
.theme-light input,.theme-light select{background:#f3fff7;color:#10251b}
.theme-blue{background:#071526!important}
.theme-purple{background:#180d27!important}
.theme-dark{background:#111!important}
</style>
</head>
<body>
<div class="app" id="app">

<header>
<div class="logo">📱 mobile.app</div>
<select id="theme" style="width:125px">
<option value="">Green Neon</option>
<option value="theme-blue">Blue</option>
<option value="theme-purple">Purple</option>
<option value="theme-light">Light</option>
<option value="theme-dark">Dark</option>
</select>
</header>

<div id="loginScreen">
<div class="panel">
<h2>Welcome 👋</h2>
<div class="clock" id="clock">00:00:00</div>
<div class="date" id="date"></div>
<input id="username" placeholder="Enter your username">
<input id="password" type="password" placeholder="Password">
<button onclick="login()">Login</button>
<button class="secondary" onclick="guestLogin()">Continue as Guest</button>
<p class="small">Welcome to mobile.app</p>
</div>
</div>

<div id="homeScreen" class="hidden">
<div class="panel">
<h2 id="welcome">Home</h2>
<div class="clock" id="homeClock"></div>
<div class="date" id="homeDate"></div>
</div>

<div class="grid">
<button onclick="openApp('calculator')">🧮 Calculator</button>
<button onclick="openApp('password')">🔐 Password Generator</button>
</div>
<div class="panel">
<h2>🧩 Gaming Hub</h2>
<p class="small">Your mini gaming zone</p>
<button onclick="openApp('hub')">Open Gaming Hub 🎮</button>
</div>
<button class="secondary" onclick="logout()">Logout</button>
</div>

<div id="hubScreen" class="tool-screen hidden">
<div class="panel">
<h2>🧩 Gaming Hub</h2>
<button onclick="openApp('flappy')">🐦 Flappy Bird</button>
<button onclick="openApp('guess')">🔢 Number Guess</button>
<button onclick="openApp('snake')">🐍 Snake.io</button>
<button class="secondary" onclick="goHome()">⬅ Back Home</button>
</div>
</div>

<div id="calculatorScreen" class="tool-screen hidden">
<div class="panel">
<h2>🧮 Calculator</h2>
<input id="calcDisplay" placeholder="0" readonly>
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
<button class="secondary" onclick="clearCalc()">Clear</button>
<button class="secondary" onclick="goHome()">⬅ Back Home</button>
</div>
</div>

<div id="passwordScreen" class="tool-screen hidden">
<div class="panel">
<h2>🔐 Password Generator</h2>
<label>Password Length</label>
<input type="number" id="passLength" min="4" max="64" value="16">
<button onclick="generatePassword()">Generate Password</button>
<div class="output" id="passOutput">Your password will appear here</div>
<button class="secondary" onclick="copyPassword()">Copy Password</button>
<button class="secondary" onclick="goHome()">⬅ Back Home</button>
</div>
</div>

<div id="guessScreen" class="tool-screen hidden">
<div class="panel">
<h2>🔢 Number Guess</h2>
<p class="small">Guess a number between 1 and 100</p>
<input id="guessInput" type="number" placeholder="Your guess">
<button onclick="checkGuess()">Check Guess</button>
<div class="output" id="guessMessage">Start guessing!</div>
<button class="secondary" onclick="resetGuess()">New Game</button>
<button class="secondary" onclick="backToHub()">⬅ Back to Gaming Hub</button>
</div>
</div>

<div id="flappyScreen" class="tool-screen hidden">
<div class="panel">
<h2>🐦 Flappy Bird</h2>
<div class="score">Score: <span id="birdScore">0</span></div>
<canvas id="birdCanvas" width="320" height="420"></canvas>
<button onclick="startBird()">Start Game</button>
<button class="secondary" onclick="birdJump()">TAP TO FLY</button>
<button class="secondary" onclick="backToHub()">⬅ Back to Gaming Hub</button>
</div>
</div>

<div id="snakeScreen" class="tool-screen hidden">
<div class="panel">
<h2>🐍 Snake.io</h2>
<div class="score">🏆 Score: <span id="snakeScore">0</span></div>
<div class="score">Best: <span id="bestScore">0</span></div>
<canvas id="snakeCanvas" width="320" height="320"></canvas>
<button onclick="startSnake()">Start Game</button>
<div class="grid">
<button onclick="changeDirection(0,-1)">⬆️</button>
<button onclick="changeDirection(-1,0)">⬅️</button>
<button onclick="changeDirection(1,0)">➡️</button>
<button onclick="changeDirection(0,1)">⬇️</button>
</div>
<p class="small">Swipe on the game screen or use buttons.</p>
<button class="secondary" onclick="backToHub()">⬅ Back to Gaming Hub</button>
</div>
</div>

</div>

<script>
let currentUser="Guest";
let secretNumber=Math.floor(Math.random()*100)+1;
let guessAttempts=0;
let calcExpression="";
let birdTimer=null;
let snakeTimer=null;

function updateClock(){
 let d=new Date();
 let t=d.toLocaleTimeString();
 let dt=d.toDateString();
 document.getElementById("clock").textContent=t;
 document.getElementById("date").textContent=dt;
 document.getElementById("homeClock").textContent=t;
 document.getElementById("homeDate").textContent=dt;
}
setInterval(updateClock,1000);
updateClock();

document.getElementById("theme").addEventListener("change",function(){
 document.getElementById("app").className="app "+this.value;
});

function login(){
 let u=document.getElementById("username").value.trim();
 if(!u){alert("Enter username");return}
 currentUser=u;
 showHome();
}
function guestLogin(){currentUser="Guest";showHome()}
function showHome(){
 hideAll();
 document.getElementById("homeScreen").classList.remove("hidden");
 document.getElementById("welcome").textContent="Welcome, "+currentUser+"!";
}
function logout(){
 hideAll();
 document.getElementById("loginScreen").classList.remove("hidden");
}
function hideAll(){
 document.querySelectorAll("#loginScreen,#homeScreen,.tool-screen")
 .forEach(x=>x.classList.add("hidden"));
 stopSnake();
 if(birdTimer){clearInterval(birdTimer);birdTimer=null}
}
function openApp(name){
 hideAll();
 document.getElementById(name+"Screen").classList.remove("hidden");
}
function goHome(){showHome()}
function backToHub(){openApp("hub")}

function calcPress(v){
 calcExpression+=v;
 document.getElementById("calcDisplay").value=calcExpression;
}
function clearCalc(){
 calcExpression="";
 document.getElementById("calcDisplay").value="";
}
function calculate(){
 try{
  if(!/^[0-9+\-*/.() ]+$/.test(calcExpression))throw Error();
  let result=Function('"use strict";return ('+calcExpression+')')();
  if(!Number.isFinite(result))throw Error();
  calcExpression=String(result);
  document.getElementById("calcDisplay").value=calcExpression;
 }catch(e){
  document.getElementById("calcDisplay").value="Error";
  calcExpression="";
 }
}

function resetGuess(){
 secretNumber=Math.floor(Math.random()*100)+1;
 guessAttempts=0;
 document.getElementById("guessInput").value="";
 document.getElementById("guessMessage").textContent="New game started!";
}
function checkGuess(){
 let n=Number(document.getElementById("guessInput").value);
 if(!n||n<1||n>100){
  document.getElementById("guessMessage").textContent="Enter a number from 1 to 100";
  return;
 }
 guessAttempts++;
 let m="";
 if(n===secretNumber)m="🎉 Correct! Attempts: "+guessAttempts;
 else if(n<secretNumber)m="Too low! Try a higher number.";
 else m="Too high! Try a lower number.";
 document.getElementById("guessMessage").textContent=m;
}

function generatePassword(){
 let length=Math.max(4,Math.min(64,Number(document.getElementById("passLength").value)||16));
 let chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
 let result="";
 let values=new Uint32Array(length);
 crypto.getRandomValues(values);
 for(let i=0;i<length;i++)result+=chars[values[i]%chars.length];
 document.getElementById("passOutput").textContent=result;
}
function copyPassword(){
 let p=document.getElementById("passOutput").textContent;
 if(p && p!=="Your password will appear here"){
  navigator.clipboard.writeText(p).then(()=>alert("Copied!"));
 }
}

/* FLAPPY BIRD */
let birdY=180,birdV=0,birdScore=0,birdStarted=false;
let pipes=[];
const bc=document.getElementById("birdCanvas");
const bx=bc.getContext("2d");

function drawBird(){
 bx.clearRect(0,0,320,420);
 bx.fillStyle="#102c1b";bx.fillRect(0,0,320,420);
 bx.fillStyle="#ffe34d";
 bx.beginPath();bx.arc(75,birdY,12,0,Math.PI*2);bx.fill();
 bx.fillStyle="#ff5533";
 bx.fillRect(85,birdY-4,10,6);
 pipes.forEach(p=>{
  bx.fillStyle="#31df77";
  bx.fillRect(p.x,0,45,p.top);
  bx.fillRect(p.x,p.top+115,45,420);
 });
 bx.fillStyle="white";bx.font="16px Arial";
 bx.fillText("Score: "+birdScore,10,25);
}
function startBird(){
 if(birdTimer)clearInterval(birdTimer);
 birdY=180;birdV=0;birdScore=0;birdStarted=true;
 pipes=[{x:320,top:130}];
 document.getElementById("birdScore").textContent=0;
 birdTimer=setInterval(()=>{
  if(!birdStarted)return;
  birdV+=0.35;birdY+=birdV;
  pipes.forEach(p=>p.x-=2.5);
  if(pipes[pipes.length-1].x<170)
   pipes.push({x:320,top:70+Math.random()*180});
  if(pipes[0].x< -50)pipes.shift();
  for(let p of pipes){
   if(75+12>p.x&&75-12<p.x+45&&
     (birdY-12<p.top||birdY+12>p.top+115)){
     endBird();return;
   }
  }
  if(birdY>408||birdY<0){endBird();return}
  pipes.forEach(p=>{
   if(!p.passed&&p.x<75){p.passed=true;birdScore++}
  });
  document.getElementById("birdScore").textContent=birdScore;
  drawBird();
 },25);
}
function birdJump(){
 if(!birdStarted){startBird();return}
 birdV=-6;
}
function endBird(){
 birdStarted=false;
 clearInterval(birdTimer);birdTimer=null;
 drawBird();
 bx.fillStyle="white";bx.font="22px Arial";
 bx.fillText("Game Over!",100,210);
}
bc.addEventListener("click",birdJump);
drawBird();

/* SNAKE.IO */
const sc=document.getElementById("snakeCanvas");
const sx=sc.getContext("2d");
const cell=16;
const cells=20;
let snake=[],food={x:10,y:10};
let dir={x:1,y:0},nextDir={x:1,y:0};
let snakePoints=0;
let snakeRunning=false;
let best=0;

function drawSnake(){
 sx.fillStyle="#07150e";
 sx.fillRect(0,0,320,320);
 sx.fillStyle="#e83c4b";
 sx.beginPath();
 sx.arc(food.x*cell+8,food.y*cell+8,7,0,Math.PI*2);
 sx.fill();
 snake.forEach((p,i)=>{
  sx.fillStyle=i===0?"#37a5ff":"#176ed0";
  sx.fillRect(p.x*cell+1,p.y*cell+1,14,14);
 });
}
function startSnake(){
 stopSnake();
 snake=[{x:10,y:10},{x:9,y:10},{x:8,y:10}];
 dir={x:1,y:0};nextDir={x:1,y:0};
 snakePoints=0;
 document.getElementById("snakeScore").textContent=0;
 snakeRunning=true;
 placeFood();
 drawSnake();
 snakeTimer=setInterval(snakeStep,140);
}
function stopSnake(){
 snakeRunning=false;
 if(snakeTimer){clearInterval(snakeTimer);snakeTimer=null}
}
function placeFood(){
 food={
  x:Math.floor(Math.random()*cells),
  y:Math.floor(Math.random()*cells)
 };
 if(snake.some(p=>p.x===food.x&&p.y===food.y))placeFood();
}
function changeDirection(x,y){
 if(!snakeRunning)return;
 if(x===-dir.x&&y===-dir.y)return;
 nextDir={x,y};
}
function snakeStep(){
 if(!snakeRunning)return;
 dir=nextDir;
 let head={x:snake[0].x+dir.x,y:snake[0].y+dir.y};
 if(head.x<0||head.x>=cells||head.y<0||head.y>=cells){
  endSnake();return;
 }
 let eating=head.x===food.x&&head.y===food.y;
 let body=eating?snake:snake.slice(0,-1);
 if(body.some(p=>p.x===head.x&&p.y===head.y)){
  endSnake();return;
 }
 snake.unshift(head);
 if(eating){
  snakePoints++;
  document.getElementById("snakeScore").textContent=snakePoints;
  placeFood();
 }else snake.pop();
 drawSnake();
}
function endSnake(){
 stopSnake();
 if(snakePoints>best)best=snakePoints;
 document.getElementById("bestScore").textContent=best;
 drawSnake();
 sx.fillStyle="white";
 sx.font="22px Arial";
 sx.fillText("GAME OVER",95,165);
}
let touchStartX=0,touchStartY=0;
sc.addEventListener("touchstart",e=>{
 touchStartX=e.touches[0].clientX;
 touchStartY=e.touches[0].clientY;
},{passive:true});
sc.addEventListener("touchend",e=>{
 let dx=e.changedTouches[0].clientX-touchStartX;
 let dy=e.changedTouches[0].clientY-touchStartY;
 if(Math.abs(dx)>Math.abs(dy)){
  if(dx>15)changeDirection(1,0);
  if(dx< -15)changeDirection(-1,0);
 }else{
  if(dy>15)changeDirection(0,1);
  if(dy< -15)changeDirection(0,-1);
 }
},{passive:true});
document.addEventListener("keydown",e=>{
 if(e.key==="ArrowUp")changeDirection(0,-1);
 if(e.key==="ArrowDown")changeDirection(0,1);
 if(e.key==="ArrowLeft")changeDirection(-1,0);
 if(e.key==="ArrowRight")changeDirection(1,0);
});
drawSnake();
</script>
</body>
</html>
"""

components.html(APP, height=1050, scrolling=True)
