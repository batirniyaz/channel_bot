from bot.instance import bot as main_bot
import bot.handlers

if __name__ == "__main__":
    print('Bot is running...')
    main_bot.infinity_polling()
