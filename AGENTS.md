# Agent Instructions

This repository is the Blueprints operating system for reusable agent skills, prompts, standards, playbooks, templates, and tool guidance.

## Priority

1. Preserve public-repo safety.
2. Keep Blueprints reusable across projects and tools.
3. Prefer small, composable guidance over giant monolithic prompts.
4. Update the registry when adding, renaming, or retiring skills.
5. Verify scripts and examples before committing.

## Core Files

- `registry/skills.json` is the dispatch map.
- `skills/blueprint/SKILL.md` is the front door.
- `skills/blueprint-orchestrator/SKILL.md` is the command center.
- `skills/blueprint-audit/SKILL.md` is for repo onboarding.
- `skills/blueprint-install/SKILL.md` is for installing guidance into projects.

## Safety

Never commit real credentials, tokens, private infrastructure details, generated local state, or machine-specific secrets. If a real secret is ever committed to this public repo, rotate it even if history is rewritten.

## Verification

Before committing changes to registry or scripts, run:

```bash
scripts/validate-registry.py
scripts/list-skills.py
scripts/audit-blueprints.py .
```
