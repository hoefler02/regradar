from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('API_KEY')

def get_embedding_function():
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
        api_key=API_KEY
        # With the `text-embedding-3` class
        # of models, you can specify the size
        # of the embeddings you want returned.
        # dimensions=1024
    )
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
