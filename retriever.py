from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

class Retriever:
    def __init__(self, persist_directory: str = "vector_store"):
        self.vectorstore = FAISS.load_local(
            persist_directory,
            OpenAIEmbeddings(),
            allow_dangerous_deserialization=True
        )

    def retrieve(self, query: str, top_k: int = 3) -> list[str]:
        docs = self.vectorstore.similarity_search(query, k=top_k)
        return [doc.page_content for doc in docs]
