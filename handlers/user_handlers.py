from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from lexicon.lexicon import LEXICON_EN
from keyboards.keyboard import keyboard


router = Router()

# /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_EN['/start'],
                         reply_markup=keyboard)

# /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_EN['/help'])

# keyboard button
@router.callback_query(F.data.in_(['big_button_1_pressed',
                                   'big_button_2_pressed']))
async def process_buttons_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=('pressed button 1', 'pressed button 2')[callback.data == 'big_button_2_pressed'],
        reply_markup=callback.message.reply_markup
    )
    await callback.answer(
        text='that\'s notification message',
        show_alert=True)
