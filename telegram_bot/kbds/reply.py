from aiogram.types import ReplyKeyboardMarkup, KeyboardButton 


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