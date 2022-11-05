import logging

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message, CallbackQuery

from keyboards.choice_buttons import choice
from loader import dp

from utils.balance import getBalance, changeBalance

from config import ADMIN_ID


# States
class Form(StatesGroup):
    deposit_money = State()
    derived_money = State()


@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer(text="Сбербанк банкомат", reply_markup=choice)


@dp.message_handler(Command("help"))
async def show_menu(message: Message):
    await message.answer(text="Сбербанк банкомат", reply_markup=choice)


@dp.callback_query_handler(text="get_balance")
async def get_balance(call: CallbackQuery):
    await call.message.answer(f"Ваш баланс: {getBalance()} рублей")


@dp.callback_query_handler(text="deposit_money")
async def on_deposit_money_pressed(call: CallbackQuery):
    await call.answer(cache_time=60)

    await Form.deposit_money.set()

    await call.message.answer("Пожалуйста введите размер суммы для пополнения")


# Проверка на число
@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.deposit_money)
async def process_age_invalid(message: Message):
    return await message.reply("Пожалуйста введите число!\n")


@dp.message_handler(state=Form.deposit_money)
async def process_deposit_money(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["input_deposit"] = message.text

    oldBalance = getBalance()
    newBalance = oldBalance + int(message.text)
    changeBalance(newBalance)

    await state.finish()

    logging.info(f"Баланс пользователя {ADMIN_ID} увеличен на {message.text} рублей")
    logging.info(f"Текущий баланс пользователя {ADMIN_ID} составляет {getBalance()} рублей")
    await message.reply(f"Баланс пополнен на {message.text} рублей", reply_markup=choice)


@dp.callback_query_handler(text="derive_money")
async def on_derive_money_pressed(call: CallbackQuery):
    await call.answer(cache_time=60)

    await Form.derived_money.set()

    await call.message.answer("Пожалуйста введите размер суммы для вывода")


# Проверка на число
@dp.message_handler(lambda message: not message.text.isdigit(), state=Form.derived_money)
async def process_age_invalid(message: Message):
    return await message.reply("Пожалуйста введите число!\n")

# Размер суммы для вывода должен быть не меньше текущего баланса
@dp.message_handler(lambda message: message.text.isdigit() and int(message.text) > getBalance(), state=Form.derived_money)
async def process_age_invalid(message: Message):
    return await message.reply("Недостаточно средств для вывода!\n")


@dp.message_handler(state=Form.derived_money)
async def process_derived_money(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data["input_derived"] = message.text

    oldBalance = getBalance()
    newBalance = oldBalance - int(message.text)
    changeBalance(newBalance)

    await state.finish()

    logging.info(f"Баланс пользователя {ADMIN_ID} уменьшен на {message.text} рублей")
    logging.info(f"Текущий баланс пользователя {ADMIN_ID} составляет {getBalance()} рублей")
    await message.reply(f"Вы вывели {message.text} рублей", reply_markup=choice)


@dp.callback_query_handler(state="*", text="cancel")
async def cancel_buying(call: CallbackQuery, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()

    logging.info(f"Нажата кнопка выхода")

    # Ответим в окошке с уведомлением!
    await call.answer("Вы вышли", show_alert=True)

    # Отправляем пустую клавиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(reply_markup=None)
