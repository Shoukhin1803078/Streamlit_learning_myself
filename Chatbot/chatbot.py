# Home/home.py
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import (
   ChatPromptTemplate,
   MessagesPlaceholder,
   SystemMessagePromptTemplate,
   HumanMessagePromptTemplate,
)

prompt = ChatPromptTemplate.from_messages([
   SystemMessagePromptTemplate.from_template(
       "You are a helpful AI assistant focused on providing accurate and clear responses."
   ),
   MessagesPlaceholder(variable_name="history"),
   HumanMessagePromptTemplate.from_template("{input}")
])

if 'memory' not in st.session_state:
   st.session_state.memory = ConversationBufferMemory(return_messages=True)

with st.sidebar:
   openai_key = st.text_input("OpenAI API Key", type="password")
   groq_key = st.text_input("Groq API Key", type="password")
   model = st.selectbox("Model", ["GPT-4", "Groq-Mixtral"])
   if st.button("Clear History"): 
       st.session_state.memory.clear()

st.title("Chat Interface")

history = st.session_state.memory.load_memory_variables({})
for message in history.get('history', []):
   role = "user" if message.type == "human" else "assistant"
   st.chat_message(role).write(message.content)

if user_input := st.chat_input("Message"):
   if not (openai_key if model == "GPT-4" else groq_key):
       st.error("Enter API key")
       st.stop()

   try:
       llm = (ChatOpenAI(api_key=openai_key, model="gpt-4") if model == "GPT-4" 
              else ChatGroq(api_key=groq_key, model="mixtral-8x7b-32768"))
       
       chain = ConversationChain(
           llm=llm,
           memory=st.session_state.memory,
           prompt=prompt,
           verbose=True
       )
       
       st.chat_message("user").write(user_input)
       with st.spinner("Thinking..."):
           response = chain.run(user_input)
       st.chat_message("assistant").write(response)

   except Exception as e:
       st.error(f"Error: {str(e)}")




