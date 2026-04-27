"""kimi-cli: A command-line interface for MoonshotAI's Kimi API.

This package provides a CLI and Python API for interacting with
the Kimi (Moonshot AI) large language model service.

Personal fork: added __author__ and __email__ for local dev tracking.
Note: I'm using this to experiment with Moonshot's API for side projects.
"""

__version__ = "0.1.0"
__author__ = "Your Name"
__email__ = "you@example.com"
__license__ = "MIT"

# Default model to use when none is specified. Upstream defaults to
# "moonshot-v1-8k"; switching to 32k for longer context in my workflows.
DEFAULT_MODEL = "moonshot-v1-32k"

from kimi_cli.client import KimiClient
from kimi_cli.session import Session

__all__ = [
    "KimiClient",
    "Session",
    "DEFAULT_MODEL",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
]
