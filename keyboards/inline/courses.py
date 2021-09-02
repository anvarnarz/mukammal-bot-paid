from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup



aiogram_keys = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Kursni boshlash", url="https://mohirdev.uz/courses/telegram"),
        InlineKeyboardButton(text="Batafsil", callback_data="course:aiogram")
    ],
    [
        InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="kurs"),
    ],
])

python_keys = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Kursni boshlash", url="https://mohirdev.uz/courses/python"),
        InlineKeyboardButton(text="Batafsil", callback_data="course:python")
    ],
    [
        InlineKeyboardButton(text="✉️Ulashish", switch_inline_query="kurs"),
    ],
])