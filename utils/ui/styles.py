"""Stitch design system styles for Streamlit (Coordinated Desktop Intelligence)."""

from __future__ import annotations

from utils.ui.render import render_html

STITCH_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL@24,400,0&display=swap');

:root {
  --np-bg: #f8f9ff;
  --np-surface: #ffffff;
  --np-surface-low: #eff4ff;
  --np-surface-high: #dce9ff;
  --np-surface-container: #e5eeff;
  --np-primary: #4648d4;
  --np-primary-container: #6063ee;
  --np-primary-fixed: #e1e0ff;
  --np-secondary: #6b38d4;
  --np-secondary-container: #8455ef;
  --np-secondary-fixed: #e9ddff;
  --np-on-surface: #0b1c30;
  --np-on-surface-variant: #464554;
  --np-outline: #767586;
  --np-outline-variant: #c7c4d7;
  --np-tertiary: #00628d;
  --np-tertiary-container: #007cb1;
  --np-inverse-surface: #213145;
  --np-inverse-on-surface: #eaf1ff;
  --np-ai-glow: rgba(132, 85, 239, 0.15);
  --np-glass-bg: rgba(255, 255, 255, 0.72);
  --np-glass-border: rgba(70, 72, 212, 0.12);
  --np-header-height: 0;
  --np-sidebar-width: 280px;
}

html, body, [class*="css"] {
  font-family: 'Inter', 'Geist', -apple-system, BlinkMacSystemFont, sans-serif !important;
}

h1, h2, h3, .np-page-title, .np-brand-title, .np-form-title, .np-kpi-value {
  font-family: 'Geist', sans-serif !important;
  letter-spacing: -0.02em;
}

.np-mono {
  font-family: 'JetBrains Mono', monospace !important;
  letter-spacing: 0.05em;
}

.stApp {
  background: var(--np-bg) !important;
  color: var(--np-on-surface) !important;
  min-height: 100vh !important;
  height: auto !important;
  overflow-x: hidden !important;
  overflow-y: auto !important;
}

html, body {
  height: auto !important;
  overflow-x: hidden !important;
  overflow-y: auto !important;
}

[data-testid="stAppViewContainer"] {
  height: auto !important;
  min-height: 100vh !important;
  max-height: none !important;
  overflow-x: hidden !important;
  overflow-y: visible !important;
  margin-top: 0 !important;
  padding-top: 0 !important;
}

.block-container {
  padding-bottom: 2rem !important;
}

[data-testid="stMain"] {
  flex: 1 1 auto !important;
  width: 100% !important;
  min-width: 0 !important;
  height: auto !important;
  overflow: visible !important;
}

[data-testid="stMain"] > div,
[data-testid="stMain"] [data-testid="stAppViewContainer"] {
  width: 100% !important;
  height: auto !important;
  overflow: visible !important;
}

[data-testid="stMain"] .block-container {
  width: 100% !important;
  max-width: min(1080px, calc(100% - 1.5rem)) !important;
  margin-left: auto !important;
  margin-right: auto !important;
  padding-top: 1.5rem !important;
  padding-bottom: 3rem !important;
  padding-left: clamp(1rem, 2.5vw, 2.5rem) !important;
  padding-right: clamp(1rem, 2.5vw, 2.5rem) !important;
  box-sizing: border-box !important;
  height: auto !important;
  max-height: none !important;
  overflow: visible !important;
}

/* Sidebar collapsed — center content on desktop only (skipped on mobile) */
@media (min-width: 769px) {
  .stApp:has([data-testid="stSidebar"][aria-expanded="false"]) [data-testid="stMain"] .block-container,
  .stApp:has([data-testid="stSidebar"][aria-hidden="true"]) [data-testid="stMain"] .block-container {
    max-width: min(1280px, calc(100vw - 5rem)) !important;
    padding-left: clamp(1.5rem, 5vw, 4rem) !important;
    padding-right: clamp(1.5rem, 5vw, 4rem) !important;
  }

  .stApp:has([data-testid="stSidebar"][aria-expanded="false"]) [data-testid="stHorizontalBlock"],
  .stApp:has([data-testid="stSidebar"][aria-hidden="true"]) [data-testid="stHorizontalBlock"] {
    justify-content: center !important;
  }

  .stApp:has([data-testid="stSidebar"][aria-expanded="false"]) .np-page-title,
  .stApp:has([data-testid="stSidebar"][aria-expanded="false"]) .np-page-sub,
  .stApp:has([data-testid="stSidebar"][aria-expanded="false"]) .np-page-sub-compact,
  .stApp:has([data-testid="stSidebar"][aria-expanded="false"]) .np-status-bar,
  .stApp:has([data-testid="stSidebar"][aria-hidden="true"]) .np-page-title,
  .stApp:has([data-testid="stSidebar"][aria-hidden="true"]) .np-page-sub,
  .stApp:has([data-testid="stSidebar"][aria-hidden="true"]) .np-page-sub-compact,
  .stApp:has([data-testid="stSidebar"][aria-hidden="true"]) .np-status-bar {
    max-width: 1280px;
    margin-left: auto;
    margin-right: auto;
  }
}

[data-testid="stSidebarNav"],
[data-testid="stSidebarNavItems"],
section[data-testid="stSidebarNav"] {
  display: none !important;
  height: 0 !important;
  min-height: 0 !important;
  overflow: hidden !important;
  padding: 0 !important;
  margin: 0 !important;
}

[data-testid="stSidebar"] {
  background: #ffffff !important;
  border-right: 1px solid var(--np-outline-variant) !important;
  box-shadow: 1px 0 0 rgba(19, 27, 46, 0.04);
}

[data-testid="stSidebar"][aria-expanded="true"] {
  min-width: 280px !important;
  width: 280px !important;
}

[data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
  width: 280px !important;
}

[data-testid="stSidebar"] .block-container {
  padding: 1.25rem 1rem 1.5rem !important;
  display: flex !important;
  flex-direction: column !important;
  min-height: 100% !important;
  height: 100% !important;
  max-height: 100vh !important;
  gap: 0.5rem !important;
  width: 100% !important;
  max-width: 280px !important;
  overflow-x: hidden !important;
  overflow-y: auto !important;
  -webkit-overflow-scrolling: touch !important;
  box-sizing: border-box !important;
}

/* Fixed sidebar + scrollable main (non-onboarding pages) */
html:has(.stApp),
html:has(.stApp) body {
  height: 100% !important;
  overflow: hidden !important;
}

.stApp {
  height: 100vh !important;
  max-height: 100vh !important;
  overflow: hidden !important;
}

.stApp [data-testid="stAppViewContainer"] {
  height: 100vh !important;
  max-height: 100vh !important;
  overflow: hidden !important;
  display: flex !important;
  flex-direction: row !important;
  align-items: stretch !important;
}

.stApp:has(.np-sidebar-visible-flag) section[data-testid="stSidebar"],
.stApp:has(.np-sidebar-visible-flag) [data-testid="stSidebar"] {
  position: fixed !important;
  top: 0 !important;
  left: 0 !important;
  width: var(--np-sidebar-width) !important;
  min-width: var(--np-sidebar-width) !important;
  height: 100vh !important;
  max-height: 100vh !important;
  overflow-x: hidden !important;
  overflow-y: auto !important;
  z-index: 998 !important;
  flex-shrink: 0 !important;
  visibility: visible !important;
  opacity: 1 !important;
  transform: none !important;
  pointer-events: auto !important;
  -webkit-overflow-scrolling: touch;
}

.stApp:has(.np-sidebar-hidden-flag) section[data-testid="stSidebar"],
.stApp:has(.np-sidebar-hidden-flag) [data-testid="stSidebar"] {
  width: 0 !important;
  min-width: 0 !important;
  overflow: hidden !important;
  visibility: hidden !important;
  pointer-events: none !important;
  border: none !important;
}

.stApp:has(.np-sidebar-visible-flag) [data-testid="stMain"],
.stApp:has(.np-sidebar-visible-flag) section.main {
  margin-left: var(--np-sidebar-width) !important;
  width: calc(100% - var(--np-sidebar-width)) !important;
  max-width: calc(100% - var(--np-sidebar-width)) !important;
}

.stApp:has(.np-sidebar-hidden-flag) [data-testid="stMain"],
.stApp:has(.np-sidebar-hidden-flag) section.main {
  margin-left: 0 !important;
  width: 100% !important;
  max-width: 100% !important;
}

.stApp [data-testid="stMain"],
.stApp section.main {
  height: 100vh !important;
  max-height: 100vh !important;
  overflow-x: hidden !important;
  overflow-y: auto !important;
  -webkit-overflow-scrolling: touch;
}

.stApp [data-testid="stMain"] > div,
.stApp [data-testid="stMain"] .block-container,
.stApp section.main > div,
.stApp section.main .block-container {
  height: auto !important;
  max-height: none !important;
  overflow: visible !important;
}

.stApp .np-sidebar-shell {
  min-height: calc(100vh - 2.5rem);
}

/* « / » chevron toggle — fixed outside sidebar, always visible */
.stApp [data-testid="stSidebarCollapsedControl"],
.stApp [data-testid="collapsedControl"],
.stApp [data-testid="stSidebarCollapseButton"],
.stApp [data-testid="stSidebarNavCollapseButton"],
.stApp [data-testid="stSidebarHeader"] {
  display: none !important;
  visibility: hidden !important;
  pointer-events: none !important;
}
.st-key-np_sidebar_chevron {
  position: fixed !important;
  top: 0.75rem !important;
  left: 0.75rem !important;
  z-index: 1010 !important;
  width: 2.1rem !important;
  margin: 0 !important;
  padding: 0 !important;
  pointer-events: auto !important;
  visibility: visible !important;
  opacity: 1 !important;
}
.stApp:has(.np-sidebar-visible-flag) .st-key-np_sidebar_chevron {
  left: calc(var(--np-sidebar-width) - 0.65rem) !important;
  transform: translateX(-100%) !important;
}
.st-key-np_sidebar_chevron [data-testid="stVerticalBlock"],
.st-key-np_sidebar_chevron [data-testid="stVerticalBlockBorderWrapper"] {
  gap: 0 !important;
  overflow: visible !important;
}
.st-key-np_sidebar_chevron .stButton {
  margin: 0 !important;
}
.st-key-np_sidebar_chevron .stButton > button {
  width: 2.1rem !important;
  height: 2.1rem !important;
  min-width: 2.1rem !important;
  min-height: 2.1rem !important;
  padding: 0 !important;
  margin: 0 !important;
  border-radius: 8px !important;
  font-size: 1.15rem !important;
  font-weight: 700 !important;
  line-height: 1 !important;
  color: var(--np-primary) !important;
  background: #ffffff !important;
  border: 1px solid var(--np-outline-variant) !important;
  box-shadow: 0 2px 10px rgba(19, 27, 46, 0.12) !important;
}
.st-key-np_sidebar_chevron .stButton > button:hover {
  border-color: var(--np-primary-container) !important;
  box-shadow: 0 4px 14px rgba(70, 72, 212, 0.18) !important;
}

[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
  display: flex !important;
  flex-direction: column !important;
  gap: 0.5rem !important;
  width: 100% !important;
  min-height: auto !important;
  height: auto !important;
  flex: 1 1 auto !important;
  overflow: visible !important;
}

[data-testid="stSidebar"] [data-testid="stVerticalBlockBorderWrapper"] {
  width: 100% !important;
}

[data-testid="stSidebar"] .st-key-sidebar_signout,
[data-testid="stSidebar"] .st-key-sidebar_signout .stButton {
  margin-top: auto !important;
  padding-top: 0.75rem !important;
  border-top: 1px solid var(--np-outline-variant) !important;
  flex-shrink: 0 !important;
}

.st-key-np_sidebar_nav,
.st-key-np_sidebar_cta,
.st-key-np_sidebar_footer,
.np-sidebar-brand,
[data-testid="stSidebar"] [data-testid="stPageLink"],
[data-testid="stSidebar"] [class*="st-key-np_nav_"] {
  flex-shrink: 0 !important;
}
.st-key-np_sidebar_nav {
  flex: 0 0 auto !important;
  width: 100% !important;
  overflow: visible !important;
}

