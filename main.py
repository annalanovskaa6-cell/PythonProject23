from config import BOT_TOKEN
from aiogram import Bot, Dispatcher
from asyncio import run
from aiogram import F
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, \
    CallbackQuery
from aiogram.filters import Command
async def main():
    bot = Bot(token = BOT_TOKEN)
    dp = Dispatcher()


    start_test_btn = KeyboardButton(
        text = "Начать тест"
    )
    menu_buttons = ReplyKeyboardMarkup(
        keyboard = [[start_test_btn]]
    )
    questions = [
        {"Кто выиграл чемпионат мира по футболу в 2022 году?":
             {"Аргентина": True,
              "Испания": False,
              "Франция": False
              }
         },
        {"В каком году произошло крещение Руси?": "988 год"},
        {"Кто был последним императором Римской империи перед её падением?": "Флавий Ромул Август"}
    ]
    counter = 0
    @dp.message(Command(commands="start"))
    async def start_handler(message: Message):
        await message.answer(
            "Начинаем тест, нажмите начать тест",
            reply_markup = menu_buttons
        )
    @dp.message(F.text == "Начать тест")
    async def start_test_handler(message: Message):
        counter = 0
        answ = list(questions[counter].keys())
        text = list(questions[0].values())[0]
        answ_1_btn = InlineKeyboardButton(
            text = text,
            callback_data = "question"
        )
        answ_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[answ_1_btn]]
        )
        await message.answer(
            answ[0],
            reply_markup = answ_keyboard
        )
    @dp.callback_query(F.data.startswith("question"))
    async def answ_handler(callback: CallbackQuery):
        nonlocal counter
        counter += 1
        answ = list(questions[counter].keys())[0]
        text = list(questions[counter].values())[0]
        answ_1_btn = InlineKeyboardButton(
            text=text,
            callback_data="question"
        )
        answ_keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[answ_1_btn]]
        )
        await callback.message.answer(
            text = answ,
            reply_markup = answ_keyboard
        )















    await dp.start_polling(bot)
print("[LOG] Бот запущен")
run(main()) #запускает цикла событий (dp)