import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import load_dotenv
import os

from handlers.user_private import user_private_router


# Разрешенные типы обновлений (https://core.telegram.org/bots/api#update)
ALLOWED_UPDATES = ['message', 'edited_message']


load_dotenv()

bot = Bot(token=os.getenv('TOKEN'), 
          default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()


# @dp.message()
# async def ping(message: types.Message):
#     await bot.send_message(message.from_user.id, "tuk-tuk")

dp.include_router(user_private_router)

async def main():
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())    
