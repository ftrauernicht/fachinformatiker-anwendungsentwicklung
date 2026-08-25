# Prüfungsfragen: Projektmanagement

## Inhaltsverzeichnis

- [Grundlagen](#grundlagen)
  - [1. Was macht ein Projekt zum Projekt? Nennen Sie vier Merkmale nach DIN 69901.](#1-was-macht-ein-projekt-zum-projekt-nennen-sie-vier-merkmale-nach-din-69901)
  - [2. Erklären Sie das magische Dreieck. Warum heißt es magisch?](#2-erklären-sie-das-magische-dreieck-warum-heißt-es-magisch)
  - [3. Nennen Sie drei Aufgaben des Projektleiters.](#3-nennen-sie-drei-aufgaben-des-projektleiters)
- [Netzplan](#netzplan)
  - [4. Wie rechnet man Vorwärts- und Rückwärtsrechnung im Netzplan?](#4-wie-rechnet-man-vorwärts--und-rückwärtsrechnung-im-netzplan)
  - [5. Was ist der Gesamtpuffer, was der freie Puffer?](#5-was-ist-der-gesamtpuffer-was-der-freie-puffer)
  - [6. Was ist der kritische Pfad, und woran erkennt man ihn?](#6-was-ist-der-kritische-pfad-und-woran-erkennt-man-ihn)
  - [7. Was ist der Unterschied zwischen Netzplan und Gantt-Diagramm?](#7-was-ist-der-unterschied-zwischen-netzplan-und-gantt-diagramm)
- [Wirtschaftlichkeit und Vorgehen](#wirtschaftlichkeit-und-vorgehen)
  - [8. Eine Investition kostet 60.000 €, der jährliche Rückfluss beträgt 15.000 €. Wie lang ist die Amortisationszeit?](#8-eine-investition-kostet-60000--der-jährliche-rückfluss-beträgt-15000--wie-lang-ist-die-amortisationszeit)
  - [9. Was ist der Unterschied zwischen Aufwand und Dauer?](#9-was-ist-der-unterschied-zwischen-aufwand-und-dauer)
  - [10. Nennen Sie die Rollen in Scrum und ihre Aufgabe.](#10-nennen-sie-die-rollen-in-scrum-und-ihre-aufgabe)

## Grundlagen

### 1. Was macht ein Projekt zum Projekt? Nennen Sie vier Merkmale nach DIN 69901.

<details markdown="1">
<summary>Antwort</summary>

- **Einmaligkeit** des Vorhabens
- **Konkrete Zielvorgaben** in Kosten, Terminen und Ressourcen
- **Zeitliche, finanzielle und personelle Begrenzung**
- **Abgrenzung** gegenüber anderen Vorhaben
- **Projektspezifische Organisation**
- **Interdisziplinarität** der Aufgabe und des Teams

Vier davon genügen. Das entscheidende Abgrenzungsmerkmal gegenüber dem Tagesgeschäft ist
die **Einmaligkeit**.

</details>

### 2. Erklären Sie das magische Dreieck. Warum heißt es magisch?

<details markdown="1">
<summary>Antwort</summary>

Die drei Ecken sind **Zeit**, **Kosten** und **Qualität beziehungsweise Leistungsumfang**.
Sie hängen voneinander ab: Wer eine Größe verändert, verändert zwangsläufig mindestens
eine der beiden anderen.

- Termin vorziehen → mehr Personal (Kosten) oder weniger Umfang
- Budget kürzen → längere Laufzeit oder weniger Umfang
- Umfang erweitern → mehr Zeit oder mehr Geld

„Magisch" heißt es, weil sich nicht alle drei gleichzeitig optimieren lassen. Wer es
versucht, bekommt keine Magie, sondern ein gescheitertes Projekt.

</details>

### 3. Nennen Sie drei Aufgaben des Projektleiters.

<details markdown="1">
<summary>Antwort</summary>

- **Planen**: Umfang abgrenzen, Arbeitspakete bilden, Termine und Ressourcen festlegen
- **Steuern**: Fortschritt gegen den Plan messen, bei Abweichung gegensteuern
- **Berichten**: Auftraggeber und Lenkungsausschuss über Stand, Risiken und Änderungen
  unterrichten
- **Team führen**: Aufgaben zuteilen, Hindernisse ausräumen, Konflikte lösen
- **Risiken bewirtschaften**: erkennen, bewerten, Gegenmaßnahmen festlegen

</details>

## Netzplan

### 4. Wie rechnet man Vorwärts- und Rückwärtsrechnung im Netzplan?

<details markdown="1">
<summary>Antwort</summary>

**Vorwärtsrechnung** (von links nach rechts, ergibt die frühesten Zeiten):

- `FEZ = FAZ + D`
- Der FAZ eines Vorgangs ist der **größte** FEZ aller Vorgänger. Der Vorgang kann erst
  beginnen, wenn der letzte Vorgänger fertig ist.

**Rückwärtsrechnung** (von rechts nach links, ergibt die spätesten Zeiten):

- `SAZ = SEZ − D`
- Der SEZ eines Vorgangs ist der **kleinste** SAZ aller Nachfolger. Er muss fertig sein,
  bevor der früheste Nachfolger beginnen muss.

Abkürzungen: FAZ frühester Anfangszeitpunkt, FEZ frühester Endzeitpunkt, SAZ spätester
Anfangszeitpunkt, SEZ spätester Endzeitpunkt, D Dauer.

</details>

### 5. Was ist der Gesamtpuffer, was der freie Puffer?

<details markdown="1">
<summary>Antwort</summary>

**Gesamtpuffer** `GP = SAZ − FAZ` (gleichwertig `SEZ − FEZ`): um wie viel sich der Vorgang
verschieben darf, **ohne das Projektende** zu gefährden. Dabei darf er allerdings den
Puffer nachfolgender Vorgänge aufbrauchen.

**Freier Puffer** `FP = kleinster FAZ der Nachfolger − FEZ`: um wie viel sich der Vorgang
verschieben darf, **ohne einen Nachfolger** zu verschieben.

Es gilt immer `FP ≤ GP`.

</details>

### 6. Was ist der kritische Pfad, und woran erkennt man ihn?

<details markdown="1">
<summary>Antwort</summary>

Der kritische Pfad ist die **längste Kette** von Vorgängen vom Anfang bis zum Ende des
Projekts. Seine Länge ist die Projektdauer.

Erkennungsmerkmal: alle Vorgänge darauf haben **Gesamtpuffer null**, also `FAZ = SAZ` und
`FEZ = SEZ`.

Praktische Bedeutung: Jede Verzögerung auf dem kritischen Pfad verschiebt das Projektende
um genau denselben Betrag. Verzögerungen daneben tun das erst, wenn sie den Puffer
übersteigen. Wer beschleunigen will, muss am kritischen Pfad ansetzen — überall sonst
verpufft der Aufwand.

Ein Netzplan kann **mehrere** kritische Pfade haben.

</details>

### 7. Was ist der Unterschied zwischen Netzplan und Gantt-Diagramm?

<details markdown="1">
<summary>Antwort</summary>

Der **Netzplan** zeigt die **logischen Abhängigkeiten**: was setzt was voraus. Daraus
ergeben sich Projektdauer, Puffer und kritischer Pfad. Er ist ein Rechenwerkzeug.

Das **Gantt-Diagramm** (Balkenplan) zeigt die Vorgänge als Balken auf einer **Zeitachse**.
Es macht Dauer und Überschneidung auf einen Blick sichtbar, zeigt Abhängigkeiten aber nur
eingeschränkt.

In der Praxis ergänzen sie sich: rechnen im Netzplan, berichten mit dem Gantt-Diagramm.

</details>

## Wirtschaftlichkeit und Vorgehen

### 8. Eine Investition kostet 60.000 €, der jährliche Rückfluss beträgt 15.000 €. Wie lang ist die Amortisationszeit?

<details markdown="1">
<summary>Antwort</summary>

```text
                       Investition           60.000 €
Amortisationszeit = ---------------------- = ---------- = 4 Jahre
                    jährlicher Rückfluss      15.000 €
```

Der Rückfluss ist dabei **Gewinn plus Abschreibung**, nicht der Umsatz. Wer mit dem Umsatz
rechnet, bekommt eine zu kurze Amortisationszeit heraus.

Aussagekraft: Die Rechnung sagt, wann das Geld wieder da ist — nicht, ob sich die
Investition lohnt. Was nach der Amortisation passiert, bleibt unberücksichtigt.

</details>

### 9. Was ist der Unterschied zwischen Aufwand und Dauer?

<details markdown="1">
<summary>Antwort</summary>

**Aufwand** ist Arbeitsleistung, gemessen in Personentagen (PT) oder Personenstunden.
**Dauer** ist Kalenderzeit.

Ein Arbeitspaket von 10 PT dauert bei einer Person 10 Tage, bei zwei Personen im Idealfall
5 Tage — im Idealfall.

Der Zusammenhang ist nicht beliebig teilbar: Manche Aufgaben lassen sich nicht aufteilen,
und zusätzliche Personen erzeugen Einarbeitungs- und Abstimmungsaufwand. Deshalb gilt
Brooks' Gesetz: *Einem verspäteten Projekt weitere Leute hinzuzufügen, verspätet es
zusätzlich.*

</details>

### 10. Nennen Sie die Rollen in Scrum und ihre Aufgabe.

<details markdown="1">
<summary>Antwort</summary>

| Rolle | Aufgabe |
|---|---|
| **Product Owner** | verantwortet den fachlichen Wert, pflegt und priorisiert das Product Backlog, entscheidet **was** gebaut wird |
| **Scrum Master** | verantwortet den Prozess, räumt Hindernisse aus, schützt das Team vor Störungen von außen; **kein** Vorgesetzter |
| **Entwicklungsteam** | baut das Produkt, entscheidet **wie**, schätzt selbst und organisiert sich selbst |

Ereignisse: Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective.
Artefakte: Product Backlog, Sprint Backlog, Increment.

Die häufigste Verwechslung in Prüfungsantworten: der Scrum Master ist **nicht** der
Projektleiter und weist niemandem Aufgaben zu.

</details>
