"""Syntax guardrails for executable examples."""

from pathlib import Path
import py_compile


def test_umarizal_example_compiles() -> None:
    """Ensure the Umarizal example has valid Python syntax."""
    example = Path(__file__).resolve().parents[1] / "examples" / "umarizal_example.py"
    py_compile.compile(str(example), doraise=True)
