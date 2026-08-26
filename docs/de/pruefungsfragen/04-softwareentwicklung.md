# Prüfungsfragen: Softwareentwicklung

## Inhaltsverzeichnis

- [Web und HTTP](#web-und-http)
  - [1. Ordnen Sie die Statuscodes 200, 301, 403, 404 und 500 zu und erklären Sie sie.](#1-ordnen-sie-die-statuscodes-200-301-403-404-und-500-zu-und-erklären-sie-sie)
  - [2. Was ist der Unterschied zwischen 401 und 403?](#2-was-ist-der-unterschied-zwischen-401-und-403)
  - [3. Warum ist HTML keine Programmiersprache?](#3-warum-ist-html-keine-programmiersprache)
  - [4. Was ist der Unterschied zwischen GET und POST?](#4-was-ist-der-unterschied-zwischen-get-und-post)
- [Objektorientierung](#objektorientierung)
  - [5. Erklären Sie Kapselung, Vererbung und Polymorphie.](#5-erklären-sie-kapselung-vererbung-und-polymorphie)
  - [6. Was ist der Unterschied zwischen abstrakter Klasse und Interface?](#6-was-ist-der-unterschied-zwischen-abstrakter-klasse-und-interface)
  - [7. Was ist der Unterschied zwischen Aggregation und Komposition?](#7-was-ist-der-unterschied-zwischen-aggregation-und-komposition)
  - [8. Was bedeuten die Sichtbarkeiten +, -, # und ~ im Klassendiagramm?](#8-was-bedeuten-die-sichtbarkeiten-----und--im-klassendiagramm)
- [Vorgehen und Qualität](#vorgehen-und-qualität)
  - [9. Was ist der Unterschied zwischen Wasserfallmodell und agilem Vorgehen?](#9-was-ist-der-unterschied-zwischen-wasserfallmodell-und-agilem-vorgehen)
  - [10. Was ist der Unterschied zwischen Unit-Test, Integrationstest und Abnahmetest?](#10-was-ist-der-unterschied-zwischen-unit-test-integrationstest-und-abnahmetest)
- [Qualität, Test und Muster](#qualität-test-und-muster)
  - [11. Nennen Sie fünf Softwarequalitätsmerkmale nach ISO/IEC 25010 mit je einem Beispiel für ihre Verletzung.](#11-nennen-sie-fünf-softwarequalitätsmerkmale-nach-isoiec-25010-mit-je-einem-beispiel-für-ihre-verletzung)
  - [12. Was ist der Unterschied zwischen Black-Box- und White-Box-Test?](#12-was-ist-der-unterschied-zwischen-black-box--und-white-box-test)
  - [13. Ein Eingabefeld erlaubt Werte von 1 bis 100. Welche Werte prüft eine Grenzwertanalyse?](#13-ein-eingabefeld-erlaubt-werte-von-1-bis-100-welche-werte-prüft-eine-grenzwertanalyse)
  - [14. Was ist der Unterschied zwischen Lasttest und Stresstest?](#14-was-ist-der-unterschied-zwischen-lasttest-und-stresstest)
  - [15. Erklären Sie den Zyklus der testgetriebenen Entwicklung.](#15-erklären-sie-den-zyklus-der-testgetriebenen-entwicklung)
  - [16. Was ist der Unterschied zwischen einem Architekturmuster und einem Entwurfsmuster? Nennen Sie je zwei Beispiele.](#16-was-ist-der-unterschied-zwischen-einem-architekturmuster-und-einem-entwurfsmuster-nennen-sie-je-zwei-beispiele)
  - [17. Ein Onlineshop richtet sich an Verbraucher. Welche Anforderung stellt das BFSG, und welcher technische Maßstab gilt?](#17-ein-onlineshop-richtet-sich-an-verbraucher-welche-anforderung-stellt-das-bfsg-und-welcher-technische-maßstab-gilt)

## Web und HTTP

### 1. Ordnen Sie die Statuscodes 200, 301, 403, 404 und 500 zu und erklären Sie sie.

<details markdown="1">
<summary>Antwort</summary>

| Code | Bedeutung | Klasse |
|---|---|---|
| 200 OK | Anfrage erfolgreich bearbeitet | 2xx Erfolg |
| 301 Moved Permanently | Ressource liegt dauerhaft woanders, Client soll umlernen | 3xx Umleitung |
| 403 Forbidden | Server hat verstanden, weigert sich aber. Anmelden hilft nicht | 4xx Clientfehler |
| 404 Not Found | Ressource gibt es nicht | 4xx Clientfehler |
| 500 Internal Server Error | Fehler auf dem Server, die Anfrage war in Ordnung | 5xx Serverfehler |

Die erste Ziffer gibt die Klasse: 1xx Information, 2xx Erfolg, 3xx Umleitung, 4xx Fehler
beim Client, 5xx Fehler beim Server.

</details>

### 2. Was ist der Unterschied zwischen 401 und 403?

<details markdown="1">
<summary>Antwort</summary>

**401 Unauthorized** bedeutet: *nicht angemeldet*. Der Server weiß nicht, wer fragt.
Anmelden kann das Problem lösen. Der Name ist historisch irreführend — gemeint ist
Authentifizierung, nicht Autorisierung.

**403 Forbidden** bedeutet: *angemeldet, aber nicht berechtigt*. Der Server weiß, wer
fragt, und lässt es trotzdem nicht zu. Erneutes Anmelden ändert daran nichts.

</details>

### 3. Warum ist HTML keine Programmiersprache?

<details markdown="1">
<summary>Antwort</summary>

Weil ihr die Merkmale einer Programmiersprache fehlen: **Variablen**, **Kontrollstrukturen**
(Bedingungen, Schleifen) und die Fähigkeit, Berechnungen auszuführen. HTML beschreibt
ausschließlich die Struktur eines Dokuments.

HTML ist eine **Auszeichnungssprache** (Markup Language). Zum Vergleich: auch SQL ist
keine klassische Programmiersprache, sondern eine Abfragesprache — auch wenn die Grenze
dort durch Prozeduren verwischt.

</details>

### 4. Was ist der Unterschied zwischen GET und POST?

<details markdown="1">
<summary>Antwort</summary>

| | GET | POST |
|---|---|---|
| Daten stehen | in der URL | im Nachrichtenrumpf |
| Länge | begrenzt | praktisch unbegrenzt |
| Zwischenspeicherbar | ja | nein |
| Im Browserverlauf | ja | nein |
| Zweck | Daten **abrufen** | Daten **übermitteln** oder verändern |

Sicherheitlich wichtig: GET-Parameter landen im Browserverlauf, in Server-Protokolldateien
und im Referer. Kennwörter gehören deshalb nie in eine GET-Anfrage. Verschlüsselt sind
beide nur durch HTTPS — POST allein verschlüsselt nichts.

</details>

## Objektorientierung

### 5. Erklären Sie Kapselung, Vererbung und Polymorphie.

<details markdown="1">
<summary>Antwort</summary>

**Kapselung:** Daten und die Methoden, die auf ihnen arbeiten, liegen zusammen in einer
Klasse. Der Zustand ist von außen nicht direkt erreichbar (`private`), sondern nur über
definierte Methoden. Damit kann ein Objekt nie in einen ungültigen Zustand geraten.

**Vererbung:** Eine Unterklasse übernimmt Attribute und Methoden ihrer Oberklasse und
erweitert oder überschreibt sie. Vermeidet doppelten Code und bildet eine
*ist-ein*-Beziehung ab: ein Sparbuch **ist ein** Konto.

**Polymorphie:** Derselbe Aufruf verhält sich je nach tatsächlichem Objekt
unterschiedlich. `konto.zinsenBerechnen()` rechnet anders, wenn dahinter ein Sparbuch
steht als bei einem Girokonto — der aufrufende Code muss den Unterschied nicht kennen.

</details>

### 6. Was ist der Unterschied zwischen abstrakter Klasse und Interface?

<details markdown="1">
<summary>Antwort</summary>

| | Abstrakte Klasse | Interface |
|---|---|---|
| Kann Implementierung enthalten | ja, teilweise | klassisch nein |
| Kann Attribute (Zustand) haben | ja | nein, nur Konstanten |
| Mehrfach nutzbar | nein, eine Oberklasse | ja, beliebig viele |
| Beziehung | *ist ein* | *kann etwas* |

Faustregel: Eine abstrakte Klasse eignet sich für verwandte Klassen mit gemeinsamem Code.
Ein Interface eignet sich für eine Fähigkeit, die auch völlig unterschiedliche Klassen
haben können — `Druckbar`, `Vergleichbar`, `Serialisierbar`.

</details>

### 7. Was ist der Unterschied zwischen Aggregation und Komposition?

<details markdown="1">
<summary>Antwort</summary>

Beide beschreiben eine *Teil-von*-Beziehung, aber unterschiedlich streng.

**Aggregation** (leere Raute): Das Teil kann ohne das Ganze existieren. Eine Abteilung
enthält Mitarbeiter; wird die Abteilung aufgelöst, gibt es die Mitarbeiter weiterhin.

**Komposition** (gefüllte Raute): Das Teil kann ohne das Ganze **nicht** existieren und
gehört zu genau einem Ganzen. Ein Haus besteht aus Räumen; wird das Haus abgerissen, sind
die Räume weg.

Die Raute steht in beiden Fällen am **Ganzen**.

</details>

### 8. Was bedeuten die Sichtbarkeiten +, -, # und ~ im Klassendiagramm?

<details markdown="1">
<summary>Antwort</summary>

| Zeichen | Sichtbarkeit | Zugriff |
|---|---|---|
| `+` | public | von überall |
| `-` | private | nur innerhalb der Klasse |
| `#` | protected | in der Klasse und ihren Unterklassen |
| `~` | package | innerhalb desselben Pakets |

Als Vorgabe gilt: Attribute `private`, Methoden nach Bedarf `public`. Ein `public`
Attribut widerspricht der Kapselung.

</details>

## Vorgehen und Qualität

### 9. Was ist der Unterschied zwischen Wasserfallmodell und agilem Vorgehen?

<details markdown="1">
<summary>Antwort</summary>

**Wasserfall** arbeitet Phasen nacheinander ab — Analyse, Entwurf, Umsetzung, Test,
Einführung. Jede Phase endet mit einem Ergebnis, das die nächste voraussetzt. Vorteil:
planbar, gut dokumentiert, feste Kosten. Nachteil: Änderungen sind spät teuer, und der
Kunde sieht das Ergebnis erst am Ende.

**Agil** (Scrum, Kanban) liefert in kurzen Zyklen lauffähige Teilergebnisse und passt den
Plan laufend an. Vorteil: frühes Feedback, Änderungen sind eingeplant. Nachteil: Umfang
und Kosten stehen zu Beginn nicht fest, und es setzt eine mitarbeitende Fachseite voraus.

Prüfungstypische Zuordnung: fester Anforderungskatalog und Festpreis → Wasserfall; unklare
oder sich ändernde Anforderungen → agil.

</details>

### 10. Was ist der Unterschied zwischen Unit-Test, Integrationstest und Abnahmetest?

<details markdown="1">
<summary>Antwort</summary>

| Stufe | Prüft | Wer |
|---|---|---|
| **Unit-Test** | eine einzelne Klasse oder Methode, isoliert | Entwicklung |
| **Integrationstest** | das Zusammenspiel mehrerer Komponenten, auch mit Datenbank und Schnittstellen | Entwicklung |
| **Systemtest** | das vollständige System gegen die Spezifikation | Test oder QS |
| **Abnahmetest** | ob das System die Anforderungen des Auftraggebers erfüllt | Auftraggeber |

Die Reihenfolge folgt dem V-Modell: links die Spezifikationsstufen, rechts die zugehörige
Teststufe. Je weiter rechts ein Fehler auffällt, desto teurer wird er.

</details>

## Qualität, Test und Muster

### 11. Nennen Sie fünf Softwarequalitätsmerkmale nach ISO/IEC 25010 mit je einem Beispiel für ihre Verletzung.

<details markdown="1">
<summary>Antwort</summary>

| Merkmal | Beispiel für eine Verletzung |
|---|---|
| **Funktionale Eignung** | Die Rechnungssumme wird falsch gerundet |
| **Leistungseffizienz** | Die Suche antwortet erst nach zwölf Sekunden |
| **Benutzbarkeit** | Der Abbrechen-Knopf speichert |
| **Zuverlässigkeit** | Nach drei Tagen ohne Neustart bleibt der Dienst stehen |
| **Wartbarkeit** | Eine neue Steuerklasse erfordert Änderungen an neunzehn Stellen |

Die weiteren drei der acht sind Kompatibilität, Sicherheit und Übertragbarkeit. Die Fassung von 2023 hat Benutzbarkeit in Interaktionsfähigkeit und Übertragbarkeit in Flexibilität umbenannt und Betriebssicherheit als neuntes Merkmal ergänzt.

</details>

### 12. Was ist der Unterschied zwischen Black-Box- und White-Box-Test?

<details markdown="1">
<summary>Antwort</summary>

**Black Box:** getestet wird gegen die Spezifikation, ohne Kenntnis des Quelltextes. Eingabe hinein, Ausgabe vergleichen. Verfahren sind Äquivalenzklassenbildung und Grenzwertanalyse.

**White Box:** der Quelltext ist bekannt, getestet wird gegen seine Struktur. Maß ist die Überdeckung — Anweisungs-, Zweig- oder Pfadüberdeckung.

Beide ergänzen sich: Black Box findet fehlende Funktionen, White Box findet nicht erreichbaren oder ungetesteten Code.

</details>

### 13. Ein Eingabefeld erlaubt Werte von 1 bis 100. Welche Werte prüft eine Grenzwertanalyse?

<details markdown="1">
<summary>Antwort</summary>

**0, 1, 100 und 101** — jeweils der Wert direkt außerhalb und direkt innerhalb der Grenze. Häufig werden zusätzlich 2 und 99 geprüft.

Nicht geprüft wird 50: Ein Wert aus der Mitte der Äquivalenzklasse bringt keine zusätzliche Erkenntnis.

Begründung: Fehler entstehen an den Rändern, weil dort die Vergleichsoperatoren stehen. Ein `<` statt `<=` fällt nur bei genau 100 auf.

</details>

### 14. Was ist der Unterschied zwischen Lasttest und Stresstest?

<details markdown="1">
<summary>Antwort</summary>

Der **Lasttest** prüft, ob das System die **erwartete** Last verkraftet — etwa 500 gleichzeitige Nutzer bei vereinbarten Antwortzeiten.

Der **Stresstest** geht bewusst darüber hinaus und sucht die **Grenze**. Interessant ist dabei weniger, wo sie liegt, als was beim Überschreiten passiert: Verweigert das System neue Anfragen geordnet, oder stürzt es ab und verliert Daten?

Verwandt sind der Dauertest über viele Stunden, der schleichende Speicherlecks sichtbar macht, und der Skalierbarkeitstest, der prüft, ob mehr Hardware auch mehr Durchsatz bringt.

Gemessen werden in allen Fällen Antwortzeit, Durchsatz und Fehlerrate — und zwar gegen vorher festgelegte Zielwerte.

</details>

### 15. Erklären Sie den Zyklus der testgetriebenen Entwicklung.

<details markdown="1">
<summary>Antwort</summary>

**Red-Green-Refactor**, in dieser Reihenfolge:

1. **Rot** — einen Test für die gewünschte Funktion schreiben. Er schlägt fehl, weil es die Funktion noch nicht gibt.
2. **Grün** — gerade so viel Code schreiben, dass der Test durchläuft. Nicht mehr.
3. **Refactor** — den Code aufräumen, ohne sein Verhalten zu ändern; der Test sichert das ab.

Der wesentliche Nutzen liegt nicht in der Testabdeckung, sondern im Entwurf: Wer den Aufruf zuerst schreibt, bemerkt eine unbequeme Schnittstelle sofort und nicht erst beim dritten Aufrufer.

</details>

### 16. Was ist der Unterschied zwischen einem Architekturmuster und einem Entwurfsmuster? Nennen Sie je zwei Beispiele.

<details markdown="1">
<summary>Antwort</summary>

Der Unterschied ist die Reichweite.

Ein **Architekturmuster** ordnet das System als Ganzes: Schichtenarchitektur, Model View Controller, Client-Server, Microservices.

Ein **Entwurfsmuster** löst ein Problem innerhalb weniger Klassen: Singleton, Beobachter, Strategie, Fabrikmethode.

Entwurfsmuster werden in drei Gruppen eingeteilt — Erzeugungs-, Struktur- und Verhaltensmuster.

</details>

### 17. Ein Onlineshop richtet sich an Verbraucher. Welche Anforderung stellt das BFSG, und welcher technische Maßstab gilt?

<details markdown="1">
<summary>Antwort</summary>

Das Barrierefreiheitsstärkungsgesetz gilt seit dem **28. Juni 2025**. Dienstleistungen im elektronischen Geschäftsverkehr, die sich an Verbraucher richten, müssen barrierefrei sein; dazu gehört eine veröffentlichte Erklärung zur Barrierefreiheit.

Ausgenommen sind Kleinstunternehmen mit weniger als zehn Beschäftigten und höchstens zwei Millionen Euro Jahresumsatz — allerdings nur bei Dienstleistungen, nicht bei Produkten.

Technischer Maßstab ist die Norm **EN 301 549**, die für Webinhalte auf die **WCAG 2.1 Stufe AA** verweist. Deren vier Grundsätze: wahrnehmbar, bedienbar, verständlich, robust.

Konkret heißt das im Code: Alternativtexte, ausreichender Kontrast, vollständige Tastaturbedienung mit sichtbarem Fokus, beschriftete Formularfelder und gültiges, semantisches HTML.

</details>
