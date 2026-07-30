# Cyber English AI Tutor 🌐

AI-powered English learning platform with cybersecurity-focused vocabulary and personalized tutoring.

## Features

- 📖 **Vocabulary Learning** — AI-powered word analysis with phonetics, examples, and memory tips
- 💬 **AI Conversation** — Practice English with an adaptive AI tutor
- 📚 **Reading Assistant** — Multi-domain articles with smart annotations
- ✍️ **Sentence Analysis** — Grammar checking and improvement suggestions
- 📊 **Learning Dashboard** — Track progress and personalized recommendations

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up your API key (copy .env.example to .env)
cp .env.example .env
# Edit .env and add your API key

# Run the app
streamlit run app.py
```

## Tech Stack

- **Frontend/Backend:** Streamlit (Python)
- **AI:** OpenAI / DeepSeek / Qwen API
- **Database:** SQLite
- **Data:** CSV / Local files

## Project Structure

```
CyberEnglishAI/
├── app.py                 # Main entry point
├── pages/                 # Module pages
│   ├── vocabulary.py
│   ├── conversation.py
│   ├── reading.py
│   ├── sentence.py
│   └── dashboard.py
├── core/                  # Core functionality
│   ├── llm.py            # AI API interface
│   ├── database.py       # SQLite operations
│   └── config.py         # Configuration
├── data/                  # Data files
│   ├── vocabulary.csv
│   ├── articles/
│   └── user_history/
├── utils/                 # Utility modules
│   ├── text_analysis.py
│   └── english_level.py
├── requirements.txt
└── README.md
```
