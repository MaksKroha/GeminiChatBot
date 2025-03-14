from gemini import short_text
from database import execute
from handlers import SEPARATOR

from User import User


def update_history(user: User):
    keyboard_buttons = []
    try:
        table_data = execute(f"SELECT * FROM t_{user.get_chat_id()}", True)
        if len(table_data) > 1:
            Exception("Table too long")

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
        print("HISTORY UPDATED")
    except Exception as e:
        print(e)

