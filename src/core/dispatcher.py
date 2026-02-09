from aiogram import Dispatcher

from src.bot import router

def setup_dispatcher() -> Dispatcher:
    dp = Dispatcher()

    dp.include_router(router)

    return dp