from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from lexicon.lexicon import LEXICON_EN
from keyboards.keyboard import keyboard_url


router = Router()

# /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_EN['/start'],
                         reply_markup=keyboard_url)

# /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_EN['/help'])
