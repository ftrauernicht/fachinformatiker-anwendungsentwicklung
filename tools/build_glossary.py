#!/usr/bin/env python3
"""Stichwortverzeichnis aus den Überschriften aller deutschen Kapitel bauen.

Wer beim Lernen über „SLA" stolpert, sucht nicht nach einem Kapitel, sondern
nach dem Begriff. Auf der Website erledigt das die Volltextsuche — auf
github.com gibt es keine, und ausgedruckt schon gar nicht.

Dieses Skript sammelt die Überschriften, die einen Fachbegriff benennen, und
schreibt sie als A–Z-Verzeichnis in den markierten Abschnitt von
docs/de/glossar.md.

    python tools/build_glossary.py            # Verzeichnis neu schreiben
    python tools/build_glossary.py --check    # nur prüfen, Exitcode 1 bei Abweichung
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"
GLOSSARY = DOCS / "de" / "glossar.md"

BEGIN = "<!-- stichwortverzeichnis:anfang -->"
END = "<!-- stichwortverzeichnis:ende -->"

HEADING = re.compile(r"^(#{2,5})\s+(.*?)\s*#*$")
FENCE = re.compile(r"^\s*(```|~~~)")

# Überschriften, die überall vorkommen und keinen Begriff benennen.
GENERIC = {
    "inhaltsverzeichnis", "vorteile", "nachteile", "vorteil", "nachteil",
    "beispiel", "beispiele", "anwendung", "erläuterung", "elemente", "konzept",
    "syntax", "quellen", "wozu", "notation", "themen", "diagramme", "übersicht",
    "mögliche fehler", "zusammenfassung", "ziel", "aufbau", "allgemein",
    "worauf es in der prüfung ankommt", "abgrenzung", "funktionsweise",
    "einsatzbereiche", "arten von datenbanken", "häufige fehler",
    "was in prüfungsantworten zählt", "warum das hier steht",
    "1. möglicher block", "2. möglicher block", "weiteres", "sonstiges",
    "zur darstellung", "rechenregeln", "merke",
}

# Diese Dateien beschreiben, üben oder fassen zusammen — sie definieren nichts.
SKIP_DIRS = ("pruefungsfragen", "spickzettel")

ABBREVIATION = re.compile(r"\b[A-Z][A-Z0-9/]{1,7}\b")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def slugify(text: str) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\s\-]", "", text, flags=re.UNICODE)
    return text.replace(" ", "-")


def sort_key(term: str) -> tuple:
    """Umlaute einsortieren wie im Duden: ä bei a, ö bei o, ü bei u, ß bei ss."""
    folded = (term.lower()
              .replace("ä", "a").replace("ö", "o").replace("ü", "u").replace("ß", "ss"))
    folded = unicodedata.normalize("NFKD", folded)
    folded = "".join(c for c in folded if not unicodedata.combining(c))
    return (folded, term)


def initial(term: str) -> str:
    first = sort_key(term)[0][:1].upper()
    return first if first.isalpha() else "0–9"


def is_term(text: str) -> bool:
    """Benennt diese Überschrift einen nachschlagbaren Begriff?"""
    plain = re.sub(r"[*`]", "", text).strip()
    if plain.lower() in GENERIC or len(plain) < 2:
        return False
    if ABBREVIATION.search(plain):          # enthält eine Abkürzung: DHCP, SLA, ACID
        return True
    return len(plain.split()) <= 3          # oder ist ein kurzer Begriff


def collect() -> dict[str, list[tuple[str, str]]]:
    """Begriff -> Liste von (Kapitelname, relativer Link)."""
    entries: dict[str, list[tuple[str, str]]] = {}
    for path in sorted((DOCS / "de").rglob("*.md")):
        if path == GLOSSARY or path.name == "index.md":
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue

        chapter = None
        seen: dict[str, int] = {}
        in_fence = False
        for line in path.read_text(encoding="utf-8").splitlines():
            if FENCE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if line.startswith("# "):
                chapter = line[2:].strip()
                continue
            match = HEADING.match(line)
            if not match:
                continue
            text = match.group(2).strip()
            base = slugify(text)
            count = seen.get(base, 0)
            seen[base] = count + 1
            if not is_term(text):
                continue
            anchor = base if count == 0 else f"{base}-{count}"
            target = os.path.relpath(path, GLOSSARY.parent).replace(os.sep, "/")
            term = re.sub(r"[*`]", "", text).strip().rstrip(":.,;")
            entries.setdefault(term, []).append((chapter or path.stem, f"{target}#{anchor}"))
    return entries


def render(entries: dict[str, list[tuple[str, str]]]) -> list[str]:
    lines = [
        BEGIN,
        "",
        "<!-- Erzeugt von tools/build_glossary.py — nicht von Hand ändern. -->",
        "",
        f"{len(entries)} Begriffe aus allen Kapiteln, alphabetisch. Umlaute stehen beim",
        "Grundbuchstaben.",
    ]
    letter = None
    for term in sorted(entries, key=sort_key):
        first = initial(term)
        if first != letter:
            letter = first
            lines += ["", f"### {letter}", ""]
        targets = ", ".join(f"[{chapter}]({link})" for chapter, link in entries[term])
        lines.append(f"- **{term}** — {targets}")
    lines += ["", END]
    return lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="nur melden, nichts schreiben")
    args = parser.parse_args()

    text = GLOSSARY.read_text(encoding="utf-8")
    if BEGIN not in text or END not in text:
        print(f"{GLOSSARY.name}: Marker {BEGIN} / {END} fehlen", file=sys.stderr)
        return 2

    lines = text.splitlines()
    start = next(i for i, l in enumerate(lines) if l.strip() == BEGIN)
    stop = next(i for i, l in enumerate(lines) if l.strip() == END)

    entries = collect()
    rebuilt = lines[:start] + render(entries) + lines[stop + 1:]

    if rebuilt == lines:
        print(f"Stichwortverzeichnis ist aktuell ({len(entries)} Begriffe).")
        return 0
    if args.check:
        print("Stichwortverzeichnis veraltet — python tools/build_glossary.py")
        return 1
    GLOSSARY.write_text("\n".join(rebuilt) + "\n", encoding="utf-8", newline="\n")
    print(f"Stichwortverzeichnis neu gebaut: {len(entries)} Begriffe.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
