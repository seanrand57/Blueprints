# Vision

Blueprints is meant to become a reusable operating system for autonomous and semi-autonomous software teams.

It should help with:

- agent coding workflows
- pull request creation and review
- testing strategy
- project setup
- documentation
- security review
- release readiness
- tool and MCP configuration
- cross-agent collaboration

## Design Goals

- Tool-neutral: useful in Codex, Cursor, Claude Code, cloud agents, and CI.
- Composable: small files can be mixed into project-specific instructions.
- Auditable: guidance is versioned and easy to review.
- Practical: every blueprint should map to real work.
- Extensible: new agent roles and workflows should be easy to add.

## First-Class Agent Roles

- Builder: implements scoped changes.
- Reviewer: finds bugs, regressions, risks, and missing tests.
- Tester: designs and runs verification.
- Maintainer: updates standards, dependencies, docs, and release notes.
- Coordinator: breaks broad goals into sequenced work.
- Researcher: gathers current docs, APIs, and constraints.

## Near-Term Milestones

1. Define the repo taxonomy.
2. Add baseline engineering standards.
3. Add review and testing playbooks.
4. Add a portable `blueprint` skill.
5. Add install or sync scripts for downstream projects.
