# Clears a range of messages in a Telegram chat.
# Deletes messages sequentially from the highest
# message ID to the lowest. If an error occurs
# (e.g., message not found), it retries by skipping
# the problematic message. This function ensures
# all messages within the specified range are
# attempted for deletion.
def clear(bot, chat_id, min_msg_id, max_msg_id):
    try:
        while max_msg_id >= min_msg_id:
            bot.delete_message(chat_id, max_msg_id)
            max_msg_id -= 1
    except Exception:
        clear(bot, chat_id, min_msg_id, max_msg_id - 1)