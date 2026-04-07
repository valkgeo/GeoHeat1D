"""Derived thermal metrics from temperature fields."""

import numpy as np


def peak_temperature_by_depth(result):
    """Peak temperature at each depth across all modeled times."""
    return np.max(result.temperature_c, axis=1)


<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
def peak_temperature_by_distance_from_contact(result) -> tuple[np.ndarray, np.ndarray]:
    """Peak temperature summarized by nearest-contact distance.

    Returns sorted unique distances and the corresponding peak temperature at each
<<<<<<< ours
    distance (max over depths sharing that distance).
=======
    distance (max over depths sharing that same distance from contact).
>>>>>>> theirs
    """
    distances = result.distance_from_contact_m
    peaks = peak_temperature_by_depth(result)

    unique_distances = np.unique(distances)
    peak_by_distance = np.zeros(unique_distances.shape, dtype=float)
<<<<<<< ours
    for i, d in enumerate(unique_distances):
        peak_by_distance[i] = np.max(peaks[np.isclose(distances, d)])
=======
    for i, distance in enumerate(unique_distances):
        peak_by_distance[i] = np.max(peaks[np.isclose(distances, distance)])
>>>>>>> theirs

    return unique_distances, peak_by_distance


<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
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
