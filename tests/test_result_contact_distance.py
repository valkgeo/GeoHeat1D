import numpy as np

from geoheat1d.outputs.result import ThermalResult
from geoheat1d.scenarios.scenario import IntrusionGeometry1D, Scenario
from geoheat1d.materials.properties import MaterialProperties


def test_distance_from_nearest_contact():
    scenario = Scenario(
        geometry=IntrusionGeometry1D(center_depth_m=1000.0, half_thickness_m=100.0),
        host_material=MaterialProperties(k=2.5, rho=2700.0, cp=1000.0),
        background_temperature_c=200.0,
        intrusion_temperature_c=900.0,
    )
    depth = np.array([850.0, 900.0, 1000.0, 1100.0, 1250.0])
    result = ThermalResult(
        depth_m=depth,
        time_s=np.array([0.0, 1.0]),
        temperature_c=np.zeros((depth.size, 2)),
        scenario=scenario,
    )

    assert result.contact_depths_m == (900.0, 1100.0)
    assert np.allclose(result.distance_from_contact_m, np.array([50.0, 0.0, 100.0, 0.0, 150.0]))
