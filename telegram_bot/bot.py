from telegram import Bot
from library_service import settings

async def send_telegram_notification(message):
    bot = Bot(token=settings.TG_BOT_TOKEN)
    await bot.send_message(chat_id=settings.TG_CHAT_ID, text=message)