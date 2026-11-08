# from langchain_ollama import ChatOllama

# llm = ChatOllama(
#     model="llama3.2",
#     temperature=0
# )
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="openai/gpt-oss-20b"
    #model_name="allam-2-7b"
)