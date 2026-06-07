# Security Review Playbook

Use this before publishing, releasing, or handling auth/data changes.

## Scan

- credentials and secret-looking values
- `.env` and generated config
- CI/CD config
- logs and telemetry
- screenshots and docs
- dependency manifests
- auth and authorization code paths

## Report

Lead with concrete findings. Include file and line references when possible.

Severity guide:

- `P0`: active secret or direct unauthorized access.
- `P1`: likely exploitable security flaw or sensitive public exposure.
- `P2`: meaningful risk with narrower trigger.
- `P3`: hardening or hygiene issue.

## Public Repo Rule

Anything committed to a public repo should be treated as public forever. If a real secret was committed, rotate it even if the commit is later rewritten.
