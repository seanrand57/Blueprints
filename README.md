# Blueprints

Blueprints is a shared home for reusable agent operating material: skills, tools, prompts, coding standards, review playbooks, and project bootstrap templates.

The goal is simple: keep the best working patterns in one public repo, then let Codex, Cursor, Claude Code, cloud agents, CI bots, and project teams pull from the same source of truth instead of copying guidance from project to project.

## What Belongs Here

- `skills/` reusable agent skills and workflows
- `tools/` tool manifests, MCP notes, CLI wrappers, and integration recipes
- `prompts/` reusable prompt blocks and role instructions
- `standards/` engineering, testing, security, PR, and review expectations
- `playbooks/` step-by-step operating procedures for common tasks
- `templates/` starter files for new projects and agent workspaces
- `docs/` strategy, architecture, and maintenance notes
- `scripts/` helper scripts for syncing or installing blueprints

## Core Idea

Each project should be able to reference this repo as its central agent blueprint library. Local project guidance can stay lightweight and project-specific, while this repo carries the common operating system.

Possible usage patterns:

- Add this repo as a Git submodule in project repos.
- Clone it into a standard local path and reference files from project instructions.
- Use scripts to copy selected templates into a new project.
- Let an agent skill fetch and compose the right blueprints for a task.

## Starting Map

```text
Blueprints/
  skills/
  tools/
  prompts/
  standards/
  playbooks/
  templates/
  docs/
  scripts/
```

## Operating Principles

1. Keep guidance portable across tools.
2. Prefer small reusable modules over giant all-purpose prompts.
3. Make every blueprint easy for agents and humans to inspect.
4. Version changes through pull requests when the impact is broad.
5. Capture what works in real projects, then refine it here.

## Status

This repo is intentionally starting small. The next milestone is a `blueprint` skill that can select and assemble the right standards, prompts, and playbooks for a given project or task.
