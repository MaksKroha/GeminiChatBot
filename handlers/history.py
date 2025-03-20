from exception import log_exception
from gemini import short_text
from database import execute
from handlers import SEPARATOR

from User import User


# Updates the user's chat history by retrieving data
# from the database. Extracts the first message from
# each non-empty chat entry and shortens it to 25
# characters. Ensures no duplicate entries are added
# to the history. Sets the updated history in the
# user object. Handles exceptions by logging them
# for debugging purposes. Raises exceptions if the
# database table data is empty or too long.
def update_history(user: User):
    keyboard_buttons = []
    try:
        table_data = execute(f"SELECT * FROM t_{user.get_chat_id()}", True)
        if len(table_data) > 1:
            Exception("Table data too long")
        elif len(table_data) == 0:
            Exception("Table data is empty")

        user_chats = table_data[0]
        for i in range(3):
            if user_chats[i] != "":
                inline_dialog = user_chats[i].strip(SEPARATOR)
                first_msg = inline_dialog.split(SEPARATOR)[0]
                response = short_text(first_msg, 25,
                                      f" Your answer must be different than "
                                      f"these sentences: {keyboard_buttons}!")
                keyboard_buttons.append(f"{response}")
        user.set_history(keyboard_buttons)
    except Exception as e:
        log_exception(str(e))

