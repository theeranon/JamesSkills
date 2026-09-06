#!/usr/bin/env python3
"""Text-only Claude adapter; validate local flags before any paid model request."""
import hashlib
import json
import subprocess
import sys


def main():
    payload = json.load(sys.stdin)
    help_text = subprocess.run(['claude', '--help'], capture_output=True, text=True, check=True, timeout=20).stdout
    required = ['--safe-mode', '--disable-slash-commands', '--no-session-persistence',
                '--tools', '--system-prompt', '--output-format', '--effort', '--max-budget-usd']
    if any(flag not in help_text for flag in required):
        raise RuntimeError('Installed Claude does not advertise required isolation flags')
    auth = subprocess.run(['claude', 'auth', 'status'], capture_output=True, text=True, timeout=20)
    try:
        auth_state = json.loads(auth.stdout)
    except ValueError:
        auth_state = {}
    if auth_state.get('loggedIn') is False:
        print(json.dumps({'error_category': 'auth_unavailable'}))
        return
    version = subprocess.run(['claude', '--version'], capture_output=True, text=True, check=True, timeout=20).stdout.strip()
    instruction = 'Complete the user task accurately. Return only the requested response. No tools are available.'
    if payload['instruction']:
        instruction += '\n\n' + payload['instruction']
    command = ['claude', '--safe-mode', '-p', '--disable-slash-commands', '--tools', '',
               '--no-session-persistence', '--output-format', 'json', '--effort', 'low',
               '--max-budget-usd', '0.25', '--system-prompt', instruction]
    completed = subprocess.run(command, input=payload['context'] + '\n' + payload['task'],
                               text=True, capture_output=True, timeout=90)
    if completed.returncode:
        raise RuntimeError('Claude request failed; stderr deliberately excluded from receipts')
    result = json.loads(completed.stdout)
    if result.get('is_error') or not result.get('result'):
        raise RuntimeError('Claude returned no successful response')
    metadata = {'host_version': version, 'help_hash': hashlib.sha256(help_text.encode()).hexdigest(),
                'model_usage': result.get('modelUsage', {}), 'usage': result.get('usage', {}),
                'cost_usd': result.get('total_cost_usd'), 'duration_ms': result.get('duration_ms'),
                'num_turns': result.get('num_turns'), 'isolation': 'safe-mode + no tools + skills disabled',
                'limitation': 'Admin policy still applies; forced text injection, not native discovery.'}
    print(json.dumps({'response': result['result'], 'metadata': metadata}))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        # Provider diagnostics can contain account paths or credentials; never echo them.
        print('Claude adapter failed; no provider diagnostics recorded.', file=sys.stderr)
        sys.exit(1)
