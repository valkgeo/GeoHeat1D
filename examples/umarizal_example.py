"""Executable Umarizal-style baseline scenario for GeoHeat1D v1 development.

This example demonstrates a deep crustal intrusion (mafic sill at ~4 kbar)
intruding host rock at amphibolite-facies background temperatures, with a
linear crustal geothermal gradient.

Generates publication-style figures:
- umarizal_lateral_profile.png: 
  Lateral thermal profile at the emplacement depth (erosional cross-section view).
  How temperature spreads outward from the intrusion into country rock at a fixed
  crustal level.
- umarizal_temperature_vs_time.png: 
  Temperature evolution at selected distances from intrusion contact.

Run:
    python examples/umarizal_example.py
"""

import numpy as np

from geoheat1d.materials.properties import MaterialProperties
from geoheat1d.scenarios.runner import run_scenario
from geoheat1d.scenarios.scenario import IntrusionGeometry1D, Scenario
from geoheat1d.viz.profile_plots import plot_lateral_profile_at_depth
from geoheat1d.viz.time_series_plots import plot_temperature_time_series_by_distance


def main() -> None:
    # Host rock thermophysical properties (typical gabbroic host)
    host = MaterialProperties(k=2.5, rho=2700.0, cp=1000.0)
    
    # Tabular intrusion geometry
    # Center depth ~5 km (~5000 m) corresponds to ~4 kbar pressure
    # Half-thickness 500 m represents a typical sill/dike thickness in this setting
    geometry = IntrusionGeometry1D(center_depth_m=5000.0, half_thickness_m=500.0)
    
    # Temperature structure:
    # - Surface temperature: 10°C (reasonable continental surface)
    # - Geothermal gradient: 48°C/km (hot region, typical of active orogenic belt)
    #   -> At z=5000m: T_bg = 10 + 48*5 = 250°C (low amphibolite facies)
    # - Intrusion temperature: 950°C (basaltic melt at mantle potential temperature)
    # - Thermal anomaly at center: ΔT = 950 - 250 = 700°C
    scenario = Scenario(
        geometry=geometry,
        host_material=host,
        surface_temperature_c=10.0,
        geothermal_gradient_c_per_km=48.0,
        intrusion_temperature_c=950.0,
    )

    # Depth range encompassing the intrusion and aureole
    z = np.linspace(2500.0, 7500.0, 201)
    # Time range from ~30 years to ~300 Ma
    t = np.geomspace(1e3, 1e13, 180)

    print("Running thermal model...")
    result = run_scenario(scenario, z=z, t=t)
    
    # Reference depth = emplacement depth (inferred from thermobarometry)
    # This represents the specific crustal level being observed as an erosional cross-section
    reference_depth = 5000.0
    
    # Generate publication-style lateral profile figure
    print(f"Creating lateral profile figure at z = {reference_depth:.0f} m...")
    fig_lateral, _ = plot_lateral_profile_at_depth(result, reference_depth_m=reference_depth)
    fig_lateral.savefig("umarizal_lateral_profile.png", dpi=150, bbox_inches="tight")
    print("Saved: umarizal_lateral_profile.png")
    
    # Generate temperature-time series figure
    print("Creating temperature-time series figure...")
    fig_time, _ = plot_temperature_time_series_by_distance(result)
    fig_time.savefig("umarizal_temperature_vs_time.png", dpi=150, bbox_inches="tight")
    print("Saved: umarizal_temperature_vs_time.png")


if __name__ == "__main__":
    main()
