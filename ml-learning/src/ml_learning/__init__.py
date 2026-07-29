"""Machine Learning package with Supervised and Unsupervised learning submodules."""

from ml_learning.supervised.gradient_descent import GradientDescentOptimizer
from ml_learning.supervised.linear_regression import LinearRegression
from ml_learning.supervised.metrics import mean_squared_error, r2_score
from ml_learning.unsupervised.kmeans import KMeans
from ml_learning.unsupervised.pca import PCA

__all__ = [
    "LinearRegression",
    "GradientDescentOptimizer",
    "mean_squared_error",
    "r2_score",
    "KMeans",
    "PCA",
]
