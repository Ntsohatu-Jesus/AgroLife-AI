from langchain_community.document_loaders import TextLoader
import os

def load_documents(path):
    docs = []
    for file in os.listdir(path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(path, file))
            docs.extend(loader.load())
    return docs