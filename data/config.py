from pydantic_settings import BaseSettings
from typing import Optional, List

class Settings(BaseSettings):
    BOT_TOKEN: str
    ADMINS: List[int] = []
    USE_REDIS: bool = False
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
