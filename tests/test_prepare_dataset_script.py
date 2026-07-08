import csv
from pathlib import Path

from scripts.prepare_dataset import prepare_dataset


def test_prepare_dataset_writes_train_and_test_csv_files(tmp_path: Path) -> None:
    input_csv = tmp_path / "raw_articles.csv"
    output_dir = tmp_path / "processed"

    input_csv.write_text(
        "title,content,label,source,url\n"
        "Real title,Real content,real,Example,https://example.com/real\n"
        "Fake title,Fake content, FAKE ,Example,https://example.com/fake\n"
        "Another fake,More fake content,fake,Example,https://example.com/fake2\n"
        "Another real,More real content, REAL ,Example,https://example.com/real2\n",
        encoding="utf-8",
    )

    prepare_dataset(
        input_csv=input_csv,
        output_dir=output_dir,
        test_size=0.25,
        seed=42,
    )

    assert (output_dir / "train.csv").exists()
    assert (output_dir / "test.csv").exists()

    train_csv_path = output_dir / "train.csv"
    test_csv_path = output_dir / "test.csv"

    with train_csv_path.open(encoding="utf-8", newline="") as train_csv:
        train_rows = list(csv.DictReader(train_csv))
    with test_csv_path.open(encoding="utf-8", newline="") as test_csv:
        test_rows = list(csv.DictReader(test_csv))

    assert len(train_rows) == 3
    assert len(test_rows) == 1
    assert len(train_rows) + len(test_rows) == 4

    all_rows = train_rows + test_rows
    labels = {row["label"] for row in all_rows}

    assert labels == {"fake", "real"}
