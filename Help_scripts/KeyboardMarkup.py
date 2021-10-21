from Help_scripts import db
from aiogram import types
from main_bot import cd_like, cd_learn_more


def what_show(user_id, db2: db.BotDB):
    attractions = db2.get_like_attraction_from_user(user_id)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if len(attractions) > 0:

        buttons = ["Все достопримечательности", 'Мои достопримечательности']
        keyboard.add(*buttons)
    else:
        buttons = ["Все достопримечательности"]
        keyboard.add(*buttons)
    return keyboard


def what_datail(user_id, attractions_id, db2: db.BotDB):
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    if db2.is_user_like_attraction(user_id, attractions_id):
        buttons = [types.InlineKeyboardButton(text='❤', callback_data=cd_like.new(id_user=user_id,
                                                                                  id_attraction=attractions_id)),
                   types.InlineKeyboardButton(text='Узнать больше',
                                              callback_data=cd_learn_more.new(id_attraction=attractions_id)),
                   ]
        keyboard.add(*buttons)
    else:
        buttons = [types.InlineKeyboardButton(text='Узнать больше',
                                              callback_data=cd_learn_more.new(id_attraction=attractions_id))]
        keyboard.add(*buttons)
    return keyboard
