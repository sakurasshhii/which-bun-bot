from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery
from time import sleep
from random import randint
from collections import Counter
from lexicon import *
from module.user_data import users
import keyboards
import logging


logger = logging.getLogger(__name__)
router = Router()
keyboard = keyboards.InlineKeyboardGenerator(BUTTONS_LEXIC)


# /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    users.setdefault(message.from_user.id, {})
    await message.answer(
        text=LEXICON_RU['/start'],
        reply_markup=keyboard(
            1, 'quest_y', 'quest_n'
        )
    )

# /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

# quest abort
@router.callback_query(F.data, F.data == 'quest_n')
async def process_quest_abort(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['quest_no'],
        reply_markup=keyboard(
            1, 'quest_y'
        )
    )

# quest start
@router.callback_query(F.data, F.data == 'quest_y')
async def process_quest_start(callback: CallbackQuery):
    users[callback.from_user.id]['cache'] = Counter()
    users[callback.from_user.id]['current'] = 0
    await callback.message.edit_text(
        text=LEXICON_RU['quest_start']
    )
    await callback.message.answer(
        text=keyboards.test_queue[0][0],
        reply_markup=keyboards.test_queue[0][1]
    )

# quest continious
@router.callback_query(F.data, F.data.startswith('quest,'))
async def process_next_question(callback: CallbackQuery):
    logger.info(f'your callback data: {callback.data}')
    users[callback.from_user.id]['cache'].update(
        Counter([c for c in callback.data.split(',') if c in QUEST_RES])
    )
    logger.info(f'current user: {callback.from_user.id}\n'\
                   f'cache: {users[callback.from_user.id]["cache"]}')
    
    users[callback.from_user.id]['current'] += 1
    try:
        await callback.message.edit_text(
            text=keyboards.test_queue[users[callback.from_user.id]['current']][0],
            reply_markup=keyboards.test_queue[users[callback.from_user.id]['current']][1]
        )
    except IndexError:
        await callback.message.edit_text(
            text=LEXICON_RU['quest_last'],
            reply_markup=keyboard(
                1, *[i[0] for i in users[callback.from_user.id]['cache'].most_common(3)]
            )
        )

# last quest callback
@router.callback_query(F.data, F.data.in_(QUEST_RES))
async def process_quest_result(callback: CallbackQuery):
    users[callback.from_user.id]['cache'].update(Counter([callback.data]))
    logger.info(f'user results: {users[callback.from_user.id]["cache"]}')
    await callback.message.edit_text(
        text=LEXICON_RU['quest_load/1']
    )
    sleep(1)
    await callback.message.answer(
        text=LEXICON_RU['quest_load/2']
    )
    sleep(1)
    result = users[callback.from_user.id]['cache'].most_common(1)[0][0]
    await callback.message.answer(
        text=LEXICON_RU['quest_end'].format(
            randint(4001, 9999), 
            QUEST_RES[result]
        )
    )
    await callback.message.answer_photo(
        photo=PIC_URL[result]
    )
