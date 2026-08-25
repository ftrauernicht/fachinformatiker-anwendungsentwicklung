# Prüfungsfragen: IT-Service-Management

## Inhaltsverzeichnis

- [Prozesse](#prozesse)
  - [1. Was macht einen Prozess aus? Nennen Sie die Merkmale.](#1-was-macht-einen-prozess-aus-nennen-sie-die-merkmale)
  - [2. Unterscheiden Sie Wertschöpfungs-, Support- und Managementprozesse.](#2-unterscheiden-sie-wertschöpfungs--support--und-managementprozesse)
  - [3. Was ist der Unterschied zwischen Incident und Problem?](#3-was-ist-der-unterschied-zwischen-incident-und-problem)
- [Rollen und Eskalation](#rollen-und-eskalation)
  - [4. Was ist ein SPOC, und welchen Zweck erfüllt er?](#4-was-ist-ein-spoc-und-welchen-zweck-erfüllt-er)
  - [5. Erklären Sie First-, Second- und Third-Level-Support.](#5-erklären-sie-first--second--und-third-level-support)
  - [6. Wie wird die Priorität eines Incidents bestimmt?](#6-wie-wird-die-priorität-eines-incidents-bestimmt)
- [Verträge und Rahmenwerke](#verträge-und-rahmenwerke)
  - [7. Was gehört in ein SLA? Nennen Sie fünf Punkte.](#7-was-gehört-in-ein-sla-nennen-sie-fünf-punkte)
  - [8. 99,5 % Verfügbarkeit im Monat — wie viel Ausfall ist das?](#8-995--verfügbarkeit-im-monat--wie-viel-ausfall-ist-das)

## Prozesse

### 1. Was macht einen Prozess aus? Nennen Sie die Merkmale.

<details markdown="1">
<summary>Antwort</summary>

Ein Prozess ist eine geregelte Folge von Aktivitäten mit

- einem **definierten Auslöser** und einem **definierten Ende**,
- einer **Eingabe** und einer daraus erzeugten **Ausgabe** (EVA-Prinzip),
- **Wiederholbarkeit** — er läuft nicht einmalig, sondern regelmäßig gleich ab,
- einer **Verantwortlichkeit**, also jemandem, dem der Prozess gehört.

Abgrenzung zum Projekt: ein Projekt ist einmalig und zeitlich befristet, ein Prozess
wiederholt sich.

</details>

### 2. Unterscheiden Sie Wertschöpfungs-, Support- und Managementprozesse.

<details markdown="1">
<summary>Antwort</summary>

| Art | Beitrag | Beispiele |
|---|---|---|
| **Wertschöpfungsprozess** (Kernprozess) | erzeugt unmittelbar den Nutzen für den Kunden, der Kunde bezahlt dafür | Softwareentwicklung, Fertigung, Auslieferung |
| **Supportprozess** | hält die Kernprozesse am Laufen, ohne selbst Kundennutzen zu erzeugen | IT-Betrieb, Personalwesen, Buchhaltung, Einkauf |
| **Managementprozess** | steuert und überwacht die anderen beiden | Strategie, Controlling, Qualitätsmanagement |

Prüfungstypischer Prüfstein: „Würde der Kunde dafür bezahlen?" Ja → Kernprozess.

</details>

### 3. Was ist der Unterschied zwischen Incident und Problem?

<details markdown="1">
<summary>Antwort</summary>

Ein **Incident** ist eine einzelne Störung: ein Dienst arbeitet nicht wie vereinbart. Ziel
des Incident Managements ist die **schnelle Wiederherstellung** des Betriebs — notfalls
mit einem Workaround, ohne die Ursache zu kennen.

Ein **Problem** ist die **Ursache** eines oder mehrerer Incidents. Ziel des Problem
Managements ist, diese Ursache dauerhaft zu beseitigen, damit der Incident nicht
wiederkehrt.

Beispiel: Drei Anrufe „Drucker druckt nicht" sind drei Incidents. Der defekte
Druckertreiber im Standard-Image dahinter ist das Problem.

</details>

## Rollen und Eskalation

### 4. Was ist ein SPOC, und welchen Zweck erfüllt er?

<details markdown="1">
<summary>Antwort</summary>

**Single Point of Contact** — die eine Anlaufstelle, über die Anwender jede Störung und
jede Anfrage melden, meist der Service Desk.

Zweck:

- Der Anwender muss nicht wissen, wer zuständig ist.
- Alle Meldungen werden **erfasst und zählbar**, was die Grundlage für Auswertungen und
  für das Problem Management ist.
- Wiederholte Fragen lassen sich sofort aus der Known-Error-Database beantworten.

Ohne SPOC laufen Meldungen an Einzelpersonen vorbei am System — sie tauchen in keiner
Statistik auf und niemand merkt, dass dieselbe Störung zum zehnten Mal auftritt.

</details>

### 5. Erklären Sie First-, Second- und Third-Level-Support.

<details markdown="1">
<summary>Antwort</summary>

| Stufe | Wer | Aufgabe |
|---|---|---|
| **First Level** | Service Desk, SPOC | Annahme, Kategorisierung, Priorisierung; löst mit bekannten Lösungen aus der Known-Error-Database |
| **Second Level** | Fachadministration | übernimmt, was der First Level nicht lösen kann; tiefere Systemkenntnis |
| **Third Level** | Entwicklung oder Hersteller | Spezialwissen, Änderungen am Produkt selbst |

Die Weitergabe nach oben heißt **funktionale Eskalation**. Davon zu unterscheiden ist die
**hierarchische Eskalation**: die Führungsebene wird eingeschaltet, weil die vereinbarte
Zeit zu reißen droht — nicht, weil Fachwissen fehlt.

</details>

### 6. Wie wird die Priorität eines Incidents bestimmt?

<details markdown="1">
<summary>Antwort</summary>

Aus zwei Größen:

- **Auswirkung** (Impact): wie viele Anwender oder wie kritische Geschäftsprozesse sind
  betroffen?
- **Dringlichkeit** (Urgency): wie schnell wächst der Schaden?

Beide zusammen ergeben in einer Matrix die Priorität:

| | Dringlichkeit hoch | mittel | niedrig |
|---|---|---|---|
| **Auswirkung hoch** | 1 | 2 | 3 |
| **mittel** | 2 | 3 | 4 |
| **niedrig** | 3 | 4 | 5 |

Der häufigste Fehler ist, die Priorität nach der Lautstärke des Anrufers zu vergeben.

</details>

## Verträge und Rahmenwerke

### 7. Was gehört in ein SLA? Nennen Sie fünf Punkte.

<details markdown="1">
<summary>Antwort</summary>

Ein **Service Level Agreement** ist die Vereinbarung zwischen Servicegeber und
Servicenehmer über die Qualität eines Dienstes. Darin stehen:

- **Leistungsbeschreibung** — was genau umfasst der Dienst, und was nicht
- **Servicezeiten** — wann gilt die Vereinbarung, etwa Mo–Fr 8–18 Uhr
- **Verfügbarkeit** in Prozent, mit der Bezugsgröße (99,5 % pro Monat)
- **Reaktions- und Wiederherstellungszeiten**, meist je Priorität gestaffelt
- **Messung und Berichterstattung** — wer misst, womit, wie oft
- **Folgen bei Nichteinhaltung** — Vertragsstrafe, Gutschrift
- **Preise und Abrechnungsmodell**

Abgrenzung: ein **OLA** (Operational Level Agreement) regelt dasselbe zwischen internen
Abteilungen, ein **UC** (Underpinning Contract) mit einem externen Zulieferer.

</details>

### 8. 99,5 % Verfügbarkeit im Monat — wie viel Ausfall ist das?

<details markdown="1">
<summary>Antwort</summary>

Ein Monat mit 30 Tagen hat 30 · 24 = 720 Stunden.

0,5 % von 720 h = **3,6 Stunden**, also 3 Stunden 36 Minuten zulässiger Ausfall.

Zum Vergleich, jeweils pro Monat:

| Verfügbarkeit | zulässiger Ausfall |
|---|---|
| 99 % | 7,2 Stunden |
| 99,5 % | 3,6 Stunden |
| 99,9 % | 43,2 Minuten |
| 99,99 % | 4,3 Minuten |

Aufpassen: Wird die Verfügbarkeit auf die **Servicezeit** bezogen statt auf den ganzen
Monat, ändert sich das Ergebnis erheblich. Bei Mo–Fr 8–18 Uhr sind es nur rund 220
Stunden, und 0,5 % davon sind gut eine Stunde.

</details>
