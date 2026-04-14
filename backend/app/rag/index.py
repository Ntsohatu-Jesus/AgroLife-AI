from loader import load_documents
from splitter import split_docs
from embeddings import get_embeddings
from vector_store import create_vectorstore

docs = load_documents("data/agriculture_docs")
chunks = split_docs(docs)

embeddings = get_embeddings()
vectorstore = create_vectorstore(chunks, embeddings)

vectorstore.save_local("faiss_index")
print("✅ Index built successfully")