#!/usr/bin/env python3
"""Automated verification harness for JamesSkills README.md and visual assets.

Enforces standards from ai-context/README_STANDARD.md and DEC-012:
- Exactly 21 canonical skills from catalog.json are documented in the Scannable Directory Table.
- The Iconic Showcase features valid Before/After comparison tables.
- Natural coexistence of English and Thai across the documentation.
- All image links resolve to non-empty assets on disk.
- Core regression test suites remain 100% green.
"""

import json
from pathlib import Path
import re
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
CATALOG_PATH = ROOT / "catalog.json"
ASSETS_DIR = ROOT / "assets"

THAI_UNICODE_PATTERN = re.compile(r"[\u0E00-\u0E7F]")
ENGLISH_PATTERN = re.compile(r"[A-Za-z]{3,}")
HTML_IMG_PATTERN = re.compile(r"""<img[^>]+src=["']([^"']+)["']""", re.IGNORECASE)
MD_IMG_PATTERN = re.compile(r"""!\[.*?\]\(([^)]+)\)""", re.IGNORECASE)


class TestReadmeContentCompleteness(unittest.TestCase):
    """Verification of README.md skill catalog and showcase completeness."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.readme_text = README_PATH.read_text(encoding="utf-8")
        cls.catalog_data = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
        cls.canonical_skills = [
            item["name"]
            for item in cls.catalog_data.get("skills", [])
            if item.get("status") == "promoted"
        ]

    def test_catalog_has_exactly_21_canonical_skills(self) -> None:
        """Verify catalog.json contains exactly 21 canonical skills."""
        self.assertEqual(
            21,
            len(self.canonical_skills),
            f"Expected 21 canonical skills in catalog.json, found {len(self.canonical_skills)}: {self.canonical_skills}",
        )

    def test_all_21_canonical_skills_documented_in_readme(self) -> None:
        """Verify all 21 canonical skills from catalog.json are documented in README directory."""
        missing = []
        for skill_name in self.canonical_skills:
            pattern = re.compile(rf"[`/]{re.escape(skill_name)}[`/]", re.IGNORECASE)
            if not pattern.search(self.readme_text):
                missing.append(skill_name)

        self.assertFalse(
            missing,
            f"Missing canonical skills in README.md: {missing}",
        )

    def test_iconic_showcase_has_before_after_tables(self) -> None:
        """Verify the Iconic Showcase contains valid Before/After tables."""
        tables = re.findall(r"<table[\s\S]*?</table>", self.readme_text, re.IGNORECASE)
        self.assertGreaterEqual(
            len(tables),
            1,
            "Expected at least one Before/After showcase table in README.md",
        )
        for table in tables:
            has_before = bool(re.search(r"before|standard ai", table, re.IGNORECASE))
            has_after = bool(re.search(r"after|jamesskills", table, re.IGNORECASE))
            self.assertTrue(
                has_before and has_after,
                "Showcase table must contain both Before and After headers",
            )

    def test_bilingual_english_and_thai_coexistence(self) -> None:
        """Verify README incorporates both English and Thai text naturally."""
        self.assertTrue(
            bool(THAI_UNICODE_PATTERN.search(self.readme_text)),
            "README must contain Thai Unicode characters",
        )
        self.assertTrue(
            bool(ENGLISH_PATTERN.search(self.readme_text)),
            "README must contain English documentation text",
        )


class TestReadmeAssetIntegrity(unittest.TestCase):
    """Verification of visual asset integrity and image references in README.md."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.readme_text = README_PATH.read_text(encoding="utf-8")
        cls.html_images = HTML_IMG_PATTERN.findall(cls.readme_text)
        cls.md_images = MD_IMG_PATTERN.findall(cls.readme_text)
        cls.all_images = cls.html_images + cls.md_images

    def test_all_referenced_images_exist_on_disk(self) -> None:
        """Verify all local image files referenced in README exist on disk and are non-empty."""
        broken_links = []
        empty_files = []

        for img_src in self.all_images:
            clean_path = img_src.split("?")[0].split("#")[0].strip()
            if clean_path.startswith("http://") or clean_path.startswith("https://"):
                continue

            target_path = ROOT / clean_path
            if not target_path.exists() or not target_path.is_file():
                broken_links.append((img_src, str(target_path)))
            elif target_path.stat().st_size == 0:
                empty_files.append((img_src, str(target_path)))

        self.assertFalse(
            broken_links,
            f"Broken image links in README.md: {broken_links}",
        )
        self.assertFalse(
            empty_files,
            f"Empty image files referenced in README.md: {empty_files}",
        )

    def test_assets_directory_contains_valid_files(self) -> None:
        """Verify assets/ directory exists and contains non-empty media assets."""
        self.assertTrue(
            ASSETS_DIR.exists() and ASSETS_DIR.is_dir(),
            f"Assets directory not found at {ASSETS_DIR}",
        )
        asset_files = [
            f for f in ASSETS_DIR.iterdir()
            if f.is_file() and not f.name.startswith(".")
        ]
        self.assertGreater(
            len(asset_files),
            0,
            "Assets directory exists but contains no valid media files",
        )


class TestRegressionProtection(unittest.TestCase):
    """Ensure existing regression test suites remain intact and functional."""

    REGRESSION_TEST_FILES = [
        "tests/test_skill_handbook.py",
        "tests/test_portfolio_lifecycle.py",
        "tests/test_catchup_contracts.py",
        "tests/test_core_composition_contracts.py",
        "tests/test_output_contracts.py",
        "tests/test_project_self_standard.py",
        "tests/test_update_preflight.py",
    ]

    def test_all_regression_test_files_exist(self) -> None:
        """Verify all existing contract and regression test files exist on disk."""
        missing = [f for f in self.REGRESSION_TEST_FILES if not (ROOT / f).exists()]
        self.assertFalse(missing, f"Missing regression test files: {missing}")

    def test_run_existing_contract_suites(self) -> None:
        """Execute each contract test suite and verify 0 exit code."""
        failures = []
        for rel_path in self.REGRESSION_TEST_FILES:
            full_path = ROOT / rel_path
            res = subprocess.run(
                [sys.executable, str(full_path)],
                cwd=str(ROOT),
                capture_output=True,
                text=True,
            )
            if res.returncode != 0:
                failures.append(
                    f"{rel_path} exited with code {res.returncode}:\nSTDOUT: {res.stdout}\nSTDERR: {res.stderr}"
                )

        self.assertFalse(
            failures,
            f"Regression test suite failures encountered:\n" + "\n---\n".join(failures),
        )


def main() -> int:
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestReadmeContentCompleteness))
    suite.addTests(loader.loadTestsFromTestCase(TestReadmeAssetIntegrity))
    suite.addTests(loader.loadTestsFromTestCase(TestRegressionProtection))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    sys.exit(main())
