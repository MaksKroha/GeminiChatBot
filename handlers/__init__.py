# external package import
from dotenv import load_dotenv
from os import getenv

load_dotenv()
SEPARATOR = getenv("SEPARATOR")

# this package import
from .other import other
from .start import start

__all__ = ["start", "other", "SEPARATOR"]

