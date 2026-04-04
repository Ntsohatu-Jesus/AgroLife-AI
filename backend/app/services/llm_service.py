import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ Use EXACT model format from test.py output
MODEL_NAME = "models/gemini-flash-latest"

def generate_response(prompt: str):
    try:
        model = genai.GenerativeModel(MODEL_NAME)

        response = model.generate_content(prompt)

        if hasattr(response, "text") and response.text:
            return response.text

        return "No response generated."

    except Exception as e:
        return f"Error: {str(e)}"