# Spickzettel: SQL

## Inhaltsverzeichnis

- [Reihenfolge der Klauseln](#reihenfolge-der-klauseln)
- [WHERE gegen HAVING](#where-gegen-having)
- [Verbundarten](#verbundarten)
- [Aggregatfunktionen](#aggregatfunktionen)
- [Bedingungen](#bedingungen)
- [DDL: Struktur](#ddl-struktur)
- [DML: Daten](#dml-daten)
- [Sprachgruppen](#sprachgruppen)
- [Mengenoperationen](#mengenoperationen)
- [Datentypen](#datentypen)

## Reihenfolge der Klauseln

Geschrieben wird in dieser Reihenfolge:

```sql
SELECT   spalten
FROM     tabelle
JOIN     andere_tabelle ON bedingung
WHERE    zeilenbedingung
GROUP BY spalten
HAVING   gruppenbedingung
ORDER BY spalten [ASC | DESC]
LIMIT    anzahl;
```

**Ausgeführt** wird sie anders, und das erklärt die meisten Fehler:

`FROM` → `JOIN` → `WHERE` → `GROUP BY` → `HAVING` → `SELECT` → `ORDER BY` → `LIMIT`

Daraus folgt: Ein Alias aus `SELECT` ist in `WHERE` noch nicht bekannt (weil `WHERE`
vorher läuft), in `ORDER BY` dagegen schon.

## WHERE gegen HAVING

| | WHERE | HAVING |
|---|---|---|
| Filtert | einzelne Zeilen | Gruppen |
| Läuft | vor `GROUP BY` | nach `GROUP BY` |
| Aggregatfunktionen | **nein** | ja |

```sql
SELECT KundenNr, COUNT(*) AS Anzahl, SUM(Betrag) AS Summe
FROM Bestellung
WHERE Datum >= '2026-01-01'     -- welche Zeilen zählen überhaupt mit
GROUP BY KundenNr
HAVING COUNT(*) > 5             -- welche Gruppen bleiben stehen
ORDER BY Summe DESC;
```

## Verbundarten

| Art | Liefert |
|---|---|
| `INNER JOIN` | nur Zeilen mit Partner in **beiden** Tabellen |
| `LEFT [OUTER] JOIN` | alle Zeilen links, rechts `NULL` wo kein Partner |
| `RIGHT [OUTER] JOIN` | alle Zeilen rechts, links `NULL` wo kein Partner |
| `FULL [OUTER] JOIN` | alle Zeilen beider Seiten |
| `CROSS JOIN` | kartesisches Produkt, jede mit jeder |
| `SELF JOIN` | Tabelle mit sich selbst, über zwei Aliase |

```sql
-- Kunden ohne jede Bestellung finden
SELECT k.Name
FROM Kunde k
LEFT JOIN Bestellung b ON k.KundenNr = b.KundenNr
WHERE b.BestellNr IS NULL;
```

Der Trick in der letzten Zeile ist prüfungstypisch: nach einem `LEFT JOIN` erkennt man die
partnerlosen Zeilen daran, dass die rechte Seite `NULL` ist.

## Aggregatfunktionen

| Funktion | Liefert | NULL-Behandlung |
|---|---|---|
| `COUNT(*)` | Anzahl aller Zeilen | zählt auch Zeilen mit NULL |
| `COUNT(spalte)` | Anzahl der Werte | **ignoriert NULL** |
| `COUNT(DISTINCT spalte)` | Anzahl verschiedener Werte | ignoriert NULL |
| `SUM`, `AVG` | Summe, Mittelwert | ignorieren NULL |
| `MIN`, `MAX` | kleinster, größter Wert | ignorieren NULL |

Der Unterschied zwischen `COUNT(*)` und `COUNT(spalte)` ist eine beliebte Fangfrage.

## Bedingungen

```sql
WHERE Preis BETWEEN 10 AND 20          -- einschließlich beider Grenzen
WHERE Land IN ('DE', 'AT', 'CH')
WHERE Name LIKE 'Mei%'                 -- % = beliebig viele Zeichen
WHERE Name LIKE 'M_ier'                -- _ = genau ein Zeichen
WHERE Rabatt IS NULL                   -- niemals = NULL schreiben
WHERE NOT Aktiv
```

**NULL ist kein Wert, sondern die Abwesenheit eines Werts.** `spalte = NULL` ist niemals
wahr — auch nicht, wenn dort NULL steht. Es geht nur `IS NULL` und `IS NOT NULL`.

## DDL: Struktur

```sql
CREATE TABLE Kunde (
    KundenNr  INT          PRIMARY KEY AUTO_INCREMENT,
    Name      VARCHAR(100) NOT NULL,
    Email     VARCHAR(255) UNIQUE,
    Rabatt    DECIMAL(4,2) DEFAULT 0.00,
    AnlageDat DATE         NOT NULL
);

CREATE TABLE Bestellung (
    BestellNr INT PRIMARY KEY,
    KundenNr  INT NOT NULL,
    Betrag    DECIMAL(10,2),
    CONSTRAINT fk_kunde FOREIGN KEY (KundenNr)
        REFERENCES Kunde(KundenNr)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

ALTER TABLE Kunde ADD COLUMN Telefon VARCHAR(30);
ALTER TABLE Kunde MODIFY COLUMN Name VARCHAR(150) NOT NULL;
ALTER TABLE Kunde DROP COLUMN Telefon;

DROP TABLE Bestellung;
```

| Fremdschlüsselregel | Wirkung beim Löschen des Elternsatzes |
|---|---|
| `RESTRICT` / `NO ACTION` | verbietet das Löschen, solange Kinder existieren |
| `CASCADE` | löscht die Kinder mit |
| `SET NULL` | setzt den Fremdschlüssel der Kinder auf NULL |

## DML: Daten

```sql
INSERT INTO Kunde (Name, Email, AnlageDat)
VALUES ('Meier', 'meier@example.org', '2026-03-04');

UPDATE Kunde SET Rabatt = 5.00 WHERE KundenNr = 4711;

DELETE FROM Kunde WHERE KundenNr = 4711;
```

Ein `UPDATE` oder `DELETE` **ohne `WHERE`** trifft die ganze Tabelle. In der Prüfung kostet
das Punkte, im Betrieb den Abend.

## Sprachgruppen

| Gruppe | Wofür | Befehle |
|---|---|---|
| **DDL** | Struktur | `CREATE`, `ALTER`, `DROP`, `TRUNCATE` |
| **DML** | Daten | `INSERT`, `UPDATE`, `DELETE`, `SELECT` |
| **DCL** | Rechte | `GRANT`, `REVOKE` |
| **TCL** | Transaktionen | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

## Mengenoperationen

| Operator | Wirkung |
|---|---|
| `UNION` | vereinigt, **entfernt Duplikate** |
| `UNION ALL` | vereinigt, behält Duplikate, schneller |
| `INTERSECT` | nur Zeilen, die in beiden vorkommen |
| `EXCEPT` / `MINUS` | Zeilen der ersten ohne die der zweiten |

Voraussetzung: gleiche Spaltenanzahl, verträgliche Datentypen.

## Datentypen

| Typ | Wofür |
|---|---|
| `INT`, `BIGINT`, `SMALLINT` | Ganzzahlen |
| `DECIMAL(p,s)` / `NUMERIC` | **Geldbeträge** — exakt, keine Rundungsfehler |
| `FLOAT`, `DOUBLE` | Gleitkomma, für Messwerte; **nicht** für Geld |
| `VARCHAR(n)` | Text variabler Länge |
| `CHAR(n)` | Text fester Länge, wird aufgefüllt |
| `TEXT`, `CLOB` | lange Texte |
| `DATE`, `TIME`, `DATETIME`, `TIMESTAMP` | Datum und Zeit |
| `BOOLEAN` | wahr/falsch |
| `BLOB` | Binärdaten |

`DECIMAL(10,2)` heißt: 10 Stellen insgesamt, davon 2 nach dem Komma.
