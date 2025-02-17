import telebot
from google import genai
import json

# MAIN VARIABLES
json_data = None
bot = None
client = None

with open("package.json", "r") as jsonfile:
    json_data = json.load(jsonfile)

bot = telebot.TeleBot(json_data["telegram_bot_token"])
client = genai.Client(api_key=json_data["gemini_api_key"])


@bot.message_handler(commands=["hello"])
def helloCommand(msg):
    bot.send_message(msg.chat.id, "Hello")


@bot.message_handler()
def getResponseFromGemini(msg):
    response = client.models.generate_content(model="gemini-2.0-flash",
                                              contents=f"{msg.json['text']}")
    bot.send_message(msg.chat.id, response.text)


bot.infinity_polling()
