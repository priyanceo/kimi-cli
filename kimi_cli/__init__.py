"""kimi-cli: A command-line interface for MoonshotAI's Kimi API.

This package provides a CLI and Python API for interacting with
the Kimi (Moonshot AI) large language model service.
"""

__version__ = "0.1.0"
__author__ = "kimi-cli contributors"
__license__ = "MIT"

from kimi_cli.client import KimiClient
from kimi_cli.session import Session

__all__ = [
    "KimiClient",
    "Session",
    "__version__",
]
