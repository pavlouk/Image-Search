from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    UNSPLASH_KEY: str = ""
    UNSPLASH_API: str = "https://api.unsplash.com/search/photos"
    ENV_NAME: str = "Local"
    BASE_URL: str = "http://localhost:8000"
    DB_URL: str = "sqlite:///./thumbnails.db"

    class Config:
        env_file = ".env"


settings = Settings()
