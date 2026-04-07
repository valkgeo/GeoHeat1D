"""Executable Umarizal-style baseline scenario for GeoHeat1D v1 development.

Run:
    python examples/umarizal_example.py
"""

import numpy as np

from geoheat1d.materials.properties import MaterialProperties
from geoheat1d.scenarios.runner import run_scenario
from geoheat1d.scenarios.scenario import IntrusionGeometry1D, Scenario
from geoheat1d.viz.profile_plots import plot_profile_at_time


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
    fig, _ = plot_profile_at_time(result, time_index=60)
    fig.savefig("umarizal_profile.png", dpi=150, bbox_inches="tight")
    print("Saved: umarizal_profile.png")


if __name__ == "__main__":
    main()
