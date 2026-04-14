from app.services.llm_service import generate_response
from app.services.weather_service import get_weather_data
from app.services.rag_service import get_rag_context
from app.services.health_service import get_health_advice

memory = {}


def run_agent(query: str, session_id: str = "default"):
    query_lower = query.lower()
    previous = memory.get(session_id, "")

    # WEATHER
    if "weather" in query_lower or "rain" in query_lower:
        weather = get_weather_data("Bamenda")

        prompt = f"""
User question: {query}

Weather data:
{weather}

Give practical farming advice based on this weather.
"""
        return generate_response(prompt)

    # HEALTH
    if "snake" in query_lower or "cut" in query_lower or "injury" in query_lower:
        return get_health_advice(query)

    # FARMING → USE RAG
    if any(word in query_lower for word in ["maize", "tomato", "farm", "crop", "plant"]):
        rag_context = get_rag_context(query)

        prompt = f"""
You are an agricultural assistant for African farmers.

Previous conversation:
{previous}

User question:
{query}

Relevant farming knowledge:
{rag_context}

Give detailed, practical, step-by-step advice that a local farmer can follow.
"""

        response = generate_response(prompt)
        memory[session_id] = query
        return response

    # DEFAULT (GENERAL AI)
    prompt = f"""
Answer the question simply and clearly:

{query}
"""

    response = generate_response(prompt)
    memory[session_id] = query

    return response