from loader import bot

async def on_shutdawn(dp):
	await bot.close()

if __name__ == '__main__':
	from aiogram import executor
	from handlers import dp

	executor.start_polling(dp)
	# executor.start_polling(dp, on_shutdawn=on_shutdawn)