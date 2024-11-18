from telebot import types

from .instance import bot
from .gemini_api import generate

from config import CHANNEL_ID

id_channel = '-100' + CHANNEL_ID


@bot.message_handler(commands=['start', 'help'])
def bot_start(message: types.Message):
    bot.reply_to(message, 'Hi, I was created by BatyaMoget. I am saying to him million thanks')


@bot.message_handler(is_admin=True, commands=['get_id'])
def get_id(message: types.Message):
    cid = message.chat.id
    mid = message.message_id
    fid = message.from_user.id
    bot.send_message(message.chat.id, '\n'.join([f'cid: {cid}', f'mid: {mid}', f'fid: {fid}']))


@bot.message_handler(is_admin=True, commands=['post'])
def handle_post(message: types.Message):
    bot.send_message(message.chat.id, 'Please write the topic of the post')
    bot.register_next_step_handler(message, foo)


@bot.message_handler(is_admin=True, chat_types=['private'])
def foo(message: types.Message):
    bot.send_message(message.chat.id, 'Seconds please... 🕒\tGenerating post... 🕒')
    generated_text = generate(message.text)
    bot.send_message(id_channel, generated_text, parse_mode='HTML')
    bot.send_message(message.chat.id, 'Post has been sent to the target channel')

