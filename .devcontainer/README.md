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
