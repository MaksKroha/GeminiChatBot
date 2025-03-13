from keyboard import get_reply_keyboard
from database import execute


def start(bot, message):
    try:
        reply_keyboard = get_reply_keyboard("History", "New Chat")
        start_message = f"Hello, dear {message.chat.username}"


        execute(f"""
            CREATE TABLE IF NOT EXISTS t_{message.chat.id}(
                chat_1 TEXT,
                chat_2 TEXT,
                chat_3 TEXT
            );
        """)
        execute(f"""
            INSERT INTO t_{message.chat.id}(chat_1, chat_2, chat_3) 
            SELECT '', '', '' 
            WHERE NOT EXISTS (SELECT 1 FROM t_{message.chat.id});
        """)

        bot.send_message(message.chat.id, start_message, reply_markup=reply_keyboard)
    except Exception as e:
        print(e)