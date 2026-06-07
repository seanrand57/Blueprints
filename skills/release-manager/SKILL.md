---
name: release-manager
description: Prepare a repo or branch for release with changelog, versioning, release notes, verification, deployment checklist, and rollback plan.
---

# Release Manager

Use this skill when work is ready to ship.

## Workflow

1. Identify release scope:
   - commits since last tag
   - PR or branch
   - package/app version
2. Inspect:
   - changelog conventions
   - version files
   - CI status
   - tests run
   - migrations
   - feature flags
   - docs needing updates
3. Prepare release artifacts:
   - changelog entry
   - release notes
   - deployment checklist
   - rollback plan
4. Verify and report.

## Release Checklist

- Tests pass or gaps are explicit.
- Security-sensitive changes have review.
- User-facing changes are documented.
- Migrations have rollback or recovery notes.
- Version/tag plan is clear.
- Post-release smoke checks are defined.

## Output

```md
## Release Plan

Version/tag:
Summary:
Changes:
Verification:
Deployment:
Rollback:
Post-release checks:
Risks:
```
