"""Bulbul by NayePankh Foundation — brand logo assets."""

from __future__ import annotations

import base64
from functools import lru_cache
from pathlib import Path

from core.config import APP_NAME, APP_NAME_SHORT, ORG_NAME

ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets"
LOGO_SVG_PATH = ASSETS_DIR / "logo.svg"
LOGO_MARK_PNG_PATH = ASSETS_DIR / "logo-mark.png"
@lru_cache(maxsize=16)
def logo_svg_markup(size: int = 48, css_class: str = "np-brand-logo") -> str:
    svg = LOGO_SVG_PATH.read_text(encoding="utf-8")
    return (
        f'<img class="{css_class}" src="data:image/svg+xml;base64,'
        f'{base64.b64encode(svg.encode("utf-8")).decode("ascii")}" '
        f'alt="{APP_NAME} logo" width="{size}" height="{size}" />'
    )


def logo_mark_path() -> str:
    return str(LOGO_MARK_PNG_PATH)
