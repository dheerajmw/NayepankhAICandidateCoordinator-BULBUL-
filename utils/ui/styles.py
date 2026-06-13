"""Stitch design system styles for Streamlit (Coordinated Desktop Intelligence)."""

from __future__ import annotations

from utils.ui.render import render_html

STITCH_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL@24,400,0&display=swap');

:root {
  --np-bg: #faf8ff;
  --np-surface: #ffffff;
  --np-surface-low: #f2f3ff;
  --np-surface-high: #e2e7ff;
  --np-primary: #004ac6;
  --np-primary-container: #2563eb;
  --np-primary-fixed: #dbe1ff;
  --np-secondary-container: #d0e1fb;
  --np-on-surface: #131b2e;
  --np-on-surface-variant: #434655;
  --np-outline-variant: #c3c6d7;
  --np-tertiary: #943700;
  --np-inverse-surface: #283044;
  --np-inverse-on-surface: #eef0ff;
}

html, body, [class*="css"] {
  font-family: 'Geist', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

.stApp {
  background: var(--np-bg) !important;
  color: var(--np-on-surface) !important;
}

.block-container {
  padding-top: 1.5rem !important;
  max-width: 1440px !important;
}

[data-testid="stSidebar"] {
  background: var(--np-surface) !important;
  border-right: 1px solid var(--np-outline-variant) !important;
  min-width: 280px !important;
}

[data-testid="stSidebar"] .block-container {
  padding-top: 2rem !important;
  display: flex;
  flex-direction: column;
  min-height: calc(100vh - 4rem);
}

[data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] {
  margin-top: auto;
}

[data-testid="stMetric"] {
  background: var(--np-surface);
  border: 1px solid var(--np-outline-variant);
  border-radius: 8px;
  padding: 1rem 1.25rem;
  transition: border-color 0.2s ease;
}
[data-testid="stMetric"]:hover {
  border-color: var(--np-primary-container);
}

[data-testid="stMetricLabel"] {
  color: var(--np-on-surface-variant) !important;
  font-size: 0.875rem !important;
  font-weight: 600 !important;
}
[data-testid="stMetricValue"] {
  color: var(--np-on-surface) !important;
  font-size: 1.75rem !important;
  font-weight: 600 !important;
}

.stButton > button {
  border-radius: 8px !important;
  font-weight: 600 !important;
  font-size: 0.875rem !important;
  border: 1px solid transparent !important;
  transition: all 0.2s ease !important;
}
.stButton > button[kind="primary"] {
  background: var(--np-primary-container) !important;
  color: white !important;
}
.stButton > button[kind="secondary"] {
  background: var(--np-surface) !important;
  color: var(--np-on-surface) !important;
  border-color: var(--np-outline-variant) !important;
}

.stTabs [data-baseweb="tab-list"] {
  gap: 8px;
  background: transparent;
}
.stTabs [data-baseweb="tab"] {
  border-radius: 8px !important;
  padding: 0.5rem 1rem !important;
  font-weight: 600 !important;
  background: var(--np-surface-low) !important;
  border: 1px solid var(--np-outline-variant) !important;
}
.stTabs [aria-selected="true"] {
  background: var(--np-secondary-container) !important;
  color: var(--np-primary) !important;
  border-color: var(--np-primary-container) !important;
}

[data-testid="stExpander"] {
  background: var(--np-surface) !important;
  border: 1px solid var(--np-outline-variant) !important;
  border-radius: 8px !important;
}

div[data-testid="stForm"] {
  border: 1px solid var(--np-outline-variant) !important;
  border-radius: 12px !important;
  padding: 1.5rem !important;
  background: var(--np-surface) !important;
  box-shadow: 0 1px 3px rgba(19, 27, 46, 0.04) !important;
}

div[data-testid="stForm"] [data-testid="stFormSubmitButton"] > button {
  width: 100% !important;
  margin-top: 0.5rem !important;
  min-height: 44px !important;
}

/* Input fields — style BaseWeb wrappers only (not parent blocks with hints) */
[data-testid="stTextInput"],
[data-testid="stTextArea"],
[data-testid="stNumberInput"],
[data-testid="stSelectbox"],
[data-testid="stDateInput"],
[data-testid="stMultiSelect"] {
  margin-bottom: 0.35rem !important;
}

[data-testid="stWidgetLabel"] p,
[data-testid="stTextInput"] label p,
[data-testid="stTextArea"] label p,
[data-testid="stSelectbox"] label p {
  font-weight: 600 !important;
  color: var(--np-on-surface) !important;
  font-size: 0.875rem !important;
  margin-bottom: 0.35rem !important;
}

div[data-baseweb="input"],
div[data-baseweb="textarea"],
div[data-baseweb="select"] > div {
  background-color: var(--np-surface-low) !important;
  border: 1.5px solid var(--np-outline-variant) !important;
  border-radius: 8px !important;
  min-height: 44px !important;
  box-sizing: border-box !important;
  transition: border-color 0.15s ease, box-shadow 0.15s ease !important;
}

div[data-baseweb="textarea"] {
  min-height: 96px !important;
}

div[data-baseweb="input"]:focus-within,
div[data-baseweb="textarea"]:focus-within,
div[data-baseweb="select"]:focus-within > div {
  border-color: var(--np-primary-container) !important;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.12) !important;
}

