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
    """Forward-model scenario definition.
    
    Defines initial conditions for a tabular intrusion in host rock with linear
    geothermal gradient.
    """

    geometry: IntrusionGeometry1D
    host_material: MaterialProperties
    surface_temperature_c: float
    geothermal_gradient_c_per_km: float
    intrusion_temperature_c: float
    background_temperature_c: float = None  # DEPRECATED: use surface_temperature_c + gradient instead
