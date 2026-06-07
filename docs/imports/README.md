# Imports

This directory documents material imported into Blueprints from local Codex, agent, Cursor, and project workspaces.

## Imported Skill Packs

| Destination | Source | Notes |
| --- | --- | --- |
| `skills/imported/blueprint-agents/` | Blueprints agent skill collection | Engineering, writing, design, review, testing, and workflow skills maintained as native Blueprints material. |
| `skills/imported/codex-local/nemoclaw-user-get-started/` | `/Users/seanrand/.codex/skills/nemoclaw-user-get-started/` | Local Codex skill for NemoClaw onboarding. |
| `skills/imported/agents-local/microsoft-foundry/` | `/Users/seanrand/.agents/skills/microsoft-foundry/` | Microsoft Foundry agent, model deployment, quota, RBAC, and fine-tuning workflows. |

## Imported Tool And Template Files

| Destination | Source | Notes |
| --- | --- | --- |
| `tools/cursor/mcp.example.json` | `/Users/seanrand/Documents/Cursor/.cursor/mcp.json` | Cursor MCP config with placeholder credentials. |
| `templates/codex/environments/world-cup-predictor.environment.toml` | `/Users/seanrand/Documents/World Cup Predictor/.codex/environments/environment.toml` | Codex environment setup template. |
| `templates/codex/environments/world-cup-predictor.environment-2.toml` | `/Users/seanrand/Documents/World Cup Predictor/.codex/environments/environment-2.toml` | Minimal Codex environment template. |

## Public Repo Safety

Before committing these imports, Blueprints was scanned for high-confidence secret patterns such as GitHub PATs, OpenAI-style keys, Slack tokens, AWS access keys, and private key blocks.

The Cursor MCP file uses `YOUR_GITHUB_PAT` as a placeholder. Do not replace placeholders with real credentials in this public repo.
