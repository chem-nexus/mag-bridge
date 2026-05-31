#!/bin/bash
set -euo pipefail

echo "[updateContentCommand]:: Starting Background Dependency Installation..."

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
# Kept under .devcontainer/ so devcontainer tooling stays separate from app code.
# PATH in devcontainer.json points at .devcontainer/node_modules/.bin so the
# binaries are reachable without `npx`.
if [ ! -d ".devcontainer/node_modules" ]; then
	echo "[updateContentCommand]:: Installing devcontainer tooling (claude, promptfoo, repomix)..."
	(cd .devcontainer && npm install)
else
	echo "[updateContentCommand]:: .devcontainer/node_modules exists. Skipping."
fi

# Symlink node_modules inside the promptfoo skill dir so Promptfoo's module resolver
# (which walks up from evals/ → promptfoo/) can find packages in .devcontainer/node_modules.
# Not committed to either repo — node_modules is gitignored in both.
PROMPTFOO_SKILL_DIR=".claude/skills/promptfoo"
if [ ! -L "${PROMPTFOO_SKILL_DIR}/node_modules" ]; then
	echo "[updateContentCommand]:: Linking ${PROMPTFOO_SKILL_DIR}/node_modules -> .devcontainer/node_modules..."
	ln -sf "$(pwd)/.devcontainer/node_modules" "${PROMPTFOO_SKILL_DIR}/node_modules"
else
	echo "[updateContentCommand]:: ${PROMPTFOO_SKILL_DIR}/node_modules symlink exists. Skipping."
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
    .venv/bin/playwright install chromium
else
    echo "[updateContentCommand]:: Playwright not installed, skipping browser download."
fi
