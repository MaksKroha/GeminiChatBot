from .history import update_history
from .clear import clear

from keyboard import get_reply_keyboard

from handlers import SEPARATOR

from database import execute
from database import replace_table_data

from gemini import get_gemini_response

import handlers


def other(bot, message):
    if message.text.lower() == "history":
        print("history")
        if handlers.current_chat:
            print("current chat")
            if handlers.current_chat["name"] is None:
                print("handlers.current_chat[name] is None")
                if handlers.current_chat["dialog"] != "" and handlers.current_chat["modified"]:
                    print("hdl.current_chat[dialog] != """)
                    chats = execute(f"SELECT * FROM t_{message.chat.id};", fetchone=True)
                    print(f"chats: {chats}")
                    replace_table_data(f"t_{message.chat.id}",
                                       handlers.current_chat["dialog"].strip(handlers.SEPARATOR),
                                       chats[0],
                                       chats[1])
                    print("ends")
            if handlers.current_chat["name"] in handlers.HISTORY:
                print("handlers.current_chat[name] in handlers.HISTORY")
                if handlers.current_chat["modified"]:
                    chats = execute(f"SELECT * FROM t_{message.chat.id};", fetchone=True)
                    replace_table_data(f"t_{message.chat.id}",
                                       handlers.current_chat["dialog"] if handlers.HISTORY.index(handlers.current_chat["name"]) == 0 else chats[0],
                                       handlers.current_chat["dialog"] if handlers.HISTORY.index(handlers.current_chat["name"]) == 1 else chats[1],
                                       handlers.current_chat["dialog"] if handlers.HISTORY.index(handlers.current_chat["name"]) == 2 else chats[2])
                    print("updated table existing chats")
            # if current_chat["name"] in HISTORY:
            # create a new package with database communication
            # change table if modified

        update_history(message)
        print("history updated")
        clear(bot, message.chat.id, message.message_id - 10, message.message_id - 1)
        print("messages cleared")
        print(f"history - {handlers.HISTORY if handlers.HISTORY else []}")
        bot.send_message(message.chat.id,
                         "Please select option for you!",
                         reply_markup=get_reply_keyboard("New Chat", *handlers.HISTORY if handlers.HISTORY else []))
        print("msg sent")

    elif message.text.lower() == "new chat":
        print("new chat")
        clear(bot, message.chat.id, message.message_id - 10, message.message_id - 1)
        handlers.current_chat = {"name": None, "dialog": "", "modified": False}
    # clear all messages
    # just saving message into a list
    # after history btn checks if user was chating
    # if so save to bd
    elif handlers.HISTORY and message.text == handlers.HISTORY[0].strip("\n"):
        print("history[0]")
        # handlers.current_chat = "chat_1"

        dialog = execute(f"SELECT * FROM t_{message.chat.id}", fetchone=True)[0]
        handlers.current_chat = {"name": handlers.HISTORY[0], "dialog": dialog, "modified": False}

        print(dialog)
        chat = dialog.split(SEPARATOR)

        for chat_msg in chat:
            bot.send_message(message.chat.id,
                             chat_msg,
                             reply_markup=get_reply_keyboard("History", "New Chat"))
    # TODO: replace 3 elifs with one function!!!
    elif handlers.current_chat is None:
        print("handlers.current_chat is None")
        bot.send_message(message.chat.id,
                         "Please select option for you!",
                         reply_markup=get_reply_keyboard("History", "New Chat"))
    else:
        print("Chat with responses")
        handlers.current_chat["modified"] = True
        handlers.current_chat["dialog"] = handlers.current_chat["dialog"] + f"{SEPARATOR}{message.text}"
        response = get_gemini_response(message.text)
        handlers.current_chat["dialog"] = handlers.current_chat["dialog"] + f"{SEPARATOR}{response}"
        bot.send_message(message.chat.id, response, reply_markup=get_reply_keyboard("History", "New Chat"))
