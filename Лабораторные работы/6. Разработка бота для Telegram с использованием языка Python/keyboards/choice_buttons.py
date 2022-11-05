from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


choice = InlineKeyboardMarkup(row_width=2)

get_balance = InlineKeyboardButton(text="Узнать баланс", callback_data="get_balance")
choice.insert(get_balance)

deposit_money = InlineKeyboardButton(text="Пополнить счёт", callback_data="deposit_money")
choice.insert(deposit_money)

derive_money = InlineKeyboardButton(text="Снять наличные", callback_data="derive_money")
choice.insert(derive_money)

cancel_button = InlineKeyboardButton(text="Выход", callback_data="cancel")
choice.insert(cancel_button)

