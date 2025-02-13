from langchain_openai import OpenAIEmbeddings

api_key = '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'

def get_embedding_function():
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
        api_key=api_key
        # With the `text-embedding-3` class
        # of models, you can specify the size
        # of the embeddings you want returned.
        # dimensions=1024
    )
    # embeddings = OllamaEmbeddings(model="nomic-embed-text")
    return embeddings
