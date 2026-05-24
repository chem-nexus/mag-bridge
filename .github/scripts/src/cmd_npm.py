"""npm dependency management commands: install, npm-update, list-outdated, update-lock, rebuild-node."""

from __future__ import annotations

import shutil
import subprocess
import sys

import click

from src.config import settings
from src.utils import EnvUtils, LogLevel, cli


@cli.command()
@click.option("--frontend-only", is_flag=True, help="Install frontend deps only")
@click.option("--electron-only", is_flag=True, help="Install electron deps only")
def install(frontend_only: bool, electron_only: bool) -> None:
    """Install npm dependencies."""
    EnvUtils.log(LogLevel.HEADER, "Installing Dependencies")

    if not frontend_only and not electron_only:
        EnvUtils.log(LogLevel.INFO, "Installing Frontend dependencies...")
        subprocess.run([EnvUtils.node_bin("npm"), "install"], cwd=settings.frontend, check=True)
        EnvUtils.log(LogLevel.WARN, "For Electron, run 'python scripts/environment.py install --electron-only' on the host machine")
    elif frontend_only:
        EnvUtils.log(LogLevel.INFO, "Installing Frontend dependencies...")
        subprocess.run([EnvUtils.node_bin("npm"), "install"], cwd=settings.frontend, check=True)
    elif electron_only:
        EnvUtils.log(LogLevel.INFO, "Installing Electron dependencies...")
        subprocess.run([EnvUtils.node_bin("npm"), "install"], cwd=settings.electron, check=True)

    EnvUtils.log(LogLevel.SUCCESS, "Dependencies installed")


@cli.command("npm-update")
def npm_update() -> None:
    """Update frontend npm dependencies via npm-check-updates."""
    EnvUtils.log(LogLevel.HEADER, "Updating Frontend npm Dependencies")
    EnvUtils.log(LogLevel.INFO, "Checking for updates with npm-check-updates...")
    subprocess.run(
        [EnvUtils.node_bin("npm"), "exec", "npm-check-updates", "--", "--packageFile", "package.json", "--upgrade"],
        cwd=settings.frontend,
        check=True,
    )
    EnvUtils.log(LogLevel.INFO, "Installing updated dependencies...")
    result = subprocess.run([EnvUtils.node_bin("npm"), "install"], cwd=settings.frontend)
    if result.returncode == 0:
        EnvUtils.log(LogLevel.SUCCESS, "npm dependencies updated")
    else:
        EnvUtils.log(LogLevel.ERROR, "npm dependencies update FAILED")
        sys.exit(result.returncode)


@cli.command("list-outdated")
def list_outdated() -> None:
    """List outdated frontend npm dependencies."""
    subprocess.run([EnvUtils.node_bin("npm"), "outdated", "--long"], cwd=settings.frontend)


@cli.command("update-lock")
def update_lock() -> None:
    """Update frontend package-lock.json without installing."""
    EnvUtils.log(LogLevel.INFO, "Updating package-lock.json...")
    subprocess.run([EnvUtils.node_bin("npm"), "install", "--package-lock-only"], cwd=settings.frontend, check=True)
    EnvUtils.log(LogLevel.SUCCESS, "package-lock.json updated")


@cli.command("rebuild-node")
def rebuild_node() -> None:
    """Reset frontend lockfile and reinstall node_modules."""
    EnvUtils.log(LogLevel.HEADER, "Rebuilding Frontend Node Dependencies")
    lock = settings.frontend / "package-lock.json"
    modules = settings.frontend / "node_modules"

    EnvUtils.log(LogLevel.INFO, "Removing package-lock.json and node_modules...")
    if lock.exists():
        lock.unlink()
    if modules.exists():
        shutil.rmtree(modules)

    EnvUtils.log(LogLevel.INFO, "Installing dependencies from scratch...")
    result = subprocess.run([EnvUtils.node_bin("npm"), "install"], cwd=settings.frontend)
    if result.returncode == 0:
        EnvUtils.log(LogLevel.SUCCESS, "Lockfile regenerated and dependencies reinstalled")
    else:
        EnvUtils.log(LogLevel.ERROR, "Failed to reset lockfile or reinstall dependencies")
        sys.exit(result.returncode)
