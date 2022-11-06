from aiogram import executor
from handlers import dp

from loader import bot, storage

from utils.notify_admins import on_startup_notify


async def on_startup(dp):
	await on_startup_notify(dp)

async def on_shutdown(dp):
	await bot.close()
	await storage.close()


if __name__ == '__main__':
	executor.start_polling(dp, on_startup=on_startup_notify, on_shutdown=on_shutdown)
