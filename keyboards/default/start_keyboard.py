from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Bosh menyu"),
        ],
    ],
    resize_keyboard=True,
)
