"""Streamlit Cloud entry point — delegates to app.py."""

from __future__ import annotations

import streamlit as st

from core.config import APP_NAME
from utils.ui.logo import logo_mark_path

st.set_page_config(
    page_title=APP_NAME,
    page_icon=logo_mark_path(),
    layout="wide",
    initial_sidebar_state="expanded",
)

from app import main

main()
