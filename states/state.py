from aiogram.dispatcher.filters.state import StatesGroup, State

# Simple state
class Registration(StatesGroup):
    fullName = State() # ism
    email = State() # email
    phoneNum = State() # Tel raqami
