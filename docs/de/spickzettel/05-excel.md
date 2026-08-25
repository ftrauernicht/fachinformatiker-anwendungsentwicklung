# Spickzettel: Tabellenkalkulation

## Inhaltsverzeichnis

- [Warum das hier steht](#warum-das-hier-steht)
- [Bezüge](#bezüge)
- [Grundfunktionen](#grundfunktionen)
- [Bedingungen](#bedingungen)
- [Bedingtes Zählen und Rechnen](#bedingtes-zählen-und-rechnen)
- [Nachschlagen](#nachschlagen)
- [Fehlerwerte](#fehlerwerte)
- [Was in Prüfungsantworten zählt](#was-in-prüfungsantworten-zählt)

## Warum das hier steht

In der Abschlussprüfung 2023 wurden in GA2 Excel-Formeln abgefragt. Damit ist
Tabellenkalkulation kein Randthema — auch wenn sie im Rahmenlehrplan wenig Raum einnimmt.

Die Aufgaben verlangen meist: eine Formel aufschreiben, eine gegebene Formel erklären, oder
sagen, was beim Kopieren einer Formel passiert.

## Bezüge

| Schreibweise | Verhalten beim Kopieren |
|---|---|
| `A1` | relativ — Spalte und Zeile wandern mit |
| `$A$1` | absolut — bleibt fest |
| `$A1` | Spalte fest, Zeile wandert |
| `A$1` | Zeile fest, Spalte wandert |

Das Dollarzeichen friert ein, was **dahinter** steht. In Excel schaltet <kbd>F4</kbd>
zwischen den vier Formen um.

Typische Aufgabe: In `C2` steht `=A2*$B$1`, kopiert nach `C3` wird daraus `=A3*$B$1`. Der
Faktor in B1 bleibt stehen, der Wert aus Spalte A wandert mit.

## Grundfunktionen

| Deutsch | Englisch | Zweck |
|---|---|---|
| `SUMME` | `SUM` | addieren |
| `MITTELWERT` | `AVERAGE` | Durchschnitt |
| `ANZAHL` | `COUNT` | Zellen **mit Zahlen** zählen |
| `ANZAHL2` | `COUNTA` | nicht leere Zellen zählen |
| `MIN`, `MAX` | `MIN`, `MAX` | kleinster, größter Wert |
| `RUNDEN` | `ROUND` | kaufmännisch runden |
| `AUFRUNDEN`, `ABRUNDEN` | `ROUNDUP`, `ROUNDDOWN` | in eine Richtung runden |
| `HEUTE` | `TODAY` | heutiges Datum |
| `JETZT` | `NOW` | Datum und Uhrzeit |

```text
=SUMME(B2:B20)
=MITTELWERT(B2:B20)
=RUNDEN(B2*1,19; 2)
```

Trennzeichen: In der deutschen Oberfläche werden Argumente mit **Semikolon** getrennt und
Dezimalstellen mit **Komma** geschrieben.

## Bedingungen

```text
=WENN(B2>=50; "bestanden"; "durchgefallen")
=WENN(B2>=90; "sehr gut"; WENN(B2>=75; "gut"; "befriedigend"))
=WENN(UND(B2>=50; C2="ja"); "ok"; "prüfen")
=WENN(ODER(B2>100; C2>100); "Sonderfall"; "normal")
=WENNFEHLER(A2/B2; "Division durch null")
```

| Deutsch | Englisch |
|---|---|
| `WENN` | `IF` |
| `UND`, `ODER`, `NICHT` | `AND`, `OR`, `NOT` |
| `WENNFEHLER` | `IFERROR` |

Verschachtelte `WENN` liest man von außen nach innen: Die erste erfüllte Bedingung
gewinnt, alle folgenden werden nicht mehr geprüft. Deshalb muss die Reihenfolge stimmen —
mit `>=50` zuerst wäre keine bessere Note mehr erreichbar.

## Bedingtes Zählen und Rechnen

```text
=ZÄHLENWENN(B2:B20; ">=50")
=ZÄHLENWENNS(B2:B20; ">=50"; C2:C20; "Hamburg")
=SUMMEWENN(A2:A20; "Hamburg"; B2:B20)
=SUMMEWENNS(B2:B20; A2:A20; "Hamburg"; C2:C20; ">2026-01-01")
=MITTELWERTWENN(A2:A20; "Hamburg"; B2:B20)
```

Aufpassen bei der Argumentreihenfolge: `SUMMEWENN` nennt zuerst den **Prüfbereich**,
`SUMMEWENNS` zuerst den **Summenbereich**. Das ist keine Schikane, sondern historisch
gewachsen — und eine beliebte Fangfrage.

## Nachschlagen

```text
=SVERWEIS(A2; Tabelle2!$A$2:$C$100; 3; FALSCH)
=WVERWEIS(A2; Tabelle2!$A$1:$Z$3; 2; FALSCH)
=INDEX($C$2:$C$100; VERGLEICH(A2; $A$2:$A$100; 0))
```

| Argument von `SVERWEIS` | Bedeutung |
|---|---|
| 1 | gesuchter Wert |
| 2 | Bereich, in dem gesucht wird — **erste Spalte** enthält das Suchkriterium |
| 3 | Nummer der Spalte im Bereich, deren Wert zurückkommt |
| 4 | `FALSCH` = exakte Übereinstimmung, `WAHR` = ungefähr (Bereich muss sortiert sein) |

Drei Regeln, die fast alle SVERWEIS-Fehler abdecken:

1. Das Suchkriterium muss in der **ersten Spalte** des Bereichs stehen. Nach links kann
   SVERWEIS nicht schauen — dafür braucht es `INDEX` mit `VERGLEICH`.
2. Der Bereich gehört **absolut** gesetzt (`$A$2:$C$100`), sonst verrutscht er beim
   Kopieren.
3. Das vierte Argument gehört fast immer auf `FALSCH`. Mit `WAHR` liefert die Formel bei
   unsortierten Daten still falsche Ergebnisse.

In neueren Versionen ersetzt `XVERWEIS` (`XLOOKUP`) all das und kann auch nach links
suchen.

## Fehlerwerte

| Fehler | Ursache |
|---|---|
| `#DIV/0!` | Division durch null oder durch eine leere Zelle |
| `#NV` | Nachschlagen ohne Treffer (nicht verfügbar) |
| `#WERT!` | falscher Datentyp, etwa Text statt Zahl |
| `#BEZUG!` | Bezug zeigt ins Leere, meist nach dem Löschen einer Spalte |
| `#NAME?` | Funktionsname falsch geschrieben |
| `#ZAHL!` | Ergebnis nicht darstellbar, etwa Wurzel aus einer negativen Zahl |
| `######` | kein Fehler — die Spalte ist nur zu schmal |

## Was in Prüfungsantworten zählt

- **Das Gleichheitszeichen nicht vergessen.** Ohne `=` ist es Text, keine Formel.
- **Semikolon als Argumenttrenner**, nicht Komma.
- **Bereiche absolut setzen**, wenn die Formel kopiert werden soll — und begründen können,
  warum.
- Wird nach der Wirkung des Kopierens gefragt, gehört die **veränderte Formel** in die
  Antwort, nicht nur das Ergebnis.
