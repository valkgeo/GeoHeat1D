"""GeoHeat1D: 1D conductive thermal modeling for tabular intrusions."""

from .materials.properties import MaterialProperties
from .outputs.result import ThermalResult
from .physics.jaeger_tabular import JaegerTabularModel
from .scenarios.runner import run_scenario
from .scenarios.scenario import IntrusionGeometry1D, Scenario

__all__ = (
    "MaterialProperties",
    "JaegerTabularModel",
    "IntrusionGeometry1D",
    "Scenario",
    "ThermalResult",
    "run_scenario",
)
