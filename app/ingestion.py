from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
#from langchain.embeddings import OpenAIEmbeddings
#from langchain.vectorstores import FAISS
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.openai import OpenAIEmbeddings
import os
from pathlib import Path

class IncidentIngestionPipeline:
    def __init__(self, docs_path: str, embeddings_model=None, file_extensions=None):
        """Initialize the ingestion pipeline."""
        self.docs_path = docs_path
        self.embeddings = embeddings_model or OpenAIEmbeddings()
        self.file_extensions = file_extensions or ["txt"]
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            separators=["\n\n", "\n", " ", ""]
        )
        self.vector_store = None

    def load_files(self):
        """Step 1: Load files from directory."""
        documents = []
        seen_paths = set()
        for ext in self.file_extensions:
            pattern = f"**/*.{ext.lstrip('.')}"
            for file_path in Path(self.docs_path).glob(pattern):
                # Avoid loading the same file twice if extensions overlap
                if file_path in seen_paths:
                    continue
                seen_paths.add(file_path)

                try:
                    loader = TextLoader(str(file_path), encoding="utf-8")
                    docs = loader.load()
                    documents.extend(docs)
                except Exception as e:
                    print(f"Error loading {file_path}: {e}")
        return documents

    def clean_text(self, documents):
        """Step 2: Clean text content."""
        for doc in documents:
            doc.page_content = (
                doc.page_content
                .strip()
                .replace("\x00", "")
                .replace("\r\n", "\n")
            )
        return documents

    def chunk_documents(self, documents):
        """Step 3: Split documents into chunks."""
        return self.text_splitter.split_documents(documents)

    def generate_embeddings_and_store(self, chunks):
        """Step 4 & 5: Generate embeddings and store in FAISS."""
        #self.vector_store = FAISS.from_documents(chunks, self.embeddings)
        #return self.vector_store
        embedding_model = OpenAIEmbeddings()
        self.vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embedding_model,
            persist_directory="./chroma_db"
        )
        self.vector_store.persist()
        return self.vector_store

    def run_pipeline(self):
        """Execute the complete pipeline."""
        print("Loading files...")
        documents = self.load_files()
        
        print("Cleaning text...")
        documents = self.clean_text(documents)
        
        print("Chunking documents...")
        chunks = self.chunk_documents(documents)
        
        print("Generating embeddings and storing...")
        self.generate_embeddings_and_store(chunks)
        
        #print(f"Pipeline complete. Stored {len(chunks)} chunks.")
        print(f"Pipeline complete. Loaded {len(documents)} docs. Stored {len(chunks)} chunks.")
        return self.vector_store

    # def save_vector_store(self, path: str):
    #     """Save vector store to disk."""
    #     if self.vector_store:
    #         self.vector_store.save_local(path)

    def load_vector_store(self, path: str):
        """Load vector store from disk."""
        #self.vector_store = FAISS.load_local(path, self.embeddings)
        self.vector_store = Chroma.load_local(path, self.embeddings)
        return self.vector_store


if __name__ == "__main__":
    pipeline = IncidentIngestionPipeline(docs_path="./data")
    vector_store = pipeline.run_pipeline()
    #pipeline.save_vector_store("./vector_db")