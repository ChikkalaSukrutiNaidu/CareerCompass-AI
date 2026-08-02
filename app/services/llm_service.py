from langchain_groq import ChatGroq
from app.config.settings import GROQ_API_KEY


def get_llm():
    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )