---
name: blueprint
description: Compose reusable Blueprints guidance for agent coding, review, testing, project setup, and tool configuration.
---

# Blueprint Skill

Use this skill when a project needs shared guidance from the Blueprints repository.

## Workflow

1. Identify the task type:
   - implementation
   - review
   - testing
   - documentation
   - project setup
   - tool configuration
2. Load the smallest relevant set of files from this repo.
3. Combine shared Blueprints guidance with local project instructions.
4. Prefer local project rules when they conflict with shared defaults.
5. Report which blueprints were used.

## Recommended Files

- Implementation: `standards/engineering.md`, `prompts/agent-coding.md`
- Review: `playbooks/pr-review.md`, `prompts/reviewer.md`
- Testing: `playbooks/testing.md`
- Strategy: `docs/vision.md`

## Output

Keep the final guidance short and task-specific. Avoid dumping the entire repository into context.
