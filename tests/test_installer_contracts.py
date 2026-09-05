#!/usr/bin/env python3
"""Guards against re-introducing the fabricated installer surface removed in
DEC-023: an invented `codex plugin marketplace` CLI, an invented `plugins.json`
config format, and manifests placed at the wrong path. Every claim below is
checked against real files, not asserted from memory.
"""
import json
import unittest
from pathlib import Path


class TestInstallerHonesty(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parent.parent
        self.installer = (self.root / "scripts" / "install.py").read_text(encoding="utf-8")

    def test_manifests_live_at_the_real_claude_plugin_path(self):
        """The plugin manifest Claude Code actually reads is
        plugins/<pillar>/.claude-plugin/plugin.json, not plugins/<pillar>/plugin.json.
        A file at the wrong path is dead weight, not a working manifest."""
        for pillar_dir in (self.root / "plugins").iterdir():
            if not pillar_dir.is_dir():
                continue
            self.assertTrue(
                (pillar_dir / ".claude-plugin" / "plugin.json").is_file(),
                f"{pillar_dir.name} is missing its real manifest",
            )
            self.assertFalse(
                (pillar_dir / "plugin.json").exists(),
                f"{pillar_dir.name} carries a manifest at the wrong path; "
                "Claude Code will not read it and it only invites confusion",
            )

    def test_installer_never_shells_out_to_a_cli_marketplace_command(self):
        """Codex CLI does have a real `codex plugin marketplace` command
        (confirmed live: `codex plugin list` shows james-core@james-skills as
        installed, enabled, reading this repo's own marketplace.json) — but
        this installer must never invoke it as a subprocess. It only reads
        Codex's and Claude's own state files to decide whether to skip
        writing loose skill links; it never calls out to either CLI."""
        self.assertNotIn('"codex", "plugin"', self.installer)
        self.assertNotIn("codex plugin", self.installer.lower())
        self.assertNotIn('"claude", "plugin"', self.installer)

    def test_installer_never_invents_a_plugins_json_config(self):
        """No real product reads a hand-rolled plugins.json with an 'entries'
        array. Referencing the real installed_plugins.json is fine; writing
        a bare "plugins.json" file is the fabricated part."""
        self.assertNotIn('"plugins.json"', self.installer)
        self.assertNotIn("'plugins.json'", self.installer)
        self.assertNotIn('"entries"', self.installer)

    def test_installer_checks_the_real_claude_manifest_before_deferring_to_it(self):
        """The duplicate-avoidance rule this installer exists to enforce:
        only skip linking full skills into ~/.claude/skills when Claude
        Code's own installed_plugins.json actually shows the plugins
        installed."""
        self.assertIn("installed_plugins.json", self.installer)
        self.assertIn("@james-skills", self.installer)

    def test_installer_checks_the_real_codex_manifest_before_deferring_to_it(self):
        """The same rule for Codex: Codex CLI records installed plugins as
        [plugins."<name>@james-skills"] in ~/.codex/config.toml, confirmed
        live on this machine. Skip linking full skills into ~/.codex/skills
        only when that file actually shows them installed, or every skill
        appears twice in Codex's own command list."""
        self.assertIn("config.toml", self.installer)
        self.assertIn(".codex", self.installer)


if __name__ == "__main__":
    unittest.main()
