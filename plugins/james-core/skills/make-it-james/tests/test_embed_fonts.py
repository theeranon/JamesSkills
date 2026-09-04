#!/usr/bin/env python3
"""Regression checks for offline IBM Plex Sans Thai embedding."""

from __future__ import annotations

import importlib.util
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).parents[1] / "scripts" / "embed_ibm_plex_thai.py"
SPEC = importlib.util.spec_from_file_location("embed_ibm_plex_thai", SCRIPT)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def main() -> int:
    with tempfile.TemporaryDirectory() as temporary:
        font_dir = Path(temporary)
        for filename in MODULE.WEIGHTS.values():
            (font_dir / filename).write_bytes(b"\x00\x01\x00\x00test-font")

        html = """<!doctype html><html><head>
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Thai" rel="stylesheet">
</head><body>ทดสอบ</body></html>"""
        fonts = MODULE.resolve_fonts(font_dir)
        first = MODULE.embed_html(html, fonts)
        second = MODULE.embed_html(first, fonts)

        assert "fonts.googleapis.com" not in first
        assert "fonts.gstatic.com" not in first
        assert first.count("<!-- james-fonts:start -->") == 1
        assert first.count("data:font/ttf;base64,") == 4
        assert second.count("<!-- james-fonts:start -->") == 1
        assert second.count("data:font/ttf;base64,") == 4

    print("PASS offline IBM Plex Sans Thai embedding and idempotency")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
