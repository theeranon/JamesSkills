#!/usr/bin/env python3
"""Filesystem outcomes and the native/shared duplicate regression (DEC-025)."""
import json
import os
import shutil
import subprocess
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
import install
from codex_skills import desired_overrides, reconcile


class InstallerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()/'repo'
        self.home = Path(self.tmp.name).resolve()/'home'
        self.home.mkdir()
        self.catalog = {'skills': [
            {'name':'alpha','category':'james-core','status':'promoted','aliases':['old-alpha']},
            {'name':'beta','category':'james-software','status':'promoted','aliases':[]},
            {'name':'pilot','category':'james-core','status':'pilot','aliases':[]}]}
        for item in self.catalog['skills']:
            d=self.root/'plugins'/item['category']/'skills'/item['name']
            d.mkdir(parents=True,exist_ok=True)
            (d/'SKILL.md').write_text(item['name'])
        d=self.root/'aliases/old-alpha'
        d.mkdir(parents=True)
        (d/'SKILL.md').write_text('alias')
        self.environment=patch.dict(os.environ,{},clear=False)
        self.environment.start()
        os.environ.pop('CODEX_HOME',None)
        os.environ.pop('CLAUDE_CONFIG_DIR',None)
        self.addCleanup(self.environment.stop)

    def apply(self):
        links,removals=install.plan(self.root,self.home,self.catalog)
        for dst in removals:dst.unlink()
        for dst,src in links.items():install.link(src,dst,self.root)
        return links

    def local_skill(self,name='alpha',enabled=True):
        item=next(i for i in self.catalog['skills'] if i['name']==name)
        return {'name':item['category']+':'+name,'enabled':enabled,'pluginId':None,
                'path':str(self.root/'plugins'/item['category']/'skills'/name/'SKILL.md')}

    def native(self,name='alpha',enabled=True):
        s=self.local_skill(name,enabled)
        s['pluginId']=s['name'].split(':')[0]+'@james-skills'
        s['path']=str(self.home/'cache'/name/'SKILL.md')
        return s

    def test_clean_install_idempotent_aliases_and_no_pilot(self):
        first=self.apply()
        self.assertEqual(first,self.apply())
        for root in ['.agents','.codex','.claude']:
            base=self.home/root/'skills'
            self.assertEqual((base/'alpha/SKILL.md').read_text(),'alpha')
            self.assertTrue((base/'old-alpha').is_symlink())
            self.assertFalse((base/'pilot').exists())

    def test_directory_file_and_foreign_symlink_collisions_preserved_before_any_write(self):
        for kind in ['dir','file','symlink']:
            with self.subTest(kind=kind):
                dst=self.home/'.codex/skills/alpha';dst.parent.mkdir(parents=True,exist_ok=True)
                if kind=='dir':dst.mkdir();(dst/'keep').write_text('mine')
                elif kind=='file':dst.write_text('mine')
                else:dst.symlink_to(self.home/'foreign')
                with self.assertRaisesRegex(RuntimeError,'Collision'):self.apply()
                self.assertFalse((self.home/'.agents/skills/alpha').exists())
                if kind=='dir':self.assertEqual((dst/'keep').read_text(),'mine');(dst/'keep').unlink();dst.rmdir()
                else:dst.unlink()

    def test_partial_claude_install_does_not_hide_other_pillars(self):
        d=self.home/'cache/core';(d/'.claude-plugin').mkdir(parents=True);(d/'skills').mkdir()
        (d/'.claude-plugin/plugin.json').write_text('{}')
        (d/'skills/alpha').mkdir();(d/'skills/alpha/SKILL.md').write_text('alpha')
        manifest=self.home/'.claude/plugins/installed_plugins.json';manifest.parent.mkdir(parents=True)
        manifest.write_text(json.dumps({'plugins':{'james-core@james-skills':[{'scope':'user','installPath':str(d)}]}}))
        self.apply()
        self.assertFalse((self.home/'.claude/skills/alpha').exists())
        self.assertTrue((self.home/'.claude/skills/beta').is_symlink())
        settings=self.home/'.claude/settings.json';settings.write_text(json.dumps({'enabledPlugins':{'james-core@james-skills':False}}))
        self.apply()
        self.assertTrue((self.home/'.claude/skills/alpha').is_symlink())

    def test_rejected_case_shared_root_plus_native_plugin(self):
        local=self.local_skill();native=self.native()
        changes,_=desired_overrides(self.root,self.catalog,[local,native],set())
        self.assertEqual(changes,[(local['path'],False)])
        self.assertNotEqual(changes[0][0],native['path'])

    def test_same_mechanism_second_pillar(self):
        local=self.local_skill('beta')
        changes,_=desired_overrides(self.root,self.catalog,[local,self.native('beta')],set())
        self.assertEqual(changes,[(local['path'],False)])

    def test_countercase_missing_disabled_or_other_plugin_keeps_local_enabled(self):
        local=self.local_skill()
        for native in [None,self.native(enabled=False),dict(self.native(),pluginId='james-core@other')]:
            changes,_=desired_overrides(self.root,self.catalog,[local]+([native] if native else []),set())
            self.assertEqual(changes,[])

    def test_preexisting_user_disable_preserved_and_owned_disable_restored(self):
        local=self.local_skill(enabled=False)
        self.assertEqual(desired_overrides(self.root,self.catalog,[local],set())[0],[])
        self.assertEqual(desired_overrides(self.root,self.catalog,[local],{local['path']})[0],[(local['path'],True)])

    def test_reconcile_roundtrip_and_check_detects_regression(self):
        local=self.local_skill();native=self.native()
        class Client:
            def call(self,method,params):
                if method=='skills/list':return {'data':[{'skills':[local,native]}]}
                if method=='skills/config/write':
                    assert params['path']==local['path']
                    local['enabled']=params['enabled'];return {}
                raise AssertionError(method)
        with self.assertRaisesRegex(RuntimeError,'unresolved'):
            reconcile(self.root,self.home,self.catalog,client=Client())
        reconcile(self.root,self.home,self.catalog,repair=True,client=Client())
        self.assertFalse(local['enabled']);self.assertTrue(native['enabled'])
        reconcile(self.root,self.home,self.catalog,client=Client())
        native['enabled']=False
        reconcile(self.root,self.home,self.catalog,repair=True,client=Client())
        self.assertTrue(local['enabled'])

    def test_failed_validator_stops_before_creating_discovery_links(self):
        scripts=self.root/'scripts';scripts.mkdir()
        for name in ['install.py','codex_skills.py']:
            shutil.copy2(ROOT/'scripts'/name,scripts/name)
        (scripts/'validate').write_text('#!/usr/bin/env bash\nexit 71\n')
        result=subprocess.run([sys.executable,str(scripts/'install.py')],
            env=dict(os.environ,HOME=str(self.home)),capture_output=True,text=True)
        self.assertNotEqual(result.returncode,0)
        self.assertFalse((self.home/'.agents').exists())
        self.assertFalse((self.home/'.codex').exists())

    def test_failed_symlink_creation_preserves_previous_managed_link(self):
        links=self.apply()
        dst=self.home/'.agents/skills/alpha'
        previous=os.readlink(dst)
        replacement=self.root/'plugins/james-software/skills/beta'
        with patch.object(Path,'symlink_to',side_effect=OSError('permission denied')):
            with self.assertRaises(OSError):install.link(replacement,dst,self.root)
        self.assertEqual(os.readlink(dst),previous)
        self.assertEqual((dst/'SKILL.md').read_text(),'alpha')

    def test_whole_plugin_links_cannot_expose_pilot(self):
        (self.home/'.gemini/config').mkdir(parents=True)
        with self.assertRaisesRegex(RuntimeError,'pilot'):
            install.plan(self.root,self.home,self.catalog)
        self.assertFalse((self.home/'.agents/skills').exists())

    def test_plugin_manifest_layout(self):
        for p in (ROOT/'plugins').iterdir():
            if p.is_dir():
                self.assertTrue((p/'.claude-plugin/plugin.json').is_file())
                self.assertFalse((p/'plugin.json').exists())

if __name__=='__main__':unittest.main()
