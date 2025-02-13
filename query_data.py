import argparse
from langchain.vectorstores.chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from get_embedding_function import get_embedding_function
from get_llm_function import get_llm_function

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
You are an assistant who answers questions about the West Point regulations. You are provided with the following context from the documents. You will answer the question based on the regulations. If you are not sure what the answer to the question is based on the evidence, or it is unclear, say that you are not sure and refer the cadet to their chain of command or TAC team. 

{context}

---

QUESTION: {question}
"""


def main():
    # Create CLI.
    parser = argparse.ArgumentParser()
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text
    query_rag(query_text)


def gen_rag_prompt(query_text: str):
    # Prepare the DB.
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    # Search the DB.
    results = db.similarity_search_with_score(query_text, k=5)
    sources = [doc.metadata.get("id", None) for doc, _score in results]

    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    print(prompt)

    return prompt, sources

#model = Ollama(model="deepseek-r1")
#model = get_llm_function()
#response_text = model.invoke(prompt)

#sources = [doc.metadata.get("id", None) for doc, _score in results]
#formatted_response = f"Response: {response_text}\nSources: {sources}"
#print(formatted_response)
#return response_text


if __name__ == "__main__":
    main()
