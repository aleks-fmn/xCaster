""""
Filename: reply.py
-----------------------------------------------------------------------

Этот файл выполняет построение клавиатур используемых в работе бота.
"""


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove 
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
	# согласно документации клавиатуру дложна быть списком из списов.
	keyboard = [
		[
			KeyboardButton(text='Для сотрудников'),
			KeyboardButton(text='Стать сотрудником парка')
        ],
        [
			KeyboardButton(text='ТОП 10 водителей'),
			KeyboardButton(text='Часто задаваемые вопросы')
        ]
	],
    resize_keyboard=True
)

staff_kb = ReplyKeyboardMarkup(
	# keyboard = [
	# 	[KeyboardButton(text='Пункты предрейсового осмотра')],
	# 	[KeyboardButton(text='Требования оклейки автомобиля')],
    #     [KeyboardButton(text='Контакты парка')],
	# 	[KeyboardButton(text='Заказать расчет')]
	# ],
    keyboard = [
		[KeyboardButton(text='Пункты предрейсового осмотра')],
        [KeyboardButton(text='Требования оклейки автомобиля')],
        [KeyboardButton(text='Контакты парка')],
        [KeyboardButton(text='Заказать расчет')]
	],
    resize_keyboard=True
)

req_driver_kb = ReplyKeyboardMarkup(
    keyboard = [
		[KeyboardButton(text='Требования к водителю для вступления в реестр')],
        [KeyboardButton(text='На главную')]
	],
    resize_keyboard=True
)

req_car_kb = ReplyKeyboardMarkup(
    keyboard = [
		[KeyboardButton(text='Требования к автомобилю для вступления в реестр')],
        [KeyboardButton(text='Подать документы')],
        [KeyboardButton(text='На главную')]
	],
    resize_keyboard=True
)

send_doc_kb = ReplyKeyboardMarkup(
    keyboard = [
		[KeyboardButton(text='Подать документы')],
        [KeyboardButton(text='На главную')]
	],
    resize_keyboard=True
)

to_main_kb = ReplyKeyboardMarkup(
    keyboard = [
		[KeyboardButton(text='На главную')]
	],
    resize_keyboard=True
)

#del_start_kb = ReplyKeyboardRemove()
