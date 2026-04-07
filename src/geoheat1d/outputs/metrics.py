"""Derived thermal metrics from temperature fields."""

import numpy as np


def peak_temperature_by_depth(result):
    """Peak temperature at each depth across all modeled times."""
    return np.max(result.temperature_c, axis=1)


def max_temperature(result) -> float:
    """Single global maximum temperature over depth and time."""
    return float(np.max(result.temperature_c))


def time_above_temperature(result, threshold_c: float) -> np.ndarray:
    """Total modeled duration above threshold at each depth (seconds)."""
    above = result.temperature_c >= threshold_c
    dt = np.diff(result.time_s)
    if dt.size == 0:
        return np.zeros(result.depth_m.shape, dtype=float)
    totals = np.zeros(result.depth_m.shape, dtype=float)
    for i in range(result.depth_m.size):
        totals[i] = np.sum(dt * above[i, :-1])
    return totals
