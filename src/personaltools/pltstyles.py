"""Matplotlib style paths for easy access."""

from pathlib import Path

# Get the directory containing this module
_STYLES_DIR = Path(__file__).parent / "matplotlib_styles"

# Expose style paths as module attributes
ieee = str(_STYLES_DIR / "ieee.mplstyle")
