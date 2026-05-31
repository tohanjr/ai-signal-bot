from telegram import Bot
import asyncio

from config import TELEGRAM_TOKEN, CHANNEL_ID

bot = Bot(token=TELEGRAM_TOKEN)

def send_signal(message):

    async def send():
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=message
        )

    asyncio.run(send())
