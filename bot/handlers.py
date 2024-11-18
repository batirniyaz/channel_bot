from telebot import types

from .instance import bot
from .gemini_api import generate


@bot.message_handler(commands=['start', 'help'])
def bot_start(message: types.Message):
    bot.reply_to(message, 'Hi, I was created by BatyaMoget. I am saying to him million thanks')


@bot.message_handler(commands=['get_id'])
def get_id(message: types.Message):
    cid = message.chat.id
    mid = message.message_id
    fid = message.from_user.id
    bot.send_message(message.chat.id, '\n'.join([f'cid: {cid}', f'mid: {mid}', f'fid: {fid}']))


@bot.message_handler(commands=['post'])
def handle_post(message: types.Message):
    bot.send_message(message.chat.id, 'Please write the topic of the post')
    bot.register_next_step_handler(message, foo)


@bot.message_handler(chat_types=['private'])
def foo(message: types.Message):
    bot.send_message(message.chat.id, 'Seconds please... \t 🕒Generating post... 🕒')
    # generated_text = generate(message.text)
    text = """
    Пример:
<pre>
name = "Batirniyaz"
age = 25
print(f"Привет, {name}! Тебе уже {age} лет.")
</pre>
    """
    bot.send_message(message.chat.id, text, parse_mode='HTML')

