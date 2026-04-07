"""Time-series plotting helpers for selected contact-distance tracks."""

from collections.abc import Sequence

import matplotlib.pyplot as plt
import numpy as np


def plot_temperature_time_series_by_distance(
    result,
    distances_m: Sequence[float],
):
    """Plot temperature vs time for selected nearest-contact distances."""
    fig, ax = plt.subplots()

    for requested_distance in distances_m:
        idx = int(np.argmin(np.abs(result.distance_from_contact_m - requested_distance)))
        nearest_distance = result.distance_from_contact_m[idx]
        ax.plot(result.time_s, result.temperature_c[idx, :], label=f"d={nearest_distance:.1f} m")

    ax.set_xlabel("Time since emplacement (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Thermal evolution at selected distances from contact")
    ax.legend()
    return fig, ax
