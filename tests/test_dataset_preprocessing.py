import pytest

from packages.shared.datasets import RawArticleRecord
from packages.shared.datasets.preprocessing import (
    build_processed_text,
    normalize_label,
    normalize_whitespace,
    preprocess_raw_article,
    preprocess_raw_articles,
)


def test_normalize_whitespace_collapses_extra_spaces() -> None:
    raw_text = "  This   is    test content  "

    normalized_text = normalize_whitespace(raw_text)

    assert normalized_text == "This is test content"


def test_normalize_whitespace_handles_newlines_and_tabs() -> None:
    raw_text = "This\n\nis\t test\ncontent"

    normalized_text = normalize_whitespace(raw_text)

    assert normalized_text == "This is test content"


def test_build_processed_text_combines_title_and_content() -> None:
    title = "Test   title"
    content = "This\n\nis\t test content"

    result = build_processed_text(title, content)

    assert result == "Test title This is test content"


def test_normalize_label_accepts_supported_labels() -> None:
    label = "fake"

    normalized_label = normalize_label(label)

    assert normalized_label == "fake"


def test_normalize_label_is_case_insensitive() -> None:
    label = "REAL"

    normalized_label = normalize_label(label)

    assert normalized_label == "real"


def test_normalize_label_rejects_unsupported_labels() -> None:
    label = "misleading"

    with pytest.raises(ValueError):
        normalize_label(label)


def test_preprocess_raw_article_returns_processed_article_record() -> None:
    raw_article_record = RawArticleRecord(
        title="Test article",
        content="This is test content",
        label="fake",
        source="Test source",
        url="https://example.com/news/article",
    )

    processed_article_record = preprocess_raw_article(raw_article_record)

    assert processed_article_record.text == "Test article This is test content"
    assert processed_article_record.label == "fake"
    assert processed_article_record.source == raw_article_record.source
    assert str(processed_article_record.url) == str(raw_article_record.url)


def test_preprocess_raw_article_normalizes_text_whitespace() -> None:
    article_record = RawArticleRecord(
        title="     Test    article ",
        content="This\n\nis\t test  content ",
        label="real",
    )

    processed_article_record = preprocess_raw_article(article_record)

    assert processed_article_record.text == "Test article This is test content"
    assert processed_article_record.label == "real"


def test_preprocess_raw_articles_processes_multiple_records() -> None:
    raw_article_record_1 = RawArticleRecord(
        title="Test article 1",
        content="This is test content",
        label="fake",
        source="Test source",
        url="https://example.com/news/article1",
    )
    raw_article_record_2 = RawArticleRecord(
        title="Test article 2",
        content="This is test content",
        label="real",
        source="Test source",
        url="https://example.com/news/article2",
    )

    processed_article_records = preprocess_raw_articles(
        [raw_article_record_1, raw_article_record_2]
    )

    assert len(processed_article_records) == 2

    assert processed_article_records[0].text == "Test article 1 This is test content"
    assert processed_article_records[0].label == "fake"
    assert processed_article_records[0].source == raw_article_record_1.source
    assert processed_article_records[0].url == raw_article_record_1.url

    assert processed_article_records[1].text == "Test article 2 This is test content"
    assert processed_article_records[1].label == "real"
    assert processed_article_records[1].source == raw_article_record_2.source
    assert processed_article_records[1].url == raw_article_record_2.url
