#!/usr/bin/env bash
set -euo pipefail

BIN=/usr/local/bin/iron-proxy
CFG="${IRON_PROXY_CONFIG:-${PROJECT_DIR}/.devcontainer/iron-proxy/proxy.yaml}"

if [ ! -d ""${PROJECT_DIR}"" ] && [ "$CFG" = ""${PROJECT_DIR}"/.devcontainer/iron-proxy/proxy.yaml" ]; then
  CFG=".devcontainer/iron-proxy/proxy.yaml"
fi

if ! command -v "$BIN" >/dev/null 2>&1; then
  echo "[iron-proxy] binary missing — rebuild the container (iron-proxy build stage in Dockerfile)"
  exit 1
fi
if nc -z 0.0.0.0 8080 2>/dev/null; then
  echo "[iron-proxy] already listening on :8080 — nothing to do"
  exit 0
fi

echo "[iron-proxy] starting $("$BIN" --version) with config $CFG"
nohup env -u HTTPS_PROXY -u HTTP_PROXY -u https_proxy -u http_proxy "$BIN" -config "$CFG" >/tmp/iron-proxy.log 2>&1 &
PID=$!

SUCCESS=0
for i in {1..10}; do
  sleep 0.5
  if nc -z 0.0.0.0 8080 2>/dev/null; then
    SUCCESS=1
    break
  fi
  if ! kill -0 $PID 2>/dev/null; then
    break
  fi
done

if [ $SUCCESS -eq 0 ]; then
  echo "[iron-proxy] CRITICAL ERROR: Proxy failed to start or bind to :8080"
  tail -n 15 /tmp/iron-proxy.log || true
  exit 1
fi

echo "[iron-proxy] pid $PID — audit log: /tmp/iron-proxy.log (JSON lines)"
