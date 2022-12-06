from pydantic.env_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URI: str
    SECRET_KEY: str


settings = Settings(".env")
