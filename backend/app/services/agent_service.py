from app.services.llm_service import generate_response, smart_fallback

memory_store = {}


def classify_intent(query: str) -> str:
    q = query.lower()

    if any(word in q for word in ["injury", "cut", "bleeding", "snake", "pain", "wound"]):
        return "health"

    if "weather" in q:
        return "weather"

    if any(word in q for word in ["plan", "schedule"]):
        return "planner"

    return "general"


def run_agent(query: str, session_id: str = "default"):

    intent = classify_intent(query)

    # 🩺 HEALTH
    if intent == "health":
        from app.services.health_service import get_health_advice
        result = get_health_advice(query)
        return {"response": str(result), "session_id": session_id}

    # 🌦 WEATHER
    if intent == "weather":
        from app.services.weather_service import get_weather_data
        result = get_weather_data("Bamenda")
        return {"response": str(result), "session_id": session_id}

    # 📅 PLANNER
    if intent == "planner":
        from app.services.planner_service import generate_plan
        duration = "monthly" if "month" in query.lower() else "weekly"
        result = generate_plan("farming", duration)
        return {"response": str(result), "session_id": session_id}

    # 🤖 AI (MAIN IMPROVEMENT)
    previous = memory_store.get(session_id, "")

    full_prompt = f"""
You are AgroLife AI, an intelligent assistant focused on African farming and rural conditions.

Guidelines:
- Be practical and clear
- Use step-by-step instructions
- Keep answers concise but useful
- Adapt to African farming realities (limited resources, local methods)

Previous conversation:
{previous}

User question:
{query}

Answer:
"""

    ai_response = generate_response(full_prompt)

    if not ai_response or len(ai_response.strip()) < 20:
        ai_response = smart_fallback(query)

    memory_store[session_id] = previous + "\nUser: " + query + "\nAI: " + ai_response

    return {
        "response": str(ai_response),
        "session_id": session_id
    }