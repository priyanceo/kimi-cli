"""kimi-cli: A command-line interface for MoonshotAI's Kimi API.

This package provides a CLI and Python API for interacting with
the Kimi (Moonshot AI) large language model service.

Personal fork: added __author__ and __email__ for local dev tracking.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "you@example.com"
__license__ = "MIT"

from kimi_cli.client import KimiClient
from kimi_cli.session import Session

__all__ = [
    "KimiClient",
    "Session",
    "__version__",
    "__author__",
]
