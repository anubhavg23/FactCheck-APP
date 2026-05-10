# 🔍 FactCheck AI — Automated Truth Layer

An AI-powered fact-checking web app that reads a PDF, extracts verifiable claims, cross-references them against live web data, and flags inaccuracies — powered by **Gemini 2.5 Flash** (with Thinking) + **Tavily Search**.

**Live Demo:** `https://your-app.streamlit.app` *(replace after deployment)*

---

## ✨ Features

- 📄 **PDF Upload** — Drag and drop any text-based PDF
- 🤖 **Claim Extraction** — Gemini Flash identifies stats, dates, financial figures, and named facts
- 🌐 **Live Web Search** — Tavily searches the internet in real-time to verify each claim
- 🧠 **Deep Reasoning** — Gemini's Thinking Mode (`thinking_level: HIGH`) cross-references evidence
- 📊 **Trust Score** — Document-level credibility score based on flagged claims
- 📥 **JSON Export** — Download the full structured report

## 🏷️ Verdict Types

| Verdict | Meaning |
|---|---|
| ✅ Verified | Claim matches current web evidence |
| ⚠️ Inaccurate | Claim is outdated or the number is wrong |
| ❌ False | Claim contradicts evidence or zero credible evidence found |

---

## 🚀 Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/factcheck-ai.git
cd factcheck-ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your API keys
mkdir -p .streamlit
cat > .streamlit/secrets.toml << 'KEYS'
GEMINI_API_KEY = "AIza-your-key-here"
TAVILY_API_KEY = "tvly-your-key-here"
KEYS

# 4. Run the app
streamlit run app.py
```

---

## ☁️ Deploy to Streamlit Cloud (Free)

1. Push this repo to GitHub — keep `.streamlit/secrets.toml` gitignored
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Select your repo and set `app.py` as the entry point
4. Under **Advanced settings → Secrets**, paste:

```toml
GEMINI_API_KEY = "AIza-your-key"
TAVILY_API_KEY = "tvly-your-key"
```

5. Click **Deploy** — live in ~2 minutes ✅

---

## 🔑 API Keys (Both Free)

| Service | Free Tier | Link |
|---|---|---|
| Google Gemini | Free via AI Studio | [aistudio.google.com](https://aistudio.google.com) |
| Tavily | 1,000 searches/month | [tavily.com](https://tavily.com) |

---

## 🏗️ Architecture

```
PDF Upload
    │
    ▼
pdfplumber ──► Extract raw text
    │
    ▼
Gemini 2.5 Flash ──► Identify verifiable claims (JSON array)
    │
    ▼  (for each claim)
Tavily Search API ──► Live web results (top 3)
    │
    ▼
Gemini 2.5 Flash + Thinking (HIGH) ──► Verdict + explanation
    │
    ▼
Streamlit UI ──► Cards + Trust Score + JSON download
```

---

## 🧠 Tech Stack

| Layer | Tool |
|---|---|
| Frontend | Streamlit |
| PDF Parsing | pdfplumber |
| AI Model | `gemini-2.5-flash-preview` (google-genai) |
| Reasoning | `ThinkingConfig(thinking_level="HIGH")` |
| Web Search | Tavily API |

---

## 📁 File Structure

```
factcheck-ai/
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── .gitignore
├── .streamlit/
│   └── secrets.toml        # API keys (gitignored — DO NOT COMMIT)
└── README.md
```

---

## 🧪 Testing with a Trap Document

The app catches intentional lies and outdated statistics. To test:

1. Create a PDF with wrong stats (e.g., *"ChatGPT has 50 million users as of 2024"*)
2. Upload to the app
3. The app should flag this as **Inaccurate** or **False** with correct figures + sources

---

*Built for GEO Product Assessment · Anubhav Gupta · 2025*