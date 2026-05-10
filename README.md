# 🔍 FactCheck AI — Automated Truth Layer

An AI-powered fact-checking web app that reads a PDF, extracts verifiable claims, cross-references them against live web data, and flags inaccuracies.

**Live Demo:** `https://your-app.streamlit.app` *(replace after deployment)*

---

## ✨ Features

- 📄 **PDF Upload** — Drag and drop any text-based PDF
- 🤖 **Claim Extraction** — Claude identifies statistics, dates, financial figures, and named facts
- 🌐 **Live Web Search** — Tavily searches the internet in real-time to verify each claim
- 🧠 **AI Verdict** — Claude cross-references web evidence and returns a reasoned verdict
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
# Create .streamlit/secrets.toml (already gitignored)
echo 'ANTHROPIC_API_KEY = "sk-ant-..."' >> .streamlit/secrets.toml
echo 'TAVILY_API_KEY    = "tvly-..."'   >> .streamlit/secrets.toml

# 4. Run the app
streamlit run app.py
```

---

## ☁️ Deploy to Streamlit Cloud (Free)

1. Push this repo to GitHub (keep `.streamlit/secrets.toml` gitignored)
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**
3. Select your repo and `app.py` as the entry point
4. Under **Advanced settings → Secrets**, paste:

```toml
ANTHROPIC_API_KEY = "sk-ant-your-key"
TAVILY_API_KEY    = "tvly-your-key"
```

5. Click **Deploy** — your app will be live in ~2 minutes ✅

---

## 🔑 API Keys (Both Free Tiers)

| Service | Free Tier | Link |
|---|---|---|
| Anthropic | $5 credits on signup | [console.anthropic.com](https://console.anthropic.com) |
| Tavily | 1,000 searches/month | [tavily.com](https://tavily.com) |

---

## 🏗️ Architecture

```
PDF Upload
    │
    ▼
pdfplumber → Extract raw text
    │
    ▼
Claude Sonnet 4 → Identify verifiable claims (JSON)
    │
    ▼  (for each claim)
Tavily Search API → Live web results + quick answer
    │
    ▼
Claude Sonnet 4 → Verdict + explanation + correct info
    │
    ▼
Streamlit UI → Rendered cards + Trust Score + JSON export
```

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

The app is designed to catch intentional lies and outdated statistics. To test:

1. Create a PDF with some intentionally wrong stats (e.g., "ChatGPT has 100 million users as of 2025" when the real number is higher)
2. Upload to the app
3. The app should flag these as **Inaccurate** or **False** and provide the correct figures with sources

---

*Built for the GEO Assessment · Anubhav Gupta · 2025*