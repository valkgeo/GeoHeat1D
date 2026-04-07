"""Executable Umarizal-style baseline scenario for GeoHeat1D v1 development.

Run:
    python examples/umarizal_example.py
"""

import numpy as np

from geoheat1d.materials.properties import MaterialProperties
from geoheat1d.scenarios.runner import run_scenario
from geoheat1d.scenarios.scenario import IntrusionGeometry1D, Scenario
from geoheat1d.viz.profile_plots import plot_peak_temperature_profile, plot_profile_at_time
from geoheat1d.viz.time_series_plots import plot_temperature_time_series_by_distance


def main() -> None:
    host = MaterialProperties(k=2.5, rho=2700.0, cp=1000.0)
    geometry = IntrusionGeometry1D(center_depth_m=5000.0, half_thickness_m=500.0)
    scenario = Scenario(
        geometry=geometry,
        host_material=host,
        background_temperature_c=250.0,
        intrusion_temperature_c=950.0,
    )

    z = np.linspace(2500.0, 7500.0, 201)
    t = np.geomspace(1e3, 1e13, 180)

    result = run_scenario(scenario, z=z, t=t)

    fig_profile, _ = plot_profile_at_time(result, time_index=60)
    fig_profile.savefig("umarizal_profile_contact_distance.png", dpi=150, bbox_inches="tight")

    fig_timeseries, _ = plot_temperature_time_series_by_distance(
        result,
        distances_m=[0.0, 200.0, 500.0, 1000.0],
    )
    fig_timeseries.savefig("umarizal_time_series_contact_distance.png", dpi=150, bbox_inches="tight")

    fig_peak, _ = plot_peak_temperature_profile(result)
    fig_peak.savefig("umarizal_peak_temperature_contact_distance.png", dpi=150, bbox_inches="tight")

    print("Saved: umarizal_profile_contact_distance.png")
    print("Saved: umarizal_time_series_contact_distance.png")
    print("Saved: umarizal_peak_temperature_contact_distance.png")


if __name__ == "__main__":
    main()
