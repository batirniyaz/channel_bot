import telebot
from config import TOKEN
from .filter import IsAdmin

bot = telebot.TeleBot(TOKEN, threaded=False)

bot.add_custom_filter(IsAdmin())
