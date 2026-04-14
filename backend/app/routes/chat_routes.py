from rag.rag_pipeline import get_rag_chain

rag_chain = get_rag_chain()

@router.post("/chat")
def chat(query: str):
    response = rag_chain.run(query)
    return {"response": response}