# Testing Playbook

Use this to choose verification for implementation work.

## Fast Pass

- Run relevant unit tests.
- Run typecheck or lint when available.
- Exercise the changed path manually when it is user-facing.

## Broader Pass

Use broader verification when changes affect:

- shared utilities
- authentication or permissions
- persistence or migrations
- payment, billing, or financial flows
- build and deployment configuration
- public APIs
- critical user journeys

## Reporting

Always report:

- what was run
- whether it passed
- what was not run
- any residual risk
