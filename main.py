import asyncio
import logging

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers
from keyboards.menu import set_main_menu


logger = logging.getLogger(name=__name__)
logging.basicConfig(
    level=logging.INFO,
    format='#%(levelname)s [%(asctime)s] - '\
    '%(filename)s:%(lineno)d - %(message)s'
)

async def main() -> None:
    config: Config = load_config()

    bot = Bot(token=config.tg_bot.bot_token)
    dp = Dispatcher()

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)
    dp.startup.register(set_main_menu)
    
    logger.warning('start polling...')
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
