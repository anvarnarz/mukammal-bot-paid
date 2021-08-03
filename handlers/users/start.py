from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.startKeyboard import menuStart

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\n")
    await message.answer("Telefoningiz va Manzilingizni yuboring", reply_markup=menuStart)
