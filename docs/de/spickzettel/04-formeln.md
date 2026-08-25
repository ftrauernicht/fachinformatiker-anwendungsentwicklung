# Spickzettel: Formeln

## Inhaltsverzeichnis

- [Wirtschaftlichkeit](#wirtschaftlichkeit)
  - [Beispiel Break-even](#beispiel-break-even)
- [Netzplan](#netzplan)
  - [Vorgangsknoten](#vorgangsknoten)
- [Verfügbarkeit](#verfügbarkeit)
- [Speicher und Übertragung](#speicher-und-übertragung)
  - [Übertragungsdauer](#übertragungsdauer)
  - [RAID-Nettokapazität](#raid-nettokapazität)
- [Zahlensysteme](#zahlensysteme)

## Wirtschaftlichkeit

| Größe | Formel |
|---|---|
| Deckungsbeitrag je Stück | Verkaufspreis − variable Stückkosten |
| Gesamtdeckungsbeitrag | Deckungsbeitrag je Stück × Menge |
| Gewinn | Gesamtdeckungsbeitrag − Fixkosten |
| Break-even-Menge | Fixkosten ÷ Deckungsbeitrag je Stück |
| Break-even-Umsatz | Break-even-Menge × Verkaufspreis |
| Amortisationszeit | Investition ÷ jährlicher Rückfluss |
| Jährlicher Rückfluss | Gewinn + Abschreibung |
| Lineare Abschreibung | (Anschaffungswert − Restwert) ÷ Nutzungsdauer |
| Rentabilität | Gewinn ÷ eingesetztes Kapital × 100 % |
| Produktivität | Ausbringungsmenge ÷ Einsatzmenge |
| Wirtschaftlichkeit | Ertrag ÷ Aufwand |

**Rückfluss ist nicht Umsatz.** Wer bei der Amortisationszeit den Umsatz einsetzt, bekommt
eine viel zu kurze Zeit heraus. Die Abschreibung kommt hinzu, weil sie zwar Kosten mindert,
aber kein Geld abfließen lässt.

### Beispiel Break-even

Verkaufspreis 80 €, variable Kosten 30 €, Fixkosten 20.000 € im Monat.

```text
Deckungsbeitrag  = 80 € − 30 €        = 50 € je Stück
Break-even-Menge = 20.000 € ÷ 50 €    = 400 Stück
Break-even-Umsatz = 400 × 80 €        = 32.000 €
```

Ab dem 401. Stück entsteht Gewinn.

## Netzplan

| Größe | Formel |
|---|---|
| FEZ (frühester Endzeitpunkt) | FAZ + D |
| FAZ eines Vorgangs | **größter** FEZ aller Vorgänger |
| SAZ (spätester Anfangszeitpunkt) | SEZ − D |
| SEZ eines Vorgangs | **kleinster** SAZ aller Nachfolger |
| Gesamtpuffer GP | SAZ − FAZ, gleichwertig SEZ − FEZ |
| Freier Puffer FP | kleinster FAZ der Nachfolger − FEZ |

- **Kritischer Pfad:** alle Vorgänge mit GP = 0. Seine Länge ist die Projektdauer.
- Vorwärtsrechnung von links: **Maximum** der Vorgänger.
- Rückwärtsrechnung von rechts: **Minimum** der Nachfolger.
- Es gilt immer FP ≤ GP.

### Vorgangsknoten

| | | |
|---|---|---|
| **FAZ** | **D** | **FEZ** |
| **Nr.** | **Vorgangsbezeichnung** | |
| **SAZ** | **GP** · **FP** | **SEZ** |

## Verfügbarkeit

Verfügbarkeit in Prozent = Betriebszeit ÷ (Betriebszeit + Ausfallzeit) × 100

Zulässige Ausfallzeit **pro Monat mit 30 Tagen** (720 Stunden):

| Verfügbarkeit | Ausfall pro Monat | Ausfall pro Jahr |
|---|---|---|
| 99 % | 7 h 12 min | 3 Tage 15 h |
| 99,5 % | 3 h 36 min | 1 Tag 20 h |
| 99,9 % | 43 min | 8 h 46 min |
| 99,95 % | 22 min | 4 h 23 min |
| 99,99 % | 4 min 19 s | 53 min |
| 99,999 % | 26 s | 5 min 15 s |

**Aufpassen:** Bezieht sich die Zusage auf die **Servicezeit** statt auf den Kalendermonat,
ändert sich alles. Mo–Fr 8–18 Uhr sind rund 220 statt 720 Stunden im Monat.

Weitere Kennzahlen:

| Kennzahl | Bedeutung |
|---|---|
| MTBF | Mean Time Between Failures — mittlere Zeit zwischen zwei Ausfällen |
| MTTR | Mean Time To Repair — mittlere Reparaturdauer |
| Verfügbarkeit | MTBF ÷ (MTBF + MTTR) |
| RTO | Recovery Time Objective — wie lange darf der Ausfall dauern |
| RPO | Recovery Point Objective — wie viel Datenverlust ist hinnehmbar |

## Speicher und Übertragung

| Umrechnung | Wert |
|---|---|
| 1 Byte | 8 Bit |
| 1 kB (dezimal) | 1.000 Byte |
| 1 KiB (binär) | 1.024 Byte |
| 1 MB | 1.000 kB — 1 MiB = 1.024 KiB |
| 1 GB | 1.000 MB — 1 GiB = 1.024 MiB |

**Netzwerkgeschwindigkeiten stehen in Bit pro Sekunde, Dateigrößen in Byte.** Das ist der
Faktor 8, der in Prüfungsaufgaben regelmäßig fehlt.

### Übertragungsdauer

```text
Dauer [s] = Datenmenge [Bit] ÷ Übertragungsrate [Bit/s]
```

Beispiel: 500 MB über 100 Mbit/s.

```text
500 MB · 8         = 4.000 Mbit
4.000 Mbit ÷ 100   = 40 Sekunden (theoretisch)
```

In der Praxis kommen Protokoll-Overhead und Kollisionen dazu; ein Aufschlag von 10–20 % ist
realistisch und in Aufgaben oft ausdrücklich gefordert.

### RAID-Nettokapazität

| Level | Nettokapazität bei *n* gleich großen Platten |
|---|---|
| RAID 0 | n × Größe |
| RAID 1 | Größe (bei zwei Platten) |
| RAID 5 | (n − 1) × Größe, mindestens 3 Platten |
| RAID 6 | (n − 2) × Größe, mindestens 4 Platten |
| RAID 10 | n ÷ 2 × Größe, mindestens 4 Platten |

## Zahlensysteme

| Dezimal | Binär | Hexadezimal | Oktal |
|---|---|---|---|
| 0 | 0000 | 0 | 0 |
| 1 | 0001 | 1 | 1 |
| 2 | 0010 | 2 | 2 |
| 3 | 0011 | 3 | 3 |
| 4 | 0100 | 4 | 4 |
| 5 | 0101 | 5 | 5 |
| 6 | 0110 | 6 | 6 |
| 7 | 0111 | 7 | 7 |
| 8 | 1000 | 8 | 10 |
| 9 | 1001 | 9 | 11 |
| 10 | 1010 | A | 12 |
| 11 | 1011 | B | 13 |
| 12 | 1100 | C | 14 |
| 13 | 1101 | D | 15 |
| 14 | 1110 | E | 16 |
| 15 | 1111 | F | 17 |

**Binär → hexadezimal:** von rechts in Vierergruppen aufteilen, jede Gruppe einzeln
umwandeln.

`11010110` → `1101` `0110` → `D` `6` → **0xD6**

**Dezimal → binär:** fortgesetzt durch 2 teilen, die Reste von unten nach oben lesen.

```text
214 : 2 = 107 Rest 0
107 : 2 =  53 Rest 1
 53 : 2 =  26 Rest 1
 26 : 2 =  13 Rest 0
 13 : 2 =   6 Rest 1
  6 : 2 =   3 Rest 0
  3 : 2 =   1 Rest 1
  1 : 2 =   0 Rest 1
                    -> 11010110
```

Zweierpotenzen, die man auswendig können sollte:

| n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 16 | 20 | 24 | 32 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2ⁿ | 2 | 4 | 8 | 16 | 32 | 64 | 128 | 256 | 512 | 1.024 | 65.536 | 1.048.576 | 16.777.216 | 4.294.967.296 |
