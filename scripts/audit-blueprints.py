#!/usr/bin/env python3
import json
import os
import sys
from pathlib import Path

root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
blueprints_root = Path(__file__).resolve().parents[1]
registry = json.loads((blueprints_root / "registry" / "skills.json").read_text())

def exists_any(names):
    return [name for name in names if (root / name).exists()]

files = {
    "agent_guidance": exists_any(["AGENTS.md", "CLAUDE.md", ".cursorrules"]),
    "codex": exists_any([".codex"]),
    "cursor": exists_any([".cursor"]),
    "node": exists_any(["package.json", "pnpm-lock.yaml", "package-lock.json", "yarn.lock"]),
    "python": exists_any(["pyproject.toml", "requirements.txt", "setup.py"]),
    "ci": exists_any([".github/workflows", ".gitlab-ci.yml"]),
    "docs": exists_any(["docs", "README.md", "CONTRIBUTING.md"]),
    "tests": exists_any(["tests", "test", "__tests__", "spec"]),
}

recommended = ["blueprint", "blueprint-orchestrator", "blueprint-audit"]
if not files["agent_guidance"]:
    recommended.append("blueprint-install")
if files["node"] or files["python"]:
    recommended.extend(["tdd", "review", "diagnose"])
if files["ci"]:
    recommended.append("release-manager")
if files["docs"]:
    recommended.extend(["to-prd", "to-issues"])

seen = []
for item in recommended:
    if item not in seen:
        seen.append(item)

skill_map = {skill["name"]: skill for skill in registry["skills"]}

print("# Blueprint Audit")
print()
print(f"Target: `{root}`")
print()
print("## Detected")
for key, value in files.items():
    rendered = ", ".join(value) if value else "missing"
    print(f"- {key}: {rendered}")
print()
print("## Recommended Skills")
for name in seen:
    skill = skill_map.get(name)
    if skill:
        print(f"- `{name}`: {skill['path']}")
print()
print("## Suggested Next Step")
if not files["agent_guidance"]:
    print("Run `blueprint-install` or `scripts/install-blueprints.sh <repo>` to add project guidance.")
else:
    print("Use `blueprint-orchestrator` to choose the right workflow for the next task.")
