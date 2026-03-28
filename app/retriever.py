from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings()

vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_model
)

def get_relevant_context(query):
    
    docs = vector_store.similarity_search_with_score(query, k=3)
    return [
        f"{doc.metadata.get('source','')}\n\n{doc.page_content}"
        for doc, score in docs
    ]
