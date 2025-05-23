import streamlit as st
import openai

# Load API key securely from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Child Therapy AI Assistant")

examples = [
    "My 5-year-old is aggressive and hits other kids.",
    "My child is too shy and avoids talking to anyone.",
    "My child throws tantrums when I say no.",
    "My daughter gets anxious before school.",
    "My son lies about his homework."
]

example_choice = st.selectbox("Try a sample concern:", [""] + examples)
user_input = st.text_input("Or enter a child’s concern or behavior...", value=example_choice)

if user_input:
    st.markdown("### Suggested Guidance:")
    st.markdown(f"Your input: **{user_input}**")
    st.markdown("_(This is where the AI-generated advice will appear.)_")
