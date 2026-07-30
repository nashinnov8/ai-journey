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
        random_indices = np.random.choice(X.shape[0], self.n_clusters, replace=False)

        self.centroids = X[random_indices]

        for _ in range(self.max_iter):
            label = self.predict(X)

            # Lưu lại tâm cũ để so sánh
            old_centroids = self.centroids.copy()

            # Cập nhật tâm cụm
            for j in range(self.n_clusters):
                # lấy ra điểm thuộc centroids đó
                points_in_centroids = X[label == j]

                if len(points_in_centroids) > 0:
                    self.centroids[j] = np.mean(points_in_centroids, axis=0)

            if np.allclose(self.centroids, old_centroids, atol=self.tol):
                break
        return self

    def predict(self, X: np.ndarray) -> np.ndarray:
        """Predict the closest cluster for each sample in X."""
        # TODO: Implement nearest centroid assignment logic
        if self.centroids is None:
            raise ValueError("Model must be trained")

        X_newaxis = X[:, np.newaxis]
        distances = np.linalg.norm(X_newaxis - self.centroids, axis=2)
        return np.argmin(distances, axis=1)
