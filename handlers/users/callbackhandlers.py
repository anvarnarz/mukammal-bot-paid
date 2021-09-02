from aiogram.types import Message, CallbackQuery
from loader import dp, bot

@dp.callback_query_handler(text="course:aiogram")
async def aiogram_course_inf(call: CallbackQuery):
    msg = "Ushbu darsimizda siz barcha talablarga javob beradigan, zamonaviy Telegram bot yaratishni oʻrganasiz.\n\n"
    msg += "Darsimiz quyidagi mavzularni oʻz ichiga oladi:\n"
    msg += "✅ Telegram bilan ishlash uchun eng mukammal va doimiy yangilanib turuvchi aiogram moduli asosida bot yaratish\n"
    msg += "✅ Dasturiy taʼminot yaratish metodologiyasi\n"
    msg += "✅ Bot logikasi\n"
    msg += "✅ Bot uchun tayyor va qulay shablon\n"
    msg += "✅ Turli APIlar bilan bogʻlanish\n"
    msg += "✅ Pythondagi foydali paketlar bilan tanishish\n"
    msg += "✅ Botga tugmalar, menyular qoʻshish\n"
    msg += "✅ Foydlanuvchilar bilan ishlash\n"
    msg += "✅ Guruhlar va kanallarda ishlaydigan bot yaratish\n"
    msg += "✅ Maʼlumotlar bazasi (SQLite, PostgreSQL)\n"
    msg += "✅ Toʻlov tizimlari bilan ishlash\n"
    msg += "✅ Bot uchun Admin panel yaratish (Django)\n"
    msg += "✅ Botni Heroku, Amazon va boshqa istalgan serverga yuklash\n"
    await bot.send_message(chat_id=call.from_user.id, text=msg)
    # await call.answer(msg)
    await call.answer(cache_time=60)