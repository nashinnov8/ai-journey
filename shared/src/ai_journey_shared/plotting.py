"""Plotting and visualization helpers with pathlib integration."""

from pathlib import Path

import matplotlib.pyplot as plt


def setup_plot_style() -> None:
    """Configure modern plot aesthetics for Matplotlib charts."""
    plt.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.size": 11,
            "axes.titlesize": 14,
            "axes.labelsize": 12,
            "axes.edgecolor": "#CCCCCC",
            "axes.linewidth": 0.8,
            "grid.color": "#E5E5E5",
            "grid.linestyle": "--",
            "grid.alpha": 0.7,
            "figure.autolayout": True,
        }
    )


def save_figure(
    fig: plt.Figure,
    output_path: Path,
    dpi: int = 300,
    transparent: bool = False,
) -> Path:
    """Save matplotlib figure to specified pathlib Path, ensuring directory exists.

    Args:
        fig: The matplotlib Figure object to save.
        output_path: Destination path (Path object).
        dpi: Dots per inch resolution.
        transparent: Whether background is transparent.

    Returns:
        The resolved Path where figure was saved.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_path, dpi=dpi, transparent=transparent, bbox_inches="tight")
    plt.close(fig)
    return output_path
