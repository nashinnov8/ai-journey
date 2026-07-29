# 🛠️ `ai-journey-shared`

Shared utility package providing cross-cutting functionalities across all subprojects in `ai-journey`.

## Features

- **Plotting & Visualization**: Standardized themes, loss curves, confusion matrices, and figure saving helpers using `pathlib`.
- **Data & Seed Management**: Helper functions for reproducibility (setting random seeds across `numpy`, `torch`, `random`).
- **Performance Profiling**: Execution time decorators and memory usage trackers.

## Installation / Usage in Subprojects

Inside any subproject (e.g. `ml-learning`), you can depend on this shared library in editable mode via `pyproject.toml`:

```toml
[project]
dependencies = [
    "ai-journey-shared",
]

[tool.uv.sources]
ai-journey-shared = { path = "../shared", editable = true }
```
