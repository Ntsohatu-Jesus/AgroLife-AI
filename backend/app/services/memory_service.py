conversation_memory = {}


def save_message(session_id: str, role: str, message: str):
    if session_id not in conversation_memory:
        conversation_memory[session_id] = []

    conversation_memory[session_id].append({
        "role": role,
        "message": message
    })


def get_history(session_id: str):
    return conversation_memory.get(session_id, [])