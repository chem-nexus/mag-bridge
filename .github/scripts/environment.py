#!/usr/bin/env python3
"""
MagBridge Development Environment CLI

Run 'python .github/scripts/environment.py --help' for all commands.

Internal structure:
    .github/scripts/src/config.py    — paths, ports, platform constants
    .github/scripts/src/utils.py     — shared helpers + Click group
    .github/scripts/src/cmd_dev.py   — dev server commands
    .github/scripts/src/cmd_build.py — build / packaging commands
    .github/scripts/src/cmd_npm.py   — npm dependency commands
    .github/scripts/src/cmd_ops.py   — run, logs, remove-quarantine
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure .github/scripts/ is on sys.path so the 'src' package is importable regardless
# of the working directory from which this script is invoked.
sys.path.insert(0, str(Path(__file__).parent))

from src import cli  # noqa: E402

if __name__ == "__main__":
    cli()
