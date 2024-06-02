from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from lexicon import *
from utilities.filters import quest_callback
import keyboards


router = Router()
keyboard = keyboards.InlineKeyboardGenerator(BUTTONS_LEXIC)

# /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=keyboard(
            1, 'quest_y', 'quest_n'
        )
    )

# /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_EN['/help'])

# keyboard button
@router.callback_query(F.data, F.data == 'quest_y')
async def process_buttons_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['quest_start']
    )
    await callback.message.answer(
        text=keyboards.test_q_queue[0],
        reply_markup=keyboards.test_queue[0]
    )

@router.callback_query(quest_callback)
async def process_next_question(callback: CallbackQuery):
    print('catch', callback.data.text)
    callback.answer()
