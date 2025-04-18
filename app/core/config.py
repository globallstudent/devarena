from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+psycopg2://postgres:2021@localhost:5432/devarena_db"
    class Config:
        env_file = ".env"

settings = Settings()
