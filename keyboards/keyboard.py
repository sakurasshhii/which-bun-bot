from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


url_button_1 = InlineKeyboardButton(
    text='Tg bot with python&aiogram',
    url='https://stepik.org/120924'
)

url_button_2 = InlineKeyboardButton(
    text='Tg Bot API documentation',
    url='https://core.telegram.org/bots/api'
)

keyboard_url = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1], [url_button_2]]
)
