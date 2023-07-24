from celery import shared_task
import time
import telebot
from library_service import settings


BOT_TOKEN = settings.TG_BOT_TOKEN
CHAT_ID = settings.TG_CHAT_ID


@shared_task
def send_telegram_message_when_borrowing(message):
    bot = telebot.TeleBot(BOT_TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)
