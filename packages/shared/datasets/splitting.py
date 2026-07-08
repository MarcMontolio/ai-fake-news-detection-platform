import random

from packages.shared.datasets.schemas import ProcessedArticleRecord


def validate_test_size(test_size: float) -> None:
    if test_size <= 0 or test_size >= 1:
        raise ValueError("Test size must be greater than 0 and less than l")


def split_dataset(
    records: list[ProcessedArticleRecord], test_size: float = 0.2, seed: int = 42
) -> tuple[list[ProcessedArticleRecord], list[ProcessedArticleRecord]]:
    validate_test_size(test_size)

    if len(records) < 2:
        msg = "At least 2 records are required to create a train/test split"
        raise ValueError(msg)

    shuffled_records = records.copy()

    random_generator = random.Random(seed)
    random_generator.shuffle(shuffled_records)

    total_records = len(shuffled_records)

    test_count = int(total_records * test_size)
    test_count = max(1, test_count)
    test_count = min(test_count, total_records - 1)

    test_records = shuffled_records[:test_count]

    train_records = shuffled_records[test_count:]

    return train_records, test_records
