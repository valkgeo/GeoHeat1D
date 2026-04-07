"""Jaeger-style analytical solution for finite tabular intrusion in 1D conduction."""

import numpy as np
from scipy.special import erf

from ..core.validation import ensure_1d_array
from .base import ThermalModel


class JaegerTabularModel(ThermalModel):
    """Analytical 1D conductive model for an instantaneous tabular intrusion.

    Governing equation:
        T(z, t) = T_bg(z) + ΔT · θ(z, t)
    
    where:
        T_bg(z) = T_surface + G · (z / 1000)  [linear crustal geotherm]
        ΔT = T_intrusion - T_bg(z0)  [thermal anomaly at intrusion center]
        θ(z, t) = Jaeger slab solution (error function based)
        z0 = center_depth_m
        G = geothermal_gradient_c_per_km
    
    Initial conditions (t ≤ 0):
        Inside intrusion (|z - z0| ≤ a): T = T_intrusion
        Outside intrusion: T = T_bg(z)
    
    Physical assumptions:
        - Instantaneous thermal perturbation at t=0 (step function)
        - Uniform host rock properties (k, ρ, cp) with depth
        - Slab geometry with sharp boundaries
        - Conductive heat transfer dominates (semi-infinite medium)
    
    Mathematical framework:
        Uses the complementary error function solution for a slab initial
        condition in infinite 1D conduction, superimposed on a linear
        background temperature profile.
    """

    def temperature_field(self, z, t, scenario) -> np.ndarray:
        """Compute temperature field for a tabular intrusion in a linear geotherm.
        
        Args:
            z: Depth array (m, positive downward)
            t: Time array (s, t=0 is emplacement)
            scenario: Scenario object with geometry, material, temperature parameters
        
        Returns:
            Temperature array of shape (len(z), len(t)) in °C
        """
        z_arr = ensure_1d_array("z", z)
        t_arr = ensure_1d_array("t", t)

        a = scenario.geometry.half_thickness_m
        z0 = scenario.geometry.center_depth_m
        kappa = scenario.host_material.kappa
        T_surface = scenario.surface_temperature_c
        G = scenario.geothermal_gradient_c_per_km

        # Compute background temperature at any depth: T_bg(z) = T_surface + G * (z / 1000)
        T_bg_z = T_surface + G * (z_arr / 1000.0)
        # Compute background temperature at intrusion center: T_bg(z0)
        T_bg_z0 = T_surface + G * (z0 / 1000.0)
        # Compute thermal anomaly: ΔT = T_intrusion - T_bg(z0)
        dt = scenario.intrusion_temperature_c - T_bg_z0

        out = np.zeros((z_arr.size, t_arr.size), dtype=float)
        for j, tj in enumerate(t_arr):
            if tj <= 0:
                # Initial condition: step function in thermal anomaly
                inside = np.abs(z_arr - z0) <= a
                out[:, j] = np.where(inside, scenario.intrusion_temperature_c, T_bg_z)
                continue

            # Jaeger solution for thermal anomaly: θ(z, t) = 0.5 * [erf(arg1) - erf(arg2)]
            denom = 2.0 * np.sqrt(kappa * tj)
            arg1 = (z_arr - z0 + a) / denom
            arg2 = (z_arr - z0 - a) / denom
            theta = 0.5 * (erf(arg1) - erf(arg2))
            # Total temperature: T(z,t) = T_bg(z) + ΔT * θ(z,t)
            out[:, j] = T_bg_z + dt * theta

        return out
