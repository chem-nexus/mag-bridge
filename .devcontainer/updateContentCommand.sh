#!/bin/bash
set -euo pipefail

echo '==> [Lifecycle: updateContentCommand] Ensuring Developer Dependencies...'

# ------------------------------------------------------
# 1. ENVIRONMENT INFRASTRUCTURE SETUP
# ------------------------------------------------------
if [ ! -d ".venv" ]; then
	echo "[updateContentCommand]:: Creating fresh Linux-native virtual environment..."
	uv venv --clear --seed .venv
else
	echo "[updateContentCommand]:: Virtual environment exists."
fi

# ------------------------------------------------------
# 2. APPLICATION DEPENDENCY INSTALLATION
# ------------------------------------------------------
# Devcontainer Tooling Dependencies — Claude Code CLI, Promptfoo, Repomix.
# package.json + node_modules both live in .devcontainer/ (single source of truth).
# A symlink ./node_modules -> .devcontainer/node_modules is created at the workspace root
# so Promptfoo's module resolver (which walks up from .claude/skills/promptfoo/evals/)
# can find packages without any symlink inside the .claude/ submodule.
if [ ! -d ".devcontainer/node_modules" ]; then
	echo "[updateContentCommand]:: Installing devcontainer tooling (claude, promptfoo, repomix)..."
	(cd .devcontainer && npm install)
else
	echo "[updateContentCommand]:: .devcontainer/node_modules exists. Skipping."
fi
# Remove old symlink inside .claude/ submodule if it exists from a previous setup.
unlink ".claude/skills/promptfoo/node_modules" 2>/dev/null || true
# Workspace-root symlink for Promptfoo resolver — not committed (node_modules gitignored).
if [ ! -e "node_modules" ]; then
	echo "[updateContentCommand]:: Linking ./node_modules -> .devcontainer/node_modules..."
	ln -sf .devcontainer/node_modules node_modules
else
	echo "[updateContentCommand]:: ./node_modules exists. Skipping."
fi

# Python Dependencies
echo "[updateContentCommand]:: Installing Python requirements via uv..."
uv pip install -r requirements.txt -r requirements-ci.txt -r requirements-dev.txt

# Playwright Chromium browser binary — version tied to playwright in requirements-dev.txt.
# OS-level deps are baked into the Dockerfile image (INSTALL_CHROMIUM=1).
# Cached across rebuilds via PLAYWRIGHT_BROWSERS_PATH (persisted under the workspace bind
# mount); `playwright install` is idempotent and re-downloads only when the pinned version bumps.
if .venv/bin/python -c "import playwright" 2>/dev/null; then
    echo "[updateContentCommand]:: Installing Playwright Chromium browser..."
    .venv/bin/playwright install chromium && echo "[updateContentCommand]:: Playwright Chromium browser installation complete."
else
    echo "[updateContentCommand]:: Playwright not installed, skipping browser download."
fi
