"""Unsupervised Learning: K-Means Clustering algorithm starter template."""

from typing import Self

import numpy as np


class KMeans:
    """K-Means Clustering algorithm.

    Attributes:
        n_clusters: Number of clusters (k).
        max_iter: Maximum number of iterations.
        centroids: Cluster centroids matrix of shape (k, n_features).
    """

    def __init__(self, n_clusters: int = 3, max_iter: int = 300, tol: float = 1e-4) -> None:
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol
        self.centroids: np.ndarray | None = None

    def fit(self, X: np.ndarray) -> Self:
        """Compute K-means clustering centroids."""
        # TODO: Implement K-Means clustering iterative centroid optimization
        raise NotImplementedError("Implement K-Means fit algorithm here!")

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict the closest cluster for each sample in X."""
        # TODO: Implement nearest centroid assignment logic
        raise NotImplementedError("Implement K-Means predict logic here!")
