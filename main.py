import asyncio
import requests
from config import Config, load_config
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
config: Config = load_config()
bot_token = config.bot.token
bot = Bot(token=bot_token)
dp = Dispatcher()
@dp.message(Command(commands=['start']))
async def process_start(message: Message):
    await message.answer("Привет! Я твой первый бот")
#help
@dp.message(Command(commands=['help']))
async def process_help(message: Message):
    await message.answer("Чем тебе помочь?")
@dp.message(Command(commands=['dog']))
async def process_dog(message: Message):
    request = requests.get("https://dog.ceo/api/breeds/image/random")
    await message.answer(request.text)
@dp.message()
async def send_echo(message: Message):
    await message.reply(message.text)
async def main():
    await dp.start_polling(bot)
if __name__ == '__main__':
    asyncio.run(main())