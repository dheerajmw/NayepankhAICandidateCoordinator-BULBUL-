"""Reusable LLM engine — structured JSON in/out with OpenAI/Gemini support."""

from __future__ import annotations

from typing import Any

from core import ai_engine


def llm_configured() -> bool:
    return ai_engine.llm_configured()


def complete_json(system_prompt: str, user_prompt: str) -> dict[str, Any]:
    """Send prompt + data context; return parsed JSON dict."""
    return ai_engine.complete_json(system_prompt, user_prompt)


def complete_json_safe(
    system_prompt: str,
    user_prompt: str,
    fallback: dict[str, Any],
) -> dict[str, Any]:
    """Return LLM JSON or fallback when no API key / call fails."""
    if not llm_configured():
        return fallback
    try:
        return complete_json(system_prompt, user_prompt)
    except Exception:
        return fallback
