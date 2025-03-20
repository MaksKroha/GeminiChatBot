from keyboard import telebot


# Creates a custom reply keyboard for Telegram
# with the provided arguments as buttons.
# Configures the keyboard to resize dynamically
# and remain visible after use. Returns the
# configured keyboard markup for use in messages.
def get_reply_keyboard(*args):
    keyboard_markup = telebot.types.ReplyKeyboardMarkup(
        one_time_keyboard=False,
        resize_keyboard=True
    )
    for arg in args:
        keyboard_markup.add(arg)
    return keyboard_markup