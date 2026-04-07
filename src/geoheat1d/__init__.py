"""GeoHeat1D: 1D conductive thermal modeling for tabular intrusions."""

from .materials.properties import MaterialProperties
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
from .physics.jaeger_tabular import JaegerTabularModel
from .scenarios.scenario import IntrusionGeometry1D, Scenario
from .scenarios.runner import run_scenario
from .outputs.result import ThermalResult
=======
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
from .outputs.result import ThermalResult
from .physics.jaeger_tabular import JaegerTabularModel
from .scenarios.runner import run_scenario
from .scenarios.scenario import IntrusionGeometry1D, Scenario
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
<<<<<<< ours
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs
=======
>>>>>>> theirs

__all__ = [
=======

__all__ = (
>>>>>>> theirs
    "MaterialProperties",
    "JaegerTabularModel",
    "IntrusionGeometry1D",
    "Scenario",
    "ThermalResult",
    "run_scenario",
<<<<<<< ours
]
=======
)
>>>>>>> theirs
