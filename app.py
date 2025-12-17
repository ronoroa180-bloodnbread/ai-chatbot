import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Chatbot")

st.title("🤖 AI Chatbot")
st.write("Ask factual questions like capitals, definitions, etc.")

# Load QA model once
if "qa" not in st.session_state:
    with st.spinner("Loading AI model..."):
        st.session_state.qa = pipeline(
            "question-answering",
            model="distilbert-base-cased-distilled-squad"
        )

question = st.text_input("Your question:")

context = """
India is a country in South Asia. Its capital city is New Delhi.
The Prime Minister of India resides in New Delhi.
"""

if question:
    answer = st.session_state.qa(
        question=question,
        context=context
    )
    st.success(f"Answer: {answer['answer']}")
