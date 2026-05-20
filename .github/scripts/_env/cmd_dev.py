"""Dev server commands: fullstack, frontend, backend, electron, stop."""

from __future__ import annotations

import os
import platform
import signal
import subprocess
import sys
import time
from typing import NoReturn

import click

from _env.config import settings
from _env.utils import EnvUtils, LogLevel, cli


@cli.command()
@click.option("--skip-install", is_flag=True, help="Skip npm install check")
def fullstack(skip_install: bool) -> NoReturn:
    """Start Angular + FastAPI backend (runs in container)."""
    EnvUtils.log(LogLevel.HEADER, "Starting MagBridge Full Stack Development Mode")

    click.echo("📦 Services:")
    click.echo(f"   - Angular dev server (port {settings.port_angular})")
    click.echo(f"   - FastAPI backend (port {settings.port_backend})")
    click.echo()

    if not EnvUtils.check_venv():
        sys.exit(1)
    if not skip_install and not EnvUtils.check_node_modules(settings.frontend, "Angular"):
        sys.exit(1)

    click.echo("🧹 Cleaning up existing processes...")
    EnvUtils.kill_port(settings.port_angular)
    EnvUtils.kill_port(settings.port_backend)

    processes: list[subprocess.Popen] = []

    def cleanup(signum: int | None = None, frame: object = None) -> NoReturn:
        click.echo("\n🛑 Stopping services...")
        for proc in processes:
            try:
                proc.terminate()
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
            except Exception:
                pass
        EnvUtils.kill_port(settings.port_angular)
        EnvUtils.kill_port(settings.port_backend)
        EnvUtils.log(LogLevel.SUCCESS, "All services stopped")
        sys.exit(0)

    signal.signal(signal.SIGINT, cleanup)
    signal.signal(signal.SIGTERM, cleanup)

    click.echo(f"🔧 Starting Backend on http://0.0.0.0:{settings.port_backend}...")
    env = os.environ.copy()
    env["NODE_ENV"] = "development"
    backend_proc = subprocess.Popen(
        [
            str(settings.venv_python),
            "-m",
            "uvicorn",
            "backend:app",
            "--reload",
            "--host",
            "0.0.0.0",
            "--port",
            str(settings.port_backend),
        ],
        cwd=settings.root,
        env=env,
    )
    processes.append(backend_proc)
    time.sleep(2)

    click.echo(f"🎨 Starting Angular on http://0.0.0.0:{settings.port_angular}...")
    angular_proc = subprocess.Popen(["npm", "run", "serve-reloader"], cwd=settings.frontend)
    processes.append(angular_proc)

    click.echo()
    EnvUtils.log(LogLevel.SUCCESS, "Services started!")
    click.echo(f"   📡 Backend:  http://localhost:{settings.port_backend} (PID: {backend_proc.pid})")
    click.echo(f"   📡 API Docs: http://localhost:{settings.port_backend}/docs")
    click.echo(f"   🌐 Angular:  http://localhost:{settings.port_angular} (PID: {angular_proc.pid})")
    click.echo()
    EnvUtils.log(LogLevel.WARN, "Press Ctrl+C to stop all services")
    click.echo()

    try:
        while True:
            for proc in processes:
                if proc.poll() is not None:
                    EnvUtils.log(LogLevel.ERROR, f"Process {proc.pid} exited with code {proc.returncode}")
                    cleanup()
            time.sleep(1)
    except KeyboardInterrupt:
        cleanup()

    sys.exit(0)


@cli.command()
def frontend() -> NoReturn:
    """Start Angular dev server only."""
    EnvUtils.log(LogLevel.HEADER, "Starting Angular Dev Server")

    if not EnvUtils.check_node_modules(settings.frontend, "Angular"):
        sys.exit(1)

    EnvUtils.kill_port(settings.port_angular)

    click.echo(f"🎨 Starting Angular on http://0.0.0.0:{settings.port_angular}...")
    try:
        subprocess.run(["npm", "run", "serve-reloader"], cwd=settings.frontend, check=True)
    except KeyboardInterrupt:
        click.echo("\n🛑 Angular stopped")
    except subprocess.CalledProcessError as e:
        EnvUtils.log(LogLevel.ERROR, f"Angular exited with code {e.returncode}")
        sys.exit(e.returncode)

    sys.exit(0)


