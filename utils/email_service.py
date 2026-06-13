"""Email delivery via SMTP with dry-run fallback when not configured."""

from __future__ import annotations

import os
import smtplib
from email.mime.text import MIMEText
from typing import Literal

from core.config import APP_NAME, EMAIL_MAX_RETRIES, EMAIL_RETRY_DELAY_SECONDS
from automation.retry import with_retry

DeliveryChannel = Literal["smtp", "log"]


def email_configured() -> bool:
    return bool(os.getenv("SMTP_HOST") and os.getenv("SMTP_FROM"))


def admin_email() -> str:
    return os.getenv("ADMIN_EMAIL", "admin@nayepankh.org").strip()


def send_email(to: str, subject: str, body: str) -> tuple[bool, DeliveryChannel, str | None]:
    """Send an email. Returns (success, channel, error_message)."""
    to = to.strip()
    if not to:
        return False, "log", "Missing recipient email"

    if not email_configured():
        _log_email(to, subject, body)
        return True, "log", None

    try:
        with_retry(
            lambda: _send_smtp(to, subject, body),
            max_retries=EMAIL_MAX_RETRIES,
            delay_seconds=EMAIL_RETRY_DELAY_SECONDS,
            label="SMTP send",
        )
        return True, "smtp", None
    except Exception as exc:  # noqa: BLE001
        return False, "smtp", str(exc)


def _log_email(to: str, subject: str, body: str) -> None:
    print("--- EMAIL (dry-run / SMTP not configured) ---")
    print(f"To: {to}")
    print(f"Subject: {subject}")
    print(body)
    print("--- END EMAIL ---")


def _send_smtp(to: str, subject: str, body: str) -> None:
    host = os.environ["SMTP_HOST"]
    port = int(os.getenv("SMTP_PORT", "587"))
    username = os.getenv("SMTP_USER", "")
    password = os.getenv("SMTP_PASSWORD", "")
    from_addr = os.environ["SMTP_FROM"]
    use_tls = os.getenv("SMTP_USE_TLS", "true").lower() == "true"

    message = MIMEText(body, "plain", "utf-8")
    message["Subject"] = subject
    message["From"] = from_addr
    message["To"] = to

    with smtplib.SMTP(host, port, timeout=30) as server:
        if use_tls:
            server.starttls()
        if username and password:
            server.login(username, password)
        server.sendmail(from_addr, [to], message.as_string())


def render_deadline_reminder(
    volunteer_name: str,
    task_title: str,
    deadline: str,
    days_left: int,
    urgent: bool = False,
) -> tuple[str, str]:
    if urgent:
        subject = f"Urgent: {task_title} due tomorrow — {APP_NAME}"
        body = (
            f"Hi {volunteer_name},\n\n"
            f"This is an urgent reminder that your assigned task \"{task_title}\" "
            f"is due on {deadline} (1 day remaining).\n\n"
            f"Please update your progress or contact the coordinator if you need help.\n\n"
            f"— {APP_NAME}"
        )
    else:
        subject = f"Reminder: {task_title} due in 3 days — {APP_NAME}"
        body = (
            f"Hi {volunteer_name},\n\n"
            f"Friendly reminder: your task \"{task_title}\" is due on {deadline} "
            f"({days_left} days remaining).\n\n"
            f"— {APP_NAME}"
        )
    return subject, body


def render_overdue_escalation(
    task_title: str,
    volunteer_name: str,
    deadline: str,
    days_overdue: int,
) -> tuple[str, str]:
    subject = f"Escalation: overdue task \"{task_title}\" — {APP_NAME}"
    body = (
        f"Admin notice,\n\n"
        f"The task \"{task_title}\" assigned to {volunteer_name} was due on {deadline} "
        f"and is now {days_overdue} day(s) overdue (status not completed).\n\n"
        f"Please follow up with the volunteer.\n\n"
        f"— {APP_NAME}"
    )
    return subject, body


def render_completion_confirmation(
    volunteer_name: str,
    task_title: str,
) -> tuple[str, str]:
    subject = f"Thank you — task completed: {task_title}"
    body = (
        f"Hi {volunteer_name},\n\n"
        f"Thank you for completing \"{task_title}\". Your contribution makes a real "
        f"difference at NayePankh Foundation.\n\n"
        f"— {APP_NAME}"
    )
    return subject, body
