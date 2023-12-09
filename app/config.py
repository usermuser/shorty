import os

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # что делает field?????? и что за переменная env ????? как бысторо перейти посмотреть(хоткей)????
    db_url: str = Field(..., env='DATABASE_URL')
# создание экземпляра settings
settings = Settings()
