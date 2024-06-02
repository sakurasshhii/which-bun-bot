from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.generator import InlineKeyboardGenerator
from lexicon.data_dict import QUEST


# Создаем объекты инлайн-кнопок
big_button_1 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='big_button_1_pressed'
)

big_button_2 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data='big_button_2_pressed'
)

# Создаем объект инлайн-клавиатуры
keyboard_1 = InlineKeyboardMarkup(
    inline_keyboard=[[big_button_1],
                     [big_button_2]]
)

test_queue: list[dict[str: list[InlineKeyboardMarkup, ]]] = list()
for question, answers in QUEST.items():
    kb = InlineKeyboardBuilder()
    kb.row(*[InlineKeyboardButton(
        text=k,
        callback_data=v
        ) for k, v in answers.items()
        ],
        width=1
    )
    test_queue.append((question, kb.as_markup()))
