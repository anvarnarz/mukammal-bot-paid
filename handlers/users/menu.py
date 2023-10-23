from aiogram.dispatcher.filters import Command,Text
from aiogram.types import Message, ReplyKeyboardMarkup,ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.pythonKeyboard import menuPython
from loader import dp

@dp.message_handler(Command('menu'))
async def show_menu(msg: Message):
    await msg.answer("kurslarni tanlang", reply_markup=menu)

@dp.message_handler(text = "Telegram bot")
async def send_link(msg: Message):
    await msg.answer("Mukammal Telegram bot kursia xush kelipsiz!")

@dp.message_handler(text = "Python")
async def send_link(msg: Message):
    await msg.answer("mavzu tanlang", reply_markup=menuPython)

@dp.message_handler(text = "#00 Kirish")
async def send_picture(msg: Message):
    await msg.answer_photo("https://plus.unsplash.com/premium_photo-1695762436978-070e000dff53?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8cGhvdHxlbnwwfHwwfHx8MA%3D%3D&w=1000&q=80", reply_markup=ReplyKeyboardRemove())

@dp.message_handler(text = "Boshiga")
async def send_link(msg: Message):
    await msg.answer("Kurslarni tanlang",reply_markup=menu)
