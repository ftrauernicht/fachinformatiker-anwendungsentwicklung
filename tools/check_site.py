#!/usr/bin/env python3
"""Die gebaute Website auf Verweise ins Leere prüfen.

`mkdocs build --strict` prüft nur Links, die als Markdown geschrieben sind.
Rohes HTML sieht es nicht — und dort steckt der Fehler, den man beim Bauen
nicht bemerkt: MkDocs schreibt relative Pfade in <img src="…"> nicht um. Eine
Seite kann fehlerfrei bauen und trotzdem hundert kaputte Bilder zeigen.

Dieses Skript geht die fertigen HTML-Dateien durch und prüft für jeden lokalen
Verweis, ob die Datei tatsächlich im Ausgabeverzeichnis liegt.

    python tools/check_site.py            # nach mkdocs build ausführen
    python tools/check_site.py --format github
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.parse
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SITE = REPO / "site"
MKDOCS = REPO / "mkdocs.yml"

SKIP_SCHEMES = ("http://", "https://", "mailto:", "tel:", "data:", "javascript:", "#")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


class References(HTMLParser):
    """Sammelt alles, was auf eine andere Datei zeigt."""

    WANTED = {"src", "href", "poster", "data"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name in self.WANTED and value:
                self.targets.append(value)


def site_prefix() -> str:
    """Der Pfadteil aus site_url, also z. B. /fachinformatiker-anwendungsentwicklung/.

    Unter diesem Präfix liegt die Website auf GitHub Pages. Verweise, die damit
    beginnen, gehören auf das Ausgabeverzeichnis abgebildet.
    """
    match = re.search(r"^site_url:\s*(\S+)", MKDOCS.read_text(encoding="utf-8"), re.M)
    if not match:
        return "/"
    path = urllib.parse.urlparse(match.group(1)).path
    return path if path.endswith("/") else path + "/"


def resolve(target: str, page: Path, prefix: str) -> Path | None:
    """Datei, auf die der Verweis zeigt — oder None, wenn er nicht zu prüfen ist."""
    target = target.split("#", 1)[0].split("?", 1)[0]
    if not target or target.startswith(SKIP_SCHEMES) or target.startswith("//"):
        return None
    target = urllib.parse.unquote(target)

    if target.startswith("/"):
        if not target.startswith(prefix):
            return None  # zeigt aus der Website heraus, nicht unsere Sache
        resolved = SITE / target[len(prefix):]
    else:
        resolved = page.parent / target

    resolved = resolved.resolve()
    return resolved / "index.html" if resolved.is_dir() else resolved


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=["text", "github"], default="text")
    args = parser.parse_args()

    if not SITE.is_dir():
        print("site/ nicht gefunden — bitte zuerst mkdocs build ausführen", file=sys.stderr)
        return 2

    prefix = site_prefix()
    pages = sorted(SITE.rglob("*.html"))
    broken: list[tuple[str, str]] = []
    checked = 0

    for page in pages:
        parser_ = References()
        parser_.feed(page.read_text(encoding="utf-8", errors="replace"))
        for target in parser_.targets:
            resolved = resolve(target, page, prefix)
            if resolved is None:
                continue
            checked += 1
            if not resolved.exists():
                broken.append((page.relative_to(SITE).as_posix(), target))

    for where, target in broken:
        message = f"Verweis {target} zeigt auf eine Datei, die es in site/ nicht gibt"
        if args.format == "github":
            print(f"::error file=site/{where}::{message}")
        else:
            print(f"FEHLER site/{where}  {message}")

    print(f"\n{len(pages)} Seiten, {checked} lokale Verweise geprüft — {len(broken)} kaputt")
    return 1 if broken else 0


if __name__ == "__main__":
    raise SystemExit(main())