.np-sidebar-shell {
  display: flex;
  flex-direction: column;
  flex: 1;
  min-height: 0;
  margin: -0.25rem 0 0 0;
}
.np-sidebar-brand {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1.25rem 0.5rem 1.75rem 0.5rem;
  margin-bottom: 0.25rem;
}
.np-sidebar-brand-icon {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: transparent;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.np-sidebar-brand-icon .np-brand-logo {
  border-radius: 12px;
  box-shadow: 0 8px 20px rgba(0, 74, 198, 0.22);
}
.np-sidebar-brand-icon .material-symbols-outlined {
  margin-right: 0;
  font-size: 22px;
}
.np-sidebar-brand-title {
  font-family: 'Geist', sans-serif !important;
  font-size: 1.125rem;
  font-weight: 700;
  color: var(--np-primary);
  margin: 0;
  line-height: 1.2;
  letter-spacing: -0.02em;
}
.np-sidebar-brand-sub {
  font-family: 'JetBrains Mono', monospace !important;
  font-size: 0.6875rem;
  color: var(--np-on-surface-variant);
  margin: 0.15rem 0 0 0;
  text-transform: uppercase;
  letter-spacing: 0.12em;
}
.np-sidebar-nav {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  flex: 1;
}
.np-sidebar-link,
.np-sidebar-footer-link {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--np-on-surface-variant) !important;
  text-decoration: none !important;
  transition: background 0.15s ease, color 0.15s ease;
}
.np-sidebar-link:hover,
.np-sidebar-footer-link:hover {
  background: var(--np-surface-low) !important;
  color: var(--np-on-surface) !important;
}
.np-sidebar-link-active {
  background: var(--np-primary-container) !important;
  color: #fffbff !important;
  font-weight: 600;
}
.np-sidebar-link-active:hover {
  background: var(--np-primary-container) !important;
  color: #fffbff !important;
}
.np-sidebar-link-disabled {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--np-outline) !important;
  cursor: not-allowed;
  opacity: 0.72;
}
.np-sidebar-icon {
  font-size: 20px !important;
  margin-right: 0 !important;
  width: 20px;
  flex-shrink: 0;
}
.np-sidebar-cta {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  margin: 1rem 0 0.5rem 0;
  padding: 0.75rem 1rem;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--np-primary) 0%, var(--np-secondary-container) 100%);
  color: #fffbff !important;
  font-size: 0.875rem;
  font-weight: 600;
  text-decoration: none !important;
  box-shadow: 0 8px 24px rgba(70, 72, 212, 0.22);
  transition: opacity 0.15s ease, transform 0.15s ease;
}
.np-sidebar-cta:hover {
  opacity: 0.92;
  transform: translateY(-1px);
  color: #fffbff !important;
}
.np-sidebar-footer {
  margin-top: auto;
  padding-top: 1rem;
  border-top: 1px solid var(--np-outline-variant);
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.np-sidebar-shell a.np-sidebar-link,
.np-sidebar-shell a.np-sidebar-cta,
.np-sidebar-shell a.np-sidebar-footer-link {
  text-decoration: none !important;
}

.st-key-np_sidebar_nav [data-testid="stVerticalBlock"],
.st-key-np_sidebar_nav [data-testid="stVerticalBlockBorderWrapper"],
.st-key-np_sidebar_footer [data-testid="stVerticalBlock"],
.st-key-np_sidebar_footer [data-testid="stVerticalBlockBorderWrapper"] {
  gap: 0.25rem !important;
}
.st-key-np_sidebar_footer {
  margin-top: auto !important;
  padding-top: 1rem !important;
  border-top: 1px solid var(--np-outline-variant) !important;
  flex-shrink: 0 !important;
}
.st-key-np_sidebar_cta {
  margin: 0.5rem 0 0.25rem 0 !important;
  flex-shrink: 0 !important;
}

[data-testid="stSidebar"] a.np-sidebar-link,
[data-testid="stSidebar"] a.np-sidebar-cta,
[data-testid="stSidebar"] a.np-sidebar-footer-link {
  display: flex !important;
  width: 100% !important;
  box-sizing: border-box !important;
}

[data-testid="stSidebar"] [data-testid="stPageLink"] {
  margin: 0 !important;
  width: 100% !important;
}
[data-testid="stSidebar"] [data-testid="stPageLink"] [data-testid="stVerticalBlock"],
[data-testid="stSidebar"] [data-testid="stPageLink"] [data-testid="stVerticalBlockBorderWrapper"] {
  gap: 0 !important;
  width: 100% !important;
}
[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"] {
  display: flex !important;
  align-items: center !important;
  gap: 0.75rem !important;
  padding: 0.5rem 1rem !important;
  border-radius: 8px !important;
  font-size: 0.875rem !important;
  font-weight: 500 !important;
  color: var(--np-on-surface-variant) !important;
  text-decoration: none !important;
  background: transparent !important;
  margin: 0 !important;
  width: 100% !important;
  min-height: 2.5rem !important;
  box-shadow: none !important;
  transition: background 0.15s ease, color 0.15s ease;
}
[data-testid="stSidebar"] [data-testid="stPageLink-NavLink"]:hover {
  background: var(--np-surface-low) !important;
  color: var(--np-on-surface) !important;
}
[data-testid="stSidebar"] [class*="st-key-np_nav_"]:has(.np-nav-active-flag) [data-testid="stPageLink-NavLink"],
[data-testid="stSidebar"] [class*="st-key-np_nav_"]:has(.np-nav-active-flag) [data-testid="stPageLink-NavLink"]:hover {
  background: var(--np-primary-container) !important;
  color: #ffffff !important;
  font-weight: 600 !important;
}
[data-testid="stSidebar"] [class*="st-key-np_nav_"]:has(.np-nav-active-flag) [data-testid="stPageLink-NavLink"] *,
[data-testid="stSidebar"] [class*="st-key-np_nav_"]:has(.np-nav-active-flag) [data-testid="stPageLink-NavLink"] p,
[data-testid="stSidebar"] [class*="st-key-np_nav_"]:has(.np-nav-active-flag) [data-testid="stPageLink-NavLink"] span,
[data-testid="stSidebar"] [class*="st-key-np_nav_"]:has(.np-nav-active-flag) [data-testid="stPageLink-NavLink"] [data-testid="stMarkdownContainer"] {
  color: #ffffff !important;
}
.np-sidebar-link-active,
.np-sidebar-link-active:hover {
  color: #ffffff !important;
}
.np-sidebar-link-active .np-sidebar-icon,
.np-sidebar-link-active .material-symbols-outlined,
.np-sidebar-link-active span {
  color: #ffffff !important;
}
.st-key-np_sidebar_cta [data-testid="stPageLink-NavLink"] {
  justify-content: center !important;
  padding: 0.75rem 1rem !important;
  border-radius: 12px !important;
  background: linear-gradient(135deg, var(--np-primary) 0%, var(--np-secondary-container) 100%) !important;
  color: #fffbff !important;
  font-weight: 600 !important;
  box-shadow: 0 8px 24px rgba(70, 72, 212, 0.22) !important;
}
.st-key-np_sidebar_cta [data-testid="stPageLink-NavLink"]:hover {
  opacity: 0.92;
  transform: translateY(-1px);
  color: #fffbff !important;
  background: linear-gradient(135deg, var(--np-primary) 0%, var(--np-secondary-container) 100%) !important;
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
  background: linear-gradient(135deg, var(--np-primary) 0%, var(--np-secondary-container) 100%) !important;
  color: white !important;
  box-shadow: 0 8px 24px rgba(70, 72, 212, 0.22) !important;
  border: none !important;
}
.stButton > button[kind="primary"]:hover {
  opacity: 0.92 !important;
  transform: translateY(-1px);
}
.stButton > button[kind="secondary"] {
  background: var(--np-surface) !important;
  color: var(--np-on-surface) !important;
  border-color: var(--np-outline-variant) !important;
}

.stTabs [data-baseweb="tab-list"] {
  gap: 8px;
  background: transparent;
  border-bottom: none !important;
}
.stTabs [data-baseweb="tab-border"],
.stTabs [data-baseweb="tab-highlight"] {
  display: none !important;
}
.stTabs [data-baseweb="tab"] {
  border-radius: 8px !important;
  padding: 0.5rem 1rem !important;
  font-weight: 600 !important;
  background: var(--np-surface-low) !important;
  border: 1px solid var(--np-outline-variant) !important;
  border-bottom: 1px solid var(--np-outline-variant) !important;
}
.stTabs [aria-selected="true"] {
  background: var(--np-secondary-container) !important;
  color: #fffbff !important;
  border-color: var(--np-primary-container) !important;
  border-bottom: 1px solid var(--np-primary-container) !important;
  box-shadow: none !important;
}
.stTabs [aria-selected="true"] p,
.stTabs [aria-selected="true"] span,
.stTabs [aria-selected="true"] div {
  color: #fffbff !important;
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
  box-shadow: 0 0 0 3px rgba(96, 99, 238, 0.18) !important;
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
  width: 100% !important;
}

[data-testid="column"] {
  display: flex !important;
  flex-direction: column !important;
  min-width: 0 !important;
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

#MainMenu, footer {
  visibility: hidden !important;
  display: none !important;
}

header[data-testid="stHeader"] {
  display: none !important;
  visibility: hidden !important;
  height: 0 !important;
  min-height: 0 !important;
  max-height: 0 !important;
  padding: 0 !important;
  margin: 0 !important;
  overflow: hidden !important;
  border: none !important;
}

header[data-testid="stHeader"] [data-testid="stToolbar"],
header[data-testid="stHeader"] button[kind="header"],
header[data-testid="stHeader"] [data-testid="stSidebarCollapsedControl"],
header[data-testid="stHeader"] [data-testid="collapsedControl"] {
  display: none !important;
  visibility: hidden !important;
}

[data-testid="stAppDeployButton"] {
  display: none !important;
}

.material-symbols-outlined {
  font-family: 'Material Symbols Outlined' !important;
  font-size: 20px;
  vertical-align: middle;
  margin-right: 8px;
}

/* Custom component classes — Luminous Intelligence */
.np-brand-block {
  padding: 0 0 1.25rem 0;
  border-bottom: 1px solid var(--np-outline-variant);
  margin-bottom: 1.25rem;
}
.np-brand-row {
  display: flex;
  align-items: center;
  gap: 0.875rem;
}
.np-brand-icon {
  width: 40px;
  height: 40px;
  border-radius: 12px;
  background: linear-gradient(135deg, var(--np-primary) 0%, var(--np-secondary-container) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 8px 20px rgba(70, 72, 212, 0.25);
  flex-shrink: 0;
}
.np-brand-copy { min-width: 0; }
.np-brand-logo {
  display: block;
  flex-shrink: 0;
  border-radius: 12px;
  box-shadow: 0 8px 24px rgba(0, 74, 198, 0.2);
}
.np-topbar-logo {
  box-shadow: none;
  border-radius: 8px;
}
.np-onboarding-icon:has(.np-brand-logo),
.np-onboarding-v2-avatar:has(.np-brand-logo) {
  background: transparent;
  box-shadow: none;
  padding: 0;
  overflow: visible;
}
.np-onboarding-v2-avatar .np-brand-logo {
  border-radius: 0.85rem;
}
.np-onboarding-icon .np-brand-logo {
  border-radius: 16px;
}
.np-brand-title {
  font-size: 1.125rem;
  font-weight: 700;
  color: var(--np-primary);
  margin: 0;
  line-height: 1.2;
}
.np-brand-sub {
  font-size: 0.6875rem;
  font-family: 'JetBrains Mono', monospace !important;
  color: var(--np-on-surface-variant);
  margin: 0.2rem 0 0 0;
  text-transform: uppercase;
  letter-spacing: 0.12em;
}
.np-page-title {
  font-size: 2rem;
  font-weight: 600;
  color: var(--np-on-surface);
  margin: 0 0 0.35rem 0;
  line-height: 1.2;
}
.np-page-header {
  margin-bottom: 1.75rem;
}
.np-page-header .np-page-sub,
.np-page-header .np-page-sub-compact {
  margin-bottom: 0;
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
  height: auto !important;
  min-height: 0 !important;
  width: 100%;
}

.st-key-onboarding_page [data-testid="stMain"] .block-container {
  padding-top: 0 !important;
  padding-bottom: 0.75rem !important;
}

.st-key-onboarding_page [data-testid="stVerticalBlock"] {
  gap: 0.25rem !important;
}

.st-key-onboarding_page [data-testid="stHorizontalBlock"] {
  gap: 0.5rem !important;
  align-items: stretch !important;
}

.st-key-volunteer_hero_shell {
  background: #ffffff !important;
  border: 1px solid var(--np-outline-variant) !important;
  border-radius: 16px !important;
  padding: 0 !important;
  overflow: visible !important;
}

.st-key-volunteer_form_shell {
  border: 1px solid var(--np-outline-variant) !important;
  background: #ffffff !important;
  box-shadow: 0 10px 30px rgba(70, 72, 212, 0.08) !important;
  border-radius: 16px !important;
  padding: 0.85rem 1rem 0.8rem 1rem !important;
  box-sizing: border-box !important;
}

.st-key-volunteer_form_shell div[data-testid="stForm"] {
  border: none !important;
  box-shadow: none !important;
  padding: 0.25rem 0 0 0 !important;
  margin: 0 !important;
  background: transparent !important;
}

.st-key-volunteer_form_shell div[data-testid="stForm"] [data-testid="stVerticalBlock"] {
  gap: 0.45rem !important;
}

.st-key-volunteer_form_shell [data-testid="stTextInput"],
.st-key-volunteer_form_shell [data-testid="stTextArea"] {
  margin-bottom: 0 !important;
}

.st-key-volunteer_form_shell div[data-baseweb="input"],
.st-key-volunteer_form_shell div[data-baseweb="textarea"] {
  background-color: #ffffff !important;
  border: 1px solid var(--np-outline-variant) !important;
  border-radius: 10px !important;
  min-height: 38px !important;
}

.st-key-volunteer_form_shell div[data-baseweb="textarea"] {
  min-height: 56px !important;
}

.st-key-volunteer_form_shell div[data-baseweb="input"]:hover,
.st-key-volunteer_form_shell div[data-baseweb="textarea"]:hover {
  border-color: #8b93ab !important;
}

.st-key-volunteer_hero_shell .np-onboarding-hero-compact {
  min-height: 0 !important;
  height: 100% !important;
}

.st-key-volunteer_hero_shell .np-hero-panel {
  min-height: 500px;
  margin: 0;
}

.st-key-volunteer_form_shell [data-testid="stFormSubmitButton"] {
  padding-top: 0.25rem !important;
}

.st-key-volunteer_form_shell [data-testid="stFormSubmitButton"] > button {
  margin-top: 0.35rem !important;
  min-height: 42px !important;
  font-size: 0.92rem !important;
  font-weight: 600 !important;
  border-radius: 10px !important;
  box-shadow: 0 6px 18px rgba(70, 72, 212, 0.18) !important;
}

/* Volunteer onboarding — compact single-page layout */
.np-onboarding-hero-compact {
  min-height: 0 !important;
  height: 100% !important;
  padding: 1.05rem 1.15rem !important;
  display: flex !important;
  flex-direction: column !important;
}
.np-onboarding-body-compact {
  gap: 0.75rem !important;
  justify-content: center !important;
  max-width: none !important;
  margin: 0 !important;
}
.np-onboarding-compact-head {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
}
.np-onboarding-icon-compact {
  width: 40px !important;
  height: 40px !important;
  border-radius: 12px !important;
  flex-shrink: 0;
}
.np-onboarding-compact-copy {
  min-width: 0;
}
.np-onboarding-hero-compact .np-onboarding-title {
  font-size: 1.125rem !important;
  margin: 0 0 0.1rem 0 !important;
  line-height: 1.25 !important;
}
.np-onboarding-hero-compact .np-onboarding-typing {
  font-size: 0.8125rem !important;
  border-right: none !important;
  animation: none !important;
  white-space: normal !important;
  overflow: visible !important;
  width: auto !important;
  margin: 0 !important;
  line-height: 1.35 !important;
  color: var(--np-on-surface-variant) !important;
}
.np-onboarding-hero-compact .np-onboarding-progress {
  padding: 0.6rem 0.75rem !important;
  margin-top: 0 !important;
}
.np-onboarding-hero-compact .np-onboarding-progress-label {
  font-size: 0.75rem !important;
}
.np-onboarding-hero-compact .np-onboarding-progress-pct {
  font-size: 0.75rem !important;
}
.np-onboarding-form-header-compact {
  margin-bottom: 0.55rem !important;
}
.np-onboarding-form-header-compact .np-onboarding-form-title {
  font-size: 1.125rem !important;
  margin-bottom: 0.1rem !important;
}
.np-onboarding-form-header-compact .np-onboarding-form-sub {
  font-size: 0.8125rem !important;
  line-height: 1.35 !important;
}
.np-field-label-compact {
  margin: 0.12rem 0 0.25rem 0 !important;
  font-size: 0.8125rem !important;
}
.st-key-volunteer_form_shell [data-testid="stTextInput"] label p,
.st-key-volunteer_form_shell [data-testid="stTextArea"] label p {
  font-size: 0.8125rem !important;
  margin-bottom: 0.2rem !important;
}
.st-key-volunteer_form_shell [data-testid="stPills"] {
  margin: 0 0 0.25rem 0 !important;
  min-height: 0 !important;
}
.st-key-volunteer_form_shell [data-testid="stPills"] > div {
  gap: 0.35rem !important;
  flex-wrap: wrap !important;
}
.st-key-volunteer_form_shell [data-testid="stPills"] button {
  min-height: 1.625rem !important;
  padding: 0.15rem 0.55rem !important;
  font-size: 0.75rem !important;
  border-radius: 999px !important;
  line-height: 1.2 !important;
}
.st-key-volunteer_form_shell [data-testid="stPills"] button:focus-visible {
  outline: none !important;
  box-shadow: 0 0 0 2px rgba(96, 99, 238, 0.2) !important;
}
.st-key-tag_pills_onboarding_skills [data-testid="stPills"] button[aria-pressed="true"] {
  background: var(--np-primary-fixed) !important;
  color: #2f2ebe !important;
  border: 1px solid rgba(70, 72, 212, 0.2) !important;
}
.st-key-tag_pills_onboarding_skills [data-testid="stPills"] button[aria-pressed="false"] {
  background: #ffffff !important;
  color: var(--np-on-surface-variant) !important;
  border: 1px dashed var(--np-outline-variant) !important;
}
.st-key-tag_pills_onboarding_interests [data-testid="stPills"] button[aria-pressed="true"] {
  background: var(--np-secondary-fixed) !important;
  color: #5516be !important;
  border: 1px solid rgba(107, 56, 212, 0.2) !important;
}
.st-key-tag_pills_onboarding_interests [data-testid="stPills"] button[aria-pressed="false"] {
  background: #ffffff !important;
  color: var(--np-on-surface-variant) !important;
  border: 1px dashed var(--np-outline-variant) !important;
}
.st-key-volunteer_form_shell [data-testid="stHorizontalBlock"]:has([data-testid="stTextInput"]) {
  align-items: end !important;
}

.st-key-volunteer_form_shell [data-testid="stHorizontalBlock"]:has([data-testid="stPills"]) {
  align-items: end !important;
}
.st-key-volunteer_form_shell [data-testid="stHorizontalBlock"]:has([data-testid="stTextInput"]) .stButton > button {
  min-width: 40px !important;
  min-height: 38px !important;
  padding: 0 !important;
  font-size: 1.125rem !important;
  line-height: 1 !important;
  white-space: nowrap !important;
  border-radius: 10px !important;
  border: 1px dashed var(--np-outline-variant) !important;
  background: var(--np-surface-low) !important;
  color: var(--np-on-surface-variant) !important;
  font-weight: 700 !important;
}
.st-key-volunteer_form_shell [data-testid="stHorizontalBlock"]:has([data-testid="stTextInput"]) .stButton > button:hover {
  border-color: var(--np-primary-container) !important;
  color: var(--np-primary) !important;
}
.st-key-availability_row [data-testid="stCheckbox"] {
  background: transparent !important;
  border: none !important;
  border-radius: 0 !important;
  padding: 0 !important;
  margin: 0 !important;
  min-height: 0 !important;
}
.st-key-availability_row [data-testid="stCheckbox"] label {
  width: auto !important;
  padding: 0 !important;
  white-space: nowrap !important;
}
.st-key-availability_row [data-testid="stCheckbox"] label p {
  font-size: 0.8125rem !important;
  font-weight: 600 !important;
  white-space: nowrap !important;
}
.st-key-availability_row [data-testid="stCheckbox"] label[data-baseweb="checkbox"] {
  gap: 0.35rem !important;
}
.np-screening-card-compact {
  padding: 1rem 1.15rem !important;
  margin-top: 0.5rem !important;
}

/* Volunteer onboarding — Stitch layout */
.np-onboarding-hero {
  position: relative;
  display: flex;
  flex-direction: column;
  min-height: 560px;
  height: 100%;
  padding: 2rem 1.75rem;
  background: #ffffff;
  overflow: hidden;
}
.np-onboarding-glow {
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at center, rgba(132, 85, 239, 0.15) 0%, transparent 70%);
  pointer-events: none;
}
.np-onboarding-body {
  position: relative;
  z-index: 1;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  max-width: 28rem;
  margin: 0 auto;
  justify-content: center;
}
.np-onboarding-icon {
  width: 48px;
  height: 48px;
  border-radius: 16px;
  background: linear-gradient(135deg, var(--np-secondary) 0%, var(--np-secondary-container) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fffbff;
  box-shadow: 0 8px 24px rgba(107, 56, 212, 0.25);
}
.np-onboarding-title {
  font-family: 'Geist', sans-serif !important;
  font-size: 1.75rem;
  font-weight: 600;
  color: var(--np-on-surface);
  margin: 0;
  line-height: 1.2;
  letter-spacing: -0.02em;
}
.np-onboarding-typing {
  font-size: 1.05rem;
  color: var(--np-on-surface-variant);
  margin: 0;
  line-height: 1.5;
  border-right: 2px solid var(--np-primary);
  white-space: nowrap;
  overflow: hidden;
  width: fit-content;
  max-width: 100%;
  animation: np-typing 3.5s steps(38, end), np-caret 0.75s step-end infinite;
}
@keyframes np-typing {
  from { width: 0; }
  to { width: 100%; }
}
@keyframes np-caret {
  from, to { border-color: transparent; }
  50% { border-color: var(--np-primary); }
}
.np-onboarding-glass {
  background: rgba(255, 255, 255, 0.72);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(70, 72, 212, 0.1);
  border-radius: 16px;
  border-top-left-radius: 4px;
  padding: 1rem 1.1rem;
  color: var(--np-on-surface-variant);
  font-size: 0.9375rem;
  line-height: 1.55;
}
.np-onboarding-progress {
  background: var(--np-surface-low);
  border: 1px solid rgba(199, 196, 215, 0.45);
  border-radius: 16px;
  padding: 1.25rem 1.35rem;
}
.np-onboarding-progress-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.65rem;
}
.np-onboarding-progress-label {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  font-size: 0.875rem;
  font-weight: 600;
  color: var(--np-primary);
}
.np-onboarding-progress-pct {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  color: var(--np-on-surface-variant);
}
.np-onboarding-progress-track {
  width: 100%;
  height: 8px;
  background: var(--np-surface-variant);
  border-radius: 999px;
  overflow: hidden;
}
.np-onboarding-progress-fill {
  height: 100%;
  background: var(--np-primary);
  border-radius: 999px;
  transition: width 0.5s ease-out;
}
.np-onboarding-progress-note {
  margin: 0.55rem 0 0 0;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.6875rem;
  color: var(--np-outline);
  font-style: italic;
}
.np-onboarding-secure {
  position: relative;
  z-index: 1;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  margin-top: auto;
  padding-top: 1.5rem;
  color: rgba(70, 69, 84, 0.45);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.6875rem;
}
.np-onboarding-secure .material-symbols-outlined {
  font-size: 16px !important;
  margin-right: 0 !important;
}
.np-spin {
  animation: np-spin 1.2s linear infinite;
  font-size: 18px !important;
  margin-right: 0 !important;
}
@keyframes np-spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
.np-onboarding-form-header {
  margin-bottom: 1.5rem;
}
.np-onboarding-form-title {
  font-family: 'Geist', sans-serif !important;
  font-size: 1.5rem;
  font-weight: 500;
  color: var(--np-on-surface);
  margin: 0 0 0.35rem 0;
  line-height: 1.3;
}
.np-onboarding-form-sub {
  font-size: 1rem;
  color: var(--np-on-surface-variant);
  margin: 0;
  line-height: 1.5;
}
.np-field-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--np-on-surface-variant);
  margin: 0.5rem 0 0.35rem 0;
}
.np-chip-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 0.35rem 0 0.75rem 0;
}
.np-chip {
  display: inline-flex;
  align-items: center;
  padding: 0.35rem 0.75rem;
  border-radius: 999px;
  font-size: 0.8125rem;
  font-weight: 600;
  line-height: 1.2;
}
.np-chip-primary {
  background: var(--np-primary-fixed);
  color: #2f2ebe;
  border: 1px solid rgba(70, 72, 212, 0.2);
}
.np-chip-secondary {
  background: var(--np-secondary-fixed);
  color: #5516be;
  border: 1px solid rgba(107, 56, 212, 0.2);
}
.st-key-volunteer_form_shell .stButton > button {
  min-height: 2rem !important;
  padding: 0.3rem 0.55rem !important;
}

