"""Abstract interfaces for forward thermal models."""

from abc import ABC, abstractmethod
import numpy as np


class ThermalModel(ABC):
    """Base class for 1D forward thermal models."""

    @abstractmethod
    def temperature_field(self, z, t, scenario) -> np.ndarray:
        """Return temperature field on depth-time grid."""
