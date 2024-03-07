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



import streamlit as st                                                      
from langchain_core.messages import HumanMessage, AIMessage                 
from langchain_core.prompts import ChatPromptTemplate                       
from langchain_core.output_parsers import StrOutputParser                   
from langchain_openai import ChatOpenAI                                     
from dotenv import load_dotenv                                              

load_dotenv()                                                               

# Initialize chat history variable
if "chat_history" not in st.session_state:                                  
    st.session_state.chat_history = []                                      

# App config                                                                
st.set_page_config(page_title="Streaming bot", page_icon="🤖")              
st.title("Streaming bot")  

# Get response  
def get_response(query, chat_history):                                      
    template = """                                                  
    You are a helpful assistant.
    Answer the following questions considering
    the history of the conversation:

    Chat history: {chat_history}
    User question: {user_question}
    """
    prompt = ChatPromptTemplate.from_template(template)                     

    llm = ChatOpenAI()                                                      
        
    chain = prompt | llm | StrOutputParser()                                
    
    return chain.invoke({                                                   
        "chat_history": chat_history,                                       
        "user_question": user_query,                                        
    })                                                                      


# Conversation
for message in st.session_state.chat_history:                               
    if isinstance(message, HumanMessage):                                   
        with st.chat_message("Human"):                                      
            st.markdown(message.content)                                    
    else:                                                                   
        with st.chat_message("AI"):                                         
            st.markdown(message.content)                                    

# User input
user_query = st.chat_input("Your message")                                  
if user_query is not None and user_query != "":                             
    st.session_state.chat_history.append(HumanMessage(user_query))           
    
    with st.chat_message("Human"):                                          
        st.markdown(user_query)                                             
        
    with st.chat_message("AI"):                                             
        ai_response = get_response(user_query, st.session_state.chat_history)       
        st.markdown(ai_response)                                            
    
    st.session_state.chat_history.append(AIMessage(ai_response))            
