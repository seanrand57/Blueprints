# Registry

The registry is the machine-readable map that turns Blueprints from a folder of useful material into a dispatchable operating system.

## Files

- `skills.json` lists high-signal skills with paths, categories, triggers, tags, maturity, and dependencies.

## Maturity

- `core`: native Blueprints skill intended as part of the default operating system.
- `ready`: imported or bundled skill that is ready to route to.
- `experimental`: useful but should be validated before broad reuse.

## Maintenance

Update `registry/skills.json` when adding, renaming, or retiring skills. Keep triggers short and practical: they should match how a user asks for work, not how the skill is internally organized.
