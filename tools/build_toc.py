#!/usr/bin/env python3
"""Inhaltsverzeichnisse aus den Überschriften neu erzeugen.

Jede Kapitelseite trägt ein handgepflegtes Inhaltsverzeichnis. Von Hand
gepflegt heißt: es veraltet, sobald jemand eine Überschrift umbenennt. Dieses
Skript baut die Liste aus den tatsächlichen Überschriften neu auf.

    python tools/build_toc.py            # Inhaltsverzeichnisse neu schreiben
    python tools/build_toc.py --check    # nur prüfen, Exitcode 1 bei Abweichung

Erkannt wird der Abschnitt an seiner Überschrift ("## Inhaltsverzeichnis" bzw.
"## Table of contents"). Seiten ohne diese Überschrift bleiben unberührt.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"

TOC_HEADINGS = {"inhaltsverzeichnis", "table of contents"}
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*$")
FENCE = re.compile(r"^\s*(```|~~~)")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def slugify(text: str) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\s\-]", "", text, flags=re.UNICODE)
    return text.replace(" ", "-")


def headings_of(lines: list[str]) -> list[tuple[int, int, str, str]]:
    """(Zeilennummer, Ebene, Text, eindeutiger Anker) aller Überschriften."""
    result = []
    seen: dict[str, int] = {}
    in_fence = False
    for index, line in enumerate(lines):
        if FENCE.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = HEADING.match(line)
        if not match:
            continue
        base = slugify(match.group(2))
        count = seen.get(base, 0)
        seen[base] = count + 1
        anchor = base if count == 0 else f"{base}-{count}"
        result.append((index, len(match.group(1)), match.group(2), anchor))
    return result


def build(lines: list[str]) -> list[str] | None:
    """Neue Zeilen der Datei zurückgeben, oder None wenn kein Abschnitt existiert."""
    heads = headings_of(lines)
    toc = next((h for h in heads if h[1] == 2 and h[2].strip().lower() in TOC_HEADINGS), None)
    if toc is None:
        return None
    toc_index = toc[0]

    listed = [h for h in heads if h[0] != toc_index and 2 <= h[1] <= 5]
    if not listed:
        return None
    # Nicht jede Seite beginnt mit einer H2. Die flachste vorkommende Ebene
    # bildet den linken Rand, sonst steht die erste Zeile eingerückt da.
    top = min(level for _index, level, _text, _anchor in listed)
    entries = ["  " * (level - top) + f"- [{text}](#{anchor})"
               for _index, level, text, anchor in listed]

    # Alter Block: alles zwischen der Überschrift und der nächsten Überschrift.
    end = len(lines)
    for index, _level, _text, _anchor in heads:
        if index > toc_index:
            end = index
            break
    while end > toc_index + 1 and not lines[end - 1].strip():
        end -= 1

    rest = lines[end:]
    while rest and not rest[0].strip():
        rest.pop(0)
    return lines[: toc_index + 1] + [""] + entries + [""] + rest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="nur melden, nichts schreiben")
    args = parser.parse_args()

    stale = 0
    for path in sorted(DOCS.rglob("*.md")):
        lines = path.read_text(encoding="utf-8").splitlines()
        rebuilt = build(lines)
        if rebuilt is None or rebuilt == lines:
            continue
        stale += 1
        if args.check:
            print(f"veraltet: {path.relative_to(REPO).as_posix()}")
        else:
            path.write_text("\n".join(rebuilt) + "\n", encoding="utf-8", newline="\n")
            print(f"neu gebaut: {path.relative_to(REPO).as_posix()}")

    if args.check and stale:
        print(f"\n{stale} Inhaltsverzeichnis(se) veraltet — python tools/build_toc.py")
        return 1
    if not stale:
        print("Alle Inhaltsverzeichnisse sind aktuell.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
