---
name: molecule-video-creator
description: Use when user asks to create, animate, draw, or generate a video of a molecule, structure, or chemical — including chalk animations, AI-enhanced video, erasing, drawing styles, speed, color, line thickness, direction, or stroke path. Not video-demo-creator (UI screen recordings) or html-video-production (social HTML→MP4). Former skill folder video-creator.
---

# Molecule Video Creator

## Overview

Handles all ChemIllusion video creation via a forced-tool call that extracts fully populated parameters. Always resolve every parameter to a default — never leave fields ambiguous. Present cost and key settings to the user, then offer ≤3 action buttons.

## Video Types

| Type | When | Cost |
|------|------|------|
| **Structure** | Default — "animate", "draw", "chalk", "video" | Free (quota) |
| **AI Video** | "make beautiful", "flux", "AI-enhanced", provider specified | per-frame AI cost (not in this repo) |
| **Artistic Bond** | "bonds", "rope/ribbon/neon bonds", "artistic" | Paid (estimated) |
| **Nomenclature** | "name song", "mnemonic", "pronunciation video" | Paid |
| **Reaction** | "reaction video" | Coming soon |

## Forced-Tool Call Schema

Force a call to `configure_video_parameters` to extract all settings. Every field must resolve to a value.

```json
{
 "name": "configure_video_parameters",
 "parameters": {
 "video_type": "structure",
 "animation_direction": "forward",
 "animation_range_start": 0.2,
 "animation_range_end": 1.0,
 "tool_style": "chalk",
 "molecule_color_key": "chalk_white",
 "line_thickness": "thick",
 "reference_frame_mode": "left_to_right",
 "playback_speed_multiplier": 2,
 "duration_seconds": 1,
 "draw_units_per_frame": 1,
 "ai_provider": "bfl_locked",
 "frame_generation_model": "flux_klein",
 "render_gif": false,
 "user_summary": "Drawing aspirin in chalk, left to right, ~1s"
 }
}
```

## Defaults (use these when user doesn't specify)

| Parameter | Default |
|-----------|---------|
| video_type | structure |
| animation_direction | forward |
| animation_range_start | 0.2 (20%) |
| animation_range_end | 1.0 (100%) |
| tool_style | chalk |
| molecule_color_key | chalk_white |
| line_thickness | thick |
| reference_frame_mode | left_to_right |
| playback_speed_multiplier | 2 |
| duration_seconds | 1 |
| draw_units_per_frame | 1 |
| ai_provider | bfl_locked |
| frame_generation_model | flux_klein |
| render_gif | false |

## Natural Language → Parameter Mapping

### Direction
| User says | Values |
|-----------|--------|
| "reverse", "erase", "disappear", "undraw" | direction=reverse, tool_style=eraser |
| "forward", default | direction=forward |

### Tool Style (Preset)
| User says | tool_style |
|-----------|-----------|
| "chalk", "chalkboard", default | chalk |
| "pencil", "paper", "clean page" | pencil |
| "brush", "easel", "paint" | brush |
| "marker", "whiteboard" | marker |
| "laser", "projector", "pointer" | laser |
| "erase" | eraser (also sets direction=reverse) |
| "no tool", "plain", "bare" | none |

### Stroke Path (reference_frame_mode)
| User says | value |
|-----------|-------|
| "left to right", "LTR", default | left_to_right |
| "right to left", "RTL" | right_to_left |
| "center", "from center", "outward" | center |

### Color (auto-defaults from tool_style; only override if user specifies)
| tool_style | default key | other options |
|-----------|-------------|---------------|
| chalk | chalk_white | chalk_blue, chalk_yellow, chalk_pink |
| laser | projector_cyan | projector_yellow, projector_coral, projector_white |
| marker / eraser | board_black | board_navy, board_green, board_maroon |
| pencil / none | graphite | navy_ink, forest_ink, brick_ink |
| brush | ink_black | ink_navy, ink_green, ink_burgundy |

