from dataclasses import dataclass
from environs import Env
import logging


logger = logging.getLogger(__name__)

@dataclass 
class TgBot:
    bot_token: str
    admin_id: str

@dataclass 
class Config:
    tg_bot: TgBot


def load_config(path: str = None) -> Config:
    logger.info('loading Env()...')
    env = Env()
    env.read_env(path)
    return Config(
        tg_bot=TgBot(
            bot_token=env('BOT_TOKEN'),
            admin_id=env('SUPERADMIN')
        )
    )
