from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set API keys for OpenRouter
os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")

# Enable LangSmith tracking (optional)
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Define the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful chatbot. Please respond to the user's query."),
        ("user", "Question: {question}"),
    ]
)

# Streamlit UI
st.title("LangChain using OpenRouter")
input_text = st.text_input("Enter Your Query Here")

# Initialize OpenRouter LLM instead of OpenAI
llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),  # Use OpenRouter API key
    openai_api_base="https://openrouter.ai/api/v1",  # OpenRouter API endpoint
    model="meta-llama/llama-3.2-3b-instruct:free"  # ✅ Use correct model name
)

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Process user input
if input_text:
    st.write(chain.invoke({'question': input_text}))
