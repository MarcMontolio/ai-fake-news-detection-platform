from pathlib import Path

import pytest
from pydantic import ValidationError

from packages.shared.datasets import load_raw_articles_from_csv


def test_load_raw_articles_from_csv_loads_valid_rows(tmp_path: Path) -> None:
    csv_path = tmp_path / "articles.csv"

    csv_path.write_text(
        "title,content,label,source,url\n"
        "Test article,This is test content,fake,Test source,https://example.com/news/article\n",
        encoding="utf-8",
    )

    records = load_raw_articles_from_csv(csv_path)

    assert len(records) == 1

    record = records[0]

    assert record.title == "Test article"
    assert record.content == "This is test content"
    assert record.label == "fake"
    assert record.source == "Test source"
    assert str(record.url) == "https://example.com/news/article"


def test_load_raw_articles_from_csv_rejects_missing_required_column(
    tmp_path: Path,
) -> None:
    csv_path = tmp_path / "articles.csv"

    csv_path.write_text(
        "title,label,source,url\n"
        "Test article,fake,Test source,https://example.com/news/article\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="missing required columns"):
        load_raw_articles_from_csv(csv_path)


def test_load_raw_articles_from_csv_rejects_missing_header(tmp_path: Path) -> None:
    csv_path = tmp_path / "articles.csv"

    csv_path.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="missing a header row"):
        load_raw_articles_from_csv(csv_path)


def test_load_raw_articles_from_csv_rejects_invalid_row_data(tmp_path: Path) -> None:
    csv_path = tmp_path / "articles.csv"

    csv_path.write_text(
        "title,content,label,source,url\n"
        ",This is test content,fake,Test source,https://example.com/news/article\n",
        encoding="utf-8",
    )

    with pytest.raises(ValidationError):
        load_raw_articles_from_csv(csv_path)


def test_load_raw_articles_from_csv_converts_empty_optional_fields_to_none(
    tmp_path: Path,
) -> None:
    csv_path = tmp_path / "articles.csv"

    csv_path.write_text(
        "title,content,label,source,url\nTest article,This is test content,fake,,\n",
        encoding="utf-8",
    )

    records = load_raw_articles_from_csv(csv_path)

    assert len(records) == 1

    record = records[0]

    assert record.source is None
    assert record.url is None


def test_load_raw_articles_from_csv_loads_multiple_rows(tmp_path: Path) -> None:
    csv_path = tmp_path / "articles.csv"

    csv_path.write_text(
        "title,content,label,source,url\n"
        "Test article 1,This is test content,fake,Test source,https://example.com/news/article1\n"
        "Test article 2,This is test content,real,Test source,https://example.com/news/article2\n",
        encoding="utf-8",
    )

    records = load_raw_articles_from_csv(csv_path)

    assert len(records) == 2

    record_1 = records[0]
    record_2 = records[1]

    assert record_1.title == "Test article 1"
    assert record_1.label == "fake"
    assert record_2.title == "Test article 2"
    assert record_2.label == "real"


def test_load_raw_articles_from_csv_handles_utf8_bom_headers(tmp_path: Path) -> None:
    csv_path = tmp_path / "articles.csv"

    csv_path.write_text(
        "title,content,label,source,url\n"
        "Test article,This is test content,fake,Test source,https://example.com/news/article\n",
        encoding="utf-8-sig",
    )

    records = load_raw_articles_from_csv(csv_path)

    assert len(records) == 1

    record = records[0]

    assert record.title == "Test article"
    assert record.label == "fake"


def test_load_raw_articles_from_csv_accepts_raw_label_values(tmp_path: Path) -> None:
    csv_path = tmp_path / "articles.csv"

    csv_path.write_text(
        "title,content,label,source,url\n"
        "Test article,This is test content, REAL ,Test source,https://example.com/news/article\n",
        encoding="utf-8-sig",
    )

    records = load_raw_articles_from_csv(csv_path)

    assert len(records) == 1

    record = records[0]

    assert record.label == " REAL "
