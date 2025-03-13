def clear(bot, chat_id, min_msg_id, max_msg_id):
    try:
        while max_msg_id >= min_msg_id:
            bot.delete_message(chat_id, max_msg_id)
            max_msg_id -= 1
    except Exception:
        clear(bot, chat_id, min_msg_id, max_msg_id - 1)