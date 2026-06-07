# Engineering Standards

Use these defaults unless a project has stricter local rules.

## Code Changes

- Read the surrounding code before editing.
- Keep changes scoped to the requested behavior.
- Prefer existing project patterns over new abstractions.
- Avoid unrelated refactors.
- Add comments only when they explain non-obvious intent.
- Preserve user changes and dirty worktrees.

## Tests

- Match test depth to risk and blast radius.
- Add focused tests for bug fixes and shared behavior changes.
- Run the narrowest meaningful verification first.
- Broaden verification when touching shared contracts, build systems, or user-facing flows.

## Dependencies

- Prefer standard library and existing dependencies.
- Add new dependencies only when they remove meaningful complexity.
- Document why a new dependency is worth carrying.

## Pull Requests

- Explain the user-visible change.
- Call out tests run and tests not run.
- Note risks, migrations, and follow-up work.
- Keep PRs reviewable; split broad work when needed.
