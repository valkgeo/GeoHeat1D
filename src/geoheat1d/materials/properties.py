"""Material property containers for host and intrusion thermodynamics."""

from dataclasses import dataclass


@dataclass(frozen=True)
class MaterialProperties:
    """Minimal material properties for conductive heat transfer.

    Attributes
    ----------
    k : float
        Thermal conductivity in W/m/K.
    rho : float
        Density in kg/m^3.
    cp : float
        Heat capacity in J/kg/K.
    """

    k: float
    rho: float
    cp: float

    @property
    def kappa(self) -> float:
        """Thermal diffusivity m^2/s."""
        return self.k / (self.rho * self.cp)
