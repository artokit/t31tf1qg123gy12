import asyncio
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from routers import admin, user, sender

TOKEN = '7147216330:AAHp8shpZaq5Wdm3MHX1ZtqD1ih_TA0QKNM'
bot = Bot(TOKEN)

dp = Dispatcher(storage=MemoryStorage())
dp.include_routers(user.router, admin.router)
sender.set_bot(dp, bot)
sender.init_handlers()
asyncio.run(dp.start_polling(bot))
