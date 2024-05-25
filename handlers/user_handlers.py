from aiogram import Router
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from aiogram.types import Message


router = Router()

# /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])

# /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
