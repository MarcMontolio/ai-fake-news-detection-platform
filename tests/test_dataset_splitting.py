import pytest

from packages.shared.datasets.schemas import ProcessedArticleRecord
from packages.shared.datasets.splitting import split_dataset, validate_test_size


def test_validate_test_size_accepts_valid_values() -> None:
    valid_test_sizes = [0.1, 0.2, 0.5, 0.8, 0.9]

    for valid_test_size in valid_test_sizes:
        validate_test_size(valid_test_size)


def test_validate_test_size_rejects_invalid_values() -> None:
    invalid_test_sizes = [0, 1, -0.1, 1.5]

    for invalid_test_size in invalid_test_sizes:
        with pytest.raises(ValueError):
            validate_test_size(invalid_test_size)


def create_processed_records(count: int) -> list[ProcessedArticleRecord]:
    return [
        ProcessedArticleRecord(
            text=f"Article {index}",
            label="fake" if index % 2 == 0 else "real",
        )
        for index in range(count)
    ]


def test_split_dataset_splits_records_by_test_size() -> None:
    records = create_processed_records(10)

    train_records, test_records = split_dataset(records, test_size=0.2, seed=42)

    assert len(train_records) == 8
    assert len(test_records) == 2


def test_split_dataset_is_reproducible_with_same_seed() -> None:
    records = create_processed_records(10)

    train_records_1, test_records_1 = split_dataset(records, test_size=0.2, seed=42)
    train_records_2, test_records_2 = split_dataset(records, test_size=0.2, seed=42)

    assert train_records_1 == train_records_2
    assert test_records_1 == test_records_2


def test_split_dataset_changes_with_different_seeds() -> None:
    records = create_processed_records(10)

    train_records_1, test_records_1 = split_dataset(records, test_size=0.2, seed=42)
    train_records_2, test_records_2 = split_dataset(records, test_size=0.2, seed=123)

    assert train_records_1 != train_records_2 or test_records_1 != test_records_2


def test_split_dataset_does_not_modify_original_records() -> None:
    records = create_processed_records(10)
    original_records = records.copy()

    split_dataset(records, test_size=0.2, seed=42)

    assert records == original_records


def test_split_dataset_does_not_drop_records() -> None:
    records = create_processed_records(10)

    train_records, test_records = split_dataset(records, test_size=0.2, seed=42)

    assert len(train_records) + len(test_records) == len(records)

    original_texts = sorted(record.text for record in records)
    split_texts = sorted(record.text for record in train_records + test_records)

    assert original_texts == split_texts


def test_split_dataset_rejects_invalid_test_size() -> None:
    records = create_processed_records(10)

    with pytest.raises(ValueError):
        split_dataset(records, test_size=0, seed=42)

    with pytest.raises(ValueError):
        split_dataset(records, test_size=1, seed=42)

    with pytest.raises(ValueError):
        split_dataset(records, test_size=-0.1, seed=42)

    with pytest.raises(ValueError):
        split_dataset(records, test_size=1.5, seed=42)
