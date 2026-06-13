#!/usr/bin/env python3
"""Run deadline reminders and escalations (for cron or n8n Execute Command)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from automation.reminder_engine import run_reminder_check  # noqa: E402


def main() -> int:
    sent = run_reminder_check()
    print(f"Reminder check complete. {len(sent)} notification(s) processed.")
    for record in sent:
        print(
            f"  - {record['notification_type']} → {record['recipient']} "
            f"({record['status']}, {record['channel']})"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
