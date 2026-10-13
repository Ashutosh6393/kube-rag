import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
    QDRANT_CLUSTER_ENDPOINT = os.getenv("QDRANT_CLUSTER_ENDPOINT")
    QDRANT_COLLECTION = "kube-rag"

    GROK_API_KEY = os.getenv("GROK_API_KEY")
    GROK_MODEL = "llama-3.3-70b-versatile"



settings = Settings()