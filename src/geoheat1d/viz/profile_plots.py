"""Simple plotting helpers for thermal profiles and time series."""

import matplotlib.pyplot as plt


def plot_profile_at_time(result, time_index: int = -1):
    """Plot temperature vs depth for a selected model time index."""
    fig, ax = plt.subplots()
    ax.plot(result.temperature_c[:, time_index], result.depth_m)
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Depth (m)")
    ax.invert_yaxis()
    ax.set_title(f"Temperature profile at t={result.time_s[time_index]:.3e} s")
    return fig, ax
