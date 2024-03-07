# pip install langchain streamlit langchain-openai python-dotenv grep
# pip freeze | findstr langchain streamlit langchain-openai python-dotenv >> requirements.txt
# pip freeze | findstr streamlit >> requirements.txt
# pip freeze | findstr langchain-openai >> requirements.txt
# pip freeze | findstr python-dotenv >> requirements.txt
# pip freeze | findstr grep >> requirements.txt

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# app config
st.set_page_config(page_title="Streaming bot", page_icon="🤖")
st.title("Streaming bot")
