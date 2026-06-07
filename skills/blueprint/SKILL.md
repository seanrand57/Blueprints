---
name: blueprint
description: Compose reusable Blueprints guidance for agent coding, review, testing, project setup, and tool configuration.
---

# Blueprint Skill

Use this skill when a project needs shared guidance from the Blueprints repository. This is the front door. For broad or ambiguous work, route through `blueprint-orchestrator`.

## Workflow

1. Identify the task type:
   - implementation
   - review
   - testing
   - documentation
   - project setup
   - tool configuration
   - security
   - release
   - product/spec
   - design/prototype
2. Load the smallest relevant set of files from this repo.
3. Check `registry/skills.json` for matching skills.
4. Combine shared Blueprints guidance with local project instructions.
5. Prefer local project rules when they conflict with shared defaults.
6. Report which blueprints were used.

## Recommended Files

- Implementation: `standards/engineering.md`, `prompts/agent-coding.md`
- Review: `playbooks/pr-review.md`, `prompts/reviewer.md`
- Testing: `playbooks/testing.md`
- Strategy: `docs/vision.md`
- Orchestration: `skills/blueprint-orchestrator/SKILL.md`, `playbooks/autonomous-team.md`
- Repo onboarding: `skills/blueprint-audit/SKILL.md`, `skills/blueprint-install/SKILL.md`, `playbooks/repo-onboarding.md`
- Security: `skills/security-review/SKILL.md`, `playbooks/security-review.md`
- Release: `skills/release-manager/SKILL.md`

## Imported Skill Packs

When the task needs a more specialized workflow, inspect these imported packs:

- `skills/imported/blueprint-agents/` for engineering, review, TDD, QA, product shaping, writing, and interface-design workflows.
- `skills/imported/codex-local/` for local Codex skills.
- `skills/imported/agents-local/` for broader agent platform skills such as Microsoft Foundry.

Use `docs/imports/imported-skills.md` as the quick index before reading a full skill. Use `docs/imports/external-skill-catalog.md` to identify upstream curated skills that are available locally but intentionally not vendored here.

## Output

Keep the final guidance short and task-specific. Avoid dumping the entire repository into context.
