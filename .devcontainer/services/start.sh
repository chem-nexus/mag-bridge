#!/usr/bin/env bash
set -euo pipefail

SERVICES_DIR="${PROJECT_DIR}/.devcontainer/services"

_wait_port() {
  local name="$1" port="$2" log="$3"
  for i in {1..20}; do
    sleep 0.5
    if nc -z 127.0.0.1 "$port" 2>/dev/null; then
      echo "[services] $name pid $(cat "/tmp/${name}.pid" 2>/dev/null || echo '?') — :${port} OK"
      return 0
    fi
  done
  echo "[services] ERROR: $name failed to bind :${port} after 10s"
  tail -n 30 "$log" 2>/dev/null || true
  return 1
}

# --- Loki ---
LOKI_BIN=/usr/local/bin/loki
if [ ! -x "$LOKI_BIN" ]; then
  echo "[services] loki binary missing — rebuild container (INSTALL_LOKI stage)"
elif nc -z 127.0.0.1 3100 2>/dev/null; then
  echo "[services] loki already listening on :3100"
else
  mkdir -p /tmp/loki/chunks /tmp/loki/rules
  # Strip OTEL exporter vars — they point at Loki's own port and cause a
  # self-referential schema conflict (opentelemetry schema 1.39/1.40 mismatch).
  nohup env \
    -u OTEL_EXPORTER_OTLP_ENDPOINT \
    -u OTEL_EXPORTER_OTLP_PROTOCOL \
    "$LOKI_BIN" -config.file="${SERVICES_DIR}/loki/loki.yaml" \
    >/tmp/loki.log 2>&1 &
  echo $! >/tmp/loki.pid
  _wait_port loki 3100 /tmp/loki.log
fi

# --- Grafana ---
GRAFANA_BIN=/usr/local/grafana/bin/grafana
if [ ! -x "$GRAFANA_BIN" ]; then
  echo "[services] grafana binary missing — rebuild container (INSTALL_GRAFANA stage)"
elif nc -z 127.0.0.1 3000 2>/dev/null; then
  echo "[services] grafana already listening on :3000"
else
  mkdir -p /tmp/grafana/data /tmp/grafana/logs /tmp/grafana/plugins
  nohup env \
    -u OTEL_EXPORTER_OTLP_ENDPOINT \
    -u OTEL_EXPORTER_OTLP_PROTOCOL \
    GF_PATHS_HOME=/usr/local/grafana \
    GF_PATHS_PROVISIONING="${SERVICES_DIR}/grafana/provisioning" \
    GF_PATHS_DATA=/tmp/grafana/data \
    GF_PATHS_LOGS=/tmp/grafana/logs \
    GF_PATHS_PLUGINS=/tmp/grafana/plugins \
    GF_SERVER_HTTP_PORT=3000 \
    GF_SECURITY_ADMIN_USER=admin \
    GF_SECURITY_ADMIN_PASSWORD=admin \
    GF_ANALYTICS_REPORTING_ENABLED=false \
    GF_ANALYTICS_CHECK_FOR_UPDATES=false \
    "$GRAFANA_BIN" server --homepath=/usr/local/grafana \
    >/tmp/grafana.log 2>&1 &
  echo $! >/tmp/grafana.pid
  _wait_port grafana 3000 /tmp/grafana.log
fi
