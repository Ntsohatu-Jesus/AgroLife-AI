from langchain.chains import RetrievalQA
from retriever import get_retriever
from langchain.chat_models import ChatOpenAI  # replace with Gemini later

def get_rag_chain():
    retriever = get_retriever()
    
    llm = ChatOpenAI(temperature=0.3)
    
    return RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )