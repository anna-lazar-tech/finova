import os

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Finova API")
    API_V1_PREFIX: str = os.getenv("API_V1_PREFIX", "/api/v1")
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./finova.db"
    )


settings = Settings()