"""GeoHeat1D: 1D conductive thermal modeling for tabular intrusions."""

from .materials.properties import MaterialProperties
from .physics.jaeger_tabular import JaegerTabularModel
from .scenarios.scenario import IntrusionGeometry1D, Scenario
from .scenarios.runner import run_scenario
from .outputs.result import ThermalResult

__all__ = [
    "MaterialProperties",
    "JaegerTabularModel",
    "IntrusionGeometry1D",
    "Scenario",
    "ThermalResult",
    "run_scenario",
]
