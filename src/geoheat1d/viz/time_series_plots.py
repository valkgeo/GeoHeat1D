"""Time-series plotting helpers for thermal evolution analysis."""

import matplotlib.pyplot as plt
import numpy as np


def plot_temperature_time_series_by_distance(result, distances_from_contact=None):
    """Plot temperature vs time at selected distances from intrusion contact.
    
    Shows how temperature evolves with time at fixed distances from the intrusion,
    useful for evaluating mineralogical reaction kinetics or cooling rates.
    
    Args:
        result: ThermalResult object
        distances_from_contact: List of distances (m) from nearest intrusion contact.
                               If None, uses [0, 250, 500, 1000] m.
    
    Returns:
        fig, ax: matplotlib figure and axes objects
    """
    if distances_from_contact is None:
        distances_from_contact = [0, 250, 500, 1000]
    
    # Extract scenario geometry
    center_depth = result.scenario.geometry.center_depth_m
    half_thickness = result.scenario.geometry.half_thickness_m
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(distances_from_contact)))
    
    for dist_contact, color in zip(distances_from_contact, colors):
        # Find depths at this distance from the nearest contact (both upper and lower)
        depth_upper = center_depth - half_thickness - dist_contact
        depth_lower = center_depth + half_thickness + dist_contact
        
        # Find closest index to each depth
        idx_upper = np.argmin(np.abs(result.depth_m - depth_upper))
        idx_lower = np.argmin(np.abs(result.depth_m - depth_lower))
        
        # Plot average of the two symmetric positions (upper and lower)
        temp_upper = result.temperature_c[idx_upper, :]
        temp_lower = result.temperature_c[idx_lower, :]
        temp_avg = 0.5 * (temp_upper + temp_lower)
        
        if dist_contact == 0:
            label = "At intrusion contact"
        else:
            label = f"{dist_contact:.0f} m from contact"
        
        ax.loglog(result.time_s, temp_avg, marker='o', markersize=4,
                 label=label, color=color, linewidth=2)
    
    ax.set_xlabel("Time since emplacement (s)", fontsize=11)
    ax.set_ylabel("Temperature (°C)", fontsize=11)
    ax.set_title("Temperature evolution at selected distances from intrusion", 
                fontsize=12, fontweight='bold')
    ax.legend(loc='best', fontsize=10)
    ax.grid(True, alpha=0.3, which='both')
    
    return fig, ax
