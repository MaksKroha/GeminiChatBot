# external package import
from dotenv import load_dotenv
from os import getenv

load_dotenv()
SEPARATOR = getenv("SEPARATOR")

HISTORY = None

current_chat = None

# this package import
from .history import update_history
from .other import other
from .start import start

__all__ = ["update_history", "other", "start", "HISTORY", "SEPARATOR", "current_chat"]

