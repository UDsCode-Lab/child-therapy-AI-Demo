import openai
import streamlit as st

# Load your OpenAI API key securely from secrets.toml
openai.api_key = st.secrets["OPENAI_API_KEY"]

try:
    response = openai.Model.list()
    print("✅ API key works! You have access to:")
    for model in response['data'][:5]:  # print just a few models
        print("-", model['id'])
except Exception as e:
    print("❌ There is a problem with the API key:")
    print(e)
