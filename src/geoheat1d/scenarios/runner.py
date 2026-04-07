"""Execution helpers for running one or more scenarios."""

import numpy as np

from ..outputs.result import ThermalResult
from ..physics.jaeger_tabular import JaegerTabularModel


def run_scenario(scenario, z, t, model=None) -> ThermalResult:
    """Run a single scenario and return a result container."""
    model = model or JaegerTabularModel()
    z = np.asarray(z, dtype=float)
    t = np.asarray(t, dtype=float)
    temperature = model.temperature_field(z, t, scenario)
    return ThermalResult(depth_m=z, time_s=t, temperature_c=temperature, scenario=scenario)
