from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart, ChatMemberUpdatedFilter, KICKED
from config_data import load_config

import handlers
import logging


config = load_config()

# logging settings
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)
log_handler = logging.StreamHandler()
log_handler.setFormatter(
        fmt='#%(levelname)-8s [%(asctime)s] - %(filename)s:'\
        '%(lineno)d - %(name)s - %(message)s'
        )
logger.addHandler(log_handler)

# bot registration
bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()


# /start; /help; /cancel
dp.message.register(handlers.process_start_command, CommandStart())
dp.message.register(handlers.process_help_command, Command(commands=['help']))
dp.message.register(handlers.process_cancel, Command(commands=['cancel']))

# game no; yes
dp.message.register(handlers.process_play_no, F.text.lower().in_(['no', 'n', 'нет']))
dp.message.register(handlers.process_play_yes, F.text.lower().in_(['yes', 'y', 'да', 'play', 'start']))
# number guessing
dp.message.register(handlers.process_guessing, lambda i: i.text and i.text.isdigit() and 1 <= int(i.text) <= 100)
# /statistics
dp.message.register(handlers.process_stat, Command(commands=['statistics']))

# /do_something — sending a cat picture
dp.message.register(utilities.process_cat_command, Command(commands=['do_something']))

# unexpected messagess
dp.message.register(handlers.process_any_message)

# user blocked the bot
dp.my_chat_member.register(errors.process_kicked, ChatMemberUpdatedFilter(member_status_changed=KICKED))


if __name__ == '__main__':
    dp.run_polling(bot) # dispetcher runs the bot object
