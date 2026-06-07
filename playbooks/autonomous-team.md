# Autonomous Team Playbook

Use this playbook when a goal needs multiple agent roles.

## Roles

- Coordinator: clarifies scope, chooses skills, sequences work.
- Builder: implements the smallest useful change.
- Tester: designs and runs verification.
- Reviewer: checks correctness, safety, and maintainability.
- Documenter: updates docs, PR notes, release notes, or handoff.

## Default Loop

1. Audit the repo if context is missing.
2. Convert the goal into an execution recipe.
3. Build in small slices.
4. Verify each slice.
5. Review against spec and standards.
6. Record what changed and what remains.

## Handoff Artifact

```md
## Handoff

Goal:
Current state:
Decisions:
Files changed:
Verification:
Open risks:
Next action:
```
