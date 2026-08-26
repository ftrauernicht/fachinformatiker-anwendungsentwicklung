# Struktogramm (Nassi-Shneiderman)

> **Seit dem Prüfungskatalog 2025 nicht mehr Bestandteil der Abschlussprüfung.** An seine Stelle treten Pseudocode und das [Aktivitätsdiagramm](07-aktivitaetsdiagramm.md); wer eine Pseudocode-Aufgabe mit einem Struktogramm beantwortet, bekommt dafür keine Punkte mehr. Die Notation bleibt in dieser Sammlung, weil sie im Berufsschulunterricht weiter vorkommt und Schachtelung daran besonders anschaulich ist. Einzelheiten in [Die Abschlussprüfung im Überblick](../00-pruefung.md), der Ersatz in [Algorithmen](../10-algorithmen.md).

## Inhaltsverzeichnis

- [Nassi-Shneiderman / Struktogramm](#nassi-shneiderman--struktogramm)
  - [Erklärung](#erklärung)
  - [Diagrammblöcke](#diagrammblöcke)
    - [Process Symbol](#process-symbol)
    - [Decision Symbol](#decision-symbol)
      - [1. Möglicher Block](#1-möglicher-block)
      - [2. Möglicher Block](#2-möglicher-block)
      - [Beispiel Verschachtelung](#beispiel-verschachtelung)
      - [Case-Statement](#case-statement)
    - [Schleifen](#schleifen)
      - [Iteration Symbol](#iteration-symbol)

## Nassi-Shneiderman / Struktogramm

[^1]

### Erklärung

Ein Nassi-Shneiderman-Diagramm ist ein Diagrammtyp zur Darstellung von Programmentwürfen im Rahmen der Methode der Strukturierten Programmierung.

Da Nassi-Shneiderman-Diagramme Programmstrukturen und Kontrollstrukturen darstellen, werden sie auch als **Struktogramme** bezeichnet.

### Diagrammblöcke

Die meisten der nachfolgenden Strukturblöcke können ineinander geschachtelt werden. Das aus den unterschiedlichen Strukturblöcken zusammengesetzte Struktogramm ist im Ganzen rechteckig, also genauso breit wie sein breitester Strukturblock.

#### Process Symbol

[![Process Symbol](../../assets/img/nassi-shneiderman/sequence.png "Process Symbol")](https://de.wikipedia.org/wiki/Nassi-Shneiderman-Diagramm#Process_Symbol)

- Jede Anweisung wird in einen rechteckigen Strukturblock geschrieben.
- Die Strukturblöcke werden nacheinander von oben nach unten durchlaufen.
- Leere Strukturblöcke sind nur in Verzweigungen zulässig.
- Alternative Begriffe: Folge, Befehlsfolge, Anweisungsfolge, Anweisungsblock, Linearer Ablauf, Sequenz.

#### Decision Symbol

Alternative Begriffe: Verzweigung, Alternative, Selektion

##### 1. Möglicher Block

[![Decision Symbol 1](../../assets/img/nassi-shneiderman/single-selection.png "Einfachauswahl")](https://de.wikipedia.org/wiki/Nassi-Shneiderman-Diagramm#Decision_Symbol)

- Nur wenn die Bedingung zutreffend ist, wird der Anweisungsblock 1 durchlaufen `(if)`. Trifft die Bedingung nicht zu, wird der Durchlauf ohne eine weiter Anweisung fortgeführt (Austritt unten).
- Alternative Begriffe: Bedingte Verarbeitung, Einfache Auswahl/Selektion, Einfache Verzweigung.

##### 2. Möglicher Block

[![Decision Symbol 2](../../assets/img/nassi-shneiderman/dual-selection.png "Zweifachauswahl")](https://de.wikipedia.org/wiki/Nassi-Shneiderman-Diagramm#Decision_Symbol)

- Wenn die Bedingung Zutreffend ist, wir der erste Anweisungsblock durchlaufen. Tritt die Bedingung nicht zu, wird der zweite Anweisungsblock durchlaufen. `(if else)`
- Alternative Begriffe: Einfacher Alternative, Zweifache Auswahl, Alternative Verzweigung/Verarbeitung.

##### Beispiel Verschachtelung

[![Mehrfachauswahl](../../assets/img/nassi-shneiderman/multiple-selection.png "Mehrfachauswahl")](https://de.wikipedia.org/wiki/Nassi-Shneiderman-Diagramm#Decision_Symbol)

- Eine Verschachtelung ist im Ja und Nein Fall möglich.

##### Case-Statement

[![Case-Statement](../../assets/img/nassi-shneiderman/case-selection.png "Case-Statement")](https://de.wikipedia.org/wiki/Nassi-Shneiderman-Diagramm#Decision_Symbol)

- Der Wert von **Variable** kann bedingt auf Gleichheit aber auch auf Bereiche (größer/kleiner bei Zahlen) geprüft werden. Der entsprechend Zutreffende "Fall" mit dem zugehörigen Anweisungsblock wird durchlaufen (`switch`, `select`).
- Alternative Begriffe: Mehrfache Alternative, Fallauswahl, Mehrfachauswahl, Case, Select.

#### Schleifen

##### Iteration Symbol

[^1]: <https://de.wikipedia.org/wiki/Nassi-Shneiderman-Diagramm>
