# Prüfungsfragen: Datenbanken

## Inhaltsverzeichnis

- [Normalisierung](#normalisierung)
  - [1. Nennen Sie die Bedingungen der ersten, zweiten und dritten Normalform.](#1-nennen-sie-die-bedingungen-der-ersten-zweiten-und-dritten-normalform)
  - [2. Warum ist die Tabelle nicht in der 2. Normalform?](#2-warum-ist-die-tabelle-nicht-in-der-2-normalform)
  - [3. Nennen Sie die drei Anomalien und je ein Beispiel.](#3-nennen-sie-die-drei-anomalien-und-je-ein-beispiel)
  - [4. Wann normalisiert man bewusst **nicht** bis zur 3. Normalform?](#4-wann-normalisiert-man-bewusst-nicht-bis-zur-3-normalform)
- [SQL](#sql)
  - [5. Was ist der Unterschied zwischen WHERE und HAVING?](#5-was-ist-der-unterschied-zwischen-where-und-having)
  - [6. Was ist der Unterschied zwischen INNER JOIN und LEFT JOIN?](#6-was-ist-der-unterschied-zwischen-inner-join-und-left-join)
  - [7. Was ist der Unterschied zwischen UNION und UNION ALL?](#7-was-ist-der-unterschied-zwischen-union-und-union-all)
  - [8. Was macht DELETE, was TRUNCATE, was DROP?](#8-was-macht-delete-was-truncate-was-drop)
  - [9. Nennen Sie die Sprachgruppen von SQL mit je zwei Befehlen.](#9-nennen-sie-die-sprachgruppen-von-sql-mit-je-zwei-befehlen)
- [Modellierung und Transaktionen](#modellierung-und-transaktionen)
  - [10. Wie wird eine n:m-Beziehung in einer relationalen Datenbank umgesetzt?](#10-wie-wird-eine-nm-beziehung-in-einer-relationalen-datenbank-umgesetzt)
  - [11. Wofür steht ACID?](#11-wofür-steht-acid)
  - [12. Was ist der Unterschied zwischen Primärschlüssel und Fremdschlüssel?](#12-was-ist-der-unterschied-zwischen-primärschlüssel-und-fremdschlüssel)

## Normalisierung

### 1. Nennen Sie die Bedingungen der ersten, zweiten und dritten Normalform.

<details markdown="1">
<summary>Antwort</summary>

| Form | Bedingung |
|---|---|
| **1. NF** | Jedes Attribut hat einen **atomaren** Wert. Keine Listen, keine Wiederholungsgruppen in einem Feld. |
| **2. NF** | 1. NF **und** jedes Nichtschlüsselattribut hängt vom **gesamten** Schlüssel ab, nicht nur von einem Teil davon. Relevant nur bei zusammengesetzten Schlüsseln. |
| **3. NF** | 2. NF **und** kein Nichtschlüsselattribut hängt von einem anderen Nichtschlüsselattribut ab (keine transitive Abhängigkeit). |

Merksatz: *Der Schlüssel, der ganze Schlüssel und nichts als der Schlüssel.*

</details>

### 2. Warum ist die Tabelle nicht in der 2. Normalform?

`Bestellung(BestellNr, ArtikelNr, Menge, Artikelbezeichnung)`, Schlüssel ist
`(BestellNr, ArtikelNr)`.

<details markdown="1">
<summary>Antwort</summary>

`Artikelbezeichnung` hängt nur von `ArtikelNr` ab, also von einem **Teil** des
zusammengesetzten Schlüssels. `Menge` dagegen hängt richtigerweise von beiden ab.

Auflösung:

```text
Bestellposition(BestellNr, ArtikelNr, Menge)
Artikel(ArtikelNr, Artikelbezeichnung)
```

</details>

### 3. Nennen Sie die drei Anomalien und je ein Beispiel.

<details markdown="1">
<summary>Antwort</summary>

- **Einfüge-Anomalie:** Ein neuer Artikel lässt sich nicht anlegen, solange er nicht
  bestellt wurde — weil die Bestellnummer Teil des Schlüssels ist und nicht leer sein darf.
- **Änderungs-Anomalie:** Die Artikelbezeichnung ändert sich und muss in jeder Zeile
  nachgezogen werden. Wird eine übersehen, widerspricht sich die Datenbank.
- **Lösch-Anomalie:** Mit der letzten Bestellung eines Artikels verschwindet auch die
  Information, dass es diesen Artikel überhaupt gibt.

Alle drei verschwinden durch Normalisierung.

</details>

### 4. Wann normalisiert man bewusst **nicht** bis zur 3. Normalform?

<details markdown="1">
<summary>Antwort</summary>

Wenn die Lesegeschwindigkeit wichtiger ist als die Redundanzfreiheit. Jede weitere
Normalform bedeutet mehr Tabellen und damit mehr Verbundoperationen (Joins) beim Lesen.

Typische Fälle: Auswertungs- und Berichtsdatenbanken (Data Warehouse), Zwischenspeicher,
historisierte Daten, bei denen der damalige Wert gerade **nicht** mitwandern soll — etwa
der Preis auf einer bereits geschriebenen Rechnung.

Diese bewusste Rücknahme heißt **Denormalisierung**. Sie erkauft Geschwindigkeit mit dem
Risiko widersprüchlicher Daten.

</details>

## SQL

### 5. Was ist der Unterschied zwischen WHERE und HAVING?

<details markdown="1">
<summary>Antwort</summary>

**WHERE** filtert **einzelne Zeilen**, bevor gruppiert wird. **HAVING** filtert
**Gruppen**, nachdem `GROUP BY` sie gebildet hat — und darf deshalb als einziges mit
Aggregatfunktionen arbeiten.

```sql
SELECT KundenNr, COUNT(*) AS Anzahl
FROM Bestellung
WHERE Datum >= '2026-01-01'   -- welche Zeilen zählen mit
GROUP BY KundenNr
HAVING COUNT(*) > 5;          -- welche Gruppen bleiben übrig
```

Ein `WHERE COUNT(*) > 5` ist immer ein Fehler.

</details>

### 6. Was ist der Unterschied zwischen INNER JOIN und LEFT JOIN?

<details markdown="1">
<summary>Antwort</summary>

**INNER JOIN** liefert nur Zeilen, für die es in **beiden** Tabellen einen Partner gibt.

**LEFT JOIN** liefert alle Zeilen der linken Tabelle; wo rechts kein Partner existiert,
stehen `NULL`-Werte.

```sql
-- alle Kunden mit ihren Bestellungen, auch Kunden ohne Bestellung
SELECT k.Name, b.BestellNr
FROM Kunde k
LEFT JOIN Bestellung b ON k.KundenNr = b.KundenNr;
```

Prüfungstypisch: „Alle Kunden, auch die ohne Bestellung" → `LEFT JOIN`. „Alle Kunden, die
bestellt haben" → `INNER JOIN`.

</details>

### 7. Was ist der Unterschied zwischen UNION und UNION ALL?

<details markdown="1">
<summary>Antwort</summary>

Beide hängen die Ergebnismengen zweier Abfragen untereinander. **UNION entfernt
Duplikate**, `UNION ALL` behält sie.

Weil UNION dafür sortieren oder hashen muss, ist es langsamer. Wenn feststeht, dass keine
Duplikate auftreten können, ist `UNION ALL` die richtige Wahl.

Voraussetzung für beide: gleiche Spaltenanzahl und verträgliche Datentypen.

</details>

### 8. Was macht DELETE, was TRUNCATE, was DROP?

<details markdown="1">
<summary>Antwort</summary>

| Befehl | Wirkung | Art |
|---|---|---|
| `DELETE FROM t WHERE …` | löscht einzelne Zeilen, protokolliert, rücknehmbar | DML |
| `TRUNCATE TABLE t` | löscht **alle** Zeilen auf einen Schlag, Struktur bleibt | DDL |
| `DROP TABLE t` | löscht die **Tabelle selbst**, samt Struktur | DDL |

`DELETE` ohne `WHERE` leert die Tabelle ebenfalls, ist aber langsamer, weil jede Zeile
einzeln protokolliert wird. `TRUNCATE` setzt zusätzlich meist den Autowert zurück.

</details>

### 9. Nennen Sie die Sprachgruppen von SQL mit je zwei Befehlen.

<details markdown="1">
<summary>Antwort</summary>

| Gruppe | Bedeutung | Befehle |
|---|---|---|
| **DDL** | Data Definition Language | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | Data Manipulation Language | `INSERT`, `UPDATE`, `DELETE`, `SELECT` |
| **DCL** | Data Control Language | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

`SELECT` wird gelegentlich als eigene Gruppe DQL geführt.

</details>

## Modellierung und Transaktionen

### 10. Wie wird eine n:m-Beziehung in einer relationalen Datenbank umgesetzt?

<details markdown="1">
<summary>Antwort</summary>

Über eine **Zwischentabelle** (Verbindungs- oder Kopplungstabelle). Direkt lässt sich
n:m nicht abbilden.

```text
Student(MatrNr, Name)
Kurs(KursNr, Titel)
Belegung(MatrNr, KursNr, Note)      <- Zwischentabelle
```

Der Schlüssel der Zwischentabelle ist die Kombination beider Fremdschlüssel. Attribute,
die zur *Beziehung* gehören und nicht zu einer der beiden Seiten — hier die Note —
gehören genau dorthin.

</details>

### 11. Wofür steht ACID?

<details markdown="1">
<summary>Antwort</summary>

| | | Bedeutung |
|---|---|---|
| **A** | Atomicity (Atomarität) | Eine Transaktion läuft ganz oder gar nicht. |
| **C** | Consistency (Konsistenz) | Vorher und nachher ist die Datenbank in einem gültigen Zustand. |
| **I** | Isolation | Gleichzeitige Transaktionen beeinflussen sich nicht. |
| **D** | Durability (Dauerhaftigkeit) | Nach dem Commit überlebt das Ergebnis auch einen Stromausfall. |

Standardbeispiel für Atomarität: eine Überweisung besteht aus Abbuchen und Gutschreiben.
Bricht sie dazwischen ab, darf **keins von beidem** stehen bleiben.

</details>

### 12. Was ist der Unterschied zwischen Primärschlüssel und Fremdschlüssel?

<details markdown="1">
<summary>Antwort</summary>

Ein **Primärschlüssel** identifiziert eine Zeile in *seiner eigenen* Tabelle eindeutig. Er
ist eindeutig, nie `NULL` und ändert sich idealerweise nie.

Ein **Fremdschlüssel** verweist auf den Primärschlüssel einer *anderen* Tabelle. Er darf
mehrfach vorkommen und je nach Modellierung auch `NULL` sein — dann besteht die Beziehung
für diese Zeile eben nicht.

Der Fremdschlüssel sichert die **referentielle Integrität**: es kann keine Bestellung zu
einem Kunden geben, den es nicht gibt.

</details>
