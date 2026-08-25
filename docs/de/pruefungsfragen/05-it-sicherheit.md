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
