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
             {
                 "Аргентина": True,
                 "Испания": False,
                 "Франция": False
              }
         },
        {"В каком году произошло крещение Руси?":
             {
                 "988 год": True,
                 "856 год": False,
                 "1048 год": False
             }
         },
        {"Кто был последним императором Римской империи перед её падением?":
            {
                "Флавий Ромул Август ": True,
                "Гай Юлий Цезарь": False,
                "Октавиан Август": False
             }
         }
    ]
    counter = 0
    user_answ = []
    async def get_answ_btns(btns: dict):
        s = []
        for i, (key, value) in enumerate(btns.items()):
            btn = InlineKeyboardButton(
                text = key,
                callback_data = f"question_{i}"
            )
            s.append([btn])
        answ_keyboard = InlineKeyboardMarkup(
            inline_keyboard = s
        )
        return answ_keyboard
    @dp.message(Command(commands="start"))
    async def start_handler(message: Message):
        await message.answer(
            "Начинаем тест, нажмите начать тест",
            reply_markup = menu_buttons
        )
    @dp.message(F.text == "Начать тест")
    async def start_test_handler(message: Message):
        quest = list(questions[0].keys())[0]
        btns_data = questions[0][quest]
        keyboard = await get_answ_btns(btns_data)
        await message.answer(
            quest,
            reply_markup = keyboard
        )
    @dp.callback_query(F.data.startswith("question"))
    async def answ_handler(callback: CallbackQuery):
        nonlocal counter, user_answ
        data = callback.data
        num = int(data.split("_")[1])
        user_answ.append(num)
        counter += 1
        if counter == 3:
            s = ""
            for i in s:

            # 1 вопрос
            # Какой результат деления на 10
            # ответ : {ответ пользователя}
            await callback.message.answer("")
        else:
            answ = list(questions[counter].keys())[0]
            btns_data= list(questions[counter].values())[0]
            keyboard = await get_answ_btns(btns_data)
            await callback.message.answer(
                text = answ,
                reply_markup = keyboard
        )











    await dp.start_polling(bot)
print("[LOG] Бот запущен")
run(main()) #запускает цикла событий (dp)