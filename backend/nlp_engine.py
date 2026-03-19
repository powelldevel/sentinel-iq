import json
import os

# Find the path to our json file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "memory.json")


def load_memory():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_memory(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_to_memory(text):
    memory = load_memory()
    # Don't add duplicates
    if text not in memory:
        memory.append(text)
        save_memory(memory)


def ask_memory(question):
    memory = load_memory()
    if not memory:
        return "Memory is empty. Please ingest news first."

    # Clean up the question and split into words
    question_words = question.lower().strip().split()

    # Look through every fact in our database
    for fact in memory:
        fact_lower = fact.lower()
        # SUCCESS CHECK: If ANY of the user's words (fire, accident, etc.)
        # are found in the stored news, return the whole news report!
        if any(word in fact_lower for word in question_words):
            return f"Sentinel Intelligence Report: {fact}"

    return "I couldn't find anything about that in my memory."