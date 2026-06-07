#!/usr/bin/env bash
set -euo pipefail

target_dir="${1:-.}"
mode="${2:-reference}"
source_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

mkdir -p "$target_dir/.blueprints"

if [[ "$mode" == "copy" || "$mode" == "hybrid" ]]; then
  cp -R "$source_dir"/skills "$target_dir/.blueprints/"
  cp -R "$source_dir"/tools "$target_dir/.blueprints/"
  cp -R "$source_dir"/prompts "$target_dir/.blueprints/"
  cp -R "$source_dir"/standards "$target_dir/.blueprints/"
  cp -R "$source_dir"/playbooks "$target_dir/.blueprints/"
  cp -R "$source_dir"/templates "$target_dir/.blueprints/"
  cp -R "$source_dir"/docs "$target_dir/.blueprints/"
  cp -R "$source_dir"/registry "$target_dir/.blueprints/"
else
  cp "$source_dir/templates/blueprints/README.md" "$target_dir/.blueprints/README.md"
fi

if [[ ! -f "$target_dir/AGENTS.md" ]]; then
  cp "$source_dir/templates/AGENTS.blueprint.md" "$target_dir/AGENTS.md"
fi

echo "Installed Blueprints ($mode) into $target_dir"
