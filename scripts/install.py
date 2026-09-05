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

def print_error(msg):
    print(f"[ERROR] {msg}")

def run_command(cmd, ignore_error=False):
    try:
        subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        if not ignore_error:
            print_error(f"Command failed: {' '.join(cmd)}")

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

def register_via_cli(repo_dir):
    """Registers plugins properly using the native CLI (if installed) so they appear in the UI."""
    plugins = ["james-core", "james-productivity", "james-software"]
    
    # Codex CLI
    if shutil.which("codex"):
        print_step("Registering plugins natively in Codex CLI...")
        run_command(["codex", "plugin", "marketplace", "remove", "james-skills"], ignore_error=True)
        run_command(["codex", "plugin", "marketplace", "add", str(repo_dir)])
        for plugin in plugins:
            run_command(["codex", "plugin", "add", f"{plugin}@james-skills"], ignore_error=True)

    # Claude CLI
    if shutil.which("claude"):
        print_step("Registering plugins natively in Claude CLI...")
        run_command(["claude", "plugin", "marketplace", "remove", "james-skills"], ignore_error=True)
        run_command(["claude", "plugin", "marketplace", "add", str(repo_dir)])
        for plugin in plugins:
            run_command(["claude", "plugin", "install", f"{plugin}@james-skills"], ignore_error=True)

def main():
    repo_dir = Path(__file__).parent.parent.absolute()
    home = Path.home()
    
    print_step("Validating repository...")
    if platform.system() != "Windows":
        os.system(f'"{repo_dir}/scripts/validate"')
        os.system(f'"{repo_dir}/scripts/install-hooks"')
        
    # Attempt native CLI registration
    register_via_cli(repo_dir)

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

        print_step(f"Installing structural fallbacks to {base_dir}...")
        
        # Cleanup legacy standalone skills to prevent double-loading
        if skills_target.exists():
            for item in skills_target.iterdir():
                if item.is_symlink():
                    try:
                        if str(repo_dir) in str(item.resolve()):
                            item.unlink()
                    except Exception:
                        pass
                elif item.name in ["james-core", "james-productivity", "james-software", "make-it-james", "proactive-habits", "i-have-adhd"]:
                    safe_remove(str(item))
        
        # Hard copy fallback for plugins
        for plugin in (repo_dir / "plugins").iterdir():
            if plugin.is_dir() and (plugin / "plugin.json").exists():
                dst = plugins_target / plugin.name
                safe_remove(str(dst))
                if platform.system() == "Windows":
                    try:
                        import _winapi
                        _winapi.CreateJunction(str(plugin), str(dst))
                    except OSError:
                        shutil.copytree(str(plugin), str(dst))
                else:
                    shutil.copytree(str(plugin), str(dst))

        # Write plugins.json explicitly
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
                    
    print_success(f"Installed successfully natively across platforms from {repo_dir}")

if __name__ == "__main__":
    main()
