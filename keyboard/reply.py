from keyboard import telebot


def get_reply_keyboard(*args):
    keyboard_markup = telebot.types.ReplyKeyboardMarkup(
        one_time_keyboard=False,
        resize_keyboard=True
    )
    for arg in args:
        keyboard_markup.add(arg)
    return keyboard_markup