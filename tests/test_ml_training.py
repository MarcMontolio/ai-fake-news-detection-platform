from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

from packages.shared.ml.training import (
    build_baseline_pipeline,
    train_baseline_classifier,
)


def test_build_baseline_pipeline_returns_pipeline() -> None:
    pipeline = build_baseline_pipeline()

    assert isinstance(pipeline, Pipeline)


def test_build_baseline_pipeline_has_expected_steps() -> None:
    pipeline = build_baseline_pipeline()

    pipeline_steps = pipeline.named_steps

    assert "tfidf" in pipeline_steps
    assert "classifier" in pipeline_steps


def test_train_baseline_classifier_returns_trained_pipeline() -> None:
    texts = [
        "shocking fake claim about politics",
        "false viral story spreads online",
        "hoax article with misleading information",
        "verified report from official sources",
        "confirmed article based on evidence",
        "factual news report with sources",
    ]

    labels = [
        "fake",
        "fake",
        "fake",
        "real",
        "real",
        "real",
    ]

    trained_pipeline = train_baseline_classifier(texts, labels)

    assert isinstance(trained_pipeline, Pipeline)

    predictions = trained_pipeline.predict(
        ["verified official report from reliable sources"]
    )

    assert len(predictions) == 1
    assert predictions[0] in {"fake", "real"}


def test_build_baseline_pipeline_uses_expected_components() -> None:
    pipeline = build_baseline_pipeline()

    pipeline_steps = pipeline.named_steps

    assert isinstance(pipeline_steps["tfidf"], TfidfVectorizer)
    assert isinstance(pipeline_steps["classifier"], LogisticRegression)
