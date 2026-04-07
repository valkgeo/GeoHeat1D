"""Structured result containers for forward-model output."""

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ThermalResult:
    """Container for a full depth-time temperature field."""

    depth_m: np.ndarray
    time_s: np.ndarray
    temperature_c: np.ndarray
    scenario: object
