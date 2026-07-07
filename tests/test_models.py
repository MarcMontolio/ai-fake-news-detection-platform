from packages.shared.db.models.analysis import Analysis
from packages.shared.db.models.article import Article
from packages.shared.db.models.explanation import Explanation
from packages.shared.db.models.source import Source


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


def test_explanation_model_has_expected_name() -> None:
    assert Explanation.__tablename__ == "explanations"


def test_source_model_has_expected_name() -> None:
    assert Source.__tablename__ == "sources"


def test_explanation_model_has_expected_columns() -> None:
    assert list(Explanation.__table__.columns.keys()) == [
        "id",
        "analysis_id",
        "feature",
        "impact",
        "weight",
    ]


def test_source_model_has_expected_columns() -> None:
    assert list(Source.__table__.columns.keys()) == [
        "id",
        "domain",
        "credibility_score",
        "bias_label",
        "factuality_label",
        "notes",
        "updated_at",
    ]


def test_explanation_analysis_relationship_is_configured() -> None:
    foreign_keys = Explanation.__table__.columns["analysis_id"].foreign_keys

    foreign_key = next(iter(foreign_keys))

    assert foreign_key.target_fullname == "analyses.id"


def test_source_domain_is_unique() -> None:
    assert Source.__table__.columns["domain"].unique is True


def test_source_domain_has_index() -> None:
    assert Source.__table__.columns["domain"].index is True


def test_source_updated_at_has_onupdate_value() -> None:
    assert Source.__table__.columns["updated_at"].onupdate is not None
