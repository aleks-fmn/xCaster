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


#del_start_kb = ReplyKeyboardRemove()
