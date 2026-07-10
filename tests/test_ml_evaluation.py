import pytest

pytest.importorskip("sklearn")

from packages.shared.ml.evaluation import build_confusion_matrix, evaluate_predictions


def test_evaluate_prediction_returns_expected_metric_keys() -> None:
    true_labels = ["fake", "real", "fake", "real"]
    predicted_labels = ["fake", "real", "real", "real"]

    metrics = evaluate_predictions(true_labels, predicted_labels)

    assert set(metrics) == {"accuracy", "precision", "recall", "f1"}


def test_evaluate_prediction_returns_metric_values_between_zero_and_one() -> None:
    true_labels = ["fake", "real", "fake", "real"]
    predicted_labels = ["fake", "real", "real", "real"]

    metrics = evaluate_predictions(true_labels, predicted_labels)

    for metric_value in metrics.values():
        assert isinstance(metric_value, float)
        assert metric_value >= 0.0
        assert metric_value <= 1.0


def test_evaluate_prediction_returns_one_for_perfect_predictions() -> None:
    true_labels = ["fake", "real", "fake", "real"]
    predicted_labels = ["fake", "real", "fake", "real"]

    metrics = evaluate_predictions(true_labels, predicted_labels)

    assert metrics["accuracy"] == 1.0
    assert metrics["precision"] == 1.0
    assert metrics["recall"] == 1 - 0
    assert metrics["f1"] == 1.0


def test_build_confusion_matrix_returns_expected_matrix() -> None:
    true_labels = ["fake", "fake", "real", "real"]
    predicted_labels = ["fake", "real", "fake", "real"]

    matrix = build_confusion_matrix(true_labels, predicted_labels)

    assert matrix == [[1, 1], [1, 1]]
