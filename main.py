from configs.config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from asyncio import run
from handlers import router
async def main():
    bot = Bot(token = BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await dp.start_polling(bot)
print("[LOG] Бот запущен")
run(main()) #запускает цикла событий (dp)