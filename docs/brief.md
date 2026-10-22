# The Grim Repositioner: Build Brief

Oct 21, 2026 · forked from Mock & Roll (Lumostage stage configurator)

An internal tool for trying out new layouts of the existing Lumostage studio: new LED wall
builds, different curves, moved rolling walls and ceilings. It answers "how many panels does
this need, and does it fit the room?" before anyone touches a truss.

## What carried over from Mock & Roll

- **The studio, unchanged.** It's the 2026-10 floor-plan revision: room 80′ E-W × 71′ N-S, 27′ walls, doors,
  the kitchen / washroom block and green room, the partition west of the volume, and the column (8″ post,
  18″ keep-out, 6″ clearance). The room is fixed and not editable. It lives in `STUDIO`, not in saved layouts.
  The exception is the **partition** west of the volume. Its three straight runs are "building walls" saved in each
  layout (`partitions`). They don't move, but each can be removed (shown dashed, ignored by the clash checks) and put back.
- **The frame:** origin at the old curve's centre, +Z = north (the shooting floor), −X = east, 1 world unit = 1 ft.
  The plan keeps the volume at the top (north is down) as Mock & Roll did.
- **The defaults** reproduce the stage as it stands: main wall 36 × 10 at 5° (half circle), two 10 × 8 rolling
  walls on 16′ × 4′ × 2′ decks, a 10 × 6 LED ceiling at 20′.
- Units (ft-in / metres), the walk camera, the studio shell in 3D, and the brand-dark shell (reskinned).

Everything else was dropped: the film camera and lenses, reflections, people and rigs, vehicles and sets,
blocking and moves, playback and 360° content, the plate canvas, the prompt maker, the storyboard and script,
the phone viewer and publishing.

## The model

- **Panel module:** 50 cm (1.6404′). Every size comes from panel counts and is never typed as a length.
- **Wall** = a run of **sections**. Each section is `panels` panels at `curveDeg` degrees between neighbours.
  Positive curves are concave toward the face; negative curves are convex. Each panel is a flat 50 cm chord. Where
  two sections meet, the joint takes the average angle, so 36 at 5° lands exactly on a half circle (180°).
  - Example: a hockey stick is `30 @ 5°` + `60 @ 0°`.
  - Wall-wide: panels high, footing (floor-standing) or rolling deck (length / depth / height).
  - **Pin:** start, middle or end. That point and its direction stay fixed while sections are edited.
    `x, z` is where the pin sits; `rotationDeg` is the run direction there (0° = running west, face north).
- **Ceiling** = panels wide × panels long, height (bottom face), x / z (centre), turn, and tilt (+ lifts the north edge).
  Rig range is 4′–20′, with motors at 24′.

## Features

- Plan (2D, true scale, crisp), 3D (walk camera), or both side by side.
- **Plan:** drag to move (snaps to 1″ / 3″ / 6″ / 1′, or metric steps; Shift = free), drag the red handle
  to turn (15° steps, Shift = 1°), `[` `]` turn, arrows nudge, wheel zoom, drag empty floor to pan, Measure tool.
- **Ghost:** the stage as it stands, dashed under the new layout.
- **Side panel**, in three fixed zones:
  - **Count and checks:** total panels, wall / ceiling split, panels owned, and the omens (click one to select the piece).
  - **Pieces:** a list of walls and ceilings that doesn't move when you select something. Each row shows its size, a warning flag
    and a show / hide toggle; arrow keys move through it.
  - **Inspector:** the selected piece, laid out in build order: Shape (sections with steppers, presets, add section),
    Height (panels high, floor or deck), Position (x / z / turn, hold-fixed point, Square up / Centre / Flip face / Mirror),
    Measurements, then Duplicate / Delete.
  - Steppers and ↑ / ↓ adjust numbers (Shift for bigger or finer steps). A run of quick changes undoes as one step.
  - Lengths show and type as feet-and-inches (`19' 2.75"`) or metres.
- **File menu:** Save (Ctrl+S, under the layout name), saved layouts, Export / Import JSON, and Start over.
- **Panel count:** wall + ceiling + total, checked against "panels owned" (stored per browser).
- **Omens** (advisory clash checks; nothing is blocked):
  - a wall through the studio wall, into a room, across the partition, into the column or its clearance
  - walls overlapping each other
  - a wall in the fire lane
  - a wall taller than the room, or than a ceiling above it
  - a ceiling outside the room or outside the rig range
  - more panels than you own
- Undo / redo, autosave, named layouts saved in the browser, JSON export / import.
- **Print plan:** A3 landscape. The plan on white with all labels, plus a panel schedule and the omens.

## Known approximations

- **Fire lane:** 3.5′ inside the room's perimeter and round the kitchen / green-room block. In Mock & Roll it also
  ran inside the fixed curve and left the area behind the volume staff-only. With the wall movable, the lane now
  follows the room.
- **Main wall size:** the panel maths gives a half circle of r 18′ 9.6″ (tips 37′ 7″ apart). The tape measure says
  38′ 4″ tip to tip at ~177.5°, the difference being cabinet gaps. The model uses true panel maths.
- **Default rolling walls:** placed just inside the mouth at z = 7.6′. A 16′ 4.8″ wall barely fits between the
  tip line and the column, so the default flags a clearance warning. That's real, not a bug.

## Stack

Single `index.html`, vanilla Three.js r128 (`vendor/three/three.min.js`) for 3D and a 2D canvas for the plan.
No build step. It runs from the file or `python serve.py` (port 8139). The title font (Pirata One) loads from Google
Fonts when online and falls back to Georgia offline.
