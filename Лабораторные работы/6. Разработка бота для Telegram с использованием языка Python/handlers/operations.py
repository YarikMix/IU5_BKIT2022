import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.choice_buttons import choice
from loader import dp

from utils.balance import getBalance, changeBalance

from config import ADMIN_ID


@dp.message_handler(commands=["start", "help"])
async def show_menu(message: Message):
    await message.answer(text="Сбербанк банкомат", reply_markup=choice)


@dp.callback_query_handler(text="get_balance")
async def get_balance(call: CallbackQuery):
    await call.message.answer(f"Ваш баланс: {getBalance()} рублей")


@dp.callback_query_handler(text="deposit_money")
async def on_deposit_money_pressed(call: CallbackQuery):
    await call.answer(cache_time=60)

    newBalance = getBalance() + 100
    changeBalance(newBalance)

    logging.info(f"Баланс пользователя {ADMIN_ID} увеличен на 100 рублей")
    logging.info(f"Текущий баланс пользователя {ADMIN_ID} составляет {getBalance()} рублей")
    await call.message.answer("Баланс пополнен на 100 рублей", reply_markup=choice)


@dp.callback_query_handler(text="derive_money")
async def on_derive_money_pressed(call: CallbackQuery):
    await call.answer(cache_time=60)

    newBalance = getBalance() - 100
    changeBalance(newBalance)

    logging.info(f"Баланс пользователя {ADMIN_ID} уменьшен на 100 рублей")
    logging.info(f"Текущий баланс пользователя {ADMIN_ID} составляет {getBalance()} рублей")
    await call.message.answer("Вы вывели 100 рублей", reply_markup=choice)


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    logging.info(f"Нажата кнопка выхода")

    # Ответим в окошке с уведомлением!
    await call.answer("Вы вышли", show_alert=True)

    # Отправляем пустую клавиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(reply_markup=None)
