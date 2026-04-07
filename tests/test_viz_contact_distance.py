import numpy as np

from geoheat1d.materials.properties import MaterialProperties
from geoheat1d.scenarios.runner import run_scenario
from geoheat1d.scenarios.scenario import IntrusionGeometry1D, Scenario
from geoheat1d.viz.profile_plots import plot_peak_temperature_profile, plot_profile_at_time
from geoheat1d.viz.time_series_plots import plot_temperature_time_series_by_distance


def _result():
    scenario = Scenario(
        geometry=IntrusionGeometry1D(center_depth_m=1000.0, half_thickness_m=100.0),
        host_material=MaterialProperties(k=2.5, rho=2700.0, cp=1000.0),
        background_temperature_c=200.0,
        intrusion_temperature_c=900.0,
    )
    z = np.linspace(700.0, 1300.0, 51)
    t = np.array([0.0, 1e5, 1e7])
    return run_scenario(scenario, z, t)


def test_profile_plot_uses_contact_distance_labels():
    result = _result()
    fig, ax = plot_profile_at_time(result, time_index=1)
    assert "Distance from nearest intrusion contact" in ax.get_xlabel()
    assert ax.get_ylabel() == "Temperature (°C)"
    fig.clf()


def test_time_series_plot_labels():
    result = _result()
    fig, ax = plot_temperature_time_series_by_distance(result, distances_m=[0.0, 50.0])
    assert ax.get_xlabel() == "Time since emplacement (s)"
    assert ax.get_ylabel() == "Temperature (°C)"
    fig.clf()


def test_peak_plot_labels():
    result = _result()
    fig, ax = plot_peak_temperature_profile(result)
    assert ax.get_ylabel() == "Peak temperature (°C)"
    fig.clf()
