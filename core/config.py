"""Central environment configuration for Phase 5."""

from __future__ import annotations

import os

from dotenv import load_dotenv

load_dotenv()


APP_NAME = "Bulbul by NayePankh Foundation"
APP_NAME_SHORT = "Bulbul"
ORG_NAME = "NayePankh Foundation"


def _get(name: str, default: str = "") -> str:
    return os.getenv(name, default).strip()


STORAGE_BACKEND = _get("STORAGE_BACKEND", "auto").lower()
PROMPT_VERSION = _get("PROMPT_VERSION", "v1")
ADMIN_PASSWORD = _get("ADMIN_PASSWORD")
WEBHOOK_TOKEN = _get("WEBHOOK_TOKEN")
WEBHOOK_PORT = int(_get("WEBHOOK_PORT", "8080"))

SUPABASE_URL = _get("SUPABASE_URL")
SUPABASE_KEY = _get("SUPABASE_KEY")

LLM_FALLBACK_ENABLED = _get("LLM_FALLBACK_ENABLED", "true").lower() == "true"
EMAIL_MAX_RETRIES = int(_get("EMAIL_MAX_RETRIES", "3"))
EMAIL_RETRY_DELAY_SECONDS = float(_get("EMAIL_RETRY_DELAY_SECONDS", "1.0"))


def use_supabase() -> bool:
    if STORAGE_BACKEND == "json":
        return False
    if STORAGE_BACKEND == "supabase":
        if not SUPABASE_URL or not SUPABASE_KEY:
            raise RuntimeError("STORAGE_BACKEND=supabase requires SUPABASE_URL and SUPABASE_KEY")
        return True
    return bool(SUPABASE_URL and SUPABASE_KEY)


def storage_label() -> str:
    return "Supabase (PostgreSQL)" if use_supabase() else "JSON (local files)"


def admin_auth_required() -> bool:
    """Password gate only in production when ADMIN_PASSWORD is configured."""
    if not ADMIN_PASSWORD:
        return False
    return app_env().lower() in ("production", "prod")


def app_env() -> str:
    return _get("APP_ENV", "development")
