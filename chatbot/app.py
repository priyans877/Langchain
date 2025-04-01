from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv()


os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

# Langmith tracking

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

# Prompt temlate 
prompt = ChatPromptTemplate.from_messages(
    [
        ("system" , "You Are a Helpful Chatbot, Please responce to the user Query"),
        ("user" , "Question:{question}"),
    ]
)

st.title("Langchain usign OPENAI")
input_text = st.text_input("Enter Your Query Here")


llm=ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))
    