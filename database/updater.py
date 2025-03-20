from User import User

from .executor import execute
from .replacer import replace_table_data

from exception import log_exception


# Updates an existing chat in the database for the
# current user. Retrieves the current chat data
# and replaces the corresponding entry in the
# database table based on the chat's position in
# the history. Ensures only the modified chat is
# updated while preserving other chat entries.
# Logs any exceptions that occur during the process.
def update_existing_chat(user: User):
    try:
        chats = execute(f"SELECT * FROM t_{user.get_chat_id()};", fetchone=True)
        if chats:
            dialog_index = user.get_history().index(user.get_current_chat()["name"])
            replace_table_data(f"t_{user.get_chat_id()}",
                               user.get_current_chat()["dialog"] if dialog_index == 0 else chats[0],
                               user.get_current_chat()["dialog"] if dialog_index == 1 else chats[1],
                               user.get_current_chat()["dialog"] if dialog_index == 2 else chats[2])
    except Exception as e:
        log_exception(str(e))

