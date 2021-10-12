from aiogram import Bot, Dispatcher, types, executor
import logging
from Help_scripts import Settings_bot
from Help_scripts.db import BotDB

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=Settings_bot.TOKEN)

dp = Dispatcher(bot)

db = BotDB()


@dp.message_handler(commands = 'start')
async def hello(message : types.Message):
    if db.user_exists(message.from_user.id):
        db.user_add(message.from_user.id)
        await message.answer('Добро пожаловать')
    else:
        await message.answer('Рады вас вновь встретить')


@dp.message_handler(commands = 'exit')
async def close(message : types.Message):
    db.close()




if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=False)
