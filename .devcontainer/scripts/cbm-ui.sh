#!/usr/bin/env bash
# cbm-ui.sh — Spawn the codebase-memory-mcp graph UI in the foreground.
#
# Usage:
#   bash .devcontainer/scripts/cbm-ui.sh
#
# Then open http://localhost:9749 in your browser.
# Port 9749 is already forwarded by devcontainer.json.
#
# Ctrl+C (or closing the terminal) tears the server down completely — the binary
# and any child workers are killed and the port is freed. This process is
# independent of Claude Code's STDIO MCP session; both share CBM_CACHE_DIR.
set -euo pipefail

BIN=/usr/local/bin/codebase-memory-mcp
PORT=9749

"$BIN" --ui=true --host=0.0.0.0 --port="$PORT" &
SERVER_PID=$!

cleanup() {
    trap - INT TERM EXIT
    echo
    echo "==> Stopping CBM UI (PID ${SERVER_PID})..."

    # Children first, then the server itself — graceful TERM.
    pkill -TERM -P "$SERVER_PID" 2>/dev/null || true
    kill -TERM "$SERVER_PID" 2>/dev/null || true

    # Wait up to ~3s for a clean exit, then force-kill anything left.
    for _ in $(seq 1 15); do
        kill -0 "$SERVER_PID" 2>/dev/null || break
        sleep 0.2
    done
    pkill -KILL -P "$SERVER_PID" 2>/dev/null || true
    kill -KILL "$SERVER_PID" 2>/dev/null || true

    # Guaranteed backstop: free the port no matter what still holds it.
    fuser -k "${PORT}/tcp" 2>/dev/null || true

    echo "==> Stopped. Port ${PORT} released."
}
trap cleanup INT TERM EXIT

echo "==> CBM UI running (PID ${SERVER_PID}) → http://localhost:${PORT}"
echo "==> Press Ctrl+C to stop."
wait "$SERVER_PID"