User color hints: "pink"→chalk_pink, "blue"→chalk_blue/board_navy, "yellow"→chalk_yellow/projector_yellow, "green"→board_green/ink_green

### Line Thickness
| User says | value |
|-----------|-------|
| "thin", "light", "fine" | thin |
| "medium", "normal" | medium |
| "thick", "bold", "heavy", default | thick |

### Speed
| User says | playback_speed_multiplier |
|-----------|--------------------------|
| "slow", "slowly" | 1 |
| "normal", "medium", default | 2 |
| "fast", "quickly" | 3 |

### AI Provider / Model
| User says | ai_provider | frame_generation_model |
|-----------|------------|----------------------|
| "flux", "bfl", "frame-locked", default | bfl_locked | flux_klein |
| "gemini", "nano banana", "nano banana 2" | bfl_locked | gemini-3.1-flash-image-preview |
| "gpt", "openai", "gpt-image" | bfl_locked | gpt-image-2 |
| "bria" | bfl_locked | bria-reimagine |
| "fal", "realtime preview" | fal | flux_klein |
| "experimental", "full-frame" | bfl_experimental | flux_klein |

## AI Video Cost Estimation

**BFL (frame-locked or experimental):** cost scales with frame count (exact per-frame rate not in this repo).

**Fal (realtime):** cost scales with duration (exact per-second rate not in this repo).

**Structure-only:** Free (uses quota)

Show the user an estimated range, not an exact figure.

## User Message Format

After extracting parameters, respond with this pattern:

```
🎬 **[Structure / AI] Video** — [Molecule name or "your molecule"]

Style: [Preset label] · [Color label] · [Thickness] lines
Direction: [Forward/Reverse] · [20]%–[100]% range
Stroke path: [Left-to-right / Right-to-left / Center]
Speed: ×[N] · [N]s duration

[AI only] Model: [Label] · Est. cost: ~$[X.XX]

[1–3 buttons]
```

## UI Buttons (max 3, pick most relevant)

| Button label | When to show |
|-------------|-------------|
| "Reverse direction" | User hasn't specified direction |
| "Change style" | User hasn't specified tool style |
| "Add AI video" | Video is structure-only and user might want AI |
| "Pink chalk" | Chalk style and user hasn't specified color |
| "Try Flux AI" | Default structure video, upgrade available |

Default (no context clues): show only **"Generate"** — don't clutter.

## Parameters NOT to Surface to User

Never ask about these — they are internal:
- `draw_units_per_frame`
- `fps_policy`
- `standard_reference_frame`
- `render_formats` (mp4 always true, gif only if user asks)
- Exact float range values (use 20/40/60/80/100% buckets)

## Brand Design Standards (enforced in all HTML video output)

### 4-color palette

| Name | Hex | Role |
|------|-----|------|
| **Gold** | `#f59e0b` | Brand accent, logo "I", CTAs, feature highlights |
| **White** | `#ffffff` | Primary text, logo base ("Chem"/"llusion") |
| **Blue** | `#0ea5e9` | Interactive elements, URLs, links, progress bars |
| **Red** | `#ef4444` | **Competitor contrast ONLY** — never on ChemIllusion features |

**Retired — never use:** teal `#14b8a6`, green `#22c55e`. Replace with gold or blue.

### Logo rendering

`ChemIllusion` is always rendered as: `Chem` (white) + `I` (gold `#f59e0b`) + `llusion` (white), using **Raleway 800–900**, letter-spacing `-0.02em`.

```jsx
function Logo({ size, color = '#fff', style = {} }) {
 return (
 <span style={{
 fontFamily: "'Raleway', 'Inter', sans-serif",
 fontWeight: 900, letterSpacing: '-0.02em',
 color, fontSize: size, lineHeight: 1, ...style,
 }}>
 Chem<span style={{ color: '#f59e0b' }}>I</span>llusion
 </span>
 );
}
```

Always include `<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Raleway:wght@800;900&display=swap" rel="stylesheet">` in the HTML `<head>`.

### Video font minimums

