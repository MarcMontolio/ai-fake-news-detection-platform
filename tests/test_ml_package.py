from packages.shared import ml


def test_ml_package_imports_successfully() -> None:
    ml_package = ml

    assert ml_package is not None


def test_ml_package_exports_training_functions() -> None:
    build_baseline_pipeline = ml.build_baseline_pipeline

    train_baseline_classifier = ml.train_baseline_classifier

    assert callable(build_baseline_pipeline)
    assert callable(train_baseline_classifier)
