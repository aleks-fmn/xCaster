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


@user_private_router.message(or_f(Command('check_car'), 
								  F.text.lower().contains('пункты предрейсового осмотра')))
async def check_car(message: types.Message):
	text = as_list(
		as_marked_section(
			Bold("1. Проверка документов:"),
			"Наличие водительского удостоверения;",
			"Действие страхового полиса ОСАГО/КАСКО;",
			"Путевой лист (если требуется);",
			"Технический паспорт транспортного средства.",
			marker="- "
		),
		as_marked_section(
			Bold("2. Внешний осмотр кузова:"),
			"Проверка целостности лакокрасочного покрытия;",
			"Отсутствие видимых повреждений (вмятины, царапины, трещины);",
			"Исправность зеркал заднего вида;",
			"Состояние номерных знаков (читаемость, крепление).",
			marker="- "
		),
		as_marked_section(
			Bold("3. Осмотр шин:"),
			"Давление воздуха в шинах должно соответствовать норме;",
			"Глубина протектора шин должна быть достаточной (не менее 1,6 мм для легковых автомобилей);",
			"Осмотреть шины на наличие порезов, трещин, вздутий.",
			marker="- "
		),
		as_marked_section(
			Bold("4. Ремни безопасности:"),
			"Ремни безопасности должны быть натянуты, не иметь повреждений и правильно фиксироваться;",
			"Пряжки ремней должны защелкиваться и расстегиваться без проблем.",
			marker="- "
		),
		as_marked_section(
			Bold("5. Тормоза:"),
			"Педаль тормоза должна нажиматься плавно, без провалов и рывков;",
			"Рабочая тормозная система должна обеспечивать эффективное торможение;",
			"Стояночный тормоз должен надежно удерживать автомобиль на месте.",
			marker="- "
		),
		sep='\n\n'
	)
	await message.answer(text.as_html(), reply_markup=reply.to_main_kb)


@user_private_router.message(or_f(Command('pretrip_inspection'), 
								  F.text.lower().contains('Пункты предрейсового осмотра')))
async def pretrip_inspection(message: types.Message):
	await message.answer('pretrip_inspection point', reply_markup=reply.to_main_kb)


@user_private_router.message(or_f(Command('staff'), F.text.lower().contains('для сотрудников')))
async def staff_cmd(message: types.Message):
	await message.answer('text', reply_markup=reply.staff_kb)


@user_private_router.message(or_f(Command('became_staff'), F.text.lower().contains('стать сотрудником парка')))
async def became_staff(message: types.Message):
	await message.answer_document(
		document=types.FSInputFile(path='./docs/Документ_1.pdf'),
		thumbnail=types.FSInputFile(path='./media/icon_pdf.png'),
		reply_markup=reply.req_driver_kb
	)


@user_private_router.message(or_f(Command('req_to_driver'), F.text.lower().contains('требования к водителю')))
async def req_to_driver(message: types.Message):
		await message.answer_document(
			document=types.FSInputFile(path='./docs/Документ_3.pdf'),
			thumbnail=types.FSInputFile(path='./media/icon_pdf.png'),
			reply_markup=reply.req_car_kb
	)
		

@user_private_router.message(or_f(Command('req_to_car'), F.text.lower().contains('требования к автомобилю')))
async def req_to_car(message: types.Message):
		await message.answer_document(
			document=types.FSInputFile(path='./docs/Документ_2.pdf'),
			thumbnail=types.FSInputFile(path='./media/icon_pdf.png'),
			reply_markup=reply.send_doc_kb
	)


@user_private_router.message(or_f(Command('send_doc'), F.text.lower().contains('подать документы')))
async def req_to_car(message: types.Message):
		url='https://docs.google.com/forms/d/e/1FAIpQLScJmxv4_XLsubBBk75IN1QPvW3jhqVJ9KGzvuQAw2njRPivqg/viewform?usp=header'
		await message.answer(url, reply_markup=reply.send_doc_kb)


@user_private_router.message(or_f(Command('to_main'), 
								  F.text.lower().contains('на главную')))
async def to_main_cmd(message: types.Message):
	await message.answer('На главную', reply_markup=reply.start_kb)


@user_private_router.message(F.text)
async def invalid_cmd(message: types.Message):
	await message.answer(undef_behavior_text)


	

