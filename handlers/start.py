from exception import log_exception
from keyboard import get_reply_keyboard
from database import execute
from User import User


# Initializes the user's interaction with the bot.
# Sends a welcome message addressing the user by
# their username and provides a reply keyboard
# with options like "History" and "New Chat".
# Ensures a database table specific to the user's
# chat ID exists, creating it if necessary. The
# table stores up to three chat entries (chat_1,
# chat_2, chat_3), initialized with empty strings
# if no data is present. Handles exceptions by
# logging them for debugging purposes. This
# function is typically called when the user
# starts or restarts the conversation with the bot.
def start(bot, user: User):
    try:
        reply_keyboard = get_reply_keyboard("History", "New Chat")
        start_message = f"Hello, dear {user.get_username()}"


        execute(f"""
            CREATE TABLE IF NOT EXISTS t_{user.get_chat_id()}(
                chat_1 TEXT,
                chat_2 TEXT,
                chat_3 TEXT
            );
        """)
        execute(f"""
            INSERT INTO t_{user.get_chat_id()}(chat_1, chat_2, chat_3) 
            SELECT '', '', '' 
            WHERE NOT EXISTS (SELECT 1 FROM t_{user.get_chat_id()});
        """)

        bot.send_message(user.get_chat_id(), start_message, reply_markup=reply_keyboard)
    except Exception as e:
        log_exception(str(e))