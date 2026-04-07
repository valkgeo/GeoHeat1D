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

=======
"""Time-series plotting helpers for selected contact-distance tracks."""

from collections.abc import Sequence

>>>>>>> theirs
import matplotlib.pyplot as plt
import numpy as np


def plot_temperature_time_series_by_distance(
    result,
<<<<<<< ours
    distances_m: list[float],
=======
    distances_m: Sequence[float],
>>>>>>> theirs
):
    """Plot temperature vs time for selected nearest-contact distances."""
    fig, ax = plt.subplots()

<<<<<<< ours
    for d in distances_m:
        idx = int(np.argmin(np.abs(result.distance_from_contact_m - d)))
        nearest_d = result.distance_from_contact_m[idx]
        ax.plot(result.time_s, result.temperature_c[idx, :], label=f"d={nearest_d:.1f} m")
=======
    for requested_distance in distances_m:
        idx = int(np.argmin(np.abs(result.distance_from_contact_m - requested_distance)))
        nearest_distance = result.distance_from_contact_m[idx]
        ax.plot(result.time_s, result.temperature_c[idx, :], label=f"d={nearest_distance:.1f} m")
>>>>>>> theirs

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
