import numpy as np

from geoheat1d.materials.properties import MaterialProperties
from geoheat1d.physics.jaeger_tabular import JaegerTabularModel
from geoheat1d.scenarios.scenario import IntrusionGeometry1D, Scenario


def _scenario():
    """Test scenario: simple case with zero gradient (equivalent to uniform background)."""
    return Scenario(
        geometry=IntrusionGeometry1D(center_depth_m=0.0, half_thickness_m=10.0),
        host_material=MaterialProperties(k=2.5, rho=2700.0, cp=1000.0),
        surface_temperature_c=200.0,
        geothermal_gradient_c_per_km=0.0,  # Zero gradient for backward compatibility
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


def test_geothermal_gradient_initial_condition():
    """Test that the geothermal gradient is properly applied to the initial condition."""
    model = JaegerTabularModel()
    
    # Scenario with non-zero gradient: 25 °C/km
    scenario = Scenario(
        geometry=IntrusionGeometry1D(center_depth_m=4000.0, half_thickness_m=500.0),
        host_material=MaterialProperties(k=2.5, rho=2700.0, cp=1000.0),
        surface_temperature_c=10.0,
        geothermal_gradient_c_per_km=25.0,
        intrusion_temperature_c=800.0,
    )
    
    z = np.array([2000.0, 4000.0, 6000.0])
    t = np.array([0.0])
    temp = model.temperature_field(z, t, scenario)
    
    # Expected background temperatures: T_bg(z) = 10 + 25 * (z / 1000)
    # z=2000: T_bg = 10 + 25*2 = 60°C (outside intrusion, should be 60°C)
    # z=4000: T_bg = 10 + 25*4 = 110°C (at center, inside intrusion, should be 800°C)
    # z=6000: T_bg = 10 + 25*6 = 160°C (outside intrusion, should be 160°C)
    
    assert abs(temp[0, 0] - 60.0) < 1e-6   # Outside, above center
    assert abs(temp[1, 0] - 800.0) < 1e-6  # Inside, at center
    assert abs(temp[2, 0] - 160.0) < 1e-6  # Outside, below center


def test_late_time_relaxes_to_gradient():
    """Test that at late times, temperature relaxes to the background geotherm."""
    model = JaegerTabularModel()
    
    scenario = Scenario(
        geometry=IntrusionGeometry1D(center_depth_m=4000.0, half_thickness_m=500.0),
        host_material=MaterialProperties(k=2.5, rho=2700.0, cp=1000.0),
        surface_temperature_c=10.0,
        geothermal_gradient_c_per_km=25.0,
        intrusion_temperature_c=800.0,
    )
    
    z = np.array([3000.0, 5000.0])
    t = np.array([1e20])  # Very late time
    temp = model.temperature_field(z, t, scenario)
    
    # Expected: T_bg(z) = 10 + 25 * (z / 1000) at late time
    expected_3000 = 10.0 + 25.0 * 3.0
    expected_5000 = 10.0 + 25.0 * 5.0
    
    assert abs(temp[0, 0] - expected_3000) < 1e-1  # ~75°C
    assert abs(temp[1, 0] - expected_5000) < 1e-1  # ~135°C
