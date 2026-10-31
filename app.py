
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
button,input{font:inherit}
button{cursor:pointer;border:0;color:white}
#app{height:100dvh;width:100%;max-width:650px;margin:auto;padding:12px;overflow:hidden;background:radial-gradient(ellipse at 15% 10%,#35216c 0,transparent 40%),radial-gradient(ellipse at 90% 80%,#075b77 0,transparent 38%),linear-gradient(145deg,#090e24,#15102e 60%,#071c2b);position:relative}
.screen{height:100%;width:100%;overflow-y:auto;overflow-x:hidden;border:1px solid #ffffff22;border-radius:25px;padding:18px;background:#ffffff09;backdrop-filter:blur(18px);box-shadow:0 15px 50px #0006}
.hidden{display:none!important}
h1,h2,h3,p{margin-top:0}
h1{font-size:27px}
h2{font-size:22px}
.muted{color:#b8c5dc;font-size:13px}
.clock{text-align:center;padding:18px 5px 22px}
.clock-icon{font-size:28px}
#time{font-size:39px;font-weight:800;letter-spacing:2px;margin:5px}
#date{color:#c5cde0;font-size:13px}
.input{width:100%;padding:14px;border:1px solid #ffffff2c;border-radius:13px;background:#101a35;color:white;margin:7px 0;outline:none}
.btn{padding:13px 15px;border-radius:13px;background:linear-gradient(110deg,#6553e9,#168eae);font-weight:bold;margin:5px 0;width:100%;box-shadow:0 5px 18px #0003}
.btn.secondary{background:#ffffff14;border:1px solid #ffffff22}
.btn.small{width:auto;padding:10px 15px}
.row{display:flex;gap:9px}
.row>*{flex:1;min-width:0}
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
#loading{position:absolute;inset:12px;z-index:20;border-radius:25px;background:#090e24f5;display:flex;flex-direction:column;align-items:center;justify-content:center}
.spinner{width:54px;height:54px;border:4px solid #ffffff25;border-top-color:#25d9ed;border-radius:50%;animation:spin .8s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.bar{height:5px;width:190px;background:#ffffff22;border-radius:8px;margin-top:20px;overflow:hidden}
.bar:after{content:"";display:block;height:100%;width:0;background:#24d9ed;animation:load 2s linear forwards}
@keyframes load{to{width:100%}}
@media(max-height:700px){.screen{padding:12px}.clock{padding:8px 4px 12px}#time{font-size:32px}.home-tile{min-height:68px}.btn{padding:11px}}
</style>
</head>
<body>
<div id="app">

<div id="loading" class="hidden">
  <div class="spinner"></div>
  <h2 style="margin:20px 0 5px">Loading your app</h2>
  <div class="muted">Please wait...</div>
  <div class="bar"></div>
</div>

<section id="login" class="screen">
  <div class="clock">
    <div class="clock-icon">◷</div>
    <div id="time">00:00:00</div>
    <div id="date">Loading date...</div>
  </div>
  <div style="text-align:center;margin-bottom:18px">
    <h1>Welcome Back</h1>
    <div class="muted">Your personal mobile space</div>
  </div>
  <input id="username" class="input" placeholder="Username" autocomplete="username">
  <input id="password" class="input" type="password" placeholder="Password" autocomplete="current-password">
  <button class="btn" onclick="loginUser()">LOGIN</button>
  <button class="btn secondary" onclick="enterApp('Guest')">Continue as Guest</button>
  <button class="btn secondary" onclick="enterApp('Guest')">◉ &nbsp; Fingerprint Demo</button>
  <p class="muted" style="text-align:center;margin-top:12px">Fingerprint is a demo shortcut.</p>
</section>

<section id="home" class="screen hidden">
  <div style="display:flex;justify-content:space-between;align-items:center">
    <div><div class="muted">WELCOME</div><h1 id="welcomeName">Home</h1></div>
    <button class="back" onclick="goLogin()">↪</button>
  </div>
  <div class="card" style="display:flex;justify-content:space-between;align-items:center">
    <div><div class="muted">TODAY</div><b id="homeDate">Loading...</b></div>
    <div style="font-size:29px">◷</div>
    <b id="homeTime">00:00</b>
  </div>
  <div class="home-grid">
    <button class="home-tile" onclick="showPage('calculator')"><span class="bigicon">🧮</span><b>Calculator</b><span class="muted">Quick calculations</span></button>
    <button class="home-tile" onclick="showPage('passwordPage')"><span class="bigicon">🔐</span><b>Password Generator</b><span class="muted">Create passwords</span></button>
    <button class="home-tile hub" onclick="showPage('gaming')"><span class="bigicon">🧩</span><b>Gaming Hub</b><span class="muted">Play your favourite games</span></button>
  </div>
  <div class="card"><b>✨ Your Space</b><p class="muted" style="margin:7px 0 0">Choose an activity and enjoy.</p></div>
</section>

<section id="calculator" class="screen hidden">
  <button class="back" onclick="showPage('home')">← Back</button>
  <h2>🧮 Calculator</h2>
  <input id="calcDisplay" value="0" readonly>
  <div class="calc-grid" id="calcButtons"></div>
</section>

<section id="passwordPage" class="screen hidden">
  <button class="back" onclick="showPage('home')">← Back</button>
  <h2>🔐 Password Generator</h2>
  <div class="card">
    <label class="muted">Password length</label>
    <input id="passLength" class="input" type="number" min="6" max="32" value="16">
    <label><input id="passUpper" type="checkbox" checked> Uppercase letters</label><br><br>
    <label><input id="passLower" type="checkbox" checked> Lowercase letters</label><br><br>
    <label><input id="passNumbers" type="checkbox" checked> Numbers</label><br><br>
    <label><input id="passSymbols" type="checkbox" checked> Symbols</label>
    <button class="btn" onclick="generatePassword()">Generate Password</button>
    <input id="passOutput" class="input" readonly placeholder="Your password appears here">
    <button class="btn secondary" onclick="copyPassword()">Copy Password</button>
    <div id="passMessage" class="muted"></div>
  </div>
</section>

<section id="gaming" class="screen hidden">
  <button class="back" onclick="showPage('home')">← Back</button>
  <h2>🧩 Gaming Hub</h2>
  <p class="muted">Choose your game</p>
  <button class="btn" onclick="startGuess()">🔢 Number Guessing</button>
  <button class="btn" onclick="startFlappy()">🐦 Flappy Bird</button>
  <button class="btn" onclick="startSnake()">🐍 Snake.io</button>
</section>

<section id="guessPage" class="screen hidden">
  <button class="back" onclick="showPage('gaming')">← Back</button>
  <h2>🔢 Number Guessing</h2>
  <div class="card">
    <p>Guess a number between <b>1 and 20</b>.</p>
    <h1 id="attempts">Attempts left: 5</h1>
    <input id="guessInput" class="input" type="number" min="1" max="20" placeholder="Enter your guess">
    <button class="btn" onclick="makeGuess()">Submit Guess</button>
    <div id="guessMessage" style="min-height:25px;margin-top:12px"></div>
    <button id="guessAgain" class="btn secondary hidden" onclick="startGuess()">Play Again</button>
  </div>
</section>

<section id="flappyPage" class="screen hidden">
  <button class="back" onclick="stopFlappy();showPage('gaming')">← Back</button>
  <h2>🐦 Flappy Bird</h2>
  <p class="muted">Tap the game or press SPACE to fly.</p>
  <div class="game-area">
    <canvas id="flappyCanvas" width="360" height="480"></canvas>
  </div>
  <div class="row">
    <div class="card"><small>Score</small><h2 id="flappyScore">0</h2></div>
    <div class="card"><small>Best</small><h2 id="flappyBest">0</h2></div>
  </div>
  <button class="btn" onclick="flappyStart()">Start / Restart</button>
  <button class="btn secondary" onclick="flap()">FLAP ↑</button>
</section>

<section id="snakePage" class="screen hidden">
  <button class="back" onclick="stopSnake();showPage('gaming')">← Back</button>
  <h2>🐍 Snake.io</h2>
  <p class="muted">Eat apples. Avoid the walls and your tail.</p>
  <div class="game-area">
    <canvas id="snakeCanvas" width="360" height="360"></canvas>
  </div>
  <div class="row">
    <div class="card"><small>Score</small><h2 id="snakeScore">0</h2></div>
    <div class="card"><small>Best</small><h2 id="snakeBest">0</h2></div>
  </div>
  <button class="btn" onclick="startSnakeGame()">Start / Restart</button>
  <div class="game-controls">
    <button onclick="changeDir(0,-1)">▲</button>
  </div>
  <div class="game-controls">
    <button onclick="changeDir(-1,0)">◀</button>
    <button onclick="changeDir(0,1)">▼</button>
    <button onclick="changeDir(1,0)">▶</button>
  </div>
</section>

</div>
<script>
const $=id=>document.getElementById(id);
let currentUser="Guest";

function updateClock(){
 const d=new Date();
 $("time").textContent=d.toLocaleTimeString();
 $("date").textContent=d.toLocaleDateString(undefined,{weekday:"long",day:"numeric",month:"long",year:"numeric"});
 $("homeTime").textContent=d.toLocaleTimeString([],{hour:"2-digit",minute:"2-digit"});
 $("homeDate").textContent=d.toLocaleDateString([],{weekday:"short",day:"numeric",month:"short"});
}
updateClock();setInterval(updateClock,1000);

function enterApp(name){
 currentUser=name;
 $("loading").classList.remove("hidden");
 setTimeout(()=>{
  $("loading").classList.add("hidden");
  $("welcomeName").textContent=name;
  showPage("home");
 },2000);
}
function loginUser(){
 let u=$("username").value.trim(),p=$("password").value;
 if(!u||!p){alert("Please enter username and password.");return}
 enterApp(u);
}
function goLogin(){showPage("login")}
function showPage(id){
 document.querySelectorAll(".screen").forEach(s=>s.classList.add("hidden"));
 $(id).classList.remove("hidden");
}

// Calculator
const keys=["C","⌫","%","÷","7","8","9","×","4","5","6","−","1","2","3","+","±","0",".","="];
let calc="0",fresh=false;
function renderCalc(){
 $("calcDisplay").value=calc;
}
function calcPress(k){
 if(k==="C"){calc="0";fresh=false}
 else if(k==="⌫"){calc=calc.length>1?calc.slice(0,-1):"0"}
 else if(k==="±"){calc=String(-Number(calc))}
 else if(k==="="){
  try{
   let expr=calc.replace(/×/g,"*").replace(/÷/g,"/").replace(/−/g,"-").replace(/%/g,"/100");
   if(!/^[0-9+\-*/.() ]+$/.test(expr))throw Error();
   let result=Function('"use strict";return ('+expr+')')();
   calc=Number.isFinite(result)?String(Number(result.toFixed(8))):"Error";
   fresh=true;
  }catch(e){calc="Error";fresh=true}
 }else{
  if(calc==="Error"||fresh){calc="0";fresh=false}
  if("÷×−+".includes(k)){
   if("÷×−+".includes(calc.slice(-1)))calc=calc.slice(0,-1);
   calc+=k;
  }else if(k==="."){
   let part=calc.split(/[+\-×÷]/).pop();
   if(!part.includes("."))calc+=".";
  }else calc=calc==="0"?k:calc+k;
 }
 renderCalc();
}
$("calcButtons").innerHTML=keys.map(k=>`<button class="${k==="="? "eq":k==="C"?"clear":"÷×−+".includes(k)?"op":""}" data-key="${k}">${k}</button>`).join("");
$("calcButtons").addEventListener("click",e=>{
 let b=e.target.closest("button");if(b)calcPress(b.dataset.key);
});

// Password generator
function generatePassword(){
 let n=Math.max(6,Math.min(32,Number($("passLength").value)||16));
 let sets=[];
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

// Number Guess
let secret=0,tries=5,guessDone=false;
function startGuess(){
 secret=Math.floor(Math.random()*20)+1;tries=5;guessDone=false;
 $("attempts").textContent="Attempts left: 5";
 $("guessMessage").textContent="You have five attempts. Good luck!";
 $("guessInput").value="";$("guessInput").disabled=false;
 $("guessAgain").classList.add("hidden");showPage("guessPage");
}
function makeGuess(){
 if(guessDone)return;
 let v=Number($("guessInput").value);
 if(!Number.isInteger(v)||v<1||v>20){$("guessMessage").textContent="Enter a whole number from 1 to 20.";return}
 tries--;
 $("attempts").textContent="Attempts left: "+tries;
 if(v===secret){
  $("guessMessage").textContent="🎉 Correct! You won!";
  guessDone=true;
 }else if(tries===0){
  $("guessMessage").textContent="Game over! The number was "+secret+".";
  guessDone=true;
 }else{
  $("guessMessage").textContent=v<secret?"Too low! Try a higher number.":"Too high! Try a lower number.";
 }
 if(guessDone){$("guessInput").disabled=true;$("guessAgain").classList.remove("hidden")}
 $("guessInput").value="";
}

// Flappy Bird
const fc=$("flappyCanvas"),fx=fc.getContext("2d");
let bird,pipes,flScore,flRunning=false,flOver=true,flFrame=0,flLoop=null;
let flBest=Number(localStorage.getItem("flappyBest")||0);
$("flappyBest").textContent=flBest;
function startFlappy(){showPage("flappyPage");flappyStart()}
function flappyStart(){
 stopFlappy();bird={x:75,y:220,vy:0};pipes=[];flScore=0;flFrame=0;flRunning=true;flOver=false;
 $("flappyScore").textContent="0";
 pipes.push({x:390,gapY:190,passed:false});
 flLoop=setInterval(flappyTick,1000/60);
 drawFlappy();
}
function stopFlappy(){if(flLoop)clearInterval(flLoop);flLoop=null;flRunning=false}
function flap(){
 if(!flRunning){if(flOver)flappyStart();return}
 bird.vy=-5.2;
}
function flappyTick(){
 if(!flRunning)return;
 flFrame++;
 bird.vy+=0.28;bird.y+=bird.vy;
 if(flFrame%105===0)pipes.push({x:370,gapY:95+Math.random()*220,passed:false});
 pipes.forEach(p=>p.x-=2.5);
 pipes=pipes.filter(p=>p.x>-65);
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
 fx.fillStyle="#ffffff99";[[55,70],[220,105],[300,55]].forEach(([x,y])=>{fx.beginPath();fx.arc(x,y,19,0,Math.PI*2);fx.arc(x+18,y+4,15,0,Math.PI*2);fx.fill()});
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

// Snake
const sc=$("snakeCanvas"),sx=sc.getContext("2d"),CELL=18,GRID=20;
let snake,apple,dir,nextDir,snScore=0,snTimer=null,snRunning=false,snOver=true;
let snBest=Number(localStorage.getItem("snakeBest")||0);
$("snakeBest").textContent=snBest;
function startSnake(){showPage("snakePage");startSnakeGame()}
function stopSnake(){if(snTimer)clearInterval(snTimer);snTimer=null;snRunning=false}
function randomApple(){
 let a;do{a={x:Math.floor(Math.random()*GRID),y:Math.floor(Math.random()*GRID)}}while(snake.some(s=>s.x===a.x&&s.y===a.y));
 return a;
}
function startSnakeGame(){
 stopSnake();snake=[{x:9,y:10},{x:8,y:10},{x:7,y:10}];
 dir={x:1,y:0};nextDir={x:1,y:0};snScore=0;apple=randomApple();snRunning=true;snOver=false;
 $("snakeScore").textContent="0";drawSnake();
 snTimer=setInterval(snakeTick,115);
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
 if(head.x===apple.x&&head.y===apple.y){
  snScore++;$("snakeScore").textContent=snScore;apple=randomApple();
 }else snake.pop();
 drawSnake();
}
function drawSnake(){
 sx.fillStyle="#082c35";sx.fillRect(0,0,360,360);
 sx.strokeStyle="#ffffff0b";
 for(let i=0;i<=GRID;i++){sx.beginPath();sx.moveTo(i*CELL,0);sx.lineTo(i*CELL,360);sx.stroke();sx.beginPath();sx.moveTo(0,i*CELL);sx.lineTo(360,i*CELL);sx.stroke()}
 sx.fillStyle="#ff4e59";sx.beginPath();sx.arc(apple.x*CELL+9,apple.y*CELL+9,7,0,Math.PI*2);sx.fill();
 snake.forEach((s,i)=>{sx.fillStyle=i===0?"#6cecff":"#168ed5";sx.beginPath();sx.roundRect(s.x*CELL+1,s.y*CELL+1,16,16,5);sx.fill()});
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

components.html(APP, height=880, scrolling=False)
