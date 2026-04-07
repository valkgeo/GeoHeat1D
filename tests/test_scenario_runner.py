import numpy as np

from geoheat1d.materials.properties import MaterialProperties
from geoheat1d.scenarios.runner import run_scenario
from geoheat1d.scenarios.scenario import IntrusionGeometry1D, Scenario


def test_run_scenario_returns_expected_shape():
    scenario = Scenario(
        geometry=IntrusionGeometry1D(center_depth_m=1000.0, half_thickness_m=100.0),
        host_material=MaterialProperties(k=2.0, rho=2600.0, cp=900.0),
        background_temperature_c=150.0,
        intrusion_temperature_c=850.0,
    )
    z = np.linspace(0.0, 2000.0, 31)
    t = np.array([0.0, 1e9, 1e10])
    result = run_scenario(scenario, z, t)
    assert result.temperature_c.shape == (31, 3)
