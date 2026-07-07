import pytest
from pydantic import ValidationError

from packages.shared.datasets import ProcessedArticleRecord, RawArticleRecord


def test_raw_article_record_accepts_valid_data() -> None:
    record = RawArticleRecord(
        title="Test article",
        content="This is test content",
        label="fake",
        source="Test source",
        url="https://example.com/news/article",
    )

    assert record.title == "Test article"
    assert record.content == "This is test content"
    assert record.label == "fake"
    assert record.source == "Test source"
    assert str(record.url) == "https://example.com/news/article"


def test_raw_article_record_rejects_invalid_label() -> None:
    with pytest.raises(ValidationError):
        RawArticleRecord(
            title="Test article",
            content="This is test content",
            label="misleading",
        )


def test_raw_article_record_rejects_empty_title() -> None:
    with pytest.raises(ValidationError):
        RawArticleRecord(title="", content="This is test content", label="fake")


def test_raw_article_record_rejects_empty_content() -> None:
    with pytest.raises(ValidationError):
        RawArticleRecord(title="Test article", content="", label="fake")


def test_raw_article_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        RawArticleRecord(
            title="Test article",
            content="This is test content",
            label="fake",
            extra="Extra field",
        )


def test_processed_article_record_accepts_valid_data() -> None:
    record = ProcessedArticleRecord(
        text="This is test processed article text",
        label="fake",
        source="Test source",
        url="https://example.com/news/article",
    )

    assert record.text == "This is test processed article text"
    assert record.label == "fake"
    assert record.source == "Test source"
    assert str(record.url) == "https://example.com/news/article"


def test_processed_article_record_rejects_invalid_label() -> None:
    with pytest.raises(ValidationError):
        ProcessedArticleRecord(
            text="This is test processed article text",
            label="misleading",
        )


def test_processed_article_record_rejects_empty_text() -> None:
    with pytest.raises(ValidationError):
        ProcessedArticleRecord(text="", label="fake")


def test_processed_article_record_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        ProcessedArticleRecord(
            text="This is test processed article", label="fake", extra="Extra field"
        )
