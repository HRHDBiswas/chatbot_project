"""
Simple Rule-Based Chatbot
HCI Course - Traditional Chatbot Project
Uses: Python standard library + NLTK
"""

import re
import random
import string
import nltk

# Download required NLTK data (only needed once)
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

# ─────────────────────────────────────────────
#  Intent definitions: patterns + responses
# ─────────────────────────────────────────────
INTENTS = {
    "greeting": {
        "patterns": [
            r"h+e+l+o+",
            r"\bhi+\b",
            r"\bhey\b",
            r"\bhiya\b",
            r"good\s*(morning|afternoon|evening|day)",
            r"what'?s\s*up",
            r"howdy",
            r"sup\b",
        ],
        "responses": [
            "Hello! How can I help you today?",
            "Hey there! What can I do for you?",
            "Hi! Ask me anything — type 'help' to see what I can do.",
            "Good to see you! What's on your mind?",
        ],
    },
    "farewell": {
        "patterns": [
            r"\bbye\b",
            r"goodbye",
            r"see\s*you",
            r"\blater\b",
            r"take\s*care",
            r"have\s*a\s*good",
            r"good\s*night",
            r"ciao",
        ],
        "responses": [
            "Goodbye! Have a great day!",
            "See you around!",
            "Take care!",
            "Bye! Come back if you have more questions.",
        ],
    },
    "capabilities": {
        "patterns": [
            r"what\s*can\s*you\s*do",
            r"\bhelp\b",
            r"\bcommands?\b",
            r"capabilities",
            r"features",
            r"what\s*do\s*you\s*(do|know|support)",
            r"how\s*do\s*you\s*work",
            r"your\s*(functions?|abilities|skills)",
        ],
        "responses": [
            (
                "Here's what I can do:\n"
                "  • Respond to greetings and farewells\n"
                "  • Tell you about myself\n"
                "  • Answer basic questions\n"
                "  • Handle unrecognized input gracefully\n"
                "Try asking: 'who are you', 'hello', or 'bye'."
            )
        ],
    },
    "identity": {
        "patterns": [
            r"who\s*are\s*you",
            r"what\s*are\s*you",
            r"tell\s*me\s*about\s*(your)?self",
            r"your\s*name",
            r"are\s*you\s*(a\s*)?(bot|robot|ai|computer|human)",
            r"introduce\s*yourself",
        ],
        "responses": [
            "I'm a simple rule-based chatbot built with Python and NLTK. I use pattern matching — no AI or machine learning under the hood.",
            "I'm a traditional chatbot: I match your input against predefined patterns and return a scripted response. No LLMs here!",
        ],
    },
    "thanks": {
        "patterns": [
            r"thank(s|\s*you)",
            r"thx",
            r"ty\b",
            r"appreciate\s*it",
            r"cheers",
        ],
        "responses": [
            "You're welcome!",
            "Happy to help!",
            "No problem at all!",
            "Anytime!",
        ],
    },
    "fallback": {
        "patterns": [r".*"],
        "responses": [
            "I'm not sure I understand. Could you rephrase that?",
            "Hmm, I didn't quite catch that. Try asking 'help' to see what I can do.",
            "That one's outside my capabilities. Type 'help' for a list of things I understand.",
            "I don't have a response for that — yet. Try asking me something else.",
        ],
    },
}


# ─────────────────────────────────────────────
#  Text normalisation
# ─────────────────────────────────────────────
def normalize(text: str) -> str:
    """Lowercase and strip punctuation."""
    text = text.lower().strip()
    text = text.translate(str.maketrans("", "", string.punctuation))
    return text


# ─────────────────────────────────────────────
#  Intent matching
# ─────────────────────────────────────────────
def get_response(user_input: str) -> str:
    """Return the best response for the given input."""
    cleaned = normalize(user_input)
    for intent, data in INTENTS.items():
        for pattern in data["patterns"]:
            if re.search(pattern, cleaned):
                return random.choice(data["responses"])
    # Should never reach here because 'fallback' catches everything
    return "I don't have a response for that."


# ─────────────────────────────────────────────
#  Main conversation loop
# ─────────────────────────────────────────────
def main():
    print("=" * 50)
    print("  Simple Rule-Based Chatbot")
    print("  Type 'help' to see capabilities.")
    print("  Type 'quit' or 'exit' to stop.")
    print("=" * 50)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Goodbye!")
            break

        if not user_input:
            continue

        if user_input.lower() in {"quit", "exit"}:
            print("Bot: Goodbye! Have a great day!")
            break

        response = get_response(user_input)
        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
