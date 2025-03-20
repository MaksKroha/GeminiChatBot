from User import User

from .executor import execute
from .replacer import replace_table_data

from database import SEPARATOR

from exception import log_exception


# Adds a new chat to the database for the current
# user. Retrieves existing chat data and updates
# the table by inserting the new chat dialog at
# the top, shifting older chats down. Ensures the
# new chat is added while preserving the previous
# two chats. Logs any exceptions that occur
# during the process.
def add_new_chat_to_db(user: User):
    try:
        chats = execute(f"SELECT * FROM t_{user.get_chat_id()};", fetchone=True)
        if chats:
            replace_table_data(f"t_{user.get_chat_id()}",
                               user.get_current_chat()["dialog"].strip(SEPARATOR),
                               chats[0],
                               chats[1])
    except Exception as e:
        log_exception(str(e))

