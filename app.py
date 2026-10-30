
import streamlit as st
import random

st.set_page_config(
    page_title="mobile.app",
    page_icon="📱",
    layout="centered"
)

# =============== DESIGN ===============

st.markdown("""
<style>
.stApp {
    background: #020805;
    color: #eaffef;
}

.block-container {
    max-width: 460px !important;
    min-height: 95vh;
    margin: 12px auto !important;
    padding: 35px 20px !important;
    border: 8px solid #17251c;
    border-radius: 42px;
    background: linear-gradient(160deg, #07160d, #020805);
    box-shadow: 0 0 22px #00ff6650,
                inset 0 0 15px #00ff6615;
}

h1, h2, h3 {
    color: #39ff88 !important;
    text-align: center;
}

p, label {
    color: #d5ffe3 !important;
}

.stButton > button {
    width: 100%;
    min-height: 55px;
    border-radius: 15px;
    border: 1px solid #20d968;
    background: #102b1c;
    color: #50ff91;
    font-size: 17px;
    font-weight: bold;
}

.stButton > button:hover {
    background: #17452b;
    border-color: #55ff99;
    color: white;
}

div[data-testid="column"] .stButton > button {
    min-height: 115px;
    border-radius: 22px;
    font-size: 17px;
}

.calc-display {
    background: #001b0c;
    border: 2px solid #19d968;
    border-radius: 15px;
    padding: 20px 12px;
    margin: 12px 0 18px;
    color: #55ff91;
    text-align: right;
    font-size: 32px;
    font-weight: bold;
    overflow-wrap: anywhere;
}

.game-display {
    background: #001b0c;
    border: 2px solid #19d968;
    border-radius: 15px;
    padding: 18px;
    text-align: center;
    color: #55ff91;
    font-size: 20px;
    font-weight: bold;
}

.stNumberInput input {
    background: #0b1c12;
    color: #55ff91;
    border: 1px solid #20d968;
    border-radius: 10px;
}

@media (max-width: 500px) {
    .block-container {
        width: calc(100% - 16px) !important;
        min-height: 95vh;
        margin: 8px auto !important;
        padding: 25px 15px !important;
        border-radius: 35px;
    }
}
</style>
""", unsafe_allow_html=True)


# =============== SESSION SETUP ===============

