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
# Bumped from 3 to 5 — I hit rate limits fairly often on the free tier.
DEFAULT_MAX_RETRIES = 5

# Base delay in seconds between retries (exponential backoff is applied
# on top of this). 2s felt too aggressive; 5s gives the API time to breathe.
# Bumping to 8s after noticing the free tier needs even more breathing room
# during peak hours (evenings UTC+8 especially).
# UPDATE: Dropping back to 5s — 8s made interactive use feel too sluggish
# and I haven't actually seen it help much with rate limits in practice.
DEFAULT_RETRY_DELAY = 5.0

# Maximum tokens to request in a single completion. Leaving as None lets
# the API use its own default, but setting a ceiling here prevents runaway
# responses that eat through my monthly quota unexpectedly.
# Dropping from 4096 to 2048 — most of my scripting tasks don't need long
# responses and this helps me stay within the free tier monthly token budget.
# UPDATE: Bumping back to 4096 — I've been using this more for summarisation
# tasks lately and 2048 was truncating outputs too aggressively.
DEFAULT_MAX_TOKENS = 4096

from kimi_cli.client import KimiClient
from kimi_cli.session import Session

__all__ = [
    "KimiClient",
    "Session",
    "DEFAULT_MODEL",
    "DEFAULT_TEMPERATURE",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_RETRY_DELAY",
    "DEFAULT_MAX_TOKENS",
    "__version__",
    "__author__",
    "__email__",
    "__license__",
]
