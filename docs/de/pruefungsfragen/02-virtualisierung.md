# Prüfungsfragen: Virtualisierung

## Inhaltsverzeichnis

- [Hypervisor](#hypervisor)
  - [1. Was ist der Unterschied zwischen Typ-1- und Typ-2-Hypervisor?](#1-was-ist-der-unterschied-zwischen-typ-1--und-typ-2-hypervisor)
  - [2. Nennen Sie drei Gründe, warum ein Unternehmen Server virtualisiert.](#2-nennen-sie-drei-gründe-warum-ein-unternehmen-server-virtualisiert)
  - [3. Was spricht gegen Virtualisierung?](#3-was-spricht-gegen-virtualisierung)
- [Container](#container)
  - [4. Worin unterscheiden sich Container und virtuelle Maschine?](#4-worin-unterscheiden-sich-container-und-virtuelle-maschine)
  - [5. Warum ist ein Container schlechter isoliert als eine VM?](#5-warum-ist-ein-container-schlechter-isoliert-als-eine-vm)
  - [6. Was ist der Unterschied zwischen Image und Container?](#6-was-ist-der-unterschied-zwischen-image-und-container)
  - [7. Was passiert mit den Daten in einem Container, wenn er gelöscht wird?](#7-was-passiert-mit-den-daten-in-einem-container-wenn-er-gelöscht-wird)
  - [8. Wozu dient ein Dockerfile, und wozu docker-compose?](#8-wozu-dient-ein-dockerfile-und-wozu-docker-compose)

## Hypervisor

### 1. Was ist der Unterschied zwischen Typ-1- und Typ-2-Hypervisor?

<details markdown="1">
<summary>Antwort</summary>

**Typ 1 (bare metal)** läuft direkt auf der Hardware, ohne Betriebssystem darunter.
Beispiele: VMware ESXi, Microsoft Hyper-V, Proxmox VE, KVM. Weniger Overhead, bessere
Leistung, im Rechenzentrum der Normalfall.

**Typ 2 (hosted)** läuft als Anwendung in einem vorhandenen Betriebssystem. Beispiele:
VirtualBox, VMware Workstation. Bequemer einzurichten, aber jeder Zugriff auf die
Hardware geht durch das Wirtsbetriebssystem hindurch.

Faustregel für die Prüfung: Server → Typ 1, Arbeitsplatz → Typ 2.

</details>

### 2. Nennen Sie drei Gründe, warum ein Unternehmen Server virtualisiert.

<details markdown="1">
<summary>Antwort</summary>

- **Auslastung.** Ein physischer Server ist meist zu 10–20 % ausgelastet. Mehrere
  virtuelle Maschinen auf einem Blech nutzen dieselbe Hardware deutlich besser.
- **Kosten.** Weniger Hardware bedeutet weniger Anschaffung, weniger Strom, weniger
  Kühlung, weniger Platz im Rack.
- **Betrieb.** Snapshots, Klone und Live-Migration erlauben Sicherung, Test und Wartung
  ohne Ausfallzeit.

Weitere gültige Nennungen: schnellere Bereitstellung, Trennung von Diensten, einfachere
Notfallwiederherstellung.

</details>

### 3. Was spricht gegen Virtualisierung?

<details markdown="1">
<summary>Antwort</summary>

- **Ein einzelner Ausfall trifft alle.** Fällt der Wirt aus, sind sämtliche VMs darauf
  weg. Ohne Cluster ist das ein neuer Single Point of Failure.
- **Leistungsverlust** durch die Virtualisierungsschicht, spürbar bei sehr I/O-lastigen
  Anwendungen.
- **Lizenzen.** Manche Software wird nach physischen Kernen lizenziert oder verbietet den
  Betrieb in einer VM.
- **Zusätzliches Wissen** ist nötig; die Verwaltungsschicht will selbst gepflegt und
  gesichert werden.

</details>

## Container

### 4. Worin unterscheiden sich Container und virtuelle Maschine?

<details markdown="1">
<summary>Antwort</summary>

| | Virtuelle Maschine | Container |
|---|---|---|
| Enthält | vollständiges Gastbetriebssystem | nur Anwendung und Abhängigkeiten |
| Kernel | eigener je VM | teilt sich den Kernel des Wirts |
| Größe | Gigabyte | Megabyte |
| Startzeit | Minute | Sekunde |
| Trennung | stark, durch den Hypervisor | schwächer, durch Namespaces und cgroups |

Kernaussage: eine VM virtualisiert **Hardware**, ein Container virtualisiert das
**Betriebssystem**.

</details>

### 5. Warum ist ein Container schlechter isoliert als eine VM?

<details markdown="1">
<summary>Antwort</summary>

Weil alle Container auf einem Wirt **denselben Kernel** benutzen. Die Trennung entsteht
durch Namespaces (getrennte Sicht auf Prozesse, Netz, Dateisystem) und cgroups (Grenzen
für CPU und Speicher) — beides Mechanismen *innerhalb* des Kernels.

Eine Lücke im Kernel kann deshalb aus einem Container heraus alle anderen betreffen. Bei
einer VM liegt der Hypervisor dazwischen, und jede VM hat einen eigenen Kernel.

Praktische Folge: Container mit unterschiedlichen Vertraulichkeitsstufen gehören nicht auf
denselben Wirt.

</details>

### 6. Was ist der Unterschied zwischen Image und Container?

<details markdown="1">
<summary>Antwort</summary>

Ein **Image** ist die unveränderliche Vorlage: Dateisystem, Abhängigkeiten, Startbefehl.
Es liegt in einer Registry und wird versioniert (Tag).

Ein **Container** ist eine laufende Instanz dieses Images, mit einer beschreibbaren
Schicht obendrauf. Aus einem Image lassen sich beliebig viele Container starten.

Vergleich aus der Objektorientierung: Image = Klasse, Container = Objekt.

</details>

### 7. Was passiert mit den Daten in einem Container, wenn er gelöscht wird?

<details markdown="1">
<summary>Antwort</summary>

Sie sind **weg**. Die beschreibbare Schicht eines Containers gehört zu seiner Lebensdauer.

Wer Daten behalten will, hängt ein **Volume** ein — einen Speicherbereich außerhalb des
Containers, der seine Löschung überlebt. Das ist der Grund, warum Datenbanken in
Containern immer mit Volume betrieben werden.

</details>

### 8. Wozu dient ein Dockerfile, und wozu docker-compose?

<details markdown="1">
<summary>Antwort</summary>

Ein **Dockerfile** beschreibt, wie ein Image gebaut wird: Basis-Image, kopierte Dateien,
installierte Pakete, Startbefehl. Ergebnis ist genau **ein** Image.

**docker-compose** beschreibt, wie **mehrere** Container zusammen betrieben werden:
welche Images, welche Netzwerke, welche Volumes, welche Umgebungsvariablen, welche
Abhängigkeiten untereinander. Typisch für Anwendung plus Datenbank plus Cache.

Kurz: Dockerfile baut, Compose betreibt.

</details>
