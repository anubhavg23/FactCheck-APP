import streamlit as st
import pdfplumber
from google import genai
from google.genai import types
import json
import requests
import time
import warnings
import re

# Warnings ignore
warnings.filterwarnings("ignore")

st.set_page_config(page_title="FactCheck AI", page_icon="🔍", layout="wide")

# --- Helpers ---
def clean_json_response(raw_text):
    try:
        clean_text = re.sub(r'```json\s*|```\s*', '', raw_text).strip()
        return json.loads(clean_text)
    except:
        return None

def get_gemini_client(api_key):
    # Nayi library ka naya Client logic
    return genai.Client(api_key=api_key)

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t: text += t + "\n"
    return text.strip()

# --- Main App Logic ---
try:
    gemini_key = st.secrets["GEMINI_API_KEY"]
    tavily_key = st.secrets["TAVILY_API_KEY"]
    client = get_gemini_client(gemini_key)
    model_id = "gemini-3-flash-preview" # Jo tere code mein tha
except Exception as e:
    st.error("API Keys missing in secrets.toml!")
    st.stop()

st.title("🔍 FactCheck AI (Gemini 3 Powered)")
uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    if st.button("🚀 Analyze Document", type="primary"):
        text = extract_text_from_pdf(uploaded_file)
        
        # Step 1: Claim Extraction
        with st.spinner("🤖 Extracting claims..."):
            prompt = "Extract verifiable claims (stats, dates) as a JSON array: [{\"claim\": \"text\", \"context\": \"...\"}] from: " + text[:8000]
            response = client.models.generate_content(model=model_id, contents=prompt)
            claims = clean_json_response(response.text)

        if claims:
            for i, c in enumerate(claims):
                st.write(f"**Verifying:** {c['claim']}")
                
                # Step 2: Search
                payload = {"api_key": tavily_key, "query": c['claim'], "max_results": 3}
                s_resp = requests.post("https://api.tavily.com/search", json=payload).json()
                evidence = "\n".join([r.get('content', '') for r in s_resp.get('results', [])])

                # Step 3: Verify with Thinking Config
                verify_prompt = f"Claim: {c['claim']}\nEvidence: {evidence}\nVerdict in JSON: {{\"verdict\": \"Verified|Inaccurate|False\", \"explanation\": \"...\"}}"
                
                # Thinking Config jo tune provide kiya
                config = types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(thinking_level="HIGH")
                )
                
                v_res = client.models.generate_content(
                    model=model_id, 
                    contents=verify_prompt,
                    config=config
                )
                
                res = clean_json_response(v_res.text)
                if res:
                    st.json(res) # Simple card for now
            st.balloons()