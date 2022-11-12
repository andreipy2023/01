from aiogram import types, Dispatcher
from create_bot import bot
from keyboards import kb_client
from data_base import sqlite_db


#@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id,'Привет, рад знакомству держи картинку', reply_markup=kb_client)
    await bot.send_photo(message.from_user.id, open('cat.jpg', 'rb'))

#@dp.message_handler(commands=['Режим_работы'])
async def rejim(message: types.Message):
    await bot.send_message(message.from_user.id, '3424242  444', reply_markup=kb_client)

#@dp.message_handler(commands=["location"])
async def location(message: types.Message):
    await bot.send_message(message.from_user.id, '3424242', reply_markup=kb_client)


# @dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)



def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(rejim, commands=['Режим_работы'])
    dp.register_message_handler(location, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])



