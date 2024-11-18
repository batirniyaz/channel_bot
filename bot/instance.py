import telebot
from config import TOKEN
from config import CHANNEL_ID

bot = telebot.TeleBot(TOKEN, threaded=False)


class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    key = 'is_admin'

    @staticmethod
    def check(message: telebot.types.Message):
        return bot.get_chat_member('-100' + CHANNEL_ID, message.from_user.id).status in ['administrator', 'creator']


bot.add_custom_filter(IsAdmin())
