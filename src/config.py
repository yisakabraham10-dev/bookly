from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str

    model_congig = SettingsConfigDict(
        env_file= .env
        extra= "ignore"
    )

Config = Settings()