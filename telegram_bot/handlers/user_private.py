from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command

from kbds import reply


greeter_text = """
	Здравствуйте!
	Вас приветствует виртуальный помощник парка Хаукастер.

	Преимущества:
	- Партнерские пункты предрейсового осмотра
	- Ежедневный вывод средств
	
	В данном канале Вы найдете ответы на все
	интересующие вопросы."""


user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
	await message.answer(greeter_text, reply_markup=reply.start_kb)


@user_private_router.message(Command('staff'))
async def staff_cmd(message: types.Message):
	await message.answer('text', reply_markup=reply.staff_kb)
	#await message.answer('Сообщения для сотрудников', reply_markup=reply.staff_kb)
	

