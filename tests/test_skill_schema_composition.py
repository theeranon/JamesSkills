#!/usr/bin/env python3
"""Exercise schema acceptance/rejection with independent minimal package fixtures."""
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest
spec=importlib.util.spec_from_file_location('schema',Path(__file__).with_name('test_skill_schema.py'))
schema=importlib.util.module_from_spec(spec); spec.loader.exec_module(schema)
class CompositionSchema(unittest.TestCase):
    def check_fixture(self, extra='', omit_scope=False):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp); body=root/'plugins/demo/skills/example/SKILL.md';body.parent.mkdir(parents=True)
            body.write_text('---\nname: example\nkind: mode\nlicense: CC-BY-NC-4.0\ndescription: Maintain the selected working mode throughout the conversation.\n---\n# Example\n\nKeep the selected mode active.\n\n'+('' if omit_scope else '## Scope\n- Kind: mode\n- Owns: conversation behavior\n- Boundary: no new authority\n')+'## Behavior\nCompose with requested tasks.\n## Stays active until\nUser disables it.\n'+extra+'## Counter-case\n- A task finishes; this mode remains active.\n- User disables it; stop applying it.\n## Hand back\nThe requested task result.\n')
            (root/'catalog.json').write_text(json.dumps({'skills':[{'name':'example','category':'demo','kind':'mode'}]}))
            (root/'tests').mkdir();(root/'tests/behavioral-cases.md').write_text('`example`')
            (root/'VERSION').write_text('1.0.0');(root/'.claude-plugin').mkdir()
            (root/'.claude-plugin/marketplace.json').write_text(json.dumps({'version':'1.0.0','plugins':[{'name':'demo','source':'./plugins/demo'}]}))
            (root/'plugins/demo/.claude-plugin').mkdir();(root/'plugins/demo/.claude-plugin/plugin.json').write_text(json.dumps({'name':'demo','version':'1.0.0'}))
            old=schema.ROOT
            try:
                schema.ROOT=root
                with contextlib.redirect_stdout(io.StringIO()):return schema.main()
            finally:schema.ROOT=old
    def test_mode_without_routing_or_principle_quota(self):self.assertEqual(self.check_fixture(),0)
    def test_composition_heading_is_allowed(self):self.assertEqual(self.check_fixture('## Works with\nTask workflows.\n'),0)
    def test_missing_authority_scope_still_fails(self):self.assertEqual(self.check_fixture(omit_scope=True),1)
    def test_unknown_explicit_route_still_fails(self):self.assertEqual(self.check_fixture('## Do not use this when\n- Different task -> `nonexistent`\n'),1)
if __name__=='__main__':unittest.main()