div[data-baseweb="input"] input,
div[data-baseweb="textarea"] textarea {
  background-color: transparent !important;
  border: none !important;
  box-shadow: none !important;
  color: var(--np-on-surface) !important;
  font-size: 0.9375rem !important;
  line-height: 1.45 !important;
  padding: 0.625rem 2rem 0.625rem 0.875rem !important;
  min-height: 40px !important;
  height: auto !important;
}

div[data-baseweb="input"] input::placeholder,
div[data-baseweb="textarea"] textarea::placeholder {
  color: #737686 !important;
  opacity: 1 !important;
}

.stTextInput input,
.stTextArea textarea {
  background-color: transparent !important;
  border: none !important;
  box-shadow: none !important;
  min-height: unset !important;
}

/* Keep Enter-to-submit hint out of the input box */
[data-testid="InputInstructions"] {
  display: block !important;
  margin-top: 0.2rem !important;
  font-size: 0.72rem !important;
  color: #737686 !important;
  line-height: 1.3 !important;
}

div[data-testid="stForm"] [data-testid="InputInstructions"] {
  display: none !important;
}

[data-testid="stHorizontalBlock"] {
  align-items: stretch !important;
  gap: 1.5rem !important;
}

[data-testid="column"] {
  display: flex !important;
  flex-direction: column !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] > div {
  gap: 0.5rem !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label {
  background: var(--np-surface-low) !important;
  border: 1px solid var(--np-outline-variant) !important;
  border-radius: 8px !important;
  padding: 0.65rem 0.85rem !important;
  margin: 0 !important;
  width: 100% !important;
  transition: border-color 0.15s ease, background 0.15s ease !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
  border-color: var(--np-primary-container) !important;
}

[data-testid="stSidebar"] [data-testid="stRadio"] label[data-checked="true"],
[data-testid="stSidebar"] [data-testid="stRadio"] div[aria-checked="true"] label {
  background: var(--np-secondary-container) !important;
  border-color: var(--np-primary-container) !important;
  color: var(--np-primary) !important;
}

hr, [data-testid="stDivider"] {
  margin: 2rem 0 !important;
  border-color: var(--np-outline-variant) !important;
}

[data-testid="stDataFrame"] {
  border: 1px solid var(--np-outline-variant);
  border-radius: 8px;
  overflow: hidden;
}

#MainMenu, footer, header[data-testid="stHeader"] {
  visibility: hidden;
}

.material-symbols-outlined {
  font-family: 'Material Symbols Outlined' !important;
  font-size: 20px;
  vertical-align: middle;
  margin-right: 8px;
}

/* Custom component classes */
.np-brand-block {
  padding: 0 0 1.5rem 0;
  border-bottom: 1px solid var(--np-outline-variant);
  margin-bottom: 1.5rem;
}
.np-brand-row {
  display: flex;
  align-items: center;
  gap: 0.875rem;
}
.np-brand-copy {
  min-width: 0;
}
.np-brand-logo {
  display: block;
  flex-shrink: 0;
  border-radius: 14px;
  box-shadow: 0 8px 20px rgba(0, 74, 198, 0.18);
}
.np-hero-logo-wrap .np-brand-logo {
  box-shadow: 0 10px 24px rgba(0, 0, 0, 0.18);
  margin-bottom: 1rem;
}
.np-brand-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--np-primary);
  margin: 0;
  line-height: 1.2;
}
.np-brand-sub {
  font-size: 0.875rem;
  color: var(--np-on-surface-variant);
  margin: 0.25rem 0 0 0;
}
.np-page-title {
  font-size: 1.75rem;
  font-weight: 600;
  color: var(--np-on-surface);
  margin: 0 0 0.25rem 0;
}
.np-page-sub {
  font-size: 1rem;
  color: var(--np-on-surface-variant);
  margin: 0 0 2rem 0;
}
.np-page-sub-compact {
  margin: 0 0 1.25rem 0;
}
.np-form-header {
  margin-bottom: 1rem;
}
.np-form-header-shell {
  margin: 0;
  padding: 0 0 1rem 0;
  border-bottom: 1px solid var(--np-outline-variant);
}
.np-form-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: var(--np-on-surface);
  margin: 0 0 0.35rem 0;
}
.np-form-sub {
  font-size: 0.875rem;
  color: var(--np-on-surface-variant);
  margin: 0;
  line-height: 1.5;
}
.np-form-wrap {
  display: flex;
  flex-direction: column;
  height: 100%;
}

/* Volunteer registration layout */
.st-key-volunteer_hero_shell,
.st-key-volunteer_form_shell {
  height: 100%;
  min-height: 500px;
}

.st-key-volunteer_form_shell {
  border-radius: 12px !important;
  border-color: var(--np-outline-variant) !important;
  background: var(--np-surface) !important;
  box-shadow: 0 1px 3px rgba(19, 27, 46, 0.05) !important;
  padding: 1.5rem !important;
  box-sizing: border-box !important;
}

