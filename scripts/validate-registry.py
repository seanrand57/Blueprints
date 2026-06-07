#!/usr/bin/env python3
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
registry_path = root / "registry" / "skills.json"

try:
    registry = json.loads(registry_path.read_text())
except json.JSONDecodeError as error:
    print(f"Invalid JSON: {error}", file=sys.stderr)
    sys.exit(1)

required = {"name", "path", "category", "maturity", "tags", "triggers", "depends_on"}
skills = registry.get("skills", [])
names = set()
errors = []

for index, skill in enumerate(skills):
    missing = required - set(skill)
    if missing:
        errors.append(f"skill[{index}] missing fields: {', '.join(sorted(missing))}")
        continue

    name = skill["name"]
    if name in names:
        errors.append(f"duplicate skill name: {name}")
    names.add(name)

    path = root / skill["path"]
    if not path.exists():
        errors.append(f"{name}: missing path {skill['path']}")
    elif path.name == "SKILL.md":
        text = path.read_text(errors="replace")
        if f"name: {name}" not in text and f'name: "{name}"' not in text:
            errors.append(f"{name}: SKILL.md frontmatter name does not match registry")

    for field in ("tags", "triggers", "depends_on"):
        if not isinstance(skill[field], list):
            errors.append(f"{name}: {field} must be a list")

for skill in skills:
    for dependency in skill.get("depends_on", []):
        if dependency not in names:
            errors.append(f"{skill['name']}: unknown dependency {dependency}")

if errors:
    print("Registry validation failed:", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    sys.exit(1)

print(f"Registry OK: {len(skills)} skills")
