from exception import log_exception
from handlers import SEPARATOR
from gemini import get_gemini_response
from keyboard import get_reply_keyboard
from User import User


# Adds a new conversation to the user's current chat.
# Marks the chat as modified and generates a response
# using the Gemini API based on the provided message
# and chat context. Updates the current chat dialog
# with the user's message and the generated response.
# Ensures the dialog does not exceed 6 messages by
# trimming older messages if necessary. Sends the
# response to the user with a reply keyboard.
def add_conversation_to_current_chat(bot, user: User, message: str):
    response = get_gemini_response(message, context=user.get_current_chat_dialog())

    if response is None:
        bot.send_message(user.get_chat_id(), "Your message contains violence or sexual nature!")
        return

    user.set_current_chat_modified(True)

    user.set_current_chat_dialog(user.get_current_chat_dialog() + f"{SEPARATOR}{message}")
    user.set_current_chat_dialog(user.get_current_chat_dialog() + f"{SEPARATOR}{response}")

    chat = user.get_current_chat_dialog().strip(SEPARATOR)
    if len(chat.split(SEPARATOR)) > 6:
        sep_first_index = chat.find(SEPARATOR)
        sep_second_index = chat.find(SEPARATOR, sep_first_index + len(SEPARATOR))
        user.set_current_chat_dialog(chat[sep_second_index + len(SEPARATOR):])
    bot.send_message(user.get_chat_id(), response, reply_markup=get_reply_keyboard("History", "New Chat"))
