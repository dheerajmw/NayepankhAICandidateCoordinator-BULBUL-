#!/usr/bin/env python3
"""Migrate local JSON data files into Supabase."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from core.config import SUPABASE_KEY, SUPABASE_URL  # noqa: E402


def _load(path: Path) -> list:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("Set SUPABASE_URL and SUPABASE_KEY in .env before migrating.")
        return 1

    from supabase import create_client

    client = create_client(SUPABASE_URL, SUPABASE_KEY)
    data_dir = ROOT / "data"

    volunteers = _load(data_dir / "volunteers.json")
    tasks = _load(data_dir / "tasks.json")
    match_history = _load(data_dir / "match_history.json")
    notifications = _load(data_dir / "notifications.json")
    reports = _load(data_dir / "reports.json")

    if volunteers:
        client.table("volunteers").upsert(volunteers).execute()
        print(f"Migrated {len(volunteers)} volunteer(s)")
    if tasks:
        client.table("tasks").upsert(tasks).execute()
        print(f"Migrated {len(tasks)} task(s)")
    if match_history:
        client.table("match_history").upsert(match_history).execute()
        print(f"Migrated {len(match_history)} match history record(s)")
    if notifications:
        client.table("notifications").upsert(notifications).execute()
        print(f"Migrated {len(notifications)} notification(s)")
    if reports:
        client.table("reports").upsert(reports).execute()
        print(f"Migrated {len(reports)} report(s)")

    if not any([volunteers, tasks, match_history, notifications, reports]):
        print("No JSON data found to migrate.")
    else:
        print("Migration complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
