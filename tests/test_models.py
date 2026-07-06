from packages.shared.db.models.analysis import Analysis
from packages.shared.db.models.article import Article


def test_article_model_has_expected_table_name() -> None:
    assert Article.__tablename__ == "articles"


def test_analysis_model_has_expected_table_name() -> None:
    assert Analysis.__tablename__ == "analyses"


def test_article_model_has_expected_columns() -> None:
    assert list(Article.__table__.columns.keys()) == [
        "id",
        "title",
        "content",
        "source_url",
        "source_domain",
        "created_at",
    ]


def test_analyses_model_has_expected_columns() -> None:
    assert list(Analysis.__table__.columns.keys()) == [
        "id",
        "article_id",
        "predicted_label",
        "confidence",
        "credibility_score",
        "risk_level",
        "model_version",
        "created_at",
    ]


def test_article_analysis_relationship_is_configured() -> None:
    foreign_keys = Analysis.__table__.columns["article_id"].foreign_keys

    assert len(foreign_keys) == 1

    foreign_key = next(iter(foreign_keys))

    assert foreign_key.target_fullname == "articles.id"
