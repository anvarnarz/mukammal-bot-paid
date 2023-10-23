from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPython = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="#00 Kirish"),
            KeyboardButton(text="#01 Kerakli Dasturlar"),
            KeyboardButton(text="#02 Hello World!"),

        ],
        # O'rtga qaytish uchun button
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga"),

        ],
    ],
    resize_keyboard=True
)