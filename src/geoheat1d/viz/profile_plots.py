"""Publication-ready plotting helpers using distance from intrusion contact."""

import matplotlib.pyplot as plt
import numpy as np

from ..outputs.metrics import peak_temperature_by_distance_from_contact


def plot_profile_at_time(result, time_index: int = -1):
    """Plot temperature vs distance from nearest intrusion contact."""
    fig, ax = plt.subplots()
    x = result.distance_from_contact_m
    y = result.temperature_c[:, time_index]

    order = np.argsort(x)
    ax.plot(x[order], y[order])
    ax.set_xlabel("Distance from nearest intrusion contact (m)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title(f"Temperature profile vs contact distance at t={result.time_s[time_index]:.3e} s")
    return fig, ax


def plot_peak_temperature_profile(result):
    """Optional summary plot: peak temperature vs distance from contact."""
    fig, ax = plt.subplots()
    x, y = peak_temperature_by_distance_from_contact(result)
    ax.plot(x, y)
    ax.set_xlabel("Distance from nearest intrusion contact (m)")
    ax.set_ylabel("Peak temperature (°C)")
    ax.set_title("Peak temperature as a function of contact distance")
    return fig, ax
