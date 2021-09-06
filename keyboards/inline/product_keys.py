from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def build_keyboard(product):
    keys = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Xarid qilish", callback_data=f"product:{product}"),
        ],
    ])
    return keys