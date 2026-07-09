from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


def build_baseline_pipeline() -> Pipeline:
    pipeline = Pipeline(
        steps=[
            ("tfidf", TfidfVectorizer()),
            ("classifier", LogisticRegression(max_iter=1000)),
        ]
    )

    return pipeline


def train_baseline_classifier(texts: list[str], labels: list[str]) -> Pipeline:
    pipeline = build_baseline_pipeline()

    pipeline.fit(texts, labels)

    return pipeline
