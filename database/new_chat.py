from User import User

from .executor import execute
from .replacer import replace_table_data

from database import SEPARATOR


def add_new_chat_to_db(user: User):
    chats = execute(f"SELECT * FROM t_{user.get_chat_id()};", fetchone=True)
    replace_table_data(f"t_{user.get_chat_id()}",
                       user.get_current_chat()["dialog"].strip(SEPARATOR),
                       chats[0],
                       chats[1])
    print("Added new chat")
