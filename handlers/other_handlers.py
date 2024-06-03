from aiogram import Router
from aiogram.types import Message
import lexicon
import logging


logger = logging.getLogger(__name__)
router = Router()

# all messages except /start and /help
@router.message()
async def process_all_answer(message: Message):
    logger.error('user sent something')
    await message.answer(
        text=lexicon.LEXICON_RU['unexpected_message'].format(message.text)
    )
