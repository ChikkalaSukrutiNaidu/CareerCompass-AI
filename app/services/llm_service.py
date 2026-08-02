from langchain_groq import ChatGroq
from app.config.settings import GROQ_API_KEY


def get_llm():

    return ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=GROQ_API_KEY,
    )