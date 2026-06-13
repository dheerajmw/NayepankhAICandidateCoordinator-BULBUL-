---
name: Coordinated Desktop Intelligence
colors:
  surface: '#faf8ff'
  surface-dim: '#d2d9f4'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3ff'
  surface-container: '#eaedff'
  surface-container-high: '#e2e7ff'
  surface-container-highest: '#dae2fd'
  on-surface: '#131b2e'
  on-surface-variant: '#434655'
  inverse-surface: '#283044'
  inverse-on-surface: '#eef0ff'
  outline: '#737686'
  outline-variant: '#c3c6d7'
  surface-tint: '#0053db'
  primary: '#004ac6'
  on-primary: '#ffffff'
  primary-container: '#2563eb'
  on-primary-container: '#eeefff'
  inverse-primary: '#b4c5ff'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#943700'
  on-tertiary: '#ffffff'
  tertiary-container: '#bc4800'
  on-tertiary-container: '#ffede6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b4c5ff'
  on-primary-fixed: '#00174b'
  on-primary-fixed-variant: '#003ea8'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#ffdbcd'
  tertiary-fixed-dim: '#ffb596'
  on-tertiary-fixed: '#360f00'
  on-tertiary-fixed-variant: '#7d2d00'
  background: '#faf8ff'
  on-background: '#131b2e'
  surface-variant: '#dae2fd'
typography:
  display-lg:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-md:
    fontFamily: Geist
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Geist
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  headline-md:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-lg:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  sidebar-width: 280px
  container-max-width: 1440px
  gutter-desktop: 24px
  gutter-tablet: 16px
  margin-page: 48px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 24px
---

## Brand & Style
The design system is engineered for high-utility administrative environments where clarity and rapid task execution are paramount. Targeting organizational leads and volunteer coordinators, the aesthetic leans into **Corporate Minimalism** with a technical edge. 

The interface evokes a sense of calm authority through generous whitespace, high-contrast typography, and a systematic approach to information density. By leveraging "Geist" as the core typeface, the system adopts a developer-adjacent precision that feels modern and reliable. The emotional response is one of organized efficiency—removing visual noise to allow the coordinator to focus on people and logistics.

## Colors
The palette is rooted in a professional "Light Mode" foundation. The primary color (#2563eb) is used purposefully for action-oriented elements, focus states, and progress indicators. 

- **Primary**: Used for core CTAs and active navigation states.
- **Secondary**: A muted slate used for sub-headers and less critical information.
- **Neutral**: Deep charcoal for maximum legibility in body text.
- **Background**: A very soft grey-blue to reduce eye strain on large desktop displays compared to pure white.
- **Surface**: Pure white is reserved for cards and the main content area to create clear "islands" of information.

## Typography
This design system utilizes the **Geist** font family across all roles to maintain a unified, technical character. The desktop scale is expanded to accommodate larger viewing distances and higher information density.

- **Display Scales**: Reserved for dashboard overviews and primary page titles. They use tighter letter-spacing and heavier weights to anchor the page.
- **Body Text**: Optimized for long-form reading of volunteer bios and event descriptions, using a comfortable 16px base.
- **Labels**: Used for table headers and metadata, providing clear categorization without competing with primary content.

## Layout & Spacing
The layout follows a **Fixed-Fluid Hybrid** model optimized for desktop productivity.

- **Sidebar Navigation**: A persistent 280px left-hand sidebar houses the primary navigation. It remains fixed while the main content area scrolls.
- **Gutter Strategy**: In the main content area, gutters transition from 12px (mobile/compact) to 24px (desktop) to provide breathing room between data columns and cards.
- **Grid**: A 12-column grid is used within the main content area for dashboard widgets and list views. 
- **Margins**: A generous 48px outer margin ensures the UI feels "contained" and premium on ultra-wide monitors.

## Elevation & Depth
The system uses **Tonal Layering** supplemented by extremely subtle shadows to define hierarchy.

- **Level 0 (Background)**: The slate-tinted background.
- **Level 1 (Cards/Sidebar)**: Pure white surfaces with a 1px border (#e2e8f0). No shadow.
- **Level 2 (Popovers/Modals)**: Raised surfaces using a soft, neutral shadow (0px 4px 12px rgba(0,0,0,0.05)) to indicate interactivity and temporary state.
- **Interactive States**: Hovering over a card should not increase shadow depth but rather change the border color to the primary blue, maintaining a flat, crisp professional look.

## Shapes
The design system utilizes a **ROUND_EIGHT** philosophy, translating to a base 0.5rem (8px) radius. This provides a balance between the clinical feel of sharp corners and the overly casual feel of high-radius curves.

- **Standard Elements**: Buttons, input fields, and cards use the base 8px radius.
- **Large Containers**: Modals or prominent dashboard panels may scale to 16px (rounded-lg) to soften the visual impact of large blocks.
- **Selection Indicators**: Active states in the sidebar use a 6px radius to sit comfortably within the 8px padded container.

## Components
Consistent component styling ensures the interface feels like a professional tool:

- **Buttons**: Primary buttons are solid #2563eb with white text. Secondary buttons are ghost-style with a 1px border. All buttons use 14px SemiBold text.
- **Sidebar Nav**: Vertical list items with 12px internal padding. Active state is indicated by a light blue background (#eff6ff) and a 4px primary-colored left "accent" bar.
- **Input Fields**: 40px height for desktop. Uses a subtle grey border that turns primary blue on focus. 
- **Data Tables**: Minimalist approach. No vertical borders; only horizontal 1px dividers. Header text uses `label-sm` with a light grey background.
- **Cards**: Defined by an 8px radius and a 1px light border. Used to group volunteer stats or event details.
- **Status Chips**: Small, high-contrast pills (e.g., "Active", "Pending") with 50% opacity backgrounds of their respective status colors (Success Green, Warning Amber, etc.).