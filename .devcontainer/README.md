# Setup

One-time onboarding onto the shared **AI devcontainer platform**. The two private components — `.claude/`
and `devcontainers/` — are git **submodules**; one interactive script pulls them and writes your config.

## Onboarding

From the repo root:

```bash
bash .devcontainer/setup.sh
```

It prompts you to **paste your read-only token** (input hidden — never in your shell history), saves it to
`.env`, and fetches the submodules. Then set two values in `.env` and **Reopen in Container** (VS Code):

| key                         | value                                                                 |
| --------------------------- | --------------------------------------------------------------------- |
| `COMPOSE_PROJECT_NAME`      | unique, lowercase (e.g. `dev-jane`) — names your containers + volumes |
| `DEVCONTAINER_INGRESS_PORT` | a unique port, one per repo (`7700`, `7701`, …)                       |

(API keys like `CONTEXT7_API_KEY`, `TAVILY_API_KEY` are optional — blank = that MCP server stays off.)

That's it — reopen brings up your per-project stack (gateway, ingress, observability).

## Add your own services

Your repo can run its own containers — a database, a web app, a workflow engine, anything — **alongside** the
workspace, **without touching the `devcontainers/` platform**. It's two per-repo files.

**1. Declare it** in `.devcontainer/docker-compose.client.yaml` (this file merges over the platform stack). The
example uses `busybox` as a stand-in — **swap it for your real image** (for example `postgres`, `redis`, a
FastAPI, a workflow engine):

```yaml
services:
  my-service: # name it whatever you like
    image: busybox # ← your image here
    command: ["httpd", "-f", "-p", "8080"] # whatever runs your service
    networks: [central-gateway-internal] # the shared wall the workspace lives on
```

**2. Turn it on** in `.devcontainer/devcontainer.json` — add the file, then list the service so it boots with
the workspace:

```jsonc
"dockerComposeFile": [
  "../devcontainers/docker-compose.yaml",
  "docker-compose.client.yaml"          // <- your file, second (merges over the base)
],
"runServices": ["workspace", "my-service"]
```

**3. Rebuild Container.** Your service appears in the **same project box** in Docker Desktop as the workspace.
Need more than one? Add each service to the file and to `runServices` — same pattern.

### Reaching it

| From                           | How                                              | Example                                   |
| ------------------------------ | ------------------------------------------------ | ----------------------------------------- |
| your code (workspace)          | service **name** on the shared network           | `my-service:8080`                         |
| the host / browser (HTTP only) | `‹service›.‹port›.‹project›.localhost:‹ingress›` | `my-service.8080.dev-jane.localhost:7700` |

- **TCP services stay internal** — a database (for example Postgres, Redis, Mongo) is reached by name from your
  code; it gets no browser URL and doesn't need one.
- **Web UIs get a host URL** through the ingress automatically — the port rides in the subdomain, no per-service
  config. Behind the admin `basic_auth` gate (user `admin`). `‹project›` = your `COMPOSE_PROJECT_NAME`,
  `‹ingress›` = your `DEVCONTAINER_INGRESS_PORT`.
- **Everything joins `central-gateway-internal`** — the same no-internet wall as the workspace, so Docker DNS
  resolves the service names for you.
- **Data is ephemeral** unless you add a named volume (`volumes: [mydata:/path]` + a top-level `volumes: { mydata: {} }`).
  Only ever use your **own** volumes — never mount a platform/infrastructure volume.

## The token

One **read-only** fine-grained PAT with access to both submodule repos:

- repos `Sevelantis/.claude` + `Sevelantis/devcontainers`, **Contents: Read-only**
- create at <https://github.com/settings/tokens?type=beta>

`setup.sh` asks for it and stores it as `GH_TOKEN_RO` in `.env` (gitignored, `0600`). Add `GH_TOKEN_RW` only if
you push from inside the container.

## Prerequisites

- Docker + VS Code with the **Dev Containers** extension

## How it works

- **`setup.sh`** — interactive onboarding: runs `scaffold.sh`, prompts for the token (hidden — never in shell
  history, argv, or logs), writes it to `.env`, then **adds** the submodules (clone + register on a fresh repo,
  or updates them if present). Reports success/failure honestly and is re-runnable.
- **`scaffold.sh`** — the static-file half (idempotent, never clobbers): writes `.env`/`.mcp.json`/`.npmrc` and
  adds `.mcp.idx`, `.ai/`, `*.env` to `.gitignore`.
- **Submodules** — `.claude/` → `Sevelantis/.claude`, `devcontainers/` → `Sevelantis/devcontainers`; pinned by commit
  with `ignore = all`, so `git status` stays quiet even after you commit inside them.
- **Reopen in Container** runs `devcontainers/scripts/initializeCommand.sh` (host-side), which brings up this
  repo's per-project platform under your `COMPOSE_PROJECT_NAME`.

## Troubleshooting

- **Empty `.claude/` or `devcontainers/`** — the token lacks read on both `Sevelantis` repos, or wasn't entered.
  Fix `GH_TOKEN_RO` in `.env` and re-run `bash .devcontainer/setup.sh`.
- **Rebuild blocked / port clash** — `DEVCONTAINER_INGRESS_PORT` is still `CHANGE_ME` or collides with another
  running repo. Pick a unique number.
- **`git status` shows `.claude`/`devcontainers` "(new commits)"** — expected only when you commit _inside_ a
  submodule; `ignore = all` hides routine drift. Publish a new pin deliberately: `git add .claude devcontainers`.
- **Did it work?** — `bash .devcontainer/scaffold.sh --check` lists which config files are present/missing
  (optional; `setup.sh` already creates them).
- `.env` is gitignored (it holds your tokens) — never commit it.
