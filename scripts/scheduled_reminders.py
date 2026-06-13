#!/usr/bin/env python3
"""Background scheduler for reminder checks (run as a separate process)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from apscheduler.schedulers.blocking import BlockingScheduler  # noqa: E402

from automation.reminder_engine import run_reminder_check  # noqa: E402


def main() -> None:
    hours = 6
    scheduler = BlockingScheduler()
    scheduler.add_job(run_reminder_check, "interval", hours=hours, id="reminder_check")
    print(f"NayePankh Bulbul reminder scheduler started (every {hours}h). Ctrl+C to stop.")
    scheduler.start()


if __name__ == "__main__":
    main()
