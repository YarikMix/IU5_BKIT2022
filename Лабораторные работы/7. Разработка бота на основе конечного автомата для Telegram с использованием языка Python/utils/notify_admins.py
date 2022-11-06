import logging

from aiogram import Dispatcher

from config import ADMIN_ID


async def on_startup_notify(dp: Dispatcher):
	logging.info("Бот запущен")
	await dp.bot.send_message(chat_id=ADMIN_ID, text="Бот запущен")