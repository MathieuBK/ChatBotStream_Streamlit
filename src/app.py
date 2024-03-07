#1 python3 -m venv venv
#1 cd venv
#1 Scripts\activate.bat
#1 cd..
#1 pip install -r requirements.txt
#1 streamlit run src/app.py

#1 pip install langchain streamlit langchain-openai python-dotenv grep
#1 pip freeze | findstr langchain streamlit langchain-openai python-dotenv >> requirements.txt
#1 pip freeze | findstr streamlit >> requirements.txt
#1 pip freeze | findstr langchain-openai >> requirements.txt
#1 pip freeze | findstr python-dotenv >> requirements.txt
#1 pip freeze | findstr grep >> requirements.txt
#2 pip install langchain_core
#2 pip freeze | findstr langchain_core >> requirements.txt



import streamlit as st                                              #1
from langchain_core.messages import HumanMessage, AIMessage         #2
from dotenv import load_dotenv                                      #1

load_dotenv()                                                       #1

# Initialize chat history variable
if "chat_history" not in st.session_state:                          #2
    st.session_state.chat_history = []                              #2

# App config                                                        #1
st.set_page_config(page_title="Streaming bot", page_icon="🤖")      #1
st.title("Streaming bot")                                           #1


# Conversation
for message in st.session_state.chat_history:                       #2
    if isinstance(message, HumanMessage):                           #2
        with st.chat_message("Human"):                              #2
            st.markdown(message.content)                            #2
    else:                                                           #2
        with st.chat_message("AI"):                                 #2
            st.markdown(message.content)                            #2

user_query = st.chat_input("Your message")                          #2
if user_query is not None and user_query != "":                     #2
    st.session_state.chat_history.append(HumanMessage(user_query))  #2 
    
    with st.chat_message("Human"):                                  #2
        st.markdown(user_query)                                     #2
        
    with st.chat_message("AI"):                                     #2
        ai_response = "I don't know"                                #2
        st.markdown(ai_response)                                    #2
    
    st.session_state.chat_history.append(AIMessage(ai_response))    #2
