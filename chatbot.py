"""
Rule-Based AI Chatbot
=====================
A simple conversational chatbot using if-else logic and a response dictionary.
Handles greetings, farewells, FAQs, and unknown inputs gracefully.

How to run:
    python chatbot.py
"""

import datetime


# ──────────────────────────────────────────────
# PHASE 1 — Input sanitization
# ──────────────────────────────────────────────

def get_input(prompt="You: ") -> str:
    """Read a line from the user and return it cleaned (lowercase, stripped)."""
    raw_input = input(prompt)
    clean_input = raw_input.lower().strip()
    return clean_input


# ──────────────────────────────────────────────
# PHASE 2 — Response knowledge base
# ──────────────────────────────────────────────

RESPONSES: dict[str, str] = {
    # Greetings
    "hello":            "Hi there! How can I help you today?",
    "hi":               "Hey! Great to see you. What's on your mind?",
    "hey":              "Hey! What can I do for you?",
    "good morning":     "Good morning! Hope your day is off to a great start.",
    "good afternoon":   "Good afternoon! How's everything going?",
    "good evening":     "Good evening! How can I assist you tonight?",

    # Identity
    "what is your name":    "I'm RuleBot — a simple rule-based chatbot.",
    "who are you":          "I'm RuleBot, a chatbot built with if-else logic and a response dictionary.",
    "what are you":         "I'm a rule-based AI chatbot. I match your input to predefined responses.",
    "are you a bot":        "Yes! I'm a bot — no neural network, just pure decision logic.",
    "are you human":        "No, I'm a chatbot. But I'm happy to chat!",

    # Small talk
    "how are you":          "I'm doing great, thanks for asking! How about you?",
    "how are you doing":    "Running perfectly on clean logic. You?",
    "what's up":            "Not much — just waiting for your next message!",
    "tell me a joke":       "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
    "another joke":         "Why did the developer go broke? Because he used up all his cache!",

    # Date / time
    "what time is it":      f"It's currently {datetime.datetime.now().strftime('%H:%M')}.",
    "what is today":        f"Today is {datetime.datetime.now().strftime('%A, %B %d, %Y')}.",
    "what year is it":      f"It's {datetime.datetime.now().year}.",

    # Capabilities
    "what can you do":      "I can greet you, answer basic questions, tell jokes, share the time, and more. Type 'help' for a full list.",
    "help":                 (
        "Here are things I understand:\n"
        "  Greetings  : hello, hi, hey, good morning/afternoon/evening\n"
        "  Identity   : who are you, what is your name, are you a bot\n"
        "  Small talk : how are you, tell me a joke, what's up\n"
        "  Date/time  : what time is it, what is today, what year is it\n"
        "  Info       : what can you do, help\n"
        "  Goodbye    : bye, goodbye, see you, exit, quit"
    ),

    # Farewells
    "bye":          "Goodbye! Have a wonderful day! 👋",
    "goodbye":      "Farewell! Come back anytime.",
    "see you":      "See you later! Take care.",
    "see you later":"Catch you later!",
    "take care":    "You too! Bye for now.",
}

# Inputs that signal the user wants to exit the loop
EXIT_COMMANDS: set[str] = {"exit", "quit", "bye", "goodbye", "see you", "see you later"}


# ──────────────────────────────────────────────
# PHASE 3 — Response processor
# ──────────────────────────────────────────────

FALLBACK = "I'm not sure I understand. Try typing 'help' to see what I can do."

def process(user_input: str) -> str:
    """
    Look up user_input in the RESPONSES dict.
    Falls back to FALLBACK if no match is found.
    """
    return RESPONSES.get(user_input, FALLBACK)


# ──────────────────────────────────────────────
# PHASE 4 — Main loop
# ──────────────────────────────────────────────

def main() -> None:
    print("=" * 48)
    print("  RuleBot — Rule-Based AI Chatbot")
    print("  Type 'help' to see what I know.")
    print("  Type 'exit' or 'bye' to quit.")
    print("=" * 48)
    print()

    while True:
        user_input = get_input()

        # Guard against empty input
        if not user_input:
            print("Bot: Please type something!\n")
            continue

        # Exit condition — check BEFORE processing
        if user_input in EXIT_COMMANDS:
            reply = RESPONSES.get(user_input, "Goodbye!")
            print(f"Bot: {reply}\n")
            break  # Exit the loop

        # Normal response
        reply = process(user_input)
        print(f"Bot: {reply}\n")


# ──────────────────────────────────────────────
# Entry point
# ──────────────────────────────────────────────

if __name__ == "__main__":
    main()