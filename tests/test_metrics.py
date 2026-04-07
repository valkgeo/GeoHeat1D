import numpy as np

from geoheat1d.outputs.metrics import max_temperature, peak_temperature_by_depth
from geoheat1d.outputs.result import ThermalResult


def test_metrics():
    temp = np.array([[100.0, 150.0], [200.0, 180.0]])
    result = ThermalResult(
        depth_m=np.array([0.0, 10.0]),
        time_s=np.array([0.0, 1.0]),
        temperature_c=temp,
        scenario=None,
    )
    peaks = peak_temperature_by_depth(result)
    assert np.allclose(peaks, np.array([150.0, 200.0]))
    assert max_temperature(result) == 200.0
