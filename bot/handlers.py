from .instance import bot
from telebot import types


@bot.message_handler(commands=['start', 'help'])
def bot_start(message: types.Message):
    bot.reply_to(message, 'Hi, I was created by BatyaMoget. I am saying to him million thanks')

