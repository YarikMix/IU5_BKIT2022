from aiogram.dispatcher.filters.state import State, StatesGroup

class Form(StatesGroup):
    deposit_money = State()
    derived_money = State()
