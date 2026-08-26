# Prüfungsfragen: IT-Schutz und -Sicherheit

## Inhaltsverzeichnis

- [Grundbegriffe](#grundbegriffe)
  - [1. Nennen Sie die drei Schutzziele der IT-Sicherheit und je ein Beispiel für ihre Verletzung.](#1-nennen-sie-die-drei-schutzziele-der-it-sicherheit-und-je-ein-beispiel-für-ihre-verletzung)
  - [2. Was ist der Unterschied zwischen Authentisierung, Authentifizierung und Autorisierung?](#2-was-ist-der-unterschied-zwischen-authentisierung-authentifizierung-und-autorisierung)
  - [3. Nennen Sie die drei Faktoren der Authentifizierung mit je zwei Beispielen.](#3-nennen-sie-die-drei-faktoren-der-authentifizierung-mit-je-zwei-beispielen)
- [Verschlüsselung](#verschlüsselung)
  - [4. Worin unterscheiden sich symmetrische und asymmetrische Verschlüsselung?](#4-worin-unterscheiden-sich-symmetrische-und-asymmetrische-verschlüsselung)
  - [5. Wie funktioniert eine digitale Signatur, und was leistet sie?](#5-wie-funktioniert-eine-digitale-signatur-und-was-leistet-sie)
  - [6. Warum wird ein Kennwort gehasht und nicht verschlüsselt gespeichert?](#6-warum-wird-ein-kennwort-gehasht-und-nicht-verschlüsselt-gespeichert)
- [Datenschutz und Organisation](#datenschutz-und-organisation)
  - [7. Was sind personenbezogene Daten, und was gilt für besondere Kategorien?](#7-was-sind-personenbezogene-daten-und-was-gilt-für-besondere-kategorien)
  - [8. Was ist der Unterschied zwischen Anonymisierung und Pseudonymisierung?](#8-was-ist-der-unterschied-zwischen-anonymisierung-und-pseudonymisierung)
  - [9. Nennen Sie die vier Schritte einer Schutzbedarfsanalyse.](#9-nennen-sie-die-vier-schritte-einer-schutzbedarfsanalyse)
  - [10. Was ist ein ISMS, und wofür steht die zugehörige Norm?](#10-was-ist-ein-isms-und-wofür-steht-die-zugehörige-norm)
- [Angriffe](#angriffe)
  - [11. Was ist ein Man-in-the-Middle-Angriff, und was schützt zuverlässig davor?](#11-was-ist-ein-man-in-the-middle-angriff-und-was-schützt-zuverlässig-davor)
  - [12. Wie funktioniert eine SQL-Injection, und welche Gegenmaßnahme ist die wirksamste?](#12-wie-funktioniert-eine-sql-injection-und-welche-gegenmaßnahme-ist-die-wirksamste)
  - [13. Unterscheiden Sie Cross-Site-Scripting von Cross-Site-Request-Forgery.](#13-unterscheiden-sie-cross-site-scripting-von-cross-site-request-forgery)
  - [14. Was unterscheidet DoS von DDoS, und welches Schutzziel wird verletzt?](#14-was-unterscheidet-dos-von-ddos-und-welches-schutzziel-wird-verletzt)
  - [15. Wie läuft eine Anmeldung mit Kerberos ab, und warum müssen die Uhren stimmen?](#15-wie-läuft-eine-anmeldung-mit-kerberos-ab-und-warum-müssen-die-uhren-stimmen)
- [Rechtsrahmen](#rechtsrahmen)
  - [16. Welche Meldefristen sieht das NIS-2-Umsetzungsgesetz bei einem erheblichen Sicherheitsvorfall vor?](#16-welche-meldefristen-sieht-das-nis-2-umsetzungsgesetz-bei-einem-erheblichen-sicherheitsvorfall-vor)
  - [17. Nennen Sie die vier Risikostufen der EU-KI-Verordnung mit je einem Beispiel.](#17-nennen-sie-die-vier-risikostufen-der-eu-ki-verordnung-mit-je-einem-beispiel)

## Grundbegriffe

### 1. Nennen Sie die drei Schutzziele der IT-Sicherheit und je ein Beispiel für ihre Verletzung.

<details markdown="1">
<summary>Antwort</summary>

| Schutzziel | Bedeutung | Verletzung |
|---|---|---|
| **Vertraulichkeit** | Nur Berechtigte sehen die Daten | Eine unverschlüsselte Kundenliste wird abgegriffen |
| **Integrität** | Daten sind unverändert und vollständig | Ein Angreifer ändert einen Rechnungsbetrag |
| **Verfügbarkeit** | Daten und Dienste sind nutzbar, wenn sie gebraucht werden | Ein DDoS-Angriff legt den Shop lahm |

Gelegentlich wird **Authentizität** als viertes Ziel genannt: die Herkunft der Daten ist
nachweisbar.

</details>

### 2. Was ist der Unterschied zwischen Authentisierung, Authentifizierung und Autorisierung?

<details markdown="1">
<summary>Antwort</summary>

Drei Schritte in fester Reihenfolge:

1. **Authentisierung** — der Benutzer *behauptet*, wer er ist, und legt einen Nachweis
   vor. Er tippt Benutzername und Kennwort ein.
2. **Authentifizierung** — das System *prüft* diesen Nachweis. Kennwort-Hash vergleichen.
3. **Autorisierung** — das System entscheidet, *was* der nun bekannte Benutzer darf.
   Zugriff auf diesen Ordner ja, auf jenen nein.

Eselsbrücke: erst *ich bin es*, dann *stimmt, du bist es*, dann *und das darfst du*.

</details>

### 3. Nennen Sie die drei Faktoren der Authentifizierung mit je zwei Beispielen.

<details markdown="1">
<summary>Antwort</summary>

| Faktor | Beispiele |
|---|---|
| **Wissen** | Kennwort, PIN, Sicherheitsfrage |
| **Besitz** | Chipkarte, TAN-Generator, Mobiltelefon mit Authenticator-App |
| **Sein** (Biometrie) | Fingerabdruck, Iris- oder Gesichtserkennung |

**Zwei-Faktor-Authentifizierung** heißt: zwei Faktoren aus **verschiedenen** Kategorien.
Kennwort plus Sicherheitsfrage ist keine 2FA, weil beides Wissen ist. Bankkarte plus PIN
dagegen schon.

</details>

## Verschlüsselung

### 4. Worin unterscheiden sich symmetrische und asymmetrische Verschlüsselung?

<details markdown="1">
<summary>Antwort</summary>

| | Symmetrisch | Asymmetrisch |
|---|---|---|
| Schlüssel | ein gemeinsamer geheimer | Schlüsselpaar: öffentlich und privat |
| Geschwindigkeit | schnell | langsam |
| Problem | Schlüsselaustausch | Rechenaufwand |
| Verfahren | AES, DES, 3DES, Twofish | RSA, ECC, Diffie-Hellman |
| Schlüsselanzahl bei *n* Teilnehmern | *n* · (*n* − 1) / 2 | 2 · *n* |

In der Praxis wird beides kombiniert (hybride Verschlüsselung, so arbeitet TLS): der
schnelle symmetrische Sitzungsschlüssel wird asymmetrisch ausgetauscht, die eigentlichen
Daten danach symmetrisch verschlüsselt.

</details>

### 5. Wie funktioniert eine digitale Signatur, und was leistet sie?

<details markdown="1">
<summary>Antwort</summary>

Der Absender bildet einen **Hash** über die Nachricht und verschlüsselt diesen mit seinem
**privaten** Schlüssel. Der Empfänger entschlüsselt ihn mit dem **öffentlichen** Schlüssel
des Absenders, bildet selbst den Hash über die empfangene Nachricht und vergleicht.

Damit sind belegt:

- **Integrität** — bei jeder Änderung stimmen die Hashes nicht überein
- **Authentizität** — nur der Inhaber des privaten Schlüssels konnte signieren
- **Nichtabstreitbarkeit** — der Absender kann die Signatur nicht bestreiten

Was sie **nicht** leistet: Vertraulichkeit. Die Nachricht selbst bleibt lesbar, wenn sie
nicht zusätzlich verschlüsselt wird.

Wichtig für die Prüfung: Signieren nutzt die Schlüssel **umgekehrt** zum Verschlüsseln.

</details>

### 6. Warum wird ein Kennwort gehasht und nicht verschlüsselt gespeichert?

<details markdown="1">
<summary>Antwort</summary>

Weil Verschlüsselung **umkehrbar** ist. Wer den Schlüssel erbeutet, hat alle Kennwörter im
Klartext. Ein Hash ist eine Einwegfunktion: aus ihm lässt sich das Kennwort nicht
zurückrechnen.

Zum Prüfen genügt das: Das eingegebene Kennwort wird erneut gehasht und mit dem
gespeicherten Wert verglichen.

Dazu gehört ein **Salt** — ein zufälliger Wert je Benutzer, der vor dem Hashen angehängt
wird. Er verhindert, dass gleiche Kennwörter gleiche Hashes ergeben, und macht vorberechnete
Tabellen (Rainbow Tables) nutzlos. Verwendet werden bewusst langsame Verfahren wie bcrypt,
scrypt oder Argon2, nicht MD5 oder SHA-1.

</details>

## Datenschutz und Organisation

### 7. Was sind personenbezogene Daten, und was gilt für besondere Kategorien?

<details markdown="1">
<summary>Antwort</summary>

**Personenbezogene Daten** sind alle Informationen, die sich auf eine identifizierte oder
identifizierbare natürliche Person beziehen (Art. 4 DSGVO): Name, Anschrift,
Personalnummer, IP-Adresse, Kundennummer.

**Besondere Kategorien** (Art. 9 DSGVO) sind zusätzlich geschützt: Gesundheitsdaten,
biometrische Daten, ethnische Herkunft, politische Meinung, religiöse Überzeugung,
Gewerkschaftszugehörigkeit, Sexualleben. Ihre Verarbeitung ist grundsätzlich **verboten**
und nur in engen Ausnahmen erlaubt.

Nicht personenbezogen sind Daten juristischer Personen und **anonymisierte** Daten — bei
Letzteren muss der Personenbezug allerdings unumkehrbar entfernt sein.

</details>

### 8. Was ist der Unterschied zwischen Anonymisierung und Pseudonymisierung?

<details markdown="1">
<summary>Antwort</summary>

**Anonymisierung** entfernt den Personenbezug **unumkehrbar**. Danach fällt die DSGVO
nicht mehr an, weil es keine personenbezogenen Daten mehr sind.

**Pseudonymisierung** ersetzt identifizierende Merkmale durch ein Kennzeichen. Mit einer
getrennt aufbewahrten Zuordnungstabelle lässt sich der Bezug **wiederherstellen** — die
Daten bleiben deshalb personenbezogen und fallen weiter unter die DSGVO.

Die DSGVO nennt Pseudonymisierung in Art. 32 ausdrücklich als technische Maßnahme, nicht
als Ausweg aus dem Anwendungsbereich.

</details>

### 9. Nennen Sie die vier Schritte einer Schutzbedarfsanalyse.

<details markdown="1">
<summary>Antwort</summary>

1. **Zu schützende Daten erfassen** — was wird im betrachteten Verfahren überhaupt
   verarbeitet oder gespeichert?
2. **Datengruppen bilden** — inhaltlich Zusammengehöriges zusammenfassen, damit die
   folgenden Schritte nicht je Einzelfeld gemacht werden müssen.
3. **Schlimmste denkbare Folgen abschätzen** — je Datengruppe und je Schutzziel
   (Vertraulichkeit, Integrität, Verfügbarkeit), über die sechs Schadenskategorien.
4. **In eine Schutzklasse einordnen** — normal, hoch oder sehr hoch.

Ergebnis: bei „normal" genügt der IT-Grundschutz, sonst folgt eine verfahrensspezifische
Risikoanalyse.

</details>

### 10. Was ist ein ISMS, und wofür steht die zugehörige Norm?

<details markdown="1">
<summary>Antwort</summary>

Ein **Informationssicherheits-Managementsystem** ist die Gesamtheit der Verfahren und
Regeln in einer Organisation, mit denen Informationssicherheit festgelegt, gesteuert,
überwacht, aufrechterhalten und fortlaufend verbessert wird.

Es ist ausdrücklich **kein Produkt**, sondern eine Organisationsaufgabe — Technik ist nur
ein Teil davon.

Maßgebliche Norm ist **ISO/IEC 27001**; in Deutschland verbreitet ist zusätzlich der
**IT-Grundschutz** des BSI, der sich damit zertifizieren lässt. Die fortlaufende
Verbesserung folgt dem **PDCA-Zyklus**: Plan, Do, Check, Act.

</details>

## Angriffe

### 11. Was ist ein Man-in-the-Middle-Angriff, und was schützt zuverlässig davor?

<details markdown="1">
<summary>Antwort</summary>

Der Angreifer klinkt sich zwischen zwei Kommunikationspartner und gibt sich gegenüber jedem als der jeweils andere aus. Er kann mitlesen und verändern, ohne bemerkt zu werden. Typische Wege: ein gefälschter WLAN-Zugangspunkt, ARP-Spoofing, ein manipulierter DNS-Eintrag.

Schutz bietet TLS — aber nur zusammen mit der **Prüfung des Zertifikats**. Verschlüsselung allein hilft nicht: Eine sauber verschlüsselte Verbindung zum Angreifer ist genauso wertlos wie eine unverschlüsselte.

Verletzt werden Vertraulichkeit und Integrität.

</details>

### 12. Wie funktioniert eine SQL-Injection, und welche Gegenmaßnahme ist die wirksamste?

<details markdown="1">
<summary>Antwort</summary>

Eine Eingabe landet ungeprüft im Text einer SQL-Anweisung und verändert deren **Struktur**:

```sql
SELECT * FROM Benutzer WHERE Name = 'EINGABE';
-- Eingabe: ' OR '1'='1
SELECT * FROM Benutzer WHERE Name = '' OR '1'='1';
```

Wirksamste Gegenmaßnahme sind **vorbereitete Anweisungen mit Platzhaltern**. Der Server kennt die Struktur der Anweisung, bevor er die Werte sieht — ein Wert kann sie danach nicht mehr ändern.

Ergänzend: Eingaben gegen eine Positivliste prüfen, ein Datenbankkonto mit minimalen Rechten verwenden, Datenbankfehler nicht an den Nutzer durchreichen.

Nicht ausreichend ist das Maskieren von Sonderzeichen: eine Notlösung, die sich je nach Zeichensatz und Datenbanksystem umgehen lässt.

</details>

### 13. Unterscheiden Sie Cross-Site-Scripting von Cross-Site-Request-Forgery.

<details markdown="1">
<summary>Antwort</summary>

| | XSS | CSRF |
|---|---|---|
| Was der Angreifer einbringt | fremden Skriptcode in eine Seite | eine Anfrage im Namen des Opfers |
| Wem vertraut wird | der Nutzer der Seite | die Seite dem Browser des Nutzers |
| Ziel | Daten auslesen, Sitzung übernehmen | eine Aktion auslösen |
| Gegenmaßnahme | Ausgabe maskieren, Content Security Policy | Formularmerkmal je Anfrage, `SameSite` |

Kurz: XSS bringt Code zum Nutzer, CSRF bringt eine Anfrage zum Server. Bei XSS liest der Angreifer mit, bei CSRF handelt er im fremden Namen.

</details>

### 14. Was unterscheidet DoS von DDoS, und welches Schutzziel wird verletzt?

<details markdown="1">
<summary>Antwort</summary>

Beide überlasten einen Dienst, bis er für reguläre Nutzer nicht mehr erreichbar ist. Verletzt wird die **Verfügbarkeit**.

Beim **DoS** kommt der Angriff von einer Quelle und lässt sich über deren Adresse sperren. Beim **DDoS** kommen die Anfragen von vielen übernommenen Rechnern gleichzeitig — eine einzelne Sperre hilft nicht mehr.

Verbreitet ist die Verstärkung: Der Angreifer schickt kleine Anfragen mit gefälschter Absenderadresse an fremde Dienste, deren große Antworten beim Opfer landen.

Gegenmaßnahmen: Begrenzung der Anfragerate, Filter beim Netzbetreiber, Auslieferung über ein verteiltes Netz, ein Notfallplan mit Ansprechpartnern.

</details>

### 15. Wie läuft eine Anmeldung mit Kerberos ab, und warum müssen die Uhren stimmen?

<details markdown="1">
<summary>Antwort</summary>

Über einen vertrauenswürdigen Dritten, das Key Distribution Center aus Authentifizierungs- und Ticket-Dienst:

1. Der Nutzer meldet sich einmal an und erhält ein **Ticket Granting Ticket**.
2. Damit fordert er ein Ticket für einen bestimmten Dienst an.
3. Dieses legt er dem Dienst vor, der es prüft, ohne beim KDC nachzufragen.

Das **Kennwort wird nie über das Netz übertragen**; es dient nur zum Entschlüsseln der Antwort des KDC.

Die Uhren müssen übereinstimmen, weil Tickets einen Zeitstempel tragen und nur begrenzt gültig sind — das verhindert, dass ein abgefangenes Ticket später wiederverwendet wird. Weichen die Uhren um mehr als die erlaubte Spanne ab, meistens fünf Minuten, schlägt die Anmeldung fehl.

</details>

## Rechtsrahmen

### 16. Welche Meldefristen sieht das NIS-2-Umsetzungsgesetz bei einem erheblichen Sicherheitsvorfall vor?

<details markdown="1">
<summary>Antwort</summary>

| Frist | Was zu melden ist |
|---|---|
| **24 Stunden** | Erstmeldung |
| **72 Stunden** | Folgemeldung mit Bewertung |
| **1 Monat** nach der Meldung | Abschlussmeldung |

Die Fristen stehen in § 32 BSIG und laufen ab dem Zeitpunkt, an dem die Einrichtung von dem Vorfall Kenntnis erlangt.

Erfasst sind seit der Neufassung des BSIG nicht mehr nur Betreiber kritischer Anlagen, sondern auch besonders wichtige und wichtige Einrichtungen ab bestimmten Größen. Die Risikomanagementmaßnahmen stehen in § 30 BSIG und nennen zehn Bereiche, darunter Lieferkettensicherheit, Bewältigung von Sicherheitsvorfällen, Kryptografie und Multi-Faktor-Authentifizierung. § 38 nimmt die Geschäftsleitung persönlich in die Pflicht — umsetzen, überwachen, sich schulen lassen.

</details>

### 17. Nennen Sie die vier Risikostufen der EU-KI-Verordnung mit je einem Beispiel.

<details markdown="1">
<summary>Antwort</summary>

| Stufe | Beispiel | Folge |
|---|---|---|
| **Unannehmbar** | soziale Bewertung von Menschen | verboten |
| **Hoch** | Vorauswahl von Bewerbern | Konformitätsbewertung, umfangreiche Pflichten |
| **Begrenzt** | Chatbot | Transparenzpflicht |
| **Minimal** | Spamfilter | keine besonderen Pflichten |

Die Verordnung gilt gestaffelt: Verbote und die Pflicht zur KI-Kompetenz seit dem 2. Februar 2025, Modelle mit allgemeinem Verwendungszweck seit dem 2. August 2025, der überwiegende Teil ab dem 2. August 2026.

</details>
