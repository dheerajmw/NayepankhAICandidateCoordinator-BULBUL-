"""Shared helper utilities."""

from __future__ import annotations


def parse_comma_list(value: str) -> list[str]:
    if not value or not value.strip():
        return []
    return [part.strip() for part in value.split(",") if part.strip()]


def format_comma_list(items: list[str]) -> str:
    return ", ".join(items)
