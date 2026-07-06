from packages.shared.config import Settings


def test_settings_builds_default_sqlalchemy_database_url() -> None:
    settings = Settings()

    assert (
        settings.sqlalchemy_database_url
        == "postgresql+psycopg://fake_news_user:fake_news_password"
        "@localhost:5432/fake_news_platform"
    )


def test_settings_uses_explicit_database_when_provided() -> None:
    settings = Settings(
        database_url="postgresql+psycopg://user:password@postgres:5432/test_db"
    )

    assert (
        settings.sqlalchemy_database_url
        == "postgresql+psycopg://user:password@postgres:5432/test_db"
    )
