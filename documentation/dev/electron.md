# MagBridge Electron Development Guide

## Purpose

> **Goal:** Run the Electron wrapper on the host OS while connecting to the Angular frontend and FastAPI backend inside the Dev Container.

## Architecture Overview

```
┌─────────────────────────────────────┐
│  Host OS                            │
│  ┌───────────────────────────────┐  │
│  │  Electron (electron/)         │  │
│  │  → Loads http://localhost:4200│  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
              ↓ (port forwarding)
┌─────────────────────────────────────┐
│  Dev Container (Linux)              │
│  ┌───────────────────────────────┐  │
│  │  Angular Dev Server :4200     │  │
│  │  FastAPI Backend    :8000     │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

## Requirements

- **Host OS:** macOS, Windows (10/11 with Docker Desktop), or Linux
- **Node.js 22+** installed on host
- Dev Container running with ports 4200 and 8000 forwarded

## Setup (First Time)

> [!IMPORTANT]
> Run these commands on the host OS.

```bash
cd electron
npm install
```

## Development Workflow

### 1) Start Dev Container Services

> [!NOTE]
> Use either the environment CLI or manual commands.

```bash
# Terminal 1 (in Dev Container)
./environment fullstack
```

Or manually:

```bash
# Terminal 1 (in Dev Container)
cd frontend
npm run serve-reloader  # http://0.0.0.0:4200

# Terminal 2 (in Dev Container)
cd /workspaces/mag-bridge
uv run uvicorn backend:app --reload --host 0.0.0.0 --port 8000  # http://0.0.0.0:8000
```

### 2) Start Electron

```bash
cd electron
npm run dev
```

**Expected behavior:**
- Electron waits for `http://localhost:4200` (or `host.docker.internal:4200` on Windows)
- Opens an Electron window for the Angular app
- HMR works for both Electron and browser

## Production Build

```bash
cd /path/to/mag-bridge
./environment build
```

**Build output:**
1. Angular → `frontend/build/frontend/`
2. Backend → `frontend/build/backend/`
3. Electron → `frontend/build/app/`

**Result artifacts:**
- macOS: `frontend/build/app/mac-arm64/MagBridge.app`
- Windows: `frontend/build/app/win-unpacked/MagBridge.exe`
- Linux: `frontend/build/app/MagBridge-0.0.0.AppImage`

## Configuration

> [!IMPORTANT]
> All configuration lives in `app-config.js`.

### Environment Variables

- `NODE_ENV` - `development` or `production`
- `MANAGE_BACKEND` - set to `1` to let Electron manage the backend process
- `BACKEND_CMD` - Python executable (default: `python3`)
- `BACKEND_CWD` - working directory for backend (default: `../`)

### Development Overrides

```bash
UVICORN_PORT=8080 npm run dev
MANAGE_BACKEND=0 npm run dev
BACKEND_CMD=/usr/local/bin/python3.12 npm run dev
```

## File Map

```
electron/
├── package.json        # Electron dependencies
├── main.js            # Main process (window + IPC)
├── preload.js         # Context bridge (security layer)
├── logging.js         # Unified logging system
├── app-config.js      # Configuration resolver
└── README.md          # Original upstream README
```

## Troubleshooting

### Electron cannot connect to Angular

> [!NOTE]
> Check these in order:

1. Angular dev server runs in browser: `http://localhost:4200`
2. Port 4200 is forwarded from container to host
3. No firewall blocks localhost connections

**Windows-specific:**
- If `localhost:4200` fails, Electron tries `host.docker.internal:4200`
- Ensure Docker Desktop runs with WSL2 backend
- Verify Docker Desktop → Settings → Resources → WSL Integration

### Backend does not start

> [!NOTE]
> Check these in order:

1. `MANAGE_BACKEND=1` is set
2. Python virtual environment exists at `../.venv`
3. Dependencies installed: `uv pip install -r requirements.txt`

### Build fails on macOS

> [!NOTE]
> Check these in order:

1. Xcode CLI tools installed: `xcode-select --install`
2. Node.js version is 22+: `node --version`
3. Clean install: `rm -rf node_modules && npm install`

### Build fails on Windows

> [!NOTE]
> Check these in order:

1. Node.js version is 22+: `node --version`
2. Windows Build Tools installed (if needed): `npm install --global windows-build-tools`
3. Clean install: `rmdir /s node_modules && npm install`

## Security Defaults

> [!IMPORTANT]
> Electron security flags are enforced in the main process.

- `contextIsolation: true`
- `nodeIntegration: false`
- Secure IPC via `window.electronAPI`

## Logs

Development logs:
```bash
tail -f ~/magbridge-dev/app.log
```

Production logs:
```bash
tail -f ~/magbridge/app.log
```

## Related Documentation

- [Dev Container Setup](devcontainers.md)
- [Frontend (Angular)](../../frontend/README.md)
- [Environment CLI Launcher](../../environment)
- [Environment CLI Source](../../.github/scripts/environment.py)
