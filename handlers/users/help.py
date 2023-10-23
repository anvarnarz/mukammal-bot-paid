from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from states.personal_date import Personal_data
from loader import dp


@dp.message_handler(CommandHelp(),state=Personal_data.fullname)
async def bot_help(message: types.Message):
    text = ("Iltimos ism familiya kiriting:")
    
    await message.answer("\n".join(text))