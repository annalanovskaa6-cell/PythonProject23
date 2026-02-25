import asyncio
from config import Config, load_config
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, FSInputFile
from pathlib import Path

config: Config = load_config()
bot_token = config.bot.token
bot = Bot(token=bot_token)
dp = Dispatcher()

# #домашняя папка пользователя
# HOME_DIR = Path.home()
# #рабочий стол
# DESKTOP_DIR = HOME_DIR / 'Desktop'
# #папка downloads
# DOWNLOAD_DIR = HOME_DIR / 'downloads'

# @dp.message(F.photo)
# async def download_photo(message: Message, bot: Bot):
#     photo = message.photo[-1]
#     file = await bot.get_file(photo.file_id)
#     await bot.download_file(file.file_path, "/")

@dp.message(F.photo)
async def send_photo_url(message: Message):
    # photo = "https://glstatic.rg.ru/uploads/images/2016/03/05/86a8c745a45790e.jpg"
    # await message.answer_photo(
    #     photo,
    #     caption= "Фото кота"
    # )
    #отправка локального файла
    # photo = FSInputFile("files/test_1.jpg")
    # file = await bot.get_file(photo.file_id)
    # await message.reply_photo(
    #     photo = photo,
    #     caption = "Вот сохранённое фото"
    # )
@dp.message(F.photo)
async def reply_photo(message: Message):
    photo = message.photo[-1]
    await message.answer_photo(
        photo = photo.file_id,
        caption = "Не присылай больше"
    )
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())