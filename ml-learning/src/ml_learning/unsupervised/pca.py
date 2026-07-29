"""Unsupervised Learning: Principal Component Analysis (PCA) starter template."""

from typing import Self

import numpy as np


class PCA:
    """Principal Component Analysis (PCA) for dimensionality reduction.

    Attributes:
        n_components: Number of principal components to keep.
        components_: Principal axes in feature space.
        explained_variance_: Amount of variance explained by each selected component.
    """

    def __init__(self, n_components: int = 2) -> None:
        self.n_components = n_components
        self.components_: np.ndarray | None = None
        self.explained_variance_: np.ndarray | None = None

    def fit(self, X: np.ndarray) -> Self:
        """Fit PCA model using Covariance Matrix Eigendecomposition or SVD."""
        # TODO: Implement PCA fit logic (Mean centering -> Covariance -> Eigen / SVD)
        raise NotImplementedError("Implement PCA fit algorithm here!")

    def transform(self, X: np.ndarray) -> np.ndarray:
        """Apply dimensionality reduction to X."""
        # TODO: Project X onto principal components
        raise NotImplementedError("Implement PCA transform logic here!")
