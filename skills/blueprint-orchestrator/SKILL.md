---
name: blueprint-orchestrator
description: Select and sequence the right Blueprints skills for a task, producing an execution recipe for an autonomous agent team. Use for broad goals, multi-step work, cross-functional tasks, or when the user wants the repo to act like a superpower command center.
---

# Blueprint Orchestrator

Use this skill when one skill is not enough.

## Workflow

1. Classify the request:
   - build
   - debug
   - review
   - test
   - product/spec
   - design/prototype
   - release
   - security
   - repo setup
   - platform/Foundry
2. Check `registry/skills.json` for matching skills.
3. Build a short execution recipe:
   - primary skill
   - supporting skills
   - required standards/playbooks
   - verification steps
   - handoff artifacts
4. Execute directly when the user asked for action and the target is clear.
5. Report which skills were used.

## Team Modes

### Builder Loop

- `blueprint-audit` when repo context is unknown
- `tdd` or `diagnose`
- `review`
- `qa`

### Product Loop

- `grill-me` or `grill-with-docs`
- `to-prd`
- `to-issues`
- `triage`

### Frontend Loop

- `prototype`
- `frontend-design`
- `make-interfaces-feel-better`
- `qa`

### Release Loop

- `review`
- `security-review`
- `release-manager`

## Output

```md
## Blueprint Recipe

Primary skill:
Supporting skills:
Context to load:
Steps:
Verification:
Artifacts:
```

Keep recipes compact. The point is to start useful work, not write a ceremony document.
