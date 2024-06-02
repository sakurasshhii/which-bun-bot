from aiogram.types import CallbackQuery
from aiogram.filters import BaseFilter
from lexicon.lexicon import QUEST_RES


class QuestCallback(BaseFilter):
    def __call__(self, callback: CallbackQuery) -> bool | list:
        keys = list(filter(
            lambda c: c in QUEST_RES,
            callback.data.split(',')
        ))
        if keys:
            return {'keys': keys}
        return False
