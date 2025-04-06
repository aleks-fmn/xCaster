from aiogram import F, types, Router
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_line, as_list, as_marked_section, Bold 


from kbds import reply


greeter_text = """
	Здравствуйте!
	Вас приветствует виртуальный помощник парка Хаукастер.

	Преимущества:
	- Партнерские пункты предрейсового осмотра
	- Ежедневный вывод средств
	
	В данном канале Вы найдете ответы на все
	интересующие вопросы."""

undef_behavior_text = """С удовольствием поговорил бы с Вами на отвелеченные темы
	Но мой создатель ограничиил мою свободу определенными командами."""

user_private_router = Router()

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
	await message.answer(greeter_text, reply_markup=reply.start_kb)


@user_private_router.message(or_f(Command('get_contact'), 
								  F.text.lower().contains('контакты парка')))
async def get_contact(message: types.Message):
	text = as_marked_section(
		Bold("Контакты:"),
		"Телефон: +375293305566",
		"Email: haukaster@yandex.ru",
		"Подробнее: https://haukaster.by",
		marker="  ",
	)
	await message.answer(text.as_html(), reply_markup=reply.to_main_kb)


@user_private_router.message(or_f(Command('requirements_to_car'), 
								  F.text.lower().contains('требования оклейки автомобиля')))
async def get_contact(message: types.Message):
	await message.answer_photo(
		photo=types.FSInputFile(path='./media/taxi_white.jpg'), 
		caption='Белый',
		show_caption_above_media=True
	)
	await message.answer_photo(
		photo=types.FSInputFile(path='./media/taxi_yellow.jpg'), 
		caption='Желтый', 
		show_caption_above_media=True
	)
	await message.answer_photo(
		photo=types.FSInputFile(path='./media/taxi_black.jpg'), 
		caption='Черный', 
		show_caption_above_media=True,
		reply_markup=reply.to_main_kb
	)


@user_private_router.message(or_f(Command('pretrip_inspection'), 
								  F.text.lower().contains('Пункты предрейсового осмотра')))
async def pretrip_inspection(message: types.Message):
	await message.answer('pretrip_inspection point', reply_markup=reply.to_main_kb)


@user_private_router.message(or_f(Command('staff'), F.text.lower().contains('для сотрудников')))
async def staff_cmd(message: types.Message):
	await message.answer('text', reply_markup=reply.staff_kb)


@user_private_router.message(or_f(Command('to_main'), 
								  F.text.lower().contains('на главную')))
async def to_main_cmd(message: types.Message):
	await message.answer('На главную', reply_markup=reply.start_kb)


@user_private_router.message(F.text)
async def invalid_cmd(message: types.Message):
	await message.answer(undef_behavior_text)


	

