import streamlit as st
from chatbot import Chatbot

st.set_page_config(page_title="TalhaBot", page_icon="🤖", layout="centered")
st.title("🤖 TalhaBot — AI Chatbot")
st.caption("Built with DialoGPT + Intent Matching by Muhammad Talha Farooq")

@st.cache_resource
def load_bot():
    return Chatbot()

bot = load_bot()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm TalhaBot. How can I help you today?"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Type your message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = bot.respond(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)
