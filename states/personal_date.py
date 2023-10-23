from aiogram.dispatcher.filters.state import StatesGroup, State

class Personal_data(StatesGroup):
    fullname = State()
    email = State()
    phonenum = State()