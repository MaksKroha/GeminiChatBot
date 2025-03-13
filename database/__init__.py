import psycopg2
from dotenv import load_dotenv
from os import getenv

from .connection import get_connection

load_dotenv()
CONN = get_connection(getenv("DB_NAME"))

from .executor import execute
from .replacer import replace_table_data

__all__ = ["get_connection", "execute", "replace_table_data", "CONN"]