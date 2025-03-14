from User import User

from .executor import execute
from .replacer import replace_table_data


def update_existing_chat(user: User):
    chats = execute(f"SELECT * FROM t_{user.get_chat_id()};", fetchone=True)
    print(f"chats - {chats}")
    dialog_index = user.get_history().index(user.get_current_chat()["name"])
    print(f"dialog_index - {dialog_index}")
    print()
    replace_table_data(f"t_{user.get_chat_id()}",
                       user.get_current_chat()["dialog"] if dialog_index == 0 else chats[0],
                       user.get_current_chat()["dialog"] if dialog_index == 1 else chats[1],
                       user.get_current_chat()["dialog"] if dialog_index == 2 else chats[2])
    print("Updated existing chat")
