import requests
import streamlit as st

def get_llam_responce(input_text):
    url = "http://127.0.0.1:8000/llama"
    payload = {"text": input_text}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raise error for bad HTTP status
        return response.json().get('content', 'No content returned')
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

def get_deep_responce(input_text):
    url = "http://127.0.0.1:8000/deep"
    payload = {"text": input_text}
    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json().get('content', 'No content returned')
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

st.title("LangChain using OpenRouter")
input_text = st.text_input("Enter Topic for generating Essay")
input_text2 = st.text_input("Enter Topic for generating Poem")

if input_text:
    st.write(get_llam_responce(input_text))

st.markdown("---------------------------------------")

if input_text2:
    st.write(get_deep_responce(input_text2))
