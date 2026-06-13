---
name: Luminous Intelligence
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#464554'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#767586'
  outline-variant: '#c7c4d7'
  surface-tint: '#494bd6'
  primary: '#4648d4'
  on-primary: '#ffffff'
  primary-container: '#6063ee'
  on-primary-container: '#fffbff'
  inverse-primary: '#c0c1ff'
  secondary: '#6b38d4'
  on-secondary: '#ffffff'
  secondary-container: '#8455ef'
  on-secondary-container: '#fffbff'
  tertiary: '#00628d'
  on-tertiary: '#ffffff'
  tertiary-container: '#007cb1'
  on-tertiary-container: '#fcfcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c0c1ff'
  on-primary-fixed: '#07006c'
  on-primary-fixed-variant: '#2f2ebe'
  secondary-fixed: '#e9ddff'
  secondary-fixed-dim: '#d0bcff'
  on-secondary-fixed: '#23005c'
  on-secondary-fixed-variant: '#5516be'
  tertiary-fixed: '#c9e6ff'
  tertiary-fixed-dim: '#89ceff'
  on-tertiary-fixed: '#001e2f'
  on-tertiary-fixed-variant: '#004c6e'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display-lg:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
  mono-xs:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  container-max: 1440px
  gutter: 24px
  margin-desktop: 40px
  margin-mobile: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
The brand personality is **intelligent, empathetic, and precision-engineered**. It balances the technical rigor of a data-driven SaaS platform with the humanitarian warmth of an NGO mission. The visual direction is a fusion of **Minimalism** and **Glassmorphism**, taking cues from industry-leading utility tools to create a "Pro-sumer" feel that maximizes volunteer productivity without emotional coldness.

The UI should evoke a sense of clarity and focus. High-density information is tempered by generous white space and subtle "AI glow" effects—soft, directional gradients that highlight active intelligence or suggested actions. The aesthetic is "Work-Optimized": everything feels fast, responsive, and premium.

## Colors
The palette is rooted in a "Crisp White" ecosystem to maintain high legibility and a sense of cleanliness. 

- **Primary & Secondary:** A duo of Indigo (#6366f1) and Violet (#8b5cf6) provides the "Intelligence" signature. These are used for primary actions and active states.
- **Accents:** A soft Sky Blue (#0ea5e9) is used sparingly for data visualizations and secondary AI-driven highlights.
- **Neutrals:** We utilize a Slate Gray scale. Text primary sits at a deep Slate 900 for high contrast, while secondary metadata uses Slate 500.
- **Glows:** Use low-opacity versions of the primary and secondary colors (5-10% alpha) for background "blobs" and glassmorphic halos to signify AI-augmented areas of the dashboard.

## Typography
The typography system prioritizes technical clarity and modern aesthetics.

- **Headlines:** Use **Geist** for a sharp, developer-centric look that feels modern and precise. Keep tracking tight on larger sizes to maintain the "Linear" aesthetic.
- **Body:** **Inter** is used for all long-form reading and interface labels due to its exceptional legibility and neutral tone.
- **Monospace:** **JetBrains Mono** is reserved for metadata, ID tags, and AI confidence scores, providing a subtle "under-the-hood" technical feel to the volunteer intelligence data.

## Layout & Spacing
The layout follows a **Fixed-Fluid Hybrid** model. The sidebar remains fixed (240px-280px), while the main content area occupies a fluid space up to a 1440px max-width to prevent line-length issues.

- **Grid:** Use a 12-column grid for the dashboard content.
- **Rhythm:** An 8px base unit drives all spacing.
- **Mobile:** On mobile, the sidebar collapses into a bottom navigation bar or a hamburger menu, and horizontal margins shrink to 16px. Elements should transition to a single-column stack.

## Elevation & Depth
Depth is created through **Glassmorphism** and **Tonal Layers** rather than heavy shadows.

- **Surface Levels:** 
  - Level 0: Background (Slate 50 or pure white).
  - Level 1: Cards and main containers (White with a 1px Slate 100 border).
  - Level 2: Overlays and modals (White with 80% opacity, 12px backdrop blur, and a subtle 1px border at 20% primary color).
- **Shadows:** Use a single "Ambient Glow" for floating elements: `0 8px 30px rgba(0,0,0,0.04)`. Avoid heavy black shadows; instead, use a hint of the primary color in the shadow for active AI components.

## Shapes
The design system uses **Rounded** geometry to maintain an approachable feel.

- **Standard Elements:** (Inputs, Buttons, Cards) use a 0.5rem (8px) radius.
- **Large Containers:** Use 1rem (16px) for main dashboard panels to create a nested, modular look.
- **Pill Elements:** Status badges and search bars should use fully rounded (pill) corners to contrast against the structured grid of the cards.

## Components
- **Buttons:** Primary buttons use a subtle gradient (Indigo to Violet) with white text. Secondary buttons are ghost-style with a Slate 200 border.
- **Inputs:** High-contrast fields with a 1px Slate 200 border that transforms into a 1px Indigo border with a soft 2px Indigo outer glow on focus.
- **Cards:** White background, 1px border (#F1F5F9). For AI-recommended volunteers or tasks, add a subtle top-border gradient of Indigo to Violet.
- **Chips/Badges:** Use low-saturation background tints (e.g., Indigo 50) with high-saturation text (Indigo 700). 
- **Lists:** Clean, border-bottom only (Slate 50), with generous vertical padding (12px-16px).
- **AI Glow Elements:** For "Intelligence" features, use a "Scanner" animation or a soft radial gradient behind the component to signify active processing.
- **Status Indicators:** Use small, solid dots with a "ping" animation for live volunteer activity.