# Pull Request Review Playbook

Use this stance when reviewing code.

## Priority Order

1. Correctness bugs and regressions.
2. Security, privacy, and data integrity risks.
3. Missing or weak tests for changed behavior.
4. Performance issues with real user impact.
5. Maintainability concerns that create near-term risk.

## Review Method

- Start with the diff.
- Trace affected call paths.
- Check tests against behavior, not just coverage.
- Verify edge cases and failure modes.
- Prefer concrete findings with file and line references.

## Output Shape

- Lead with findings, ordered by severity.
- Include open questions or assumptions.
- Keep summaries brief and secondary.
- Say clearly when no issues are found.

## Finding Template

```md
[P1] Short title

Explain the bug or risk, why it matters, and the condition that triggers it. Include a specific file and line reference.
```
