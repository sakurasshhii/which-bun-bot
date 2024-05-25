import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config


async def main() -> None:
    config: Config = load_config()

    bot = Bot(config.tg_bot.bot_token)
    dp = Dispatcher()

    

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
