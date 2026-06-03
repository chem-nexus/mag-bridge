#!/usr/bin/env bash
# Build + install the "AI Switch" VS Code extension into the dev container.
#
# Invoked from postAttachCommand. We deliberately use the HEADLESS server binary
# (bin/code-server), NOT the remote-cli `code`. The remote-cli routes extension
# commands through the editor's IPC socket (VSCODE_IPC_HOOK_CLI), which is not
# ready when postAttach fires — so `code --install-extension` failed with
# "code or code-insiders is not installed". code-server manages the extensions
# dir directly: no IPC, no running window, no attach-timing dependency.
# Idempotent and cached: if already installed it exits immediately. Builds a
# minimal VSIX with `zip` (no vsce dependency).
set -euo pipefail

EXT_SRC="$(cd "$(dirname "$0")/../extensions/ai-switch" && pwd)"
EXT_ID="magbridge.ai-switch"
VERSION="0.0.1"

# --- Resolve the headless code-server binary (unpacked when the server installs) ---
# Poll briefly: tolerate a slow server unpack rather than skipping. Only the file
# on disk is needed — code-server needs no running server. Globs are nullglob-guarded.
shopt -s nullglob
resolve_code_server() {
    local c
    for c in /vscode/vscode-server/bin/*/bin/code-server \
             "$HOME"/.vscode-server/bin/*/bin/code-server; do
        [ -x "$c" ] && { echo "$c"; return; }
    done
}
CODE=""
for _ in $(seq 1 20); do
    CODE="$(resolve_code_server)"
    [ -n "$CODE" ] && break
    sleep 1
done
if [ -z "$CODE" ]; then
    echo "[ai-switch] code-server binary not found after waiting; skipping." >&2
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
# Surface install output (don't swallow it) and fail loudly. Silently dropping
# this is what left fresh clients with no extension and no error.
if ! "$CODE" --install-extension "$VSIX" --force; then
    echo "[ai-switch] ERROR: 'code-server --install-extension' failed (see output above)." >&2
    exit 1
fi

# Verify it actually registered — --install-extension can exit 0 without
# persisting. Never let a broken bootstrap pass quietly again.
if "$CODE" --list-extensions 2>/dev/null | grep -qix "$EXT_ID"; then
    echo "[ai-switch] Installed: $EXT_ID. Reload the window to activate."
else
    echo "[ai-switch] ERROR: $EXT_ID not present after install — bootstrap failed." >&2
    exit 1
fi
