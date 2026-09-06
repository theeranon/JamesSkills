"""Runner mechanics, never model efficacy or human-judge calibration."""
import importlib.util
import json
import sys
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('benchmark', ROOT / 'scripts/benchmark.py')
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)


class BenchmarkTests(unittest.TestCase):
    def test_coverage_and_countercases(self):
        manifest, cases = b.validate()
        self.assertEqual(len(manifest['skills']), 22)
        self.assertEqual(len(cases), 66)

    def test_wrong_owner_fails_and_json_order_does_not_matter(self):
        check = [{'type': 'json_value', 'id': 'owner', 'key': 'owner', 'allowed': ['make-it-james']}]
        self.assertFalse(b.check_response('{"owner":"zoom-out"}', check)[0]['passed'])
        self.assertTrue(b.check_response('{"reason":"wording", "owner":"make-it-james"}', check)[0]['passed'])
        self.assertTrue(b.check_response('{"owner":"make-it-james", "reason":"style"}', check)[0]['passed'])

    def test_exact_quote_survives_alternative_surrounding_wording(self):
        check = [{'type': 'literal', 'id': 'quote', 'value': 'AI generated มันก็แบบยังไม่ใช่อะ'}]
        self.assertFalse(b.check_response('AI generated ยังไม่เหมาะสม', check)[0]['passed'])
        self.assertTrue(b.check_response('ผู้ร่วมประชุมกล่าวว่า "AI generated มันก็แบบยังไม่ใช่อะ"', check)[0]['passed'])

    def test_equivalent_dates_pass_but_wrong_dates_fail(self):
        for values in [['30 November', 'November 30'], ['9 October', 'October 9']]:
            check = [{'type': 'literal_any', 'id': 'date', 'values': values}]
            for value in values:
                self.assertTrue(b.check_response('Available until ' + value, check)[0]['passed'])
            self.assertFalse(b.check_response('Available until November 29', check)[0]['passed'])
        exact = [{'type': 'literal', 'id': 'quote', 'value': '30 November'}]
        self.assertFalse(b.check_response('November 30', exact)[0]['passed'])

    def test_adapter_deadline_is_reported_as_timeout(self):
        command = [sys.executable, '-c', 'import json; print(json.dumps({"error_category":"timeout"}))']
        self.assertEqual(b.invoke(command, {}, 2)['status'], 'timeout')

    def test_protocol_failures_and_timeout(self):
        for command, status in [([sys.executable, '-c', 'print("not JSON")'], 'adapter_protocol_failure'),
                                ([sys.executable, '-c', 'print("[]")'], 'adapter_protocol_failure'),
                                ([sys.executable, '-c', 'raise SystemExit(3)'], 'adapter_failure'),
                                ([sys.executable, '-c', 'import time; time.sleep(3)'], 'timeout')]:
            self.assertEqual(b.invoke(command, {}, .1)['status'], status)

    def test_dry_run_has_no_score_and_fixed_pairs(self):
        with tempfile.TemporaryDirectory() as temp:
            args = Namespace(skill='pilot', case=None, trials=1, timeout=2, adapter=None,
                             candidates=None, seed=17, output=str(Path(temp) / 'out'))
            b.run(args)
            out = Path(args.output)
            result = b.load(out / 'summary.json')
            self.assertEqual(result['planned_attempts'], 30)
            self.assertEqual(result['counts']['unscored_dry_run'], 30)
            self.assertIsNone(result['performance_score'])
            attempts = [json.loads(line) for line in (out / 'attempts.jsonl').read_text().splitlines()]
            for pair in {a['pair_id'] for a in attempts}:
                members = [a for a in attempts if a['pair_id'] == pair]
                self.assertEqual({a['condition'] for a in members}, {'A', 'B'})
                self.assertEqual(len({a['case_hash'] for a in members}), 1)
                self.assertEqual(len({a['task_hash'] for a in members}), 1)
                self.assertEqual(len({a['instruction_hash'] for a in members}), 2)

    def test_fake_process_failure_is_not_dropped(self):
        with tempfile.TemporaryDirectory() as temp:
            config = Path(temp) / 'adapter.json'
            config.write_text(json.dumps({'command': [sys.executable, '-c', 'raise SystemExit(7)'],
                                         **{key: 'fake-mechanics-only' for key in ['model', 'host_version', 'effort', 'tools', 'isolation', 'inventory_evidence']}}))
            args = Namespace(skill='pilot', case='proactive-habits-1', trials=1, timeout=2,
                             adapter=str(config), candidates=None, seed=17, output=str(Path(temp) / 'out'))
            b.run(args)
            result = b.load(Path(args.output) / 'summary.json')
            self.assertEqual(result['planned_attempts'], 2)
            self.assertEqual(result['recorded_attempts'], 2)
            self.assertEqual(result['counts']['adapter_failure'], 2)

    def test_candidate_condition_and_frozen_hash(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp)
            candidate = folder / 'candidate.md'
            candidate.write_text('Candidate instructions for mechanics test only')
            mapping = folder / 'candidates.json'
            mapping.write_text(json.dumps({'proactive-habits': str(candidate)}))
            args = Namespace(skill='pilot', case='proactive-habits-1', trials=1, timeout=2,
                             adapter=None, candidates=str(mapping), seed=17, output=str(folder / 'out'))
            b.run(args)
            attempts = [json.loads(line) for line in (folder / 'out/attempts.jsonl').read_text().splitlines()]
            self.assertEqual({a['condition'] for a in attempts}, {'A', 'B', 'C'})
            c = next(a for a in attempts if a['condition'] == 'C')
            self.assertEqual(c['instruction_hash'], b.digest(candidate.read_text()))
            self.assertEqual(len({a['pair_id'] for a in attempts}), 1)

    def test_model_response_is_never_automatically_passed(self):
        with tempfile.TemporaryDirectory() as temp:
            config = Path(temp) / 'adapter.json'
            config.write_text(json.dumps({'command': [sys.executable, '-c', 'import json; print(json.dumps({"response":"14:00"}))'],
                                         **{key: 'fake-mechanics-only' for key in ['model', 'host_version', 'effort', 'tools', 'isolation', 'inventory_evidence']}}))
            args = Namespace(skill='pilot', case='proactive-habits-1', trials=1, timeout=2,
                             adapter=str(config), candidates=None, seed=17, output=str(Path(temp) / 'out'))
            b.run(args)
            result = b.load(Path(args.output) / 'summary.json')
            self.assertEqual(result['counts']['awaiting_human_review'], 2)
            self.assertIsNone(result['performance_score'])


if __name__ == '__main__':
    unittest.main()