.st-key-volunteer_form_shell [data-testid="stCaptionContainer"] {
  margin-top: 0.1rem !important;
}
.st-key-volunteer_form_shell [data-testid="stCaptionContainer"] p {
  font-size: 0.7rem !important;
  color: #8b6e11 !important;
  margin: 0 !important;
}
.np-kpi-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.25rem;
  margin-bottom: 1.5rem;
}
.np-kpi-card {
  background: var(--np-glass-bg);
  backdrop-filter: blur(12px);
  border: 1px solid var(--np-glass-border);
  border-radius: 12px;
  padding: 1.35rem;
  transition: box-shadow 0.2s ease, border-color 0.2s ease;
  position: relative;
  overflow: hidden;
}
.np-kpi-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--np-primary), var(--np-secondary-container));
  opacity: 0;
  transition: opacity 0.2s ease;
}
.np-kpi-card:hover {
  border-color: rgba(96, 99, 238, 0.35);
  box-shadow: 0 8px 30px rgba(70, 72, 212, 0.08);
}
.np-kpi-card:hover::before { opacity: 1; }
.np-kpi-label {
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--np-on-surface-variant);
  margin: 0.75rem 0 0.25rem 0;
}
.np-kpi-value {
  font-size: 1.875rem;
  font-weight: 600;
  color: var(--np-on-surface);
  margin: 0;
}
.np-kpi-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 42px;
  height: 42px;
  border-radius: 10px;
  background: var(--np-primary-fixed);
  color: var(--np-primary);
}
.np-kpi-badge {
  float: right;
  font-size: 0.6875rem;
  font-weight: 600;
  padding: 0.2rem 0.55rem;
  border-radius: 999px;
  background: var(--np-secondary-fixed);
  color: var(--np-secondary);
}
.np-card {
  background: var(--np-glass-bg);
  backdrop-filter: blur(12px);
  border: 1px solid var(--np-glass-border);
  border-radius: 12px;
  padding: 1.25rem;
  margin-bottom: 1rem;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.03);
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
.np-status-pending { background: #e9ddff; color: #5516be; }
.np-status-in_progress { background: #c9e6ff; color: #004c6e; }
.np-status-completed { background: #dcfce7; color: #166534; }
.np-ai-card {
  background: var(--np-glass-bg);
  backdrop-filter: blur(12px);
  border: 1px solid var(--np-glass-border);
  border-radius: 12px;
  padding: 1.1rem 1.25rem;
  margin-bottom: 0.75rem;
  position: relative;
  overflow: hidden;
}
.np-ai-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--np-primary), var(--np-secondary-container));
}
.np-ai-card-tertiary::before {
  background: linear-gradient(90deg, var(--np-tertiary), var(--np-tertiary-container));
}
.np-ai-meta {
  color: var(--np-primary-container);
  font-size: 0.8125rem;
  font-weight: 600;
  font-family: 'JetBrains Mono', monospace;
}
.np-hero-panel {
  background: var(--np-surface-low);
  color: var(--np-on-surface);
  border-radius: 16px;
  padding: 1.75rem 2rem;
  min-height: 420px;
  height: 100%;
  display: flex;
  flex-direction: column;
  box-sizing: border-box;
  border: 1px solid var(--np-outline-variant);
  position: relative;
  overflow: hidden;
}
.np-hero-panel::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 20% 20%, var(--np-ai-glow) 0%, transparent 55%);
  pointer-events: none;
}
.np-hero-body { flex: 1; position: relative; z-index: 1; }
.np-hero-icon {
  width: 48px;
  height: 48px;
  border-radius: 16px;
  background: linear-gradient(135deg, var(--np-secondary) 0%, var(--np-secondary-container) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  box-shadow: 0 8px 24px rgba(107, 56, 212, 0.25);
  margin-bottom: 1rem;
}
.np-hero-glass {
  background: var(--np-glass-bg);
  backdrop-filter: blur(12px);
  border: 1px solid var(--np-glass-border);
  border-radius: 16px;
  border-top-left-radius: 4px;
  padding: 1rem 1.15rem;
  margin: 1rem 0;
  color: var(--np-on-surface-variant);
  font-size: 0.9375rem;
  line-height: 1.55;
}
.np-hero-status {
  margin-top: auto;
  padding: 1rem 1.15rem;
  background: var(--np-surface-container);
  border-radius: 12px;
  border: 1px solid var(--np-outline-variant);
  position: relative;
  z-index: 1;
}
.np-hero-status-label {
  font-size: 0.6875rem;
  font-family: 'JetBrains Mono', monospace;
  color: var(--np-primary);
  margin: 0 0 0.35rem 0;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
.np-hero-status-value {
  font-size: 1rem;
  font-weight: 600;
  margin: 0;
  color: var(--np-on-surface);
}
.np-hero-panel h2 {
  font-size: 1.75rem;
  font-weight: 600;
  margin: 0 0 0.75rem 0;
  line-height: 1.2;
  color: var(--np-on-surface);
}
.np-hero-panel p {
  font-size: 1rem;
  color: var(--np-on-surface-variant);
  line-height: 1.6;
  margin: 0;
}
.np-hero-logo-wrap { margin-bottom: 0.5rem; }
.np-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
  padding: 0.35rem 0.85rem;
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 500;
  background: var(--np-surface);
  border: 1px solid var(--np-outline-variant);
  color: var(--np-on-surface-variant);
}
.np-system-card {
  background: var(--np-inverse-surface);
  color: var(--np-inverse-on-surface);
  border-radius: 12px;
  padding: 1.25rem;
  margin-top: auto;
  border: 1px solid rgba(255,255,255,0.08);
}
.np-screening-card {
  background: var(--np-glass-bg);
  backdrop-filter: blur(12px);
  border: 1px solid var(--np-glass-border);
  border-radius: 16px;
  padding: 1.5rem;
  margin-top: 1rem;
  position: relative;
  overflow: hidden;
}
.np-screening-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--np-primary), var(--np-secondary-container), var(--np-tertiary-container));
}
.np-flow-step {
  background: var(--np-surface-low);
  border: 1px solid var(--np-outline-variant);
  border-radius: 12px;
  padding: 1.25rem;
  height: 100%;
}
.stApp > div {
  height: auto !important;
  max-height: none !important;
  overflow: visible !important;
}

[data-testid="stVerticalBlock"],
[data-testid="stHorizontalBlock"] {
  height: auto !important;
  max-height: none !important;
  overflow: visible !important;
}

.np-flow-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.25rem;
  margin-top: 0.75rem;
  margin-bottom: 2rem;
}
.np-flow-body {
  color: var(--np-on-surface-variant);
  font-size: 0.88rem;
}
.np-flow-step strong {
  color: var(--np-primary);
  display: block;
  margin-bottom: 0.5rem;
}
.np-hero {
  background: var(--np-surface-low);
  border: 1px solid var(--np-outline-variant);
  border-radius: 16px;
  padding: 1.75rem 2rem;
  margin-bottom: 1.5rem;
  position: relative;
  overflow: hidden;
}
.np-hero::after {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(circle at 15% 20%, var(--np-ai-glow) 0%, transparent 55%);
  pointer-events: none;
}
.np-hero-grid {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 1.5rem;
  position: relative;
  z-index: 1;
}
@media (max-width: 768px) {
  .np-hero-grid { grid-template-columns: 1fr; }
}
.np-hero-badge {
  display: inline-block;
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--np-primary);
  background: var(--np-primary-fixed);
  border-radius: 999px;
  padding: 0.25rem 0.65rem;
  margin-bottom: 0.75rem;
}
.np-hero-title {
  font-size: 1.75rem;
  font-weight: 600;
  color: var(--np-on-surface);
  margin: 0 0 0.5rem 0;
  line-height: 1.2;
}
.np-hero-sub {
  font-size: 1rem;
  color: var(--np-on-surface-variant);
  margin: 0;
  line-height: 1.6;
}
.np-hero-ai-panel {
  background: var(--np-glass-bg);
  backdrop-filter: blur(12px);
  border: 1px solid var(--np-glass-border);
  border-radius: 16px;
  border-top-left-radius: 4px;
  padding: 1.15rem 1.25rem;
  align-self: center;
}
.np-hero-ai-label {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--np-primary);
  margin-bottom: 0.35rem;
}
.np-hero-ai-title {
  font-size: 1.125rem;
  font-weight: 600;
  color: var(--np-on-surface);
  margin-bottom: 0.35rem;
}
.np-hero-ai-sub {
  font-size: 0.875rem;
  color: var(--np-on-surface-variant);
  line-height: 1.5;
}
.np-ai-card-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}
.np-ai-card-title {
  font-weight: 600;
  color: var(--np-on-surface);
}
.np-ai-badge {
  font-size: 0.6875rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  padding: 0.2rem 0.55rem;
  border-radius: 999px;
  background: var(--np-secondary-fixed);
  color: var(--np-secondary);
}
.np-ai-score {
  font-family: 'JetBrains Mono', monospace;
  font-size: 1.5rem;
  font-weight: 600;
  color: var(--np-primary);
  margin: 0.25rem 0 0.5rem 0;
}
.np-ai-reason {
  margin: 0 0 0.5rem 0;
  color: var(--np-on-surface-variant);
  font-size: 0.875rem;
  line-height: 1.5;
}
.np-status-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
}
.np-pill-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #22c55e;
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

/* ── Onboarding v2 (Interactive AI) ── */
.stApp:has(.st-key-onboarding_page) {
  background: var(--np-bg) !important;
}
.stApp:has(.st-key-onboarding_page) header[data-testid="stHeader"] {
  display: none !important;
}
.stApp:has(.st-key-onboarding_page) [data-testid="stMain"],
.stApp:has(.st-key-onboarding_page) section.main {
  height: auto !important;
  min-height: 100vh !important;
  max-height: none !important;
  overflow: visible !important;
}
.stApp:has(.st-key-onboarding_page) [data-testid="stMain"] .block-container,
.stApp:has(.st-key-onboarding_page) [data-testid="stMainBlockContainer"] {
  padding-top: 0 !important;
  padding-bottom: 1.5rem !important;
  height: auto !important;
  max-height: none !important;
  overflow: visible !important;
  box-sizing: border-box !important;
}
@media (max-width: 768px) {
  .stApp:has(.st-key-onboarding_page) [data-testid="stMain"] .block-container,
  .stApp:has(.st-key-onboarding_page) [data-testid="stMainBlockContainer"] {
    padding-left: 0.625rem !important;
    padding-right: 0.625rem !important;
    width: 100% !important;
    max-width: 100% !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
  }

  .st-key-onboarding_page,
  .st-key-onboarding_page [data-testid="stVerticalBlock"],
  .st-key-volunteer_hero_shell,
  .st-key-volunteer_form_shell,
  .st-key-volunteer_hero_shell > [data-testid="stVerticalBlock"],
  .st-key-volunteer_form_shell > [data-testid="stVerticalBlock"] {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
    box-sizing: border-box !important;
  }
  .st-key-onboarding_page,
  .st-key-volunteer_form_shell {
    margin-top: 0 !important;
    padding-top: 0 !important;
  }
}
@media (min-width: 769px) {
  .stApp:has(.st-key-onboarding_page) [data-testid="stMain"] .block-container,
  .stApp:has(.st-key-onboarding_page) [data-testid="stMainBlockContainer"] {
    max-width: min(1440px, calc(100vw - 1.5rem)) !important;
  }
}
.st-key-onboarding_page {
  height: auto !important;
  max-height: none !important;
  overflow: visible !important;
  width: 100% !important;
  max-width: 100% !important;
  box-sizing: border-box !important;
}
.st-key-onboarding_page [data-testid="stVerticalBlock"] {
  display: grid !important;
  grid-template-columns: minmax(0, 1fr) !important;
  gap: 1rem !important;
  width: 100% !important;
  align-items: start !important;
  height: auto !important;
  max-height: none !important;
  min-height: 0 !important;
  overflow: visible !important;
}
.st-key-onboarding_page [data-testid="stVerticalBlock"] > *:first-child {
  grid-column: 1 / -1 !important;
}
@media (min-width: 769px) {
  html:not(.np-is-mobile) .st-key-onboarding_page [data-testid="stVerticalBlock"] {
    grid-template-columns: minmax(0, 2fr) minmax(0, 3fr) !important;
    gap: 2rem !important;
  }
}
.st-key-onboarding_page > div > [data-testid="stHorizontalBlock"]:nth-last-child(1) {
  flex: 0 0 auto !important;
  min-height: 0 !important;
  max-height: none !important;
  align-items: flex-start !important;
  overflow: visible !important;
  gap: 2rem !important;
}
.stApp:has(.st-key-onboarding_page) .st-key-onboarding_page [data-testid="stVerticalBlock"] {
  height: auto !important;
  max-height: none !important;
  overflow: visible !important;
}
.stApp:has(.st-key-onboarding_page) .st-key-onboarding_page [data-testid="column"] {
  height: auto !important;
  max-height: none !important;
  overflow: visible !important;
}
/* Onboarding — document scroll (override fixed-viewport app shell below) */
html:has(.st-key-onboarding_page),
html:has(.st-key-onboarding_page) body {
  height: auto !important;
  overflow-x: hidden !important;
  overflow-y: auto !important;
}
html:has(.st-key-onboarding_page) .stApp {
  height: auto !important;
  min-height: 100vh !important;
  max-height: none !important;
  overflow-x: hidden !important;
  overflow-y: auto !important;
}
html:has(.st-key-onboarding_page) .stApp [data-testid="stAppViewContainer"] {
  height: auto !important;
  min-height: 100vh !important;
  max-height: none !important;
  overflow: visible !important;
}

.np-onboarding-topbar {
  position: relative;
  z-index: 999;
  background: rgba(248, 249, 255, 0.88);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(199, 196, 215, 0.35);
  box-shadow: 0 1px 3px rgba(19, 27, 46, 0.04);
  margin: 0;
  padding: 0;
  border-radius: 0;
}
.np-onboarding-topbar-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 3rem;
  max-width: 1440px;
  margin: 0 auto;
  gap: 1rem;
}
.np-topbar-menu-placeholder {
  display: none !important;
}
.np-onboarding-topbar-left {
  display: flex;
  align-items: center;
  gap: 0.65rem;
  min-width: 0;
}
.np-topbar-menu-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.35rem;
  height: 2.25rem;
  padding: 0 0.65rem 0 0.5rem;
  border: 1px solid var(--np-outline-variant);
  border-radius: 10px;
  background: #ffffff;
  color: var(--np-on-surface-variant);
  cursor: pointer;
  transition: border-color 0.15s ease, color 0.15s ease, box-shadow 0.15s ease;
}
.np-topbar-menu-label {
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--np-on-surface-variant);
}
.np-topbar-menu-btn:hover .np-topbar-menu-label {
  color: var(--np-primary);
}
.np-topbar-menu-btn:hover {
  border-color: var(--np-primary-container);
  color: var(--np-primary);
  box-shadow: 0 0 0 3px rgba(96, 99, 238, 0.12);
}
.np-topbar-menu-btn .material-symbols-outlined {
  margin-right: 0;
  font-size: 20px;
}
.np-topbar-logo-icon {
  color: var(--np-primary);
  margin-right: 0 !important;
  font-size: 24px !important;
}
.np-topbar-brand {
  font-family: 'Geist', sans-serif !important;
  font-size: 1.125rem;
  font-weight: 700;
  background: linear-gradient(90deg, var(--np-primary), var(--np-secondary));
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  letter-spacing: -0.02em;
}
.np-onboarding-topbar-nav {
  display: flex;
  align-items: center;
  gap: 2rem;
}
.np-topbar-nav-link {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--np-on-surface-variant);
  cursor: default;
}
.np-topbar-nav-active {
  color: var(--np-primary);
  border-bottom: 2px solid var(--np-primary);
  padding-bottom: 0.2rem;
}
.np-onboarding-topbar-actions {
  display: flex;
  align-items: center;
  gap: 1rem;
}
.np-topbar-action {
  color: var(--np-on-surface-variant);
  cursor: pointer;
  margin-right: 0 !important;
  font-size: 22px !important;
}
.np-topbar-avatar {
  width: 2rem;
  height: 2rem;
  border-radius: 999px;
  background: var(--np-primary-container);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fffbff;
}
.np-topbar-avatar .material-symbols-outlined {
  margin-right: 0;
  font-size: 18px;
}

.np-onboarding-bg-blob {
  position: fixed;
  border-radius: 999px;
  pointer-events: none;
  z-index: 0;
}
.np-onboarding-bg-blob-left {
  top: 25%;
  left: 2.5rem;
  width: 16rem;
  height: 16rem;
  background: rgba(70, 72, 212, 0.05);
  filter: blur(100px);
}
.np-onboarding-bg-blob-right {
  bottom: 25%;
  right: 2.5rem;
  width: 24rem;
  height: 24rem;
  background: rgba(107, 56, 212, 0.05);
  filter: blur(120px);
}

.st-key-volunteer_hero_shell {
  background: transparent !important;
  border: none !important;
  border-radius: 0 !important;
  height: auto !important;
  max-height: none !important;
  overflow: visible !important;
  margin-right: 0 !important;
  width: 100% !important;
  max-width: 100% !important;
  box-sizing: border-box !important;
}
.st-key-volunteer_form_shell {
  border: 1px solid var(--np-outline-variant) !important;
  background: #ffffff !important;
  box-shadow: 0 4px 24px rgba(70, 72, 212, 0.08) !important;
  border-radius: 1.25rem !important;
  padding: 1.1rem 1.35rem 1rem 1.35rem !important;
  height: auto !important;
  max-height: none !important;
  overflow: visible !important;
  box-sizing: border-box !important;
  width: 100% !important;
  max-width: 100% !important;
}

.st-key-volunteer_form_shell > [data-testid="stVerticalBlock"] {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
  height: auto !important;
  max-height: none !important;
  overflow: visible !important;
  box-sizing: border-box;
  gap: 0.35rem !important;
}
.np-onboarding-v2-form-header {
  margin-bottom: 0.55rem;
}
.np-onboarding-v2-form-title {
  font-family: 'Geist', sans-serif !important;
  font-size: 1.35rem;
  font-weight: 600;
  letter-spacing: -0.02em;
  margin: 0 0 0.2rem 0;
  color: var(--np-on-background);
}
.np-onboarding-v2-form-sub {
  font-size: 0.8125rem;
  color: var(--np-on-surface-variant);
  margin: 0;
  line-height: 1.4;
}
.np-v2-field-label {
  font-size: 0.8125rem;
  font-weight: 500;
  color: var(--np-on-surface);
  margin: 0.35rem 0 0.35rem 0;
}
.np-v2-field-sublabel {
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--np-on-surface-variant);
  margin: 0.5rem 0 0.25rem 0;
}
.np-v2-field-hint {
  font-size: 0.72rem;
  color: var(--np-on-surface-variant);
  margin: 0 0 0.5rem 0;
  line-height: 1.35;
}
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_skills,
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_interests {
  margin-top: 0.35rem !important;
  margin-bottom: 0.15rem !important;
}
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_skills [data-testid="stHorizontalBlock"],
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_interests [data-testid="stHorizontalBlock"] {
  align-items: end !important;
  gap: 0.5rem !important;
}
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_skills [data-testid="stTextInput"] label p,
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_interests [data-testid="stTextInput"] label p {
  font-size: 0.72rem !important;
  font-weight: 600 !important;
  color: var(--np-on-surface-variant) !important;
  margin-bottom: 0.2rem !important;
}
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_skills div[data-baseweb="input"],
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_interests div[data-baseweb="input"] {
  background: #ffffff !important;
  border: 1px solid var(--np-outline-variant) !important;
  border-radius: 0.65rem !important;
  min-height: 38px !important;
}
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_skills div[data-baseweb="input"] input,
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_interests div[data-baseweb="input"] input {
  color: var(--np-on-surface) !important;
}
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_skills div[data-baseweb="input"] input::placeholder,
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_interests div[data-baseweb="input"] input::placeholder {
  color: #737686 !important;
  opacity: 1 !important;
}
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_skills .stButton > button,
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_interests .stButton > button {
  min-width: 0 !important;
  min-height: 38px !important;
  margin-top: 1.35rem !important;
  padding: 0 0.75rem !important;
  font-size: 0.8125rem !important;
  line-height: 1 !important;
  white-space: nowrap !important;
  border-radius: 0.65rem !important;
  border: 1px solid var(--np-primary) !important;
  background: rgba(70, 72, 212, 0.08) !important;
  color: var(--np-primary) !important;
  font-weight: 600 !important;
}
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_skills .stButton > button:hover,
.st-key-volunteer_form_shell .st-key-manual_row_onboarding_interests .stButton > button:hover {
  background: rgba(70, 72, 212, 0.14) !important;
  border-color: var(--np-primary) !important;
  color: var(--np-primary) !important;
}
.st-key-volunteer_form_shell .st-key-manual_add_onboarding_skills .stButton > button,
.st-key-volunteer_form_shell .st-key-manual_add_onboarding_interests .stButton > button {
  min-height: 2.35rem !important;
  border-radius: 10px !important;
  font-size: 0.8125rem !important;
  font-weight: 600 !important;
}

