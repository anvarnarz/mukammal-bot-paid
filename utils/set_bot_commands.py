from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Botni ishga tushurish"),
            types.BotCommand("help", "Yordam"),
            types.BotCommand("kitob", "Python kitobini xarid qilish"),
            types.BotCommand("praktikum", "Data Science praktikum xarid qilish"),
            types.BotCommand("mahsulotlar", "Barcha mahsulotlarni ko'rish"),
        ]
    )
