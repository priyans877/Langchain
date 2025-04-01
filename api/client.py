from langchain_openai import ChatOpenAI
from fastapi import FastAPI
import uvicorn
import os
from pydantic import BaseModel

app = FastAPI()
os.environ["OPENROUTER_API_KEY"] = os.getenv("OPENROUTER_API_KEY")
# Configure OpenRouter with LangChain
llm = ChatOpenAI(
    openai_api_base="https://openrouter.ai/api/v1",
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    model_name="mistralai/mixtral-8x7b-instruct"  # Example model
)

class UserInput(BaseModel):
    text: str
    model: str = "mistralai/mixtral-8x7b-instruct"  # Default model


def get_llm(model_name:str):
    return ChatOpenAI(
        openai_api_base="https://openrouter.ai/api/v1",
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        model_name="mistralai/mixtral-8x7b-instruct"
    )
    
    
@app.get("/test")
async def test_endpoint():
    response = llm.invoke("Hello, how are you?")
    return {"response": response.content}

@app.post('/llm_chat')
async def prompting(user_input:UserInput):
    llm = get_llm(user_input.model)
    response = llm.invoke(user_input.text)
    return {'user_input':user_input.text , "responce" : response.content }

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)