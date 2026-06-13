"""Brand logo assets for NayePankh Bulbul."""

from __future__ import annotations

import base64
from functools import lru_cache
from pathlib import Path

ASSETS_DIR = Path(__file__).resolve().parents[2] / "assets"
LOGO_SVG_PATH = ASSETS_DIR / "logo.svg"
LOGO_MARK_PNG_PATH = ASSETS_DIR / "logo-mark.png"


@lru_cache(maxsize=1)
def logo_svg_markup(size: int = 48) -> str:
    svg = LOGO_SVG_PATH.read_text(encoding="utf-8")
    return (
        f'<img class="np-brand-logo" src="data:image/svg+xml;base64,'
        f'{base64.b64encode(svg.encode("utf-8")).decode("ascii")}" '
        f'alt="NayePankh Bulbul logo" width="{size}" height="{size}" />'
    )


def logo_mark_path() -> str:
    return str(LOGO_MARK_PNG_PATH)
