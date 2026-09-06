#!/usr/bin/env python3
"""Repo-local export mode: plain committable files, no global registry involved."""
import json
import sys
import tempfile
import subprocess
from unittest import mock
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import export


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.target = Path(self.tmp.name)/'some-project'
        self.target.mkdir()
        self.catalog = json.loads((ROOT/'catalog.json').read_text())

    def test_default_exports_every_promoted_skill_as_plain_files(self):
        written = export.export(self.target, None, self.catalog)
        promoted = [s['name'] for s in self.catalog['skills'] if s['status'] == 'promoted']
        self.assertEqual(sorted(written), sorted(promoted))
        for name in promoted:
            path = self.target/'.agents/skills'/name/'SKILL.md'
            self.assertTrue(path.is_file())
            self.assertFalse(path.is_symlink())

    def test_named_subset_only(self):
        written = export.export(self.target, ['research-it'], self.catalog)
        self.assertEqual(written, ['research-it'])
        self.assertTrue((self.target/'.agents/skills/research-it/SKILL.md').is_file())
        self.assertFalse((self.target/'.agents/skills/done-for-me').exists())

    def test_alias_resolves_to_real_skill_directory(self):
        written = export.export(self.target, ['prove-it'], self.catalog)
        self.assertEqual(written, ['research-it'])
        self.assertTrue((self.target/'.agents/skills/research-it/SKILL.md').is_file())

    def test_unknown_skill_name_raises_before_writing_anything(self):
        with self.assertRaisesRegex(RuntimeError, 'Unknown skill'):
            export.export(self.target, ['not-a-real-skill'], self.catalog)

    def test_re_export_preserves_user_changes(self):
        export.export(self.target, ['research-it'], self.catalog)
        note = self.target/'.agents/skills/research-it/user-note.txt'
        note.write_text('user work')
        with self.assertRaisesRegex(RuntimeError, 'preserved'):
            export.export(self.target, ['research-it'], self.catalog)
        self.assertEqual(note.read_text(), 'user work')

    def test_late_unknown_name_does_not_partially_export(self):
        with self.assertRaisesRegex(RuntimeError, 'Unknown skill'):
            export.export(self.target, ['research-it', 'not-real'], self.catalog)
        self.assertFalse((self.target/'.agents').exists())

    def test_identical_re_export_is_idempotent(self):
        export.export(self.target, ['research-it'], self.catalog)
        file = self.target/'.agents/skills/research-it/SKILL.md'
        before = file.stat().st_mtime_ns
        export.export(self.target, ['research-it'], self.catalog)
        self.assertEqual(before, file.stat().st_mtime_ns)

    def test_shared_root_symlink_is_preserved(self):
        other = self.target/'other'
        other.mkdir()
        (self.target/'.agents').symlink_to(other, target_is_directory=True)
        with self.assertRaisesRegex(RuntimeError, 'Unsafe'):
            export.export(self.target, ['research-it'], self.catalog)
        self.assertEqual(list(other.iterdir()), [])

    def test_pilot_rejected_before_any_write(self):
        item = next(x for x in self.catalog['skills'] if x['name'] == 'research-it')
        item['status'] = 'pilot'
        with self.assertRaisesRegex(RuntimeError, 'not promoted'):
            export.export(self.target, ['done-for-me', 'research-it'], self.catalog)
        self.assertFalse((self.target/'.agents').exists())

    def test_exported_baseon_runs_after_relocation(self):
        export.export(self.target, ['baseon'], self.catalog)
        relocated = self.target.with_name('relocated')
        self.target.rename(relocated)
        skill = relocated/'.agents/skills/baseon'
        result = subprocess.run([sys.executable, str(skill/'scripts/knowledge_library.py'), 'list'],
                                cwd=relocated, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('wealth-dynamics', result.stdout)
        self.assertIn('satir-model', result.stdout)

    def test_relative_font_helper_is_exported_and_executable(self):
        export.export(self.target, ['sum-meet'], self.catalog)
        helper = (self.target/'.agents/skills/sum-meet'/
                  '../../../james-software/skills/make-it-james-ux/scripts/embed_ibm_plex_thai.py').resolve()
        self.assertTrue(helper.is_file())
        result = subprocess.run([sys.executable, str(helper), '--help'], cwd=self.target,
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('--font-dir', result.stdout)
        self.assertFalse((helper.parent.parent/'SKILL.md').exists())

    def test_dependency_collision_fails_before_skill_write(self):
        packs = self.target/'.agents/packs'
        packs.mkdir(parents=True)
        (packs/'mine.txt').write_text('preserve')
        with self.assertRaisesRegex(RuntimeError, 'dependency differs'):
            export.export(self.target, ['baseon'], self.catalog)
        self.assertFalse((self.target/'.agents/skills/baseon').exists())
        self.assertEqual((packs/'mine.txt').read_text(), 'preserve')

    def test_dependency_copy_failure_rolls_back_new_skill(self):
        real_copy = export.shutil.copytree
        def fail_dependency(source, destination, *args, **kwargs):
            if Path(source).name == 'packs':
                raise OSError('injected dependency failure')
            return real_copy(source, destination, *args, **kwargs)
        with mock.patch.object(export.shutil, 'copytree', side_effect=fail_dependency):
            with self.assertRaisesRegex(OSError, 'injected'):
                export.export(self.target, ['baseon'], self.catalog)
        self.assertFalse((self.target/'.agents/skills/baseon').exists())
        self.assertFalse((self.target/'.agents/packs').exists())


if __name__ == '__main__':
    unittest.main()