.st-key-volunteer_form_shell div[data-testid="stForm"] {
  border: none !important;
  box-shadow: none !important;
  padding: 1rem 0 0 0 !important;
  margin: 0 !important;
  background: transparent !important;
}

.st-key-volunteer_form_shell div[data-testid="stForm"] [data-testid="stVerticalBlock"] {
  gap: 0.75rem !important;
}

.st-key-volunteer_form_shell [data-testid="stTextInput"],
.st-key-volunteer_form_shell [data-testid="stTextArea"] {
  margin-bottom: 0 !important;
}

.st-key-volunteer_form_shell div[data-baseweb="input"],
.st-key-volunteer_form_shell div[data-baseweb="textarea"] {
  background-color: #ffffff !important;
  border: 1.5px solid #b8bfd4 !important;
}

.st-key-volunteer_form_shell div[data-baseweb="input"]:hover,
.st-key-volunteer_form_shell div[data-baseweb="textarea"]:hover {
  border-color: #8b93ab !important;
}

.st-key-volunteer_hero_shell .np-hero-panel {
  min-height: 500px;
  margin: 0;
}

.st-key-volunteer_form_shell [data-testid="stFormSubmitButton"] {
  padding-top: 0.25rem !important;
}

.st-key-volunteer_form_shell [data-testid="stFormSubmitButton"] > button {
  margin-top: 0.75rem !important;
  min-height: 46px !important;
  font-size: 0.9375rem !important;
}
.np-kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}
.np-kpi-card {
  background: var(--np-surface);
  border: 1px solid var(--np-outline-variant);
  border-radius: 8px;
  padding: 1.5rem;
  transition: border-color 0.2s ease;
}
.np-kpi-card:hover { border-color: var(--np-primary-container); }
.np-kpi-label {
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--np-on-surface-variant);
  margin: 0.75rem 0 0.25rem 0;
}
.np-kpi-value {
  font-size: 1.75rem;
  font-weight: 600;
  color: var(--np-on-surface);
  margin: 0;
}
.np-kpi-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  border-radius: 8px;
  background: var(--np-primary-fixed);
  color: var(--np-primary);
}
.np-kpi-badge {
  float: right;
  font-size: 0.75rem;
  font-weight: 600;
  padding: 0.125rem 0.5rem;
  border-radius: 999px;
  background: var(--np-secondary-container);
  color: var(--np-primary);
}
.np-card {
  background: var(--np-surface);
  border: 1px solid var(--np-outline-variant);
  border-radius: 8px;
  padding: 1.25rem;
  margin-bottom: 1rem;
}
.np-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;
  padding-bottom: 0.75rem;
  border-bottom: 1px solid var(--np-outline-variant);
}
.np-card-title {
  font-size: 1.25rem;
  font-weight: 600;
  margin: 0;
}
.np-status {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 999px;
  font-size: 0.6875rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.02em;
}
.np-status-pending { background: #fef3c7; color: #92400e; }
.np-status-in_progress { background: #dbeafe; color: #1e40af; }
.np-status-completed { background: #dcfce7; color: #166534; }
.np-ai-card {
  background: var(--np-surface-low);
  border: 1px solid var(--np-outline-variant);
  border-left: 4px solid var(--np-primary-container);
  border-radius: 8px;
  padding: 1rem;
  margin-bottom: 0.75rem;
}
.np-ai-card-tertiary { border-left-color: var(--np-tertiary); }
.np-hero-panel {
  background: linear-gradient(135deg, #004ac6 0%, #2563eb 100%);
  color: white;
  border-radius: 12px;
  padding: 1.75rem 2rem;
  min-height: 420px;
  height: 100%;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
}
.np-hero-body {
  flex: 1;
}
.np-hero-status {
  margin-top: auto;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.12);
  border-radius: 12px;
}
.np-hero-status-label {
  font-size: 0.75rem;
  opacity: 0.8;
  margin: 0 0 0.25rem 0;
  letter-spacing: 0.04em;
}
.np-hero-status-value {
  font-size: 1rem;
  font-weight: 600;
  margin: 0;
}
.np-hero-panel h2 {
  font-size: 1.75rem;
  font-weight: 700;
  margin: 0 0 1rem 0;
  line-height: 1.2;
}
.np-hero-panel p {
  font-size: 1.05rem;
  opacity: 0.9;
  line-height: 1.6;
}
.np-status-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
}
.np-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.35rem 0.75rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 600;
  background: var(--np-surface);
  border: 1px solid var(--np-outline-variant);
  color: var(--np-on-surface-variant);
}
.np-pill-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #22c55e;
}
.np-system-card {
  background: var(--np-inverse-surface);
  color: var(--np-inverse-on-surface);
  border-radius: 8px;
  padding: 1.25rem;
  margin-top: auto;
}
.np-skill-tag {
  display: inline-block;
  background: var(--np-surface-high);
  color: var(--np-on-surface-variant);
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-size: 0.6875rem;
  font-weight: 700;
  margin: 0.15rem 0.25rem 0.15rem 0;
}
</style>
"""


def inject_theme() -> None:
    render_html(STITCH_CSS)
