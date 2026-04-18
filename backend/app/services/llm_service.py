import os

# If Gemini works, keep it; otherwise fallback still works
try:
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
    model = genai.GenerativeModel("gemini-2.0-flash")
except:
    model = None


def generate_response(prompt: str) -> str:
    try:
        if model:
            response = model.generate_content(prompt)
            return response.text
        else:
            return None
    except:
        return None


def smart_fallback(query: str) -> str:
    query = query.lower()

    # 🌱 Farming fallback
    if any(word in query for word in ["plant", "grow", "farm", "crop", "maize", "rice", "cassava", "tomato", "yam"]):
        return """Farming Advice:

- Use fertile, well-drained soil
- Plant at the right season for your region
- Water early morning or evening
- Apply organic manure if possible
- Monitor for pests regularly

For best results, adapt these steps to your local climate conditions."""

    # 🩺 Health fallback
    if any(word in query for word in ["pain", "injury", "cut", "wound", "bleeding"]):
        return """Basic First Aid:

- Clean the affected area with clean water
- Apply pressure if bleeding
- Cover with clean cloth or bandage
- Seek medical attention if condition worsens"""

    # 🌍 General fallback (NEW — very important)
    return f"""I understand your question: "{query}"

Currently, I specialize in:
- Farming advice
- Basic health guidance
- Weather insights
- Farming plans

Please try asking within these areas, or rephrase your question for better assistance."""