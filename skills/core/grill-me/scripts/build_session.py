#!/usr/bin/env python3
import argparse, json
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("--output", required=True)
args = parser.parse_args()
data = json.loads(Path(args.input).read_text(encoding="utf-8"))
if not data.get("questions"):
    raise SystemExit("questions must be a non-empty array")
template = Path(__file__).parent.parent.joinpath("assets/session-template.html").read_text(encoding="utf-8")
payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
Path(args.output).write_text(template.replace("__GRILL_DATA__", payload), encoding="utf-8")
