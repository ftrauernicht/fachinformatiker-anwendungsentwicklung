# Prüfungsfragen: Netzwerktechnik

## Inhaltsverzeichnis

- [OSI-Modell](#osi-modell)
  - [1. Auf welcher Schicht arbeiten Hub, Switch und Router?](#1-auf-welcher-schicht-arbeiten-hub-switch-und-router)
  - [2. Ordnen Sie TCP, IP, HTTP und Ethernet den OSI-Schichten zu.](#2-ordnen-sie-tcp-ip-http-und-ethernet-den-osi-schichten-zu)
  - [3. Was ist der Unterschied zwischen TCP und UDP? Nennen Sie je einen Anwendungsfall.](#3-was-ist-der-unterschied-zwischen-tcp-und-udp-nennen-sie-je-einen-anwendungsfall)
- [IP-Adressierung und Subnetting](#ip-adressierung-und-subnetting)
  - [4. Gegeben ist 192.168.10.0/26. Wie viele Hosts passen hinein, und wie lautet die Broadcast-Adresse?](#4-gegeben-ist-19216810026-wie-viele-hosts-passen-hinein-und-wie-lautet-die-broadcast-adresse)
  - [5. Ein Netz braucht 100 Hosts. Welches Präfix ist das kleinste, das reicht?](#5-ein-netz-braucht-100-hosts-welches-präfix-ist-das-kleinste-das-reicht)
  - [6. Nennen Sie die drei privaten Adressbereiche.](#6-nennen-sie-die-drei-privaten-adressbereiche)
  - [7. Warum können mehrere Firmen dieselbe private Adresse verwenden?](#7-warum-können-mehrere-firmen-dieselbe-private-adresse-verwenden)
- [RAID](#raid)
  - [8. Ein Server hat vier Platten zu je 2 TB. Wie viel Nettokapazität liefern RAID 0, 1, 5 und 10?](#8-ein-server-hat-vier-platten-zu-je-2-tb-wie-viel-nettokapazität-liefern-raid-0-1-5-und-10)
  - [9. Warum ist RAID kein Backup?](#9-warum-ist-raid-kein-backup)
  - [10. Wie viele Platten braucht RAID 5 mindestens, und warum nicht weniger?](#10-wie-viele-platten-braucht-raid-5-mindestens-und-warum-nicht-weniger)
- [DHCP](#dhcp)
  - [11. Nennen Sie die vier Nachrichten eines vollständigen DHCP-Ablaufs in der richtigen Reihenfolge.](#11-nennen-sie-die-vier-nachrichten-eines-vollständigen-dhcp-ablaufs-in-der-richtigen-reihenfolge)
  - [12. Der Server lauscht auf UDP-Port 67. Warum kann der Client die Antwort nicht auf demselben Port empfangen?](#12-der-server-lauscht-auf-udp-port-67-warum-kann-der-client-die-antwort-nicht-auf-demselben-port-empfangen)
- [Speicher im Netz und Überwachung](#speicher-im-netz-und-überwachung)
  - [13. Worin unterscheiden sich NAS und SAN?](#13-worin-unterscheiden-sich-nas-und-san)
  - [14. Ein NAS enthält einen RAID-5-Verbund. Ist es damit ein SAN?](#14-ein-nas-enthält-einen-raid-5-verbund-ist-es-damit-ein-san)
  - [15. Was unterscheidet aktives von passivem Monitoring?](#15-was-unterscheidet-aktives-von-passivem-monitoring)

## OSI-Modell

### 1. Auf welcher Schicht arbeiten Hub, Switch und Router?

<details markdown="1">
<summary>Antwort</summary>

- **Hub und Repeater** auf Schicht 1 (Bitübertragung). Sie verstärken das Signal und
  schicken es an alle Ports weiter, ohne den Inhalt anzusehen.
- **Switch und Bridge** auf Schicht 2 (Sicherung). Sie lesen die MAC-Adresse und leiten
  den Frame gezielt an den richtigen Port.
- **Router** auf Schicht 3 (Vermittlung). Er liest die IP-Adresse und entscheidet, in
  welches Netz das Paket weitergeht.

Siehe [OSI-Modell](../01-netzwerktechnik.md#osi-schichten-modell).

</details>

### 2. Ordnen Sie TCP, IP, HTTP und Ethernet den OSI-Schichten zu.

<details markdown="1">
<summary>Antwort</summary>

| Protokoll | Schicht |
|---|---|
| HTTP | 7 — Anwendung |
| TCP | 4 — Transport |
| IP | 3 — Vermittlung |
| Ethernet | 2 — Sicherung |

Merkhilfe: die Einheit verrät die Schicht. Bit → 1, Frame → 2, Paket → 3, Segment → 4.

</details>

### 3. Was ist der Unterschied zwischen TCP und UDP? Nennen Sie je einen Anwendungsfall.

<details markdown="1">
<summary>Antwort</summary>

**TCP** ist verbindungsorientiert: Verbindungsaufbau per Drei-Wege-Handschlag,
Empfangsbestätigungen, Neuübertragung verlorener Segmente, Reihenfolge garantiert. Dafür
langsamer und mit mehr Overhead. Anwendungsfall: HTTP, E-Mail, Dateiübertragung — überall,
wo jedes Byte ankommen muss.

**UDP** ist verbindungslos: kein Verbindungsaufbau, keine Bestätigung, keine garantierte
Reihenfolge. Dafür schnell und mit wenig Overhead. Anwendungsfall: DNS-Abfragen,
Videostreaming, Voice over IP — dort ist ein verlorenes Paket weniger schlimm als eine
Verzögerung durch Neuübertragung.

</details>

## IP-Adressierung und Subnetting

### 4. Gegeben ist 192.168.10.0/26. Wie viele Hosts passen hinein, und wie lautet die Broadcast-Adresse?

<details markdown="1">
<summary>Antwort</summary>

/26 heißt: 26 Bit Netzanteil, also 32 − 26 = **6 Bit Hostanteil**.

- Adressen insgesamt: 2⁶ = 64
- Nutzbare Hosts: 64 − 2 = **62** (Netzadresse und Broadcast fallen weg)
- Subnetzmaske: 255.255.255.**192** (192 = 11000000)
- Netzadresse: 192.168.10.**0**
- Broadcast: 192.168.10.**63**
- Erster Host: 192.168.10.1, letzter Host: 192.168.10.62

Das nächste Subnetz beginnt bei 192.168.10.64.

</details>

### 5. Ein Netz braucht 100 Hosts. Welches Präfix ist das kleinste, das reicht?

<details markdown="1">
<summary>Antwort</summary>

Gesucht ist das kleinste *n* mit 2ⁿ − 2 ≥ 100.

- 2⁶ − 2 = 62 → zu wenig
- 2⁷ − 2 = **126** → reicht

7 Hostbits, also 32 − 7 = **/25**, Maske 255.255.255.128. Damit bleiben 26 Adressen
ungenutzt — kleiner geht es nicht, weil Präfixe nur in Zweierpotenzen springen.

</details>

### 6. Nennen Sie die drei privaten Adressbereiche.

<details markdown="1">
<summary>Antwort</summary>

| Bereich | CIDR | Klasse |
|---|---|---|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 | A |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 | B |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 | C |

Der häufigste Fehler ist, den B-Bereich bei 172.16.255.255 enden zu lassen. Er reicht bis
172.**31**.255.255, das sind 16 Netze der Größe /16.

</details>

### 7. Warum können mehrere Firmen dieselbe private Adresse verwenden?

<details markdown="1">
<summary>Antwort</summary>

Weil private Adressen im Internet **nicht geroutet** werden. Ein Router im Internet
verwirft Pakete mit solchen Zieladressen. Der Adressbereich ist damit nur innerhalb des
jeweiligen privaten Netzes sichtbar und kann beliebig oft parallel vergeben werden.

Nach außen tritt das Netz über einen Router mit einer öffentlichen Adresse auf; die
Übersetzung erledigt NAT (Network Address Translation).

</details>

## RAID

### 8. Ein Server hat vier Platten zu je 2 TB. Wie viel Nettokapazität liefern RAID 0, 1, 5 und 10?

<details markdown="1">
<summary>Antwort</summary>

| Level | Nettokapazität | Rechnung | Ausfalltoleranz |
|---|---|---|---|
| RAID 0 | 8 TB | 4 × 2 TB | keine Platte |
| RAID 1 | 2 TB (Vierfachspiegel) bzw. 4 TB (zwei Paare) | Kapazität der kleinsten Platte | 1 Platte je Spiegel |
| RAID 5 | 6 TB | (4 − 1) × 2 TB | 1 Platte |
| RAID 10 | 4 TB | 4 × 2 TB ÷ 2 | 1 Platte je Spiegelpaar |

Faustformel RAID 5: *(n − 1) × Plattengröße*, weil genau eine Platte an Kapazität für die
Parität draufgeht — verteilt über alle Platten, nicht auf einer eigenen.

</details>

### 9. Warum ist RAID kein Backup?

<details markdown="1">
<summary>Antwort</summary>

RAID schützt gegen den **Ausfall von Hardware**, nicht gegen Fehler im Inhalt. Alles, was
geschrieben wird, wird sofort auf alle Platten geschrieben — auch eine versehentliche
Löschung, ein fehlerhaftes Programm oder eine Verschlüsselung durch Ransomware.

Ein Backup ist eine Kopie zu einem *früheren Zeitpunkt* an einem *anderen Ort*. RAID
erfüllt beides nicht.

</details>

### 10. Wie viele Platten braucht RAID 5 mindestens, und warum nicht weniger?

<details markdown="1">
<summary>Antwort</summary>

**Drei.** RAID 5 verteilt Daten und Paritätsinformation über alle Platten. Die Parität
entsteht als XOR über die Datenblöcke; damit sie einen Ausfall ausgleichen kann, müssen
mindestens zwei Datenblöcke plus ein Paritätsblock auf verschiedenen Platten liegen.

Mit zwei Platten wäre die Parität identisch mit dem Datenblock — das wäre RAID 1.

</details>

## DHCP

### 11. Nennen Sie die vier Nachrichten eines vollständigen DHCP-Ablaufs in der richtigen Reihenfolge.

<details markdown="1">
<summary>Antwort</summary>

**DISCOVER → OFFER → REQUEST → ACK** (Merkwort: *DORA*)

1. **DHCPDISCOVER** — der Client ohne Adresse fragt per Broadcast alle Server im Netz
2. **DHCPOFFER** — jeder Server antwortet mit einem Adressangebot
3. **DHCPREQUEST** — der Client fordert eines der Angebote an, per Broadcast, damit die
   anderen Server ihr Angebot zurückziehen
4. **DHCPACK** — der gewählte Server bestätigt und nennt die Lease-Zeit

</details>

### 12. Der Server lauscht auf UDP-Port 67. Warum kann der Client die Antwort nicht auf demselben Port empfangen?

<details markdown="1">
<summary>Antwort</summary>

Weil der Client zu diesem Zeitpunkt noch **keine IP-Adresse** hat und die Antwort deshalb
als Broadcast kommt. Ein Broadcast erreicht alle Geräte im Netz. Ohne getrennte Ports
würden auch andere DHCP-Server die Antwort auf ihrem Lausch-Port 67 empfangen und
verarbeiten.

Deshalb: Server lauscht auf **67**, Client empfängt auf **68**.

</details>

## Speicher im Netz und Überwachung

### 13. Worin unterscheiden sich NAS und SAN?

<details markdown="1">
<summary>Antwort</summary>

Im Wesentlichen in der Ebene des Zugriffs.

| | NAS | SAN |
|---|---|---|
| Zugriffsebene | Datei | Block |
| Protokolle | SMB, NFS | Fibre Channel, iSCSI |
| Netz | vorhandenes LAN | eigenes Speichernetz |
| Der Client sieht | eine Freigabe | eine lokale Festplatte |
| Einsatz | Dateiablage, Sicherung | Datenbanken, Virtualisierung |

Ein NAS gibt ein Dateisystem frei, das es selbst verwaltet. Ein SAN liefert rohe Blöcke; das Dateisystem legt der zugreifende Server an.

</details>

### 14. Ein NAS enthält einen RAID-5-Verbund. Ist es damit ein SAN?

<details markdown="1">
<summary>Antwort</summary>

Nein. RAID und die Netzanbindung sind zwei verschiedene Fragen.

**RAID** beschreibt, wie Daten **innerhalb** eines Speichersystems über mehrere Platten verteilt werden — zur Ausfallsicherheit, zur Geschwindigkeit oder zu beidem.

**NAS und SAN** beschreiben, wie dieses Speichersystem **im Netz** erreichbar ist — über Dateifreigaben oder als Blockgerät.

Beides kommt üblicherweise zusammen vor: Ein NAS enthält fast immer selbst einen RAID-Verbund, bleibt aber ein NAS.

</details>

### 15. Was unterscheidet aktives von passivem Monitoring?

<details markdown="1">
<summary>Antwort</summary>

Beim **aktiven** Monitoring fragt der Überwachungsserver die Systeme in festen Abständen ab — per SNMP, mit einem Prüfskript oder durch einen Verbindungsversuch auf den Port.

Beim **passiven** Monitoring melden sich die Systeme selbst, etwa über Syslog oder einen installierten Agenten.

Der praktische Unterschied liegt im Ausfall: Ein aktiver Test merkt, wenn ein System gar nicht mehr antwortet. Eine passive Meldung, die nicht kommt, fällt erst auf, wenn jemand ihr Ausbleiben überwacht.

Zu einer brauchbaren Überwachung gehören außerdem zwei Schwellenwerte — Warnung und kritisch — und ein Verfahren gegen Fehlalarme. Eine Überwachung, die täglich zwanzig Meldungen erzeugt, wird ignoriert.

</details>
