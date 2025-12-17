import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Chatbot")

st.title("🤖 AI Chatbot")
st.write("Ask me anything!")

# Keep model in session so it loads only once
if "chatbot" not in st.session_state:
    st.session_state.chatbot = None

if st.session_state.chatbot is None:
    if st.button("Load AI Model"):
        with st.spinner("Loading AI model (first time takes ~1 minute)..."):
            st.session_state.chatbot = pipeline(
                "text-generation",
                model="distilgpt2"
            )
else:
    user_input = st.text_input("You:")

    if user_input:
        with st.spinner("Thinking..."):
            response = st.session_state.chatbot(
                user_input,
                max_length=80,
                num_return_sequences=1
            )
            st.write("Bot:", response[0]["generated_text"])
