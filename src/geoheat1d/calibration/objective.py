"""Simple observational constraints and misfit functions."""

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class TemperatureObservation:
    """Single temperature constraint at depth and time."""

    depth_m: float
    time_s: float
    temperature_c: float
    sigma_c: float = 10.0


def weighted_l2_misfit(result, observations: list[TemperatureObservation]) -> float:
    """Compute weighted L2 misfit using nearest neighbor sampling."""
    total = 0.0
    for obs in observations:
        iz = int(np.argmin(np.abs(result.depth_m - obs.depth_m)))
        it = int(np.argmin(np.abs(result.time_s - obs.time_s)))
        pred = result.temperature_c[iz, it]
        residual = (pred - obs.temperature_c) / obs.sigma_c
        total += residual**2
    return float(total)
