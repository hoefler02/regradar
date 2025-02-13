from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain_ollama.llms import OllamaLLM
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')

def get_llm_function():
    llm = ChatOpenAI(api_key=API_KEY, model="gpt-4o")
    # llm = OllamaLLM(model="deepseek-r1")
    return llm
