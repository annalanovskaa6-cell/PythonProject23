from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram import F
from aiogram.types import Message
import os
async def main():
    bot = Bot(token = BOT_TOKEN)
    dp = Dispatcher()

    # @dp.message(F.photo)
    # async def get_photo(message: Message, bot: Bot):
    #     print(f"[LOG] пользователь {message.from_user.id} вызвал функцию get_photo")
    #     photo = message.photo[-1]
    #     file = await bot.get_file(photo.file_id)
    #     print(f"[LOG] получение файла {file.file_unique_id}")
    #     PATH = os.path.join("files", f"{file.file_unique_id}.jpg")
    #     print(PATH)
    #     await bot.download_file(file.file_path, destination=PATH)
    #     print(f"[LOG] сохранение файла {PATH}")
    #     await message.answer("Крутое фото")

        # @dp.message(F.video)
        # async def get_photo(message: Message, bot: Bot):
        #     print(f"[LOG] пользователь {message.from_user.id} вызвал функцию get_photo")
        #     video = message.video
        #     file = await bot.get_file(video.file_id)
        #     print(f"[LOG] получение файла {file.file_unique_id}")
        #     PATH = os.path.join("files", f"{file.file_unique_id}.mp4")
        #     await bot.download_file(file.file_path, destination=PATH)
        #     print(f"[LOG] сохранение файла {PATH}")
        #     await message.answer("Крутое видео")

    @dp.message(F.photo | F.video)
    async def get_photo(message: Message, bot: Bot):
        os.makedirs("downloads", exist_ok=True)
        if message.photo:
            file = await bot.get_file(message.photo[-1].file_id)
            PATH = os.path.join("downloads", f"{file.file_unique_id}.jpg")
        else:
            file = await bot.get_file(message.video.file_id)
            PATH = os.path.join("downloads", f"{file.file_unique_id}.mp4")
        await bot.download_file(file.file_path, destination=PATH)
        await message.answer("Крутые фото или видео")

    # # https://catfact.ninja/fact
    # @dp.message(Command(commands = ['catfact']))
    # async def get_cat_fact(message: Message):
    #     print(f"[LOG] пользователь {message.from_user.id} нажал команду /catfact")
    #     print(f"[LOG] запрашиваю факт о котах")
    #     response = get("https://catfact.ninja/fact")
    #     print(f"[LOG] Получен результат со статусом {response.status_code}")
    #     response_json = response.json()
    #     print(response_json["fact"])
    #     await message.answer(response_json["fact"])
    # @dp.message(Command(commands=['start']))
    # async def start_handler(message: Message):
    #     print(f"[LOG] пользователь {message.from_user.id} нажал кнопку /start")
    #     await message.answer(f"Привет {message.from_user.full_name}")
    # @dp.message(Command(commands=['breeds']))
    # async def send_breed(message: Message):
    #     response = get("https://catfact.ninja/breeds")
    #     response_json = response.json()
    #     print(response_json["data"][0]["country"])
    #     print(response_json["data"][0]["breed"])
    # @dp.message()
    # async def send_other_message(message: Message):
    #     await message.answer("Ты мне надоел, хватит присылать какой-то бред!!")
    #     print(f"[LOG] пользователь получил ответ")
    await dp.start_polling(bot)
print("[LOG] Бот запущен")
run(main()) #запускает цикла событий (dp)