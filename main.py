import time
import telebot
import psycopg2

from dotenv import load_dotenv
from os import getenv

# MINE PACKAGES
import handlers



load_dotenv()
bot = telebot.TeleBot(getenv("TG_BOT_TOKEN"))


@bot.message_handler(commands=["start"])
def start(message):
    handlers.start(bot, message)

@bot.message_handler()
def other(message):
    handlers.other(bot, message)


bot.infinity_polling()
