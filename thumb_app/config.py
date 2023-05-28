from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    UNSPLASH_KEY: str
    UNSPLASH_API: str = "https://api.unsplash.com/search/photos"
    ENV_NAME: str = "Local"
    BASE_URL: str = "http://localhost:8000"
    DB_URL: str = "sqlite:///./thumbnails.db"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()  # type: ignore
    print(f"Loading settings for: {settings.ENV_NAME}")
    return settings
