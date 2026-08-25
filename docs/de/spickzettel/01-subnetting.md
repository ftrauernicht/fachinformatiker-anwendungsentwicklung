# Spickzettel: Subnetting

## Inhaltsverzeichnis

- [Präfix, Maske, Größe](#präfix-maske-größe)
- [Die Maskenwerte](#die-maskenwerte)
- [In vier Schritten zum Ergebnis](#in-vier-schritten-zum-ergebnis)
- [Von der Hostzahl zum Präfix](#von-der-hostzahl-zum-präfix)
- [Private Bereiche und Sonderadressen](#private-bereiche-und-sonderadressen)
- [Binär und dezimal im Kopf](#binär-und-dezimal-im-kopf)
- [Häufige Fehler](#häufige-fehler)

## Präfix, Maske, Größe

| Präfix | Subnetzmaske | Hostbits | Adressen | nutzbare Hosts | Blockgröße im letzten Oktett |
|---|---|---|---|---|---|
| /24 | 255.255.255.0 | 8 | 256 | 254 | 256 |
| /25 | 255.255.255.128 | 7 | 128 | 126 | 128 |
| /26 | 255.255.255.192 | 6 | 64 | 62 | 64 |
| /27 | 255.255.255.224 | 5 | 32 | 30 | 32 |
| /28 | 255.255.255.240 | 4 | 16 | 14 | 16 |
| /29 | 255.255.255.248 | 3 | 8 | 6 | 8 |
| /30 | 255.255.255.252 | 2 | 4 | 2 | 4 |
| /31 | 255.255.255.254 | 1 | 2 | 0 (Sonderfall Punkt-zu-Punkt) | 2 |
| /32 | 255.255.255.255 | 0 | 1 | 1 (Einzeladresse) | 1 |

| Präfix | Subnetzmaske | Adressen |
|---|---|---|
| /16 | 255.255.0.0 | 65.536 |
| /17 | 255.255.128.0 | 32.768 |
| /20 | 255.255.240.0 | 4.096 |
| /22 | 255.255.252.0 | 1.024 |
| /23 | 255.255.254.0 | 512 |

**Nutzbare Hosts = 2^Hostbits − 2.** Die zwei fallen weg für Netzadresse (alle Hostbits 0)
und Broadcast (alle Hostbits 1).

## Die Maskenwerte

Nur diese neun Werte können in einer Subnetzmaske vorkommen:

| Bits | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|---|
| Wert | 0 | 128 | 192 | 224 | 240 | 248 | 252 | 254 | 255 |

Steht in einer Aufgabe eine 255.255.255.**100**, ist die Aufgabe falsch oder es ist eine
Fangfrage.

## In vier Schritten zum Ergebnis

Gegeben: **192.168.20.77/27**

1. **Blockgröße bestimmen.** /27 → 32 − 27 = 5 Hostbits → 2⁵ = **32**.
2. **Netzadresse finden.** Größtes Vielfaches von 32, das ≤ 77 ist: 64.
   → Netz **192.168.20.64**
3. **Broadcast finden.** Netzadresse + Blockgröße − 1 = 64 + 32 − 1 = 95.
   → Broadcast **192.168.20.95**
4. **Hostbereich.** Alles dazwischen: **192.168.20.65 bis 192.168.20.94**, also 30 Hosts.

Das nächste Subnetz beginnt bei 192.168.20.96.

## Von der Hostzahl zum Präfix

| Gebrauchte Hosts | Hostbits | Präfix |
|---|---|---|
| bis 2 | 2 | /30 |
| bis 6 | 3 | /29 |
| bis 14 | 4 | /28 |
| bis 30 | 5 | /27 |
| bis 62 | 6 | /26 |
| bis 126 | 7 | /25 |
| bis 254 | 8 | /24 |
| bis 510 | 9 | /23 |
| bis 1022 | 10 | /22 |

Vorgehen: die Hostzahl auf die nächste Zeile aufrunden. Wer 100 Hosts braucht, nimmt /25,
nicht /26 — 62 wären zu wenig.

**Beim Aufteilen eines Netzes immer mit dem größten Teilnetz beginnen** (Variable Length
Subnet Mask). Sonst zerschneidet man sich die großen Blöcke und muss von vorn anfangen.

## Private Bereiche und Sonderadressen

| Bereich | CIDR | Zweck |
|---|---|---|
| 10.0.0.0 – 10.255.255.255 | /8 | privat, Klasse A |
| 172.16.0.0 – 172.31.255.255 | /12 | privat, Klasse B |
| 192.168.0.0 – 192.168.255.255 | /16 | privat, Klasse C |
| 127.0.0.0 – 127.255.255.255 | /8 | Loopback (localhost) |
| 169.254.0.0 – 169.254.255.255 | /16 | APIPA, wenn kein DHCP antwortet |
| 224.0.0.0 – 239.255.255.255 | /4 | Multicast |

## Binär und dezimal im Kopf

Die Stellenwerte eines Oktetts:

| 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |
|---|---|---|---|---|---|---|---|

**Dezimal → binär:** von links nach rechts prüfen, ob der Stellenwert hineinpasst.

`77`: 128 nein (0), 64 ja → Rest 13 (1), 32 nein (0), 16 nein (0), 8 ja → Rest 5 (1),
4 ja → Rest 1 (1), 2 nein (0), 1 ja → Rest 0 (1) = **01001101**

**Binär → dezimal:** die Stellenwerte über den Einsen addieren.

`11000000` = 128 + 64 = **192**

## Häufige Fehler

- **Die zwei vergessen.** 2⁶ = 64 Adressen, aber nur **62** Hosts.
- **/31 und /32 behandeln.** /31 wird bei Punkt-zu-Punkt-Verbindungen ohne Netz- und
  Broadcastadresse benutzt (RFC 3021), /32 ist eine einzelne Hostroute.
- **Blockgröße im falschen Oktett.** Bei /20 springt die Blockgröße im **dritten** Oktett:
  256 − 240 = 16, also 172.16.**0**.0, 172.16.**16**.0, 172.16.**32**.0 …
- **Netz- statt Hostbits gezählt.** /27 hat 27 Netzbits und **5** Hostbits, nicht 27.
