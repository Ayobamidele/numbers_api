from pydantic_settings import BaseSettings
from decouple import config
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    PROJECT_NAME :str = "Numbers API"
    PROJECT_VERSION : str = "1.0.0"
    PROJECT_DESCRIPTION: str = "A Public API that takes a number and returns interesting mathematical properties about it, along with a fun fact."
    
settings = Settings()
