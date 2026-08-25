#!/usr/bin/env python3
"""Inhaltsprüfung für die FIAE-Sammlung.

Prüft, was ein Markdown-Linter nicht sieht: ob Links und Anker wirklich
irgendwo hinführen, ob Inhaltsverzeichnisse noch zu den Überschriften passen,
ob Fußnoten definiert sind, ob jedes Bild benutzt wird und ob die deutsche und
die englische Fassung dieselben Seiten haben.

Ob die Inhaltsverzeichnisse noch zu den Überschriften passen, prüft
tools/build_toc.py --check.

    python tools/check_content.py                  # prüfen, Fehler -> Exitcode 1
    python tools/check_content.py --strict         # Warnungen zählen als Fehler
    python tools/check_content.py --format github  # Annotations für GitHub Actions
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.parse
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"
ASSETS = DOCS / "assets"

# Seiten, die bewusst nur auf Deutsch existieren: Prüfungsfragen und Spickzettel
# sind auf die deutschsprachige Prüfung zugeschnitten und werden nicht übersetzt.
PARITY_EXEMPT = ("pruefungsfragen/", "spickzettel/", "glossar.md")

# Zuordnung deutscher zu englischen Seiten. Neue Kapitel hier eintragen,
# sonst meldet die Paritätsprüfung sie als nicht zugeordnet.
PAGE_MAP = {
    "index.md": "index.md",
    "01-netzwerktechnik.md": "01-network-technology.md",
    "02-virtualisierung.md": "02-virtualization.md",
    "03-datenbanken.md": "03-databases.md",
    "04-softwareentwicklung.md": "04-software-development.md",
    "05-it-sicherheit.md": "05-it-security.md",
    "06-it-service-management.md": "06-it-service-management.md",
    "07-projektmanagement.md": "07-project-management.md",
    "08-politik-und-wirtschaft.md": "08-politics-and-economy.md",
    "09-cloud-computing.md": "09-cloud-computing.md",
    "diagramme/index.md": "diagrams/index.md",
    "diagramme/01-programmablaufplan.md": "diagrams/01-flowchart.md",
    "diagramme/02-struktogramm.md": "diagrams/02-nassi-shneiderman-diagram.md",
    "diagramme/03-klassendiagramm.md": "diagrams/03-class-diagram.md",
    "diagramme/04-anwendungsfalldiagramm.md": "diagrams/04-use-case-diagram.md",
    "diagramme/05-entity-relationship-modell.md": "diagrams/05-entity-relationship-model.md",
    "diagramme/06-zustandsdiagramm.md": "diagrams/06-state-diagram.md",
    "diagramme/07-aktivitaetsdiagramm.md": "diagrams/07-activity-diagram.md",
    "diagramme/08-sequenzdiagramm.md": "diagrams/08-sequence-diagram.md",
    "diagramme/09-objektdiagramm.md": "diagrams/09-object-diagram.md",
}

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*$")
FENCE = re.compile(r"^\s*(```|~~~)")
LINK = re.compile(r"!?\[([^\]]*)\]\(\s*<?([^)>\s]+)>?(?:\s+\"[^\"]*\")?\s*\)")
HTML_SRC = re.compile(r'<(?:img|a)[^>]*?(?:src|href)="([^"]+)"')
FOOTNOTE_DEF = re.compile(r"^\[\^([^\]]+)\]:", re.M)
FOOTNOTE_REF = re.compile(r"\[\^([^\]]+)\](?!:)")
EXTERNAL_IMG = re.compile(r'<img[^>]*src="(https?://[^"]+)"')


if hasattr(sys.stdout, "reconfigure"):  # Umlaute auch auf Windows-Runnern ausgeben
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def slugify(text: str) -> str:
    """Anker so bilden, wie GitHub und MkDocs es tun."""
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = text.strip().lower()
    text = re.sub(r"[^\w\s\-]", "", text, flags=re.UNICODE)
    return text.replace(" ", "-")


@dataclass
class Page:
    path: Path
    text: str
    # (Zeile, eindeutiger Anker, Basis-Anker ohne -1/-2, Überschriftentext)
    headings: list[tuple[int, str, str, str]] = field(default_factory=list)
    anchors: set[str] = field(default_factory=set)

    @property
    def rel(self) -> str:
        return self.path.relative_to(REPO).as_posix()


@dataclass
class Finding:
    level: str  # "error" oder "warning"
    file: str
    line: int
    message: str


def load_pages() -> list[Page]:
    pages = []
    for path in sorted(DOCS.rglob("*.md")):
        page = Page(path=path, text=path.read_text(encoding="utf-8"))
        seen: dict[str, int] = {}
        in_fence = False
        for number, line in enumerate(page.text.splitlines(), start=1):
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
            slug = base if count == 0 else f"{base}-{count}"
            page.headings.append((number, slug, base, match.group(2)))
            page.anchors.add(slug)
        pages.append(page)
    return pages


def line_of(text: str, needle: str) -> int:
    for number, line in enumerate(text.splitlines(), start=1):
        if needle in line:
            return number
    return 1


def check_links(pages: list[Page], by_path: dict[Path, Page]) -> list[Finding]:
    findings = []
    for page in pages:
        targets = [m.group(2) for m in LINK.finditer(page.text)]
        targets += HTML_SRC.findall(page.text)
        for target in targets:
            if target.startswith(("http://", "https://", "mailto:", "tel:", "data:")):
                continue
            line = line_of(page.text, target)
            if target.startswith("#"):
                if target[1:].lower() not in page.anchors:
                    findings.append(Finding("error", page.rel, line,
                                            f"Anker {target} gibt es in dieser Datei nicht"))
                continue
            if target.startswith("/"):
                findings.append(Finding(
                    "error", page.rel, line,
                    f"Absoluter Link {target} zeigt auf die Wurzel der Website, "
                    "auf github.com also ins Leere — bitte relativ verlinken"))
                continue
            path_part, _, fragment = target.partition("#")
            resolved = (page.path.parent / urllib.parse.unquote(path_part)).resolve()
            if not resolved.exists():
                findings.append(Finding("error", page.rel, line,
                                        f"Linkziel {target} existiert nicht"))
                continue
            if fragment and resolved.suffix == ".md":
                other = by_path.get(resolved)
                if other and fragment.lower() not in other.anchors:
                    findings.append(Finding("error", page.rel, line,
                                            f"Anker #{fragment} gibt es in {resolved.name} nicht"))
    return findings



def check_footnotes(pages: list[Page]) -> list[Finding]:
    findings = []
    for page in pages:
        defined = set(FOOTNOTE_DEF.findall(page.text))
        used = set(FOOTNOTE_REF.findall(page.text))
        for name in sorted(used - defined):
            findings.append(Finding("error", page.rel, line_of(page.text, f"[^{name}]"),
                                    f"Fußnote [^{name}] wird benutzt, aber nirgends definiert"))
        for name in sorted(defined - used):
            findings.append(Finding("warning", page.rel, line_of(page.text, f"[^{name}]:"),
                                    f"Fußnote [^{name}] ist definiert, wird aber nicht referenziert"))
    return findings


def check_duplicate_headings(pages: list[Page]) -> list[Finding]:
    """Zwei gleichnamige Überschriften unter derselben Elternüberschrift.

    „Vorteile“ darf in mehreren Kapiteln stehen — das ist normal. Stehen zwei
    davon aber unter derselben Elternüberschrift, ist der zweite Anker -1 und
    jede Umsortierung bricht ihn still.
    """
    findings = []
    for page in pages:
        stack: list[tuple[int, str]] = []
        groups: dict[tuple, list[tuple[int, str]]] = {}
        for line, _slug, base, text in page.headings:
            level = next(len(m.group(1)) for m in [HEADING.match(page.text.splitlines()[line - 1])] if m)
            while stack and stack[-1][0] >= level:
                stack.pop()
            parent = tuple(name for _level, name in stack)
            groups.setdefault(parent + (base,), []).append((line, text))
            stack.append((level, base))
        for spots in groups.values():
            if len(spots) > 1:
                where = ", ".join(str(line) for line, _ in spots)
                findings.append(Finding(
                    "warning", page.rel, spots[1][0],
                    f"Überschrift „{spots[0][1]}“ steht mehrfach unter derselben "
                    f"Elternüberschrift (Zeilen {where}); der zweite Anker heißt -1 "
                    "und bricht beim Umsortieren"))
    return findings


def check_assets(pages: list[Page]) -> list[Finding]:
    findings = []
    used: set[Path] = set()
    for page in pages:
        targets = [m.group(2) for m in LINK.finditer(page.text)] + HTML_SRC.findall(page.text)
        for target in targets:
            if target.startswith(("http", "#", "mailto:")):
                continue
            resolved = (page.path.parent / urllib.parse.unquote(target.partition("#")[0])).resolve()
            if ASSETS in resolved.parents:
                used.add(resolved)
    if not ASSETS.is_dir():
        return findings
    for asset in sorted(path for path in ASSETS.rglob("*") if path.is_file()):
        if asset.suffix.lower() in {".md", ".css", ".js"}:
            continue
        if asset.resolve() not in used:
            findings.append(Finding("warning", asset.relative_to(REPO).as_posix(), 1,
                                    "Datei liegt in docs/assets, wird aber von keiner Seite benutzt"))
    return findings


def check_external_images(pages: list[Page]) -> list[Finding]:
    findings = []
    for page in pages:
        for match in EXTERNAL_IMG.finditer(page.text):
            url = match.group(1)
            host = urllib.parse.urlparse(url).netloc
            findings.append(Finding(
                "warning", page.rel, line_of(page.text, url),
                f"Bild wird von {host} heiß verlinkt — es verschwindet, sobald die "
                "Gegenseite es verschiebt, und wir haben keine Kontrolle darüber"))
    return findings


def check_parity() -> list[Finding]:
    findings = []

    def pages_of(language: str) -> set[str]:
        root = DOCS / language
        if not root.is_dir():
            return set()
        return {path.relative_to(root).as_posix() for path in root.rglob("*.md")}

    german, english = pages_of("de"), pages_of("en")
    for source in sorted(german):
        if source.startswith(PARITY_EXEMPT) or source in PARITY_EXEMPT:
            continue
        target = PAGE_MAP.get(source)
        if target is None:
            findings.append(Finding(
                "warning", f"docs/de/{source}", 1,
                "Seite ist in PAGE_MAP (tools/check_content.py) nicht zugeordnet"))
        elif target not in english:
            findings.append(Finding(
                "warning", f"docs/de/{source}", 1,
                f"Keine englische Entsprechung vorhanden (erwartet: docs/en/{target})"))
    known_targets = set(PAGE_MAP.values())
    for target in sorted(english):
        if target not in known_targets:
            findings.append(Finding(
                "warning", f"docs/en/{target}", 1,
                "Seite ist in PAGE_MAP (tools/check_content.py) nicht zugeordnet"))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--strict", action="store_true",
                        help="Warnungen ebenfalls als Fehler werten")
    parser.add_argument("--format", choices=["text", "github"], default="text")
    args = parser.parse_args()

    if not DOCS.is_dir():
        print("docs/ nicht gefunden — bitte im Wurzelverzeichnis des Repositories starten",
              file=sys.stderr)
        return 2

    pages = load_pages()
    by_path = {page.path.resolve(): page for page in pages}

    findings: list[Finding] = []
    findings += check_links(pages, by_path)
    findings += check_footnotes(pages)
    findings += check_duplicate_headings(pages)
    findings += check_assets(pages)
    findings += check_external_images(pages)
    findings += check_parity()

    errors = [f for f in findings if f.level == "error"]
    warnings = [f for f in findings if f.level == "warning"]

    for finding in sorted(findings, key=lambda f: (f.level != "error", f.file, f.line)):
        if args.format == "github":
            print(f"::{finding.level} file={finding.file},line={finding.line}::{finding.message}")
        else:
            marker = "FEHLER " if finding.level == "error" else "Warnung"
            print(f"{marker} {finding.file}:{finding.line}  {finding.message}")

    print(f"\n{len(pages)} Seiten geprüft — {len(errors)} Fehler, {len(warnings)} Warnungen")
    return 1 if errors or (args.strict and warnings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
