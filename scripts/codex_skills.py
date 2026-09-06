#!/usr/bin/env python3
"""Reconcile shared skills with Codex native plugins through its real app-server API.

Keep shared links available to other hosts. Disable only the exact local SKILL.md
when an enabled native plugin supplies the same skill. No name-wide disable.
"""
from __future__ import annotations
import json
import os
from pathlib import Path
import queue
import shutil
import subprocess
import threading
import time


class CodexClient:
    def __init__(self, executable):
        self.process = subprocess.Popen([executable, 'app-server', '--stdio'],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            text=True, bufsize=1)
        self.messages = queue.Queue()
        self.sequence = 0
        def read():
            for line in self.process.stdout:
                try: self.messages.put(json.loads(line))
                except ValueError: pass
            self.messages.put({'error': 'Codex app-server closed'})
        threading.Thread(target=read, daemon=True).start()
        try:
            self.call('initialize', {'clientInfo': {'name': 'jamesskills_installer', 'version': '1'},
                                    'capabilities': {'experimentalApi': True}})
            self.process.stdin.write('{"method":"initialized"}\n')
            self.process.stdin.flush()
        except Exception:
            self.close()
            raise

    def call(self, method, params):
        self.sequence += 1
        self.process.stdin.write(json.dumps({'id': self.sequence, 'method': method, 'params': params})+'\n')
        self.process.stdin.flush()
        deadline = time.monotonic() + 30
        while time.monotonic() < deadline:
            try: message = self.messages.get(timeout=max(.01, deadline-time.monotonic()))
            except queue.Empty: break
            if message.get('id') == self.sequence:
                if 'error' in message: raise RuntimeError(str(message['error']))
                return message['result']
            if message.get('error'): raise RuntimeError(str(message['error']))
        raise RuntimeError('Codex app-server timed out: '+method)

    def close(self):
        self.process.terminate()
        try: self.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait()


def list_skills(client, root):
    result = client.call('skills/list', {'cwds': [str(root)], 'forceReload': True})
    return [s for entry in result['data'] for s in entry['skills']]


def desired_overrides(root, catalog, skills, managed):
    """Only paired, enabled native skills justify disabling a local counterpart."""
    natives = {(s.get('pluginId'), s['name'].split(':')[-1]) for s in skills
               if s.get('pluginId') and s.get('enabled')}
    local = {str(Path(s['path']).resolve()): s for s in skills if not s.get('pluginId')}
    changes = []
    expected = set()
    for item in catalog['skills']:
        if item['status'] != 'promoted': continue
        path = str((root/'plugins'/item['category']/'skills'/item['name']/'SKILL.md').resolve())
        skill = local.get(path)
        if not skill: continue
        covered = (item['category']+'@james-skills', item['name']) in natives
        if covered:
            expected.add(path)
            if skill['enabled']: changes.append((path, False))
        elif path in managed and not skill['enabled']:
            changes.append((path, True))
    return changes, expected


def check_coverage(root, catalog, skills, managed):
    """Count actual enabled owners by package identity, not display-name spelling."""
    missing, duplicates, user_disabled = [], [], []
    enabled_count = 0
    for item in catalog['skills']:
        if item['status'] != 'promoted': continue
        name = item['name']
        path = (root/'plugins'/item['category']/'skills'/name/'SKILL.md').resolve()
        entries = [s for s in skills if
                   (s.get('pluginId') == item['category']+'@james-skills'
                    and s['name'].split(':')[-1] == name)
                   or (not s.get('pluginId') and Path(s['path']).resolve() == path)]
        count = sum(bool(s.get('enabled')) for s in entries)
        if count > 1: duplicates.append(name)
        elif count == 1: enabled_count += 1
        elif any(not s.get('pluginId') and not s.get('enabled') for s in entries) and str(path) not in managed:
            user_disabled.append(name)
        else: missing.append(name)
    if missing or duplicates:
        raise RuntimeError('Codex coverage mismatch: missing='+','.join(missing)+
                           ' duplicates='+','.join(duplicates))
    if user_disabled:
        print('NOTE Codex user-disabled (preserved, not enabled coverage): '+', '.join(user_disabled))
    return enabled_count, len(user_disabled)


def reconcile(root, home, catalog, repair=False, client=None):
    executable = shutil.which('codex')
    if client is None and not executable:
        print('SKIP Codex runtime check: codex not on PATH; no runtime claim')
        return
    owns_client = client is None
    if owns_client: client = CodexClient(executable)
    codex_home = Path(os.environ.get('CODEX_HOME', str(home/'.codex')))
    state_path = codex_home/'james-skills-local-overrides.json'
    original_state = state_path.read_bytes() if state_path.exists() else None
    attempted = []
    try:
        state = json.loads(state_path.read_text()) if state_path.exists() else {'paths': []}
        managed = set(state['paths'])
        skills = list_skills(client, root)
        changes, expected = desired_overrides(root, catalog, skills, managed)
        if changes and not repair:
            raise RuntimeError(f'Codex has {len(changes)} unresolved local/plugin overrides; run scripts/install')
        if changes:
            backup_dir = codex_home/'james-skills-backups'
            backup_dir.mkdir(parents=True, exist_ok=True)
            config = codex_home/'config.toml'
            if config.exists():
                backup = backup_dir/('config-'+str(time.time_ns())+'.toml')
                shutil.copy2(config, backup)
                backup.chmod(0o600)
            for path, enabled in changes:
                before = next(s['enabled'] for s in skills if not s.get('pluginId')
                              and str(Path(s['path']).resolve()) == path)
                # Include an uncertain response: the write may already have landed.
                attempted.append((path, before))
                client.call('skills/config/write', {'path': path, 'enabled': enabled})
                if enabled: managed.discard(path)
                else: managed.add(path)
                state_path.parent.mkdir(parents=True, exist_ok=True)
                temporary = state_path.with_suffix('.tmp')
                temporary.write_text(json.dumps({'paths': sorted(managed)}, indent=2)+'\n')
                temporary.replace(state_path)
            skills = list_skills(client, root)
            remaining, _ = desired_overrides(root, catalog, skills, managed)
            if remaining: raise RuntimeError('Codex overrides did not take effect after forceReload')
        enabled_count, disabled_count = check_coverage(root, catalog, skills, managed)
        print(f'PASS Codex app-server: enabled={enabled_count} user-disabled={disabled_count} native/shared pairs={len(expected)} unresolved=0')
    except Exception as error:
        failures = []
        for path, before in reversed(attempted):
            try: client.call('skills/config/write', {'path': path, 'enabled': before})
            except Exception: failures.append(path)
        if attempted and not failures:
            try:
                if original_state is None:
                    state_path.unlink(missing_ok=True)
                else:
                    temporary = state_path.with_suffix('.rollback')
                    temporary.write_bytes(original_state)
                    temporary.replace(state_path)
            except OSError: failures.append(str(state_path))
        if failures:
            raise RuntimeError(f'{error}; Codex rollback incomplete for {len(failures)} path(s); inspect james-skills-backups') from error
        raise
    finally:
        if owns_client: client.close()
