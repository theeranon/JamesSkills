#!/usr/bin/env python3
"""Comprehensive E2E verification test suite for JamesSkills README and visual assets.

Acceptance Criteria Verified:
- AC 1 (Content Completeness):
    * Exactly 21 canonical skills from catalog.json are documented in README.md
      under the "Full Skill Directory" section.
    * Every documented skill has a structured Before/After HTML table (<table>).
    * Every Before/After block contains Thai Unicode characters ([\u0E00-\u0E7F]).
    * Both English and Thai coexist naturally across skill blocks (Bilingual requirement).
- AC 2 (Asset Integrity):
    * All image tags (<img src="..."> and ![...](...)) in README.md are discovered.
    * Every referenced image file exists on disk in assets/ or specified relative paths.
    * No empty, broken, or placeholder image links exist.
    * All image files have non-zero size (> 0 bytes).
- AC 3 (Regression Protection):
    * All existing repository contract, handbook, and lifecycle test suites remain
      intact and pass with 0 exit code.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import unittest
from pathlib import Path
from typing import Dict, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog.json"
README_PATH = ROOT / "README.md"
ASSETS_DIR = ROOT / "assets"
TESTS_DIR = ROOT / "tests"

# Thai Unicode range: \u0E00 to \u0E7F
THAI_UNICODE_PATTERN = re.compile(r"[\u0E00-\u0E7F]")
ENGLISH_PATTERN = re.compile(r"[a-zA-Z]")

# Robust heading pattern matching h3/h4 skill headings with optional emoji/icons and slashes
SKILL_HEADING_PATTERN = re.compile(
    r"^#{3,4}\s+(?:[^\w\s`/#]+\s*)?`?/?([a-z0-9-]+)`?",
    re.MULTILINE,
)

# Robust HTML and Markdown image extraction patterns
HTML_IMG_PATTERN = re.compile(
    r"""<img\s+[^>]*src=["\']([^"\']+)["\'][^>]*>""",
    re.IGNORECASE,
)
MD_IMG_PATTERN = re.compile(
    r"""!\[.*?\]\(([^)]+)\)""",
)


def load_canonical_skills() -> List[str]:
    """Load ordered canonical skill names from catalog.json."""
    if not CATALOG_PATH.exists():
        raise FileNotFoundError(f"catalog.json not found at {CATALOG_PATH}")
    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    return [skill["name"] for skill in catalog.get("skills", [])]


def extract_skill_directory_slice(readme_text: str) -> str:
    """Extract the 'Full Skill Directory' section from README.md."""
    start_match = re.search(
        r"^##\s+.*(?:Full Skill Directory|Skill Directory)",
        readme_text,
        re.MULTILINE | re.IGNORECASE,
    )
    if not start_match:
        raise ValueError("Could not find 'Full Skill Directory' section heading in README.md")

    start_pos = start_match.end()
    # Directory section ends at next major H2 heading (e.g., ## Installation, ## Developers)
    end_match = re.search(r"^##\s+(?!#)", readme_text[start_pos:], re.MULTILINE)
    end_pos = start_pos + end_match.start() if end_match else len(readme_text)
    return readme_text[start_pos:end_pos]


def parse_skill_blocks(directory_text: str, canonical_names: List[str]) -> Dict[str, str]:
    """Parse discrete content blocks for each canonical skill in the directory."""
    matches = list(SKILL_HEADING_PATTERN.finditer(directory_text))
    canonical_set = set(canonical_names)

    skill_occurrences: List[Tuple[str, int]] = []
    for m in matches:
        name = m.group(1)
        if name in canonical_set:
            skill_occurrences.append((name, m.start()))

    blocks: Dict[str, str] = {}
    for i, (name, start_idx) in enumerate(skill_occurrences):
        end_idx = (
            skill_occurrences[i + 1][1]
            if i + 1 < len(skill_occurrences)
            else len(directory_text)
        )
        blocks[name] = directory_text[start_idx:end_idx].strip()
    return blocks