| Size | Rule |
|------|------|
| 16px | Absolute minimum for any text in exported frames |
| 18px | Preferred for body text |
| 14px | Caption floor — use sparingly |
| 10–13px | **Forbidden** in video content |

Never use `vw`-based font sizes in a 1080px-stage video — convert to fixed px (e.g. `5vw` at 1080px = `54px`).

### QR code display standards

QR code images in video HTML must **always** render square and show only the scannable matrix — never the text label that many QR generators embed above or below.

**Asset generation:** Use Python `qrcode` library with `border=2` and no text. Always save as a square PNG:

```python
import qrcode
from PIL import Image

qr = qrcode.QRCode(version=None, error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=10, border=2)
qr.add_data('https://chemillusion.com/...')
qr.make(fit=True)
img = qr.make_image(fill_color='black', back_color='white').get_image()
w, h = img.size
side = max(w, h)
square = Image.new('RGB', (side, side), 'white')
square.paste(img, ((side-w)//2, (side-h)//2, (side-w)//2+w, (side-h)//2+h))
square.save('qr-name.png')
```

**Rendering in HTML:** Always wrap in a fixed square `div` with `overflow: hidden` and use `objectFit: 'contain'`. This guarantees square display and crops any leftover text padding from older QR assets:

```jsx
<div style={{
 width: 240, height: 240,
 borderRadius: 16, overflow: 'hidden',
 border: '3px solid rgba(245,158,11,0.45)',
 background: '#fff',
 display: 'flex', alignItems: 'center', justifyContent: 'center',
 flexShrink: 0,
}}>
 <img src={QR_IMG} style={{ width: '100%', height: '100%', objectFit: 'contain', display: 'block' }} />
</div>
```

**Never** use `<img src={QR_IMG} style={{ width: 240, height: 240 }} />` directly — that stretches non-square source images.

### Viewport dual-mode toggle (HTML prototypes)

HTML video prototypes that target TikTok/Reels/Shorts must support both modes via a toggle button in the controls bar:

- **TikTok mode** (export): `position: absolute; inset: 0` at full `100vw × 100vh` — use for `node export-gif.js ... --viewport 1080x1920`
- **Desktop preview mode**: fixed 1080×1920 stage, CSS `transform: scale(${deskScale})`, centered in a dark `#000` letterbox — so the 9:16 frame is visible in a browser without scrolling

The toggle label should read **"9:16 export"** / **"🖥 preview"**.

## Controls bar: HTML preview only, never in exports

The playback controls bar (scrubber, scene buttons, timer, mode toggle) must **never appear in exported GIF or MP4 frames**. It exists for in-browser authoring only.

**Required pattern for all new HTML lesson videos:**

- Render the controls bar only when `mode === 'desktop'` (see `html-video-production` skill → "Playback Controls" section for the exact template)
- In `mode === 'tiktok'`, render at most a tiny "🖥 preview" return button — never the full controls bar
- Do NOT rely on the `position:fixed` querySelector hide in `export-gif.js` as the primary mechanism — it is a fallback only

If you see controls in an exported video, the root cause is that the controls are rendered unconditionally (outside the `mode === 'desktop'` gate). Fix the HTML source and re-export; do not try to mask it in post.

## Standard Output Formats

Every completed video export produces **three deliverables** documented in the
proprietary video-export guide (not in this repo):

| File | Purpose |
|------|---------|
| `ChemIllusion Video - <Name>.html` | Editable prototype; scrub/preview in any browser |
| `chemillusion-<variant>.gif` | Embeddable preview (800px wide, 8fps, palette-optimised) |
| `chemillusion-<variant>.mp4` | Shareable deliverable (default 1280×720; use `--viewport` for 9:16/4:5/1:1), H.264 CRF 20, faststart |

Export command: `node export-gif.js <variant> --mp4` — add `--viewport 1080x1920` (or other **WxH**) for TikTok/Reels/Shorts/IG when the HTML stage matches; see **html-video-production**.

