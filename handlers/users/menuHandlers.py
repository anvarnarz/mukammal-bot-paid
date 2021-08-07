import logging

from aiogram.types import Message, CallbackQuery
from keyboards.inline.callback_data import course_callback, book_callback
from keyboards.inline.productsKeyboard import categoryMenu, coursesMenu, booksMenu, telegram_keyboard, algoritm_keyboard
from loader import dp


@dp.message_handler(text_contains="Mahsulotlar")
async def select_category(message: Message):
    logging.info(message)
    logging.info(f"{message.from_user.username=}")
    logging.info(f"{message.from_user.full_name=}")

    await message.answer(f"Mahsulot tanlang", reply_markup=categoryMenu)

@dp.callback_query_handler(text="courses")
async def buy_courses(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    logging.info(f"{call.from_user.username=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.delete()
    await call.message.answer("Kurs tanlang", reply_markup=coursesMenu)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text_contains="books")
async def buy_books(call: CallbackQuery):
    callback_data = call.data
    logging.info(f"{callback_data=}")
    # await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer("Kitoblar", reply_markup=booksMenu)
    await call.message.delete()
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    # Oynada javob qaytaramiz

    await call.message.edit_reply_markup(reply_markup=categoryMenu)
    await call.answer()

# CallbackData yordamid filtrlash
@dp.callback_query_handler(course_callback.filter(item_name="telegram"))
async def buying_course(call: CallbackQuery, callback_data: dict):

    # logging yordamida foydalanuvchidan qaytgan callback ni ko'ramiz
    logging.info(f"{callback_data=}")

    await call.message.answer(f"Siz Mukammal Telegram Bot Kursini tanladingiz.",
                              reply_markup=telegram_keyboard)

    await call.answer(cache_time=60)

@dp.callback_query_handler(book_callback.filter(item_name="python_book"))
async def buying_book(call: CallbackQuery, callback_data: dict):
    logging.info(f"{callback_data=}")
    await call.answer("Buyurtmangiz qabul qilindi", cache_time=60, show_alert=True)