from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_EN


router = Router()

# all messages except /start and /help
@router.message()
async def process_all_answer(message: Message):
    await message.answer('You sent something unexpectable ~e_e~~')

