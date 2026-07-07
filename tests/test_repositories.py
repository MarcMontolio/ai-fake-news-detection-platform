import pytest
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import Session, sessionmaker

from packages.shared.db import models
from packages.shared.db.base import Base
from packages.shared.db.repositories.analyses import AnalysisRepository
from packages.shared.db.repositories.articles import ArticleRepository


@pytest.fixture
def db_session() -> Session:
    _ = models

    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine,
    )

    session = SessionLocal()

    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(engine)


def test_article_repository_creates_article(db_session: Session) -> None:
    repository = ArticleRepository(db_session)

    article = repository.create(
        title="Test article",
        content="This is test content",
        source_url="https://example.com/news/test",
        source_domain="example.com",
    )

    assert article is not None
    assert article.title == "Test article"
    assert article.content == "This is test content"
    assert article.source_url == "https://example.com/news/test"
    assert article.source_domain == "example.com"


def test_article_repository_gets_article_by_id(db_session: Session) -> None:
    repository = ArticleRepository(db_session)

    article = repository.create(
        title="Test article",
        content="This is test content",
        source_domain="https://example.com/news/test",
        source_url="example.com",
    )

    retrieved_article = repository.get_by_id(article.id)

    assert retrieved_article is not None
    assert retrieved_article.id == article.id
    assert retrieved_article.title == "Test article"


def test_article_returns_none_for_missing_article(db_session: Session) -> None:
    repository = ArticleRepository(db_session)

    article = repository.get_by_id(999)

    assert article is None


def test_article_repository_list_recent_articles(db_session: Session) -> None:
    repository = ArticleRepository(db_session)

    repository.create(
        title="Test article 1",
        content="This is test content",
        source_domain="https://example.com/news/test1",
        source_url="example.com",
    )

    repository.create(
        title="Test article 2",
        content="This is test content",
        source_domain="https://example.com/news/test2",
        source_url="example.com",
    )

    repository.create(
        title="Test article 3",
        content="This is test content",
        source_domain="https://example.com/news/test3",
        source_url="example.com",
    )

    articles = repository.list_recent(limit=3)

    assert len(articles) == 3
    assert {article.title for article in articles} <= {
        "Test article 1",
        "Test article 2",
        "Test article 3",
    }


def test_analysis_repository_creates_analysis(db_session: Session) -> None:
    article_repository = ArticleRepository(db_session)
    analysis_repository = AnalysisRepository(db_session)

    article = article_repository.create(
        title="Test article", content="This is test content"
    )

    analysis = analysis_repository.create(
        article_id=article.id,
        predicted_label="fake",
        confidence=0.57,
        risk_level="medium",
        model_version="baseline-v1",
        credibility_score=0.25,
    )

    assert analysis.id is not None
    assert analysis.article_id == article.id
    assert analysis.predicted_label == "fake"
    assert analysis.confidence == 0.57
    assert analysis.risk_level == "medium"
    assert analysis.model_version == "baseline-v1"
    assert analysis.credibility_score == 0.25


def test_analysis_repository_gets_analysis_by_id(db_session: Session) -> None:
    article_repository = ArticleRepository(db_session)
    analysis_repository = AnalysisRepository(db_session)

    article = article_repository.create(title="Test", content="Test content")

    analysis = analysis_repository.create(
        article_id=article.id,
        predicted_label="fake",
        confidence=0.35,
        risk_level="high",
        model_version="baseline-v1",
        credibility_score=0.21,
    )

    retrieved_analysis = analysis_repository.get_by_id(analysis.id)

    assert retrieved_analysis is not None
    assert retrieved_analysis.id == analysis.id
    assert retrieved_analysis.article_id == article.id
    assert retrieved_analysis.predicted_label == "fake"


def test_analysis_repository_returns_none_for_missing_articles(
    db_session: Session,
) -> None:
    repository = ArticleRepository(db_session)

    analysis = repository.get_by_id(999)

    assert analysis is None
