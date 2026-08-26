# Prüfungsfragen: Algorithmen

## Inhaltsverzeichnis

- [Pseudocode und Kontrollstrukturen](#pseudocode-und-kontrollstrukturen)
  - [1. Eine Aufgabe verlangt einen Algorithmus in Pseudocode. Darf man stattdessen ein Struktogramm zeichnen?](#1-eine-aufgabe-verlangt-einen-algorithmus-in-pseudocode-darf-man-stattdessen-ein-struktogramm-zeichnen)
  - [2. Nennen Sie die drei Grundbausteine, aus denen sich jeder Algorithmus zusammensetzen lässt.](#2-nennen-sie-die-drei-grundbausteine-aus-denen-sich-jeder-algorithmus-zusammensetzen-lässt)
  - [3. Worin unterscheiden sich kopfgesteuerte und fußgesteuerte Schleife? Nennen Sie je einen Anwendungsfall.](#3-worin-unterscheiden-sich-kopfgesteuerte-und-fußgesteuerte-schleife-nennen-sie-je-einen-anwendungsfall)
  - [4. Schreiben Sie in Pseudocode eine Funktion, die das größte Element eines Feldes zurückgibt.](#4-schreiben-sie-in-pseudocode-eine-funktion-die-das-größte-element-eines-feldes-zurückgibt)
- [Komplexität und Suchen](#komplexität-und-suchen)
  - [5. Was beschreibt die O-Notation? Ordnen Sie lineare Suche, binäre Suche und Bubblesort ein.](#5-was-beschreibt-die-o-notation-ordnen-sie-lineare-suche-binäre-suche-und-bubblesort-ein)
  - [6. Welche Voraussetzung hat die binäre Suche, und wie viele Vergleiche braucht sie bei 1.000 Elementen?](#6-welche-voraussetzung-hat-die-binäre-suche-und-wie-viele-vergleiche-braucht-sie-bei-1000-elementen)
  - [7. Was ist ein Off-by-one-Fehler? Zeigen Sie ihn an einem Beispiel.](#7-was-ist-ein-off-by-one-fehler-zeigen-sie-ihn-an-einem-beispiel)
- [Sortieren](#sortieren)
  - [8. Geben Sie den Zustand des Feldes [7, 3, 9, 2] nach jedem Durchlauf von Bubblesort an.](#8-geben-sie-den-zustand-des-feldes-7-3-9-2-nach-jedem-durchlauf-von-bubblesort-an)
  - [9. Wie unterscheiden sich Selectionsort und Insertionsort in Vergleichen und Tauschvorgängen?](#9-wie-unterscheiden-sich-selectionsort-und-insertionsort-in-vergleichen-und-tauschvorgängen)
  - [10. Was bedeutet es, dass ein Sortierverfahren stabil ist, und wann spielt das eine Rolle?](#10-was-bedeutet-es-dass-ein-sortierverfahren-stabil-ist-und-wann-spielt-das-eine-rolle)

## Pseudocode und Kontrollstrukturen

### 1. Eine Aufgabe verlangt einen Algorithmus in Pseudocode. Darf man stattdessen ein Struktogramm zeichnen?

<details markdown="1">
<summary>Antwort</summary>

Nein. Programmablaufplan und Struktogramm sind mit dem Prüfungskatalog von 2025 aus der Prüfung entfernt worden. Verlangt wird Pseudocode oder eine Lösung in einer Programmiersprache; als grafische Darstellung ist das UML-Aktivitätsdiagramm vorgesehen.

Bis dahin war es üblich, eine Programmieraufgabe durch ein Struktogramm zu ersetzen. Wer sich darauf verlässt, schreibt heute eine Antwort ohne Punkte.

</details>

### 2. Nennen Sie die drei Grundbausteine, aus denen sich jeder Algorithmus zusammensetzen lässt.

<details markdown="1">
<summary>Antwort</summary>

- **Sequenz** — Anweisungen laufen nacheinander ab
- **Verzweigung** (Selektion) — eine Bedingung entscheidet über den weiteren Weg
- **Wiederholung** (Iteration) — ein Block läuft mehrfach

Das ist keine Konvention, sondern der Satz von Böhm und Jacopini: Jedes berechenbare Problem lässt sich allein mit diesen drei Bausteinen lösen — ohne Sprunganweisung.

</details>

### 3. Worin unterscheiden sich kopfgesteuerte und fußgesteuerte Schleife? Nennen Sie je einen Anwendungsfall.

<details markdown="1">
<summary>Antwort</summary>

| | Kopfgesteuert (`while`) | Fußgesteuert (`do-while`) |
|---|---|---|
| Bedingung wird geprüft | vor dem Durchlauf | nach dem Durchlauf |
| Anzahl der Durchläufe mindestens | null | eins |

**Kopfgesteuert**, wenn der Block unter Umständen gar nicht laufen soll: eine Liste abarbeiten, die leer sein kann.

**Fußgesteuert**, wenn er mindestens einmal laufen muss: eine Eingabe abfragen und so lange wiederholen, bis sie gültig ist.

Die Zählschleife (`for`) ist ein Sonderfall der kopfgesteuerten Schleife mit Zähler, Start, Ende und Schrittweite.

</details>

### 4. Schreiben Sie in Pseudocode eine Funktion, die das größte Element eines Feldes zurückgibt.

<details markdown="1">
<summary>Antwort</summary>

```text
groesstes(feld)
    wenn länge(feld) == 0
        gib -1 zurück
    groesstes = feld[0]
    für i von 1 bis länge(feld) - 1
        wenn feld[i] > groesstes
            groesstes = feld[i]
    gib groesstes zurück
```

Drei Punkte, an denen die Bewertung hängt: Der Startwert ist **das erste Element**, nicht null — sonst versagt die Funktion bei lauter negativen Zahlen. Die Schleife beginnt bei 1, weil Element 0 schon verglichen wurde. Und der leere Fall ist behandelt.

</details>

## Komplexität und Suchen

### 5. Was beschreibt die O-Notation? Ordnen Sie lineare Suche, binäre Suche und Bubblesort ein.

<details markdown="1">
<summary>Antwort</summary>

Die O-Notation beschreibt, wie der Aufwand mit der Eingabegröße *n* wächst. Konstante Faktoren und kleinere Terme entfallen: aus 3*n*² + 5*n* + 12 wird O(*n*²).

| Verfahren | Klasse |
|---|---|
| lineare Suche | O(n) |
| binäre Suche | O(log n) |
| Bubblesort | O(n²) |

Gefragt ist damit nicht die tatsächliche Laufzeit, sondern das Wachstum. Ein O(n²)-Verfahren kann bei zehn Elementen schneller sein als ein O(n log n)-Verfahren — bei zehntausend nie.

</details>

### 6. Welche Voraussetzung hat die binäre Suche, und wie viele Vergleiche braucht sie bei 1.000 Elementen?

<details markdown="1">
<summary>Antwort</summary>

Voraussetzung ist ein **sortiertes** Feld. Ohne Sortierung liefert das Verfahren falsche Ergebnisse, nicht bloß langsame.

Bei jedem Schritt halbiert sich der Suchbereich, es sind also höchstens ⌈log₂ 1000⌉ = **10 Vergleiche** nötig. Zum Vergleich: Die lineare Suche braucht im schlechtesten Fall 1.000.

Der Vorteil wächst mit der Größe: Bei einer Million Elementen sind es 20 statt einer Million.

Zu bedenken ist allerdings, dass das Sortieren selbst Aufwand kostet. Für eine einmalige Suche in unsortierten Daten lohnt es sich nicht.

</details>

### 7. Was ist ein Off-by-one-Fehler? Zeigen Sie ihn an einem Beispiel.

<details markdown="1">
<summary>Antwort</summary>

Ein Fehler, bei dem eine Schleife oder ein Index um genau eins danebenliegt — der häufigste Fehler in Prüfungsantworten mit Schleifen.

```text
für i von 0 bis länge(feld) - 1
    wenn feld[i] > feld[i + 1]        Zugriff über das Feldende hinaus
```

Im letzten Durchlauf ist `i` der letzte gültige Index, `i + 1` liegt außerhalb. Richtig ist `bis länge(feld) - 2`.

Der Gegenfall ist genauso häufig: `solange links < rechts` in der binären Suche prüft das letzte verbleibende Element nicht mehr.

</details>

## Sortieren

### 8. Geben Sie den Zustand des Feldes [7, 3, 9, 2] nach jedem Durchlauf von Bubblesort an.

<details markdown="1">
<summary>Antwort</summary>

| Durchlauf | Vergleiche | Feld danach |
|---|---|---|
| Start | | 7, 3, 9, 2 |
| 1 | 7↔3 tauschen, 7↔9 stehen lassen, 9↔2 tauschen | 3, 7, 2, 9 |
| 2 | 3↔7 stehen lassen, 7↔2 tauschen | 3, 2, 7, 9 |
| 3 | 3↔2 tauschen | 2, 3, 7, 9 |

Nach jedem Durchlauf steht das größte verbleibende Element endgültig am Ende. Deshalb wird der innere Durchlauf jedes Mal um ein Feld kürzer.

</details>

### 9. Wie unterscheiden sich Selectionsort und Insertionsort in Vergleichen und Tauschvorgängen?

<details markdown="1">
<summary>Antwort</summary>

**Selectionsort** sucht je Durchlauf das kleinste Element und tauscht es einmal an seinen Platz: höchstens *n* − 1 Tauschvorgänge. Die Anzahl der Vergleiche ist dagegen fest — auch ein bereits sortiertes Feld wird vollständig durchgesehen.

**Insertionsort** schiebt jedes Element so weit nach vorn, bis es passt. Bei fast sortierten Daten bricht die innere Schleife sofort ab, der Aufwand geht gegen O(n); bei absteigend sortierten Daten ist er dagegen am größten.

Merksatz: Selectionsort ist gut, wenn Tauschen teuer ist. Insertionsort ist gut, wenn die Daten schon fast stimmen.

</details>

### 10. Was bedeutet es, dass ein Sortierverfahren stabil ist, und wann spielt das eine Rolle?

<details markdown="1">
<summary>Antwort</summary>

Stabil heißt: Elemente mit gleichem Sortierschlüssel behalten ihre ursprüngliche Reihenfolge zueinander.

Das ist wichtig, sobald nacheinander nach mehreren Kriterien sortiert wird. Wer eine Liste erst nach Vornamen und dann stabil nach Nachnamen sortiert, erhält Nachnamen in Reihenfolge und innerhalb gleicher Nachnamen die Vornamen in Reihenfolge. Mit einem instabilen Verfahren ist die erste Sortierung verloren.

Von den drei elementaren Verfahren sind Bubblesort und Insertionsort stabil, Selectionsort ist es nicht — es tauscht über weite Strecken hinweg und zerreißt dabei die Reihenfolge gleicher Schlüssel.

</details>
