# Fachinformatiker Anwendungsentwicklung — Prüfungsvorbereitung

Themensammlung für die **Abschlussprüfung Teil 2 (AP2)** im Ausbildungsberuf
Fachinformatiker/-in für Anwendungsentwicklung. Auf Deutsch, mit einer maschinell
übersetzten englischen Fassung.

**→ [Als durchsuchbare Website lesen](https://ftrauernicht.github.io/fachinformatiker-anwendungsentwicklung/)**

[![Prüfen](https://github.com/ftrauernicht/fachinformatiker-anwendungsentwicklung/actions/workflows/ci.yml/badge.svg)](https://github.com/ftrauernicht/fachinformatiker-anwendungsentwicklung/actions/workflows/ci.yml)
[![Links prüfen](https://github.com/ftrauernicht/fachinformatiker-anwendungsentwicklung/actions/workflows/links.yml/badge.svg)](https://github.com/ftrauernicht/fachinformatiker-anwendungsentwicklung/actions/workflows/links.yml)

> [!IMPORTANT]
> Kein offizielles Dokument. Diese Sammlung ist privat entstanden, ohne Gewähr auf
> Vollständigkeit oder Richtigkeit. Was in deiner Prüfung tatsächlich drankommt, klärst du
> mit deinen Ausbildern und der zuständigen IHK.

## Herkunft

Dies ist ein **Fork von
[LakayFTW/exam-prep-fiae-2023](https://github.com/LakayFTW/exam-prep-fiae-2023)**.

Dort haben Auszubildende 2023 zusammengetragen, was sie für ihre eigene Prüfung brauchten
— neun Themengebiete, fünf Diagrammnotationen, rund 4.500 Zeilen, ordentlich belegt. Der
fachliche Kern dieser Sammlung stammt von ihnen und von den Quellen in den Fußnoten. Das
Original wurde zuletzt im September 2024 angefasst.

Dieser Fork führt es weiter. Er ersetzt es nicht und macht es nicht besser — er hält es in
Stand und ergänzt, was beim Lernen gefehlt hat.

## Was diese Fassung anders macht

**Es funktioniert wieder.** Beim Übernehmen waren acht Bilder unsichtbar (falsche relative
Pfade), 21 interne Links zeigten ins Leere, zwei Quellenangaben waren tot und über hundert
Rechtschreibfehler standen im Text — bis hin zu `UNTION ALL` in einem SQL-Beispiel und
einem doppelten Inhaltsverzeichnis auf einer Seite.

**Es bleibt funktionierend.** Fünf GitHub-Workflows prüfen bei jeder Änderung
Formatierung, Rechtschreibung, Links, Anker, Fußnoten, Commit-Nachrichten und ob deutsche
und englische Fassung noch dieselben Seiten haben. Einmal pro Woche läuft zusätzlich eine
Prüfung aller externen Links gegen den Hauptzweig — verrottete Quellen fallen so auf,
bevor jemand danach sucht. Ein weiterer Lauf beobachtet das Original und meldet, wenn es
dort doch wieder Commits gibt.

**Es ist durchsuchbar.** Die
[Website](https://ftrauernicht.github.io/fachinformatiker-anwendungsentwicklung/) hat eine
Volltextsuche über alle Kapitel in beiden Sprachen. Beim Lernen sucht man Begriffe, nicht
Dateien.

**Die Bilder gehören jetzt dazu.** 29 Grafiken waren von fremden Servern eingebunden, zwei
davon über einen Suchmaschinen-Cache. Alles, was frei lizenziert ist, liegt jetzt als
Kopie im Repository — mit Urheber und Lizenz in den
[Bildnachweisen](docs/bildnachweise.md). Die übrigen elf Abbildungen sind durch eigene
[Mermaid](https://mermaid.js.org/)-Diagramme ersetzt, die im Markdown stehen und sich
korrigieren lassen wie jeder andere Text.

**Etwas zum Üben.** 86 Prüfungsfragen mit eingeklappten Antworten, thematisch sortiert,
und fünf Spickzettel für die letzten Tage — Subnetting-Tabelle, SQL-Klauseln, sämtliche
UML-Symbole, die Formeln zu Break-even, Netzplan und Verfügbarkeit, dazu die
Excel-Funktionen, nach denen 2023 in GA2 gefragt wurde. Das Glossar hat ein
Stichwortverzeichnis über alle Kapitel bekommen, erzeugt aus den Überschriften.

**Vier Kapitel mehr, und eins übersetzt.** Zustands-, Aktivitäts-, Sequenz- und
Objektdiagramm standen seit 2023 als Ankündigung ohne Link im Inhaltsverzeichnis — sie
sind jetzt geschrieben, mit Beispiel und mit dem, was in der Prüfung Punkte kostet. Die
Netzwerktechnik gibt es erstmals auch auf Englisch; dabei sind fünf fachliche Fehler
aufgefallen und korrigiert worden, darunter die Behauptung, RAID 0 erhöhe die
Ausfallsicherheit.

**Ein Kapitel pro Datei, ein Titel pro Kapitel.** Vorher begann jede Seite mit der
Überschrift „Table of Content" — ein Website-Generator hätte jede einzelne Seite so
genannt. Inhaltsverzeichnisse werden jetzt aus den Überschriften erzeugt
(`npm run build:toc`) statt von Hand nachgezogen.

## Aufbau

```text
docs/
├── index.md              Startseite der Website
├── bildnachweise.md      Quelle, Urheber und Lizenz jeder Grafik
├── assets/img/           alle Bilder, thematisch sortiert
├── de/                   deutsche Fassung (maßgeblich)
│   ├── 01-netzwerktechnik.md … 09-cloud-computing.md
│   ├── diagramme/        neun Notationen von PAP bis Objektdiagramm
│   ├── pruefungsfragen/  86 Fragen mit eingeklappten Antworten
│   ├── spickzettel/      Tabellen und Formeln zum Wiederholen
│   └── glossar.md        Begriffe ohne festes Kapitel, plus Stichwortverzeichnis
└── en/                   englische Fassung (maschinell übersetzt)

tools/
├── check_content.py      Links, Anker, Fußnoten, Bilder, Sprachparität
├── build_toc.py          Inhaltsverzeichnisse erzeugen und prüfen
└── build_glossary.py     Stichwortverzeichnis erzeugen und prüfen
```

Die Nummern in den Dateinamen sorgen dafür, dass die Reihenfolge auch beim Blättern durch
den Ordner auf GitHub stimmt. Der Adressbaum der Website entspricht bewusst dem Dateibaum
des Repositories — dadurch stimmt jeder relative Pfad an beiden Orten, auch in rohem HTML,
das MkDocs sonst nicht umschreibt.

## Themen

| # | Deutsch | English |
|---|---|---|
| 01 | [Netzwerktechnik](docs/de/01-netzwerktechnik.md) | [Network technology](docs/en/01-network-technology.md) |
| 02 | [Virtualisierung](docs/de/02-virtualisierung.md) | [Virtualization](docs/en/02-virtualization.md) |
| 03 | [Datenbanken](docs/de/03-datenbanken.md) | [Databases](docs/en/03-databases.md) |
| 04 | [Softwareentwicklung](docs/de/04-softwareentwicklung.md) | [Software development](docs/en/04-software-development.md) |
| 05 | [IT-Schutz und -Sicherheit](docs/de/05-it-sicherheit.md) | [IT security](docs/en/05-it-security.md) |
| 06 | [IT-Service-Management](docs/de/06-it-service-management.md) | [IT service management](docs/en/06-it-service-management.md) |
| 07 | [Projektmanagement](docs/de/07-projektmanagement.md) | [Project management](docs/en/07-project-management.md) |
| 08 | [Politik und Wirtschaft](docs/de/08-politik-und-wirtschaft.md) | [Politics and economy](docs/en/08-politics-and-economy.md) |
| 09 | [Cloud Computing](docs/de/09-cloud-computing.md) | [Cloud computing](docs/en/09-cloud-computing.md) |
| — | [Diagramme](docs/de/diagramme/index.md) | [Diagrams](docs/en/diagrams/index.md) |
| — | [Prüfungsfragen](docs/de/pruefungsfragen/index.md) | — |
| — | [Spickzettel](docs/de/spickzettel/index.md) | — |
| — | [Glossar](docs/de/glossar.md) | — |

Prüfungsfragen und Spickzettel gibt es bewusst nur auf Deutsch: die Prüfung ist auf
Deutsch, und geprüft wird genau diese Begrifflichkeit.

## Mitmachen

Fehler gefunden? [Issue aufmachen](https://github.com/ftrauernicht/fachinformatiker-anwendungsentwicklung/issues/new/choose)
oder gleich einen Pull Request schicken — auch für einen einzelnen Tippfehler. Wie das
geht und worauf beim Schreiben zu achten ist, steht in [CONTRIBUTING.md](CONTRIBUTING.md).

Lokal prüfen, bevor du absendest:

```bash
npm install && npm run check
```

## Lizenz

Das ursprüngliche Repository hat **keine Lizenzdatei**. Damit liegen die Rechte an den
Inhalten beim jeweiligen Urheber, und dieser Fork kann keine Lizenz vergeben, die es dort
nicht gibt. Für private Prüfungsvorbereitung ist das unproblematisch; wer die Inhalte
weiterverbreiten oder in eigene Materialien übernehmen will, sollte
[LakayFTW](https://github.com/LakayFTW) fragen.

Die Grafiken sind davon ausgenommen: ihre Lizenzen stehen einzeln in den
[Bildnachweisen](docs/bildnachweise.md). Die Mermaid-Diagramme und die Werkzeuge unter
`tools/` sind in diesem Fork entstanden.

## Ursprüngliche Mitwirkende

Der Inhalt geht auf die Arbeit von [LakayFTW](https://github.com/LakayFTW),
[Jinoyoko-Fusunshi](https://github.com/Jinoyoko-Fusunshi) und
[GodDevourer](https://github.com/GodDevourer) zurück.
