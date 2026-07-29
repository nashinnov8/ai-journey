"""Supervised Learning: Linear Regression algorithm starter template.

Implement Ordinary Least Squares (OLS) closed-form solution.
"""

from typing import Self

import numpy as np


class LinearRegression:
    """Ordinary Least Squares Linear Regression.

    Attributes:
        fit_intercept: Whether to calculate the intercept for this model.
        weights: Model weights vector (includes bias if fit_intercept is True).
    """

    def __init__(self, fit_intercept: bool = True) -> None:
        self.fit_intercept = fit_intercept
        self.weights: np.ndarray | None = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> Self:
        """Fit linear model using OLS closed-form equation: theta = (X^T X)^(-1) X^T y."""
        # TODO: Implement Ordinary Least Squares analytical solution
        raise NotImplementedError("Implement OLS linear regression fit equation here!")

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict target values using the linear model."""
        # TODO: Implement prediction logic
        raise NotImplementedError("Implement prediction logic here!")

    @property
    def coef_(self) -> np.ndarray:
        """Get coefficients (excluding intercept if fit_intercept is True)."""
        if self.weights is None:
            raise ValueError("Model is not fitted yet.")
        return self.weights[1:].ravel() if self.fit_intercept else self.weights.ravel()

    @property
    def intercept_(self) -> float:
        """Get intercept value."""
        if self.weights is None:
            raise ValueError("Model is not fitted yet.")
        return float(self.weights[0, 0]) if self.fit_intercept else 0.0