.st-key-volunteer_form_shell [data-testid="stPills"] {
  margin-bottom: 0.45rem !important;
}
.st-key-volunteer_form_shell [data-testid="stPills"] > div {
  gap: 0.35rem !important;
  flex-wrap: wrap !important;
}
.st-key-volunteer_form_shell [data-testid="stPills"] button {
  min-height: 1.85rem !important;
  padding: 0.2rem 0.65rem !important;
  border-radius: 999px !important;
  font-size: 0.75rem !important;
  font-weight: 500 !important;
  border: 1px solid var(--np-outline-variant) !important;
  background: #ffffff !important;
  color: var(--np-on-surface-variant) !important;
}
.np-onboarding-v2-hero {
  background: rgba(255, 255, 255, 0.72);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.35);
  border-radius: 1.25rem;
  box-shadow: 0 0 20px rgba(70, 72, 212, 0.12);
  padding: 1.15rem 1.25rem;
  min-height: 280px;
  height: auto;
  max-height: none;
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  box-sizing: border-box;
  overflow: visible;
}
.np-onboarding-v2-hero-head {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}
.np-onboarding-v2-avatar {
  width: 3.25rem;
  height: 3.25rem;
  border-radius: 0.85rem;
  background: linear-gradient(135deg, var(--np-primary), var(--np-secondary));
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fffbff;
  box-shadow: 0 8px 24px rgba(70, 72, 212, 0.25);
  position: relative;
}
.np-onboarding-v2-status-dot {
  position: absolute;
  bottom: 0;
  right: 0;
  width: 0.85rem;
  height: 0.85rem;
  background: #22c55e;
  border: 2px solid #ffffff;
  border-radius: 999px;
  animation: np-pulse 1.5s ease-in-out infinite;
}
@keyframes np-pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.55; }
}
.np-onboarding-v2-name {
  font-family: 'Geist', sans-serif !important;
  font-size: 1.05rem;
  font-weight: 500;
  margin: 0;
  color: var(--np-on-background);
}
.np-onboarding-v2-role {
  font-size: 0.8125rem;
  font-weight: 500;
  color: var(--np-primary);
  margin: 0.1rem 0 0 0;
}
.np-onboarding-v2-chat {
  display: flex;
  flex-direction: column;
  gap: 0.65rem;
  flex: 1;
  min-height: 0;
  overflow: visible;
}
.np-onboarding-v2-bubble {
  background: rgba(70, 72, 212, 0.05);
  border: 1px solid rgba(70, 72, 212, 0.1);
  border-radius: 0.85rem;
  border-top-left-radius: 0.25rem;
  padding: 0.75rem 0.85rem;
}
.np-onboarding-v2-bubble p {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.45;
  color: var(--np-on-surface);
}
.np-onboarding-v2-typing-row {
  display: flex;
  align-items: flex-start;
  gap: 0.65rem;
}
.np-onboarding-v2-dots {
  display: flex;
  gap: 0.25rem;
  margin-top: 0.35rem;
}
.np-onboarding-v2-dots span {
  width: 0.35rem;
  height: 0.35rem;
  border-radius: 999px;
  background: rgba(70, 72, 212, 0.4);
  animation: np-bounce 1.2s ease-in-out infinite;
}
.np-onboarding-v2-dots span:nth-child(2) { animation-delay: 0.15s; }
.np-onboarding-v2-dots span:nth-child(3) { animation-delay: 0.3s; }
@keyframes np-bounce {
  0%, 100% { transform: translateY(0); opacity: 0.5; }
  50% { transform: translateY(-3px); opacity: 1; }
}
.np-onboarding-v2-typing {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--np-on-surface-variant);
  border-right: 2px solid var(--np-primary);
  padding-right: 0.15rem;
  animation: np-caret 0.75s step-end infinite;
}
.np-onboarding-v2-progress-wrap { margin-top: auto; }
.np-onboarding-v2-progress-head {
  display: flex;
  justify-content: space-between;
  align-items: flex-end;
  margin-bottom: 0.65rem;
}
.np-onboarding-v2-progress-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--np-on-surface-variant);
}
.np-onboarding-v2-progress-pct {
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.75rem;
  font-weight: 700;
  color: var(--np-primary);
}
.np-onboarding-v2-progress-track {
  width: 100%;
  height: 0.5rem;
  background: var(--np-surface-container);
  border-radius: 999px;
  overflow: hidden;
}
.np-onboarding-v2-progress-fill {
  height: 100%;
  background: var(--np-primary);
  border-radius: 999px;
  position: relative;
  transition: width 0.5s ease;
}
.np-onboarding-v2-progress-fill--active {
  transition: width 1.5s ease;
}
.np-onboarding-v2-shimmer {
  position: absolute;
  inset: 0;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.45), transparent);
  background-size: 200% 100%;
  animation: np-shimmer 2s infinite;
}
@keyframes np-shimmer {
  0% { background-position: -200% 0; }
  100% { background-position: 200% 0; }
}

.st-key-volunteer_form_shell [data-testid="stPills"] button[aria-pressed="true"] {
  border-color: var(--np-primary) !important;
  background: rgba(70, 72, 212, 0.05) !important;
  color: var(--np-primary) !important;
}

.st-key-volunteer_form_shell div[data-testid="stForm"] {
  padding: 0 !important;
  margin-top: 0.15rem !important;
}
.st-key-volunteer_form_shell div[data-testid="stForm"] [data-testid="stVerticalBlock"] {
  gap: 0.55rem !important;
}
.st-key-volunteer_form_shell div[data-baseweb="input"],
.st-key-volunteer_form_shell div[data-baseweb="textarea"] {
  background: var(--np-surface-bright, #f8f9ff) !important;
  border: 1px solid var(--np-outline-variant) !important;
  border-radius: 0.65rem !important;
  min-height: 38px !important;
}
.st-key-volunteer_form_shell div[data-baseweb="textarea"] {
  min-height: 56px !important;
}
.st-key-volunteer_form_shell div[data-baseweb="input"]:focus-within,
.st-key-volunteer_form_shell div[data-baseweb="textarea"]:focus-within {
  border-color: var(--np-primary) !important;
  box-shadow: 0 0 0 3px rgba(70, 72, 212, 0.12) !important;
}
.st-key-volunteer_form_shell [data-testid="stTextInput"] label p,
.st-key-volunteer_form_shell [data-testid="stTextArea"] label p,
.st-key-volunteer_form_shell [data-testid="stSlider"] label p {
  font-size: 0.8125rem !important;
  margin-bottom: 0.15rem !important;
}

.st-key-availability_cards,
.st-key-availability_cards > div[data-testid="stVerticalBlock"] {
  display: flex !important;
  flex-direction: row !important;
  flex-wrap: nowrap !important;
  align-items: stretch !important;
  gap: 0 !important;
  width: 100% !important;
  margin: 0.15rem 0 0.35rem 0 !important;
  padding: 0 !important;
}
.st-key-availability_cards > *,
.st-key-availability_cards [data-testid="stVerticalBlock"] > *,
.st-key-availability_cards [data-testid="column"] {
  flex: 1 1 0 !important;
  min-width: 0 !important;
  padding: 0 !important;
  margin: 0 !important;
  gap: 0 !important;
}
.st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stHorizontalBlock"] {
  gap: 0 !important;
  width: 100% !important;
}
.st-key-availability_cards [data-testid="stCheckbox"] {
  width: 100% !important;
  min-width: 0 !important;
  background: transparent !important;
  border: none !important;
  border-radius: 0 !important;
  padding: 0 !important;
  margin: 0 !important;
  box-sizing: border-box !important;
}
.st-key-availability_cards [data-testid="stCheckbox"] label[data-baseweb="checkbox"] {
  width: 100% !important;
  min-height: 2.5rem !important;
  box-sizing: border-box !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 0 !important;
  margin: 0 !important;
  padding: 0.5rem 0.35rem !important;
  background: #ffffff !important;
  border: 1px solid var(--np-outline-variant) !important;
  border-radius: 0 !important;
  cursor: pointer !important;
  position: relative !important;
  transition: border-color 0.15s ease, background 0.15s ease, box-shadow 0.15s ease !important;
}
.st-key-availability_cards > *:first-child [data-testid="stCheckbox"] label[data-baseweb="checkbox"],
.st-key-availability_cards [data-testid="stVerticalBlock"] > *:first-child [data-testid="stCheckbox"] label[data-baseweb="checkbox"] {
  border-top-left-radius: 0.75rem !important;
  border-bottom-left-radius: 0.75rem !important;
}
.st-key-availability_cards > *:not(:first-child) [data-testid="stCheckbox"] label[data-baseweb="checkbox"],
.st-key-availability_cards [data-testid="stVerticalBlock"] > *:not(:first-child) [data-testid="stCheckbox"] label[data-baseweb="checkbox"] {
  border-left: none !important;
  margin-left: -1px !important;
}
.st-key-availability_cards > *:last-child [data-testid="stCheckbox"] label[data-baseweb="checkbox"],
.st-key-availability_cards [data-testid="stVerticalBlock"] > *:last-child [data-testid="stCheckbox"] label[data-baseweb="checkbox"] {
  border-top-right-radius: 0.75rem !important;
  border-bottom-right-radius: 0.75rem !important;
}
.st-key-availability_cards [data-testid="stCheckbox"]:has(input:checked) label[data-baseweb="checkbox"] {
  border-color: var(--np-primary) !important;
  background: rgba(96, 99, 238, 0.08) !important;
  z-index: 1 !important;
  box-shadow: inset 0 0 0 1px var(--np-primary) !important;
}
.st-key-availability_cards [data-testid="stCheckbox"] label[data-baseweb="checkbox"] > span:first-child,
.st-key-availability_cards [data-testid="stCheckbox"] label[data-baseweb="checkbox"] > div[data-testid="stCheckboxVisualization"],
.st-key-availability_cards [data-testid="stCheckbox"] input[type="checkbox"] {
  position: absolute !important;
  opacity: 0 !important;
  width: 0 !important;
  height: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  overflow: hidden !important;
  pointer-events: none !important;
}
.st-key-availability_cards [data-testid="stCheckbox"] label p {
  font-size: 0.8125rem !important;
  font-weight: 600 !important;
  color: var(--np-on-surface-variant) !important;
  margin: 0 !important;
  text-align: center !important;
  white-space: nowrap !important;
}
.st-key-availability_cards [data-testid="stCheckbox"]:has(input:checked) label p {
  color: var(--np-primary) !important;
}

.np-v2-level-badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-top: 1.45rem;
  padding: 0.2rem 0.5rem;
  border-radius: 0.35rem;
  background: rgba(70, 72, 212, 0.1);
  color: var(--np-primary);
  font-family: 'JetBrains Mono', monospace;
  font-size: 0.625rem;
  font-weight: 600;
  text-transform: capitalize;
  white-space: nowrap;
}

.st-key-volunteer_form_shell [data-testid="stSlider"] {
  padding-top: 0 !important;
}

.np-v2-form-footer {
  padding-top: 0.75rem;
  border-top: 1px solid rgba(199, 196, 215, 0.35);
  margin-top: 0.35rem !important;
  margin-bottom: 0.5rem !important;
  width: 100%;
  box-sizing: border-box;
  display: flex;
  align-items: flex-start;
}
.np-v2-form-footer-copy {
  display: flex;
  flex-direction: column;
  gap: 0.1rem;
}
.np-v2-form-footer-sub {
  font-size: 0.75rem;
  color: var(--np-on-surface-variant);
}
.np-v2-form-footer-highlight {
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--np-secondary);
}

.st-key-volunteer_form_shell [data-testid="stFormSubmitButton"] {
  display: flex !important;
  justify-content: stretch !important;
  align-items: stretch !important;
  padding-top: 0 !important;
  margin-top: 0 !important;
  width: 100% !important;
}
.st-key-volunteer_form_shell [data-testid="stFormSubmitButton"] > button {
  width: 100% !important;
  min-width: 0 !important;
  min-height: 2.75rem !important;
  padding: 0 1.25rem !important;
  border-radius: 999px !important;
  font-family: 'Geist', sans-serif !important;
  font-size: 0.875rem !important;
  font-weight: 600 !important;
  background: linear-gradient(90deg, var(--np-primary), var(--np-secondary)) !important;
  box-shadow: 0 6px 18px rgba(70, 72, 212, 0.22) !important;
  border: none !important;
}

.np-onboarding-v2-success {
  margin-top: 1rem;
  padding: 1.25rem 1.5rem;
  border-radius: 1rem;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(199, 196, 215, 0.35);
}
.np-v2-success-meta {
  margin: 0.65rem 0 0 0;
  font-size: 0.85rem;
  color: var(--np-on-surface-variant);
}

/* Settings, Help Center, Account */
.np-support-header { margin-bottom: 1.75rem; }
.np-support-title {
  font-family: 'Geist', sans-serif;
  font-size: 2rem;
  font-weight: 700;
  color: var(--np-on-surface);
  margin: 0 0 0.35rem 0;
  letter-spacing: -0.02em;
}
.np-support-sub {
  margin: 0;
  font-size: 0.95rem;
  color: var(--np-on-surface-variant);
  max-width: 42rem;
  line-height: 1.5;
}
.np-glass-card {
  background: rgba(255, 255, 255, 0.72);
  border: 1px solid rgba(199, 196, 215, 0.45);
  border-radius: 1rem;
  padding: 1.25rem 1.35rem;
  margin-bottom: 1rem;
  backdrop-filter: blur(12px);
  box-shadow: 0 4px 24px rgba(11, 28, 48, 0.04);
}
.np-section-card-head {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  margin-bottom: 0.85rem;
}
.np-section-card-title {
  font-family: 'Geist', sans-serif;
  font-size: 1.05rem;
  font-weight: 600;
  margin: 0;
  color: var(--np-on-surface);
}
.np-section-icon {
  width: 2.25rem;
  height: 2.25rem;
  border-radius: 0.65rem;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.np-section-icon .material-symbols-outlined { font-size: 1.15rem !important; }
.np-section-icon-primary {
  background: rgba(96, 99, 238, 0.12);
  color: var(--np-primary);
}
.np-section-icon-secondary {
  background: rgba(107, 56, 212, 0.12);
  color: var(--np-secondary);
}
.np-ai-mode-card {
  background: rgba(255, 255, 255, 0.72);
  border: 1px solid rgba(199, 196, 215, 0.45);
  border-radius: 1rem;
  padding: 1.25rem 1.35rem;
  margin-top: 0.5rem;
}

/* Locked settings section overlay */
.st-key-org_config_locked {
  position: relative !important;
  border: 1px solid rgba(199, 196, 215, 0.45) !important;
  border-radius: 1rem !important;
  background: rgba(255, 255, 255, 0.55) !important;
  padding: 1.25rem 1.35rem 1.35rem 1.35rem !important;
  margin-bottom: 1rem !important;
  overflow: hidden !important;
  box-shadow: 0 4px 24px rgba(11, 28, 48, 0.04) !important;
}
.st-key-org_config_locked > div[data-testid="stVerticalBlock"] {
  position: relative !important;
  min-height: 22rem !important;
}
.st-key-org_config_locked > div[data-testid="stVerticalBlock"] > div:not(:has(.np-locked-overlay)) {
  filter: blur(7px) saturate(0.85) !important;
  opacity: 0.42 !important;
  pointer-events: none !important;
  user-select: none !important;
}
.st-key-org_config_locked div[data-testid="stForm"],
.st-key-org_config_locked .np-section-card-head {
  filter: blur(7px) saturate(0.85) !important;
  opacity: 0.42 !important;
  pointer-events: none !important;
}
.np-locked-overlay {
  position: absolute !important;
  inset: 0 !important;
  z-index: 20 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  padding: 1.5rem !important;
  background: linear-gradient(
    145deg,
    rgba(248, 249, 255, 0.35) 0%,
    rgba(225, 224, 255, 0.45) 50%,
    rgba(248, 249, 255, 0.3) 100%
  ) !important;
  backdrop-filter: blur(10px) saturate(1.15) !important;
  -webkit-backdrop-filter: blur(10px) saturate(1.15) !important;
  border-radius: 1rem !important;
  pointer-events: all !important;
}
.np-locked-overlay-card {
  text-align: center;
  max-width: 19rem;
  padding: 1.65rem 1.45rem 1.5rem 1.45rem;
  border-radius: 1.15rem;
  background: rgba(255, 255, 255, 0.88);
  border: 1px solid rgba(96, 99, 238, 0.2);
  box-shadow:
    0 16px 48px rgba(70, 72, 212, 0.16),
    inset 0 1px 0 rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
}
.np-locked-icon-ring {
  width: 3.65rem;
  height: 3.65rem;
  margin: 0 auto 0.9rem;
  border-radius: 999px;
  background: linear-gradient(135deg, var(--np-primary) 0%, var(--np-secondary) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fffbff;
  box-shadow: 0 10px 28px rgba(70, 72, 212, 0.35);
}
.np-locked-icon-ring .material-symbols-outlined {
  font-size: 1.65rem !important;
  margin-right: 0 !important;
}
.np-locked-badge {
  display: inline-block;
  font-size: 0.625rem;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 0.22rem 0.6rem;
  border-radius: 999px;
  background: rgba(96, 99, 238, 0.12);
  color: var(--np-primary);
  margin-bottom: 0.7rem;
}
.np-locked-title {
  font-family: 'Geist', sans-serif;
  font-size: 1.05rem;
  font-weight: 600;
  margin: 0 0 0.45rem 0;
  color: var(--np-on-surface);
}
.np-locked-message {
  margin: 0;
  font-size: 0.8125rem;
  line-height: 1.5;
  color: var(--np-on-surface-variant);
}

.np-system-health-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin-top: 2rem;
  padding: 1rem 1.25rem;
  border-radius: 1rem;
  background: linear-gradient(90deg, rgba(96, 99, 238, 0.08), rgba(132, 85, 239, 0.06));
  border: 1px solid rgba(199, 196, 215, 0.35);
}
.np-system-health-left { display: flex; align-items: center; gap: 0.85rem; }
.np-system-health-icon { color: var(--np-primary); font-size: 1.5rem !important; }
.np-system-health-title {
  margin: 0;
  font-size: 0.9rem;
  font-weight: 600;
  color: var(--np-on-surface);
}
.np-system-health-sub {
  margin: 0.15rem 0 0 0;
  font-size: 0.78rem;
  color: var(--np-on-surface-variant);
}
.np-system-health-link {
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--np-primary);
  white-space: nowrap;
}
.np-help-hero {
  position: relative;
  border-radius: 1.25rem;
  padding: 2.5rem 2rem;
  margin: 1rem 0 1.5rem 0;
  background: linear-gradient(135deg, rgba(96, 99, 238, 0.12) 0%, rgba(132, 85, 239, 0.08) 50%, rgba(0, 98, 141, 0.06) 100%);
  border: 1px solid rgba(199, 196, 215, 0.35);
  overflow: hidden;
}
.np-help-hero-glow {
  position: absolute;
  top: -40%;
  right: -10%;
  width: 280px;
  height: 280px;
  border-radius: 50%;
  background: radial-gradient(circle, rgba(96, 99, 238, 0.18), transparent 70%);
  pointer-events: none;
}
.np-help-hero-inner { position: relative; z-index: 1; max-width: 36rem; }
.np-help-hero-title {
  font-family: 'Geist', sans-serif;
  font-size: 1.75rem;
  font-weight: 700;
  margin: 0 0 0.5rem 0;
  color: var(--np-on-surface);
}
.np-help-hero-sub {
  margin: 0;
  font-size: 0.95rem;
  color: var(--np-on-surface-variant);
  line-height: 1.5;
}
.np-help-bento {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
  margin-bottom: 1.5rem;
}
.np-help-card h3 {
  font-family: 'Geist', sans-serif;
  font-size: 1rem;
  font-weight: 600;
  margin: 0.65rem 0 0.35rem 0;
}
.np-help-card p {
  margin: 0 0 0.65rem 0;
  font-size: 0.82rem;
  color: var(--np-on-surface-variant);
  line-height: 1.45;
}
.np-help-card ul {
  margin: 0;
  padding: 0;
  list-style: none;
  font-size: 0.78rem;
  color: var(--np-primary);
}
.np-help-card li { padding: 0.2rem 0; }
.np-help-card-icon {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
.np-help-card-icon-primary { background: rgba(96, 99, 238, 0.12); color: var(--np-primary); }
.np-help-card-icon-secondary { background: rgba(107, 56, 212, 0.12); color: var(--np-secondary); }
.np-help-card-icon-tertiary { background: rgba(0, 98, 141, 0.12); color: var(--np-tertiary); }
.np-help-support, .np-help-links { margin-bottom: 1rem; }
.np-help-online {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.82rem;
  font-weight: 600;
  color: #1b7f4a;
  margin: 0.75rem 0 0.35rem 0;
}
.np-help-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #22c55e;
  box-shadow: 0 0 0 3px rgba(34, 197, 94, 0.25);
}
.np-help-contact {
  margin: 0;
  font-size: 0.78rem;
  color: var(--np-on-surface-variant);
}
.np-help-link-list {
  list-style: none;
  margin: 0.75rem 0 0 0;
  padding: 0;
}
.np-help-link-list li {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.45rem 0;
  font-size: 0.82rem;
  color: var(--np-on-surface);
  border-bottom: 1px solid rgba(199, 196, 215, 0.25);
}
.np-help-link-list li:last-child { border-bottom: none; }
.np-help-link-list .material-symbols-outlined {
  font-size: 1.1rem !important;
  color: var(--np-primary);
}
.np-account-profile-row {
  display: flex;
  gap: 1.25rem;
  align-items: flex-start;
}
.np-account-avatar {
  width: 5rem;
  height: 5rem;
  border-radius: 1rem;
  background: linear-gradient(135deg, var(--np-primary), var(--np-secondary));
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  flex-shrink: 0;
}
.np-account-avatar .material-symbols-outlined { font-size: 2.25rem !important; }
.np-account-profile-copy h2 {
  font-family: 'Geist', sans-serif;
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0 0 0.5rem 0;
}
.np-account-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}
.np-account-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  padding: 0.25rem 0.65rem;
  border-radius: 999px;
  font-size: 0.72rem;
  font-weight: 600;
  background: var(--np-surface-low);
  color: var(--np-on-surface-variant);
}
.np-account-badge-primary {
  background: rgba(96, 99, 238, 0.12);
  color: var(--np-primary);
}
.np-account-badge .material-symbols-outlined { font-size: 0.95rem !important; }
.np-account-meta-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
}
.np-meta-label {
  margin: 0 0 0.15rem 0;
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--np-on-surface-variant);
}
.np-account-meta p:last-child {
  margin: 0;
  font-size: 0.88rem;
  font-weight: 500;
}
.np-account-sessions .np-session {
  padding: 0.85rem 0;
  border-bottom: 1px solid rgba(199, 196, 215, 0.3);
}
.np-account-sessions .np-session:last-child { border-bottom: none; }
.np-session-row {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
}
.np-session-row .material-symbols-outlined {
  color: var(--np-on-surface-variant);
  font-size: 1.35rem !important;
}
.np-session-title {
  margin: 0;
  font-size: 0.88rem;
  font-weight: 600;
}
.np-session-sub {
  margin: 0.15rem 0 0 0;
  font-size: 0.75rem;
  color: var(--np-on-surface-variant);
}
.np-session-tag {
  font-size: 0.65rem;
  font-weight: 700;
  text-transform: uppercase;
  padding: 0.1rem 0.4rem;
  border-radius: 4px;
  background: rgba(34, 197, 94, 0.15);
  color: #15803d;
  margin-left: 0.35rem;
}
.np-account-danger {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
  margin-top: 1.5rem;
  padding: 1rem 1.25rem;
  border-radius: 1rem;
  border: 1px solid rgba(186, 26, 26, 0.25);
  background: rgba(255, 218, 214, 0.35);
}
.np-account-danger h4 {
  display: flex;
  align-items: center;
  gap: 0.35rem;
  margin: 0 0 0.35rem 0;
  font-size: 0.9rem;
  color: var(--np-error);
}
.np-account-danger p {
  margin: 0;
  font-size: 0.78rem;
  color: var(--np-on-surface-variant);
}

