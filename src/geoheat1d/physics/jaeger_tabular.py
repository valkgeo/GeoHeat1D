"""Jaeger-style analytical solution for finite tabular intrusion in 1D conduction."""

import numpy as np
from scipy.special import erf

from ..core.validation import ensure_1d_array
from .base import ThermalModel


class JaegerTabularModel(ThermalModel):
    """Analytical 1D conductive model for an instantaneous tabular intrusion.

    Uses a slab initial-condition solution in an infinite medium.
    """

    def temperature_field(self, z, t, scenario) -> np.ndarray:
        z_arr = ensure_1d_array("z", z)
        t_arr = ensure_1d_array("t", t)

        a = scenario.geometry.half_thickness_m
        z0 = scenario.geometry.center_depth_m
        dt = scenario.intrusion_temperature_c - scenario.background_temperature_c
        kappa = scenario.host_material.kappa

        out = np.zeros((z_arr.size, t_arr.size), dtype=float)
        for j, tj in enumerate(t_arr):
            if tj <= 0:
                inside = np.abs(z_arr - z0) <= a
                out[:, j] = np.where(inside, scenario.intrusion_temperature_c, scenario.background_temperature_c)
                continue

            denom = 2.0 * np.sqrt(kappa * tj)
            arg1 = (z_arr - z0 + a) / denom
            arg2 = (z_arr - z0 - a) / denom
            theta = 0.5 * (erf(arg1) - erf(arg2))
            out[:, j] = scenario.background_temperature_c + dt * theta

        return out
