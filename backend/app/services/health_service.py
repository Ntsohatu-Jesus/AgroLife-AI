def get_health_advice(symptom: str):
    symptom = symptom.lower()

    # 🐍 Snake bite
    if "snake" in symptom:
        return {
            "condition": "Snake Bite",
            "advice": [
                "Stay calm and reduce movement to slow the spread of venom",
                "Do NOT cut the wound or try to suck out venom",
                "Remove tight clothing or jewelry near the bite area",
                "Keep the bitten area below heart level",
                "Immobilize the limb using cloth or stick if possible",
                "Go to the nearest hospital or health center immediately"
            ],
            "note": "Traditional remedies may delay proper treatment. Seek medical care urgently."
        }

    # 🔪 Cuts / wounds
    elif "cut" in symptom or "bleeding" in symptom:
        return {
            "condition": "Cut / Bleeding",
            "advice": [
                "Wash hands if possible",
                "Clean the wound with clean water",
                "Apply direct pressure with clean cloth to stop bleeding",
                "If available, apply antiseptic",
                "Cover with clean bandage or cloth",
                "Seek medical help if bleeding does not stop"
            ]
        }

    # 🔥 Burns
    elif "burn" in symptom:
        return {
            "condition": "Burn",
            "advice": [
                "Cool the burn with clean running water for at least 10 minutes",
                "Do NOT apply oil, toothpaste, or raw substances",
                "Cover with clean, non-stick cloth",
                "Avoid breaking blisters",
                "Seek medical help for severe burns"
            ]
        }

    # 🤒 Fever
    elif "fever" in symptom:
        return {
            "condition": "Fever",
            "advice": [
                "Drink plenty of clean water",
                "Rest well",
                "Use paracetamol if available",
                "Monitor temperature regularly",
                "Seek medical help if fever persists more than 2 days"
            ]
        }

    # 🩹 General fallback
    else:
        return {
            "message": "Sorry, I can only give basic first-aid advice for now.",
            "suggestion": "Try describing symptoms like 'cut', 'burn', 'snake bite', or 'fever'"
        }