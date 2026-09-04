import re

with open("scripts/install", "r") as f:
    content = f.read()

new_logic = """
for target in "${targets[@]}"; do
  base_dir="$(dirname "$target")"
  skills_target="$base_dir/skills"
  plugins_target="$base_dir/plugins"
  
  mkdir -p "$skills_target"

  # If this is an Antigravity target, we use the Plugin Architecture
  if [[ "$base_dir" == *".gemini"* ]]; then
    mkdir -p "$plugins_target"
    
    # 1. Clean up legacy standalone skills to prevent double-loading in Antigravity
    while IFS= read -r existing_link; do
      linked_path="$(readlink "$existing_link")"
      if [[ "$linked_path" == "$repo_dir/skills/"* || "$linked_path" == "$repo_dir/plugins/"* ]]; then
        unlink "$existing_link"
      fi
    done < <(find "$skills_target" -mindepth 1 -maxdepth 1 -type l | sort)

    # 2. Symlink the 3 Plugins
    for plugin in "$repo_dir/plugins/"*; do
      if [[ -d "$plugin" ]]; then
        plugin_name="$(basename "$plugin")"
        link="$plugins_target/$plugin_name"
        ln -sfn "$plugin" "$link"
      fi
    done
  else
    # If this is Claude, Cursor, or Codex, they DON'T support plugins.
    # We MUST symlink every individual skill directly into their skills/ folder!
    for plugin in "$repo_dir/plugins/"*; do
      if [[ -d "$plugin/skills" ]]; then
        for skill in "$plugin/skills/"*; do
          if [[ -d "$skill" ]]; then
            skill_name="$(basename "$skill")"
            link="$skills_target/$skill_name"
            ln -sfn "$skill" "$link"
          fi
        done
      fi
    done
  fi

  # ALIASES: Aliases always go to the skills/ folder for everyone
  while IFS=$'\t' read -r alias_name category canonical_name; do
    [[ -n "$alias_name" && -n "$canonical_name" ]] || continue
    alias_dir="$repo_dir/aliases/$alias_name"
    if [[ ! -f "$alias_dir/SKILL.md" ]]; then
      echo "FAIL alias target missing: $alias_name -> $canonical_name"
      exit 1
    fi
    alias_link="$skills_target/$alias_name"
    ln -sfn "$alias_dir" "$alias_link"
  done < <(python3 - "$repo_dir/catalog.json" <<'PY'
import json, sys
for item in json.load(open(sys.argv[1], encoding="utf-8"))["skills"]:
    if item["status"] == "promoted":
        for alias in item.get("aliases", []):
            print(f'{alias}\t{item["category"]}\t{item["name"]}')
PY
)
done

echo "Installed successfully to all platforms (Antigravity Plugins + Legacy Skills) from $repo_dir"
"""

# Replace the old loop
content = re.sub(r'for target in "\$\{targets\[@\]\}"; do.*done\n\necho "Installed 3 plugins and aliases from \$repo_dir"', new_logic.strip(), content, flags=re.DOTALL)

with open("scripts/install", "w") as f:
    f.write(content)
