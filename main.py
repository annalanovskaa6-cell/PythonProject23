# import config
# config.BOT_TOKEN
from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from asyncio import run
from requests import get
async def main():
    bot = Bot(token = BOT_TOKEN)
    dp = Dispatcher()
    # https://catfact.ninja/fact
    @dp.message(Command(commands = ['catfact']))
    async def get_cat_fact(message: Message):
        print(f"[LOG] пользователь {message.from_user.id} нажал команду /catfact")
        print(f"[LOG] запрашиваю факт о котах")
        response = get("https://catfact.ninja/fact")
        print(f"[LOG] Получен результат со статусом {response.status_code}")
        response_json = response.json()
        print(response_json["fact"])
        await message.answer(response_json["fact"])
    @dp.message(Command(commands=['start']))
    async def start_handler(message: Message):
        print(f"[LOG] пользователь {message.from_user.id} нажал кнопку /start")
        await message.answer(f"Привет {message.from_user.full_name}")
    @dp.message(Command(commands=['breeds']))
    async def send_breed(message: Message):
        response = get("https://catfact.ninja/breeds")
        response_json = response.json()
        print(response_json["data"][0]["country"])
        print(response_json["data"][0]["breed"])
    @dp.message()
    async def send_other_message(message: Message):
        await message.answer("Ты мне надоел, хватит присылать какой-то бред!!")
        print(f"[LOG] пользователь получил ответ")
    await dp.start_polling(bot)
print("[LOG] Бот запущен")
run(main()) #запускает цикла событий (dp)