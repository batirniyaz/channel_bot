from .instance import bot
from telebot import types


@bot.message_handler(commands=['start', 'help'])
def bot_start(message: types.Message):
    bot.reply_to(message, 'Hi, I was created by BatyaMoget. I am saying to him million thanks')


@bot.message_handler(commands=['get_id'])
def get_id(message: types.Message):
    cid = message.chat.id
    mid = message.message_id
    fid = message.from_user.id
    bot.send_message(message.chat.id, '\n'.join([f'cid: {cid}', f'mid: {mid}', f'fid: {fid}']))

