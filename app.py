
import streamlit as st
import streamlit.components.v1 as components
import random

st.set_page_config(page_title="mobile.app", page_icon="📱", layout="centered")

# ================= DESIGN =================

st.markdown("""
<style>
.stApp {
    background: #020805;
    color: #eaffef;
}
.block-container {
    max-width: 460px !important;
    min-height: 95vh;
    margin: 8px auto !important;
    padding: 25px 12px !important;
    border: 7px solid #17251c;
    border-radius: 38px;
    background: linear-gradient(160deg,#07160d,#020805);
    box-shadow: 0 0 22px #00ff6650;
}
h1,h2,h3 {
    color: #55ff91 !important;
    text-align: center;
}
p,label {
    color: #d5ffe3 !important;
}
.stButton > button {
    width: 100%;
    min-height: 48px;
    border-radius: 14px;
    border: 1px solid #20d968;
    background: #102b1c;
    color: #55ff91;
    font-weight: bold;
}
.stButton > button:hover {
    background: #18502d;
    color: white;
}
div[data-testid="column"] .stButton > button {
    min-height: 105px;
    padding: 5px;
    font-size: 13px;
    white-space: normal;
    border-radius: 17px;
}
.calc-display {
    background: #001508;
    border: 2px solid #20d968;
    border-radius: 15px;
    padding: 22px 12px;
    min-height: 90px;
    display: flex;
    align-items: center;
    justify-content: end;
    color: #55ff91;
    font-size: 32px;
    font-weight: bold;
    overflow-wrap: anywhere;
}
</style>
""", unsafe_allow_html=True)


# ================= SESSION =================

defaults = {
    "logged": False,
    "page": "login",
    "display": "0",
    "first": None,
    "operator": None,
    "waiting": False,
    "secret": random.randint(1, 100),
    "attempts": 0,
    "game_over": False,
    "won": False,
    "feedback": ""
}

for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ================= CALCULATOR =================

def fmt(n):
    if float(n).is_integer():
        return str(int(n))
    return f"{n:.10g}"


def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "−":
        return a - b
    if op == "×":
        return a * b
    if op == "÷":
        return None if b == 0 else a / b


def press(k):
    d = st.session_state.display

    if k == "AC":
        st.session_state.display = "0"
        st.session_state.first = None
        st.session_state.operator = None
        st.session_state.waiting = False
        return

    if k == "DEL":
        if not st.session_state.waiting:
            if d not in ("Error", "Cannot divide by zero"):
                st.session_state.display = d[:-1] or "0"
        return

    if k in "0123456789":
        if (
            d in ("Error", "Cannot divide by zero")
            or st.session_state.waiting
            or d == "0"
        ):
            st.session_state.display = k
            st.session_state.waiting = False
        else:
            st.session_state.display += k
        return

    if k == ".":
        if st.session_state.waiting:
            st.session_state.display = "0."
            st.session_state.waiting = False
        elif "." not in d and d not in ("Error", "Cannot divide by zero"):
            st.session_state.display += "."
        return

    if k in ("%", "+/−"):
        if d not in ("Error", "Cannot divide by zero"):
            n = float(d)
            st.session_state.display = fmt(
                n / 100 if k == "%" else -n
            )
        return

    if k in ("+", "−", "×", "÷"):
        if d in ("Error", "Cannot divide by zero"):
            return

        current = float(d)

        if st.session_state.operator and not st.session_state.waiting:
            result = calculate(
                st.session_state.first,
                current,
                st.session_state.operator
            )

            if result is None:
                st.session_state.display = "Cannot divide by zero"
                st.session_state.first = None
                st.session_state.operator = None
                st.session_state.waiting = True
                return

            current = result
            st.session_state.display = fmt(result)

        st.session_state.first = current
        st.session_state.operator = k
        st.session_state.waiting = True
        return

    if k == "=":
        if st.session_state.operator is not None:
            if d in ("Error", "Cannot divide by zero"):
                return

            result = calculate(
                st.session_state.first,
                float(d),
                st.session_state.operator
            )

            st.session_state.display = (
                "Cannot divide by zero"
                if result is None else fmt(result)
            )
            st.session_state.first = None
            st.session_state.operator = None
            st.session_state.waiting = True


# ================= LOGIN =================

if not st.session_state.logged:

    st.write("")
    st.write("")
    st.write("")
    st.markdown("<h1>📱 mobile.app</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align:center'>Your little world of useful tools</p>",
        unsafe_allow_html=True
    )
    st.write("")
    st.write("")
    st.write("")

    left, middle, right = st.columns([1, 2, 1])

    with middle:
        if st.button("LOGIN", key="login_button"):
            st.session_state.logged = True
            st.session_state.page = "home"
            st.rerun()


