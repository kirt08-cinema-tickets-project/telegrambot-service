from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

from src.core.config.botConfig import BotConfig
from src.core.config.grpcConfig import GrpcConfig
from src.core.config.loggerConfig import LoggerConfig

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive = False,
        env_file = BASE_DIR / ".env",
        env_prefix = "TELEGRAMBOT_SERVICE__",
        env_nested_delimiter="__",
    )
    bot : BotConfig = BotConfig()
    grpc : GrpcConfig = GrpcConfig()
    logger : LoggerConfig = LoggerConfig()


settings = Settings()
