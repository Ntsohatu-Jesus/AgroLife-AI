from app.services.llm_service import generate_response
from app.services.weather_service import get_weather_data
from app.services.rag_service import get_rag_context
from app.services.health_service import get_health_advice

memory = {}


def run_agent(query: str, session_id: str = "default"):
    query_lower = query.lower()

    # Get conversation history
    history = memory.get(session_id, [])
    history_text = " ".join(history).lower()

    # 🔥 COMBINE current query + history
    combined_context = query_lower + " " + history_text

    # WEATHER
    if "weather" in combined_context or "rain" in combined_context:
        weather = get_weather_data("Bamenda")

        prompt = f"""
User question: {query}

Weather data:
{weather}

Give practical farming advice.
"""
        response = generate_response(prompt)

    # HEALTH
    elif any(word in combined_context for word in ["snake", "cut", "injury"]):
        response = get_health_advice(query)

    # FARMING (NOW CONTEXT-AWARE ✅)
    elif any(word in combined_context for word in ["maize", "tomato", "farm", "crop", "plant"]):
        rag_context = get_rag_context(query)

        prompt = f"""
You are an agricultural assistant for African farmers.

Conversation history:
{history}

User question:
{query}

Knowledge:
{rag_context}

Give detailed, step-by-step advice.
"""
        response = generate_response(prompt)

    # DEFAULT
    else:
        response = "I currently focus on farming and basic health advice. Please ask about crops, weather, or farm-related issues."

    # SAVE MEMORY (last 3 messages)
    history.append(query)
    memory[session_id] = history[-3:]

    return response