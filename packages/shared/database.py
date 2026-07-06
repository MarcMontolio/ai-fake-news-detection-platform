from collections.abc import Generator

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session, sessionmaker

from packages.shared.config import get_settings

engine: Engine = create_engine(
    get_settings().sqlalchemy_database_url,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_sessions() -> Generator[Session]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
