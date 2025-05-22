import streamlit as st

st.set_page_config(page_title="Child Therapy AI Demo")

st.title("Child Therapy AI Assistant")

user_input = st.text_input("Enter a child’s concern or behavior...")

if user_input:
    # Simulated AI output
    st.write("🤖 AI Suggestion:")
    st.success(f"For the input: '{user_input}', a therapist might explore emotional triggers and suggest coping strategies.")
