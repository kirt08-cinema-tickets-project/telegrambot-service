from aiogram import Dispatcher

from src.core.config import settings
from src.core.grpc_clients import AuthClient

auth_url = str(settings.grpc.host) + ":" + str(settings.grpc.port)

async def on_startup(dispatcher: Dispatcher):
    dispatcher["auth_client"] = AuthClient(auth_url)
