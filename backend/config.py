from pathlib import Path

from fastapi import HTTPException
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


def _resolve_workspace_root() -> Path:
    return next(p for p in Path(__file__).resolve().parents if (p / "requirements.txt").exists())


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="", case_sensitive=False)

    workspace_root: Path = Field(default_factory=_resolve_workspace_root)
    app_data_dir: Path | None = Field(default=None, validation_alias="APP_DATA_DIR")
    app_data_dir_from_env: bool = False
    node_env: str | None = Field(default=None, validation_alias="NODE_ENV")
    sdf_dir: Path = Field(default_factory=Path)

    def model_post_init(self, __context: object) -> None:
        app_dir_from_env = self.app_data_dir is not None
        data_dir = (self.app_data_dir or (self.workspace_root / "data")).resolve()
        sdf_dir = data_dir / "sdf"
        sdf_dir.mkdir(parents=True, exist_ok=True)

        object.__setattr__(self, "app_data_dir", data_dir)
        object.__setattr__(self, "sdf_dir", sdf_dir)
        object.__setattr__(self, "app_data_dir_from_env", app_dir_from_env)

    @property
    def is_dev_mode(self) -> bool:
        return (self.node_env or "").lower() == "development"


settings = Settings()


def translate_path(path_str: str) -> Path:
    """
    Translate file path between host and container filesystems.

    Dev Mode (Electron on macOS + Backend in container):
        - Translates macOS workspace paths to container paths
        - /Users/*/mag-bridge/* → /workspaces/mag-bridge/*
        - Only allows files within workspace for security

    Prod Mode (Packaged app):
        - No translation, uses path as-is
        - Full system access

    Args:
        path_str: File path from Electron (macOS path in dev mode)

    Returns:
        Path object pointing to file in container (dev) or host (prod)

    Raises:
        HTTPException: If file not accessible in dev mode
    """
    if not settings.is_dev_mode:
        # Production mode: use path directly (Electron and backend on same system)
        return Path(path_str)

    # Development mode: translate macOS path to container path
    path = Path(path_str)

    # Try to find 'mag-bridge' in path components
    parts = path.parts
    try:
        # Find workspace root in path
        idx = None
        for i, part in enumerate(parts):
            if part == "mag-bridge":
                idx = i
                break

        if idx is None:
            raise ValueError("workspace_not_found")

        # Rebuild path from mag-bridge onwards
        # /Users/user/projects/mag-bridge/data/file.sdf → data/file.sdf
        relative_parts = parts[idx + 1 :]
        if not relative_parts:
            raise ValueError("invalid_path")

        relative = Path(*relative_parts)
        container_path = settings.workspace_root / relative

        # Verify file exists in container
        if not container_path.exists():
            raise HTTPException(status_code=404, detail=f"File not found in workspace: {relative}")

        # Verify file is within workspace (security check)
        try:
            container_path.resolve().relative_to(settings.workspace_root)
        except ValueError:
            raise HTTPException(status_code=403, detail="Access denied: File outside workspace")

        return container_path

    except ValueError as e:
        if str(e) == "workspace_not_found":
            raise HTTPException(status_code=400, detail="Dev mode: Please select file from workspace folder (e.g., mag-bridge/data/sdf/)")
        raise HTTPException(status_code=400, detail=f"Invalid file path: {path_str}")
