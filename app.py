from typing import List
from fastapi import FastAPI
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import BSHTMLLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.pydantic_v1 import BaseModel, Field
from langserve import add_routes
from dotenv import load_dotenv
from retrieve_web_page_contents import retrieve_web_page_contents
from langchain import hub
import subprocess
import uvicorn

# Load environment variables
load_dotenv()

# Constants
loader_general_file = "promptior-landing-page.html"
loader_about_us_file = "about-us-page.html"

# Retrieve web page contents
retrieve_web_page_contents(
    loader_general_file, loader_about_us_file)

# Create document loaders
loader_general = BSHTMLLoader(loader_general_file)
loader_about_us = BSHTMLLoader(loader_about_us_file)

# Load documents
docs_general = loader_general.load()
docs_about_us = loader_about_us.load()

# Split documents
text_splitter = RecursiveCharacterTextSplitter()
documents_about_us = text_splitter.split_documents(docs_about_us)
documents_general = text_splitter.split_documents(docs_general)

# Create embeddings and vector store
embedding = OpenAIEmbeddings()
vector = FAISS.from_documents(documents_about_us, embedding)
vector.add_documents(documents_general)
retriever = vector.as_retriever()

# Create retriever tool
retriever_tool = create_retriever_tool(
    retriever, "promptior_search", "promptior search!"
)

# Create agent
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
prompt = hub.pull("hwchase17/openai-functions-agent")
tools = [retriever_tool]
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)

# Create FastAPI app
app = FastAPI(
    title="Promptior Helper",
    version="1.0",
    description="A simple API server using LangChain's Runnable interfaces",
)


# Define input and output models
class Input(BaseModel):
    input: str
    chat_history: List[BaseMessage] = Field(
        ..., extra={"widget": {"type": "chat", "input": "location"}}
    )


class Output(BaseModel):
    output: str

def install_requirements():
    try:
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
    except subprocess.CalledProcessError as e:
        print("Error instalando dependencias:", e)

# Add routes to the app
add_routes(
    app, agent_executor.with_types(input_type=Input, output_type=Output), path="/agent"
)

# Run the app if this script is executed
if __name__ == "__main__":
    install_requirements()
    uvicorn.run(app, host="0.0.0.0", port=8000)
