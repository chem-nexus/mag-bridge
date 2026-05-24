"""Resolved paths, ports and platform constants for the MagBridge environment."""

from __future__ import annotations

import platform
import sys
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


def _resolve_root() -> Path:
    """Locate project root by walking up until requirements.txt is found."""
    return next(p for p in Path(__file__).resolve().parents if (p / "requirements.txt").exists())


class Settings(BaseSettings):
    """Environment-aware settings and resolved project paths."""

    model_config = SettingsConfigDict(env_prefix="MAGBRIDGE_", case_sensitive=False)

    root: Path = Field(default_factory=_resolve_root)
    product_name: str = "MagBridge"
    backend_appname: str = "backend_app"
    port_angular: int = 4200
    port_backend: int = 8000
    log_dir: Path = Field(default_factory=lambda: Path.home() / "magbridge")

    @property
    def frontend(self) -> Path:
        return self.root / "frontend"

    @property
    def electron(self) -> Path:
        return self.root / "electron"

    @property
    def backend_src(self) -> Path:
        return self.root / "backend"

    @property
    def venv_python(self) -> Path:
        if platform.system() == "Windows":
            candidate = self.root / ".venv" / "Scripts" / "python.exe"
        else:
            candidate = self.root / ".venv" / "bin" / "python"
        return candidate if candidate.exists() else Path(sys.executable)

    @property
    def venv_exists(self) -> bool:
        if platform.system() == "Windows":
            candidate = self.root / ".venv" / "Scripts" / "python.exe"
        else:
            candidate = self.root / ".venv" / "bin" / "python"
        return candidate.exists()

    @property
    def build_dir(self) -> Path:
        return self.frontend / "build"

    @property
    def package_target(self) -> Path:
        return self.build_dir / "app"

    @property
    def frontend_target(self) -> Path:
        return self.build_dir / "frontend"

    @property
    def backend_target(self) -> Path:
        return self.build_dir / "backend"

    @property
    def backend_entrypoint(self) -> Path:
        return self.backend_src / "main.py"

    @property
    def log_file(self) -> Path:
        return self.log_dir / "app.log"

    @property
    def eb_platform(self) -> str:
        system_name = platform.system()
        return "--win" if system_name == "Windows" else "--linux" if system_name == "Linux" else "--mac"

    @property
    def package_executable(self) -> Path:
        system_name = platform.system()
        if system_name == "Windows":
            return self.package_target / "win-unpacked" / f"{self.product_name}.exe"
        if system_name == "Linux":
            return self.package_target / "linux-unpacked" / self.product_name
        return self.package_target / "mac-arm64" / f"{self.product_name}.app" / "Contents" / "MacOS" / self.product_name


settings = Settings()
