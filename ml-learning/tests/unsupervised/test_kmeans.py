"""Automated unit test suite for Unsupervised K-Means implementation."""

from ml_learning.unsupervised.kmeans import KMeans
import numpy as np


def test_kmeans_basic_clustering() -> None:
    """Test that KMeans correctly separates 2 clearly distinct clusters."""
    np.random.seed(42)
    cluster1 = np.random.randn(20, 2) + np.array([0, 0])
    cluster2 = np.random.randn(20, 2) + np.array([10, 10])
    X = np.vstack([cluster1, cluster2])

    kmeans = KMeans(n_clusters=2)
    kmeans.fit(X)
    labels = kmeans.predict(X)

    assert len(np.unique(labels)) == 2
