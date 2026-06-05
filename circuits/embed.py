#!/usr/bin/env python3
"""Embed circuits/*.json into index.html as inert JSON <script> blocks.

The editor runs straight from file:// (no server, no build step), so it can't
fetch() the circuit files at runtime — they have to live inside index.html. This
script regenerates the embedded copies from the folder: it replaces everything
between the <!-- PREMADE:START --> and <!-- PREMADE:END --> markers with one
  <script type="application/json" class="premade-circuit" data-name="...">...</script>
block per JSON file. The display name is the filename without its .json suffix.

Usage:  python3 circuits/embed.py        # run from the repo root
Add a circuit by dropping a .json in this folder and re-running.
"""
import glob
import html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
INDEX = os.path.join(ROOT, "index.html")
START = "<!-- PREMADE:START -->"
END = "<!-- PREMADE:END -->"


def main():
    blocks = []
    for path in sorted(glob.glob(os.path.join(HERE, "*.json"))):
        name = os.path.splitext(os.path.basename(path))[0]
        with open(path, encoding="utf-8") as f:
            data = json.load(f)  # parse + reserialize: validates and normalises whitespace
        payload = json.dumps(data, separators=(",", ":"))
        if "</script" in payload.lower():
            sys.exit(f"refusing to embed {name}: contains a </script sequence")
        attr = html.escape(name, quote=True)
        blocks.append(
            f'  <script type="application/json" class="premade-circuit" '
            f'data-name="{attr}">{payload}</script>'
        )

    with open(INDEX, encoding="utf-8") as f:
        page = f.read()
    if START not in page or END not in page:
        sys.exit("markers <!-- PREMADE:START/END --> not found in index.html")

    pre, rest = page.split(START, 1)
    _, post = rest.split(END, 1)
    body = "\n" + "\n".join(blocks) + "\n  " if blocks else "\n  "
    page = f"{pre}{START}{body}{END}{post}"
    with open(INDEX, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"embedded {len(blocks)} circuit(s) into index.html")


if __name__ == "__main__":
    main()
