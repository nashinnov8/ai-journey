# 🚀 AI Journey: Master Machine Learning & AI Engineering

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Package Manager](https://img.shields.io/badge/uv-Fast%20Python%20Tooling-de5c8e.svg)](https://github.com/astral-sh/uv)
[![Code Style](https://img.shields.io/badge/code%20style-Ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Type Checker](https://img.shields.io/badge/type%20checker-BasedPyright-brightgreen.svg)](https://github.com/detachhead/basedpyright)

Welcome to **AI Journey**, a production-grade, monorepo-styled repository designed for long-term mastery of Artificial Intelligence, Machine Learning, Deep Learning, Large Language Models (LLMs), Computer Vision, NLP, Reinforcement Learning, and MLOps.

---

## 🎯 Learning Philosophy & Core Principles

This repository follows modern, high-grade Python software engineering principles built for scalability and long-term maintainability:

1. **Separation of Exploration & Production**:
   - **Notebooks (`notebooks/`)**: Used exclusively for quick experimentation, interactive visualizations, and exploratory data analysis (EDA).
   - **Source Code (`src/`)**: Clean, vectorized, fully type-annotated, modular Python packages built for reuse and testing. Notebooks import from `src/` rather than defining heavy algorithms inline.
2. **Subproject Isolation (`uv`)**:
   - Each domain subproject operates as an independent Python package with its own `pyproject.toml`, `uv.lock`, and isolated `.venv` managed strictly by **uv**.
3. **Single Git Authority**:
   - Monorepo structure anchored by a single root `.git`. No subproject contains nested `.git` folders.
4. **Strict Quality Gates**:
   - 100% type safety with **BasedPyright** in standard mode.
   - Ultra-fast linting and formatting via **Ruff** (Black-compatible style).
   - Standardized `pathlib.Path` usages for OS-agnostic file handling.

---

## 📂 Repository Taxonomy

```
ai-journey/
│
├── README.md                 # Root documentation, roadmap, & execution guides
├── .gitignore                # Global multi-platform & toolchain ignore configurations
├── .vscode/                  # Workspace settings for Ruff, BasedPyright, & Jupyter
│
├── math/                     # Mathematical foundations of AI/ML
├── ml-learning/              # Classical Machine Learning (Supervised, Unsupervised, Algorithms from Scratch)
├── deep-learning/            # Neural Networks, PyTorch/TensorFlow, Autograd, Model Architectures
├── llm/                      # Large Language Models, Fine-tuning, RAG, Quantization, Transformer Scratch
├── mlops/                    # Experiment tracking, Pipeline Orchestration, Model Serving, Monitoring, CI/CD
├── reinforcement-learning/   # MDPs, Q-Learning, Policy Gradients (PPO/SAC), Gymnasium
├── computer-vision/          # OpenCV, Object Detection, Segmentation, Generative Models, ViT
├── nlp/                      # Text Preprocessing, Embeddings, Sequence Models, Attention Mechanisms
├── experiments/              # Sandbox, quick proof-of-concept projects, & performance benchmarks
├── shared/                   # Shared cross-cutting Python utilities library (`ai_journey_shared`)
└── docs/                     # Technical writeups, paper summaries, & Architectural Decision Records (ADRs)
```

### Module Responsibilities

| Directory | Scope & Purpose | Key Frameworks & Topics |
| :--- | :--- | :--- |
| **`math/`** | Core mathematical algorithms implemented from scratch. | Linear Algebra, Vector Calculus, Probability & Stats, Optimization |
| **`ml-learning/`** | Classical ML algorithms, feature engineering, and metrics. | Scikit-Learn, NumPy, Decision Trees, Gradient Descent, Clustering |
| **`deep-learning/`** | Neural network architectures & autograd engines. | PyTorch, Backpropagation, CNNs, ResNets, Transformers |
| **`llm/`** | LLM development, fine-tuning, RAG, and inference engines. | Hugging Face, PEFT (LoRA), vLLM, Ollama, LangChain, LlamaIndex |
| **`mlops/`** | Deployments, pipelines, model governance, and monitoring. | MLflow, W&B, FastAPI, Docker, Triton, Prefect, DVC |
| **`reinforcement-learning/`** | Agent-environment interactions & policy learning. | Gymnasium, DQN, REINFORCE, PPO, SAC |
| **`computer-vision/`** | Image processing, feature extraction, & generative vision. | OpenCV, YOLO, U-Net, Diffusion Models, ViT |
| **`nlp/`** | Text analysis, embeddings, sequence modeling, & attention. | NLTK, SpaCy, Word2Vec, Transformer Encoder/Decoder |
| **`experiments/`** | Quick benchmarks, algorithm comparisons, and prototypes. | Prototyping, Profiling, Comparative Benchmarking |
| **`shared/`** | Reusable shared code across all subprojects. | Custom Plotting, Data Generators, Common Protocols |
| **`docs/`** | In-depth theory notes, ADRs, paper summaries. | Markdown, LaTeX Math, Architecture Diagrams |

---

## 🛠️ Tech Stack & Tooling

- **Language**: Python 3.13+
- **Environment & Dependency Manager**: `uv`
- **Linter & Formatter**: `ruff`
- **Static Type Checker**: `basedpyright`
- **Interactive Computing**: Jupyter Notebooks
- **Primary Data Science & ML Stack**: `numpy`, `pandas`, `scipy`, `scikit-learn`, `matplotlib`, `seaborn`
- **Deep Learning Stack**: `torch`, `torchvision`, `torchaudio`, `transformers`, `accelerate`

---

## ⚡ Quick Start & Development Workflow

### 1. Prerequisites

Ensure `uv` is installed on your system.

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Working in a Subproject

Navigate to any subproject (e.g., `ml-learning/`) and synchronize the environment:

```bash
cd ml-learning

# Synchronize dependencies and create virtual environment
uv sync

# Run tests using the subproject environment
uv run pytest

# Launch Jupyter Lab / Notebook
uv run jupyter lab
```

### 3. Adding Dependencies

```bash
# Add a package to the active subproject
uv add matplotlib

# Add a development dependency
uv add --dev pytest ruff basedpyright
```

---

## 🗺️ Master Learning Roadmap & Progress Checklist

### Phase 1: Foundations & Classical Machine Learning
- [ ] Math Foundations (Linear Algebra, Multi-variable Calculus, Probability)
- [x] Linear & Logistic Regression from Scratch
- [ ] Gradient Descent Variants (Batch, Mini-batch, SGD, Adam)
- [ ] Decision Trees, Random Forests & Gradient Boosted Trees (XGBoost, LightGBM)
- [ ] Support Vector Machines & Kernel Methods
- [ ] Unsupervised Learning (K-Means, PCA, t-SNE, Hierarchical Clustering)
- [ ] Model Evaluation, Cross-Validation, & Hyperparameter Tuning

### Phase 2: Deep Learning & Neural Architectures
- [ ] Custom Autograd Engine & Backpropagation from Scratch
- [ ] Multi-Layer Perceptrons (MLPs) & Regularization (Dropout, BatchNorm)
- [ ] Convolutional Neural Networks (CNNs, ResNet, EfficientNet)
- [ ] Recurrent Neural Networks & Attention Mechanisms (LSTM, GRU, Bahdanau Attention)
- [ ] Transformer Architecture from Scratch (Multi-Head Self-Attention, Positional Encoding)

### Phase 3: Specialized Domains & Advanced AI
- [ ] **LLM**: Tokenization (BPE), Decoder-only Transformers, LoRA/QLoRA Fine-tuning, RAG
- [ ] **Computer Vision**: Object Detection (YOLO), Semantic Segmentation (U-Net), Diffusion Models
- [ ] **NLP**: Embeddings, Intent Classification, Sequence-to-Sequence Translation
- [ ] **Reinforcement Learning**: Q-Learning, Deep Q-Networks (DQN), PPO, Gymnasium

### Phase 4: MLOps & Production Engineering
- [ ] Experiment Tracking with MLflow & Weights & Biases
- [ ] Data Version Control (DVC) & Reproducible Pipelines
- [ ] REST API & High-Performance Inference (FastAPI, TorchServe, Triton)
- [ ] Containerization (Docker) & CI/CD for ML Systems
- [ ] Model Monitoring, Drift Detection, & Feature Stores

---

## 📜 License & Portfolio Usage

This repository is maintained as an open-source engineering portfolio showcasing scalable, production-ready AI/ML implementations. Feel free to explore, clone, and adapt!
