from packages.shared.datasets.schemas import (
    DatasetLabel,
    ProcessedArticleRecord,
    RawArticleRecord,
)


def normalize_whitespace(text: str) -> str:
    return " ".join(text.split())


def build_processed_text(title: str, content: str) -> str:
    return normalize_whitespace(f"{title} {content}")


def normalize_label(label: str) -> DatasetLabel:
    normalized_label = label.strip().lower()

    if normalized_label == "fake":
        return "fake"

    if normalized_label == "real":
        return "real"

    raise ValueError("Label must be 'fake' or 'real'")


def preprocess_raw_article(article_record: RawArticleRecord) -> ProcessedArticleRecord:
    text = build_processed_text(article_record.title, article_record.content)
    label = normalize_label(article_record.label)

    return ProcessedArticleRecord(
        text=text,
        label=label,
        source=article_record.source,
        url=article_record.url,
    )


def preprocess_raw_articles(
    articles: list[RawArticleRecord],
) -> list[ProcessedArticleRecord]:
    return [
        preprocess_raw_article(raw_article_record) for raw_article_record in articles
    ]
