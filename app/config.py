from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment variables."""

    app_name: str = "Weather Alert Bot"
    log_level: str = "INFO"

    database_url: str = "sqlite:///./bot.db"

    telegram_bot_token: str

    weather_api_key: str | None = None
    air_api_key: str | None = None

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )


settings = Settings()
