import os

with open("scripts/install", "r") as f:
    content = f.read()

# 1. Update the targets loop to clean old skills and install plugins
new_logic = """
for target in "${targets[@]}"; do
  base_dir="$(dirname "$target")"
  skills_target="$base_dir/skills"
  plugins_target="$base_dir/plugins"
  
  mkdir -p "$skills_target"
  mkdir -p "$plugins_target"

  # CLEANUP: Remove all old standalone skill symlinks from this repo to prevent double-loading
  while IFS= read -r existing_link; do
    linked_path="$(readlink "$existing_link")"
    if [[ "$linked_path" == "$repo_dir/skills/"* || "$linked_path" == "$repo_dir/plugins/"* ]]; then
      unlink "$existing_link"
      echo "PRUNE old standalone skill link: $existing_link"
    fi
  done < <(find "$skills_target" -mindepth 1 -maxdepth 1 -type l | sort)

  # INSTALL: Symlink the 3 Plugins
  for plugin in "$repo_dir/plugins/"*; do
    if [[ -d "$plugin" ]]; then
      plugin_name="$(basename "$plugin")"
      link="$plugins_target/$plugin_name"
      if [[ -L "$link" ]]; then
        ln -sfn "$plugin" "$link"
      elif [[ -e "$link" ]]; then
        echo "FAIL existing non-link blocks plugin: $link"
        exit 1
      else
        ln -s "$plugin" "$link"
      fi
    fi
  done

  # ALIASES: Aliases stay as standalone skills (they just point to the new locations)
  while IFS=$'\t' read -r alias_name category canonical_name; do
    [[ -n "$alias_name" && -n "$canonical_name" ]] || continue
    alias_dir="$repo_dir/aliases/$alias_name"
    if [[ ! -f "$alias_dir/SKILL.md" ]]; then
      echo "FAIL alias target missing: $alias_name -> $canonical_name"
      exit 1
    fi
    alias_link="$skills_target/$alias_name"
    if [[ -L "$alias_link" ]]; then
      ln -sfn "$alias_dir" "$alias_link"
    elif [[ -e "$alias_link" ]]; then
      echo "FAIL existing non-link blocks compatibility alias: $alias_link"
      exit 1
    else
      ln -s "$alias_dir" "$alias_link"
    fi
  done < <(python3 - "$repo_dir/catalog.json" <<'PY'
import json, sys
for item in json.load(open(sys.argv[1], encoding="utf-8"))["skills"]:
    if item["status"] == "promoted":
        for alias in item.get("aliases", []):
            print(f'{alias}\t{item["category"]}\t{item["name"]}')
PY
)
done

echo "Installed 3 plugins and aliases from $repo_dir"
"""

# Replace the old `for target in "${targets[@]}"; do ... done`
import re
content = re.sub(r'for target in "\$\{targets\[@\]\}"; do.*done\n\necho "Installed links from \$repo_dir"', new_logic.strip(), content, flags=re.DOTALL)

with open("scripts/install", "w") as f:
    f.write(content)
