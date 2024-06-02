from aiogram.types import CallbackQuery


def quest_callback(F: CallbackQuery) -> bool | list:
    if F.data and F.data.startswith('quest'):
        return F.data.split(',')[1:]
    return
