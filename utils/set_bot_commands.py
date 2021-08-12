from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("set_photo", "Guruh rasmini o'zgartirish"),
            types.BotCommand("set_title", "Guruh nomini o'zgartirish "),
            types.BotCommand("set_description", "Guruh haqidagi ma'lumotni o'zgatirish"),
            types.BotCommand("ro", "Foydalanuvchini Read Only (RO) rejimga o'tkazish"),
            types.BotCommand("unro", "RO rejimdan chiqarish"),
            types.BotCommand("ban", "Ban"),
            types.BotCommand("unban", "Bandan chiqarish"),
        ]
    )
