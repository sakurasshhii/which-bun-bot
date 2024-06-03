from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.data_dict import data_convert


QUEST = data_convert('lexicon/data_raw.txt')

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
