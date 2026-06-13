#!/usr/bin/env python3
"""Production webhook server for n8n / external schedulers."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from flask import Flask, jsonify, request  # noqa: E402

from automation.reminder_engine import run_reminder_check  # noqa: E402
from core.config import WEBHOOK_PORT, WEBHOOK_TOKEN  # noqa: E402

app = Flask(__name__)


def _authorized() -> bool:
    if not WEBHOOK_TOKEN:
        return False
    return request.headers.get("X-Webhook-Token") == WEBHOOK_TOKEN


@app.get("/health")
def health():
    return jsonify({"status": "ok", "service": "naye-pankh-bulbul-webhook"})


@app.post("/webhooks/reminders")
def reminders_webhook():
    if not _authorized():
        return jsonify({"error": "unauthorized"}), 401
    sent = run_reminder_check()
    return jsonify({"processed": len(sent), "notifications": sent})


def main() -> None:
    if not WEBHOOK_TOKEN:
        print("Set WEBHOOK_TOKEN in .env before starting the webhook server.")
        sys.exit(1)
    app.run(host="0.0.0.0", port=WEBHOOK_PORT)


if __name__ == "__main__":
    main()
