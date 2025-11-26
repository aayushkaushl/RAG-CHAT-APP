import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("api_key")
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LLM_MODEL = "gpt-4o-mini"
