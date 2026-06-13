"""Render logo-mark.png from the SVG palette (one-off asset generator)."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "logo-mark.png"


def _lerp(a: int, b: int, t: float) -> int:
    return int(a + (b - a) * t)


def main() -> None:
    size = 128
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    for y in range(size):
        for x in range(size):
            t = (x + y) / (2 * (size - 1))
            r = _lerp(0x00, 0x25, t)
            g = _lerp(0x4A, 0x63, t)
            b = _lerp(0xC6, 0xEB, t)
            dx = x - size / 2
            dy = y - size / 2
            if dx * dx + dy * dy <= (size / 2 - 2) ** 2:
                img.putpixel((x, y), (r, g, b, 255))

    margin = 14
    draw.rounded_rectangle(
        (margin, margin, size - margin, size - margin),
        radius=18,
        fill=(0, 74, 198, 255),
    )

    body = (250, 248, 255, 255)
    wing = (219, 225, 255, 255)
    beak = (37, 99, 235, 255)
    eye = (19, 27, 46, 255)

    draw.ellipse((34, 52, 92, 88), fill=body)
    draw.ellipse((52, 34, 88, 62), fill=body)
    draw.polygon([(58, 30), (62, 16), (66, 24), (72, 18), (74, 28), (68, 34)], fill=wing)
    draw.arc((58, 48, 92, 78), start=200, end=330, fill=wing, width=6)
    draw.polygon([(48, 58), (34, 64), (42, 70)], fill=beak)
    draw.ellipse((70, 44, 78, 52), fill=eye)
    draw.ellipse((72, 45, 74, 47), fill=(255, 255, 255, 255))
    draw.ellipse((98, 28, 106, 36), fill=(255, 181, 150, 240))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.save(OUT, format="PNG")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
