import psycopg2
from dotenv import load_dotenv
from os import getenv

from .connection import get_connection

load_dotenv()

CONN = get_connection(getenv("DB_NAME"),
                      getenv("DB_HOST"),
                      getenv("DB_USER"),
                      getenv("DB_PASSWORD"),
                      getenv("DB_PORT"))
SEPARATOR = getenv("SEPARATOR")


from .executor import execute
from .replacer import replace_table_data
from .new_chat import add_new_chat_to_db
from .updater import update_existing_chat

__all__ = ["add_new_chat_to_db", "update_existing_chat", "execute",
           "replace_table_data", "CONN", "SEPARATOR"]