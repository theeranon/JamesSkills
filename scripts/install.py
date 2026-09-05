#!/usr/bin/env python3
import os
import sys
import json
import shutil
import platform
from pathlib import Path

def print_step(msg):
    print(f"[*] {msg}")

def print_success(msg):
    print(f"[SUCCESS] {msg}")

def print_error(msg):
    print(f"[ERROR] {msg}")

def safe_remove(dst):
    if os.path.exists(dst) or os.path.islink(dst):
        try:
            if os.path.islink(dst) or os.path.isfile(dst):
                os.unlink(dst)
            else:
                shutil.rmtree(dst)
        except Exception as e:
            print_error(f"Could not remove existing target {dst}: {e}")
            return False
    return True

def install_plugin(src, dst):
    safe_remove(dst)
    try:
        if platform.system() == "Windows":
            import _winapi
            _winapi.CreateJunction(str(src), str(dst))
        else:
            # For Mac/Linux, we create a symlink. 
            # Note: For Go-based agents that don't follow symlinks in plugins/ 
            # we also explicitly register them via plugins.json below.
            os.symlink(src, dst)
        return True
    except OSError:
        print_step(f"Symlink/Junction failed, falling back to copy for {dst}")
        shutil.copytree(src, dst)
        return True

def install_alias(src, dst):
    safe_remove(dst)
    try:
        if platform.system() == "Windows":
            import _winapi
            _winapi.CreateJunction(str(src), str(dst))
        else:
            os.symlink(src, dst)
        return True
    except OSError:
        shutil.copytree(src, dst)
        return True

def main():
    repo_dir = Path(__file__).parent.parent.absolute()
    home = Path.home()
    
    print_step("Validating repository...")
    if platform.system() != "Windows":
        os.system(f'"{repo_dir}/scripts/validate"')
        os.system(f'"{repo_dir}/scripts/install-hooks"')

    targets = [
        home / ".agents",
        home / ".codex",
        home / ".claude"
    ]
    
    if (home / ".gemini" / "config").is_dir():
        targets.append(home / ".gemini" / "config")
    if (home / ".gemini" / "antigravity" / "custom").is_dir():
        targets.append(home / ".gemini" / "antigravity" / "custom")
        
    catalog_path = repo_dir / "catalog.json"
    if not catalog_path.exists():
        print_error("catalog.json not found!")
        sys.exit(1)
        
    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)
        
    promoted_skills = [s for s in catalog.get("skills", []) if s.get("status") == "promoted"]

    for base_dir in targets:
        skills_target = base_dir / "skills"
        plugins_target = base_dir / "plugins"
        
        skills_target.mkdir(parents=True, exist_ok=True)
        plugins_target.mkdir(parents=True, exist_ok=True)

        print_step(f"Installing to {base_dir}...")
        
        # Cleanup legacy standalone skills to prevent double-loading
        if skills_target.exists():
            for item in skills_target.iterdir():
                if item.is_symlink():
                    try:
                        target_path = str(item.resolve())
                        if str(repo_dir) in target_path:
                            item.unlink()
                    except Exception:
                        pass
        
        # Install as Plugins for ALL platforms
        for plugin in (repo_dir / "plugins").iterdir():
            if plugin.is_dir() and (plugin / "plugin.json").exists():
                install_plugin(plugin, plugins_target / plugin.name)

        # Write plugins.json to explicitly tell the agent to load them 
        # (Fixes the issue where Go skips Unix symlinks)
        plugins_json_path = base_dir / "plugins.json"
        plugins_config = {"entries": []}
        if plugins_json_path.exists():
            try:
                with open(plugins_json_path, "r") as f:
                    plugins_config = json.load(f)
            except Exception:
                pass
                
        # Ensure our repo plugins path is explicitly registered
        repo_plugins_path = str(repo_dir / "plugins")
        has_entry = any(entry.get("path") == repo_plugins_path for entry in plugins_config.get("entries", []))
        if not has_entry:
            if "entries" not in plugins_config:
                plugins_config["entries"] = []
            plugins_config["entries"].append({"path": repo_plugins_path})
            with open(plugins_json_path, "w") as f:
                json.dump(plugins_config, f, indent=2)

        # ALIASES: Aliases go to the skills/ folder for everyone
        for item in promoted_skills:
            for alias in item.get("aliases", []):
                alias_dir = repo_dir / "aliases" / alias
                if (alias_dir / "SKILL.md").exists():
                    install_alias(alias_dir, skills_target / alias)
                    
    print_success(f"Installed successfully as Plugins to all platforms from {repo_dir}")

if __name__ == "__main__":
    main()
