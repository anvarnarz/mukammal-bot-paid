import io

from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsGroup
from filters.admins import AdminFilter
from loader import dp, bot


@dp.message_handler(IsGroup(), Command("set_photo", prefixes="!/"), AdminFilter())
async def set_new_photo(message: types.Message):
    source_message = message.reply_to_message
    photo = source_message.photo[-1]
    photo = await photo.download(destination=io.BytesIO())
    input_file = types.InputFile(photo)
    #1-usul
    await message.chat.set_photo(photo=input_file)


@dp.message_handler(IsGroup(), Command("set_title", prefixes="!/"), AdminFilter())
async def set_new_title(message: types.Message):
    source_message = message.reply_to_message
    title = source_message.text
    #2-usul
    await bot.set_chat_title(message.chat.id, title=title)



@dp.message_handler(IsGroup(), Command("set_description", prefixes="!/"), AdminFilter())
async def set_new_description(message: types.Message):
    source_message = message.reply_to_message
    description = source_message.text
    # 1-usul
    # await bot.set_chat_description(message.chat.id, description=description)
    # 2-usul
    await message.chat.set_description(description=description)

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
            if entity.type in ["url","text_link"]:
                await bot.delete_message(message.chat.id, message.message_id)
                await bot.send_message(message.chat.id, "Agar siz e'lonlaringiz bilan havolalar yubormoqchi bo'lsangiz, administrator @m_m_ahmadjon bilan bog'laning")

 
