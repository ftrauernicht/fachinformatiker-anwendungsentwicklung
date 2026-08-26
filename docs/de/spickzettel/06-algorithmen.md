# Spickzettel: Algorithmen

## Inhaltsverzeichnis

- [Pseudocode in einer Minute](#pseudocode-in-einer-minute)
- [Kontrollstrukturen](#kontrollstrukturen)
- [Komplexität](#komplexität)
- [Suchen](#suchen)
- [Sortieren](#sortieren)
  - [Bubblesort an [5, 2, 9, 1]](#bubblesort-an-5-2-9-1)
- [Die fünf Fehler, die am häufigsten passieren](#die-fünf-fehler-die-am-häufigsten-passieren)

## Pseudocode in einer Minute

| Weglassen | Behalten |
|---|---|
| `{` `}` | Einrückung |
| `;` | eine Anweisung je Zeile |
| Datentypen, Deklarationen | sprechende Namen |
| `import`, Klassengerüst, Einstiegsmethode | die geforderte Funktion |

```text
name(parameter1, parameter2)          Funktionskopf
    wenn bedingung                    Verzweigung
        anweisung
    sonst wenn bedingung
        anweisung
    sonst
        anweisung

    für i von 0 bis n - 1             Zählschleife
        anweisung

    solange bedingung                 kopfgesteuert
        anweisung

    wiederhole                        fußgesteuert
        anweisung
    bis bedingung

    gib wert zurück
```

Es kommt auf die Logik an, nicht auf die Schreibweise — vor allem auf die Abbruchbedingungen.

## Kontrollstrukturen

| Form | Bedingung geprüft | Läuft mindestens |
|---|---|---|
| `solange` / `while` | vor dem Durchlauf | 0-mal |
| `wiederhole … bis` / `do-while` | nach dem Durchlauf | 1-mal |
| `für` / `for` | vor dem Durchlauf | 0-mal |

Drei Grundbausteine, aus denen sich alles bauen lässt: **Sequenz, Verzweigung, Wiederholung** (Satz von Böhm und Jacopini).

## Komplexität

| Klasse | Name | Beispiel | Schritte bei n = 1.000 |
|---|---|---|---|
| O(1) | konstant | Zugriff über den Index | 1 |
| O(log n) | logarithmisch | binäre Suche | 10 |
| O(n) | linear | lineare Suche | 1.000 |
| O(n log n) | linear-logarithmisch | Mergesort, Quicksort | 10.000 |
| O(n²) | quadratisch | Bubble-, Selection-, Insertionsort | 1.000.000 |
| O(2ⁿ) | exponentiell | Durchprobieren aller Möglichkeiten | unbrauchbar |

Ablesen aus Code: eine Schleife → O(n). Schleife in Schleife → O(n²). Halbierung je Schritt → O(log n).

## Suchen

| Verfahren | Voraussetzung | Aufwand | Vergleiche bei 1.000 |
|---|---|---|---|
| lineare Suche | keine | O(n) | bis 1.000 |
| binäre Suche | **sortiert** | O(log n) | bis 10 |

```text
binäreSuche(feld, gesucht)
    links = 0
    rechts = länge(feld) - 1
    solange links <= rechts               <= , nicht <
        mitte = (links + rechts) / 2
        wenn feld[mitte] == gesucht
            gib mitte zurück
        wenn feld[mitte] < gesucht
            links = mitte + 1             + 1 , nicht mitte
        sonst
            rechts = mitte - 1
    gib -1 zurück
```

## Sortieren

| | Bubblesort | Selectionsort | Insertionsort |
|---|---|---|---|
| Idee | Nachbarn tauschen | Kleinstes nach vorn holen | An passender Stelle einfügen |
| Bester Fall | O(n) mit Abbruchprüfung | O(n²) | O(n) |
| Mittel und schlechtester Fall | O(n²) | O(n²) | O(n²) |
| Tauschvorgänge | viele | höchstens n − 1 | mittel |
| Stabil | ja | **nein** | ja |
| Gut bei | — | teurem Tauschen | fast sortierten Daten |

```text
bubblesort(feld)                          selectionsort(feld)
    für i von 0 bis n - 2                     für i von 0 bis n - 2
        für j von 0 bis n - 2 - i                 kleinstes = i
            wenn feld[j] > feld[j + 1]            für j von i + 1 bis n - 1
                tausche                               wenn feld[j] < feld[kleinstes]
                                                          kleinstes = j
                                                  tausche feld[i] und feld[kleinstes]

insertionsort(feld)
    für i von 1 bis n - 1
        aktuell = feld[i]
        j = i - 1
        solange j >= 0 und feld[j] > aktuell
            feld[j + 1] = feld[j]
            j = j - 1
        feld[j + 1] = aktuell
```

### Bubblesort an [5, 2, 9, 1]

| Durchlauf | Feld danach |
|---|---|
| Start | 5, 2, 9, 1 |
| 1 | 2, 5, 1, 9 |
| 2 | 2, 1, 5, 9 |
| 3 | 1, 2, 5, 9 |

**Stabil** heißt: gleiche Schlüssel behalten ihre Reihenfolge. Wichtig beim Sortieren nach mehreren Kriterien nacheinander.

## Die fünf Fehler, die am häufigsten passieren

1. **Off by one** — `bis n - 1` statt `bis n - 2`, wenn im Rumpf auf `feld[i + 1]` zugegriffen wird.
2. **`<` statt `<=`** in der binären Suche — das letzte Element wird nie geprüft.
3. **`mitte` statt `mitte ± 1`** — Endlosschleife.
4. **Startwert 0 beim Maximum** — versagt bei lauter negativen Zahlen. Richtig ist `feld[0]`.
5. **Rekursion ohne Abbruchfall** — der Aufrufstapel läuft über.
