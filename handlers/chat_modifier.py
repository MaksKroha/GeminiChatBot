from handlers import SEPARATOR
from gemini import get_gemini_response
from keyboard import get_reply_keyboard
from User import User


def add_conversation_to_current_chat(bot, user: User, message: str):
    user.set_current_chat_modified(True)
    response = get_gemini_response(message, context=user.get_current_chat_dialog())

    user.set_current_chat_dialog(user.get_current_chat_dialog() + f"{SEPARATOR}{message}")
    user.set_current_chat_dialog(user.get_current_chat_dialog() + f"{SEPARATOR}{response}")

    chat = user.get_current_chat_dialog().strip(SEPARATOR)
    if len(chat.split(SEPARATOR)) > 6:
        sep_first_index = chat.find(SEPARATOR)
        sep_second_index = chat.find(SEPARATOR, sep_first_index + len(SEPARATOR))
        user.set_current_chat_dialog(chat[sep_second_index + len(SEPARATOR):])
    bot.send_message(user.get_chat_id(), response, reply_markup=get_reply_keyboard("History", "New Chat"))