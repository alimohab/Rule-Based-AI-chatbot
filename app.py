from flask import Flask, render_template, request, jsonify
import datetime
from chatbot import RESPONSES, EXIT_COMMANDS, FALLBACK, process

app = Flask(__name__)

stats = {
    "messages": 0,
    "matched": 0,
    "fallbacks": 0
}

chat_history = []
processing_steps = [
    {"id": 1, "title": "Input sanitization", "status": "waiting"},
    {"id": 2, "title": "Exit check", "status": "waiting"},
    {"id": 3, "title": "Dict lookup", "status": "waiting"},
    {"id": 4, "title": "Response output", "status": "waiting"},
]


@app.route("/")
def index():
    return render_template("index.html", stats=stats, steps=processing_steps)


@app.route("/api/message", methods=["POST"])
def handle_message():
    data = request.json
    user_input = data.get("message", "").lower().strip()

    if not user_input:
        return jsonify({"error": "Empty message"}), 400

    stats["messages"] += 1

    # Phase 1: Input sanitization - already done above
    steps_log = ["Input sanitization: ✓"]

    # Phase 2: Exit check
    if user_input in EXIT_COMMANDS:
        steps_log.append("Exit check: ✓ (exit detected)")
        reply = RESPONSES.get(user_input, "Goodbye!")
    else:
        steps_log.append("Exit check: ✓ (no exit)")
        # Phase 3: Dict lookup
        if user_input in RESPONSES:
            stats["matched"] += 1
            steps_log.append("Dict lookup: ✓ (match found)")
            reply = RESPONSES[user_input]
        else:
            stats["fallbacks"] += 1
            steps_log.append("Dict lookup: ✗ (fallback)")
            reply = FALLBACK

    steps_log.append("Response output: ✓")

    chat_history.append({
        "type": "user",
        "message": user_input,
        "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
    })

    chat_history.append({
        "type": "bot",
        "message": reply,
        "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
    })

    return jsonify({
        "reply": reply,
        "stats": stats,
        "steps_log": steps_log,
        "chat_history": chat_history[-4:]
    })


@app.route("/api/suggested", methods=["GET"])
def get_suggested():
    return jsonify({
        "suggested": ["hello", "how are you", "tell me a joke", "what time is it",
                     "what can you do", "help", "who are you", "bye", "unknown input"]
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
