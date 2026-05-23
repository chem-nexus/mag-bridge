"""Build and packaging commands: build-backend, build, info, clean."""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

import click

from _env.config import settings
from _env.utils import EnvUtils, LogLevel, cli

# ---------------------------------------------------------------------------
# Internal helper (shared by build-backend and build)
# ---------------------------------------------------------------------------


def _run_build_backend() -> None:
    """Build backend with PyInstaller.

    Uses sys.executable so it works both in a venv (local dev) and with a
    system Python (CI) — as long as the script is invoked with the right
    interpreter.
    """
    if settings.backend_target.exists():
        shutil.rmtree(settings.backend_target)
    for d in [
        settings.backend_target,
        settings.backend_target / ".pyi-work",
        settings.backend_target / ".pyi-specs",
    ]:
        d.mkdir(parents=True, exist_ok=True)

    EnvUtils.log(LogLevel.INFO, f"Building backend with PyInstaller → {settings.backend_target}")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "PyInstaller",
            "--name",
            settings.backend_appname,
            "--paths",
            str(settings.backend_src),
            "--distpath",
            str(settings.backend_target),
            "--workpath",
            str(settings.backend_target / ".pyi-work"),
            "--specpath",
            str(settings.backend_target / ".pyi-specs"),
            "--noconfirm",
            str(settings.backend_entrypoint),
        ],
        cwd=settings.root,
    )
    if result.returncode == 0:
        EnvUtils.log(LogLevel.SUCCESS, f"Backend packaged: {settings.backend_target}/{settings.backend_appname}")
    else:
        EnvUtils.log(LogLevel.ERROR, "Failed to package backend")
        sys.exit(result.returncode)


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------


@cli.command("build-backend")
def build_backend() -> None:
    """Build backend with PyInstaller."""
    EnvUtils.log(LogLevel.HEADER, "Building Backend")
    _run_build_backend()


@cli.command()
@click.option("--platform", "eb_platform", default=None, help="Electron builder platform flag (--mac, --win, --linux)")
@click.option("--extra", "eb_extra", default="", help="Extra electron-builder flags")
def build(eb_platform: str | None, eb_extra: str) -> None:
    """Build full app: backend + Angular + Electron packaging."""
    EnvUtils.log(LogLevel.HEADER, "Building MagBridge Full Stack")

    platform_flag = eb_platform or settings.eb_platform

    # 1. Backend
    _run_build_backend()

    # 2. Clean frontend / package targets
    for target in [settings.frontend_target, settings.package_target]:
        if target.exists():
            shutil.rmtree(target)

    # 3. Angular
    EnvUtils.log(LogLevel.INFO, "Installing frontend deps (npm ci)...")
    subprocess.run([EnvUtils.node_bin("npm"), "ci"], cwd=settings.frontend, check=True)
    EnvUtils.log(LogLevel.INFO, "Building Angular...")
    subprocess.run([EnvUtils.node_bin("npm"), "run", "build:prod"], cwd=settings.frontend, check=True)

    # 4. Electron
    EnvUtils.log(LogLevel.INFO, "Installing Electron deps (npm ci)...")
    r = subprocess.run([EnvUtils.node_bin("npm"), "ci"], cwd=settings.electron)
    if r.returncode != 0:
        EnvUtils.log(LogLevel.WARN, "Electron deps skipped (run 'cd electron && npm ci' on host)")

    EnvUtils.log(LogLevel.INFO, f"Packaging Electron ({platform_flag})...")
    cmd = [EnvUtils.node_bin("npx"), "electron-builder", platform_flag]
    if eb_extra:
        cmd.extend(eb_extra.split())
    r = subprocess.run(cmd, cwd=settings.electron)
    if r.returncode == 0:
        EnvUtils.log(LogLevel.SUCCESS, f"Electron packaged under {settings.package_target}")
    else:
        EnvUtils.log(LogLevel.ERROR, "Failed to package Electron (run on host if needed)")
        sys.exit(r.returncode)


@cli.command()
def info() -> None:
    """Print configuration info."""
    EnvUtils.log(LogLevel.HEADER, "MagBridge Configuration")
    rows = [
        ("ROOT_DIR", settings.root),
        ("HOME_DIR", Path.home()),
        ("BUILD_DIR", settings.build_dir),
        ("PACKAGE_TARGET", settings.package_target),
        ("PRODUCT_NAME", settings.product_name),
        ("FRONTEND_SRC", settings.frontend),
        ("FRONTEND_TARGET", settings.frontend_target),
        ("ELECTRON_SRC", settings.electron),
        ("BACKEND_APPNAME", settings.backend_appname),
        ("BACKEND_SRC", settings.backend_src),
        ("BACKEND_TARGET", settings.backend_target),
        ("BACKEND_ENTRYPOINT", settings.backend_entrypoint),
        ("LOG_DIR", settings.log_dir),
        ("LOG_FILE", settings.log_file),
        ("PACKAGE_EXECUTABLE", settings.package_executable),
        ("EB_PLATFORM", settings.eb_platform),
        ("PORT_ANGULAR", settings.port_angular),
        ("PORT_BACKEND", settings.port_backend),
    ]
    for key, val in rows:
        click.echo(f"   {click.style(key, bold=True):<30} = {val}")


@cli.command()
def clean() -> None:
    """Clean build outputs."""
    EnvUtils.log(LogLevel.HEADER, "Cleaning Build Outputs")
    for target in [settings.backend_target, settings.frontend_target, settings.package_target]:
        if target.exists():
            shutil.rmtree(target)
            EnvUtils.log(LogLevel.SUCCESS, f"Removed {target}")
        else:
            click.echo(f"   (already clean) {target}")
