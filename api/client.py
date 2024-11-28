import requests
import streamlit as st


def get_openai_response(input_text):
    response = requests.post("http://localhost:8000/joke5/invoke",
                            json={'input': {"topic": input_text}})
    return response.json()["output"]["content"]


def get_llama_response(input_text):
    response = request.post("http://localhost:8000/joke2/invoke",
                            json={'input': {"topic": input_text}})
    return response.json()["output"]["content"]


st.title("Langchain Demo with LLM")
input_text = st.text_input("Write joke about")
input_text1 = st.text_input("Write joke about ")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write(get_ollama_response(input_text1))
