# The Grim Repositioner

*Every panel's time comes.*

Internal Lumostage tool for redesigning the stage: build LED walls from sections of panels at a
curve per panel (e.g. `30 @ 5°` + `60 flat` for a hockey stick), move and resize the rolling walls
and ceilings, and see the panel count and every clash with the room before anything is rigged. For client pop-ups, switch
to **Open space** (no studio, just the floor) and turn on **Car + person** (an average-size car and a 6′ person) for scale.

- **Run:** open `index.html`, or `python serve.py` → http://127.0.0.1:8139/
- **Spec / as-built:** [docs/brief.md](docs/brief.md)
- Forked from Mock & Roll (the stage configurator). The studio floor plan is carried over unchanged;
  the camera, playback and content tools were left behind. One car and one person came back as scale references.

Layouts autosave in the browser; use **Save in browser** for named versions and **Export JSON** to share one.
