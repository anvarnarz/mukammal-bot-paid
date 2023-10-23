from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from loader import dp
from states.personal_date import Personal_data

@dp.message_handler(Command("anketa"))
async def enter_test(msg: types.Message):
    await msg.answer("toliq ismingizni kiriting:")
    await Personal_data.fullname.set()


@dp.message_handler(state=Personal_data.fullname)
async def answer_fullname(msg: types.Message, state: FSMContext):
    fullname = msg.text
    await state.update_data(
        {'name': fullname}
    )
    await msg.answer("email manzilingizni kiriting:")
    await Personal_data.next()
    # await Personal_data.email.set()



@dp.message_handler(state=Personal_data.email)
async def answer_email(msg: types.Message, state: FSMContext):
    email = msg.text

    await state.update_data(
        {'email': email}
    )

    await msg.answer("Telefon raqamingingizni kiriting:")
    await Personal_data.next()


@dp.message_handler(state=Personal_data.phonenum)
async def answer_phoneNum(msg: types.Message, state: FSMContext):
    phone = msg.text
    await state.update_data(
        {'phone': phone}
    )
    #Malumotlarni qayta o'qiymiz

    data = await state.get_data()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")

    message = f"""Quyidagi malumotlari qabul qilindi\n
Ismingiz:{name}
Emailingiz: {email}
Telefon: {phone}"""
    await msg.answer(message)
    await state.finish()
