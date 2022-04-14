import logging

from aiogram import Bot, Dispatcher, types

import config

bot = Bot(token=config.TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

logging.basicConfig(format='%(filename)s [LINE:%(lineno)d] #%(Levelname)-8s 'u'[%(asctime)s] %(message)s',
					level=logging.INFO,
					)