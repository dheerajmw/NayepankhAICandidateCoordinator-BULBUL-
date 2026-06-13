"""Safe HTML rendering for custom UI blocks."""

from __future__ import annotations

import streamlit as st


def render_html(content: str) -> None:
    """Render HTML without markdown parsing (avoids code-block escaping)."""
    html_fn = getattr(st, "html", None)
    if callable(html_fn):
        html_fn(content)
        return
    st.markdown(content, unsafe_allow_html=True)
