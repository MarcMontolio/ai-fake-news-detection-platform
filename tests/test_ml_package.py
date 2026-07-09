from packages.shared import ml


def test_ml_package_imports_successfully() -> None:
    ml_package = ml

    assert ml_package is not None
