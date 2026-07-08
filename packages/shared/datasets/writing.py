import csv
from pathlib import Path

from packages.shared.datasets.schemas import ProcessedArticleRecord

PROCESSED_ARTICLE_FIELDNAMES = ["text", "label", "source", "url"]


def write_processed_articles_to_csv(
    records: list[ProcessedArticleRecord], file_path: str | Path
) -> None:
    path = Path(file_path)

    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8", newline="") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=PROCESSED_ARTICLE_FIELDNAMES)

        writer.writeheader()

        for record in records:
            writer.writerow(
                {
                    "text": record.text,
                    "label": record.label,
                    "source": record.source or "",
                    "url": str(record.url) if record.url is not None else "",
                }
            )
