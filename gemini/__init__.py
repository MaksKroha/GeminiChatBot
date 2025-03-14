# external libs import
from google import genai
from dotenv import load_dotenv
from os import getenv

__all__ = ["get_gemini_response", "short_text", "client", "SEPARATOR"]


load_dotenv()

API_KEY = getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)
SEPARATOR = getenv("SEPARATOR")


# package modules import
from .response import get_gemini_response
from .shortener import short_text


