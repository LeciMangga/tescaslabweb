from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    DB_URL: str = Field(..., env="DB_URL")
    
    class Config:
        env_file = ".env"

settings = Settings()