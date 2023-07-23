from telebot import TeleBot
from library_service import settings

BOT_TOKEN = settings.TG_BOT_TOKEN
CHAT_ID = settings.TG_CHAT_ID

bot = TeleBot(BOT_TOKEN)


def send_telegram_message_when_borrowing(message):

    bot.send_message(CHAT_ID, message)