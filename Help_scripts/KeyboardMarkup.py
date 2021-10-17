from Help_scripts import db
from aiogram import types


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