GIF defaults: **6fps, 640px wide**. Use `--fps 4 --width 480` to reduce further.
MP4 with `--mp4` always emits **two files**: portrait (`chemillusion-<variant>.mp4`) + YouTube landscape (`chemillusion-<variant>-yt.mp4`, 1920×1080 pillarboxed).

Available variants: `student` · `teacher` · `teacher-v2` · `teacher-v2-es` · `sar`

Default: always run with `--mp4`. GIF-only is only for quick iteration; MP4 is the final-delivery format.

To add a new locale: copy the base HTML, update the `CONTENT` object and any hardcoded strings in scene components, add the variant to `VARIANTS` in `export-gif.js`, then export with `--mp4`.

## S1 Title Slide Positioning Spec (Learn & Creator Series)

These are **exact values**. New videos and remakes must match them precisely regardless of whether the file uses React JSX or vanilla JS string concatenation.

| Element | Property | Exact value |
|---------|----------|-------------|
| Scene wrapper | background | `#000` |
| Scene wrapper | layout | `flex column, alignItems center, justifyContent center` |
| Logo (`ChemIllusion`) | font-size | **80px**, Raleway 900 |
| Logo | color | `Chem` white + `I` `#f59e0b` + `llusion` white |
| Series label | margin-top from logo | **20px** |
| Series label | color | **`#f59e0b`** gold — never blue (`#0ea5e9`) |
| Series label | font-size | **28px**, Inter 700, uppercase, `letter-spacing: 0.14em` |
| Icon row | margin-top from label | **28px** |
| `lessonHub` icon | size | **148 × 148px**, `object-fit: contain` |
| Colon separator | font-size | **64px**, Raleway 900, color `#f59e0b`, `margin: 0 14px`, `opacity: 0.85` |
| `lessonIcon` | size | **148 × 148px**, `object-fit: contain` |
| Phase A opacity at t=0 | constant | **1** — no fade-in ever |
| Phase A fade-out | timing | `1 - eIn(prog(t, 2.2, 3.0))` |
| Phase B fade-in | timing | `eOut(prog(t, 3.0, 4.2))`, `translateY(lerp(24,0,tagIn)px)` |
| Phase B wrapper | padding | `paddingLeft: 44`, `paddingRight: 44`, `position: absolute`, `zIndex: 5` |
| Phase B line 1 | color / size / weight | `#f59e0b` / **48px** / 800, `lineHeight: 1.3`, `letterSpacing: -0.01em` |
| Phase B line 2 | color / size / weight | `rgba(255,255,255,0.88)` / **44px** / 600, `marginTop: 14`, `lineHeight: 1.35` |

**Mistakes that are bugs, not style choices:**
- Logo smaller than 80px
- Series label in blue (`#0ea5e9`) — it must be gold (`#f59e0b`)
- Series label omitted entirely
- Icons smaller than 148×148px
- Phase A elements with fade-in from 0 at t=0
- Phase B tagline without `position: absolute` (causes layout shift)

See `html-video-production` skill → "Scene 1 — Pixel-Perfect Positioning Spec" for full JSX + vanilla JS templates.

## Lesson/Learn Series: S5 CTA Scene Rules

These rules apply to every video in the `lesson-*-tiktok` series (chain tool, lasso tool, clean-up tool, etc.):

### Help Hub icon size (S5)
- The Help Hub icon (`lessonHub` / orgo books icon) in the **S5 CTA scene** must be rendered at **≥116px** — matching the size used in S1.
- The icon must appear on its **own dedicated full-width row**, not inline with surrounding text.
- Correct layout:
 ```
 "Open the Help Hub"
 [116px icon]
 "any time."
 ```
- **Never** use a small inline icon (e.g. `40px`) in S5 — it will look broken compared to the large S1 icon.

### Lesson icon consistency across scenes
- S1 and S4 tool-icon containers: 132×132px container, icon rendered at 96px inside.
- S5 standalone Help Hub row: icon rendered at **116px** with no container box (freestanding).

