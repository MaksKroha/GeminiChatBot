from keyboard import get_reply_keyboard
from database import execute
from User import User

def start(bot, user: User, message: str):
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
        print(e)