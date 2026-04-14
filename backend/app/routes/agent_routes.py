from fastapi import APIRouter
from app.services.agent_service import run_agent

router = APIRouter()

@router.get("/agent")
def agent(query: str, session_id: str = "default"):
    response = run_agent(query, session_id)
    return {"response": response, "session_id": session_id}