from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from lexicons.lexicon import QUESTIONS, START_TEST_BTN, START_TEST_ANSW, RESULT_TEST_ANSW
from keyboards.keyboards import get_menu_keyboard, get_answ_btns
router = Router()
counter = 0
user_answ = []
@router.message(Command(commands="start"))
async def start_handler(message: Message):
    await message.answer(
        START_TEST_ANSW,
        reply_markup = await get_menu_keyboard()
    )
@router.message(F.text == START_TEST_BTN)
async def start_test_handler(message: Message):
    quest = list(QUESTIONS[0].keys())[0]
    btns_data = QUESTIONS[0][quest]
    keyboard = await get_answ_btns(btns_data)
    await message.answer(
        quest,
        reply_markup = keyboard
    )
@router.callback_query(F.data.startswith("question"))
async def answ_handler(callback: CallbackQuery):
    global counter, user_answ
    data = callback.data
    num = int(data.split("_")[1])
    user_answ.append(num)
    counter += 1
    if counter == 3:
        await callback.message.answer(RESULT_TEST_ANSW)
    else:
        answ = list(QUESTIONS[counter].keys())[0]
        btns_data= list(QUESTIONS[counter].values())[0]
        keyboard = await get_answ_btns(btns_data)
        await callback.message.answer(
            text = answ,
            reply_markup = keyboard
    )