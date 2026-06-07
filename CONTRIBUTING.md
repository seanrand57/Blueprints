# Contributing

Blueprints should stay easy for both humans and agents to navigate.

## Adding A Skill

1. Create `skills/<name>/SKILL.md` or add to an appropriate imported pack.
2. Give the skill clear frontmatter:
   - `name`
   - `description`
3. Add the skill to `registry/skills.json` if it should be routable.
4. Add supporting playbooks, templates, scripts, or prompts only when they are directly useful.
5. Run `scripts/validate-registry.py`.

## Style

- Keep instructions portable across Codex, Cursor, Claude Code, cloud agents, and CI.
- Prefer concrete workflows over philosophy.
- Keep examples free of secrets and private project details.
- Use placeholders like `YOUR_TOKEN` for credentials.

## Public Repo Safety

Assume everything in this repo is public forever. Do not commit:

- real API keys or tokens
- private URLs that reveal sensitive infrastructure
- customer data
- personal data
- generated local caches
- binary artifacts unless they are intentionally part of a template
