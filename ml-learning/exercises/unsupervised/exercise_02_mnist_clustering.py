"""Exercise 02: Unsupervised MNIST Digit Clustering Challenge.

Goal:
1. Load MNIST Digits dataset (1,797 samples, 64 features).
2. Apply K-Means clustering with K = 10 without using labels.
3. Reshape and plot the 10 learned centroids to visualize digit clusters.
"""

import sys
from pathlib import Path

import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.metrics import silhouette_score

# Set root path for imports
current_dir = Path.cwd()
ml_learning_dir = (
    current_dir.parent.parent
    if current_dir.name in ["supervised", "unsupervised"]
    else current_dir.parent
)
src_dir = ml_learning_dir / "src"
if str(src_dir) not in sys.path:
    sys.path.append(str(src_dir))

from ai_journey_shared.plotting import save_figure, setup_plot_style  # noqa: E402
from ai_journey_shared.utils import set_seed  # noqa: E402

from ml_learning.unsupervised.kmeans import KMeans  # noqa: E402


def main() -> None:
    setup_plot_style()
    set_seed(42)

    # 1. Load MNIST dataset
    digits = load_digits()
    X_raw = digits.data

    print(f"Loaded {X_raw.shape[0]} MNIST digit images of shape {X_raw.shape[1]} features.")

    # 2. Normalize features to [0, 1]
    X_scaled = X_raw / 16.0

    # 3. Fit K-Means
    kmeans = KMeans(n_clusters=10, max_iter=300, tol=1e-4)
    kmeans.fit(X_scaled)
    labels = kmeans.predict(X_scaled)

    # 4. Evaluate Silhouette Score
    score = silhouette_score(X_scaled, labels)
    print(f"Clustering Silhouette Score: {score:.4f}")

    # 5. Visualize Centroid Images
    fig, axes = plt.subplots(2, 5, figsize=(10, 5))
    for k, ax in enumerate(axes.flat):
        if kmeans.centroids is not None:
            centroid_img = kmeans.centroids[k].reshape(8, 8)
            ax.imshow(centroid_img, cmap="binary")
            ax.set_title(f"Cluster #{k}")
            ax.axis("off")

    plt.suptitle("K-Means Learned Digit Centroids", fontsize=14)
    fig_path = ml_learning_dir / "figures" / "mnist_exercise_centroids.png"
    save_figure(fig, fig_path)
    print(f"Saved centroids plot to {fig_path}")


if __name__ == "__main__":
    main()
