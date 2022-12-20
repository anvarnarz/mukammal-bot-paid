import logging

from aiogram import Dispatcher

async def on_startup_notify(dp: Dispatcher):
    print("Bot ishga tushdi")
