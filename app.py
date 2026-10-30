
import streamlit as st
import random

st.set_page_config(
    page_title="mobile.app",
    page_icon="📱",
    layout="centered"
)

# Design
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #eaf5ff, #f4edff);
}
h1, h2, h3 {
    color: #3157a5;
}
.stButton > button {
    width: 100%;
    min-height: 65px;
    border-radius: 15px;
    font-size: 18px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# Session setup
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "home"

# Welcome screen
if not st.session_state.logged_in:

    st.write("")
    st.write("")
    st.title("📱 mobile.app")
    st.caption("Your little world of useful tools")

    st.write("")
    st.write("Welcome! Continue to explore.")

    if st.button("👤 Continue as Guest"):
        st.session_state.logged_in = True
        st.session_state.page = "home"
        st.rerun()

# Main dashboard
else:

    st.title("📱 mobile.app")
    st.caption("Choose your tool")

    if st.session_state.page == "home":

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🧮 Calculator"):
                st.session_state.page = "calculator"
                st.rerun()

        with col2:
            if st.button("🎮 Number Guessing"):
                st.session_state.page = "game"
                st.rerun()

        st.write("")
        if st.button("🚪 Exit Guest"):
            st.session_state.logged_in = False
            st.session_state.page = "home"
            st.rerun()

    # Calculator
    elif st.session_state.page == "calculator":

        st.header("🧮 Calculator")

        number1 = st.number_input(
            "First number",
            value=0.0,
            key="num1"
        )

        operation = st.selectbox(
            "Choose operation",
            ["Addition (+)", "Subtraction (-)",
             "Multiplication (×)", "Division (÷)"]
        )

        number2 = st.number_input(
            "Second number",
            value=0.0,
            key="num2"
        )

        if st.button("Calculate"):
            if operation == "Addition (+)":
                result = number1 + number2
                st.success(f"Result: {result}")

            elif operation == "Subtraction (-)":
                result = number1 - number2
                st.success(f"Result: {result}")

            elif operation == "Multiplication (×)":
                result = number1 * number2
                st.success(f"Result: {result}")

            elif operation == "Division (÷)":
                if number2 == 0:
                    st.error("Cannot divide by zero!")
                else:
                    result = number1 / number2
                    st.success(f"Result: {result}")

        if st.button("⬅ Back to Home"):
            st.session_state.page = "home"
            st.rerun()

    # Number Guessing Game
    elif st.session_state.page == "game":

        st.header("🎮 Number Guessing Game")
        st.write("I have selected a number between 1 and 100.")

        if "secret_number" not in st.session_state:
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.game_over = False

        guess = st.number_input(
            "Enter your guess",
            min_value=1,
            max_value=100,
            value=50,
            step=1
        )

        if st.button("Submit Guess"):

            if not st.session_state.game_over:
                st.session_state.attempts += 1

                if guess < st.session_state.secret_number:
                    st.info("Too low! Try a higher number.")

                elif guess > st.session_state.secret_number:
                    st.info("Too high! Try a lower number.")

                else:
                    st.success(
                        f"🎉 Correct! You won in "
                        f"{st.session_state.attempts} attempts!"
                    )
                    st.session_state.game_over = True

        if st.button("🔄 New Game"):
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0
            st.session_state.game_over = False
            st.rerun()

        st.write(f"Attempts: {st.session_state.attempts}")

        if st.button("⬅ Back to Home"):
            st.session_state.page = "home"
            st.rerun()
            
