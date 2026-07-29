"""Supervised Learning: Gradient Descent optimization algorithms starter template."""

from collections.abc import Callable
from dataclasses import dataclass

import numpy as np


@dataclass
class OptimizationResult:
    """Dataclass holding optimization trajectory and final parameters."""

    weights: np.ndarray
    history: list[float]
    n_iterations: int


class GradientDescentOptimizer:
    """Batch Gradient Descent Optimizer starter template."""

    def __init__(
        self,
        learning_rate: float = 0.01,
        max_iterations: int = 1000,
        tolerance: float = 1e-6,
    ) -> None:
        self.learning_rate = learning_rate
        self.max_iterations = max_iterations
        self.tolerance = tolerance

    def optimize(
        self,
        X: np.ndarray,
        y: np.ndarray,
        initial_weights: np.ndarray | None = None,
        cost_fn: Callable[[np.ndarray, np.ndarray, np.ndarray], float] | None = None,
    ) -> OptimizationResult:
        """Run batch gradient descent to minimize Mean Squared Error."""
        # TODO: Implement batch gradient descent loop
        raise NotImplementedError("Implement gradient descent update loop here!")
