import telebot
from config import ADMIN_ID


class IsAdmin(telebot.custom_filters.SimpleCustomFilter):
    key = 'is_admin'

    @staticmethod
    def check(message: telebot.types.Message):
        return message.from_user.id == ADMIN_ID
