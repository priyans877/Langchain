from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Initialize FastAPI app
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A simple API Server"
)

# Models
llama = ChatOpenAI( 
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model="meta-llama/llama-3.2-3b-instruct:free"
)

deepseek = ChatOpenAI(
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model="deepseek/deepseek-v3-base:free"  # Using a known free model
)

# Prompts
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5-year-old child with 100 words")


llma_chain = prompt1 | llama
deep_chain = prompt3 | deepseek
# Chains
@app.get("/llama")
async def llama_endpoint():
    return llama.invoke("thristy crow")


@app.get("/deepseek")
async def deep_endpoint():
    return deep_chain.invoke("thirsty Crow")



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000, log_level="debug")