# AI Switch

Switches the Claude Code VS Code extension between AI providers, then reloads the
window so the change takes effect.

## Commands (Ctrl+Shift+P)

Look for the **AI Switch** category — it offers a provider picker plus direct
per-provider entries. The provider list is driven by the script and may change.

## How it works

Each command runs `.devcontainer/scripts/ai-switch.py <provider>`, which rewrites
`.vscode/settings.json` → `claudeCode.environmentVariables`, then triggers
`workbench.action.reloadWindow`. Provider endpoints come from `.env`.

A terminal equivalent (`ai-switch`) is also available via shell alias.