/* ── Mobile (≤768px) ── */
@media (max-width: 768px) {
  .stApp [data-testid="stMain"],
  .stApp section.main {
    margin-left: 0 !important;
    width: 100% !important;
    max-width: 100% !important;
  }

  .stApp:has(.np-sidebar-hidden-flag) [data-testid="stSidebar"],
  .stApp:has(.np-sidebar-hidden-flag) section[data-testid="stSidebar"] {
    transform: translateX(-105%) !important;
    visibility: hidden !important;
    pointer-events: none !important;
  }

  html.np-is-mobile .stApp:has(.np-sidebar-visible-flag) [data-testid="stMain"],
  html.np-is-mobile .stApp:has(.np-sidebar-hidden-flag) [data-testid="stMain"],
  html.np-is-mobile .stApp:has(.np-sidebar-visible-flag) section.main,
  html.np-is-mobile .stApp:has(.np-sidebar-hidden-flag) section.main {
    margin-left: 0 !important;
    width: 100% !important;
    max-width: 100% !important;
  }

  html.np-is-mobile .stApp:has(.np-sidebar-hidden-flag) [data-testid="stSidebar"],
  html.np-is-mobile .stApp:has(.np-sidebar-hidden-flag) section[data-testid="stSidebar"] {
    transform: translateX(-105%) !important;
    visibility: hidden !important;
    pointer-events: none !important;
  }

  html.np-is-mobile .stApp:has(.np-sidebar-visible-flag) [data-testid="stSidebar"],
  html.np-is-mobile .stApp:has(.np-sidebar-visible-flag) section[data-testid="stSidebar"] {
    transform: translateX(0) !important;
    width: var(--np-mobile-sidebar-width, 280px) !important;
    min-width: var(--np-mobile-sidebar-width, 280px) !important;
    max-width: var(--np-mobile-sidebar-width, 280px) !important;
    z-index: 1005 !important;
    box-shadow: 4px 0 32px rgba(19, 27, 46, 0.2) !important;
    visibility: visible !important;
    pointer-events: auto !important;
    overflow-x: hidden !important;
    overflow-y: auto !important;
    height: 100dvh !important;
    max-height: 100dvh !important;
    transition: transform 0.25s ease, box-shadow 0.25s ease !important;
  }

  html.np-is-mobile .st-key-np_sidebar_chevron {
    left: 0.75rem !important;
    top: 0.65rem !important;
    transform: none !important;
    z-index: 1010 !important;
    visibility: visible !important;
    opacity: 1 !important;
  }

  html.np-is-mobile .stApp:has(.np-sidebar-visible-flag) .st-key-np_sidebar_chevron {
    left: var(--np-mobile-chevron-left, calc(280px - 2.1rem)) !important;
    transform: none !important;
  }

  [data-testid="stMain"] .block-container > .stElementContainer:has(.st-key-np_sidebar_chevron),
  [data-testid="stMainBlockContainer"] > .stElementContainer:has(.st-key-np_sidebar_chevron) {
    height: 0 !important;
    min-height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: visible !important;
  }

  /* Mobile sidebar — sizing, alignment, active item styling */
  html.np-is-mobile [data-testid="stSidebar"] .block-container {
    max-width: 100% !important;
    width: 100% !important;
    height: auto !important;
    min-height: 100% !important;
    max-height: none !important;
    padding: 3.25rem 0.75rem 1.25rem 0.75rem !important;
    gap: 0.35rem !important;
    overflow-y: auto !important;
    box-sizing: border-box !important;
  }
  html.np-is-mobile [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
    gap: 0.35rem !important;
    align-items: stretch !important;
    width: 100% !important;
  }
  html.np-is-mobile .np-sidebar-brand {
    padding: 0.35rem 0.25rem 0.85rem 0.25rem !important;
    margin-bottom: 0.15rem !important;
    gap: 0.65rem !important;
    align-items: center !important;
  }
  html.np-is-mobile .np-sidebar-brand-icon {
    width: 34px !important;
    height: 34px !important;
  }
  html.np-is-mobile .np-sidebar-brand-icon .np-brand-logo {
    width: 34px !important;
    height: 34px !important;
  }
  html.np-is-mobile .np-sidebar-brand-title {
    font-size: 0.975rem !important;
    line-height: 1.15 !important;
  }
  html.np-is-mobile .np-sidebar-brand-sub {
    font-size: 0.6rem !important;
    letter-spacing: 0.1em !important;
  }
  html.np-is-mobile .st-key-np_sidebar_nav [data-testid="stVerticalBlock"],
  html.np-is-mobile .st-key-np_sidebar_nav [data-testid="stVerticalBlockBorderWrapper"],
  html.np-is-mobile .st-key-np_sidebar_footer [data-testid="stVerticalBlock"],
  html.np-is-mobile .st-key-np_sidebar_footer [data-testid="stVerticalBlockBorderWrapper"] {
    gap: 0.2rem !important;
    width: 100% !important;
  }
  html.np-is-mobile [data-testid="stSidebar"] [class*="st-key-np_nav_"],
  html.np-is-mobile [data-testid="stSidebar"] [data-testid="stPageLink"],
  html.np-is-mobile .st-key-np_sidebar_cta,
  html.np-is-mobile .st-key-np_sidebar_footer {
    width: 100% !important;
    max-width: 100% !important;
  }
  html.np-is-mobile [data-testid="stSidebar"] [data-testid="stPageLink-NavLink"],
  html.np-is-mobile [data-testid="stSidebar"] a.np-sidebar-link,
  html.np-is-mobile [data-testid="stSidebar"] a.np-sidebar-footer-link {
    padding: 0.55rem 0.75rem !important;
    min-height: 2.75rem !important;
    font-size: 0.8125rem !important;
    gap: 0.65rem !important;
    align-items: center !important;
    justify-content: flex-start !important;
    border-radius: 10px !important;
    box-sizing: border-box !important;
  }
  html.np-is-mobile [data-testid="stSidebar"] .np-sidebar-icon,
  html.np-is-mobile [data-testid="stSidebar"] .material-symbols-outlined.np-sidebar-icon {
    font-size: 1.125rem !important;
    width: 1.125rem !important;
    height: 1.125rem !important;
    flex-shrink: 0 !important;
  }
  html.np-is-mobile .st-key-np_sidebar_cta {
    margin: 0.5rem 0 0.25rem 0 !important;
  }
  html.np-is-mobile .st-key-np_sidebar_cta [data-testid="stPageLink-NavLink"],
  html.np-is-mobile .st-key-np_sidebar_cta a.np-sidebar-cta {
    padding: 0.65rem 0.85rem !important;
    min-height: 2.75rem !important;
    font-size: 0.8125rem !important;
    justify-content: center !important;
    border-radius: 12px !important;
  }
  html.np-is-mobile .st-key-np_sidebar_footer {
    padding-top: 0.75rem !important;
    margin-top: auto !important;
  }
  html.np-is-mobile [data-testid="stSidebar"] [class*="st-key-np_nav_"]:has(.np-nav-active-flag) [data-testid="stPageLink-NavLink"],
  html.np-is-mobile [data-testid="stSidebar"] [class*="st-key-np_nav_"]:has(.np-nav-active-flag) [data-testid="stPageLink-NavLink"]:hover,
  html.np-is-mobile [data-testid="stSidebar"] a.np-sidebar-link-active,
  html.np-is-mobile [data-testid="stSidebar"] a.np-sidebar-link-active:hover {
    background: var(--np-primary-container) !important;
    color: #ffffff !important;
    font-weight: 600 !important;
  }
  html.np-is-mobile [data-testid="stSidebar"] [class*="st-key-np_nav_"]:has(.np-nav-active-flag) [data-testid="stPageLink-NavLink"] *,
  html.np-is-mobile [data-testid="stSidebar"] a.np-sidebar-link-active,
  html.np-is-mobile [data-testid="stSidebar"] a.np-sidebar-link-active * {
    color: #ffffff !important;
  }

  .np-mobile-sidebar-backdrop {
    position: fixed;
    inset: 0;
    z-index: 1004;
    background: rgba(11, 28, 48, 0.35);
    backdrop-filter: blur(2px);
    -webkit-backdrop-filter: blur(2px);
  }

  [data-testid="stMain"] .block-container,
  [data-testid="stMainBlockContainer"],
  html.np-is-mobile [data-testid="stMain"] .block-container,
  html.np-is-mobile [data-testid="stMainBlockContainer"],
  .stApp:has([data-testid="stSidebar"][aria-expanded="false"]) [data-testid="stMain"] .block-container,
  .stApp:has([data-testid="stSidebar"][aria-hidden="true"]) [data-testid="stMain"] .block-container,
  .stApp:has([data-testid="stSidebar"][aria-expanded="false"]) [data-testid="stMainBlockContainer"],
  .stApp:has([data-testid="stSidebar"][aria-hidden="true"]) [data-testid="stMainBlockContainer"] {
    padding-top: 0 !important;
    padding-inline: 0.625rem !important;
    padding-left: 0.625rem !important;
    padding-right: 0.625rem !important;
    padding-bottom: 1.5rem !important;
    width: 100% !important;
    max-width: 100% !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
  }

  [data-testid="stMain"] > div,
  [data-testid="stMain"] [data-testid="stAppViewContainer"],
  .stApp [data-testid="stAppViewContainer"] {
    width: 100% !important;
    max-width: 100% !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
  }

  .stApp:has([data-testid="stSidebar"][aria-expanded="false"]) .np-status-bar,
  .stApp:has([data-testid="stSidebar"][aria-hidden="true"]) .np-status-bar,
  .stApp:has([data-testid="stSidebar"][aria-expanded="false"]) .np-page-title,
  .stApp:has([data-testid="stSidebar"][aria-hidden="true"]) .np-page-title,
  .stApp:has([data-testid="stSidebar"][aria-expanded="false"]) .np-page-sub,
  .stApp:has([data-testid="stSidebar"][aria-hidden="true"]) .np-page-sub,
  .stApp:has([data-testid="stSidebar"][aria-expanded="false"]) .np-page-sub-compact,
  .stApp:has([data-testid="stSidebar"][aria-hidden="true"]) .np-page-sub-compact {
    max-width: 100% !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
  }

  .np-hero,
  .np-hero-panel {
    padding: 1rem 0.85rem !important;
    margin-bottom: 1rem !important;
  }
  .np-hero-grid { gap: 0.85rem !important; }
  .np-hero-ai-panel { padding: 0.85rem !important; }
  .np-hero-title { font-size: 1.35rem !important; }
  .np-help-hero { padding: 1.25rem 0.85rem !important; }
  .np-glass-card { padding: 0.9rem 0.85rem !important; }

  .stApp:has(.st-key-onboarding_page) [data-testid="stMain"] .block-container,
  .stApp:has(.st-key-onboarding_page) [data-testid="stMainBlockContainer"] {
    max-width: 100% !important;
    padding-top: 0 !important;
    padding-inline: 0.625rem !important;
    padding-left: 0.625rem !important;
    padding-right: 0.625rem !important;
  }

  .np-kpi-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.65rem;
    margin-bottom: 1rem;
  }
  .np-kpi-card { padding: 0.85rem 0.9rem; }
  .np-kpi-value { font-size: 1.35rem; }
  .np-kpi-label { font-size: 0.72rem; }
  .np-kpi-icon { width: 2rem; height: 2rem; }
  .np-kpi-badge { font-size: 0.58rem; padding: 0.12rem 0.4rem; }

  .np-flow-grid { grid-template-columns: 1fr; gap: 0.85rem; }
  .np-hero-grid { grid-template-columns: 1fr; }
  .np-support-title { font-size: 1.45rem; }
  .np-support-sub { font-size: 0.875rem; }
  .np-page-title { font-size: 1.45rem; }
  .np-help-bento { grid-template-columns: 1fr; }
  .np-account-meta-grid { grid-template-columns: 1fr; }
  .np-system-health-bar {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.65rem;
  }

  [data-testid="stHorizontalBlock"] {
    flex-direction: column !important;
    gap: 0.65rem !important;
    width: 100% !important;
  }
  [data-testid="stHorizontalBlock"] [data-testid="column"] {
    width: 100% !important;
    min-width: 100% !important;
    max-width: 100% !important;
    flex: 1 1 100% !important;
  }

  .st-key-onboarding_page > div > [data-testid="stVerticalBlock"] > [data-testid="stHorizontalBlock"] [data-testid="column"],
  .st-key-onboarding_page [data-testid="column"] {
    width: 100% !important;
    min-width: 100% !important;
    max-width: 100% !important;
    flex: 1 1 100% !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="column"],
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stHorizontalBlock"] [data-testid="column"] {
    width: auto !important;
    min-width: 0 !important;
    max-width: none !important;
    flex: 1 1 0 !important;
  }

  .st-key-manual_row_onboarding_skills [data-testid="column"],
  .st-key-manual_row_onboarding_interests [data-testid="column"] {
    width: auto !important;
    min-width: 0 !important;
    max-width: none !important;
  }
  .st-key-manual_row_onboarding_skills [data-testid="column"]:first-child,
  .st-key-manual_row_onboarding_interests [data-testid="column"]:first-child {
    flex: 11 1 0 !important;
  }
  .st-key-manual_row_onboarding_skills [data-testid="column"]:last-child,
  .st-key-manual_row_onboarding_interests [data-testid="column"]:last-child {
    flex: 1 1 0 !important;
  }

  .st-key-onboarding_page > div > [data-testid="stHorizontalBlock"]:nth-last-child(1) {
    flex-direction: column !important;
    gap: 1rem !important;
    width: 100% !important;
  }

  .st-key-volunteer_hero_shell,
  .st-key-volunteer_form_shell {
    width: 100% !important;
    max-width: 100% !important;
  }

  .np-onboarding-v2-hero {
    min-height: auto;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
    padding: 1rem 0.85rem !important;
  }

  .st-key-availability_cards,
  .st-key-availability_cards > div[data-testid="stVerticalBlock"],
  .st-key-availability_cards [data-testid="stHorizontalBlock"],
  .st-key-manual_row_onboarding_skills [data-testid="stHorizontalBlock"],
  .st-key-manual_row_onboarding_interests [data-testid="stHorizontalBlock"],
  .stTabs [data-baseweb="tab-list"] {
    flex-direction: row !important;
  }

  .stTabs [data-baseweb="tab-list"] {
    flex-wrap: wrap !important;
    gap: 0.35rem !important;
  }
  .stTabs [data-baseweb="tab"] {
    padding: 0.42rem 0.7rem !important;
    font-size: 0.72rem !important;
  }

  .st-key-volunteer_hero_shell {
    margin-right: 0 !important;
  }

  div[data-testid="stForm"] {
    padding: 0.75rem 0 !important;
  }

  /* Smart Volunteer Profile form — mobile alignment & spacing */
  .st-key-volunteer_form_shell {
    padding: 0 0 7rem 0 !important;
  }
  .st-key-volunteer_form_card {
    background: rgba(255, 255, 255, 0.88) !important;
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    border: 1px solid rgba(199, 196, 215, 0.55) !important;
    border-radius: 1rem !important;
    box-shadow: 0 8px 24px rgba(70, 72, 212, 0.1) !important;
    padding: 0.875rem 0.75rem !important;
    margin-top: 0 !important;
    box-sizing: border-box !important;
    width: 100% !important;
    max-width: 100% !important;
  }
  .st-key-volunteer_form_card > [data-testid="stVerticalBlock"] {
    gap: 0.5rem !important;
  }
  .np-onboarding-v2-form-header {
    margin-bottom: 0.35rem !important;
    padding-bottom: 0 !important;
  }
  .np-onboarding-v2-form-title {
    font-size: 1.15rem;
    line-height: 1.25 !important;
    margin-bottom: 0.15rem !important;
  }
  .np-onboarding-v2-form-sub {
    font-size: 0.8125rem !important;
    line-height: 1.45 !important;
    margin-bottom: 0 !important;
  }
  .st-key-volunteer_form_shell .np-v2-field-label,
  .st-key-volunteer_form_shell .np-v2-field-sublabel {
    margin: 0.1rem 0 0.25rem 0 !important;
  }
  .st-key-volunteer_form_shell .np-v2-field-hint {
    margin: 0 0 0.35rem 0 !important;
  }
  .st-key-volunteer_form_shell div[data-testid="stForm"] {
    padding: 0 !important;
    margin-top: 0.35rem !important;
  }
  .st-key-volunteer_form_shell div[data-testid="stForm"] [data-testid="stVerticalBlock"] {
    gap: 0.65rem !important;
  }
  .st-key-volunteer_form_shell div[data-testid="stForm"] [data-testid="stHorizontalBlock"] {
    gap: 0.65rem !important;
    width: 100% !important;
    align-items: stretch !important;
  }
  .st-key-volunteer_form_shell div[data-testid="stForm"] [data-testid="column"] {
    width: 100% !important;
    min-width: 0 !important;
    max-width: 100% !important;
    flex: 1 1 100% !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
  }
  .st-key-volunteer_form_shell [data-testid="stTextInput"],
  .st-key-volunteer_form_shell [data-testid="stTextArea"],
  .st-key-volunteer_form_shell [data-testid="stPills"],
  .st-key-volunteer_form_shell .st-key-manual_row_onboarding_skills,
  .st-key-volunteer_form_shell .st-key-manual_row_onboarding_interests {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
  }
  .st-key-volunteer_form_shell div[data-baseweb="input"],
  .st-key-volunteer_form_shell div[data-baseweb="textarea"] {
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
    min-height: 44px !important;
  }
  .st-key-volunteer_form_shell div[data-baseweb="textarea"] {
    min-height: 72px !important;
  }
  .st-key-volunteer_form_shell [data-testid="stTextInput"] label p,
  .st-key-volunteer_form_shell [data-testid="stTextArea"] label p {
    margin-bottom: 0.35rem !important;
  }
  .st-key-volunteer_form_shell [data-testid="stPills"] > div {
    gap: 0.4rem !important;
    justify-content: flex-start !important;
  }
  .st-key-volunteer_form_shell [data-testid="stPills"] button {
    min-height: 2rem !important;
    padding: 0.25rem 0.7rem !important;
  }
  .st-key-volunteer_form_shell .st-key-manual_row_onboarding_skills [data-testid="stHorizontalBlock"],
  .st-key-volunteer_form_shell .st-key-manual_row_onboarding_interests [data-testid="stHorizontalBlock"] {
    align-items: stretch !important;
    gap: 0.5rem !important;
  }
  .st-key-volunteer_form_shell .st-key-manual_row_onboarding_skills .stButton > button,
  .st-key-volunteer_form_shell .st-key-manual_row_onboarding_interests .stButton > button {
    margin-top: 0.5rem !important;
    min-height: 44px !important;
    padding: 0 0.65rem !important;
  }
  .st-key-availability_cards,
  .st-key-availability_cards > div[data-testid="stVerticalBlock"] {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    align-items: stretch !important;
    gap: 0 !important;
    width: 100% !important;
    margin: 0.1rem 0 0.35rem 0 !important;
    padding: 0 !important;
  }
  .st-key-availability_cards > *,
  .st-key-availability_cards [data-testid="stVerticalBlock"] > * {
    flex: 1 1 0 !important;
    min-width: 0 !important;
    width: auto !important;
    max-width: none !important;
  }
  .st-key-availability_cards [data-testid="stCheckbox"] label[data-baseweb="checkbox"] {
    min-height: 2.65rem !important;
    padding: 0.45rem 0.2rem !important;
    justify-content: center !important;
    border-radius: 0 !important;
  }
  .st-key-availability_cards [data-testid="stCheckbox"] label p {
    font-size: 0.75rem !important;
    text-align: center !important;
    white-space: nowrap !important;
  }
  .np-v2-form-footer {
    margin-top: 0.15rem !important;
    margin-bottom: 0.65rem !important;
    padding-top: 0.85rem !important;
  }
  .st-key-volunteer_form_shell [data-testid="stFormSubmitButton"] > button {
    min-height: 2.85rem !important;
    font-size: 0.9rem !important;
  }
}

