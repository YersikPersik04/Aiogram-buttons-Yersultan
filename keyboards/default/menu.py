from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="models")
		],
		[
			KeyboardButton(text="Car parts"),
			KeyboardButton(text="resycle bin")
		],
	],
	resize_keyboard=True
)