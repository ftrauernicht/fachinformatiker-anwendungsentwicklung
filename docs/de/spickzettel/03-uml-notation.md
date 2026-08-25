# Spickzettel: UML-Notation

## Inhaltsverzeichnis

- [Klassendiagramm: Sichtbarkeit](#klassendiagramm-sichtbarkeit)
- [Klassendiagramm: Beziehungen](#klassendiagramm-beziehungen)
- [Multiplizitäten](#multiplizitäten)
- [ERM: Kardinalitäten](#erm-kardinalitäten)
- [Anwendungsfalldiagramm](#anwendungsfalldiagramm)
- [Programmablaufplan gegen Struktogramm](#programmablaufplan-gegen-struktogramm)
- [Sequenzdiagramm](#sequenzdiagramm)
- [Zustandsdiagramm](#zustandsdiagramm)
- [Aktivitätsdiagramm](#aktivitätsdiagramm)

## Klassendiagramm: Sichtbarkeit

| Zeichen | Sichtbarkeit | Zugriff von |
|---|---|---|
| `+` | public | überall |
| `-` | private | nur aus der Klasse selbst |
| `#` | protected | Klasse und Unterklassen |
| `~` | package | demselben Paket |

Schreibweise: `- kontostand: double` für ein Attribut,
`+ einzahlen(betrag: double): void` für eine Methode.
Unterstrichen bedeutet **statisch**, *kursiv* bedeutet **abstrakt**.

## Klassendiagramm: Beziehungen

| Beziehung | Linie | Merkspruch |
|---|---|---|
| Assoziation | durchgezogene Linie | „kennt" |
| Gerichtete Assoziation | Linie mit offener Pfeilspitze | „kennt, aber nur in eine Richtung" |
| Aggregation | Linie mit **leerer** Raute am Ganzen | „hat, Teil überlebt das Ganze" |
| Komposition | Linie mit **gefüllter** Raute am Ganzen | „besteht aus, Teil stirbt mit" |
| Vererbung / Generalisierung | durchgezogen, **leeres** Dreieck zur Oberklasse | „ist ein" |
| Realisierung / Implementierung | **gestrichelt**, leeres Dreieck zum Interface | „erfüllt" |
| Abhängigkeit | **gestrichelt**, offene Pfeilspitze | „benutzt vorübergehend" |

Zwei Merkregeln, die fast alle Fehler verhindern:

- **Die Raute steht immer am Ganzen**, nie am Teil.
- **Gestrichelt heißt schwach**: Realisierung und Abhängigkeit sind gestrichelt, Vererbung
  und Aggregation nicht.

## Multiplizitäten

| Angabe | Bedeutung |
|---|---|
| `1` | genau eins |
| `0..1` | keins oder eins, also optional |
| `*` oder `0..*` | beliebig viele, auch keins |
| `1..*` | mindestens eins |
| `2..5` | zwischen zwei und fünf |

Die Multiplizität steht am **Ende der Linie, das sie beschreibt**: `Kunde 1 —— * Bestellung`
heißt, ein Kunde hat beliebig viele Bestellungen und jede Bestellung genau einen Kunden.

## ERM: Kardinalitäten

Zwei Notationen, die man auseinanderhalten muss.

**Chen-Notation** (Zahlenpaar an der Beziehung):

| Angabe | Bedeutung |
|---|---|
| 1:1 | jeder Entität auf beiden Seiten steht genau eine gegenüber |
| 1:n | einer links, beliebig viele rechts |
| m:n | beliebig viele auf beiden Seiten |

**Krähenfuß-Notation** (Symbole am Linienende):

| Symbol | Bedeutung |
|---|---|
| senkrechter Strich | genau eins (Pflicht) |
| Kreis | null (optional) |
| Krähenfuß (drei Striche) | viele |
| Kreis + Krähenfuß | null oder viele |
| Strich + Krähenfuß | eins oder viele |

**m:n lässt sich relational nicht direkt abbilden.** Es braucht eine Zwischentabelle mit
den beiden Fremdschlüsseln als zusammengesetztem Primärschlüssel.

## Anwendungsfalldiagramm

| Element | Notation |
|---|---|
| Akteur | Strichmännchen, außerhalb der Systemgrenze |
| Anwendungsfall | Ellipse mit Verb im Namen |
| Systemgrenze | Rechteck um die Anwendungsfälle |
| Assoziation | durchgezogene Linie zwischen Akteur und Anwendungsfall |
| `<<include>>` | gestrichelter Pfeil, zeigt auf den **eingeschlossenen** Fall; wird immer ausgeführt |
| `<<extend>>` | gestrichelter Pfeil, zeigt auf den **erweiterten** Fall; wird nur unter Bedingung ausgeführt |
| Generalisierung | durchgezogen, leeres Dreieck |

Die Pfeilrichtung bei `include` und `extend` ist die häufigste Fehlerquelle. Eselsbrücke:

- `<<include>>` zeigt **hin zu dem, was mit eingeschlossen wird** (A ruft B → Pfeil A → B)
- `<<extend>>` zeigt **weg von dem Erweiternden hin zum Erweiterten** (B erweitert A →
  Pfeil B → A)

Beide Pfeile zeigen also von der Seite weg, die als Basis dient — nur bei `extend` ist die
Basis der erweiterte Fall.

## Programmablaufplan gegen Struktogramm

| Element | PAP (DIN 66001) | Struktogramm (DIN 66261) |
|---|---|---|
| Anfang und Ende | abgerundetes Rechteck | oberer und unterer Rand des Blocks |
| Anweisung | Rechteck | Rechteck über die volle Breite |
| Verzweigung | Raute | Dreieck oben im Block, Zweige daneben |
| Schleife | Raute mit Rücksprungpfeil | umschließender Rahmen |
| Ein- und Ausgabe | Parallelogramm | Rechteck (nicht eigens dargestellt) |
| Unterprogramm | Rechteck mit doppelten Seitenlinien | Rechteck mit doppelten Seitenlinien |
| Verbindung | Pfeil | — es gibt keine, die Reihenfolge ist die Anordnung |

Der wesentliche Unterschied: Im Struktogramm gibt es **keine Sprünge**. Es kann nur
darstellen, was strukturierte Programmierung erlaubt — und genau darin liegt sein Zweck.

## Sequenzdiagramm

| Element | Notation |
|---|---|
| Objekt | Rechteck oben mit `name:Klasse` |
| Lebenslinie | gestrichelte Senkrechte |
| Aktivierung | schmales Rechteck auf der Lebenslinie |
| Synchrone Nachricht | durchgezogener Pfeil, **gefüllte** Spitze |
| Asynchrone Nachricht | durchgezogener Pfeil, **offene** Spitze |
| Antwort | **gestrichelter** Pfeil |
| Erzeugung | Pfeil auf das Objektrechteck, `<<create>>` |
| Zerstörung | Kreuz am Ende der Lebenslinie |

Fragmente: `alt` Alternative, `opt` optional, `loop` Wiederholung, `par` parallel,
`ref` Verweis.

## Zustandsdiagramm

```text
Ereignis [Bedingung] / Aktion
```

| Element | Notation |
|---|---|
| Startzustand | ausgefüllter Kreis, genau einer |
| Zustand | Rechteck mit runden Ecken, Name ist ein Substantiv oder Partizip |
| Transition | Pfeil mit der Beschriftung oben |
| Endzustand | Kreis mit ausgefülltem Kern, mehrere erlaubt |

Innerhalb eines Zustands: `entry /` beim Betreten, `do /` währenddessen, `exit /` beim
Verlassen.

## Aktivitätsdiagramm

| Element | Notation | Wartet auf |
|---|---|---|
| Entscheidung | Raute, ein Eingang | nichts |
| Zusammenführung | Raute, ein Ausgang | **nichts** |
| Gabelung (Fork) | dicker Balken, ein Eingang | nichts |
| Vereinigung (Join) | dicker Balken, ein Ausgang | **alle** eingehenden Zweige |

Raute gegen Balken ist der Kern: Die Raute wartet nie, der Balken wartet auf alles.
