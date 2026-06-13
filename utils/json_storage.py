"""JSON file read/write utilities for V2 MVP storage."""

from __future__ import annotations

import json
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

DATABASE_DIR = Path(__file__).resolve().parent.parent / "database"

FILES = {
    "candidates": DATABASE_DIR / "candidates.json",
    "volunteers": DATABASE_DIR / "volunteers.json",
    "tasks": DATABASE_DIR / "tasks.json",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def new_id() -> str:
    return str(uuid.uuid4())


def load_list(name: str) -> list[dict[str, Any]]:
    path = FILES[name]
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, list):
        raise ValueError(f"Expected JSON array in {path}")
    return data


def save_list(name: str, records: list[dict[str, Any]]) -> None:
    path = FILES[name]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(records, handle, indent=2, ensure_ascii=False)
        handle.write("\n")


def find_by_id(name: str, record_id: str) -> dict[str, Any] | None:
    return next((r for r in load_list(name) if r.get("id") == record_id), None)


def find_by_email(name: str, email: str) -> dict[str, Any] | None:
    target = email.strip().lower()
    return next(
        (r for r in load_list(name) if r.get("email", "").strip().lower() == target),
        None,
    )