@media (max-width: 480px) {
  [data-testid="stMain"] .block-container,
  [data-testid="stMainBlockContainer"],
  html.np-is-mobile [data-testid="stMain"] .block-container,
  html.np-is-mobile [data-testid="stMainBlockContainer"],
  .stApp:has([data-testid="stSidebar"][aria-expanded="false"]) [data-testid="stMain"] .block-container,
  .stApp:has([data-testid="stSidebar"][aria-hidden="true"]) [data-testid="stMain"] .block-container,
  .stApp:has([data-testid="stSidebar"][aria-expanded="false"]) [data-testid="stMainBlockContainer"],
  .stApp:has([data-testid="stSidebar"][aria-hidden="true"]) [data-testid="stMainBlockContainer"] {
    padding-inline: 0.5rem !important;
    padding-left: 0.5rem !important;
    padding-right: 0.5rem !important;
  }

  .np-hero,
  .np-hero-panel,
  .np-help-hero {
    padding: 0.85rem 0.65rem !important;
  }

  .np-kpi-grid { grid-template-columns: 1fr; }

  .stApp:has(.st-key-onboarding_page) [data-testid="stMain"] .block-container,
  .stApp:has(.st-key-onboarding_page) [data-testid="stMainBlockContainer"] {
    padding-inline: 0.5rem !important;
    padding-left: 0.5rem !important;
    padding-right: 0.5rem !important;
  }

  .st-key-volunteer_form_shell {
    padding: 0.75rem !important;
  }

  .st-key-volunteer_form_card {
    padding: 0.875rem 0.75rem !important;
  }

  /* Availability — keep all three options on one row */
  .st-key-volunteer_form_shell .st-key-availability_cards,
  .st-key-volunteer_form_shell .st-key-availability_cards > div[data-testid="stVerticalBlock"] {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    gap: 0 !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards > *,
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stVerticalBlock"] > * {
    flex: 1 1 0 !important;
    min-width: 0 !important;
    width: auto !important;
    max-width: none !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stCheckbox"] label[data-baseweb="checkbox"] {
    border: 1px solid var(--np-outline-variant) !important;
    border-radius: 0 !important;
    margin-left: 0 !important;
    min-height: 2.65rem !important;
    padding: 0.45rem 0.2rem !important;
    justify-content: center !important;
    align-items: center !important;
    background: #ffffff !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards > *:first-child [data-testid="stCheckbox"] label[data-baseweb="checkbox"],
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stVerticalBlock"] > *:first-child [data-testid="stCheckbox"] label[data-baseweb="checkbox"] {
    border-top-left-radius: 0.75rem !important;
    border-bottom-left-radius: 0.75rem !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards > *:not(:first-child) [data-testid="stCheckbox"] label[data-baseweb="checkbox"],
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stVerticalBlock"] > *:not(:first-child) [data-testid="stCheckbox"] label[data-baseweb="checkbox"] {
    border-left: none !important;
    margin-left: -1px !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards > *:last-child [data-testid="stCheckbox"] label[data-baseweb="checkbox"],
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stVerticalBlock"] > *:last-child [data-testid="stCheckbox"] label[data-baseweb="checkbox"] {
    border-top-right-radius: 0.75rem !important;
    border-bottom-right-radius: 0.75rem !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stCheckbox"] label p {
    font-size: 0.72rem !important;
    text-align: center !important;
    white-space: nowrap !important;
  }

  /* Stack manual add rows: input full width, Add button below */
  .st-key-volunteer_form_shell .st-key-manual_row_onboarding_skills [data-testid="stHorizontalBlock"],
  .st-key-volunteer_form_shell .st-key-manual_row_onboarding_interests [data-testid="stHorizontalBlock"] {
    flex-direction: column !important;
    gap: 0.45rem !important;
  }
  .st-key-volunteer_form_shell .st-key-manual_row_onboarding_skills [data-testid="column"],
  .st-key-volunteer_form_shell .st-key-manual_row_onboarding_interests [data-testid="column"] {
    width: 100% !important;
    min-width: 0 !important;
    max-width: 100% !important;
    flex: 1 1 100% !important;
  }
  .st-key-volunteer_form_shell .st-key-manual_row_onboarding_skills .stButton > button,
  .st-key-volunteer_form_shell .st-key-manual_row_onboarding_interests .stButton > button {
    margin-top: 0 !important;
    width: 100% !important;
    min-height: 2.75rem !important;
  }
}

@media (max-width: 960px) {
  .np-help-bento { grid-template-columns: 1fr; }
  .np-account-meta-grid { grid-template-columns: 1fr; }
  .np-system-health-bar { flex-direction: column; align-items: flex-start; }
  .np-onboarding-topbar-nav { display: none; }
  .np-onboarding-v2-hero { min-height: auto; }
  .st-key-onboarding_page [data-testid="stHorizontalBlock"] {
    flex-direction: column !important;
  }
}

@media (max-width: 960px) and (min-width: 481px) {
  .st-key-availability_cards,
  .st-key-availability_cards > div[data-testid="stVerticalBlock"] {
    flex-direction: row !important;
  }
}

