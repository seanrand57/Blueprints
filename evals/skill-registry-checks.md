# Skill Registry Checks

Use these checks when changing `registry/skills.json` or adding skills.

## Required Checks

- Registry JSON parses.
- Every registered skill path exists.
- Every registered skill has `name`, `path`, `category`, `maturity`, `tags`, `triggers`, and `depends_on`.
- Every dependency points to another registered skill.
- Every registered `SKILL.md` contains matching `name` frontmatter.

## Quality Checks

- Trigger phrases match how users ask for work.
- Categories are useful for routing.
- Maturity is honest.
- Dependencies are minimal.
- Public-repo safety is considered for skills that copy, publish, install, or deploy.

## Example Prompt

```md
Use `blueprint-orchestrator` to choose the right skills for fixing a failing test in a TypeScript app, then report the execution recipe and verification plan.
```
