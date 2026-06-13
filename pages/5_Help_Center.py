"""Help Center — documentation, FAQ, and support."""

from __future__ import annotations

import streamlit as st

from core.config import APP_NAME
from utils.ui.layout import setup_page
from utils.ui.support_pages import (
    help_category_grid,
    help_hero,
    help_support_panel,
    support_page_header,
)

setup_page(f"Help Center — {APP_NAME}", active="help")

support_page_header("Help Center", f"Documentation and answers for {APP_NAME}.")

help_hero()

search = st.text_input(
    "Search Help Center",
    placeholder="Describe what you're looking for…",
    label_visibility="collapsed",
)

if search.strip():
    st.info(f'Showing topics matching "{search.strip()}". Expand an FAQ below for details.')

help_category_grid()

faq_col, side_col = st.columns([2, 1], gap="large")

FAQS = [
    (
        "How does the AI verify volunteer skills?",
        "Our AI engine uses screening scores from application data, skills, interests, and motivation. "
        "When an LLM API key is configured, Bulbul generates richer reasoning; otherwise rule-based "
        "fallbacks assign scores and suggested roles for admin review.",
    ),
    (
        "Can I export volunteer impact data?",
        "Yes. From Settings → Data Management you can export JSON snapshots of candidates, volunteers, "
        "and tasks. CSV summary exports are also available for quick audits.",
    ),
    (
        'What is the "AI Consult" feature?',
        "AI Consult refers to Bulbul's admin assist and task-matching agents. They help draft decisions, "
        "suggest volunteer matches, and summarize candidate fit during onboarding and task assignment.",
    ),
    (
        "How do I approve a volunteer application?",
        "Go to Volunteers → Review candidates. Run AI screening if needed, then Approve or Reject. "
        "Approved candidates are copied into the unified volunteer pool for task matching.",
    ),
]

with faq_col:
    st.markdown("#### Frequently Asked Questions")
    for question, answer in FAQS:
        if search.strip() and search.strip().lower() not in f"{question} {answer}".lower():
            continue
        with st.expander(question, expanded=question.startswith("How does")):
            st.write(answer)

with side_col:
    help_support_panel()

st.markdown("---")
st.markdown(
    "**Still searching?** Join the Community Forum · Attend a Live Webinar · Request On-site Training"
)
