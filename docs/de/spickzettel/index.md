# Spickzettel

Dichte Nachschlage-Seiten: Tabellen, Formeln und Notationen ohne erklärenden Fließtext.
Gedacht für die Wiederholung kurz vor der Prüfung, wenn der Stoff einmal durchgearbeitet
ist — zum Lernen taugen sie nicht, dafür sind die [Kapitel](../index.md) da.

!!! warning "In die Prüfung darf nichts davon mit"

    Erlaubte Hilfsmittel legt die IHK fest, und ein selbst mitgebrachter Spickzettel gehört
    nirgends dazu. Diese Seiten sind zum Auswendiglernen gedacht, nicht zum Mitnehmen.

| Spickzettel | Enthält |
|---|---|
| [Subnetting](01-subnetting.md) | Präfixtabelle, Rechenweg in vier Schritten, private Bereiche, Binärumrechnung |
| [SQL](02-sql.md) | Klauselreihenfolge, Verbundarten, Aggregate, DDL und DML, Datentypen |
| [UML-Notation](03-uml-notation.md) | Sichtbarkeiten, Beziehungen, Multiplizitäten, Kardinalitäten, alle Diagrammsymbole |
| [Formeln](04-formeln.md) | Wirtschaftlichkeit, Netzplan, Verfügbarkeit, Speicher, Zahlensysteme |
| [Tabellenkalkulation](05-excel.md) | Bezüge, WENN, SVERWEIS, Fehlerwerte |
| [Algorithmen](06-algorithmen.md) | Pseudocode-Gerüst, Komplexitätsklassen, Suchen, die drei Sortierverfahren |

## Die fünf Zahlen, die man auswendig braucht

| Was | Wert |
|---|---|
| Nutzbare Hosts bei *n* Hostbits | 2ⁿ − 2 |
| RAID 5 Nettokapazität | (Anzahl Platten − 1) × Plattengröße |
| Break-even-Menge | Fixkosten ÷ Deckungsbeitrag je Stück |
| Zulässiger Ausfall bei 99,9 % im Monat | 43 Minuten |
| Faktor zwischen Byte und Bit | 8 |

## Die fünf Verwechslungen, die am häufigsten Punkte kosten

1. **WHERE gegen HAVING** — WHERE filtert Zeilen vor der Gruppierung, HAVING Gruppen danach.
2. **Aggregation gegen Komposition** — leere Raute, das Teil überlebt; gefüllte Raute, es
   stirbt mit. Die Raute steht immer am Ganzen.
3. **Authentisierung gegen Authentifizierung** — erst behauptet der Benutzer, wer er ist,
   dann prüft das System die Behauptung.
4. **Incident gegen Problem** — der Incident ist die Störung, das Problem ihre Ursache.
5. **Raute gegen Balken im Aktivitätsdiagramm** — die Raute wartet nie, der Balken wartet
   auf alle Zweige.
