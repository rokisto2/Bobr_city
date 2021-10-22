from aiogram import Bot, Dispatcher, types, executor
import logging

from aiogram.types import InputMediaPhoto
from aiogram.utils.callback_data import CallbackData

from Help_scripts import Settings_bot
from Help_scripts.db import BotDB
from Help_scripts import KeyboardMarkup

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=Settings_bot.TOKEN)

dp = Dispatcher(bot)

db = BotDB()

cd_like = CallbackData('user', 'id_user', 'id_attraction')
cd_learn_more = CallbackData('attraction', 'id_attraction')


@dp.message_handler(commands='start')
async def hello(message: types.Message):
    if db.user_exists(message.from_user.id):
        db.user_add(message.from_user.id)
        await message.answer('Добро пожаловать')
    else:
        await message.answer('Рады вас вновь встретить')
    keyboard = KeyboardMarkup.what_show(user_id=message.from_user.id, db2=db)
    await message.answer('Что показать', reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'Все достопримечательности')
async def get_all_attractions(message: types.Message):
    attractions = db.get_all_attractions()
    for attraction in attractions:
        await bot.send_photo(message.chat.id, db.get_attraction_img(attraction[0])[0][0],
                             caption=attraction[1] + '\n' + attraction[2],
                             reply_markup=KeyboardMarkup.what_datail(message.from_user.id, attraction[0], db))


@dp.message_handler(lambda message: message.text == 'Мои достопримечательности')
async def get_all_attractions(message: types.Message):
    attractions = db.get_like_attraction_from_user(message.from_user.id)

    for attraction in attractions:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        buttons = [
            types.InlineKeyboardButton(text='Узнать больше',
                                       callback_data=cd_learn_more.new(id_attraction=attraction[0]))
        ]
        keyboard.add(*buttons)
        await bot.send_photo(message.chat.id, db.get_attraction_img(attraction[0])[0][0],
                             caption=attraction[1] + '\n' + attraction[2],
                             reply_markup=keyboard)


@dp.callback_query_handler(cd_learn_more.filter())
async def callback_learn_more(call: types.CallbackQuery, callback_data: dict):
    id_attraction = callback_data['id_attraction']
    attraction = db.get_attraction(id_attraction)
    attraction_img = db.get_attraction_img(id_attraction)
    if len(attraction_img) == 1:
        await bot.send_photo(call.message.chat.id, attraction_img[0][0])
    else:
        media = [InputMediaPhoto(attraction_img[0][0], attraction[1] + '\n' + attraction[2])]
        for i in attraction_img[1:]:
            media.append(InputMediaPhoto(i[0]))
        await bot.send_media_group(call.message.chat.id, media=media)
    # keyboard = types.InlineKeyboardMarkup(row_width=1)
    # id_user = call.from_user.id
    # buttons = [
    #     types.InlineKeyboardButton(text='❤', callback_data=cd_like.new(id_user=id_user,
    #                                                                    id_attraction=attraction[0]))
    # ]
    # keyboard.add(*buttons)
    await bot.send_message(call.message.chat.id, attraction[3])
    await bot.send_location(call.message.chat.id, latitude=attraction[4], longitude=attraction[5])


@dp.callback_query_handler(cd_like.filter())
async def callback_like(call: types.CallbackQuery, callback_data: dict):
    id_attraction = callback_data['id_attraction']
    id_user = callback_data['id_user']
    print(id_user,id_attraction)
    db.add_attraction_from_user(user_id=id_user, attraction_id=id_attraction)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Все достопримечательности", 'Мои достопримечательности']
    keyboard.add(*buttons)
    await bot.send_message(call.message.chat.id, "Достопримечательность добавлена", reply_markup = keyboard )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
