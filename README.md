# pcbdesign

A browser-based grid editor for single-sided PCBs that can be 3D-printed
in heat-resistant filament. Designs are exported to OpenSCAD; after
printing, the unprinted bottom layer of each hole is punched through with
an awl.

Live app: <https://lukacslacko.github.io/pcbdesign/>

## What it does

- 2.54 mm (0.1″) grid editor — matches DIP pin pitch
- Cell states: empty, board, trace, hole
- Traces are 1.6 mm pads in the centre of a cell; arms grow toward
  neighbouring trace/hole cells along the segments you actually drew
- Holes are 0.8 mm square cutouts, 0.18 mm bottom skin left for awl-punching
- Tools (keyboard shortcuts in parentheses):
  - **Erase** (E) — rectangle drag
  - **Board** (B) — rectangle drag
  - **Trace** (T) — axis-parallel line
  - **Bus** (S) — N parallel axis-parallel lines; <kbd>1</kbd>–<kbd>9</kbd>/<kbd>0</kbd> set 1–10 lines
  - **Hole** (H) — axis-parallel line
  - **DIP** (D) — click to drop a DIP package; <kbd>4</kbd>/<kbd>8</kbd>/<kbd>0</kbd> set 8/16/20 pins, narrow/broad body, <kbd>R</kbd> rotates
- Right-drag always erases
- Save/load `.json` and export `.scad`
- Designs autosave to `localStorage`

## Physical parameters (mm)

| Layer | Thickness |
| --- | --- |
| Board | 0.5 |
| Trace pad / arm height | +0.3 above board |
| Trace / pad width | 1.6 |
| Hole | 0.8 × 0.8 square |
| Bottom skin under hole | 0.18 |

Print at 0.18 mm first layer so the hole skin lands on layer 1.

## Running locally

It's a single `index.html`, no build step. Open it in a browser:

```
open index.html
```

## License

[MIT](LICENSE)
