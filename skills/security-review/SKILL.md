---
name: security-review
description: Review a repository, branch, or change for secrets, authentication flaws, authorization gaps, dependency risk, public-repo exposure, and data handling issues.
---

# Security Review

Use this skill when security, public repo safety, credentials, auth, or data exposure matter.

## Workflow

1. Identify scope:
   - current working tree
   - branch diff
   - whole repo
   - public release
2. Inspect:
   - secrets and token-looking strings
   - `.env`, config, examples, CI variables
   - auth and authorization code paths
   - API routes and server actions
   - persistence, logs, telemetry, and exports
   - dependency and supply-chain files
   - public repo metadata
3. Report findings first, ordered by severity.
4. Recommend fixes and verification.

## Checks

- No real credentials in source, examples, docs, screenshots, or history.
- Placeholders are clearly fake.
- Sensitive files are ignored.
- Auth checks happen server-side.
- User-controlled input is validated before privileged operations.
- Logs avoid secrets and PII.
- Dependencies are necessary and maintained.
- Public docs do not reveal private infrastructure details.

## Output

Use code-review style:

- findings first
- file and line references
- exploit or exposure condition
- fix recommendation
- residual risk
