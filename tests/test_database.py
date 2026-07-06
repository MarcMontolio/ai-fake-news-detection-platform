from contextlib import suppress

from packages.shared.database import SessionLocal, engine, get_db_sessions


def test_database_engine_uses_configured_url() -> None:
    assert (
        engine.url.render_as_string(hide_password=False)
        == "postgresql+psycopg://fake_news_user:fake_news_password"
        "@localhost:5432/fake_news_platform"
    )


def test_session_factory_is_bound_to_engine() -> None:
    session = SessionLocal()

    try:
        assert session.bind is engine
    finally:
        session.close()


def test_get_db_engine_yields_session_bound_to_engine() -> None:
    db_generator = get_db_sessions()
    session = next(db_generator)

    try:
        assert session.bind is engine
    finally:
        with suppress(StopIteration):
            pass
