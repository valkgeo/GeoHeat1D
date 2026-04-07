"""Executable Umarizal-style baseline scenario for GeoHeat1D v1 development.

<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
Run:
    python examples/umarizal_example.py
"""

=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
Run from repo root:
    python examples/umarizal_example.py

The script appends `<repo>/src` to `sys.path` so it can be run without
installing the package first.
"""

from pathlib import Path
import sys

# Allow running the example directly from a source checkout.
REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

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
import numpy as np

from geoheat1d.materials.properties import MaterialProperties
from geoheat1d.scenarios.runner import run_scenario
from geoheat1d.scenarios.scenario import IntrusionGeometry1D, Scenario
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
from geoheat1d.viz.profile_plots import plot_profile_at_time
=======
from geoheat1d.viz.profile_plots import plot_peak_temperature_profile, plot_profile_at_time
from geoheat1d.viz.time_series_plots import plot_temperature_time_series_by_distance
>>>>>>> theirs
=======
from geoheat1d.viz.profile_plots import plot_peak_temperature_profile, plot_profile_at_time
from geoheat1d.viz.time_series_plots import plot_temperature_time_series_by_distance
>>>>>>> theirs
=======
from geoheat1d.viz.profile_plots import plot_peak_temperature_profile, plot_profile_at_time
from geoheat1d.viz.time_series_plots import plot_temperature_time_series_by_distance
>>>>>>> theirs
=======
from geoheat1d.viz.profile_plots import plot_peak_temperature_profile, plot_profile_at_time
from geoheat1d.viz.time_series_plots import plot_temperature_time_series_by_distance
>>>>>>> theirs
=======
from geoheat1d.viz.profile_plots import plot_peak_temperature_profile, plot_profile_at_time
from geoheat1d.viz.time_series_plots import plot_temperature_time_series_by_distance
>>>>>>> theirs
=======
from geoheat1d.viz.profile_plots import plot_peak_temperature_profile, plot_profile_at_time
from geoheat1d.viz.time_series_plots import plot_temperature_time_series_by_distance
>>>>>>> theirs
=======
from geoheat1d.viz.profile_plots import plot_peak_temperature_profile, plot_profile_at_time
from geoheat1d.viz.time_series_plots import plot_temperature_time_series_by_distance
>>>>>>> theirs
=======
=======
>>>>>>> theirs
from geoheat1d.viz.profile_plots import plot_peak_temperature_profile, plot_profile_at_time
from geoheat1d.viz.time_series_plots import plot_temperature_time_series_by_distance


OUTPUT_BASENAME = "umarizal"
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs


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
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
    fig, _ = plot_profile_at_time(result, time_index=60)
    fig.savefig("umarizal_profile.png", dpi=150, bbox_inches="tight")
    print("Saved: umarizal_profile.png")
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

    fig_profile, _ = plot_profile_at_time(result, time_index=60)
    fig_profile.savefig("umarizal_profile_contact_distance.png", dpi=150, bbox_inches="tight")

=======
=======
>>>>>>> theirs

    profile_file = f"{OUTPUT_BASENAME}_profile_contact_distance.png"
    fig_profile, _ = plot_profile_at_time(result, time_index=60)
    fig_profile.savefig(profile_file, dpi=150, bbox_inches="tight")

    timeseries_file = f"{OUTPUT_BASENAME}_time_series_contact_distance.png"
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
    fig_timeseries, _ = plot_temperature_time_series_by_distance(
        result,
        distances_m=[0.0, 200.0, 500.0, 1000.0],
    )
<<<<<<< ours
<<<<<<< ours
    fig_timeseries.savefig("umarizal_time_series_contact_distance.png", dpi=150, bbox_inches="tight")

    fig_peak, _ = plot_peak_temperature_profile(result)
    fig_peak.savefig("umarizal_peak_temperature_contact_distance.png", dpi=150, bbox_inches="tight")

    print("Saved: umarizal_profile_contact_distance.png")
    print("Saved: umarizal_time_series_contact_distance.png")
    print("Saved: umarizal_peak_temperature_contact_distance.png")
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
=======
>>>>>>> theirs
    fig_timeseries.savefig(timeseries_file, dpi=150, bbox_inches="tight")

    peak_file = f"{OUTPUT_BASENAME}_peak_temperature_contact_distance.png"
    fig_peak, _ = plot_peak_temperature_profile(result)
    fig_peak.savefig(peak_file, dpi=150, bbox_inches="tight")

    print(f"Saved: {profile_file}")
    print(f"Saved: {timeseries_file}")
    print(f"Saved: {peak_file}")
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs


if __name__ == "__main__":
    main()
