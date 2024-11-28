from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()


os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

app = FastAPI(title="Langchain Server",
              version="1.0",
              description="A simple API server")

add_routes(app, ChatOpenAI(), path="/openai")

model = ChatOpenAI()

# other model
llm = Ollama(model="llama2")

prompt1 = ChatPromptTemplate.from_template("Write me a joke about {topic} with 50 words")
prompt2 = ChatPromptTemplate.from_template("Write me a joke about {topic} with 20 words")

add_routes(app, prompt1|model, path="/joke5")
add_routes(app, prompt2|model, path="/joke2")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
    