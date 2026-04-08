from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from lexicons.lexicon import START_TEST_BTN
async def get_answ_btns(btns: dict):
    s = []
    for i, (key, value) in enumerate(btns.items()):
        btn = InlineKeyboardButton(
            text=key,
            callback_data=f"question_{i}"
        )
        s.append([btn])
    answ_keyboard = InlineKeyboardMarkup(
        inline_keyboard=s
    )
    return answ_keyboard

async def get_menu_keyboard():
    start_test_btn = KeyboardButton(
        text=START_TEST_BTN
    )
    menu_buttons = ReplyKeyboardMarkup(
        keyboard=[[start_test_btn]]
    )
    return menu_buttons