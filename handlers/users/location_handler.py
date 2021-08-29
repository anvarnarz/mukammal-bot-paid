from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove

from keyboards.default.location_button import keyboard
from utils.misc.get_distance import choose_shortest
from loader import dp


@dp.callback_query_handler(text="mylocation")
async def show_contact_keys(call: CallbackQuery):
    await call.message.answer(text="Lokasiya yuboring:", reply_markup=keyboard)

@dp.message_handler(content_types='location')
async def get_contact(message: Message):
    location = message.location
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortest(location)

    text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\n Masofa: {distance:.1f} km."
                        for shop_name, distance, url, shop_location in closest_shops])

    await message.answer(f"Rahmat. \n"
                         f"Latitude = {latitude}\n"
                         f"Longitude = {longitude}\n\n"
                         f"{text}", disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())

    for shop_name, distance, url, shop_location in closest_shops:
        await message.answer_location(latitude=shop_location["lat"],
                                      longitude=shop_location["lon"])
