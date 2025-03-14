import time
import telebot
import psycopg2

from dotenv import load_dotenv
from os import getenv

from User import User

# MINE PACKAGES
import handlers



load_dotenv()
bot = telebot.TeleBot(getenv("TG_BOT_TOKEN"))
users = {}

@bot.message_handler(commands=["start"])
def start(message):
    user = User()
    user.set_chat_id(message.chat.id)
    user.set_username(message.chat.username)
    users[message.chat.id] = user

    handlers.start(bot, user, message.text)

@bot.message_handler()
def other(message):
    if message.chat.id in users:
        handlers.other(bot, users[message.chat.id], message.text, message.message_id)


bot.infinity_polling()
