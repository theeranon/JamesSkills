#!/usr/bin/env python3
"""Embed IBM Plex Sans Thai into an HTML file for offline single-file delivery."""

from __future__ import annotations

import argparse
import base64
import os
import re
from pathlib import Path


WEIGHTS = {
    400: "IBMPlexSansThai-Regular.ttf",
    500: "IBMPlexSansThai-Medium.ttf",
    600: "IBMPlexSansThai-SemiBold.ttf",
    700: "IBMPlexSansThai-Bold.ttf",
}
MARKED_BLOCK = re.compile(
    r"\s*<!-- james-fonts:start -->.*?<!-- james-fonts:end -->\s*", re.S
)
REMOTE_FONT_LINK = re.compile(
    r"\s*<link\b[^>]*(?:fonts\.googleapis\.com|fonts\.gstatic\.com)[^>]*>\s*",
    re.I,
)


def candidate_directories(explicit: Path | None) -> list[Path]:
    candidates: list[Path] = []
    if explicit is not None:
        candidates.append(explicit.expanduser())
    candidates.extend(
        [
            Path.home() / "Library" / "Fonts",
            Path.home() / ".local" / "share" / "fonts",
            Path("/usr/local/share/fonts"),
            Path("/usr/share/fonts"),
        ]
    )
    windows_root = os.environ.get("WINDIR")
    if windows_root:
        candidates.append(Path(windows_root) / "Fonts")
    return candidates


def resolve_fonts(explicit: Path | None = None) -> dict[int, Path]:
    missing = set(WEIGHTS)
    resolved: dict[int, Path] = {}
    for directory in candidate_directories(explicit):
        if not directory.is_dir():
            continue
        for weight in tuple(missing):
            direct = directory / WEIGHTS[weight]
            matches = [direct] if direct.is_file() else list(directory.rglob(WEIGHTS[weight]))
            if matches:
                resolved[weight] = matches[0]
                missing.remove(weight)
        if not missing:
            break
    if missing:
        names = ", ".join(WEIGHTS[weight] for weight in sorted(missing))
        raise FileNotFoundError(
            f"IBM Plex Sans Thai font files not found: {names}. "
            "Install the fonts or pass --font-dir."
        )
    return resolved


def font_data(path: Path) -> str:
    payload = path.read_bytes()
    if not payload.startswith((b"\x00\x01\x00\x00", b"OTTO")):
        raise ValueError(f"unsupported or invalid font file: {path}")
    return base64.b64encode(payload).decode("ascii")


def build_font_block(fonts: dict[int, Path]) -> str:
    faces: list[str] = []
    for weight in sorted(fonts):
        faces.append(
            "@font-face {\n"
            "  font-family: 'IBM Plex Sans Thai';\n"
            f"  src: url(data:font/ttf;base64,{font_data(fonts[weight])}) format('truetype');\n"
            f"  font-weight: {weight};\n"
            "  font-style: normal;\n"
            "  font-display: swap;\n"
            "}"
        )
    return (
        "<!-- james-fonts:start -->\n<style>\n"
        + "\n".join(faces)
        + "\n</style>\n<!-- james-fonts:end -->"
    )


def embed_html(html: str, fonts: dict[int, Path]) -> str:
    cleaned = REMOTE_FONT_LINK.sub("\n", html)
    cleaned = MARKED_BLOCK.sub("\n", cleaned)
    block = build_font_block(fonts)
    if re.search(r"</head\s*>", cleaned, re.I):
        return re.sub(r"</head\s*>", block + "\n</head>", cleaned, count=1, flags=re.I)
    raise ValueError("HTML has no closing </head> tag")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Embed four IBM Plex Sans Thai weights into one offline HTML file."
    )
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--font-dir", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.input.expanduser().resolve()
    output = args.output.expanduser().resolve()
    html = source.read_text(encoding="utf-8")
    embedded = embed_html(html, resolve_fonts(args.font_dir))
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(embedded, encoding="utf-8")
    print(f"PASS embedded IBM Plex Sans Thai weights=4 output={output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
