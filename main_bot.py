from aiogram import Bot, Dispatcher, types, executor
import logging
from Help_scripts import Settings_bot

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=Settings_bot.TOKEN)

dp = Dispatcher(bot)


@dp.message_handler(commands = 'hello')
async def hello(message : types.Message):
    await message.answer('Ghbs')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)