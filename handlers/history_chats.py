from telebot.formatting import hbold as bold
from database import execute
from keyboard import get_reply_keyboard
from User import User
from handlers import SEPARATOR


# Displays a specific chat from the user's history.
# Searches for the chat matching the provided message
# in the user's history. If found, retrieves the
# corresponding dialog from the database and sets it
# as the current chat. Splits the dialog into messages
# and sends them to the user, formatting them as either
# "You: [message]" or "Gemini: [message]". Uses HTML
# parsing for bold text and provides a reply keyboard
# with options like "History" and "New Chat".
def display_chat_in_history(bot, user: User, message: str):
    for i in range(len(user.get_history())):
        if message + "\n" == user.get_history()[i]:

            dialog = execute(f"SELECT chat_{i + 1} FROM t_{user.get_chat_id()}", fetchone=True)
            if dialog:
                dialog = dialog[0]
                user.set_current_chat({"name": user.get_history()[i], "dialog": dialog, "modified": False})

                for msg_i, chat_msg in enumerate(dialog.split(SEPARATOR)):
                    chat_msg = bold(f"You: {chat_msg}") if msg_i % 2 == 0 else bold("Gemini: ") + chat_msg
                    bot.send_message(user.get_chat_id(),
                                     chat_msg,
                                     reply_markup=get_reply_keyboard("History", "New Chat"),
                                     parse_mode="HTML")
            break
