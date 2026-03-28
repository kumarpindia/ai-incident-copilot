from langchain_community.vectorstores.chroma import Chroma
from langchain_community.embeddings.openai import OpenAIEmbeddings

embedding_model = OpenAIEmbeddings()

vector_store = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embedding_model
)

def get_relevant_context(query):
    # Placeholder for actual retrieval logic
    # Replace with code to fetch relevant context based on the query
    #query_embedding = embedding_model.embed_query(query)
    #results = vector_store.similarity_search_by_vector(query_embedding, k=4)
    #return results
    docs = vector_store.similarity_search_with_score(query, k=3)
    return [
        # {
        #     "source": doc.metadata["source"],
        #     "content": doc.page_content,
        #     "score": score
        # }
        f"{doc.metadata.get('source','')}\n\n{doc.page_content}"
        for doc, score in docs
    ]