@cli.command()
def backend() -> NoReturn:
    """Start FastAPI backend only."""
    EnvUtils.log(LogLevel.HEADER, "Starting FastAPI Backend")

    if not EnvUtils.check_venv():
        sys.exit(1)

    EnvUtils.kill_port(settings.port_backend)

    click.echo(f"🔧 Starting Backend on http://0.0.0.0:{settings.port_backend}...")
    env = os.environ.copy()
    env["NODE_ENV"] = "development"
    try:
        subprocess.run(
            [
                str(settings.venv_python),
                "-m",
                "uvicorn",
                "backend:app",
                "--reload",
                "--host",
                "0.0.0.0",
                "--port",
                str(settings.port_backend),
            ],
            cwd=settings.root,
            env=env,
            check=True,
        )
    except KeyboardInterrupt:
        click.echo("\n🛑 Backend stopped")
    except subprocess.CalledProcessError as e:
        EnvUtils.log(LogLevel.ERROR, f"Backend exited with code {e.returncode}")
        sys.exit(e.returncode)

    sys.exit(0)


@cli.command()
def electron() -> NoReturn:
    """Start Electron (run on the HOST machine outside the container)."""
    EnvUtils.log(LogLevel.HEADER, "Starting Electron Development Mode")

    EnvUtils.log(LogLevel.WARN, "Prerequisites:")
    click.echo("   1. Dev container must be running")
    click.echo(f"   2. Angular dev server must be running on port {settings.port_angular}")
    click.echo(f"   3. Backend must be running on port {settings.port_backend}")
    click.echo()

    if not EnvUtils.check_node_modules(settings.electron, "Electron"):
        sys.exit(1)

    # macOS Gatekeeper quarantines npm-downloaded binaries (ENOEXEC / errno -8).
    # Strip the attribute from the entire dist/ folder (works regardless of
    # exact binary path inside it).
    if platform.system() == "Darwin":
        electron_dist = settings.electron / "node_modules" / "electron" / "dist"
        if electron_dist.exists():
            EnvUtils.log(LogLevel.INFO, "Removing macOS quarantine from Electron binary...")
            subprocess.run(
                ["xattr", "-dr", "com.apple.quarantine", str(electron_dist)],
                stderr=subprocess.DEVNULL,
            )

    click.echo(f"⏳ Waiting for Angular dev server at http://localhost:{settings.port_angular}...")
    try:
        subprocess.run(["npm", "run", "dev"], cwd=settings.electron, check=True)
    except KeyboardInterrupt:
        click.echo("\n🛑 Electron stopped")
    except subprocess.CalledProcessError as e:
        EnvUtils.log(LogLevel.ERROR, f"Electron exited with code {e.returncode}")
        sys.exit(e.returncode)

    sys.exit(0)


@cli.command()
def stop() -> None:
    """Stop all development services."""
    EnvUtils.log(LogLevel.HEADER, "Stopping Development Services")

    killed_angular = EnvUtils.kill_port(settings.port_angular)
    killed_backend = EnvUtils.kill_port(settings.port_backend)

    if killed_angular:
        EnvUtils.log(LogLevel.SUCCESS, f"Killed process on port {settings.port_angular} (Angular)")
    if killed_backend:
        EnvUtils.log(LogLevel.SUCCESS, f"Killed process on port {settings.port_backend} (Backend)")

    if not killed_angular and not killed_backend:
        click.echo("No services were running")
    else:
        EnvUtils.log(LogLevel.SUCCESS, "All services stopped")
