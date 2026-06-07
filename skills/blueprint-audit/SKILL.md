---
name: blueprint-audit
description: Audit a repository and recommend which Blueprints skills, standards, templates, and guardrails should be installed or used. Use when onboarding a repo, asking what superpowers apply, or checking gaps in agent readiness.
---

# Blueprint Audit

Use this skill to inspect a target repository and produce a practical Blueprints adoption plan.

## Workflow

1. Identify the target repo root.
2. Inspect without changing files:
   - `git remote -v`
   - `git status --short --branch`
   - root guidance files: `AGENTS.md`, `CLAUDE.md`, `README.md`, `CONTRIBUTING.md`
   - Codex/Cursor/Claude config: `.codex/`, `.cursor/`, `.claude/`, `.cursorrules`
   - package and build files
   - test, lint, typecheck, CI, and deploy config
   - issue tracker clues
   - docs: `docs/`, ADRs, PRDs, context docs
3. Map findings to `registry/skills.json`.
4. Produce an adoption report.

## Report Format

```md
## Blueprint Audit

### Repo Snapshot
- Stack:
- Package/build tools:
- Test surface:
- Agent guidance:
- Issue tracker:
- CI/deploy:

### Recommended Skills
- skill: why it applies

### Missing Superpowers
- gap: suggested blueprint or template

### Install Plan
1. Smallest safe first step.
2. Next useful addition.
3. Larger optional upgrade.

### Risks
- public repo or secret risk
- missing tests
- unclear ownership
```

## Rules

- Do not modify files unless the user explicitly asks to install or sync.
- Prefer concrete evidence from files over guesses.
- If a repo is private or sensitive, call out public-repo risk before recommending copying material into a public place.
