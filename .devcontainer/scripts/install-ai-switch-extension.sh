#!/usr/bin/env bash
# Build + install the "AI Switch" VS Code extension into the dev container.
#
# Invoked from postAttachCommand (runs after the VS Code server attaches, so the
# `code` CLI exists — postStartCommand fires too early and the CLI is missing).
# Idempotent and cached: if the extension is already installed (survives container
# restarts), it exits immediately. Builds
# a minimal VSIX with `zip` (no vsce dependency) and lets `code --install-extension`
# register it, so VS Code's internal extension index is never hand-edited.
set -euo pipefail

EXT_SRC="$(cd "$(dirname "$0")/../extensions/ai-switch" && pwd)"
EXT_ID="magbridge.ai-switch"
VERSION="0.0.1"

# --- Resolve the VS Code Server CLI (not placed until the server attaches) ---
# Poll briefly: postAttachCommand normally runs after the CLI exists, but tolerate
# a slow attach rather than skipping. Globs are nullglob-guarded.
shopt -s nullglob
resolve_code() {
    local c
    c="$(command -v code 2>/dev/null || true)"
    [ -n "$c" ] && { echo "$c"; return; }
    for c in /vscode/vscode-server/bin/*/bin/remote-cli/code \
             "$HOME"/.vscode-server/bin/*/bin/remote-cli/code; do
        [ -x "$c" ] && { echo "$c"; return; }
    done
}
CODE=""
for _ in $(seq 1 20); do
    CODE="$(resolve_code)"
    [ -n "$CODE" ] && break
    sleep 1
done
if [ -z "$CODE" ]; then
    echo "[ai-switch] VS Code server CLI not found after waiting; skipping."
    exit 0
fi

# --- Cached: skip if already installed ---
if "$CODE" --list-extensions 2>/dev/null | grep -qix "$EXT_ID"; then
    echo "[ai-switch] Extension already installed."
    exit 0
fi

# --- Build a minimal VSIX (OPC zip) — no vsce ---
BUILD="$(mktemp -d)"
VSIX="$(mktemp -u --suffix=.vsix)"
trap 'rm -rf "$BUILD" "$VSIX"' EXIT

mkdir -p "$BUILD/extension"
cp "$EXT_SRC/package.json" "$EXT_SRC/extension.js" "$EXT_SRC/README.md" "$BUILD/extension/"

cat > "$BUILD/extension.vsixmanifest" <<EOF
<?xml version="1.0" encoding="utf-8"?>
<PackageManifest Version="2.0.0" xmlns="http://schemas.microsoft.com/developer/vsx-schema/2011">
  <Metadata>
    <Identity Language="en-US" Id="ai-switch" Version="${VERSION}" Publisher="magbridge" />
    <DisplayName>AI Switch</DisplayName>
    <Description>Switch Claude Code provider with auto-reload</Description>
  </Metadata>
  <Installation>
    <InstallationTarget Id="Microsoft.VisualStudio.Code" />
  </Installation>
  <Assets>
    <Asset Type="Microsoft.VisualStudio.Code.Manifest" Path="extension/package.json" Addressable="true" />
  </Assets>
</PackageManifest>
EOF

cat > "$BUILD/[Content_Types].xml" <<EOF
<?xml version="1.0" encoding="utf-8"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="json" ContentType="application/json" />
  <Default Extension="js" ContentType="application/javascript" />
  <Default Extension="md" ContentType="text/markdown" />
  <Default Extension="vsixmanifest" ContentType="text/xml" />
</Types>
EOF

( cd "$BUILD" && zip -q -r -X "$VSIX" . )

echo "[ai-switch] Installing extension..."
if "$CODE" --install-extension "$VSIX" --force >/dev/null 2>&1; then
    echo "[ai-switch] Installed. Reload the window to activate."
else
    echo "[ai-switch] Install failed (non-fatal)." >&2
fi
