"""Validation helpers for model inputs."""

import numpy as np


def ensure_1d_array(name: str, values) -> np.ndarray:
    """Return values as 1D numpy array and raise if incompatible."""
    arr = np.asarray(values, dtype=float)
    if arr.ndim != 1:
        raise ValueError(f"{name} must be a 1D array")
    return arr
