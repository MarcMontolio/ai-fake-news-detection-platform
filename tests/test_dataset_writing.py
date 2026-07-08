import csv
from pathlib import Path

from packages.shared.datasets import (
    ProcessedArticleRecord,
    write_processed_articles_to_csv,
)


def create_processed_records(count: int) -> list[ProcessedArticleRecord]:
    return [
        ProcessedArticleRecord(
            text=f"Test article {index}",
            label="fake" if index % 2 == 0 else "real",
        )
        for index in range(count)
    ]


def test_write_processed_articles_to_csv_write_records(tmp_path: Path) -> None:
    records = create_processed_records(2)

    csv_path = tmp_path / "processed" / "train.csv"

    write_processed_articles_to_csv(records=records, file_path=csv_path)

    assert csv_path.exists()

    with csv_path.open(encoding="utf-8", newline="") as csv_file:
        rows = list(csv.DictReader(csv_file))

    assert len(rows) == 2
    assert rows[0]["text"] == "Test article 0"
    assert rows[0]["label"] == "fake"
    assert rows[1]["text"] == "Test article 1"
    assert rows[1]["label"] == "real"


def test_write_processed_articles_to_csv_writes_empty_optional_fields(
    tmp_path: Path,
) -> None:
    record = ProcessedArticleRecord(
        text="Test article",
        label="fake",
        source=None,
        url=None,
    )

    csv_path = tmp_path / "processed" / "train.csv"

    write_processed_articles_to_csv(records=[record], file_path=csv_path)

    assert csv_path.exists()

    with csv_path.open(encoding="utf-8", newline="") as csv_file:
        rows = list(csv.DictReader(csv_file))

    assert len(rows) == 1
    assert rows[0]["text"] == "Test article"
    assert rows[0]["label"] == "fake"
    assert rows[0]["source"] == ""
    assert rows[0]["url"] == ""
