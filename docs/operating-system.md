# Blueprints Operating System

Blueprints is organized as an agent operating system.

## Layers

1. Registry: machine-readable dispatch metadata.
2. Router: the `blueprint` skill.
3. Command center: the `blueprint-orchestrator` skill.
4. Capabilities: implementation, review, QA, product, design, security, release, and platform skills.
5. Standards: stable expectations for engineering, testing, review, and security.
6. Templates: installable guidance for downstream projects.
7. Scripts: small utilities that make the repo inspectable and portable.

## Default Flow

```text
User goal
  -> blueprint
  -> blueprint-orchestrator
  -> selected skills + standards + playbooks
  -> implementation or report
  -> verification
  -> handoff
```

## Default Team

- Coordinator: `blueprint-orchestrator`
- Repo Scout: `blueprint-audit`
- Builder: `tdd`, `diagnose`, or relevant implementation skill
- Reviewer: `review`, `security-review`
- Tester: `qa`, `playbooks/testing.md`
- Shipper: `release-manager`

## What Makes A Good Blueprint

- It has a clear trigger.
- It tells the agent what to inspect before acting.
- It names outputs.
- It protects local project rules.
- It avoids copying unnecessary context.
- It can be reused in more than one repo.
