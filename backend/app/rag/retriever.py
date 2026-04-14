from langchain_community.vectorstores import FAISS
from embeddings import get_embeddings

def get_retriever():
    embeddings = get_embeddings()
    db = FAISS.load_local("faiss_index", embeddings)
    return db.as_retriever(search_kwargs={"k": 3})