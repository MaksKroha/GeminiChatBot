# Setting settings for logining file
import logging
logging.basicConfig(
    filename='bot.log',
    level=logging.INFO,
    format='[%(asctime)s] %(levelname)s %(filename)s:%(lineno)d (%(funcName)s) - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


import telebot
from exception import log_exception
from User import User
import handlers

# Reading from .env file
from dotenv import load_dotenv
from os import getenv
load_dotenv()
bot = telebot.TeleBot(getenv("TG_BOT_TOKEN"))
users = {}



@bot.message_handler(commands=["start"])
def start(message):
    try:
        user = User()
        user.set_chat_id(message.chat.id)
        user.set_username(message.chat.username)
        users[message.chat.id] = user

        handlers.start(bot, user)
    except Exception as e:
        log_exception(str(e))


@bot.message_handler()
def other(message):
    try:
        if message.chat.id in users:
            handlers.other(bot, users[message.chat.id], message.text, message.message_id)
    except Exception as e:
        log_exception(str(e))

bot.infinity_polling()
