import aiogram.utils.markdown as md
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ContentType

from loader import dp

from states.form import Form


@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await Form.name.set()

    await message.answer(text="Привет! Давай знакомится, как тебя зовут?")


@dp.message_handler(state=Form.name)
async def process_deposit_money(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await Form.next()

    await message.answer("Сколько тебе лет?")


@dp.message_handler(state=Form.age)
async def on_derive_money_pressed(message: Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await Form.next()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Я парень", "Я девушка")

    await message.reply("Теперь определимся с полом", reply_markup=markup)


@dp.message_handler(state=Form.gender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['gender'] = message.text

    types.ReplyKeyboardRemove()

    await Form.next()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    markup.add("Парни", "Девушки")

    await message.answer("Кто тебе интересен?", reply_markup=markup)


@dp.message_handler(state=Form.interestGender)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['interestGender'] = message.text

    markup = types.ReplyKeyboardRemove()

    await Form.next()

    await message.answer("Из какого ты города?", reply_markup=markup)


@dp.message_handler(state=Form.city)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text

    await Form.next()

    await message.answer("Расскажите о себе")


@dp.message_handler(state=Form.description)
async def process_gender(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text

    await Form.next()

    await message.answer("Теперь пришли своё фото")


@dp.message_handler(content_types=ContentType.PHOTO, state=Form.photo)
async def send_photo_file_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo_id'] = message.photo[-1].file_id

    await message.answer_photo(
        photo=data['photo_id'],
        caption=md.text(
            md.text('Так выглядит твоя анкета:'),
            md.text(""),
            md.text(data['name'] + ", " + data['age'] + ", " + data['city']),
            md.text(data['description']),
            sep='\n',
        )
    )

    await state.finish()