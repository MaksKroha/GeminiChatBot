from gemini import short_text

from database import execute

import handlers

def update_history(message):
    keyboard_buttons = []
    try:
        table_data = execute(f"SELECT * FROM t_{message.chat.id}", True)
        if len(table_data) > 1:
            Exception("Table too long")

        user_chats = table_data[0]
        for i in range(3):
            if user_chats[i] != "":
                dialog = user_chats[i].strip(handlers.SEPARATOR)
                print("separated", dialog.split(handlers.SEPARATOR))
                first_msg = dialog.split(handlers.SEPARATOR)[0]
                print("START")
                print("first_msg", first_msg)
                response = short_text(first_msg, 25)
                print("END_____")
                print(f"response {response}")
                keyboard_buttons.append(f"{response}")
    except Exception as e:
        print(e)
    print(f"keyboard_buttons {keyboard_buttons}")
    handlers.HISTORY = keyboard_buttons