defaults = {
    "logged_in": False,
    "page": "login",
    "calc_display": "0",
    "calc_first": None,
    "calc_operator": None,
    "calc_waiting": False,
    "secret_number": random.randint(1, 100),
    "attempts": 0,
    "game_over": False,
    "won": False
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# =============== CALCULATOR LOGIC ===============

def format_number(number):
    if number == int(number):
        return str(int(number))
    return f"{number:.10g}"


def calculate(first, second, operator):
    if operator == "+":
        return first + second
    if operator == "−":
        return first - second
    if operator == "×":
        return first * second
    if operator == "÷":
        if second == 0:
            return None
        return first / second


def calculator_press(key):
    display = st.session_state.calc_display

    if key == "AC":
        st.session_state.calc_display = "0"
        st.session_state.calc_first = None
        st.session_state.calc_operator = None
        st.session_state.calc_waiting = False
        return

    if key == "DEL":
        if not st.session_state.calc_waiting:
            display = display[:-1]
            st.session_state.calc_display = display or "0"
        return

    if key in "0123456789":
        if display in ("Error", "Cannot divide by zero"):
            st.session_state.calc_display = key
            st.session_state.calc_waiting = False
        elif st.session_state.calc_waiting or display == "0":
            st.session_state.calc_display = key
            st.session_state.calc_waiting = False
        else:
            st.session_state.calc_display += key
        return

    if key == ".":
        if st.session_state.calc_waiting:
            st.session_state.calc_display = "0."
            st.session_state.calc_waiting = False
        elif "." not in display and display not in ("Error", "Cannot divide by zero"):
            st.session_state.calc_display += "."
        return

    if key == "%":
        if display not in ("Error", "Cannot divide by zero"):
            st.session_state.calc_display = format_number(float(display) / 100)
        return

    if key == "+/−":
        if display not in ("Error", "Cannot divide by zero"):
            st.session_state.calc_display = format_number(float(display) * -1)
        return

    if key in ["+", "−", "×", "÷"]:
        if display in ("Error", "Cannot divide by zero"):
            return

        current = float(display)

        if (st.session_state.calc_operator is not None
                and not st.session_state.calc_waiting):

            result = calculate(
                st.session_state.calc_first,
                current,
                st.session_state.calc_operator
            )

            if result is None:
                st.session_state.calc_display = "Error"
                st.session_state.calc_first = None
                st.session_state.calc_operator = None
                st.session_state.calc_waiting = True
                return

            current = result
            st.session_state.calc_display = format_number(result)

        st.session_state.calc_first = current
        st.session_state.calc_operator = key
        st.session_state.calc_waiting = True
        return

    if key == "=":
        if st.session_state.calc_operator is not None:
            if display in ("Error", "Cannot divide by zero"):
                return

            result = calculate(
                st.session_state.calc_first,
                float(display),
                st.session_state.calc_operator
            )

            if result is None:
                st.session_state.calc_display = "Cannot divide by zero"
            else:
                st.session_state.calc_display = format_number(result)

            st.session_state.calc_first = None
            st.session_state.calc_operator = None
            st.session_state.calc_waiting = True


# =============== LOGIN SCREEN ===============

if not st.session_state.logged_in:

    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.markdown("<h1>📱 mobile.app</h1>", unsafe_allow_html=True)

    st.markdown(
        "<p style='text-align:center;color:#55ff91;'>"
        "Your little world of useful tools"
        "</p>",
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")
    st.write("")

    left, center, right = st.columns([1, 2, 1])

    with center:
        if st.button("LOGIN", key="login_button"):
            st.session_state.logged_in = True
            st.session_state.page = "home"
            st.rerun()


# =============== DASHBOARD ===============

else:

    st.markdown("<h1>📱 mobile.app</h1>", unsafe_allow_html=True)

    st.markdown(
        "<p style='text-align:center;color:#55ff91;'>"
        "Choose your tool"
        "</p>",
        unsafe_allow_html=True
    )

    st.write("")

    if st.session_state.page == "home":

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🧮\n\nCALCULATOR", key="calculator_button"):
                st.session_state.page = "calculator"
                st.rerun()

        with col2:
            if st.button("🎮\n\nNUMBER GUESSING", key="game_button"):
                st.session_state.page = "game"
                st.rerun()

        st.write("")
        if st.button("LOG OUT"):
            st.session_state.logged_in = False
            st.session_state.page = "login"
            st.rerun()


    # =============== CALCULATOR SCREEN ===============

    elif st.session_state.page == "calculator":

        st.markdown("<h2>🧮 Calculator</h2>", unsafe_allow_html=True)

        st.markdown(
            f"<div class='calc-display'>"
            f"{st.session_state.calc_display}"
            f"</div>",
            unsafe_allow_html=True
        )

        rows = [
            ["AC", "+/−", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["DEL", "0", ".", "="]
        ]

        for row_index, row in enumerate(rows):
            cols = st.columns(4)

            for col_index, key in enumerate(row):
                with cols[col_index]:
                    if st.button(
                        key,
                        key=f"calc_{row_index}_{col_index}"
                    ):
                        calculator_press(key)
                        st.rerun()

        st.write("")
        if st.button("⬅ BACK TO HOME"):
            st.session_state.page = "home"
            st.rerun()


    # =============== NUMBER GUESSING GAME ===============

    elif st.session_state.page == "game":

        st.markdown(
            "<h2>🎮 Number Guessing</h2>",
            unsafe_allow_html=True
        )

        st.markdown(
            "<div class='game-display'>"
            "Guess a number between 1 and 100"
            "</div>",
            unsafe_allow_html=True
        )

        st.write("")

        remaining = 10 - st.session_state.attempts

        st.markdown(
            f"<h3>Chances remaining: {remaining}/10</h3>",
            unsafe_allow_html=True
        )

        if not st.session_state.game_over:

            guess = st.number_input(
                "Enter your guess",
                min_value=1,
                max_value=100,
                value=50,
                step=1,
                key="game_guess"
            )

            if st.button("SUBMIT GUESS"):

                st.session_state.attempts += 1

                if guess == st.session_state.secret_number:
                    st.session_state.won = True
                    st.session_state.game_over = True

                elif st.session_state.attempts >= 10:
                    st.session_state.game_over = True

                st.rerun()

            if st.session_state.attempts > 0:
                if not st.session_state.game_over:
                    if guess < st.session_state.secret_number:
                        st.info("Too low! Try a higher number.")
                    elif guess > st.session_state.secret_number:
                        st.info("Too high! Try a lower number.")

        else:

            if st.session_state.won:
                st.success("Yay! You won !!!!")
            else:
                st.error("Oops! You're out of tries")
                st.write(
                    f"The correct number was "
                    f"{st.session_state.secret_number}"
                )

            st.write(f"Total attempts: {st.session_state.attempts}/10")

            if st.button("🔄 PLAY AGAIN"):
                st.session_state.secret_number = random.randint(1, 100)
                st.session_state.attempts = 0
                st.session_state.game_over = False
                st.session_state.won = False
                st.rerun()

        st.write("")
        if st.button("⬅ BACK TO HOME"):
            st.session_state.page = "home"
            st.rerun()
            
