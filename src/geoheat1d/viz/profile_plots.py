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
"""Simple plotting helpers for thermal profiles and time series."""

import matplotlib.pyplot as plt
import numpy as np


def plot_profile_at_time(result, time_index: int = -1):
    """Plot temperature vs depth for a selected model time index."""
    fig, ax = plt.subplots()
    ax.plot(result.temperature_c[:, time_index], result.depth_m)
    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Depth (m)")
    ax.invert_yaxis()
    ax.set_title(f"Temperature profile at t={result.time_s[time_index]:.3e} s")
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
    return fig, ax


def plot_lateral_profile_at_depth(result, reference_depth_m, time_indices=None):
    """Plot lateral thermal profile at a fixed reference depth (erosional cross-section).
    
    Scientific interpretation: Shows how temperature varies horizontally (laterally) 
    from the intrusion into country rock at a fixed crustal level (e.g., emplacement 
    depth inferred from thermobarometry).
    
    The 1D vertical thermal field is reinterpreted as a lateral profile at the 
    reference depth, with temperatures referenced to the background geotherm at 
    that level.
    
    Args:
        result: ThermalResult object containing temperature field and scenario
        reference_depth_m: Depth level (m) at which to construct the lateral profile
                          (typically emplacement depth from thermobarometry)
        time_indices: List of time indices to plot. If None, uses selected times.
    
    Returns:
        fig, ax: matplotlib figure and axes objects
    """
    # Extract scenario parameters
    center_depth = result.scenario.geometry.center_depth_m
    half_thickness = result.scenario.geometry.half_thickness_m
    T_surface = result.scenario.surface_temperature_c
    G = result.scenario.geothermal_gradient_c_per_km
    
    # Compute background temperature at reference depth
    T_bg_ref = T_surface + G * (reference_depth_m / 1000.0)
    
    # Compute background temperature at each depth in the model
    T_bg_z = T_surface + G * (result.depth_m / 1000.0)
    
    # Compute thermal anomaly at each depth: ΔT(z,t) = T(z,t) - T_bg(z)
    anomaly_c = result.temperature_c - T_bg_z[:, np.newaxis]
    
    # For lateral profile: use reference background + anomaly
    # This anchors temperatures to T_bg at the reference depth
    T_lateral = T_bg_ref + anomaly_c
    
    # Interpret vertical distance as lateral distance
    lateral_distance_m = result.depth_m - center_depth
    
    # Select time indices to plot
    if time_indices is None:
        n_times = len(result.time_s)
        time_indices = [0, n_times // 4, n_times // 2, 3 * n_times // 4, -1]
        time_indices = [i for i in time_indices if 0 <= i < n_times]
    
    # Create figure with main plot and parameter panel
    fig = plt.figure(figsize=(12, 6))
    gs = fig.add_gridspec(1, 2, width_ratios=[3, 1], wspace=0.4)
    ax_main = fig.add_subplot(gs[0])
    ax_params = fig.add_subplot(gs[1])
    
    # Plot lateral profiles for selected times
    colors = plt.cm.RdYlBu_r(np.linspace(0.2, 0.8, len(time_indices)))
    for idx, (time_idx, color) in enumerate(zip(time_indices, colors)):
        time_val = result.time_s[time_idx]
        label = f"t = {time_val:.2e} s"
        ax_main.plot(lateral_distance_m, T_lateral[:, time_idx], 
                    label=label, color=color, linewidth=2)
    
    # Shade the intrusion as a central gray band
    ax_main.axvspan(-half_thickness, half_thickness, alpha=0.25, color='gray', 
                    label='Intrusion')
    
    # Labels and styling
    ax_main.set_xlabel("Lateral distance from intrusion center (m)", fontsize=11)
    ax_main.set_ylabel("Temperature (°C)", fontsize=11)
    ax_main.set_title(f"Lateral thermal profile at z = {reference_depth_m:.0f} m (erosional cross-section)", 
                     fontsize=12, fontweight='bold')
    ax_main.legend(loc='best', fontsize=9)
    ax_main.grid(True, alpha=0.3)
    
    # Parameter panel on the right
    ax_params.axis('off')
    params_text = f"""Model Parameters:

Surface T: {T_surface:.1f}°C
Gradient: {G:.1f}°C/km
T_bg @ z_ref: {T_bg_ref:.0f}°C

Intrusion T: {result.scenario.intrusion_temperature_c:.0f}°C
Center depth: {center_depth:.0f} m
Half-thickness: {half_thickness:.0f} m

Reference depth: {reference_depth_m:.0f} m
(Emplacement level)

Host rock k: {result.scenario.host_material.k:.2f} W/m·K
"""
    ax_params.text(0.05, 0.95, params_text, transform=ax_params.transAxes,
                  fontsize=9, verticalalignment='top', family='monospace',
                  bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    return fig, ax_main


def plot_temperature_vs_distance(result, time_indices=None):
    """Plot temperature vs distance from intrusion center at multiple times.
    
    Deprecated: Use plot_lateral_profile_at_depth() instead for publication-style figures.
    This function provides a distance-based view without reference depth normalization.
    
    Args:
        result: ThermalResult object containing temperature field and scenario
        time_indices: List of time indices to plot. If None, uses selected times.
    
    Returns:
        fig, ax: matplotlib figure and axes objects
    """
    # Extract scenario geometry
    center_depth = result.scenario.geometry.center_depth_m
    half_thickness = result.scenario.geometry.half_thickness_m
    
    # Compute distance from intrusion center (relative coordinate)
    distance_m = result.depth_m - center_depth
    
    # Select time indices to plot
    if time_indices is None:
        n_times = len(result.time_s)
        time_indices = [0, n_times // 4, n_times // 2, 3 * n_times // 4, -1]
        time_indices = [i for i in time_indices if 0 <= i < n_times]
    
    # Create figure with main plot and parameter panel
    fig = plt.figure(figsize=(12, 6))
    gs = fig.add_gridspec(1, 2, width_ratios=[3, 1], wspace=0.4)
    ax_main = fig.add_subplot(gs[0])
    ax_params = fig.add_subplot(gs[1])
    
    # Plot temperature profiles for selected times
    colors = plt.cm.RdYlBu_r(np.linspace(0.2, 0.8, len(time_indices)))
    for idx, (time_idx, color) in enumerate(zip(time_indices, colors)):
        time_val = result.time_s[time_idx]
        label = f"t = {time_val:.2e} s"
        ax_main.plot(distance_m, result.temperature_c[:, time_idx], 
                    label=label, color=color, linewidth=2)
    
    # Shade the intrusion as a central gray band
    ax_main.axvspan(-half_thickness, half_thickness, alpha=0.25, color='gray', 
                    label='Intrusion')
    
    # Labels and styling
    ax_main.set_xlabel("Distance from intrusion center (m)", fontsize=11)
    ax_main.set_ylabel("Temperature (°C)", fontsize=11)
    ax_main.set_title("Thermal aureole evolution (distance-based perspective)", fontsize=12, fontweight='bold')
    ax_main.legend(loc='best', fontsize=9)
    ax_main.grid(True, alpha=0.3)
    
    # Parameter panel on the right
    ax_params.axis('off')
    params_text = f"""Model Parameters:

Surface T: {result.scenario.surface_temperature_c:.1f}°C
Gradient: {result.scenario.geothermal_gradient_c_per_km:.1f}°C/km

Intrusion T: {result.scenario.intrusion_temperature_c:.0f}°C
Center depth: {center_depth:.0f} m
Half-thickness: {half_thickness:.0f} m

Host rock k: {result.scenario.host_material.k:.2f} W/m·K
"""
    ax_params.text(0.05, 0.95, params_text, transform=ax_params.transAxes,
                  fontsize=9, verticalalignment='top', family='monospace',
                  bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    return fig, ax_main
