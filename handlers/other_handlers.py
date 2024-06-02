from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon import LEXICON_EN
import logging


logger = logging.getLogger(__name__)
router = Router()

# all messages except /start and /help
@router.message()
async def process_all_answer(message: Message):
    await message.answer('You sent something unexpectable ~e_e~~')

# missed buttons callback
@router.callback_query(F.data)
async def process_all_callbackquery(callback: CallbackQuery):
    logger.error(f'callback message: {callback.data}')
    await callback.answer()
