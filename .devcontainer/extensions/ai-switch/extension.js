// AI Switch — thin GUI wrapper around .devcontainer/scripts/ai-switch.py.
//
// Each command runs the python script (single source of truth for writing
// .vscode/settings.json), awaits its completion, then reloads the window so the
// Claude Code extension re-reads ANTHROPIC_BASE_URL. Awaiting the child process
// before reloading makes the apply→reload sequence deterministic (no race).

const vscode = require("vscode");
const cp = require("child_process");
const path = require("path");
const util = require("util");

const execFile = util.promisify(cp.execFile);

const PROVIDERS = [
  { label: "$(home) Local", detail: "Self-hosted LLM — LOCAL_BASE_URL", value: "local" },
  { label: "$(sparkle) Gemini", detail: "GEMINI_BASE_URL", value: "gemini" },
  { label: "$(cloud) Anthropic", detail: "Claude Code Pro — no override", value: "anthropic" },
];

function scriptPath() {
  const root = vscode.workspace.workspaceFolders?.[0]?.uri.fsPath || "/workspaces/mag-bridge";
  return path.join(root, ".devcontainer", "scripts", "ai-switch.py");
}

async function applyAndReload(provider) {
  try {
    await execFile("python3", [scriptPath(), provider]);
  } catch (err) {
    vscode.window.showErrorMessage(`AI Switch (${provider}) failed: ${err.message}`);
    return;
  }
  await vscode.commands.executeCommand("workbench.action.reloadWindow");
}

function activate(context) {
  const reg = (id, fn) =>
    context.subscriptions.push(vscode.commands.registerCommand(id, fn));

  reg("ai-switch.select", async () => {
    const pick = await vscode.window.showQuickPick(PROVIDERS, {
      placeHolder: "Switch AI provider (reloads the window to apply)",
    });
    if (pick) await applyAndReload(pick.value);
  });
  reg("ai-switch.local", () => applyAndReload("local"));
  reg("ai-switch.gemini", () => applyAndReload("gemini"));
  reg("ai-switch.anthropic", () => applyAndReload("anthropic"));
}

function deactivate() {}

module.exports = { activate, deactivate };
