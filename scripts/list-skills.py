#!/usr/bin/env python3
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
registry = json.loads((root / "registry" / "skills.json").read_text())

for skill in registry["skills"]:
    tags = ", ".join(skill.get("tags", []))
    print(f"{skill['name']}\t{skill['category']}\t{skill['maturity']}\t{tags}")