/* ── Stitch mobile screens (Bulbul AI OS pack) ── */
@media (max-width: 768px) {
  /* Mobile screen headers — shared glass background */
  .np-page-header,
  .np-support-header,
  .np-mob-admin-head,
  .np-mob-help-hero,
  .np-mob-task-status,
  .np-mob-account-profile,
  .np-hero,
  .np-mob-onboarding-chat {
    background: rgba(255, 255, 255, 0.88) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(199, 196, 215, 0.55) !important;
    border-radius: 1rem !important;
    box-shadow: 0 8px 24px rgba(70, 72, 212, 0.1) !important;
    box-sizing: border-box !important;
  }
  .np-page-header,
  .np-support-header,
  .np-mob-admin-head,
  .np-mob-help-hero,
  .np-mob-task-status,
  .np-mob-account-profile,
  .np-hero,
  .np-mob-onboarding-chat {
    padding: 0.875rem 0.75rem !important;
    margin-top: 0 !important;
    margin-bottom: 0.75rem !important;
  }
  .np-page-header .np-page-title {
    font-size: 1.45rem !important;
    margin-bottom: 0.35rem !important;
  }
  .np-page-header .np-page-sub,
  .np-page-header .np-page-sub-compact {
    font-size: 0.875rem !important;
    line-height: 1.45 !important;
    margin-bottom: 0 !important;
  }
  [data-testid="stElementContainer"]:has(.np-page-header),
  [data-testid="stMarkdownContainer"]:has(.np-page-header) {
    margin: 0 !important;
    padding: 0 !important;
  }

  /* Onboarding mobile — ai_onboarding_mobile */
  .st-key-volunteer_hero_shell {
    display: none !important;
    height: 0 !important;
    min-height: 0 !important;
    max-height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
    border: none !important;
  }
  .st-key-onboarding_page [data-testid="stVerticalBlock"] {
    gap: 0 !important;
  }
  .st-key-onboarding_page [data-testid="stVerticalBlock"] > div:has(.np-onboarding-bg-blob),
  .st-key-onboarding_page [data-testid="stElementContainer"]:has(.np-onboarding-bg-blob) {
    display: none !important;
    height: 0 !important;
    min-height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
  }
  .stApp:has(.st-key-onboarding_page) [data-testid="stMain"] .block-container,
  .stApp:has(.st-key-onboarding_page) [data-testid="stMainBlockContainer"] {
    padding-top: 0 !important;
  }
  .st-key-onboarding_page [data-testid="stVerticalBlock"] > div:has(.np-onboarding-v2-hero),
  .st-key-onboarding_page [data-testid="stVerticalBlock"] > .st-key-volunteer_hero_shell,
  .st-key-onboarding_page > .st-key-volunteer_hero_shell {
    display: none !important;
    height: 0 !important;
    min-height: 0 !important;
    max-height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
  }
  .st-key-volunteer_form_shell > [data-testid="stVerticalBlock"] {
    gap: 0 !important;
    margin-top: 0 !important;
    padding-top: 0 !important;
  }
  .st-key-volunteer_form_card .np-onboarding-v2-form-header {
    display: block !important;
    margin-bottom: 0.35rem !important;
    padding-bottom: 0 !important;
  }
  .st-key-volunteer_form_card .np-onboarding-v2-form-title {
    font-size: 1.15rem !important;
    line-height: 1.25 !important;
    margin-bottom: 0.15rem !important;
  }
  .st-key-volunteer_form_card .np-onboarding-v2-form-sub {
    font-size: 0.8125rem !important;
    line-height: 1.45 !important;
    margin-bottom: 0 !important;
  }
  .st-key-volunteer_form_card .np-v2-field-label,
  .st-key-volunteer_form_card .np-v2-field-sublabel {
    margin: 0.1rem 0 0.25rem 0 !important;
  }
  .st-key-volunteer_form_card .np-v2-field-label,
  .st-key-volunteer_form_card .np-v2-field-hint {
    display: block !important;
  }
  .st-key-volunteer_form_card .np-v2-field-hint {
    margin: 0 0 0.35rem 0 !important;
  }
  .st-key-volunteer_form_card [data-testid="stElementContainer"]:has(.np-onboarding-v2-form-header),
  .st-key-volunteer_form_card [data-testid="stMarkdownContainer"]:has(.np-onboarding-v2-form-header),
  .st-key-volunteer_form_card [data-testid="stElementContainer"]:has(.np-v2-field-label),
  .st-key-volunteer_form_card [data-testid="stMarkdownContainer"]:has(.np-v2-field-label),
  .st-key-volunteer_form_card [data-testid="stElementContainer"]:has(.np-v2-field-hint),
  .st-key-volunteer_form_card [data-testid="stMarkdownContainer"]:has(.np-v2-field-hint) {
    display: block !important;
    height: auto !important;
    min-height: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: visible !important;
  }
  .np-mob-onboarding-chat {
    margin-bottom: 0.75rem;
  }
  .np-mob-onboarding-chat .np-mob-onboarding-bubble {
    background: rgba(255, 255, 255, 0.92) !important;
    border: 1px solid rgba(199, 196, 215, 0.45) !important;
  }
  .st-key-onboarding_mobile_chat,
  .st-key-onboarding_mobile_chat > [data-testid="stVerticalBlock"],
  .st-key-onboarding_mobile_chat [data-testid="stElementContainer"]:has(.np-mob-onboarding-chat),
  .st-key-onboarding_mobile_chat [data-testid="stMarkdownContainer"]:has(.np-mob-onboarding-chat) {
    margin: 0 !important;
    padding: 0 !important;
    min-height: 0 !important;
  }
  .st-key-volunteer_form_shell [data-testid="stElementContainer"]:has(.np-mob-onboarding-chat),
  .st-key-volunteer_form_shell [data-testid="stMarkdownContainer"]:has(.np-mob-onboarding-chat) {
    margin: 0 !important;
    padding: 0 !important;
  }
  .st-key-volunteer_form_shell {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    margin-top: 0 !important;
  }
  .np-mob-onboarding-chat-row {
    display: flex;
    align-items: flex-start;
    gap: 0.75rem;
  }
  .np-mob-onboarding-bot {
    position: relative;
    width: 2.5rem;
    height: 2.5rem;
    border-radius: 0.75rem;
    background: var(--np-primary);
    color: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    box-shadow: 0 8px 20px rgba(70, 72, 212, 0.25);
  }
  .np-mob-onboarding-bot .material-symbols-outlined {
    font-size: 1.25rem;
  }
  .np-mob-onboarding-bot-dot {
    position: absolute;
    bottom: -2px;
    right: -2px;
    width: 0.75rem;
    height: 0.75rem;
    background: #22c55e;
    border: 2px solid #fff;
    border-radius: 999px;
  }
  .np-mob-onboarding-bubble {
    position: relative;
    max-width: 85%;
    background: rgba(255, 255, 255, 0.72);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.35);
    border-radius: 1rem;
    padding: 0.85rem 1rem;
    box-shadow: 0 4px 16px rgba(70, 72, 212, 0.08);
  }
  .np-mob-onboarding-bubble p {
    margin: 0;
    font-size: 0.875rem;
    line-height: 1.45;
    color: var(--np-on-surface);
  }
  .np-mob-onboarding-bubble strong {
    color: var(--np-primary);
  }
  .np-mob-step-head {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin: 0.45rem 0 0.3rem 0;
  }
  .st-key-volunteer_form_shell div[data-testid="stForm"] .np-mob-step-head:first-of-type {
    margin-top: 0.1rem !important;
  }
  .np-mob-step-num {
    width: 1.5rem;
    height: 1.5rem;
    border-radius: 999px;
    background: rgba(70, 72, 212, 0.1);
    color: var(--np-primary);
    font-size: 0.75rem;
    font-weight: 700;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
  .np-mob-step-title {
    margin: 0;
    font-family: 'Geist', sans-serif;
    font-size: 1.05rem;
    font-weight: 500;
    color: var(--np-on-surface);
  }
  .np-mob-onboarding-dock {
    position: fixed;
    left: 0;
    right: 0;
    bottom: 0;
    z-index: 1002;
    pointer-events: none;
  }
  .np-mob-onboarding-dock-inner {
    background: rgba(248, 249, 255, 0.95);
    backdrop-filter: blur(12px);
    border-top: 1px solid rgba(199, 196, 215, 0.25);
    box-shadow: 0 -10px 30px rgba(0, 0, 0, 0.05);
    padding: 0.75rem 1rem calc(0.85rem + env(safe-area-inset-bottom, 0px));
  }
  .np-mob-dock-status {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
  }
  .np-mob-dock-pulse-wrap {
    position: relative;
    width: 0.5rem;
    height: 0.5rem;
    margin-right: 0.35rem;
  }
  .np-mob-dock-pulse {
    position: absolute;
    inset: 0;
    border-radius: 999px;
    background: rgba(70, 72, 212, 0.4);
    animation: np-mob-ping 2s cubic-bezier(0, 0, 0.2, 1) infinite;
  }
  .np-mob-dock-dot {
    position: relative;
    display: block;
    width: 0.5rem;
    height: 0.5rem;
    border-radius: 999px;
    background: var(--np-primary);
  }
  @keyframes np-mob-ping {
    75%, 100% { transform: scale(2); opacity: 0; }
  }
  .np-mob-dock-label {
    flex: 1;
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--np-primary);
  }
  .np-mob-dock-pct {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.75rem;
    color: var(--np-on-surface-variant);
  }
  .np-mob-dock-track {
    width: 100%;
    height: 0.375rem;
    background: rgba(70, 72, 212, 0.1);
    border-radius: 999px;
    overflow: hidden;
  }
  .np-mob-dock-fill {
    height: 100%;
    background: var(--np-primary);
    border-radius: 999px;
    transition: width 0.5s ease;
  }
  .np-mob-dock-social {
    margin: 0.45rem 0 0 0;
    font-size: 0.625rem;
    color: var(--np-on-surface-variant);
  }
  .st-key-volunteer_form_shell [data-testid="stFormSubmitButton"] > button {
    min-height: 3.25rem !important;
    border-radius: 1rem !important;
    font-size: 1rem !important;
    box-shadow: 0 12px 40px rgba(70, 72, 212, 0.3) !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards,
  .st-key-volunteer_form_shell .st-key-availability_cards > div[data-testid="stVerticalBlock"] {
    display: flex !important;
    flex-direction: row !important;
    flex-wrap: nowrap !important;
    align-items: stretch !important;
    gap: 0 !important;
    width: 100% !important;
    margin: 0.1rem 0 0.35rem 0 !important;
    padding: 0 !important;
    grid-template-columns: unset !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards > *,
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stVerticalBlock"] > * {
    flex: 1 1 0 !important;
    min-width: 0 !important;
    width: auto !important;
    max-width: none !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stCheckbox"] label[data-baseweb="checkbox"] {
    flex-direction: row !important;
    align-items: center !important;
    justify-content: center !important;
    min-height: 2.65rem !important;
    padding: 0.45rem 0.2rem !important;
    border-radius: 0 !important;
    border: 1px solid var(--np-outline-variant) !important;
    background: #ffffff !important;
    backdrop-filter: none !important;
    margin-left: 0 !important;
    position: relative !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards > *:first-child [data-testid="stCheckbox"] label[data-baseweb="checkbox"],
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stVerticalBlock"] > *:first-child [data-testid="stCheckbox"] label[data-baseweb="checkbox"] {
    border-top-left-radius: 0.75rem !important;
    border-bottom-left-radius: 0.75rem !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards > *:not(:first-child) [data-testid="stCheckbox"] label[data-baseweb="checkbox"],
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stVerticalBlock"] > *:not(:first-child) [data-testid="stCheckbox"] label[data-baseweb="checkbox"] {
    border-left: none !important;
    margin-left: -1px !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards > *:last-child [data-testid="stCheckbox"] label[data-baseweb="checkbox"],
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stVerticalBlock"] > *:last-child [data-testid="stCheckbox"] label[data-baseweb="checkbox"] {
    border-top-right-radius: 0.75rem !important;
    border-bottom-right-radius: 0.75rem !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stCheckbox"]:has(input:checked) label[data-baseweb="checkbox"] {
    border-color: var(--np-primary) !important;
    background: rgba(96, 99, 238, 0.08) !important;
    box-shadow: inset 0 0 0 1px var(--np-primary) !important;
  }
  .st-key-volunteer_form_shell .st-key-availability_cards [data-testid="stCheckbox"] label p {
    font-size: 0.75rem !important;
    font-weight: 600 !important;
    text-align: center !important;
    white-space: nowrap !important;
  }
  .st-key-volunteer_form_shell .np-v2-form-footer-sub,
  .st-key-volunteer_form_shell .np-v2-form-footer-highlight {
    display: none !important;
  }
  .st-key-volunteer_form_shell .np-v2-form-footer {
    border-top: none !important;
    padding-top: 0 !important;
    margin-bottom: 0.25rem !important;
  }

  /* Admin mobile — admin_dashboard_mobile */
  .st-key-admin_page .np-page-title,
  .st-key-admin_page .np-page-sub {
    display: none !important;
  }
  .np-mob-admin-head {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 0.75rem;
    margin-bottom: 0.85rem;
  }
  .np-mob-admin-greeting {
    margin: 0;
    font-size: 0.875rem;
    color: var(--np-on-surface-variant);
  }
  .np-mob-admin-title {
    margin: 0.15rem 0 0 0;
    font-family: 'Geist', sans-serif;
    font-size: 1.35rem;
    font-weight: 500;
    color: var(--np-on-surface);
  }
  .np-mob-live-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    padding: 0.35rem 0.75rem;
    border-radius: 999px;
    background: rgba(96, 99, 238, 0.1);
    border: 1px solid rgba(96, 99, 238, 0.2);
    font-size: 0.8125rem;
    font-weight: 500;
    color: var(--np-primary);
    white-space: nowrap;
  }
  .np-mob-live-dot {
    width: 0.375rem;
    height: 0.375rem;
    border-radius: 999px;
    background: var(--np-primary);
    animation: np-mob-ping 2s cubic-bezier(0, 0, 0.2, 1) infinite;
  }
  .st-key-admin_page .np-kpi-grid {
    display: flex !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    gap: 0.75rem !important;
    margin: 0 -0.625rem 1rem 0 !important;
    padding: 0 0.625rem 0.25rem 0 !important;
    scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch;
  }
  .st-key-admin_page .np-kpi-grid::-webkit-scrollbar {
    display: none;
  }
  .st-key-admin_page .np-kpi-card {
    min-width: 10rem !important;
    flex: 0 0 auto !important;
    scroll-snap-align: center;
    background: rgba(255, 255, 255, 0.72) !important;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(241, 245, 249, 0.8) !important;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.02) !important;
  }
  .st-key-admin_page .np-kpi-card:nth-child(2) {
    border-left: 4px solid rgba(70, 72, 212, 0.4) !important;
  }
  .np-mob-candidate-card {
    background: rgba(255, 255, 255, 0.72);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(241, 245, 249, 0.8);
    border-radius: 0.85rem;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.04);
    margin-bottom: 0.65rem;
    overflow: hidden;
  }
  .np-mob-candidate-card--glow {
    position: relative;
  }
  .np-mob-candidate-card--glow::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--np-primary), var(--np-secondary));
    opacity: 0.6;
  }
  .np-mob-candidate-top {
    display: flex;
    gap: 0.75rem;
    padding: 0.85rem;
  }
  .np-mob-candidate-avatar {
    width: 3rem;
    height: 3rem;
    border-radius: 0.65rem;
    background: var(--np-surface-container);
    border: 1px solid rgba(199, 196, 215, 0.35);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--np-primary);
    flex-shrink: 0;
  }
  .np-mob-candidate-meta {
    flex: 1;
    min-width: 0;
  }
  .np-mob-candidate-name-row {
    display: flex;
    justify-content: space-between;
    gap: 0.5rem;
  }
  .np-mob-candidate-name {
    margin: 0;
    font-size: 1rem;
    font-weight: 600;
  }
  .np-mob-candidate-sub {
    margin: 0.15rem 0 0 0;
    font-size: 0.8125rem;
    color: var(--np-on-surface-variant);
  }
  .np-mob-candidate-score {
    text-align: center;
    background: rgba(70, 72, 212, 0.08);
    border-radius: 0.45rem;
    padding: 0.2rem 0.45rem;
    flex-shrink: 0;
  }
  .np-mob-candidate-score-label {
    display: block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.55rem;
    text-transform: uppercase;
    color: var(--np-primary);
  }
  .np-mob-candidate-score-value {
    display: block;
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--np-primary);
    line-height: 1.1;
  }
  .np-mob-candidate-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    margin-top: 0.5rem;
  }
  .np-mob-candidate-tag {
    padding: 0.15rem 0.45rem;
    border-radius: 0.35rem;
    background: var(--np-tertiary-fixed, #c9e6ff);
    color: var(--np-on-tertiary-fixed-variant, #004c6e);
    font-size: 0.72rem;
    font-weight: 500;
  }
  .np-mob-admin-bento {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.75rem;
    margin: 1rem 0 0.5rem 0;
  }
  .np-mob-bento-card {
    border-radius: 1rem;
    padding: 0.85rem;
    min-height: 8.75rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .np-mob-bento-card h5 {
    margin: 0 0 0.2rem 0;
    font-size: 0.875rem;
    font-weight: 600;
  }
  .np-mob-bento-card p {
    margin: 0;
    font-size: 0.72rem;
    line-height: 1.35;
    color: var(--np-on-surface-variant);
  }
  .np-mob-bento-card--light {
    background: rgba(255, 255, 255, 0.72);
    border: 1px solid rgba(199, 196, 215, 0.35);
    border-bottom: 2px solid rgba(70, 72, 212, 0.2);
  }
  .np-mob-bento-card--primary {
    background: var(--np-primary-container);
    color: var(--np-on-primary-container);
    position: relative;
    overflow: hidden;
  }
  .np-mob-bento-card--primary p {
    color: rgba(255, 251, 255, 0.85);
  }
  .st-key-admin_page [data-testid="stTabs"] {
    margin-top: 0.25rem !important;
  }
  .st-key-admin_page [data-baseweb="tab-list"] {
    overflow-x: auto !important;
    flex-wrap: nowrap !important;
  }

  /* Task mobile — task_results_mobile */
  .st-key-tasks_page .np-page-title,
  .st-key-tasks_page .np-page-sub {
    display: none !important;
  }
  .np-mob-task-status {
    position: relative;
    overflow: hidden;
    margin-bottom: 0.75rem !important;
  }
  .np-mob-task-status-scan {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--np-primary), transparent);
    animation: np-mob-scan 3s linear infinite;
  }
  @keyframes np-mob-scan {
    0% { top: 0; opacity: 0; }
    50% { opacity: 1; }
    100% { top: 100%; opacity: 0; }
  }
  .np-mob-task-status-row {
    display: flex;
    justify-content: space-between;
    gap: 0.75rem;
  }
  .np-mob-task-status-title {
    margin: 0 0 0.25rem 0;
    font-family: 'Geist', sans-serif;
    font-size: 1.05rem;
    font-weight: 500;
    color: var(--np-primary);
  }
  .np-mob-task-status-sub {
    margin: 0;
    font-size: 0.8125rem;
    color: var(--np-on-surface-variant);
  }
  .np-mob-task-accuracy {
    text-align: right;
  }
  .np-mob-task-accuracy-label {
    display: block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.625rem;
    color: var(--np-primary);
    background: rgba(70, 72, 212, 0.1);
    padding: 0.15rem 0.4rem;
    border-radius: 0.25rem;
  }
  .np-mob-task-accuracy-value {
    display: block;
    font-family: 'Geist', sans-serif;
    font-size: 1.35rem;
    font-weight: 800;
    color: var(--np-primary);
    line-height: 1.1;
  }
  .np-mob-task-badges {
    display: flex;
    flex-wrap: wrap;
    gap: 0.45rem;
    margin-top: 0.85rem;
  }
  .np-mob-task-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
    padding: 0.25rem 0.65rem;
    border-radius: 999px;
    background: var(--np-secondary-fixed);
    color: var(--np-on-secondary-fixed);
    font-size: 0.72rem;
    font-weight: 500;
  }
  .np-mob-task-badge .material-symbols-outlined {
    font-size: 0.875rem;
  }
  .np-mob-task-badge--tertiary {
    background: var(--np-tertiary-fixed);
    color: var(--np-on-tertiary-fixed);
  }
  .np-mob-match-card {
    background: rgba(255, 255, 255, 0.72);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(241, 245, 249, 1);
    border-radius: 0.85rem;
    padding: 1rem;
    margin-bottom: 0.75rem;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.04);
  }
  .np-mob-match-card--primary {
    box-shadow: 0 8px 30px rgba(70, 72, 212, 0.12);
  }
  .np-mob-match-head {
    display: flex;
    justify-content: space-between;
    gap: 0.5rem;
    margin-bottom: 0.75rem;
  }
  .np-mob-match-person {
    display: flex;
    align-items: center;
    gap: 0.65rem;
    min-width: 0;
  }
  .np-mob-match-avatar {
    width: 2.5rem;
    height: 2.5rem;
    border-radius: 999px;
    border: 2px solid rgba(70, 72, 212, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--np-primary);
    flex-shrink: 0;
  }
  .np-mob-match-person h3 {
    margin: 0;
    font-size: 0.875rem;
    font-weight: 600;
  }
  .np-mob-match-person span {
    font-size: 0.72rem;
    color: var(--np-on-surface-variant);
  }
  .np-mob-match-score {
    text-align: right;
    flex-shrink: 0;
  }
  .np-mob-match-score span {
    display: block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.55rem;
    color: var(--np-secondary-container);
  }
  .np-mob-match-score strong {
    font-size: 0.95rem;
    color: var(--np-secondary-container);
  }
  .np-mob-match-task {
    display: flex;
    align-items: center;
    gap: 0.45rem;
    padding: 0.55rem 0.75rem;
    border-radius: 0.65rem;
    background: var(--np-surface-container);
    margin-bottom: 0.65rem;
    font-size: 0.8125rem;
    font-weight: 500;
  }
  .np-mob-match-task .material-symbols-outlined {
    font-size: 1rem;
    color: var(--np-primary);
  }
  .np-mob-match-reason {
    display: flex;
    gap: 0.45rem;
    border-top: 1px solid rgba(199, 196, 215, 0.25);
    padding-top: 0.65rem;
  }
  .np-mob-match-reason .material-symbols-outlined {
    font-size: 1rem;
    color: var(--np-secondary);
    margin-top: 0.1rem;
  }
  .np-mob-match-reason h4 {
    margin: 0 0 0.2rem 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: var(--np-secondary);
    letter-spacing: 0.04em;
  }
  .np-mob-match-reason p {
    margin: 0;
    font-size: 0.75rem;
    line-height: 1.45;
    color: var(--np-on-surface-variant);
  }
  .st-key-tasks_page .np-ai-card {
    display: none !important;
  }

  /* Help mobile — help_center_mobile */
  .st-key-help_page .np-support-header,
  .st-key-help_page .np-help-hero {
    display: none !important;
  }
  .np-mob-help-hero {
    text-align: center;
    margin-bottom: 0.75rem !important;
  }
  .np-mob-help-hero h1 {
    margin: 0 0 0.35rem 0;
    font-family: 'Geist', sans-serif;
    font-size: 1.5rem;
    font-weight: 600;
    color: var(--np-on-background);
  }
  .np-mob-help-hero p {
    margin: 0;
    font-size: 0.875rem;
    color: var(--np-on-surface-variant);
  }
  .st-key-help_page [data-testid="stTextInput"] div[data-baseweb="input"] {
    min-height: 3.25rem !important;
    border-radius: 0.85rem !important;
    padding-left: 0.25rem !important;
  }
  .st-key-help_page .np-help-bento {
    display: flex !important;
    flex-direction: column !important;
    gap: 0.75rem !important;
  }
  .st-key-help_page .np-help-card:first-child {
    border-left: 4px solid var(--np-primary) !important;
    box-shadow: 0 0 20px rgba(70, 72, 212, 0.12) !important;
  }
  .st-key-help_page .np-help-card ul {
    display: none !important;
  }
  .st-key-help_page [data-testid="column"] {
    width: 100% !important;
  }
  .st-key-help_page .np-help-support,
  .st-key-help_page .np-help-links {
    display: none !important;
  }
  .np-mob-help-cta {
    margin-top: 1rem;
    padding: 1rem;
    border-radius: 1rem;
    background: rgba(229, 238, 255, 0.65);
    border: 1px solid rgba(199, 196, 215, 0.35);
  }
  .np-mob-help-cta h3 {
    margin: 0 0 0.35rem 0;
    font-size: 1rem;
    font-weight: 600;
  }
  .np-mob-help-cta p {
    margin: 0 0 0.75rem 0;
    font-size: 0.8125rem;
    color: var(--np-on-surface-variant);
    line-height: 1.45;
  }
  .np-mob-help-cta-actions {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
  }
  .np-mob-help-cta-primary,
  .np-mob-help-cta-secondary {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.45rem;
    min-height: 2.75rem;
    border-radius: 0.75rem;
    font-size: 0.875rem;
    font-weight: 600;
  }
  .np-mob-help-cta-primary {
    background: var(--np-primary);
    color: #fff;
  }
  .np-mob-help-cta-secondary {
    background: #fff;
    border: 1px solid var(--np-outline-variant);
    color: var(--np-on-surface);
  }

  /* Settings mobile — settings_mobile */
  html.np-is-mobile .stApp:has(.st-key-settings_page) .np-support-header {
    margin-bottom: 0.65rem !important;
  }
  .st-key-settings_page .np-support-header {
    margin-bottom: 0.65rem !important;
  }
  .st-key-settings_page .np-support-title {
    font-size: 1.35rem !important;
    line-height: 1.2 !important;
    margin-bottom: 0.25rem !important;
  }
  .st-key-settings_page .np-support-sub {
    font-size: 0.8125rem !important;
    line-height: 1.45 !important;
    max-width: 100% !important;
  }
  .st-key-settings_page > [data-testid="stVerticalBlock"] {
    gap: 0.75rem !important;
  }
  .st-key-settings_page [data-testid="column"] {
    width: 100% !important;
    flex: 1 1 100% !important;
    padding-left: 0 !important;
    padding-right: 0 !important;
  }
  .st-key-settings_page .st-key-org_config_locked {
    padding: 0.875rem 0.75rem !important;
    margin-bottom: 0.75rem !important;
  }
  .st-key-settings_page .st-key-org_config_locked > div[data-testid="stVerticalBlock"] {
    min-height: 13.5rem !important;
  }
  .st-key-settings_page .np-locked-overlay {
    border-radius: 0.85rem !important;
    padding: 0.5rem !important;
  }
  .st-key-settings_page .np-locked-overlay-card {
    max-width: 15.5rem !important;
    padding: 1rem 0.85rem 0.9rem 0.85rem !important;
  }
  .st-key-settings_page .np-locked-icon-ring {
    width: 2.85rem !important;
    height: 2.85rem !important;
    margin-bottom: 0.65rem !important;
  }
  .st-key-settings_page .np-locked-icon-ring .material-symbols-outlined {
    font-size: 1.35rem !important;
  }
  .st-key-settings_page .np-locked-title {
    font-size: 0.95rem !important;
    margin-bottom: 0.35rem !important;
  }
  .st-key-settings_page .np-locked-message {
    font-size: 0.75rem !important;
    line-height: 1.45 !important;
  }
  .st-key-settings_page .np-section-card-head {
    margin-bottom: 0.65rem !important;
  }
  .st-key-settings_page .np-glass-card,
  .st-key-settings_page .np-ai-mode-card {
    border-radius: 0.85rem !important;
    border: 1px solid rgba(199, 196, 215, 0.4) !important;
    background: rgba(255, 255, 255, 0.85) !important;
    padding: 0.875rem 0.75rem !important;
    margin-top: 0 !important;
    margin-bottom: 0.75rem !important;
  }
  .st-key-settings_page div[data-testid="stForm"] {
    padding: 0 !important;
    margin: 0 !important;
  }
  .st-key-settings_page [data-testid="stTextInput"] {
    margin-bottom: 0.35rem !important;
  }
  .st-key-settings_page [data-testid="stTextInput"] label p,
  .st-key-settings_page [data-testid="stTextArea"] label p {
    margin-bottom: 0.25rem !important;
  }
  .st-key-settings_page .np-system-health-bar {
    margin-top: 0.5rem !important;
    padding: 0.75rem !important;
  }
  .st-key-settings_page [data-testid="stElementContainer"]:has(.np-support-header),
  .st-key-settings_page [data-testid="stMarkdownContainer"]:has(.np-support-header) {
    margin: 0 !important;
    padding: 0 !important;
  }
  .np-mob-settings-section-head {
    display: flex;
    align-items: center;
    gap: 0.45rem;
    margin: 0.5rem 0 0.65rem 0.15rem;
  }
  .np-mob-settings-section-head h3 {
    margin: 0;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    color: var(--np-on-surface);
  }
  .np-mob-settings-section-head .material-symbols-outlined {
    font-size: 1.125rem;
    color: var(--np-primary);
  }

  /* Account mobile — account_mobile */
  .st-key-account_page .np-support-header,
  .st-key-account_page .np-account-profile {
    display: none !important;
  }
  .np-mob-account-profile {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    gap: 0.65rem;
    margin-bottom: 0.75rem !important;
  }
  .np-mob-account-avatar-ring {
    position: relative;
  }
  .np-mob-account-avatar {
    width: 6rem;
    height: 6rem;
    border-radius: 999px;
    padding: 3px;
    background: linear-gradient(135deg, var(--np-primary), var(--np-secondary));
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .np-mob-account-avatar .material-symbols-outlined {
    width: calc(100% - 6px);
    height: calc(100% - 6px);
    border-radius: 999px;
    background: #fff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2.5rem;
    color: var(--np-primary);
  }
  .np-mob-account-online {
    position: absolute;
    bottom: 0.2rem;
    right: 0.2rem;
    width: 1.1rem;
    height: 1.1rem;
    background: #22c55e;
    border: 3px solid #fff;
    border-radius: 999px;
  }
  .np-mob-account-profile h1 {
    margin: 0;
    font-family: 'Geist', sans-serif;
    font-size: 1.25rem;
    font-weight: 500;
  }
  .np-mob-account-role {
    display: inline-flex;
    padding: 0.25rem 0.75rem;
    border-radius: 999px;
    background: rgba(96, 99, 238, 0.1);
    border: 1px solid rgba(96, 99, 238, 0.2);
    color: var(--np-primary);
    font-size: 0.8125rem;
    font-weight: 500;
  }
  .st-key-account_page [data-testid="column"] {
    width: 100% !important;
    flex: 1 1 100% !important;
  }
  .st-key-account_page .np-glass-card {
    border-radius: 0.85rem !important;
  }
  .st-key-account_page .np-account-danger {
    border-left: 4px solid rgba(186, 26, 26, 0.5) !important;
    padding-left: 0.65rem !important;
  }
}