# ================= APP =================

else:

    st.markdown("<h1>📱 mobile.app</h1>", unsafe_allow_html=True)

    if st.session_state.page == "home":

        st.markdown(
            "<p style='text-align:center'>Choose your tool</p>",
            unsafe_allow_html=True
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            if st.button("🧮\nCalculator", key="home_calc"):
                st.session_state.page = "calculator"
                st.rerun()

        with c2:
            if st.button("🎮\nNumber Guessing", key="home_guess"):
                st.session_state.page = "guess"
                st.rerun()

        with c3:
            if st.button("🐦\nFlappy Bird", key="home_flappy"):
                st.session_state.page = "flappy"
                st.rerun()

        st.write("")
        if st.button("LOG OUT"):
            st.session_state.logged = False
            st.session_state.page = "login"
            st.rerun()


    # ================= CALCULATOR SCREEN =================

    elif st.session_state.page == "calculator":

        st.markdown("<h2>CALCULATOR</h2>", unsafe_allow_html=True)

        st.markdown(
            f"<div class='calc-display'>{st.session_state.display}</div>",
            unsafe_allow_html=True
        )

        rows = [
            ["AC", "+/−", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["DEL", "0", ".", "="]
        ]

        for ri, row in enumerate(rows):
            cols = st.columns(4)
            for ci, key in enumerate(row):
                with cols[ci]:
                    if st.button(key, key=f"calc_{ri}_{ci}"):
                        press(key)
                        st.rerun()

        st.write("")
        if st.button("⬅ BACK TO HOME"):
            st.session_state.page = "home"
            st.rerun()


    # ================= NUMBER GUESSING GAME =================

    elif st.session_state.page == "guess":

        st.markdown("<h2>NUMBER GUESSING GAME</h2>", unsafe_allow_html=True)

        st.markdown(
            "<div class='calc-display' style='font-size:20px;justify-content:center'>"
            "Guess a number between 1 and 100"
            "</div>",
            unsafe_allow_html=True
        )

        remaining = 10 - st.session_state.attempts
        st.markdown(
            f"<h3>Chances remaining: {remaining}/10</h3>",
            unsafe_allow_html=True
        )

        if not st.session_state.game_over:

            guess = st.number_input(
                "Your guess",
                min_value=1,
                max_value=100,
                value=50,
                step=1,
                key="guess_input"
            )

            if st.button("SUBMIT GUESS"):
                st.session_state.attempts += 1

                if guess == st.session_state.secret:
                    st.session_state.won = True
                    st.session_state.game_over = True
                    st.session_state.feedback = ""

                elif st.session_state.attempts >= 10:
                    st.session_state.game_over = True

                elif guess < st.session_state.secret:
                    st.session_state.feedback = "Too low! Try higher."

                else:
                    st.session_state.feedback = "Too high! Try lower."

                st.rerun()

            if st.session_state.feedback:
                st.info(st.session_state.feedback)

        else:

            if st.session_state.won:
                st.success("Yay! You won !!!!")
            else:
                st.error("Oops! You're out of tries")
                st.write(
                    f"The correct number was {st.session_state.secret}"
                )

            if st.button("🔄 NEW GAME"):
                st.session_state.secret = random.randint(1, 100)
                st.session_state.attempts = 0
                st.session_state.game_over = False
                st.session_state.won = False
                st.session_state.feedback = ""
                st.rerun()

        st.write("")
        if st.button("⬅ BACK TO HOME"):
            st.session_state.page = "home"
            st.rerun()


    # ================= FLAPPY BIRD =================

    elif st.session_state.page == "flappy":

        st.markdown("<h2>🐦 FLAPPY BIRD</h2>", unsafe_allow_html=True)

        flappy_html = """
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {box-sizing:border-box}
body {
 margin:0;
 background:#020805;
 color:#55ff91;
 text-align:center;
 font-family:Arial,sans-serif;
}
canvas {
 display:block;
 width:100%;
 max-width:400px;
 height:auto;
 margin:auto;
 border:2px solid #20d968;
 border-radius:12px;
 background:#102b1c;
 touch-action:manipulation;
}
button {
 display:block;
 width:100%;
 max-width:400px;
 height:60px;
 margin:12px auto;
 border:2px solid #20d968;
 border-radius:15px;
 background:#102b1c;
 color:#55ff91;
 font-size:22px;
 font-weight:bold;
 touch-action:manipulation;
}
.hint {color:#c7f9d6;font-size:13px;margin:8px}
</style>
</head>
<body>

<canvas id="game" width="360" height="480"></canvas>
<button id="jump">⬆ JUMP</button>
<div class="hint">Tap JUMP to fly. Avoid the pipes!</div>

<script>
const canvas = document.getElementById("game");
const ctx = canvas.getContext("2d");
const jumpButton = document.getElementById("jump");

let bird, pipes, score, frame, running, started;
const gravity = 0.38;
const jumpPower = -6.5;

function resetGame() {
 bird = {x:75,y:220,velocity:0,radius:12};
 pipes = [];
 score = 0;
 frame = 0;
 running = false;
 started = false;
 draw();
}

function jump() {
 if (!started) {
  started = true;
  running = true;
  bird.velocity = jumpPower;
 } else if (running) {
  bird.velocity = jumpPower;
 } else {
  resetGame();
  started = true;
  running = true;
  bird.velocity = jumpPower;
 }
}

jumpButton.addEventListener("click",jump);

canvas.addEventListener("click",function() {
 jump();
});

document.addEventListener("keydown",function(e) {
 if (e.code === "Space" || e.code === "ArrowUp") {
  e.preventDefault();
  jump();
 }
});

function addPipe() {
 const gap = 140;
 const top = 55 + Math.random() * 190;
 pipes.push({
  x:360,
  top:top,
  bottom:top+gap,
  scored:false
 });
}

function draw() {
 ctx.fillStyle="#102b1c";
 ctx.fillRect(0,0,360,480);

 ctx.fillStyle="#16452b";
 for(let i=0;i<7;i++) {
  ctx.fillRect(i*60,0,1,480);
 }

 for(const p of pipes) {
  ctx.fillStyle="#25d366";
  ctx.fillRect(p.x,0,48,p.top);
  ctx.fillRect(p.x,p.bottom,48,480-p.bottom);

  ctx.fillStyle="#55ff91";
  ctx.fillRect(p.x-4,p.top-12,56,12);
  ctx.fillRect(p.x-4,p.bottom,56,12);
 }

 ctx.fillStyle="#ffe45c";
 ctx.beginPath();
 ctx.arc(bird.x,bird.y,bird.radius,0,Math.PI*2);
 ctx.fill();

 ctx.fillStyle="#ffffff";
 ctx.beginPath();
 ctx.arc(bird.x+4,bird.y-4,3,0,Math.PI*2);
 ctx.fill();

 ctx.fillStyle="#ff8c42";
 ctx.beginPath();
 ctx.moveTo(bird.x+10,bird.y);
 ctx.lineTo(bird.x+19,bird.y+4);
 ctx.lineTo(bird.x+10,bird.y+7);
 ctx.fill();

 ctx.fillStyle="#ffffff";
 ctx.font="bold 26px Arial";
 ctx.textAlign="center";
 ctx.fillText("Score: "+score,180,35);

 if(!started) {
  ctx.font="bold 20px Arial";
  ctx.fillText("TAP JUMP TO START",180,250);
 }

 if(started && !running) {
  ctx.font="bold 26px Arial";
  ctx.fillText("GAME OVER",180,220);
  ctx.font="18px Arial";
  ctx.fillText("Tap JUMP to restart",180,255);
 }
}

function update() {
 if(running) {
  frame++;
  bird.velocity += gravity;
  bird.y += bird.velocity;

  if(frame % 95 === 0) {
   addPipe();
  }

  for(const p of pipes) {
   p.x -= 2.3;

   if(!p.scored && p.x+48 < bird.x) {
    p.scored=true;
    score++;
   }

   const horizontal =
    bird.x+bird.radius > p.x &&
    bird.x-bird.radius < p.x+48;

   const vertical =
    bird.y-bird.radius < p.top ||
    bird.y+bird.radius > p.bottom;

   if(horizontal && vertical) {
    running=false;
    break;
   }
  }

  pipes = pipes.filter(p => p.x > -60);

  if(bird.y+bird.radius >= 480 ||
     bird.y-bird.radius <= 0) {
   running=false;
  }
 }

 draw();
 requestAnimationFrame(update);
}

resetGame();
update();
</script>
</body>
</html>
        """

        components.html(flappy_html, height=620, scrolling=False)

        st.write("")
        if st.button("⬅ BACK TO HOME"):
            st.session_state.page = "home"
            st.rerun()
        
