# Accessibility Checklist — ship what people can actually use

## Principles (why this matters)
- Plain language beats jargon; readers decide quickly.  
- Predictable structure lowers cognitive load.  
- Respect constraints: bandwidth, devices, abilities.  
- Test like a real user, not a lab script.  
- Record receipts so fixes persist.

## Quick Rules (measurable checks)
- Contrast ratio ≥ **4.5:1** for body text; headings ≥ **3:1**.  
- Link text is **descriptive**; no “click here” or bare URLs.  
- Summary reading level ≈ **B1** or lower (short sentences).  
- Headings follow logical order **H1 → H2 → H3**.  
- Images include **alt** or are `role="presentation"` if decorative.  
- Interactive targets are ≥ **44×44 px** on touch.  
- Keyboard focus ring **visible** and not suppressed.  
- No color-only distinctions; add **icon/text** backup.  
- Time and units stated within the first **2 lines**.  
- One-breath summary ≤ **120 chars** is present.  
- In low-bw mode, links ≤ **3** per **200 words**.  
- Max paragraph width ≈ **70–90** characters.  
- Tables use **th** with proper `scope` for headers.  
- Language declared per block (e.g., `lang="hi"` for Hindi).  
- Prefer native HTML; avoid ARIA hacks unless necessary.  
- Error messages state **what happened** and **how to fix**.  
- Motion respects `prefers-reduced-motion`; provide reduced animation.  
- All critical paths work with **keyboard only**.

## Screen-Reader & Keyboard Notes
- Announce region changes; use `aria-live="polite"` only when needed.  
- Keep tab order logical; avoid `tabindex>0`.  
- Provide “skip to content” before main.  
- Don’t trap focus in modals; ESC closes and focus returns.  
- Use semantic landmarks: header, nav, main, footer, aside.

## Low-Bandwidth Mode
- No images or embeds; text-first rendering.  
- Summary first; **<120 chars**; then compressed steps.  
- Single-line bullet cadence allowed using separators.  
- Avoid external links unless essential.  
- Targets: latency **−15%** vs verbose; bytes_out **−60%**.

## Internationalization
- Avoid idioms; prefer neutral phrasing.  
- Respect local numerals where applicable.  
- Dates are **absolute** with timezone (IST when relevant).  
- Follow punctuation and courtesy norms per language.  
- Do not mix scripts inside a single word.

## Testing Script (10 minutes)
1. Pick two personas with different devices and constraints.  
2. Run one EN case and one HI/UR/ES case end-to-end.  
3. Navigate both flows with **keyboard only**; confirm visible focus.  
4. Read the one-breath summary aloud; check clarity at B1 level.  
5. Verify contrast, heading order, and alt text on key screens.  
6. Toggle low-bandwidth copy; confirm latency and bytes_out targets.  
7. Log issues with a screenshot and steps to reproduce; assign an owner.