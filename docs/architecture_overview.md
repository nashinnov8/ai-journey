# Architectural Decision Record (ADR-001): Repository Structure & Toolchain Selection

## Context
The goal is to construct a production-ready, scalable AI learning repository (`ai-journey`) suitable for multi-year progression spanning Machine Learning, Deep Learning, LLMs, Computer Vision, NLP, Reinforcement Learning, and MLOps.

## Decisions

### 1. Single Root Git Authority
- **Decision**: Only one Git repository is maintained at root (`ai-journey/.git`). Subprojects must not contain nested `.git` folders.
- **Rationale**: Prevents accidental detached git state, simplifies multi-project tracking, and conforms to monorepo standards.

### 2. Dependency Management via `uv`
- **Decision**: Exclusively use `uv` for virtual environment management and dependency locking. `pip`, `pipenv`, `poetry`, `conda`, and `virtualenv` are prohibited.
- **Rationale**: `uv` provides 10-100x faster package installation, native lockfile reproducibility (`uv.lock`), and effortless support for isolated subproject environments.

### 3. Separation of Concerns (Notebooks vs. Source)
- **Decision**: Exploratory code resides in `notebooks/`. Reusable logic belongs in `src/` modules under standard Python package layout (`src/module_name/`).
- **Rationale**: Avoids bloated notebooks with unmaintainable code, promotes modular software design, enables automated unit testing with `pytest`, and supports full static analysis via BasedPyright.

### 4. Code Quality & Type Safety
- **Decision**: Target Python 3.13+, standard type annotations everywhere, formatting and linting via Ruff, and type checking via BasedPyright in standard mode.
- **Rationale**: Ensures code meets enterprise production standards suitable for a professional public portfolio.
