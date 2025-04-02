import asyncio
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import os

load_dotenv()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message()
async def ping(message: types.Message) -> None:
    await bot.send_message(message.from_user.id, "tuk-tuk")

async def main():
    await dp.start_polling(bot)


asyncio.run(main())    
