from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU


# all messages except /start and /help
@dp.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
        