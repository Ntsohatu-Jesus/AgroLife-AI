import os

DATA_PATH = "app/rag/data/farming_knowledge.txt"


def load_knowledge():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return f.read()


def simple_search(query: str, knowledge: str):
    query_words = query.lower().split()

    best_lines = []

    for line in knowledge.split("\n"):
        for word in query_words:
            if word in line.lower():
                best_lines.append(line)

    return "\n".join(best_lines[:5])


def get_rag_context(query: str):
    knowledge = load_knowledge()
    context = simple_search(query, knowledge)

    return context if context else "No relevant farming data found."