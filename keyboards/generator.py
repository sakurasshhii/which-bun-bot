from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class InlineKeyboardGenerator:
    """
    helps to create keyboard
    use selected dict to search button text
    works with kwargs in the same way
    """

    def __init__(self, lexic: dict = None):
        self.lexic = dict(lexic) or dict()

    def __call__(self, width: int, *bt: str, **kbt: dict) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardBuilder()
        buttons = list()
    
        if bt:
            for name in bt:
                buttons.append(InlineKeyboardButton(
                    text=self.lexic.get(name, name),
                    callback_data=name
                ))
        if kbt:
            print(kbt)
            for cb_data, name in kbt.items():
                buttons.append(InlineKeyboardButton(
                    text=name,
                    callback_data=cb_data
                ))

        keyboard.row(
            *buttons,
            width=width
        )
        
        return keyboard.as_markup()
    