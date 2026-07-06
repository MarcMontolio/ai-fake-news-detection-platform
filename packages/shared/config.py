from functools import lru_cache
from urllib.parse import quote_plus

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )

    app_env: str = "development"
    app_host: str = "0.0.0.0"
    app_port: int = 8000

    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str = "fake_news_platform"
    postgres_user: str = "fake_news_user"
    postgres_password: str = "fake_news_password"

    database_url: str | None = None

    @property
    def sqlalchemy_database_url(self) -> str:
        if self.database_url:
            return self.database_url

        username = quote_plus(self.postgres_user)
        password = quote_plus(self.postgres_password)

        return (
            "postgresql+psycopg://"
            f"{username}:{password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )


@lru_cache
def get_settings() -> Settings:
    return Settings()
