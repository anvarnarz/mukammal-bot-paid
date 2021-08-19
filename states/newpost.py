from aiogram.dispatcher.filters.state import StatesGroup, State


class NewPost(StatesGroup):
    NewMessage = State()
    Confirm = State()
