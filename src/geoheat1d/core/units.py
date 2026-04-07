"""Unit conversion helpers for consistent SI-centric modeling."""

from .constants import SECONDS_PER_YEAR


def years_to_seconds(years: float) -> float:
    """Convert years to seconds."""
    return years * SECONDS_PER_YEAR
