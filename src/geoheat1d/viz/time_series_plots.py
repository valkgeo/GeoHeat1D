<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
"""Planned time-series plotting helpers for future richer visual diagnostics."""
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
"""Time-series plotting helpers for selected contact-distance tracks."""

import matplotlib.pyplot as plt
import numpy as np


def plot_temperature_time_series_by_distance(
    result,
    distances_m: list[float],
):
    """Plot temperature vs time for selected nearest-contact distances."""
    fig, ax = plt.subplots()

    for d in distances_m:
        idx = int(np.argmin(np.abs(result.distance_from_contact_m - d)))
        nearest_d = result.distance_from_contact_m[idx]
        ax.plot(result.time_s, result.temperature_c[idx, :], label=f"d={nearest_d:.1f} m")

    ax.set_xlabel("Time since emplacement (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Thermal evolution at selected distances from contact")
    ax.legend()
    return fig, ax
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
