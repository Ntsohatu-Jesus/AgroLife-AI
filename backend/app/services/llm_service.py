import os
import requests

API_KEY = os.getenv("GEMINI_API_KEY")

def generate_response(prompt: str):
    try:
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash:generateContent?key={API_KEY}"

        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "contents": [
                {
                    "parts": [
                        {"text": f"""
You are AgroLife AI.

You MUST give practical, detailed, step-by-step farming advice suitable for African farmers.

Be SPECIFIC to the crop mentioned.

DO NOT give generic answers.

Question:
{prompt}
"""}
                    ]
                }
            ]
        }

        response = requests.post(url, headers=headers, json=data)

        result = response.json()

        print("DEBUG GEMINI:", result)  # 🔥 VERY IMPORTANT

        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]

        return None

    except Exception as e:
        print("LLM ERROR:", e)
        return None