---
name: blueprint-install
description: Install or sync selected Blueprints guidance into a target repository. Use when the user asks to add Blueprints, create agent instructions, install shared skills, or sync templates into a project.
---

# Blueprint Install

Use this skill to install selected Blueprints material into another repo.

## Workflow

1. Confirm the target repo root.
2. Run a quick audit first:
   - current guidance files
   - dirty worktree
   - existing `.blueprints/`
   - tool-specific config
3. Choose install mode:
   - `reference`: add lightweight instructions that point to the central Blueprints repo.
   - `copy`: copy selected templates into `.blueprints/`.
   - `hybrid`: add instructions plus copy a small curated subset.
4. Install using `scripts/install-blueprints.sh` or by copying templates.
5. Report changed files and next steps.

## Default Install

Prefer `reference` mode unless the user asks for offline/local copies.

Default files:

- `AGENTS.md`
- `.blueprints/README.md`
- optional `.cursor/mcp.example.json`
- optional `.codex/environments/`

## Safety

- Never overwrite existing guidance without reading it first.
- Preserve local project rules as higher priority than shared Blueprints.
- Do not install secrets or machine-local tokens.
- Keep generated install changes reviewable.
