#!/usr/bin/env python3
"""Switch the VS Code AI extension backend between providers.

Usage (via shell alias `ai-switch`):
  ai-switch              # toggle local <-> anthropic
  ai-switch local        # route to LOCAL_BASE_URL (self-hosted, e.g. LM Studio)
  ai-switch gemini       # route to GEMINI_BASE_URL
  ai-switch anthropic    # restore Anthropic Claude Code (Pro OAuth, no override)
  ai-switch status       # show current mode

Mechanism:
  Writes .vscode/settings.json -> claudeCode.environmentVariables to override
  devcontainer.json without a container rebuild/restart. The extension reads it
  on window load, so after switching run:
    Cmd+Shift+P -> "Developer: Reload Window"

Provider endpoints come from .env (host) and are passed into the container.
`anthropic` writes an empty settings.json (no override -> falls back to Pro OAuth).
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from urllib.parse import urlparse

_here = Path(__file__).resolve()
ROOT_DIR: Path = next(p for p in _here.parents if (p / "requirements.txt").exists() or (p / ".claude").is_dir())
SETTINGS_FILE = ROOT_DIR / ".vscode" / "settings.json"

# Provider override profiles. `anthropic` is intentionally absent — it means
# "no override", which restores the extension's default Pro OAuth routing.
PROVIDERS: dict[str, dict[str, str]] = {
    "local": {
        "ANTHROPIC_BASE_URL": os.environ.get("LOCAL_BASE_URL", ""),
        "ANTHROPIC_AUTH_TOKEN": os.environ.get("LOCAL_AUTH_TOKEN", "dummy"),
    },
    "gemini": {
        "ANTHROPIC_BASE_URL": os.environ.get("GEMINI_BASE_URL", ""),
        "ANTHROPIC_AUTH_TOKEN": os.environ.get("GEMINI_AUTH_TOKEN", ""),
    },
}


def _normalize_url(url: str) -> str:
    """Ensure the endpoint has a scheme (Anthropic SDK requires one)."""
    if url and "://" not in url:
        return f"http://{url}"
    return url


def _current_mode() -> str:
    if not SETTINGS_FILE.exists():
        return "anthropic"
    try:
        data = json.loads(SETTINGS_FILE.read_text())
    except (json.JSONDecodeError, OSError):
        return "anthropic"
    url = ""
    for entry in data.get("claudeCode.environmentVariables", []):
        if entry.get("name") == "ANTHROPIC_BASE_URL":
            url = entry.get("value", "")
    if not url:
        return "anthropic"
    for name, env in PROVIDERS.items():
        if _normalize_url(env["ANTHROPIC_BASE_URL"]) == url:
            return name
    return "custom"


def _reload_hint() -> None:
    print("\n  Reload window to apply:")
    print("  Cmd+Shift+P  ->  'Developer: Reload Window'")


def switch_to(provider: str) -> None:
    env = PROVIDERS[provider]
    base_url = _normalize_url(env["ANTHROPIC_BASE_URL"])
    if not base_url:
        print(f"error: {provider} endpoint not configured (set its *_BASE_URL in .env)", file=sys.stderr)
        sys.exit(1)
    settings = {
        "claudeCode.environmentVariables": [
            {"name": "ANTHROPIC_BASE_URL", "value": base_url},
            {"name": "ANTHROPIC_AUTH_TOKEN", "value": env["ANTHROPIC_AUTH_TOKEN"]},
        ]
    }
    SETTINGS_FILE.write_text(json.dumps(settings, indent=2) + "\n")
    print(f"✓ {provider.upper()}  ->  {base_url}")
    _reload_hint()


def switch_to_anthropic() -> None:
    SETTINGS_FILE.write_text("{}\n")
    print("✓ ANTHROPIC  ->  Claude Code Pro (no override)")
    _reload_hint()


def show_status() -> None:
    mode = _current_mode()
    if mode in PROVIDERS:
        print(f"Mode: {mode.upper()}  ->  {_normalize_url(PROVIDERS[mode]['ANTHROPIC_BASE_URL'])}")
    elif mode == "anthropic":
        print("Mode: ANTHROPIC  ->  Claude Code Pro")
    else:
        print("Mode: CUSTOM  ->  unrecognized override in settings.json")


def main() -> None:
    cmd = sys.argv[1].lower() if len(sys.argv) > 1 else "toggle"

    if cmd == "toggle":
        switch_to_anthropic() if _current_mode() == "local" else switch_to("local")
    elif cmd in PROVIDERS:
        switch_to(cmd)
    elif cmd == "anthropic":
        switch_to_anthropic()
    elif cmd in ("status", "s"):
        show_status()
    else:
        print(f"Usage: ai-switch [{'|'.join(PROVIDERS)}|anthropic|status]", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
