from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from keyboards.default.contact_button import keyboard
from loader import dp


@dp.callback_query_handler(text="mycontact")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="Kontakt yuboring:", reply_markup=keyboard)

@dp.message_handler(content_types='contact')
async def get_contact(message: Message):
    contact = message.contact
    await message.answer(f"Rahmat, <b>{contact.full_name}</b>.\n"
                         f"Sizning {contact.phone_number} raqamingizni qabul qildik.\nAdminmiz siz bilan bog'lanadi.",
                         reply_markup=ReplyKeyboardRemove())
