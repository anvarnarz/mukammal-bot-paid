from aiogram.dispatcher.filters import AdminFilter
from loader import dp, bot
from aiogram import types

@dp.message_handler(content_types=["new_chat_members"]) #Зашел
async def on_user_joined(message: types.Message):
    await message.delete()


@dp.message_handler(content_types=["left_chat_member"]) #Вышел
async def on_user_exit(message: types.Message):
    await message.delete()

@dp.message_handler(content_types=['text'])
async def delete_links(message: types.Message):
    admins_list = [admin.user.id for admin in await bot.get_chat_administrators(chat_id=message.chat.id)]
    if message.from_user.id not in admins_list:

        if '@' in message.text: #Удаление сообщений с тегами (@тег)
            await bot.delete_message(message.chat.id, message.message_id)

        for entity in message.entities: #Удаление сообщений с ссылками
            if entity.type in ["url", "text_link"]:
                await bot.delete_message(message.chat.id, message.message_id)
                await bot.send_message(message.chat.id, "Agar siz e'lonlaringiz va havolalar yubormoqchi bo'lsangiz, administrator @m_m_ahmadjon bilan bog'laning")
