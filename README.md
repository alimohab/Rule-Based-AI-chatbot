# 🤖 RuleBot — Rule-Based AI Chatbot

> A lightweight, transparent, and beautifully designed rule-based chatbot with a modern dark-themed web interface. No machine learning, no black boxes — just pure decision logic you can understand and control.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Flask](https://img.shields.io/badge/Flask-2.0+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📖 Overview

**RuleBot** is a conversational chatbot built on explicit rules and a response dictionary. It processes user input through a transparent 4-phase pipeline:

1. **Input Sanitization** — Clean and normalize user text
2. **Exit Check** — Detect if the user wants to end the conversation
3. **Dict Lookup** — Match input against the knowledge base
4. **Response Output** — Return a tailored or fallback response

Perfect for learning chatbot fundamentals, building rule-based systems, or embedding a transparent AI assistant in your application.

---

## ✨ Features

- **Transparent Processing** — Watch all 4 phases execute in real-time
- **Dark Theme UI** — Modern, sleek interface with cyan accents
- **Live Statistics** — Track messages, matches, and fallbacks
- **Suggested Actions** — Quick-access buttons for common queries
- **Extensible** — Add new responses with a single dictionary entry
- **No Dependencies** — Minimal stack: Flask + vanilla JS + CSS
- **Responsive Design** — Works on desktop and tablet
- **Message History** — Persistent chat display within session

---

## 🏗️ Architecture

### 4-Phase Processing Pipeline

```
User Input
    ↓
┌─────────────────────────────────┐
│ Phase 1: Input Sanitization     │  Lowercase, strip whitespace
├─────────────────────────────────┤
│ Phase 2: Exit Check             │  Detect quit commands
├─────────────────────────────────┤
│ Phase 3: Dict Lookup            │  Match in knowledge base
├─────────────────────────────────┤
│ Phase 4: Response Output        │  Send reply (or fallback)
└─────────────────────────────────┘
    ↓
Bot Response
```

Each phase is logged in real-time on the right panel of the UI.

### Knowledge Base

RuleBot ships with 30+ predefined responses across categories:
- **Greetings** — hello, hi, hey, good morning/afternoon/evening
- **Identity** — who are you, what is your name, are you a bot
- **Small Talk** — how are you, tell me a joke, what's up
- **Date/Time** — what time is it, what is today, what year is it
- **Help** — help, what can you do
- **Farewells** — bye, goodbye, see you, exit, quit

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation

1. **Clone or download the repository:**
   ```bash
   cd Rule-Based\ AI\ Chatbot
   ```

2. **Install Flask:**
   ```bash
   pip install flask
   ```

3. **Run the Flask app:**
   ```bash
   python app.py
   ```

4. **Open your browser:**
   ```
   http://localhost:5000
   ```

That's it! 🎉

---

## 📖 Usage

### Web Interface

1. **Type a message** in the input field at the bottom
2. **Press Enter** or click **Send**
3. **Watch the magic** — see all 4 processing phases execute on the right panel
4. **View statistics** — top bar shows message count, matches, and fallbacks
5. **Use suggestions** — click any button to send a quick query

### Example Interactions

```
You: hello
Bot: Hi there! How can I help you today?

You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs! 🐛

You: what time is it
Bot: It's currently 14:32.

You: something random
Bot: I'm not sure I understand. Try typing 'help' to see what I can do.
```

---

## 📁 Project Structure

```
Rule-Based AI Chatbot/
├── app.py                    # Flask application & API endpoints
├── chatbot.py               # Core chatbot logic (4 phases)
├── templates/
│   └── index.html          # Main web interface
├── static/
│   ├── style.css           # Dark theme styling
│   └── script.js           # Interactive functionality
└── README.md               # This file
```

### File Descriptions

| File | Purpose |
|------|---------|
| `app.py` | Flask server, routes, and message processing |
| `chatbot.py` | Core chatbot functions: `get_input()`, `process()`, `RESPONSES` dict |
| `index.html` | Responsive HTML layout with chat, stats, and steps panels |
| `style.css` | Dark grey theme (#1a1a1a, #2a2a2a) with cyan accents (#00d4ff) |
| `script.js` | Real-time message sending, stats updates, step highlighting |

---

## 🎨 Design Highlights

### Dark Theme
- **Background:** Deep charcoal (#1a1a1a, #2a2a2a)
- **Text:** Light grey (#e0e0e0)
- **Accent:** Cyan (#00d4ff)
- **Borders:** Subtle grey (#333)

### Layout
- **Left Panel:** Chat interface with message history
- **Right Panel:** Processing steps visualization
- **Top Bar:** Statistics & breadcrumb navigation
- **Bottom:** Suggested buttons & message input

### Responsive
- Desktop: Side-by-side layout (chat left, steps right)
- Tablet: Steps scroll horizontally below chat

---

## 🔧 Extending RuleBot

### Adding New Responses

Edit `chatbot.py` and add entries to the `RESPONSES` dictionary:

```python
RESPONSES: dict[str, str] = {
    "your question here": "Your response here",
    "another question": "Another response",
}
```

**Example:**
```python
"what is python": "Python is a high-level programming language known for simplicity.",
"tell me a fact": "Did you know? Honey never spoils. Archaeologists found 3000-year-old honey in Egypt!",
```

### Adding Exit Commands

Extend `EXIT_COMMANDS` in `chatbot.py`:

```python
EXIT_COMMANDS: set[str] = {"exit", "quit", "bye", "goodbye", "see you", "logout"}
```

### Modifying the UI

Edit `templates/index.html` to change layout or add new panels. Edit `static/style.css` to customize colors, fonts, or spacing.

---

## 📊 API Endpoints

### `POST /api/message`
Send a message and get a response.

**Request:**
```json
{
  "message": "hello"
}
```

**Response:**
```json
{
  "reply": "Hi there! How can I help you today?",
  "stats": {
    "messages": 1,
    "matched": 1,
    "fallbacks": 0
  },
  "steps_log": [
    "Input sanitization: ✓",
    "Exit check: ✓ (no exit)",
    "Dict lookup: ✓ (match found)",
    "Response output: ✓"
  ],
  "chat_history": [...]
}
```

### `GET /`
Render the main interface.

### `GET /api/suggested`
Get suggested button text (optional, for dynamic updates).

---

## 🧪 Testing

### Unit Testing (Terminal Mode)

Run `chatbot.py` directly for terminal interaction:

```bash
python chatbot.py
```

### Integration Testing (Web Mode)

1. Start `app.py`
2. Open http://localhost:5000
3. Test queries and verify:
   - Stats update correctly
   - Steps highlight during processing
   - Chat history displays messages
   - Suggested buttons work

---

## 🎯 Use Cases

- **Educational Tool** — Learn chatbot architecture and NLP fundamentals
- **Rule-Based Assistant** — Embed in websites or applications
- **FAQ Bot** — Simple knowledge base for customer support
- **Prototyping** — Rapid iteration before ML-based solutions
- **Transparency Demo** — Show how chatbots work internally

---

## 🚫 Limitations

- **No Learning** — Responses are static; the bot doesn't learn from conversations
- **Exact Matching** — Requires exact input match (case-insensitive, whitespace-trimmed)
- **No Intent Classification** — Can't handle semantic variations or typos
- **Single Session** — No persistent storage between restarts
- **No Contextual Memory** — Each message is processed independently

For advanced use cases, consider ML-based approaches like spaCy, RASA, or transformer models.

---

## 🔮 Future Enhancements

- [ ] Fuzzy matching for typos and variations
- [ ] Intent classification (multi-category responses)
- [ ] User feedback mechanism
- [ ] Persistent conversation history (database)
- [ ] Admin panel to edit responses
- [ ] Analytics dashboard
- [ ] Multi-language support
- [ ] API key authentication for external services

---

## 📝 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute.

```
MIT License

Copyright (c) 2025 RuleBot Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, and distribute...
```

---

## 🤝 Contributing

Found a bug? Have an idea? Contributions are welcome!

1. **Fork** the repository
2. **Create a branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

---

## 💬 Questions?

- Check the **FAQ** below
- Review the code comments
- Explore the 4-phase pipeline in `chatbot.py`

### FAQ

**Q: Why rule-based instead of ML?**
A: Rule-based systems are transparent, deterministic, and easy to understand — perfect for learning and simple use cases.

**Q: How do I add custom responses?**
A: Edit the `RESPONSES` dictionary in `chatbot.py` and restart the app.

**Q: Can I use this in production?**
A: Yes, but add authentication, rate limiting, and persistent storage for production use.

**Q: How do I deploy this?**
A: Use Heroku, AWS Lambda, DigitalOcean, or any hosting platform that supports Flask. See their documentation for deployment steps.

---

## 📊 Project Stats

- **Lines of Code:** ~400
- **Responses:** 30+
- **Processing Phases:** 4
- **Dependencies:** Flask only
- **Browser Support:** All modern browsers (Chrome, Firefox, Safari, Edge)

---

## 🌟 Show Your Support

If you find this project useful, please give it a ⭐ on GitHub!

---

**Built with ❤️ by the RuleBot team**

*Last Updated: 2025 | Version 1.0.0*
