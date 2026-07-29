"""General software engineering & reproducibility utilities."""

import random

import numpy as np


def set_seed(seed: int = 42) -> None:
    """Set global random seeds across stdlib random and NumPy for reproducibility.

    Args:
        seed: The integer seed value.
    """
    random.seed(seed)
    np.random.seed(seed)
