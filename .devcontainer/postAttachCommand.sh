#!/bin/bash
set -euo pipefail

echo "[postAttachCommand]:: Starting Dev Container Post-Attach Setup..."

# ------------------------------------------------------
# 1. AI SWITCH VS CODE EXTENSION
# ------------------------------------------------------
# Build + install the "AI Switch" extension. Delegated to scripts/ (kept there
# alongside ai-switch.py, the provider-switch logic it wraps). The helper uses
# the headless code-server binary, so it is immune to editor-IPC attach timing,
# and is idempotent + cached across restarts.
echo "[postAttachCommand]:: Installing AI Switch extension..."
bash .devcontainer/scripts/install-ai-switch-extension.sh

echo "[postAttachCommand]:: Exit"