class TestReadmeContentCompleteness(unittest.TestCase):
    """AC 1: Verification of README.md skill documentation completeness and bilingual content."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.canonical_skills = load_canonical_skills()
        cls.readme_text = README_PATH.read_text(encoding="utf-8")
        cls.directory_text = extract_skill_directory_slice(cls.readme_text)
        cls.skill_blocks = parse_skill_blocks(cls.directory_text, cls.canonical_skills)

    def test_catalog_has_exactly_21_canonical_skills(self) -> None:
        """Verify catalog.json contains exactly 21 canonical skills."""
        self.assertEqual(
            len(self.canonical_skills),
            21,
            f"Expected 21 canonical skills in catalog.json, found {len(self.canonical_skills)}: {self.canonical_skills}",
        )

    def test_all_21_canonical_skills_documented_in_readme(self) -> None:
        """Verify all 21 canonical skills from catalog.json are documented in README directory."""
        found_skills = set(self.skill_blocks.keys())
        expected_skills = set(self.canonical_skills)
        missing_skills = sorted(expected_skills - found_skills)
        extra_skills = sorted(found_skills - expected_skills)

        self.assertFalse(
            missing_skills,
            f"README.md Full Skill Directory is missing {len(missing_skills)} canonical skill(s): {missing_skills}",
        )
        self.assertFalse(
            extra_skills,
            f"README.md Full Skill Directory contains unknown skill(s): {extra_skills}",
        )
        self.assertEqual(
            len(found_skills),
            21,
            f"Expected exactly 21 documented skills in README, found {len(found_skills)}",
        )

    def test_every_skill_has_before_after_table(self) -> None:
        """Verify every canonical skill has an HTML Before/After table with valid structure."""
        missing_tables = []
        malformed_tables = []

        for skill_name in self.canonical_skills:
            block = self.skill_blocks.get(skill_name)
            if not block:
                missing_tables.append(f"{skill_name} (skill block missing)")
                continue

            table_match = re.search(r"<table[\s\S]*?</table>", block, re.IGNORECASE)
            if not table_match:
                missing_tables.append(skill_name)
                continue

            table_content = table_match.group(0)
            has_before = bool(re.search(r"before", table_content, re.IGNORECASE))
            has_after = bool(re.search(r"after|outcome", table_content, re.IGNORECASE))
            has_cells = bool(re.search(r"<td[\s\S]*?>", table_content, re.IGNORECASE))

            if not (has_before and has_after and has_cells):
                malformed_tables.append(
                    f"{skill_name} (before={has_before}, after={has_after}, cells={has_cells})"
                )

        self.assertFalse(
            missing_tables,
            f"Skills missing Before/After <table>: {missing_tables}",
        )
        self.assertFalse(
            malformed_tables,
            f"Skills with malformed Before/After <table>: {malformed_tables}",
        )

    def test_thai_unicode_present_in_every_before_after_block(self) -> None:
        """Verify Thai Unicode characters ([\u0E00-\u0E7F]) exist in every Before/After block."""
        missing_thai = []
        for skill_name in self.canonical_skills:
            block = self.skill_blocks.get(skill_name)
            if not block:
                missing_thai.append(f"{skill_name} (skill block missing)")
                continue

            table_match = re.search(r"<table[\s\S]*?</table>", block, re.IGNORECASE)
            target_text = table_match.group(0) if table_match else block

            if not THAI_UNICODE_PATTERN.search(target_text):
                missing_thai.append(skill_name)

        self.assertFalse(
            missing_thai,
            f"Skills missing Thai Unicode characters in Before/After block: {missing_thai}",
        )

    def test_bilingual_english_and_thai_coexistence(self) -> None:
        """Verify all skill blocks incorporate both English and Thai text naturally."""
        non_bilingual = []
        for skill_name in self.canonical_skills:
            block = self.skill_blocks.get(skill_name)
            if not block:
                continue
            has_english = bool(ENGLISH_PATTERN.search(block))
            has_thai = bool(THAI_UNICODE_PATTERN.search(block))
            if not (has_english and has_thai):
                non_bilingual.append(f"{skill_name} (en={has_english}, th={has_thai})")

        self.assertFalse(
            non_bilingual,
            f"Skills failing bilingual English+Thai requirement: {non_bilingual}",
        )


class TestReadmeAssetIntegrity(unittest.TestCase):
    """AC 2: Verification of visual asset integrity and image references in README.md."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.readme_text = README_PATH.read_text(encoding="utf-8")
        cls.html_images = HTML_IMG_PATTERN.findall(cls.readme_text)
        cls.md_images = MD_IMG_PATTERN.findall(cls.readme_text)
        cls.all_images = cls.html_images + cls.md_images

    def test_image_tags_present_and_well_formed(self) -> None:
        """Verify README contains image tags and none have empty or invalid src."""
        self.assertGreater(
            len(self.all_images),
            0,
            "Expected at least one visual asset image referenced in README.md",
        )
        for img_src in self.all_images:
            cleaned = img_src.strip()
            self.assertTrue(
                cleaned and cleaned != "#" and not cleaned.startswith("http://example"),
                f"Invalid or placeholder image src found: '{img_src}'",
            )

    def test_all_referenced_images_exist_on_disk(self) -> None:
        """Verify all local image files referenced in README exist on disk and are non-empty."""
        broken_links = []
        empty_files = []

        for img_src in self.all_images:
            clean_path = img_src.split("?")[0].split("#")[0].strip()
            if clean_path.startswith("http://") or clean_path.startswith("https://"):
                continue  # Skip remote URLs

            target_path = ROOT / clean_path
            if not target_path.exists() or not target_path.is_file():
                broken_links.append((img_src, str(target_path)))
            elif target_path.stat().st_size == 0:
                empty_files.append((img_src, str(target_path)))

        self.assertFalse(
            broken_links,
            f"Broken image links in README.md (file missing on disk): {broken_links}",
        )
        self.assertFalse(
            empty_files,
            f"Empty image files referenced in README.md (0 bytes): {empty_files}",
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
        for f in asset_files:
            self.assertGreater(
                f.stat().st_size,
                0,
                f"Asset file {f.name} is 0 bytes",
            )


class TestRegressionProtection(unittest.TestCase):
    """AC 3: Ensure existing regression test suites remain intact and functional."""

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
    """Run verification suite as standalone runner with structured summary output."""
    print("=" * 70)
    print("JamesSkills README & Asset Verification Harness")
    print(f"Root: {ROOT}")
    print("=" * 70)

    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestReadmeContentCompleteness))
    suite.addTests(loader.loadTestsFromTestCase(TestReadmeAssetIntegrity))
    suite.addTests(loader.loadTestsFromTestCase(TestRegressionProtection))

    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    print("\n" + "=" * 70)
    if result.wasSuccessful():
        print(f"ALL VERIFICATION TESTS PASSED ({result.testsRun} tests)")
        print("=" * 70)
        return 0
    else:
        print(
            f"VERIFICATION SUITE FAILED: {len(result.failures)} failure(s), "
            f"{len(result.errors)} error(s) out of {result.testsRun} tests"
        )
        print("=" * 70)
        return 1


if __name__ == "__main__":
    sys.exit(main())
