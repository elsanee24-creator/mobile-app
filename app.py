import os

import streamlit as st
from google import genai
from google.genai import types


# -------------------- Page setup --------------------
st.set_page_config(
    page_title="AI Master",
    page_icon="🤖",
    layout="centered",
)

SYSTEM_INSTRUCTION = """
You are "AI Master", an advanced, helpful, and clear AI assistant.

For every user prompt, structure your response into these three stages:

Stage 1: Explanation
- Explain the concepts, background, or context behind the user's question or problem.

Stage 2: Solution
- Give a clear, actionable, step-by-step solution, code, or direct answer.

Stage 3: AI Master Summary
- Give a concise takeaway, key recommendation, or high-level summary.

Adapt the length of each stage to the question. For simple questions, keep all
three stages brief. For complex questions, explain them in more detail.
Use clear headings and readable formatting. Introduce yourself as AI Master
when appropriate, but do not repeat an introduction in every response.
"""


def get_api_key():
    """Read the Gemini key from Streamlit secrets or an environment variable."""
    try:
        secret_key = st.secrets.get("GEMINI_API_KEY", "")
    except Exception:
        secret_key = ""

    return secret_key or os.getenv("GEMINI_API_KEY", "")


def generate_answer(prompt: str, client: genai.Client, model: str) -> str:
    """Send one prompt to Gemini and return its text response."""
    response = client.models.generate_content(
        model=model,
        contents=prompt,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION,
            temperature=0.7,
        ),
    )

    answer = getattr(response, "text", None)
    if answer and answer.strip():
        return answer.strip()

    return "Gemini returned an empty response. Please try again."


# -------------------- App interface --------------------
st.title("🤖 AI Master")
st.caption("Your helpful AI assistant")

with st.sidebar:
    st.subheader("Settings")
    model_name = st.text_input(
        "Gemini model",
        value=os.getenv("GEMINI_MODEL", "gemini-3.8-flash"),
        help="Change this if the model is unavailable for your API key.",
    )
    if st.button("Clear chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()
    st.caption("Your API key stays in Streamlit Secrets or environment variables.")

if "messages" not in st.session_state:
    st.session_state.messages = []

api_key = get_api_key()

if not api_key:
    st.info(
        "Gemini API key is not set yet. Add GEMINI_API_KEY in "
        "Streamlit Cloud → App → Settings → Secrets, then reboot the app."
    )
    st.code('GEMINI_API_KEY = "your-gemini-api-key"', language="toml")
    st.stop()

if not model_name.strip():
    st.error("Enter a Gemini model name in the sidebar.")
    st.stop()

try:
    client = genai.Client(api_key=api_key)
except Exception as error:
    st.error(f"Could not initialize Gemini: {error}")
    st.stop()

# Show the previous conversation.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input replaces the original terminal input() loop.
user_prompt = st.chat_input("Ask AI Master anything...")

if user_prompt:
    st.session_state.messages.append(
        {"role": "user", "content": user_prompt}
    )
    with st.chat_message("user"):
        st.markdown(user_prompt)

    with st.chat_message("assistant"):
        with st.spinner("AI Master is thinking..."):
            try:
                answer = generate_answer(user_prompt, client, model_name.strip())
                st.markdown(answer)
                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )
            except Exception as error:
                error_message = (
                    f"Sorry, Gemini could not complete the request.\n\n"
                    f"**Error:** `{error}`\n\n"
                    "Check that your API key is valid, the model name is "
                    "available to your key, and your API quota has not been reached."
                )
                st.error(error_message)
                st.session_state.messages.append(
                    {"role": "assistant", "content": error_message}
                )
