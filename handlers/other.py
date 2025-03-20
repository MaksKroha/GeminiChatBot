from .history import update_history
from .clear import clear
from .history_chats import display_chat_in_history
from .chat_modifier import add_conversation_to_current_chat

from keyboard import get_reply_keyboard

from User import User
from database import add_new_chat_to_db
from database import update_existing_chat


# Handles user commands and interactions outside
# of direct chat input. Processes commands like
# "history" and "new chat". For "history", it
# updates the chat history, clears previous
# messages, and displays available options. For
# "new chat", it resets the current chat and
# prepares for a new conversation. If the user
# selects a chat from history, it displays the
# chat. For invalid inputs, it provides available
# options. Otherwise, it adds the user's message
# and AI response to the current chat dialog.
def other(bot, user: User, message: str, message_id: int):
    if message.lower() == "history":
        # checking if user is some chat now
        if user.get_current_chat():
            if user.get_current_chat()["name"] is None and \
                    user.get_current_chat()["dialog"] != "":
                add_new_chat_to_db(user)

            if user.get_history() and \
                    user.get_current_chat()["name"] in user.get_history() and \
                    user.get_current_chat()["modified"]:
                update_existing_chat(user)

        update_history(user)
        clear(bot, user.get_chat_id(), message_id - 20, message_id - 1)
        bot.send_message(user.get_chat_id(),
                         "Please select option for you!",
                         reply_markup=get_reply_keyboard(
                             "New Chat",
                             *user.get_history() if user.get_history() else [])
                         )

    elif message.lower() == "new chat":
        # setting user window into new_chat window
        clear(bot, user.get_chat_id(), message_id - 20, message_id - 1)
        user.set_current_chat({"name": None, "dialog": "", "modified": False})
        bot.send_message(user.get_chat_id(), "Ask me about something",
                         reply_markup=get_reply_keyboard("History", "New Chat"))

    elif user.get_history() and message + "\n" in user.get_history():
        # if user selected chat from history list, if so - display chat history
        display_chat_in_history(bot, user, message)
    elif user.current_chat is None:
        # if user type something wrong
        # giving possible options available on his stage
        bot.send_message(user.get_chat_id(),
                         "Please select option for you!",
                         reply_markup=get_reply_keyboard("History", "New Chat"))
    else:
        # adding his message and AI response to user chat dialog
        add_conversation_to_current_chat(bot, user, message)
