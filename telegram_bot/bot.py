from telebot import TeleBot
from library_service import settings

BOT_TOKEN = settings.TG_BOT_TOKEN
CHAT_ID = settings.TG_CHAT_ID

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.reply_to(message, "Bot has started!")


bot.polling()