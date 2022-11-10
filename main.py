from aiogram.utils import executor
from create_bot import dp
from handlers import client,  admin, others
from data_base import sqlite_db

async def on_startup(_):
    print('Включен')
    sqlite_db.sql_start()







client.register_handler_client(dp)
admin.register_handlers_admin(dp)
others.register_handler_others(dp)



if __name__ == "__main__":
        executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
