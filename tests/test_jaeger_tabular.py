import numpy as np

from geoheat1d.materials.properties import MaterialProperties
from geoheat1d.physics.jaeger_tabular import JaegerTabularModel
from geoheat1d.scenarios.scenario import IntrusionGeometry1D, Scenario


def _scenario():
    return Scenario(
        geometry=IntrusionGeometry1D(center_depth_m=0.0, half_thickness_m=10.0),
        host_material=MaterialProperties(k=2.5, rho=2700.0, cp=1000.0),
        background_temperature_c=200.0,
        intrusion_temperature_c=900.0,
    )


def test_initial_condition_inside_and_outside():
    model = JaegerTabularModel()
    z = np.array([-20.0, 0.0, 20.0])
    t = np.array([0.0])
    temp = model.temperature_field(z, t, _scenario())
    assert temp[1, 0] == 900.0
    assert temp[0, 0] == 200.0


def test_late_time_relaxes_toward_background():
    model = JaegerTabularModel()
    z = np.array([0.0])
    t = np.array([1e20])
    temp = model.temperature_field(z, t, _scenario())
    assert abs(temp[0, 0] - 200.0) < 1e-2
