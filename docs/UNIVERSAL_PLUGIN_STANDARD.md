# Universal Agent Plugin Standard

This document defines the structural and installation contract required to guarantee that customizations in this repository successfully mount and **display in the UI** as Plugins across all AI agent platforms (Antigravity, Claude, Cursor, Codex, etc.).

## 1. The Core Architecture & Discovery Problem
Different AI agents use different mechanisms to discover and display plugins:
- **Marketplace UI Agents (Claude, Codex):** These agents maintain an internal registry (`installed_plugins.json`). Simply placing files in a `plugins/` directory will **not** cause them to appear in the user's UI. They require explicit registration via their respective CLIs (`codex plugin add`, `claude plugin install`).
- **File-Watcher Agents (Antigravity):** These agents discover plugins by walking the filesystem. However, agents written in Go (using `filepath.Walk`) **strictly ignore Unix symlinks** for security. If an installer just symlinks folders, these agents will silently fail to load the plugins.

## 2. The Structural Mandate
To guarantee cross-platform compatibility, this repository must strictly adhere to:
1. **Plugin Grouping**: Skills must be grouped into Plugin directories under `/plugins/<namespace>/`.
2. **Manifest Requirement**: Every plugin directory MUST contain a valid `plugin.json` manifest.
3. **Internal Structure**: Skills belong inside the plugin at `plugins/<namespace>/skills/<skill-name>/SKILL.md`.

## 3. The Installation Mandate (The "Never Again" Rule)
Any installation script (`install.py`) **MUST** implement a two-pronged strategy:

### A. Primary Strategy: Native CLI Registration
To ensure plugins appear in the application UI (e.g. Codex/Claude "Installed" tabs), the installer **must** detect available agent CLIs and invoke them to add the marketplace and install the plugins natively:
```bash
codex plugin marketplace add <repo_dir>
codex plugin add <plugin>@<marketplace>
```
The installer must dynamically scan the `plugins/` directory to discover new plugins, rather than hardcoding a list of names.

### B. Fallback Strategy: Hard-Copy & Explicit Registration
For agents without CLIs, or as a robust fallback, the installer MUST NOT rely solely on Unix symlinks.
1. **Windows**: Use Directory Junctions (`_winapi.CreateJunction`).
2. **Mac/Linux**: Perform a recursive hard copy (`shutil.copytree`) into the agent's target directory.
3. **Explicit Config**: The installer must inject the repository's absolute path into the agent's `plugins.json` (for agents that support explicit path loading).
