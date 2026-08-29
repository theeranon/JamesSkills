#!/usr/bin/env python3
"""Regression checks for repository-wide portability and secret detection."""

import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts/check_repository_boundary.py"
SPEC = importlib.util.spec_from_file_location("check_repository_boundary", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def labels(text: str) -> set[str]:
    return {label for label, _line in MODULE.scan_text(text)}


def main() -> int:
    assert labels("portable instructions with no sensitive values") == set()
    assert "machine-specific home path" in labels("/" + "Users" + "/example/work")
    assert "possible credential assignment" in labels("api" + "_key = real-looking-value")
    assert "possible credential assignment" in labels("password" + ": real-looking-value")
    assert "private key material" in labels(
        "-----BEGIN " + "PRIVATE KEY-----\nnot-real\n"
    )
    assert MODULE.scan_repository(ROOT) == []
    print("PASS repository boundary clean, credential, private-key and machine-path cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
