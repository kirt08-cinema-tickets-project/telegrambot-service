import asyncio
import logging

from aiogram import Bot

from src.core.config import settings
from src.core.dispatcher import setup_dispatcher
from src.bot.grcp_clients import on_startup

log = logging.getLogger(__name__)
logging.basicConfig(
    format=settings.logger.format, 
    level=settings.logger.log_level   
)

async def main():
    bot = Bot(settings.bot.token)
    dp = setup_dispatcher()
    dp.startup.register(on_startup)
    await dp.start_polling(bot)

if __name__ == "__main__":
    log.info("Start Up")
    asyncio.run(main())
    log.info("Shut down")
