from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)


def evaluate_predictions(
    true_labels: list[str], predicted_labels: list[str]
) -> dict[str, float]:
    accuracy_value = accuracy_score(true_labels, predicted_labels)
    precision_value = precision_score(
        true_labels, predicted_labels, average="macro", zero_division=0
    )
    recall_value = recall_score(
        true_labels, predicted_labels, average="macro", zero_division=0
    )
    f1_value = f1_score(true_labels, predicted_labels, average="macro", zero_division=0)

    metrics = {
        "accuracy": float(accuracy_value),
        "precision": float(precision_value),
        "recall": float(recall_value),
        "f1": float(f1_value),
    }

    return metrics


def build_confusion_matrix(
    true_labels: list[str], predicted_labels: list[str]
) -> list[list[int]]:
    matrix = confusion_matrix(true_labels, predicted_labels, labels=["fake", "real"])

    matrix_list = matrix.tolist()

    return matrix_list
