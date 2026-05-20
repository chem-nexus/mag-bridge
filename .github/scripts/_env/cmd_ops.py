"""Operational commands: run, logs, remove-quarantine."""

from __future__ import annotations

import platform
import subprocess
import sys

import click

from _env.config import settings
from _env.utils import EnvUtils, LogLevel, cli


@cli.command("run")
def run_app() -> None:
    """Run the packaged MagBridge app."""
    EnvUtils.log(LogLevel.HEADER, "Running Packaged App")
    settings.log_dir.mkdir(parents=True, exist_ok=True)
    if settings.log_file.exists():
        settings.log_file.unlink()

    EnvUtils.log(LogLevel.INFO, f"Launching: {settings.package_executable}")
    try:
        subprocess.run([str(settings.package_executable)], check=True)
    except FileNotFoundError:
        EnvUtils.log(LogLevel.ERROR, f"Executable not found: {settings.package_executable}")
        EnvUtils.log(LogLevel.WARN, "Run 'python scripts/environment.py build' first")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        EnvUtils.log(LogLevel.ERROR, f"App exited with code {e.returncode}")
        sys.exit(e.returncode)


@cli.command()
def logs() -> None:
    """Tail app logs."""
    settings.log_dir.mkdir(parents=True, exist_ok=True)
    EnvUtils.log(LogLevel.INFO, f"Tailing logs at: {settings.log_file}")
    try:
        if platform.system() == "Windows":
            subprocess.run(
                ["powershell", "-Command", f"Get-Content -Wait -Path '{settings.log_file}'"],
                check=True,
            )
        else:
            subprocess.run(["tail", "-f", str(settings.log_file)], check=True)
    except KeyboardInterrupt:
        click.echo("\n🛑 Log tailing stopped")
