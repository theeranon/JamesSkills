#!/usr/bin/env python3
"""Filesystem outcomes and the native/shared duplicate regression (DEC-025)."""
import json
import io
from contextlib import redirect_stdout
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
        local=self.local_skill();native=self.native();beta=self.local_skill('beta')
        class Client:
            def call(self,method,params):
                if method=='skills/list':return {'data':[{'skills':[local,native,beta]}]}
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

    def test_override_uncertain_second_write_restores_runtime_and_existing_state(self):
        local=self.local_skill();beta=self.local_skill('beta')
        skills=[local,beta,self.native(),self.native('beta')]
        state=self.home/'.codex/james-skills-local-overrides.json'
        state.parent.mkdir(parents=True)
        original=json.dumps({'paths':['unrelated-user-owned-entry']})+'\n'
        state.write_text(original)
        calls=[]
        class Client:
            def call(self,method,params):
                if method=='skills/list':return {'data':[{'skills':skills}]}
                if method=='skills/config/write':
                    calls.append(dict(params))
                    target=next(x for x in [local,beta] if x['path']==params['path'])
                    target['enabled']=params['enabled']
                    if target is beta and not params['enabled']:
                        raise RuntimeError('response lost after write')
                    return {}
                raise AssertionError(method)
        with self.assertRaisesRegex(RuntimeError,'response lost'):
            reconcile(self.root,self.home,self.catalog,repair=True,client=Client())
        self.assertTrue(local['enabled']);self.assertTrue(beta['enabled'])
        self.assertEqual(state.read_text(),original)
        self.assertEqual([c['enabled'] for c in calls],[False,False,True,True])

    def test_override_postcheck_failure_restores_runtime_and_removes_new_state(self):
        local=self.local_skill();native=self.native()
        class Client:
            def call(self,method,params):
                if method=='skills/list':return {'data':[{'skills':[local,native]}]}
                if method=='skills/config/write':
                    local['enabled']=params['enabled'];return {}
                raise AssertionError(method)
        with self.assertRaisesRegex(RuntimeError,'coverage'):
            reconcile(self.root,self.home,self.catalog,repair=True,client=Client())
        self.assertTrue(local['enabled']);self.assertTrue(native['enabled'])
        self.assertFalse((self.home/'.codex/james-skills-local-overrides.json').exists())

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

    def test_gemini_flat_links_exclude_pilot_and_preserve_other_hosts(self):
        for directory in ['.gemini/config', '.gemini/antigravity/custom']:
            (self.home/directory).mkdir(parents=True)
        first=self.apply()
        self.assertEqual(first,self.apply())
        for directory in ['.gemini/config', '.gemini/antigravity/custom', '.agents', '.codex', '.claude']:
            skills=self.home/directory/'skills'
            self.assertTrue((skills/'alpha').is_symlink())
            self.assertTrue((skills/'beta').is_symlink())
            self.assertTrue((skills/'old-alpha').is_symlink())
            self.assertFalse((skills/'pilot').exists())

    def reconcile_inventory(self,skills):
        class Client:
            def call(self,method,params):
                if method=='skills/list':return {'data':[{'skills':skills}]}
                raise AssertionError('Read-only inventory unexpectedly mutated: '+method)
        output=io.StringIO()
        with redirect_stdout(output):
            reconcile(self.root,self.home,self.catalog,client=Client())
        return output.getvalue()

    def test_empty_and_partial_inventory_fail_coverage(self):
        for skills in [[],[self.local_skill()]]:
            with self.subTest(count=len(skills)):
                with self.assertRaisesRegex(RuntimeError,'(?i)missing|coverage'):
                    self.reconcile_inventory(skills)

    def test_plain_name_local_only_inventory_passes(self):
        skills=[dict(self.local_skill(name),name=name) for name in ['alpha','beta']]
        self.reconcile_inventory(skills)

    def test_native_and_disabled_local_inventory_passes(self):
        self.reconcile_inventory([self.native(),self.local_skill(enabled=False),self.local_skill('beta')])

    def test_preexisting_user_disable_is_reported_and_preserved(self):
        disabled=self.local_skill(enabled=False)
        output=self.reconcile_inventory([disabled,self.local_skill('beta')])
        self.assertFalse(disabled['enabled'])
        self.assertRegex(output.lower(),'user.disabled|disabled.by.user|explicit.*disabled')

    def test_foreign_same_name_plugin_does_not_supply_missing_skill(self):
        foreign=dict(self.native(),pluginId='james-core@unrelated')
        with self.assertRaisesRegex(RuntimeError,'(?i)missing|coverage'):
            self.reconcile_inventory([foreign,self.local_skill('beta')])

    def test_transaction_late_link_failure_restores_prior_links(self):
        self.apply()
        first=self.home/'.agents/skills/alpha'
        second=self.home/'.codex/skills/alpha'
        old_first=os.readlink(first);old_second=os.readlink(second)
        replacement=self.root/'plugins/james-software/skills/beta'
        original=install.link
        def failing_link(src,dst,root):
            if dst==second:raise OSError('late link failure')
            return original(src,dst,root)
        with patch.object(install,'link',side_effect=failing_link):
            with self.assertRaises(OSError):
                install.apply_plan({first:replacement,second:replacement},set(),self.root,postcheck=lambda:None)
        self.assertEqual(os.readlink(first),old_first)
        self.assertEqual(os.readlink(second),old_second)

    def test_transaction_postcheck_failure_restores_removed_and_replaced_links(self):
        self.apply()
        replaced=self.home/'.agents/skills/alpha'
        removed=self.home/'.codex/skills/old-alpha'
        added=self.home/'.agents/skills/new-beta'
        unrelated=self.home/'.agents/skills/user-note'
        unrelated.write_text('keep me')
        before={p:os.readlink(p) for p in [replaced,removed]}
        replacement=self.root/'plugins/james-software/skills/beta'
        def reject():raise RuntimeError('postcheck failed')
        with self.assertRaisesRegex(RuntimeError,'postcheck failed'):
            install.apply_plan({replaced:replacement,added:replacement},{removed},self.root,postcheck=reject)
        for path,target in before.items():self.assertEqual(os.readlink(path),target)
        self.assertFalse(added.exists());self.assertFalse(added.is_symlink())
        self.assertEqual(unrelated.read_text(),'keep me')

    def test_claude_refresh_update_failure_never_uninstalls_or_reinstalls(self):
        scripts=self.root/'scripts';scripts.mkdir()
        shutil.copy2(ROOT/'scripts/refresh-claude-plugins',scripts/'refresh-claude-plugins')
        validator=scripts/'validate';validator.write_text('#!/bin/sh\nexit 0\n');validator.chmod(0o755)
        manifest=self.home/'.claude/plugins/installed_plugins.json'
        manifest.parent.mkdir(parents=True)
        manifest.write_text(json.dumps({'plugins':{'james-core@james-skills':[]}}))
        fake_bin=self.root/'fake-bin';fake_bin.mkdir()
        executable=fake_bin/'claude'
        executable.write_text('#!/bin/sh\nprintf "%s\\n" "$*" >> "$CALL_LOG"\n'
                              'if [ "$1 $2" = "plugin update" ]; then exit 42; fi\nexit 0\n')
        executable.chmod(0o755)
        log=self.root/'claude-calls.txt'
        result=subprocess.run(['bash',str(scripts/'refresh-claude-plugins')],
            env=dict(os.environ,HOME=str(self.home),PATH=str(fake_bin)+os.pathsep+os.environ['PATH'],CALL_LOG=str(log)),
            capture_output=True,text=True)
        self.assertEqual(result.returncode,42)
        self.assertEqual(log.read_text().splitlines(),[
            'plugin marketplace update james-skills',
            'plugin update james-core@james-skills --scope user'])
        self.assertTrue(manifest.exists())

    def test_plugin_manifest_layout(self):
        for p in (ROOT/'plugins').iterdir():
            if p.is_dir():
                self.assertTrue((p/'.claude-plugin/plugin.json').is_file())
                self.assertFalse((p/'plugin.json').exists())

if __name__=='__main__':unittest.main()
