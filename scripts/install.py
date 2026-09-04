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

def create_symlink_or_junction(src, dst):
    if os.path.exists(dst) or os.path.islink(dst):
        try:
            if os.path.islink(dst) or os.path.isfile(dst):
                os.unlink(dst)
            else:
                shutil.rmtree(dst)
        except Exception as e:
            print_error(f"Could not remove existing target {dst}: {e}")
            return False
            
    try:
        if platform.system() == "Windows":
            # On Windows, try junction for directories to avoid needing Admin rights
            if os.path.isdir(src):
                import _winapi
                _winapi.CreateJunction(str(src), str(dst))
            else:
                os.symlink(src, dst)
        else:
            os.symlink(src, dst)
        return True
    except OSError as e:
        # Fallback to copy on Windows if symlink fails and it's not a directory
        if platform.system() == "Windows":
            print_step(f"Symlink failed, falling back to copy for {dst}")
            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
            return True
        print_error(f"Failed to link {src} -> {dst}: {e}")
        return False

def main():
    repo_dir = Path(__file__).parent.parent.absolute()
    home = Path.home()
    
    print_step("Validating repository...")
    if platform.system() != "Windows":
        os.system(f'"{repo_dir}/scripts/validate"')
        os.system(f'"{repo_dir}/scripts/install-hooks"')
    else:
        print_step("Skipping bash validation on Windows.")

    targets = [
        home / ".agents" / "skills",
        home / ".codex" / "skills",
        home / ".claude" / "skills"
    ]
    
    if (home / ".gemini" / "config").is_dir():
        targets.append(home / ".gemini" / "config" / "skills")
    if (home / ".gemini" / "antigravity" / "custom").is_dir():
        targets.append(home / ".gemini" / "antigravity" / "custom" / "skills")
        
    catalog_path = repo_dir / "catalog.json"
    if not catalog_path.exists():
        print_error("catalog.json not found!")
        sys.exit(1)
        
    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog = json.load(f)
        
    promoted_skills = [s for s in catalog.get("skills", []) if s.get("status") == "promoted"]

    for target in targets:
        base_dir = target.parent
        skills_target = base_dir / "skills"
        plugins_target = base_dir / "plugins"
        
        skills_target.mkdir(parents=True, exist_ok=True)

        if ".gemini" in str(base_dir):
            plugins_target.mkdir(parents=True, exist_ok=True)
            
            # Cleanup old skills
            if skills_target.exists():
                for item in skills_target.iterdir():
                    if item.is_symlink() or item.is_junction():
                        try:
                            # basic check if it belongs to this repo
                            target_path = str(item.resolve())
                            if str(repo_dir) in target_path:
                                item.unlink()
                        except Exception:
                            pass
            
            # Symlink plugins
            for plugin in (repo_dir / "plugins").iterdir():
                if plugin.is_dir():
                    create_symlink_or_junction(plugin, plugins_target / plugin.name)
        else:
            # Legacy Claude/Cursor support
            for plugin in (repo_dir / "plugins").iterdir():
                plugin_skills = plugin / "skills"
                if plugin_skills.is_dir():
                    for skill in plugin_skills.iterdir():
                        if skill.is_dir():
                            create_symlink_or_junction(skill, skills_target / skill.name)

        # Aliases
        for item in promoted_skills:
            for alias in item.get("aliases", []):
                alias_dir = repo_dir / "aliases" / alias
                if (alias_dir / "SKILL.md").exists():
                    create_symlink_or_junction(alias_dir, skills_target / alias)
                    
    print_success(f"Installed successfully to all platforms from {repo_dir}")

if __name__ == "__main__":
    main()
