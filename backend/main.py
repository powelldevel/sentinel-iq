import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. This tells Python to look in the current folder for your other files
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import nlp_engine as nlp
import data_ingestion as di

# 2. We create the "app" first
app = FastAPI()

# 3. NOW we add the Security Handshake (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "SentinelIQ is standing guard!"}

@app.post("/analyze")
def analyze(text: str):
    return nlp.analyze_text(text)

@app.post("/ingest_news/")
def ingest_news():
    articles = di.fetch_incident_news()
    for art in articles:
        content = f"{art.get('title')} - {art.get('description')}"
        nlp.add_to_memory(content)
    return {"message": f"Successfully ingested {len(articles)} articles."}

@app.get("/ask_sentinel/")
def ask_sentinel(question: str):
    return {"answer": nlp.ask_memory(question)}