from telebot import TeleBot
from library_service import settings
from celery import shared_task
import time

BOT_TOKEN = settings.TG_BOT_TOKEN
CHAT_ID = settings.TG_CHAT_ID

bot = TeleBot(BOT_TOKEN)

@shared_task
def send_telegram_message_when_borrowing(message):
    time.sleep(60)
    bot.send_message(CHAT_ID, message)