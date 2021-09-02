from aiogram import types
from data.courses_python import inline_results_python
from data.courses_telegram import inline_results_telegram
from loader import dp
from keyboards.inline.courses import aiogram_keys, python_keys


@dp.inline_handler(text="python")
async def empty_query(query: types.InlineQuery):
    await query.answer(inline_results_python)

@dp.inline_handler(text="telegram")
async def empty_query(query: types.InlineQuery):
    await query.answer(inline_results_telegram)


@dp.inline_handler(text="rasm")
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultPhoto(
                id="005",
                photo_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Telegram-bot.png",
                thumb_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Telegram-bot.png",
                caption="<b>Mukammal Telegram bot</b> kursi.",
                reply_markup=aiogram_keys
            ),
            types.InlineQueryResultPhoto(
                id="006",
                photo_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Anvar-aka-python.png",
                thumb_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Anvar-aka-python.png",
                caption="<b>Python Dasturlash Asoslari</b> kursi.",
                reply_markup=python_keys
            ),
            types.InlineQueryResultVideo(
                id="007",
                video_url="https://streamable.com/ryeff4",
                caption="Million dolarlik g'oya",
                description="Go'yalarning asl bahosi",
                title="Million 💲 g'oya ",
                thumb_url="https://i.imgur.com/bY2XasE.png",
                mime_type="video/mp4",  # video/mp4 yoki text/html
            ),
        ]
    )

@dp.inline_handler()
async def empty_query(query: types.InlineQuery):
    await query.answer(
        results=[
            types.InlineQueryResultArticle(
                id="kurs001",
                title="Dasturlash Asoslari. Python",
                input_message_content=types.InputTextMessageContent(
                    message_text="Dars uchun link: https://mohirdev.uz/courses/python",
                ),
                url="https://mohirdev.uz/courses/python",
                thumb_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Telegram-bot.png",
                description="Dasturlash asoslarini eng mashshur dasturlash tili - Pythonda o'rganamiz"
            ),
            types.InlineQueryResultArticle(
                id="kurs002",
                title="Mukammal Telegram Bot",
                input_message_content=types.InputTextMessageContent(
                    message_text="Dars uchun link: https://mohirdev.uz/courses/telegram",
                ),
                url="https://mohirdev.uz/courses/telegram",
                thumb_url="https://i1.wp.com/mohirdev.uz/wp-content/uploads/Anvar-aka-python.png",
                description="Python dasturlash tilida Mukammal telegram bot yozishni o'rganamiz"
            ),
            types.InlineQueryResultArticle(
                id="kurs003",
                title="Ma'lumotlar Tuzilmasi va Algoritmlar",
                input_message_content=types.InputTextMessageContent(
                    message_text="Dars uchun link: https://mohirdev.uz/courses/algoritmlar",
                ),
                url="https://mohirdev.uz/courses/algoritmlar",
                thumb_url="https://i0.wp.com/mohirdev.uz/wp-content/uploads/ALGORITMLAR.png",
                description="Har bir dasturchi bilishi muhim bo'lgan eng dolzarb kurs."
            ),
            types.InlineQueryResultArticle(
                id="kurs004",
                title="Python Django Web dasturlash",
                input_message_content=types.InputTextMessageContent(
                    message_text="Dars uchun link: https://mohirdev.uz/courses/django",
                ),
                url="https://mohirdev.uz/courses/django",
                thumb_url="https://i0.wp.com/mohirdev.uz/wp-content/uploads/photo1627374915.jpeg",
                description="Django frameworkida Web dasturlar yaratishni o'rganamiz"
            ),
        ],
    )