# Prüfungsfragen: Cloud Computing

## Inhaltsverzeichnis

- [Servicemodelle](#servicemodelle)
  - [1. Ordnen Sie IaaS, PaaS und SaaS zu: Wer verantwortet was?](#1-ordnen-sie-iaas-paas-und-saas-zu-wer-verantwortet-was)
  - [2. Ein Kunde will eine eigene Java-Anwendung betreiben, sich aber nicht um Betriebssystem-Updates kümmern. Welches Modell?](#2-ein-kunde-will-eine-eigene-java-anwendung-betreiben-sich-aber-nicht-um-betriebssystem-updates-kümmern-welches-modell)
  - [3. Nennen Sie die fünf wesentlichen Merkmale von Cloud Computing nach NIST.](#3-nennen-sie-die-fünf-wesentlichen-merkmale-von-cloud-computing-nach-nist)
- [Bereitstellungsmodelle](#bereitstellungsmodelle)
  - [4. Unterscheiden Sie Private, Public, Hybrid und Community Cloud.](#4-unterscheiden-sie-private-public-hybrid-und-community-cloud)
  - [5. Nennen Sie je zwei Vor- und Nachteile der Public Cloud.](#5-nennen-sie-je-zwei-vor--und-nachteile-der-public-cloud)
- [Recht und Betrieb](#recht-und-betrieb)
  - [6. Worauf ist bei einem Cloud-Vertrag aus Sicht der DSGVO zu achten?](#6-worauf-ist-bei-einem-cloud-vertrag-aus-sicht-der-dsgvo-zu-achten)
  - [7. Was ist Vendor Lock-in, und wie begegnet man ihm?](#7-was-ist-vendor-lock-in-und-wie-begegnet-man-ihm)
  - [8. Was bedeutet „Shared Responsibility", und warum ist es prüfungsrelevant?](#8-was-bedeutet-shared-responsibility-und-warum-ist-es-prüfungsrelevant)

## Servicemodelle

### 1. Ordnen Sie IaaS, PaaS und SaaS zu: Wer verantwortet was?

<details markdown="1">
<summary>Antwort</summary>

| Schicht | On Premises | IaaS | PaaS | SaaS |
|---|---|---|---|---|
| Anwendung | Kunde | Kunde | Kunde | **Anbieter** |
| Daten | Kunde | Kunde | Kunde | Kunde |
| Laufzeitumgebung | Kunde | Kunde | **Anbieter** | **Anbieter** |
| Betriebssystem | Kunde | Kunde | **Anbieter** | **Anbieter** |
| Virtualisierung | Kunde | **Anbieter** | **Anbieter** | **Anbieter** |
| Server, Netz, Rechenzentrum | Kunde | **Anbieter** | **Anbieter** | **Anbieter** |

Von links nach rechts wandert Verantwortung zum Anbieter. Die **Daten** bleiben in jedem
Modell beim Kunden — das ist die Zeile, die in Prüfungsfragen zum Datenschutz zählt.

Beispiele: IaaS — virtuelle Maschine bei AWS EC2. PaaS — Azure App Service, Heroku.
SaaS — Microsoft 365, Salesforce.

</details>

### 2. Ein Kunde will eine eigene Java-Anwendung betreiben, sich aber nicht um Betriebssystem-Updates kümmern. Welches Modell?

<details markdown="1">
<summary>Antwort</summary>

**PaaS.** Der Anbieter stellt Betriebssystem und Laufzeitumgebung bereit und pflegt beide;
der Kunde bringt nur seine Anwendung mit.

Bei IaaS müsste der Kunde das Betriebssystem selbst aktuell halten. SaaS scheidet aus,
weil es dort keine eigene Anwendung gibt — SaaS liefert fertige Software.

</details>

### 3. Nennen Sie die fünf wesentlichen Merkmale von Cloud Computing nach NIST.

<details markdown="1">
<summary>Antwort</summary>

1. **On-Demand Self-Service** — der Nutzer bekommt Ressourcen selbst, ohne Rückfrage beim
   Anbieter
2. **Breiter Netzzugang** — erreichbar über Standardmechanismen von beliebigen Geräten
3. **Ressourcen-Pooling** — die Ressourcen werden mehreren Kunden gemeinsam bereitgestellt
   (Mandantenfähigkeit)
4. **Schnelle Elastizität** — Kapazität wächst und schrumpft kurzfristig, aus Sicht des
   Nutzers scheinbar unbegrenzt
5. **Messbarer Dienst** — Nutzung wird gemessen, überwacht und abgerechnet

</details>

## Bereitstellungsmodelle

### 4. Unterscheiden Sie Private, Public, Hybrid und Community Cloud.

<details markdown="1">
<summary>Antwort</summary>

| Modell | Wer nutzt sie | Typisch für |
|---|---|---|
| **Private Cloud** | eine Organisation allein, im eigenen oder gemieteten Rechenzentrum | hohe Anforderungen an Datenschutz und Kontrolle |
| **Public Cloud** | offen für jeden, Ressourcen geteilt | Standardlasten, schwankender Bedarf |
| **Hybrid Cloud** | Kombination beider, verbunden über definierte Schnittstellen | sensible Daten intern, Lastspitzen extern |
| **Community Cloud** | mehrere Organisationen mit gemeinsamen Anforderungen | Behörden, Hochschulen, Kliniken |

Der Prüfungsklassiker ist die Hybrid Cloud mit *Cloud Bursting*: der Normalbetrieb läuft
intern, Lastspitzen wandern in die Public Cloud.

</details>

### 5. Nennen Sie je zwei Vor- und Nachteile der Public Cloud.

<details markdown="1">
<summary>Antwort</summary>

**Vorteile:**

- Keine Investition in Hardware, Abrechnung nach Verbrauch (aus CAPEX wird OPEX)
- Kapazität lässt sich in Minuten anpassen, statt Wochen auf Hardware zu warten
- Wartung, Ersatzteile und Rechenzentrumsbetrieb entfallen

**Nachteile:**

- Abhängigkeit vom Anbieter, bis hin zum **Vendor Lock-in**, wenn proprietäre Dienste
  benutzt werden
- Datenschutz und Ort der Verarbeitung müssen vertraglich geregelt sein
- Ohne Internetverbindung kein Zugriff
- Bei dauerhaft hoher Grundlast auf Sicht teurer als eigene Hardware

</details>

## Recht und Betrieb

### 6. Worauf ist bei einem Cloud-Vertrag aus Sicht der DSGVO zu achten?

<details markdown="1">
<summary>Antwort</summary>

- **Auftragsverarbeitungsvertrag** nach Art. 28 DSGVO ist Pflicht, sobald der Anbieter
  personenbezogene Daten verarbeitet
- **Ort der Verarbeitung**: innerhalb der EU beziehungsweise des EWR unproblematisch. Bei
  Drittländern braucht es eine Rechtsgrundlage — Angemessenheitsbeschluss oder
  Standardvertragsklauseln plus Prüfung des Einzelfalls
- **Unterauftragnehmer** müssen benannt und genehmigt sein
- **Löschung und Rückgabe** der Daten am Vertragsende, nachweisbar
- **Technische und organisatorische Maßnahmen** nach Art. 32 sind zu belegen, etwa durch
  ein Zertifikat nach ISO/IEC 27001
- **Meldewege** bei einer Datenschutzverletzung, damit die 72-Stunden-Frist eingehalten
  werden kann

Verantwortlich bleibt in jedem Fall der **Auftraggeber**, nicht der Cloud-Anbieter.

</details>

### 7. Was ist Vendor Lock-in, und wie begegnet man ihm?

<details markdown="1">
<summary>Antwort</summary>

**Vendor Lock-in** ist die Abhängigkeit von einem Anbieter, aus der ein Wechsel technisch
oder wirtschaftlich unverhältnismäßig teuer wird. Ursachen sind proprietäre Schnittstellen,
eigene Datenformate und Gebühren für den Datenabzug.

Gegenmaßnahmen:

- Offene Standards und Formate bevorzugen
- Container statt anbietereigener Laufzeitumgebungen
- Infrastruktur als Code, damit sich der Aufbau anderswo wiederholen lässt
- Ausstiegsszenario schon bei Vertragsabschluss festlegen, inklusive Datenexport
- Mehrere Anbieter einsetzen, wo es sich lohnt (Multi-Cloud)

</details>

### 8. Was bedeutet „Shared Responsibility", und warum ist es prüfungsrelevant?

<details markdown="1">
<summary>Antwort</summary>

Das Modell der **geteilten Verantwortung** legt fest, wofür der Anbieter und wofür der
Kunde einsteht.

Der Anbieter verantwortet die Sicherheit **der** Cloud: Rechenzentrum, Hardware,
Virtualisierungsschicht, physischen Zugang. Der Kunde verantwortet die Sicherheit **in**
der Cloud: Zugriffsrechte, Konfiguration, Verschlüsselung, seine eigenen Daten und
Anwendungen.

Prüfungsrelevant, weil daraus die häufigste Ursache von Cloud-Vorfällen folgt: ein
falsch konfigurierter Speicherbereich, öffentlich erreichbar. Das ist kein Versagen des
Anbieters — es fällt in die Verantwortung des Kunden.

</details>
