from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class InlineKeyboardGenerator:
    """helps to create keyboard"""

    def __init__(self, lexic: dict):
        self.lexic = lexic

    def __call__(self, width: int, *bt: str, **kbt: dict) -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardBuilder()
        buttons: list[InlineKeyboardButton] = []
        
        keyboard.row(*self.make_button(buttons, *bt, **kbt), width=width)
        
        return keyboard.as_markup()
    
    def make_button(self, buttons, *bt: str, **kbt: dict) -> list[InlineKeyboardButton]:
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
        
        return buttons
    