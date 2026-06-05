# 🤖 AI Chatbot with NLP

A conversational AI chatbot combining **rule-based intent matching** with a **transformer-based model** (DialoGPT). Deployable as a terminal app or web interface via Streamlit.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Transformers-yellow.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red.svg)

---

## 🚀 Features

- Rule-based intent detection (greetings, FAQs, farewells)
- Transformer-based fallback using DialoGPT
- Streamlit web interface
- CLI mode for terminal use
- Extensible intent JSON config

---

## 📁 Project Structure

```
ai-chatbot-nlp/
├── chatbot.py           # Core chatbot logic
├── app_streamlit.py     # Streamlit web UI
├── app_cli.py           # CLI interface
├── data/
│   └── intents.json     # Intent definitions (patterns + responses)
├── models/              # Saved model files (if fine-tuned)
├── utils/
│   ├── intent_matcher.py  # Rule-based intent matching
│   └── preprocessor.py    # Text cleaning utilities
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone https://github.com/muhammadtalha-farooq/ai-chatbot-nlp.git
cd ai-chatbot-nlp
pip install -r requirements.txt
```

---

## 🖥️ Usage

**Terminal chatbot:**
```bash
python app_cli.py
```

**Streamlit web interface:**
```bash
streamlit run app_streamlit.py
```

---

## 🧰 Requirements

```
transformers>=4.35.0
torch>=2.0.0
streamlit>=1.28.0
nltk>=3.8.0
numpy>=1.24.0
```

---

## 👤 Author

**Muhammad Talha Farooq**  
AI & Machine Learning Enthusiast | NLP Developer  
[LinkedIn](https://www.linkedin.com/in/muhammadtalha-farooq-73ab5b335)
