import os
import json
import unittest
from pathlib import Path

class TestUniversalPluginStandard(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).parent.parent.absolute()

    def test_all_plugins_have_manifests(self):
        """Verify every folder in plugins/ has a plugin.json manifest."""
        plugins_dir = self.root / "plugins"
        self.assertTrue(plugins_dir.exists(), "plugins/ directory must exist")
        
        plugin_folders = [d for d in plugins_dir.iterdir() if d.is_dir()]
        self.assertTrue(len(plugin_folders) > 0, "Must have at least one plugin")
        
        for plugin in plugin_folders:
            manifest = plugin / "plugin.json"
            self.assertTrue(manifest.exists(), f"Plugin {plugin.name} is missing plugin.json")
            with open(manifest, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.assertIn("name", data, f"Plugin {plugin.name} manifest must declare a name")

    def test_installer_enforces_explicit_registration(self):
        """Verify install.py explicitly writes to plugins.json to bypass Go symlink limits."""
        installer_path = self.root / "scripts" / "install.py"
        self.assertTrue(installer_path.exists(), "install.py missing")
        
        with open(installer_path, "r", encoding="utf-8") as f:
            code = f.read()
            
        self.assertIn('plugins.json', code, "Installer MUST reference plugins.json")
        self.assertIn('"entries"', code, "Installer MUST inject path into the 'entries' array")

    def test_installer_enforces_native_cli_registration(self):
        """Verify install.py calls native CLIs to register plugins into UI marketplaces."""
        installer_path = self.root / "scripts" / "install.py"
        with open(installer_path, "r", encoding="utf-8") as f:
            code = f.read()
            
        self.assertIn('codex", "plugin", "marketplace", "add"', code, "Installer MUST use Codex CLI")
        self.assertIn('claude", "plugin", "marketplace", "add"', code, "Installer MUST use Claude CLI")

if __name__ == "__main__":
    unittest.main()
