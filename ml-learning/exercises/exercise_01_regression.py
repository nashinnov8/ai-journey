"""Exercise 01: Implement Ridge Regression (L2 Regularization) from Scratch.

Goal: Extend the OLS Linear Regression formula:
    theta = (X^T X + lambda * I)^(-1) X^T y
"""

from typing import Self

import numpy as np


class RidgeRegressionScratch:
    """L2 Regularized Linear Regression from scratch."""

    def __init__(self, alpha: float = 1.0, fit_intercept: bool = True) -> None:
        self.alpha = alpha
        self.fit_intercept = fit_intercept
        self.weights: np.ndarray | None = None

    def fit(self, X: np.ndarray, y: np.ndarray) -> Self:
        """Fit Ridge Regression model using closed-form analytical solution."""
        X_mat = np.asarray(X, dtype=np.float64)
        y_vec = np.asarray(y, dtype=np.float64).reshape(-1, 1)

        if self.fit_intercept:
            ones = np.ones((X_mat.shape[0], 1), dtype=np.float64)
            X_mat = np.hstack((ones, X_mat))

        n_features = X_mat.shape[1]
        # L2 Penalty matrix identity_mat, without penalizing intercept (w_0)
        identity_mat = np.eye(n_features, dtype=np.float64)
        if self.fit_intercept:
            identity_mat[0, 0] = 0.0

        # Analytical solution: (X^T X + alpha * I)^(-1) X^T y
        a_mat = X_mat.T @ X_mat + self.alpha * identity_mat
        self.weights = np.linalg.solve(a_mat, X_mat.T @ y_vec)
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Make predictions on new data."""
        if self.weights is None:
            raise ValueError("Model is not fitted yet.")

        X_mat = np.asarray(X, dtype=np.float64)
        if self.fit_intercept:
            ones = np.ones((X_mat.shape[0], 1), dtype=np.float64)
            X_mat = np.hstack((ones, X_mat))

        return (X_mat @ self.weights).ravel()
