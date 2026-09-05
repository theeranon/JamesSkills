#!/usr/bin/env python3
import os
import sys
import json
import shutil
import platform
import subprocess
from pathlib import Path

def print_step(msg):
    print(f"[*] {msg}")

def print_success(msg):
    print(f"[SUCCESS] {msg}")

def print_warning(msg):
    print(f"[WARNING] {msg}")

def print_error(msg):
    print(f"[ERROR] {msg}")

def run_command(cmd, ignore_error=False):
    """Runs a shell command and optionally captures/warns on errors."""
    try:
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        if not ignore_error:
            print_warning(f"Command failed: {' '.join(cmd)}\n{e.stderr.strip()}")
        return None

def safe_remove(dst):
    if os.path.exists(dst) or os.path.islink(dst):
        try:
            if os.path.islink(dst) or os.path.isfile(dst):
                os.unlink(dst)
            else:
                shutil.rmtree(dst)
        except Exception:
            pass
    return True

def get_dynamic_plugins(repo_dir):
    """Dynamically scan the plugins/ directory for valid plugins."""
    plugins_dir = repo_dir / "plugins"
    if not plugins_dir.exists():
        return []
    
    valid_plugins = []
    for plugin in plugins_dir.iterdir():
        if plugin.is_dir() and (plugin / "plugin.json").exists():
            valid_plugins.append(plugin.name)
    return sorted(valid_plugins)

def register_via_cli(repo_dir, plugins):
    """Registers plugins properly using native CLIs so they appear in agent UI."""
    if not plugins:
        return

    # 1. Codex CLI Registration
    if shutil.which("codex"):
        print_step("Registering plugins natively via Codex CLI...")
        # Ignore errors on remove in case it's not added yet
        run_command(["codex", "plugin", "marketplace", "remove", "james-skills"], ignore_error=True)
        
        # Add the local marketplace
        success = run_command(["codex", "plugin", "marketplace", "add", str(repo_dir)])
        if success is not None:
            # Install each plugin natively
            for plugin in plugins:
                run_command(["codex", "plugin", "add", f"{plugin}@james-skills"])
        else:
            print_warning("Failed to add Codex marketplace. UI integration may be incomplete.")

    # 2. Claude CLI Registration
    if shutil.which("claude"):
        print_step("Registering plugins natively via Claude CLI...")
        run_command(["claude", "plugin", "marketplace", "remove", "james-skills"], ignore_error=True)
        
        success = run_command(["claude", "plugin", "marketplace", "add", str(repo_dir)])
        if success is not None:
            for plugin in plugins:
                run_command(["claude", "plugin", "install", f"{plugin}@james-skills"])
        else:
            print_warning("Failed to add Claude marketplace. UI integration may be incomplete.")

def main():
    repo_dir = Path(__file__).parent.parent.absolute()
    home = Path.home()
    
    print_step("Validating repository...")
    if platform.system() != "Windows":
        val_res = run_command([str(repo_dir / "scripts" / "validate")], ignore_error=False)
        if val_res is None:
            print_error("Repository validation failed. Aborting installation.")
            sys.exit(1)
        run_command([str(repo_dir / "scripts" / "install-hooks")], ignore_error=True)
        
    dynamic_plugins = get_dynamic_plugins(repo_dir)
    if not dynamic_plugins:
        print_error("No valid plugins found in the plugins/ directory.")
        sys.exit(1)

    print_step(f"Discovered plugins to install: {', '.join(dynamic_plugins)}")
        
    # Attempt native CLI registration first (best UX)
    register_via_cli(repo_dir, dynamic_plugins)

    targets = [
        home / ".agents",
        home / ".codex",
        home / ".claude",
        home / ".cursor"
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

        print_step(f"Installing structural fallbacks to {base_dir}...")
        
        # Cleanup legacy standalone skills and old plugin folders
        if skills_target.exists():
            for item in skills_target.iterdir():
                if item.is_symlink():
                    try:
                        if str(repo_dir) in str(item.resolve()):
                            item.unlink()
                    except Exception:
                        pass
                elif item.name in dynamic_plugins or item.name in ["make-it-james", "proactive-habits", "i-have-adhd"]:
                    safe_remove(str(item))
        
        # Hard copy fallback for plugins (bypasses Go symlink limit)
        for plugin_name in dynamic_plugins:
            src = repo_dir / "plugins" / plugin_name
            dst = plugins_target / plugin_name
            safe_remove(str(dst))
            if platform.system() == "Windows":
                try:
                    import _winapi
                    _winapi.CreateJunction(str(src), str(dst))
                except OSError:
                    shutil.copytree(str(src), str(dst))
            else:
                shutil.copytree(str(src), str(dst))

        # Write plugins.json explicitly for strict agents
        plugins_json_path = base_dir / "plugins.json"
        plugins_config = {"entries": []}
        if plugins_json_path.exists():
            try:
                with open(plugins_json_path, "r") as f:
                    plugins_config = json.load(f)
            except Exception:
                pass
                
        repo_plugins_path = str(repo_dir / "plugins")
        has_entry = any(entry.get("path") == repo_plugins_path for entry in plugins_config.get("entries", []))
        if not has_entry:
            if "entries" not in plugins_config:
                plugins_config["entries"] = []
            plugins_config["entries"].append({"path": repo_plugins_path})
            with open(plugins_json_path, "w") as f:
                json.dump(plugins_config, f, indent=2)

        # Aliases fallback
        for item in promoted_skills:
            for alias in item.get("aliases", []):
                alias_dir = repo_dir / "aliases" / alias
                if (alias_dir / "SKILL.md").exists():
                    dst = skills_target / alias
                    safe_remove(str(dst))
                    if platform.system() == "Windows":
                        try:
                            import _winapi
                            _winapi.CreateJunction(str(alias_dir), str(dst))
                        except OSError:
                            shutil.copytree(str(alias_dir), str(dst))
                    else:
                        shutil.copytree(str(alias_dir), str(dst))
                    
    print_success(f"Installed natively & structural fallbacks updated across platforms from {repo_dir}")

if __name__ == "__main__":
    main()