### S5 scene structure (bottom anchors)
- `LESSON COMPLETE` badge: `bottom: 700px`
- "Try this lesson" + QR code row: `bottom: 230px`
- Help Hub row (dedicated): `bottom: 68px`

## TikTok, Instagram, and short-form (HTML + GIF/MP4 pipeline)

When the user asks for **TikTok**, **Reels**, **Shorts**, or **Instagram** in the context of **ChemIllusion Design System HTML videos** or **export-gif.js** output, follow the **html-video-production** skill (not this tool’s `configure_video_parameters` flow). In short:

- **Aspect ratio:** Use **9:16 at 1080×1920** for TikTok / Reels / Shorts / Stories; **4:5 (1080×1350)** or **1:1 (1080×1080)** for Instagram feed as specified in that skill.
- **First frame:** Include a **visible hero still** (screenshot, structure, or logo) at `t=0` so the thumbnail looks good in feeds.
- **Export:** `node export-gif.js <variant> --viewport 1080x1920 --mp4` (HTML stage dimensions must match).

The in-molecule **structure/AI video** from this skill is not automatically re-encoded for 9:16; for social **marketing** HTML exports, use **html-video-production** + **export-gif.js** as above.

## Reaction Videos

Currently disabled. If user asks: "Reaction videos are coming soon! In the meantime, I can create a multi-molecule structure video with your reactants and products side by side."

## Quick Reference Card

```
STRUCTURE VIDEO defaults:
 tool_style=chalk color=chalk_white thickness=thick
 direction=forward range=20%-100% path=left_to_right
 speed=2x duration=1s → FREE

AI VIDEO defaults (adds to structure):
 provider=bfl_locked model=flux_klein
 cost ≈ frames × $0.017
```

## Modifying an Existing Video (recipe-based editing)

When a user wants to change **one thing** about a video they already made, use `modify_molecule_video` — it re-derives via `POST /videos/{id}/re-derive` without re-running the full creation sequence.

### When to use modify_molecule_video vs. open_molecule_video
- **modify_molecule_video**: User references an existing video ("make that one green", "add labels", "remove audio")
- **open_molecule_video**: User wants a new video ("make a chalk animation")

### Recipe patch fields
| Field | Values |
|-------|--------|
| `tool_style` | chalk, pencil, brush, marker, laser, eraser |
| `molecule_color_key` | green, red, blue, pink, yellow, orange, purple, black, white |
| `line_thickness` | thin, medium, thick |
| `text_level` | none, minimal, standard, detailed |
| `text_size` | small, medium, large |
| `audio_on` | true / false |
| `audio_voice` | echo, alloy, nova, shimmer |
| `audio_numbering` | natural, iupac |

### Keyword mapping
- "green chalk" → `{tool_style: "chalk", molecule_color_key: "green"}`
- "no labels / clean" → `{text_level: "none"}`
- "detailed labels" → `{text_level: "detailed"}`
- "add audio / narration" → `{audio_on: true}`
- "remove audio / mute" → `{audio_on: false}`
- "thicker lines" → `{line_thickness: "thick"}`

### Backend endpoint
the video re-derive endpoint (not in this repo) — free (no AI billing), graceful fallback (text/audio failures are non-fatal).


## Reaction animations: house style + offline rdkit-2D renderer

Use the proprietary reaction-animation renderer (not in this repo) when AI video can't make an
accurate mechanism. Produces mp4 + gif + poster from SMILES; attach to a
reaction_coordinate teaching asset's `video` ref. Pin these (they were the real review
failures): ALL-BLACK atoms (`useBWAtomPalette` -> Br is black, not brown); caption/title
text at ~1x the atom-label size (`fixedFontSize`, real TrueType, never PIL's ~10px
bitmap fallback); titles auto-fit; word-wrapped notes; no purple. `--intermediate` gives
a 2-step mechanism with a whole-frame fade. Full house style and dynamic-asset anchoring
rules: proprietary reaction-animation documentation (not in this repo).
