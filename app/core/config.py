from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    app_name: str = Field(default="FastAPI ToDo")
    database_url: str = Field(default="sqlite:///./local.db", alias="DATABASE_URL")

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
