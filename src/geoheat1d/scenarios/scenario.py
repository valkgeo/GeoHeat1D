"""Scenario objects for defining forward thermal experiments."""

from dataclasses import dataclass

from ..materials.properties import MaterialProperties


@dataclass(frozen=True)
class IntrusionGeometry1D:
    """Geometry of a tabular intrusion in 1D."""

    center_depth_m: float
    half_thickness_m: float


@dataclass(frozen=True)
class Scenario:
    """Forward-model scenario definition."""

    geometry: IntrusionGeometry1D
    host_material: MaterialProperties
    background_temperature_c: float
    intrusion_temperature_c: float
