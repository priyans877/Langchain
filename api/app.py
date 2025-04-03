from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
from pydantic import BaseModel

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


class InputData(BaseModel):
    text: str


# Models
llama = ChatOpenAI( 
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model="meta-llama/llama-3.2-3b-instruct:free"
)

deepseek = ChatOpenAI(
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1",
    model="deepseek/deepseek-chat-v3-0324:free"  # Using a known free model
)

# Prompts
prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("do this{topic}")


llma_chain = prompt1 | llama
deep_chain = prompt2 | deepseek
# Chains


# add_routes(
#     app,
#     prompt1 | llama,
#     path = '/essay',    
# )
# add_routes(
#     app,
#     prompt2 | deepseek,
#     path = '/deep',    
# )

@app.post("/llama")
async def llama_endpoint(data:InputData):
    responce = llma_chain.invoke(data.text)
    print(responce)
    return responce

@app.post("/deep")
async def deep_endpoint(data : InputData):
    print(data.text)
    responce = deep_chain.invoke(data.text)
    print(responce)
    return responce



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")