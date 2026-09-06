#!/usr/bin/env python3
"""Public development probes. Deterministic checks are necessary, never sufficient."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import random
import subprocess
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'tests/benchmarks'


def digest(value):
    if not isinstance(value, bytes):
        value = json.dumps(value, ensure_ascii=False, sort_keys=True).encode()
    return hashlib.sha256(value).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())


def validate():
    skills = {s['name']: s for s in load(ROOT / 'catalog.json')['skills'] if s['status'] == 'promoted'}
    manifest = load(DATA / 'manifest.json')
    cases = load(DATA / 'development.json')
    assert set(manifest['skills']) == set(skills), 'catalog coverage differs'
    assert len({c['id'] for c in cases}) == len(cases), 'duplicate case id'
    for name, item in manifest['skills'].items():
        assert item['card'] and name in (ROOT / item['card']).read_text()
        expected = f"plugins/{skills[name]['category']}/skills/{name}/SKILL.md"
        assert item['canonical'] == expected and (ROOT / expected).is_file()
        own = [c for c in cases if c['skill'] == name]
        assert item['state'] == ('public-development' if own else 'card-only')
        if own:
            assert {c['role'] for c in own} == {'rejected-mechanism', 'transfer-mechanism', 'legitimate-countercase'}
    for case in cases:
        assert case['skill'] in skills
        assert all(case[k] for k in ('goal', 'prompt', 'family', 'rubric', 'checks'))
        assert case['split'] == 'public-development'
        assert {'goal_alignment', 'proportionality', 'truth_and_authority'} <= set(case['rubric'])
    return manifest, cases


def check_response(response, checks):
    """Only exact preservation/structured outcomes; no keyword-based semantic grading."""
    results = []
    for rule in checks:
        if rule['type'] == 'literal':
            passed = rule['value'] in response
        elif rule['type'] == 'json_value':
            try:
                parsed = json.loads(response)
                passed = parsed[rule['key']] in rule['allowed']
            except (ValueError, KeyError, TypeError):
                passed = False
        else:
            raise ValueError('unknown check type')
        results.append({'id': rule['id'], 'passed': passed})
    return results


def invoke(command, payload, timeout):
    # Fresh cwd prevents accidental task residue, NOT a security sandbox or sealed holdout.
    # Adapter inherits normal environment for explicitly configured provider authentication.
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix='james-benchmark-') as cwd:
        try:
            result = subprocess.run(command, input=json.dumps(payload, ensure_ascii=False),
                                    text=True, capture_output=True, cwd=cwd, timeout=timeout)
            if result.returncode:
                return {'status': 'adapter_failure', 'exit_code': result.returncode,
                        'elapsed_seconds': time.monotonic() - started}
            obj = json.loads(result.stdout)
            if not isinstance(obj, dict):
                raise ValueError('adapter response must be an object')
            if obj.get('error_category') in {'auth_unavailable'}:
                return {'status': obj['error_category'], 'elapsed_seconds': time.monotonic() - started}
            if not isinstance(obj['response'], str) or not obj['response'].strip():
                raise ValueError('empty response')
            return {'status': 'response_received', 'response': obj['response'],
                    'elapsed_seconds': time.monotonic() - started,
                    'provider_metadata': obj.get('metadata', {})}
        except subprocess.TimeoutExpired:
            return {'status': 'timeout', 'elapsed_seconds': time.monotonic() - started}
        except (ValueError, KeyError, TypeError, OSError):
            return {'status': 'adapter_protocol_failure', 'elapsed_seconds': time.monotonic() - started}


def run(args):
    manifest, cases = validate()
    selected = cases if args.skill == 'pilot' else [c for c in cases if c['skill'] == args.skill]
    if args.case:
        selected = [c for c in selected if c['id'] == args.case]
    if not selected:
        raise ValueError('skill has no executable development probes')
    if args.trials < 1 or args.trials > 3 or args.timeout <= 0:
        raise ValueError('trials must be 1..3 and timeout positive')
    config = load(args.adapter) if args.adapter else None
    if config:
        for field in ('command', 'model', 'host_version', 'effort', 'tools', 'isolation', 'inventory_evidence'):
            if not config.get(field):
                raise ValueError('adapter config missing ' + field)
        if not isinstance(config['command'], list) or not all(isinstance(x, str) for x in config['command']):
            raise ValueError('command must be an argv array, not shell code')
    candidates = load(args.candidates) if args.candidates else {}
    if candidates and set(candidates) != {c['skill'] for c in selected}:
        raise ValueError('candidate map must cover exactly selected skills')
    # Freeze all inputs before the first model call. A and B share task and resource inventory.
    bodies = {name: (ROOT / manifest['skills'][name]['canonical']).read_text()
              for name in {c['skill'] for c in selected}}
    candidate_bodies = {name: Path(path).read_text() for name, path in candidates.items()}
    conditions = ['A', 'B'] + (['C'] if candidates else [])
    schedule = []
    rng = random.Random(args.seed)
    for case in selected:
        for trial in range(args.trials):
            order = conditions.copy()
            rng.shuffle(order)
            schedule.extend((case, trial, condition) for condition in order)
    out = Path(args.output)
    out.mkdir(parents=True, exist_ok=False)
    run_meta = {'schema_version': 1, 'started_utc': datetime.now(timezone.utc).isoformat(),
                'base_revision': subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=ROOT,
                                                capture_output=True, text=True).stdout.strip(), 'track': 'forced-instruction-response-development',
                'split': 'public-development', 'seed': args.seed, 'trials': args.trials,
                'conditions': conditions, 'planned_attempts': len(schedule),
                'suite_hash': digest(selected), 'manifest_hash': digest(manifest),
                'runner_hash': digest(Path(__file__).read_bytes()), 'timeout_seconds': args.timeout,
                'adapter_config_hash': digest(config), 'adapter_metadata':
                {k: v for k, v in (config or {}).items() if k != 'command'},
                'evidence': 'response-only; no routing, persistence, rendering, runtime discovery or efficacy claim'}
    (out / 'run.json').write_text(json.dumps(run_meta, ensure_ascii=False, indent=2))
    counts = {'unscored_dry_run': 0, 'auth_unavailable': 0, 'adapter_failure': 0, 'timeout': 0,
              'adapter_protocol_failure': 0, 'necessary_checks_failed': 0, 'awaiting_human_review': 0}
    with (out / 'attempts.jsonl').open('w') as receipt:
        for case, trial, condition in schedule:
            body = '' if condition == 'A' else bodies[case['skill']] if condition == 'B' else candidate_bodies[case['skill']]
            payload = {'protocol': 1, 'instruction': body, 'task': case['prompt'],
                       'context': case.get('context', ''), 'tools': 'none',
                       'constraint': 'Return response only. No tools, external actions or claimed unperformed execution.'}
            entry = {'case_id': case['id'], 'family': case['family'], 'trial': trial,
                     'condition': condition, 'task_hash': digest(case['prompt']),
                     'case_hash': digest(case), 'instruction_hash': digest(body),
                     'pair_id': f"{case['id']}:{trial}", 'payload_hash': digest(payload)}
            result = invoke(config['command'], payload, args.timeout) if config else {'status': 'unscored_dry_run'}
            if result['status'] == 'response_received':
                result['checks'] = check_response(result['response'], case['checks'])
                result['status'] = ('awaiting_human_review' if all(c['passed'] for c in result['checks'])
                                    else 'necessary_checks_failed')
                result['response_hash'] = digest(result['response'])
            counts[result['status']] += 1
            receipt.write(json.dumps({**entry, **result}, ensure_ascii=False) + '\n')
            receipt.flush()
    summary = {'planned_attempts': len(schedule), 'recorded_attempts': sum(counts.values()),
               'counts': counts, 'performance_score': None,
               'reason': 'Public response probes require human rubric review; no promotion verdict.'}
    (out / 'summary.json').write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--validate', action='store_true')
    parser.add_argument('--skill', default='pilot')
    parser.add_argument('--case', help='One public probe ID for a bounded A/B smoke run')
    parser.add_argument('--adapter', help='JSON config for explicitly selected model subprocess; absent means dry-run')
    parser.add_argument('--candidates', help='JSON map skill name to candidate SKILL.md path; enables C')
    parser.add_argument('--output', help='New output directory outside the repository recommended')
    parser.add_argument('--trials', type=int, default=1)
    parser.add_argument('--timeout', type=float, default=120)
    parser.add_argument('--seed', type=int, default=17)
    args = parser.parse_args()
    try:
        if args.validate:
            manifest, cases = validate()
            print(f"Structural fixture validation: {len(manifest['skills'])} skills, {len(cases)} public probes. No model score.")
        else:
            if not args.output:
                parser.error('--output required')
            run(args)
    except (AssertionError, ValueError, OSError) as exc:
        parser.exit(2, str(exc) + '\n')


if __name__ == '__main__':
    main()
