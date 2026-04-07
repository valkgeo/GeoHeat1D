"""Structured result containers for forward-model output."""

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ThermalResult:
    """Container for a full depth-time temperature field.

    Internal coordinates remain absolute depth. Publication-ready plotting
    helpers can rely on nearest-contact distance properties.
    """

    depth_m: np.ndarray
    time_s: np.ndarray
    temperature_c: np.ndarray
    scenario: object

    @property
    def contact_depths_m(self) -> tuple[float, float]:
        """Upper and lower intrusion contact depths in meters."""
        center = self.scenario.geometry.center_depth_m
        half_thickness = self.scenario.geometry.half_thickness_m
        return center - half_thickness, center + half_thickness

    @property
    def distance_from_contact_m(self) -> np.ndarray:
        """Distance to nearest intrusion contact for each modeled depth (meters)."""
        upper, lower = self.contact_depths_m
        to_upper = np.abs(self.depth_m - upper)
        to_lower = np.abs(self.depth_m - lower)
        return np.minimum(to_upper, to_lower)
