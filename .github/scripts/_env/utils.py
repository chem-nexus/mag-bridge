"""Shared helpers: CLI group, output formatting, port management, env checks."""

from __future__ import annotations

import os
import platform
import shutil
import signal
import subprocess
from enum import Enum
from pathlib import Path

import click

from _env.config import settings

# ---------------------------------------------------------------------------
# CLI group
# ---------------------------------------------------------------------------


@click.group()
@click.version_option(version="1.0.0", prog_name="MagBridge Environment")
def cli() -> None:
    """MagBridge development environment manager."""
    pass


# ---------------------------------------------------------------------------
# Utility helpers
# ---------------------------------------------------------------------------


class LogLevel(Enum):
    HEADER = "header"
    SUCCESS = "success"
    ERROR = "error"
    WARN = "warn"
    INFO = "info"


class EnvUtils:
    """Helper utilities for environment scripts."""

    @staticmethod
    def log(level: LogLevel, msg: str) -> None:
        if level == LogLevel.HEADER:
            click.echo(f"\n🚀 {click.style(msg, fg='cyan', bold=True)}\n")
            return
        if level == LogLevel.SUCCESS:
            click.echo(f"✅ {msg}")
            return
        if level == LogLevel.ERROR:
            click.echo(f"❌ {click.style(msg, fg='red')}", err=True)
            return
        if level == LogLevel.WARN:
            click.echo(f"⚠️  {click.style(msg, fg='yellow')}")
            return
        if level == LogLevel.INFO:
            click.echo(f"📦 {msg}")
            return

    @staticmethod
    def node_bin(bin_name: str) -> str:
        """Return a resolvable Node binary name (npm/npx), handling Windows .cmd."""
        candidates = [bin_name]
        if os.name == "nt":
            candidates = [f"{bin_name}.cmd", f"{bin_name}.exe", bin_name]

        for candidate in candidates:
            if shutil.which(candidate):
                return candidate

        EnvUtils.log(LogLevel.ERROR, f"{bin_name} not found on PATH. Install Node.js and ensure npm is available.")
        raise SystemExit(1)

    @staticmethod
    def kill_port(port: int) -> bool:
        """Kill process listening on *port*. Returns True if anything was killed."""
        if platform.system() == "Windows":
            try:
                result = subprocess.run(
                    ["netstat", "-ano"],
                    capture_output=True,
                    text=True,
                )
                killed = False
                for line in result.stdout.splitlines():
                    if f":{port}" in line and "LISTENING" in line:
                        parts = line.split()
                        if parts:
                            subprocess.run(
                                ["taskkill", "/F", "/PID", parts[-1]],
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL,
                            )
                            killed = True
                return killed
            except Exception:
                return False

        # Unix: lsof → fuser fallback
        try:
            result = subprocess.run(
                ["lsof", "-ti", f":{port}"],
                capture_output=True,
                text=True,
            )
            if result.stdout.strip():
                for pid in result.stdout.strip().split("\n"):
                    try:
                        os.kill(int(pid), signal.SIGKILL)
                    except (ProcessLookupError, ValueError):
                        pass
                return True
        except FileNotFoundError:
            subprocess.run(
                f"fuser -k {port}/tcp",
                shell=True,
                stderr=subprocess.DEVNULL,
                stdout=subprocess.DEVNULL,
            )
        return False

    @staticmethod
    def check_venv() -> bool:
        """Return False (with error message) if the project venv is absent."""
        if not settings.venv_exists:
            EnvUtils.log(LogLevel.ERROR, "Virtual environment not found!")
            click.echo("   Run: uv venv .venv && uv pip install -r requirements.txt")
            return False
        return True

    @staticmethod
    def check_node_modules(path: Path, name: str) -> bool:
        """Auto-install node_modules if missing. Returns False on failure."""
        node_modules = path / "node_modules"
        if not node_modules.exists():
            EnvUtils.log(LogLevel.INFO, f"Installing {name} dependencies...")
            result = subprocess.run([EnvUtils.node_bin("npm"), "install"], cwd=path)
            if result.returncode != 0:
                EnvUtils.log(LogLevel.ERROR, f"Failed to install {name} dependencies")
                return False
        return True
