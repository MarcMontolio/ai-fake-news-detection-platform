import argparse
from pathlib import Path

from packages.shared.datasets import (
    load_raw_articles_from_csv,
    preprocess_raw_articles,
    split_dataset,
    write_processed_articles_to_csv,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Prepare train and test CSV datasets from a raw labelled news dataset."
        )
    )

    parser.add_argument(
        "--input-csv",
        required=True,
        help="Path to the raw labelled input CSV file.",
    )

    parser.add_argument(
        "--output-dir",
        required=True,
        help=(
            "Directory where the processed train.csv and test.csv files "
            "will be written."
        ),
    )

    parser.add_argument(
        "--test-size",
        type=float,
        default=0.2,
        help="Fraction of records to use for the test split. Default: 0.2.",
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Random seed used to create a reproducible train/test split. Default: 42.",
    )

    return parser.parse_args()


def prepare_dataset(
    input_csv: str | Path,
    output_dir: str | Path,
    test_size: float = 0.2,
    seed: int = 42,
) -> None:
    raw_records = load_raw_articles_from_csv(input_csv)

    processed_records = preprocess_raw_articles(raw_records)

    train_records, test_records = split_dataset(
        records=processed_records,
        test_size=test_size,
        seed=seed,
    )

    output_dir_path = Path(output_dir)

    write_processed_articles_to_csv(train_records, output_dir_path / "train.csv")
    write_processed_articles_to_csv(test_records, output_dir_path / "test.csv")


def main() -> None:
    args = parse_args()

    prepare_dataset(
        input_csv=args.input_csv,
        output_dir=args.output_dir,
        test_size=args.test_size,
        seed=args.seed,
    )


if __name__ == "__main__":
    main()
