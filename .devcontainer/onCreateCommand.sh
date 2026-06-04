#!/bin/bash
set -euo pipefail

echo '==> [Lifecycle: onCreateCommand] Base OS built. Workspace not mounted yet.'
echo '==> [Lifecycle: onCreateCommand] Starting Dev Container On-Create Setup...'

# ------------------------------------------------------
# START IRON PROXY
# ------------------------------------------------------
# Starts the network egress proxy to route workload traffic, reach agents,
# and monitor telemetry before any content update or dependency resolution runs.
echo "[onCreateCommand]:: Starting Iron Proxy..."
bash .devcontainer/iron-proxy/start.sh && echo "[onCreateCommand]:: Iron Proxy started successfully." || echo "[onCreateCommand]:: Failed to start Iron Proxy. Check logs for details."

echo "[onCreateCommand]:: Exit"


