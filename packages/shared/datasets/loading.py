import csv
from pathlib import Path

from packages.shared.datasets.schemas import RawArticleRecord

REQUIRED_COLUMNS = {"title", "content", "label"}


def load_raw_articles_from_csv(file_path: str | Path) -> list[RawArticleRecord]:
    path = Path(file_path)

    with path.open(encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)

        if reader.fieldnames is None:
            msg = "CSV file is missing a header row"
            raise ValueError(msg)

        missing_columns = REQUIRED_COLUMNS - set(reader.fieldnames)

        if missing_columns:
            msg = f"CSV file is missing required columns {sorted(missing_columns)}"
            raise ValueError(msg)

        return [
            RawArticleRecord(
                title=row["title"],
                content=row["content"],
                label=row["label"],
                source=row.get("source") or None,
                url=row.get("url") or None,
            )
            for row in reader
        ]
