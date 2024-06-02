from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
import logging


logger = logging.getLogger(__name__)
router = Router()

# all messages except /start and /help
@router.message()
async def process_all_answer(message: Message):
    logger.error('user sent something')
    await message.answer()

# missed buttons callback
@router.callback_query(F.data)
async def process_all_callbackquery(callback: CallbackQuery):
    logger.error(f'callback message: {callback.data}')
    await callback.answer()
