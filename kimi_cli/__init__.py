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

# Default temperature for generation. Moonshot's API accepts 0.0-1.0;
# keeping it slightly lower than the upstream default (1.0) for more
# consistent, less random outputs in my scripting use cases.
DEFAULT_TEMPERATURE = 0.7

# Maximum number of retries on transient API errors (e.g. rate limits,
# 5xx responses). Upstream doesn't expose this; adding it here so I can
# tune retry behaviour without digging into the client code each time.
DEFAULT_MAX_RETRIES = 3

from kimi_cli.client import KimiClient
from kimi_cli.session import Session

__all__ = [
    "KimiClient",
    "Session",
    "DEFAULT_MODEL",
    "DEFAULT_TEMPERATURE",
    "DEFAULT_MAX_RETRIES",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
]
