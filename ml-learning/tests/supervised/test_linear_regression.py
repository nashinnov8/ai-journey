"""Automated unit test suite for Supervised Linear Regression implementation."""

from ml_learning.supervised.linear_regression import LinearRegression
from ml_learning.supervised.metrics import mean_squared_error, r2_score
import numpy as np
import pytest


@pytest.mark.skip(reason="Implement LinearRegression.fit() and predict() first!")
def test_linear_regression_perfect_fit() -> None:
    """Test that LinearRegression accurately recovers known linear equation y = 3x + 5."""
    np.random.seed(42)
    X = np.linspace(0, 10, 50).reshape(-1, 1)
    y = 3.0 * X.ravel() + 5.0

    model = LinearRegression(fit_intercept=True)
    model.fit(X, y)

    predictions = model.predict(X)
    assert pytest.approx(model.intercept_, abs=1e-5) == 5.0
    assert pytest.approx(model.coef_[0], abs=1e-5) == 3.0
    assert pytest.approx(r2_score(y, predictions), abs=1e-5) == 1.0


def test_metrics_calculation() -> None:
    """Test MSE and R2 metrics against known baseline values."""
    y_true = np.array([1.0, 2.0, 3.0, 4.0])
    y_pred = np.array([1.1, 1.9, 3.2, 3.8])

    mse = mean_squared_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)

    assert mse > 0.0
    assert 0.9 < r2 <= 1.0
