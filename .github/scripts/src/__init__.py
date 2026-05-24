"""MagBridge environment management — internal package.

Import order matters: utils defines `cli`, then command modules decorate it.
"""

import src.cmd_build  # noqa: F401, E402

# Import command modules to trigger @cli.command() registration
import src.cmd_dev  # noqa: F401, E402
import src.cmd_npm  # noqa: F401, E402
import src.cmd_ops  # noqa: F401, E402
from src.utils import cli  # defines the Click group

__all__ = ["cli"]
