from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    msg = f"Salom, {message.from_user.full_name}!\n"
    await message.answer(msg)
