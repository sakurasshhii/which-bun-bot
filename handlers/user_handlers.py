from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from keyboards.generator import InlineKeyboardGenerator
from lexicon import *


router = Router()
keyboard = InlineKeyboardGenerator(BUTTONS_LEXIC)

# /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_EN['/start'],
        reply_markup=keyboard(
            2, 'button 0', 'batt1', *BUTTONS_TEST
        )
    )

# /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_EN['/help'])

# keyboard button
@router.callback_query(F.data)
async def process_buttons_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=('button pressed!'),
        reply_markup=callback.message.reply_markup
    )
    await callback.answer(
        text='that\'s notification message',
        show_alert=True)
