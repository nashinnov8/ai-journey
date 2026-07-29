# 📊 Machine Learning Subproject (`ml-learning`)

This subproject hosts classical Machine Learning algorithms, statistical modeling techniques, exploratory Jupyter notebooks, reusable `src/` modules, datasets, generated figures, and hands-on exercises, organized strictly by paradigm: **Supervised Learning** and **Unsupervised Learning**.

---

## 📁 Directory Taxonomy & Paradigm Split

```
ml-learning/
│
├── notebooks/
│   ├── supervised/              # Supervised Learning Notebooks
│   │   └── 01_linear_regression.ipynb
│   └── unsupervised/            # Unsupervised Learning Notebooks
│       └── 01_kmeans.ipynb
│
├── src/ml_learning/
│   ├── supervised/              # Supervised Algorithms (Regression, Classification)
│   │   ├── linear_regression.py
│   │   ├── gradient_descent.py
│   │   └── metrics.py
│   └── unsupervised/            # Unsupervised Algorithms (Clustering, Dimensionality Reduction)
│       ├── kmeans.py
│       └── pca.py
│
├── exercises/
│   ├── supervised/
│   └── unsupervised/
│
├── tests/
│   ├── supervised/
│   │   └── test_linear_regression.py
│   └── unsupervised/
│       └── test_kmeans.py
│
├── datasets/                    # Datasets & synthetic data generators
├── figures/                     # Output plots & visualizations saved by code/notebooks
├── pyproject.toml               # Modern uv package & dependency configuration
└── README.md
```

---

## 🚀 Environment Setup & Commands

Run all commands from within the `ml-learning/` directory using `uv`:

```bash
# 1. Install & sync dependencies in isolated virtual environment
uv sync

# 2. Run unit tests
uv run pytest

# 3. Run Ruff linter & type checker
uv run ruff check src/
uv run basedpyright src/

# 4. Launch Jupyter Notebook / Lab
uv run jupyter lab
```
