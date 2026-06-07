#!/usr/bin/env bash
set -euo pipefail

target_dir="${1:-.}"

mkdir -p "$target_dir/.blueprints"
cp -R skills tools prompts standards playbooks templates docs "$target_dir/.blueprints/"

echo "Installed Blueprints into $target_dir/.blueprints"