/* Mobile onboarding — tight top spacing (html.np-is-mobile from layout JS) */
html.np-is-mobile .stApp:has(.st-key-onboarding_page) [data-testid="stMain"] .block-container,
html.np-is-mobile .stApp:has(.st-key-onboarding_page) [data-testid="stMainBlockContainer"] {
  padding-top: 0 !important;
}
html.np-is-mobile .stApp:has(.st-key-onboarding_page) .st-key-onboarding_page [data-testid="stVerticalBlock"] {
  gap: 0 !important;
  row-gap: 0 !important;
}
html.np-is-mobile .stApp:has(.st-key-onboarding_page) .st-key-volunteer_hero_shell,
html.np-is-mobile .stApp:has(.st-key-onboarding_page) .np-onboarding-v2-hero,
html.np-is-mobile .stApp:has(.st-key-onboarding_page) .st-key-onboarding_page [data-testid="stElementContainer"]:has(.np-onboarding-bg-blob) {
  display: none !important;
  height: 0 !important;
  min-height: 0 !important;
  max-height: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  overflow: hidden !important;
  visibility: hidden !important;
}
html.np-is-mobile .stApp:has(.st-key-onboarding_page) .st-key-onboarding_mobile_chat .np-mob-onboarding-chat,
html.np-is-mobile .stApp:has(.st-key-onboarding_page) .np-mob-onboarding-chat {
  margin-top: 0 !important;
  margin-bottom: 0.75rem !important;
}
html.np-is-mobile [data-testid="stMain"] .block-container > .stElementContainer:has(.st-key-np_sidebar_chevron),
html.np-is-mobile [data-testid="stMainBlockContainer"] > .stElementContainer:has(.st-key-np_sidebar_chevron),
html.np-is-mobile .stApp:has(.st-key-onboarding_page) [data-testid="stMain"] .block-container > .stElementContainer:has(.st-key-np_sidebar_chevron),
html.np-is-mobile .stApp:has(.st-key-onboarding_page) [data-testid="stMainBlockContainer"] > .stElementContainer:has(.st-key-np_sidebar_chevron) {
  height: 0 !important;
  min-height: 0 !important;
  margin: 0 !important;
  padding: 0 !important;
  overflow: visible !important;
}
html.np-is-mobile .stApp:has(.st-key-onboarding_page) .st-key-onboarding_page,
html.np-is-mobile .stApp:has(.st-key-onboarding_page) .st-key-onboarding_mobile_chat,
html.np-is-mobile .stApp:has(.st-key-onboarding_page) .st-key-volunteer_form_shell {
  margin-top: 0 !important;
  padding-top: 0 !important;
}

@media (min-width: 769px) {
  html:not(.np-is-mobile) .np-mob-onboarding-chat,
  html:not(.np-is-mobile) .np-mob-onboarding-dock,
  html:not(.np-is-mobile) .st-key-onboarding_mobile_chat,
  .np-mob-step-head,
  .np-mob-admin-head,
  .np-mob-candidate-card,
  .np-mob-admin-bento,
  .np-mob-task-status,
  .np-mob-match-card,
  .np-mob-help-hero,
  .np-mob-help-cta,
  .np-mob-account-profile,
  .np-mob-settings-section-head {
    display: none !important;
  }
  html:not(.np-is-mobile) .st-key-volunteer_hero_shell {
    display: block !important;
  }
  .st-key-volunteer_form_shell {
    background: #ffffff !important;
    border: 1px solid var(--np-outline-variant) !important;
    box-shadow: 0 4px 24px rgba(70, 72, 212, 0.08) !important;
    padding: 1.1rem 1.35rem 1rem 1.35rem !important;
  }
  .st-key-volunteer_form_card {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
  }
  .np-onboarding-v2-form-header {
    display: block !important;
  }
  .st-key-help_page .np-support-header,
  .st-key-help_page .np-help-hero,
  .st-key-help_page .np-help-support,
  .st-key-help_page .np-help-links,
  .st-key-account_page .np-support-header,
  .st-key-account_page .np-account-profile,
  .st-key-admin_page .np-page-title,
  .st-key-admin_page .np-page-sub,
  .st-key-tasks_page .np-page-title,
  .st-key-tasks_page .np-page-sub,
  .st-key-tasks_page .np-ai-card {
    display: block !important;
  }
}
</style>
<script>
(function () {
  let npLastRouteKey = sessionStorage.getItem("np_route_key") || "";

  function npRouteKey(win) {
    const loc = win.location;
    return loc.pathname + loc.search + loc.hash;
  }

  function npClearSidebarNavHide() {
    try {
      sessionStorage.removeItem("np_sidebar_nav_hide");
    } catch (e) {
      /* ignore */
    }
  }

  function npMarkSidebarNavHide() {
    try {
      sessionStorage.setItem("np_sidebar_nav_hide", "1");
    } catch (e) {
      /* ignore */
    }
  }

  function npShouldForceHideSidebar(isMobile) {
    if (!isMobile) {
      return false;
    }
    try {
      return sessionStorage.getItem("np_sidebar_nav_hide") === "1";
    } catch (e) {
      return false;
    }
  }

  function npSyncMobileQueryFlag(mobile) {
    try {
      const win = window.parent && window.parent.location ? window.parent : window;
      const url = new URL(win.location.href);
      const want = mobile ? "1" : "0";
      if (url.searchParams.get("np_m") !== want) {
        url.searchParams.set("np_m", want);
        win.history.replaceState({}, "", url);
      }
    } catch (e) {
      /* ignore */
    }
  }

  function npSwapSidebarFlags(doc, hidden) {
    doc.querySelector(".np-sidebar-visible-flag")?.remove();
    doc.querySelector(".np-sidebar-hidden-flag")?.remove();
    const flag = doc.createElement("div");
    flag.className = hidden ? "np-sidebar-hidden-flag" : "np-sidebar-visible-flag";
    flag.setAttribute("aria-hidden", "true");
    const anchor =
      doc.querySelector('[data-testid="stMain"] .block-container') ||
      doc.querySelector('[data-testid="stMain"]') ||
      doc.body;
    if (anchor) {
      anchor.insertBefore(flag, anchor.firstChild || null);
    }
  }

  function npAppLayoutFix() {
    try {
      const doc = window.parent && window.parent.document ? window.parent.document : document;

      const html = doc.documentElement;
      const body = doc.body;
      const app = doc.querySelector(".stApp");
      const appView = doc.querySelector('[data-testid="stAppViewContainer"]');
      const sidebar = doc.querySelector('[data-testid="stSidebar"]');
      const main =
        doc.querySelector('[data-testid="stMain"]') ||
        doc.querySelector("section.main");
      const win = window.parent && window.parent.location ? window.parent : window;
      const routeKey = npRouteKey(win);
      const viewportW =
        win.innerWidth ||
        window.innerWidth ||
        doc.documentElement.clientWidth ||
        (app && app.clientWidth) ||
        1024;
      const isMobile = viewportW <= 768;
      const isOnboarding = !!doc.querySelector(".st-key-onboarding_page");
      doc.documentElement.classList.toggle("np-is-mobile", isMobile);
      npSyncMobileQueryFlag(isMobile);
      if (npLastRouteKey && routeKey !== npLastRouteKey && isMobile) {
        npMarkSidebarNavHide();
        npSwapSidebarFlags(doc, true);
      }
      npLastRouteKey = routeKey;
      try {
        sessionStorage.setItem("np_route_key", routeKey);
      } catch (e) {
        /* ignore */
      }
      if (npShouldForceHideSidebar(isMobile)) {
        npSwapSidebarFlags(doc, true);
      } else if (!isMobile) {
        npClearSidebarNavHide();
      }

      function npSyncMobileBackdrop(show) {
        var existing = doc.getElementById("np-mobile-sidebar-backdrop");
        if (!show) {
          if (existing) existing.remove();
          return;
        }
        if (!existing) {
          existing = doc.createElement("div");
          existing.id = "np-mobile-sidebar-backdrop";
          existing.className = "np-mobile-sidebar-backdrop";
          existing.setAttribute("aria-hidden", "true");
          doc.body.appendChild(existing);
        }
      }

      if (isOnboarding) {
        [html, body].forEach(function (el) {
          if (!el) return;
          el.style.setProperty("height", "auto", "important");
          el.style.setProperty("overflow-x", "hidden", "important");
          el.style.setProperty("overflow-y", "auto", "important");
        });
        if (app) {
          app.style.setProperty("height", "auto", "important");
          app.style.setProperty("min-height", "100vh", "important");
          app.style.setProperty("max-height", "none", "important");
          app.style.setProperty("overflow-x", "hidden", "important");
          app.style.setProperty("overflow-y", "auto", "important");
        }
        if (appView) {
          appView.style.setProperty("height", "auto", "important");
          appView.style.setProperty("min-height", "100vh", "important");
          appView.style.setProperty("max-height", "none", "important");
          appView.style.setProperty("overflow", "visible", "important");
        }
      } else {
        [html, body].forEach(function (el) {
          if (!el) return;
          el.style.setProperty("height", "100%", "important");
          el.style.setProperty("overflow", "hidden", "important");
        });

        if (app) {
          app.style.setProperty("height", "100vh", "important");
          app.style.setProperty("max-height", "100vh", "important");
          app.style.setProperty("overflow", "hidden", "important");
        }
        if (appView) {
          appView.style.setProperty("height", "100vh", "important");
          appView.style.setProperty("max-height", "100vh", "important");
          appView.style.setProperty("overflow", "hidden", "important");
        }
      }

      const hidden = !!doc.querySelector(".np-sidebar-hidden-flag");
      const mobileSidebarPx = isMobile ? Math.min(280, Math.round(viewportW * 0.88)) : 280;
      let sidebarW = hidden ? 0 : 280;
      if (isMobile) {
        sidebarW = 0;
        doc.documentElement.style.setProperty("--np-mobile-sidebar-width", mobileSidebarPx + "px");
        doc.documentElement.style.setProperty(
          "--np-mobile-chevron-left",
          Math.max(12, mobileSidebarPx - 34) + "px"
        );
      } else {
        doc.documentElement.style.removeProperty("--np-mobile-sidebar-width");
        doc.documentElement.style.removeProperty("--np-mobile-chevron-left");
      }

      if (sidebar && !hidden) {
        sidebar.style.setProperty("position", "fixed", "important");
        sidebar.style.setProperty("top", "0", "important");
        sidebar.style.setProperty("left", "0", "important");
        sidebar.style.setProperty("width", (isMobile ? mobileSidebarPx : 280) + "px", "important");
        sidebar.style.setProperty("min-width", (isMobile ? mobileSidebarPx : 280) + "px", "important");
        sidebar.style.setProperty("max-width", (isMobile ? mobileSidebarPx : 280) + "px", "important");
        sidebar.style.setProperty("height", "100dvh", "important");
        sidebar.style.setProperty("max-height", "100dvh", "important");
        sidebar.style.setProperty("overflow-x", "hidden", "important");
        sidebar.style.setProperty("overflow-y", "auto", "important");
        sidebar.style.setProperty("z-index", isMobile ? "1005" : "998", "important");
        sidebar.style.setProperty("transform", isMobile ? "translateX(0)" : "none", "important");
        sidebar.style.setProperty("visibility", "visible", "important");
        sidebar.style.setProperty("opacity", "1", "important");
        sidebar.style.setProperty("pointer-events", "auto", "important");
        if (isMobile) {
          sidebar.style.setProperty(
            "box-shadow",
            "4px 0 32px rgba(19, 27, 46, 0.2)",
            "important"
          );
        }
      } else if (sidebar) {
        sidebar.style.setProperty("width", "0", "important");
        sidebar.style.setProperty("min-width", "0", "important");
        sidebar.style.setProperty("max-width", "0", "important");
        sidebar.style.setProperty(
          "transform",
          isMobile ? "translateX(-105%)" : "none",
          "important"
        );
        sidebar.style.setProperty("visibility", "hidden", "important");
        sidebar.style.setProperty("pointer-events", "none", "important");
      }

      npSyncMobileBackdrop(isMobile && !hidden);

      if (isMobile && sidebar) {
        doc.querySelectorAll(
          '[data-testid="stSidebar"] a[href], [data-testid="stSidebar"] [data-testid="stPageLink"]'
        ).forEach(function (el) {
          if (el.dataset.npNavBound) {
            return;
          }
          el.dataset.npNavBound = "1";
          el.addEventListener(
            "click",
            function () {
              npMarkSidebarNavHide();
              npSwapSidebarFlags(doc, true);
            },
            true
          );
        });
      }

      const chevron = doc.querySelector(".st-key-np_sidebar_chevron");
      if (chevron && !chevron.dataset.npNavBound) {
        chevron.dataset.npNavBound = "1";
        chevron.addEventListener(
          "click",
          function () {
            npClearSidebarNavHide();
          },
          true
        );
      }
      if (chevron) {
        chevron.style.setProperty("position", "fixed", "important");
        chevron.style.setProperty("top", isMobile ? "10px" : "12px", "important");
        chevron.style.setProperty("z-index", "1010", "important");
        chevron.style.setProperty("pointer-events", "auto", "important");
        chevron.style.setProperty("visibility", "visible", "important");
        chevron.style.setProperty("opacity", "1", "important");
        if (isMobile) {
          if (hidden) {
            chevron.style.setProperty("left", "12px", "important");
            chevron.style.setProperty("transform", "none", "important");
          } else {
            chevron.style.setProperty("left", Math.max(12, mobileSidebarPx - 34) + "px", "important");
            chevron.style.setProperty("transform", "none", "important");
          }
        } else if (hidden) {
          chevron.style.setProperty("left", "12px", "important");
          chevron.style.setProperty("transform", "none", "important");
        } else {
          chevron.style.setProperty("left", "calc(280px - 10px)", "important");
          chevron.style.setProperty("transform", "translateX(-100%)", "important");
        }
      }

      if (main) {
        main.style.setProperty("margin-left", isMobile ? "0" : sidebarW + "px", "important");
        main.style.setProperty(
          "margin-right",
          "0",
          "important"
        );
        main.style.setProperty(
          "width",
          isMobile || !sidebarW ? "100%" : "calc(100% - " + sidebarW + "px)",
          "important"
        );
        main.style.setProperty("max-width", "100%", "important");
        if (isOnboarding) {
          main.style.setProperty("height", "auto", "important");
          main.style.setProperty("min-height", "100vh", "important");
          main.style.setProperty("max-height", "none", "important");
          main.style.setProperty("overflow", "visible", "important");
        } else {
          main.style.setProperty("height", "100vh", "important");
          main.style.setProperty("max-height", "100vh", "important");
          main.style.setProperty("overflow-y", "auto", "important");
          main.style.setProperty("overflow-x", "hidden", "important");
        }
      }

      if (isMobile && appView) {
        appView.style.setProperty("padding-left", "0", "important");
        appView.style.setProperty("padding-right", "0", "important");
        appView.style.setProperty("width", "100%", "important");
        appView.style.setProperty("max-width", "100%", "important");
      }

      if (isMobile) {
        doc.querySelectorAll(
          '[data-testid="stMainBlockContainer"], [data-testid="stMain"] .block-container'
        ).forEach(function (el) {
          el.style.setProperty("padding-top", "0", "important");
          el.style.setProperty("padding-left", "0.625rem", "important");
          el.style.setProperty("padding-right", "0.625rem", "important");
          el.style.setProperty("width", "100%", "important");
          el.style.setProperty("max-width", "100%", "important");
          el.style.setProperty("margin-left", "0", "important");
          el.style.setProperty("margin-right", "0", "important");
        });

        doc.querySelectorAll(
          '[data-testid="stMain"] .block-container > .stElementContainer:has(.st-key-np_sidebar_chevron), ' +
          '[data-testid="stMainBlockContainer"] > .stElementContainer:has(.st-key-np_sidebar_chevron)'
        ).forEach(function (wrap) {
          wrap.style.setProperty("height", "0", "important");
          wrap.style.setProperty("min-height", "0", "important");
          wrap.style.setProperty("margin", "0", "important");
          wrap.style.setProperty("padding", "0", "important");
          wrap.style.setProperty("overflow", "visible", "important");
        });

        doc.querySelectorAll(
          ".np-page-header, .np-support-header, .np-mob-admin-head, .np-mob-help-hero, " +
          ".np-mob-task-status, .np-mob-account-profile, .np-hero, .np-mob-onboarding-chat"
        ).forEach(function (el) {
          el.style.setProperty("margin-top", "0", "important");
        });

        doc.querySelectorAll('[data-testid="column"]').forEach(function (el) {
          if (
            el.closest(".st-key-manual_row_onboarding_skills") ||
            el.closest(".st-key-manual_row_onboarding_interests") ||
            el.closest(".st-key-availability_cards")
          ) {
            return;
          }
          el.style.setProperty("width", "100%", "important");
          el.style.setProperty("min-width", "100%", "important");
          el.style.setProperty("max-width", "100%", "important");
          el.style.setProperty("flex", "1 1 100%", "important");
        });
      }

      if (isOnboarding && isMobile) {
        doc.querySelectorAll(".st-key-volunteer_hero_shell, .np-onboarding-v2-hero").forEach(function (el) {
          el.style.setProperty("display", "none", "important");
          el.style.setProperty("height", "0", "important");
          el.style.setProperty("min-height", "0", "important");
          el.style.setProperty("margin", "0", "important");
          el.style.setProperty("padding", "0", "important");
        });
      }

      doc.querySelectorAll(
        '[data-testid="stMain"] > div, [data-testid="stMain"] .block-container, section.main > div, section.main .block-container'
      ).forEach(function (el) {
        el.style.setProperty("height", "auto", "important");
        el.style.setProperty("max-height", "none", "important");
        el.style.setProperty("overflow", "visible", "important");
      });
    } catch (e) {
      /* ignore */
    }
  }

  npAppLayoutFix();
  window.addEventListener("resize", npAppLayoutFix);
  window.addEventListener("hashchange", npAppLayoutFix);
  window.addEventListener("popstate", npAppLayoutFix);
  window.addEventListener("pageshow", npAppLayoutFix);
  setInterval(npAppLayoutFix, 600);
})();
</script>
"""


def inject_theme() -> None:
    render_html(STITCH_CSS)
