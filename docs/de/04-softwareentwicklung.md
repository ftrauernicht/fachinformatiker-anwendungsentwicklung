# Softwareentwicklung

## Inhaltsverzeichnis

- [Web Entwicklung](#web-entwicklung)
  - [Auszeichnungssprachen](#auszeichnungssprachen)
    - [HTML - Hypertext Markup Language](#html---hypertext-markup-language)
      - [DOM - Document Object Model](#dom---document-object-model)
  - [Protokolle](#protokolle)
    - [HTTP/S](#https)
      - [HTTP-400](#http-400)
      - [HTTP-500](#http-500)
- [Objektorientierung](#objektorientierung)
  - [Interfaces](#interfaces)
    - [Deklaration](#deklaration)
    - [Beispiel](#beispiel)
    - [Namenskonventionen](#namenskonventionen)
  - [Abstraktion](#abstraktion)
    - [Programmiersprachen](#programmiersprachen)
    - [Abstraktion in der objektorientierten Programmierung](#abstraktion-in-der-objektorientierten-programmierung)
- [Softwarequalität](#softwarequalität)
- [Testen](#testen)
  - [Teststufen](#teststufen)
  - [Black-Box- und White-Box-Test](#black-box--und-white-box-test)
  - [Last- und Performancetest](#last--und-performancetest)
  - [Testgetriebene Entwicklung](#testgetriebene-entwicklung)
- [Architektur- und Entwurfsmuster](#architektur--und-entwurfsmuster)
  - [Architekturmuster](#architekturmuster)
  - [Entwurfsmuster](#entwurfsmuster)
  - [Abgrenzung der beiden Begriffe](#abgrenzung-der-beiden-begriffe)
- [Rechtliche Pflichten bei Webanwendungen](#rechtliche-pflichten-bei-webanwendungen)
  - [Impressum nach dem Digitale-Dienste-Gesetz](#impressum-nach-dem-digitale-dienste-gesetz)
  - [Barrierefreiheit nach dem Barrierefreiheitsstärkungsgesetz](#barrierefreiheit-nach-dem-barrierefreiheitsstärkungsgesetz)

## Web Entwicklung

### Auszeichnungssprachen

#### HTML - Hypertext Markup Language

[^3]
HTML ist eine textbasierte Auszeichnungssprache zur Strukturierung elektronischer Dokumente wie Texte mit Hyperlinks, Bilder und anderen Inhalten. HTML-Dokumente sind die Grundlage des WWW (World-Wide-Web) und werden von Webbrowsern dargestellt.

Anders als einige Leute behaupten ist HTML **KEINE** Programmiersprache.
HTML kann Merkmale einer Programmiersprache wie **Variablen** und **Kontrollstrukturen** nicht ausweisen.

##### DOM - Document Object Model

[^4]
Document Object Model

- meist HTML
- kann aber auch XML oder XHTML sein
- Das DOM stellt eine Baumstruktur dar, in der jedes Element des Dokumentes als Knoten im Baum repräsentiert wird.

### Protokolle

#### HTTP/S

[^1] [^2]

- Hyper Text Transport Protocol
- Secure Hyper Text Transport Protocol

##### HTTP-400

HTTP Response Code 400 bezieht sich auf Client Fehler

###### Arten von HTTP-400

- 400 Bad Request
  - Der Server kann oder will die Anfrage nicht bearbeiten wegen eines vermeidlichen Client Errors (Request falsch, Syntax falsch, Inhalt zu groß etc.)
- 403 Forbidden
  - Die Anfrage hat Daten enthalten die vom Server zwar verstanden wurde aber nicht verarbeitet wird (Eintrag doppelt)
- 404 Not Found
  - Die Angefragte Resource konnte nicht gefunden werden

##### HTTP-500

HTTP Response Code 500 bezieht sich auf Server Fehler

###### Arten von HTTP-500

- 500 Internal Server Error
  - Eine generische Fehlermeldung welche gegeben wird wenn etwas unerwartetes passiert ist
- 502 Bad Gateway
  - Der Server fungierte als Gateway oder Proxy und erhielt eine ungültige Antwort
- 503 Service Unavailable
  - Der Server kann die Anfrage nicht verarbeiten (zu viele Anfragen, down for maintenance)

## Objektorientierung

### Interfaces

Ein Interface oder auch Schnittstelle definiert in der objektorientierte Programmierung, welche Methoden in den unterschiedlichen Klassen u. Ä vorhanden sind oder sein müssen.  
Eine Schnittstelle gibt an, welche Methoden vorhanden sind oder vorhanden sein müssen.  
Schnittstellen stellen eine Garantie über die in einer Klasse vorhandenen Methoden dar. Sie geben an, dass alle Objekte, die diese Schnittstellen besitzen, gleich behandelt werden können.

In Programmiersprachen die keine Mehrfachvererbung unterstützen wie z.B. Java, können Schnittstellen verwendet werden, um Kompatibilitäten zwischen Klassen zu definieren, die nicht voneinander erben.

#### Deklaration

Andere Programmiersprachen, die Mehrfachvererbung unterstützen, zum Beispiel C++, kennen zwar das Konzept von Schnittstellen, behandeln diese aber wie gewöhnliche Klassen. Man spricht dann auch von abstrakten Klassen. Manchmal wird auch eine eigene Sprache (eine sogenannte Schnittstellenbeschreibungssprache, IDL) zur Deklaration der Schnittstelle verwendet – meist ist das bei Middleware-Systemen wie CORBA oder DCOM der Fall. Objektbasierte Sprachen ohne strenge Typisierung kennen meist keine Schnittstellen.

#### Beispiel

**C#**

```c#
public interface IFace
{
    void Move(float x, float y);
    void Turn(float x, float y, double angle);
    void Scale(float factor);
    double GetArea();
    void SetColor(Color color);
    Color GetColor();
}

public class Polygon : IFace
{
    private List<PointF> points;
    private Color color;

    public Polygon(List<PointF> points, Color color)
    {
        this.points = points;
        this.color = color;
    }

public void Move(float x, float y)
	{
		for (int i = 0; i < points.Count; i++)
		{
			PointF point = points[i];
			points[i] = new PointF(point.X + x, point.Y + y);
		}
	}
	
	public void Turn(float x, float y, double angleInDegrees)
	{
		double angleInRadians = angleInDegrees * (Math.PI / 180);
		double cosine = Math.Cos(angleInRadians);
		double sine = Math.Sin(angleInRadians);
		for (int i = 0; i < points.Count; i++)
		{
			PointF point = points[i];
			points[i] = new PointF((float) (cosine * (point.X - x) - sine * (point.Y - y) + x), (float) (sine * (point.X - x) + cosine * (point.Y - y) + y));
		}
	}
	
	public void Scale(float factor)
	{
		for (int i = 0; i < points.Count; i++)
		{
			PointF point = points[i];
			points[i] = new PointF(factor * point.X, factor * point.Y);
		}
	}
	
	public double GetArea()
	{
		double area = 0.0;
		for (int i = 0; i < points.Count; i++)
		{
			PointF point1 = points[i];
			PointF point2 = points[(i + 1) % points.Count];
			area += (point1.Y + point2.Y) * (point1.X - point2.X);
		}
		return Math.Abs(area / 2.0);
	}
	
	public void SetColor(Color color)
	{
		this.color = color;
	}
	
	public Color GetColor()
	{
		return color;
	}
}
```

#### Namenskonventionen

In einigen Programmiersprachen ist es üblich, Schnittstellen durch besondere Präfixe oder Suffixe erkennbar zu machen. So wird häufig ein "I" oder ein "IF" angehängt.  
Im oben aufgeführtem Beispiel wäre dies ein "I" für "IFace". Dies wird normalerweise bei C# angewandt.

### Abstraktion

[^6]
Der Begriff Abstraktion wird in der Informatik häufig eingesetzt und beschreibt die Trennung zwischen **Konzept** und **Umsetzung**.  

#### Programmiersprachen

Unterschiedliche Programmiersprachen bieten unterschiedliche Möglichkeiten von Abstraktion, wie zum Beispiel:

- In Objektorientierten Sprachen wie C++, Object Pascal oder Java, wurde das Konzept der Abstraktion in Form einer eigenen deklarativen Anweisung umgesetzt. Nach einer derartigen Deklaration ist es die Aufgabe des Programmierers, eine Klasse zu implementieren, um eine Instanz eines Objektes davon erzeugen zu können.

#### Abstraktion in der objektorientierten Programmierung

Benötigt Ausarbeitung

## Softwarequalität

Qualität ist in der Prüfung kein Gefühl, sondern eine Liste. Maßgeblich ist das Produktqualitätsmodell der Normenreihe ISO/IEC 25010, das acht Merkmale nennt und jedes davon in Untermerkmale zerlegt.[^7]

| Merkmal | Frage dahinter | Beispiel für eine Verletzung |
|---|---|---|
| **Funktionale Eignung** | Tut die Software, was sie soll — vollständig und richtig? | Die Rechnungssumme wird falsch gerundet |
| **Leistungseffizienz** | Wie viel Zeit und wie viele Betriebsmittel braucht sie dafür? | Die Suche antwortet erst nach zwölf Sekunden |
| **Kompatibilität** | Arbeitet sie mit anderen Systemen zusammen, ohne sie zu stören? | Der Export erzeugt eine Datei, die keine andere Anwendung lesen kann |
| **Benutzbarkeit** | Kommen die vorgesehenen Nutzer damit zurecht? | Der Abbrechen-Knopf speichert |
| **Zuverlässigkeit** | Läuft sie über die Zeit stabil und erholt sich von Fehlern? | Nach dem dritten Tag ohne Neustart bleibt der Dienst stehen |
| **Sicherheit** | Sind Daten und Funktionen vor unbefugtem Zugriff geschützt? | Eine fremde Kundennummer in der Adresszeile zeigt fremde Daten |
| **Wartbarkeit** | Wie teuer ist eine Änderung? | Eine neue Steuerklasse erfordert Änderungen an neunzehn Stellen |
| **Übertragbarkeit** | Lässt sie sich in eine andere Umgebung bringen? | Die Anwendung läuft nur mit genau dieser Datenbankversion |

Die Fassung von 2023 hat das Modell überarbeitet: Benutzbarkeit heißt jetzt Interaktionsfähigkeit, Übertragbarkeit heißt Flexibilität, und Betriebssicherheit ist als neuntes Merkmal hinzugekommen — die Frage, ob das System Menschen, Sachwerte oder Umwelt gefährden kann.[^7] In Lehrbüchern und Prüfungsaufgaben findet sich bislang überwiegend die Einteilung mit acht Merkmalen.

Zwei Begriffe, die im Deutschen beide „Sicherheit" heißen und regelmäßig verwechselt werden: **Security** schützt das System vor seiner Umwelt, **Safety** die Umwelt vor dem System.

## Testen

### Teststufen

Die Teststufen bauen aufeinander auf, und jede gehört zu einer Stufe der Spezifikation. Genau das ist der Kern des V-Modells: links die Spezifikation, rechts der zugehörige Test.[^8]

| Stufe | Prüfgegenstand | Grundlage | Wer prüft |
|---|---|---|---|
| **Komponententest** (Unit-Test) | eine einzelne Klasse oder Methode, isoliert | technischer Feinentwurf | Entwicklung |
| **Integrationstest** | das Zusammenspiel mehrerer Komponenten, auch mit Datenbank und Schnittstellen | Architektur, Grobentwurf | Entwicklung |
| **Systemtest** | das vollständige System in einer produktionsnahen Umgebung | Pflichtenheft | Test oder Qualitätssicherung |
| **Abnahmetest** | ob das System die Anforderungen des Auftraggebers erfüllt | Lastenheft, Vertrag | Auftraggeber |

Der Prüfungskatalog von 2025 hat die Aufzählung dabei von „Komponenten-, Funktions-, Integrationstest" auf „Komponenten-, Integrations-, Systemtest" umgestellt.

Je später ein Fehler auffällt, desto teurer wird seine Beseitigung — je Stufe grob um den Faktor zehn. Das ist das eigentliche Argument für automatisierte Komponententests, nicht die Zahl in der Überdeckungsstatistik.

### Black-Box- und White-Box-Test

**Black Box** heißt: getestet wird gegen die Spezifikation, ohne den Quelltext zu kennen. Eingabe hinein, Ausgabe vergleichen. Die üblichen Verfahren sind Äquivalenzklassenbildung und Grenzwertanalyse.

**White Box** heißt: der Quelltext ist bekannt, getestet wird gegen seine Struktur. Maß ist die Überdeckung — Anweisungs-, Zweig- oder Pfadüberdeckung.

Die Grenzwertanalyse ist der Klassiker in Prüfungsaufgaben. Bei einer erlaubten Menge von 1 bis 100 werden 0, 1, 100 und 101 getestet, nicht 50: Fehler sitzen an den Rändern, weil dort die Vergleichsoperatoren stehen.

### Last- und Performancetest

Seit 2025 steht beides ausdrücklich im Prüfungskatalog. Diese Tests messen nicht, *ob* etwas funktioniert, sondern *wie gut* unter Belastung.[^9]

| Testart | Frage dahinter |
|---|---|
| **Lasttest** | Hält das System die erwartete Last aus, etwa 500 gleichzeitige Nutzer? |
| **Stresstest** | Wo liegt die Grenze, und was passiert beim Überschreiten? |
| **Dauertest** | Läuft es auch nach 48 Stunden noch, oder wächst der Speicherverbrauch stetig? |
| **Skalierbarkeitstest** | Bringt doppelte Hardware auch doppelten Durchsatz? |

Gemessen werden Antwortzeit, Durchsatz und Fehlerrate. Ein Lasttest ohne vorher festgelegte Zielwerte erzeugt Zahlen, aber kein Ergebnis.

### Testgetriebene Entwicklung

Bei testgetriebener Entwicklung wird der Test vor dem Code geschrieben. Der Zyklus heißt Red-Green-Refactor:[^10]

1. **Rot** — einen Test schreiben, der die gewünschte Funktion prüft. Er schlägt fehl, weil es die Funktion noch nicht gibt.
2. **Grün** — gerade so viel Code schreiben, dass der Test durchläuft. Nicht mehr.
3. **Refactor** — den Code aufräumen, ohne sein Verhalten zu ändern. Der eben geschriebene Test sichert das ab.

Der Nutzen liegt weniger in der Testabdeckung als im Entwurf: Wer den Aufruf zuerst schreibt, merkt sofort, wenn eine Schnittstelle unbequem zu benutzen ist.

## Architektur- und Entwurfsmuster

Beides sind wiederverwendbare Lösungen für wiederkehrende Probleme. Sie unterscheiden sich in der Flughöhe: Ein Architekturmuster ordnet das System als Ganzes, ein Entwurfsmuster löst ein Problem innerhalb weniger Klassen.

### Architekturmuster

Architekturmuster legen fest, aus welchen Bausteinen ein System besteht und wie sie miteinander reden.[^11]

| Muster | Idee | Typischer Einsatz |
|---|---|---|
| **Schichtenarchitektur** | Präsentation, Fachlogik und Datenhaltung getrennt; jede Schicht kennt nur die darunterliegende | Standard für Geschäftsanwendungen |
| **Model View Controller** | Datenmodell, Darstellung und Steuerung getrennt | Bedienoberflächen, besonders im Web |
| **Client-Server** | ein Dienst, viele Anfragende | fast jede vernetzte Anwendung |
| **Microservices** | fachlich geschnittene, unabhängig ausrollbare Dienste | große Systeme mit vielen Teams |
| **Ereignisgesteuerte Architektur** | Komponenten reagieren auf Ereignisse, statt sich direkt aufzurufen | Verarbeitungsketten, lose Kopplung |

### Entwurfsmuster

Die klassische Einteilung stammt aus dem Buch der sogenannten Viererbande und kennt drei Gruppen:[^12]

| Gruppe | Zweck | Beispiele |
|---|---|---|
| **Erzeugungsmuster** | wie Objekte entstehen | Singleton, Fabrikmethode, Erbauer |
| **Strukturmuster** | wie Objekte zusammengesetzt werden | Adapter, Dekorierer, Fassade, Kompositum |
| **Verhaltensmuster** | wie Objekte zusammenarbeiten | Beobachter, Strategie, Befehl, Iterator |

Drei tauchen in Aufgaben besonders häufig auf:

- **Singleton** stellt sicher, dass es von einer Klasse genau ein Objekt gibt — etwa für eine Konfiguration. Erkennungsmerkmal ist der private Konstruktor.
- **Beobachter** benachrichtigt angemeldete Objekte über eine Zustandsänderung, ohne sie im Einzelnen zu kennen. Grundlage jeder Ereignisbehandlung.
- **Strategie** kapselt austauschbare Algorithmen hinter einer gemeinsamen Schnittstelle, zum Beispiel mehrere Verfahren zur Berechnung von Versandkosten.

### Abgrenzung der beiden Begriffe

Ein Muster ist weder Bibliothek noch fertiger Code, sondern eine Beschreibung. In der Prüfung ist das Erkennen wichtiger als das Implementieren: Gefragt werden Name, Zweck und ein Beispiel — selten das vollständige Klassendiagramm.

## Rechtliche Pflichten bei Webanwendungen

Drei Pflichten treffen praktisch jede öffentlich erreichbare Anwendung, und alle drei haben sich seit 2023 geändert.

### Impressum nach dem Digitale-Dienste-Gesetz

Das Telemediengesetz gibt es nicht mehr. Seit dem 14. Mai 2024 steht die Impressumspflicht in § 5 des Digitale-Dienste-Gesetzes; inhaltlich hat sich nichts geändert, nur der Begriff „Telemedien" ist durch „digitale Dienste" ersetzt worden.[^13] Wer in einer Anwendung noch „§ 5 TMG" ausgibt, zitiert eine aufgehobene Norm.

Aus demselben Gesetzespaket ist das TTDSG zum TDDDG geworden — Telekommunikation-Digitale-Dienste-Datenschutz-Gesetz. Die Einwilligung für Cookies und vergleichbare Zugriffe auf das Endgerät steht dort weiterhin in § 25.[^14]

### Barrierefreiheit nach dem Barrierefreiheitsstärkungsgesetz

Das Barrierefreiheitsstärkungsgesetz gilt seit dem 28. Juni 2025. Es verpflichtet unter anderem Anbieter von Dienstleistungen im elektronischen Geschäftsverkehr — Onlineshops, Buchungsstrecken, Apps —, ihr Angebot barrierefrei zu gestalten, sofern es sich an Verbraucher richtet.[^15]

Ausgenommen sind Kleinstunternehmen mit weniger als zehn Beschäftigten und höchstens zwei Millionen Euro Jahresumsatz, allerdings nur bei Dienstleistungen und nicht bei Produkten.

Der technische Maßstab ist die europäische Norm EN 301 549, die für Webinhalte auf die WCAG 2.1 in der Stufe AA verweist. Deren vier Grundsätze:[^16]

| Grundsatz | Bedeutung | Beispiel für eine Maßnahme |
|---|---|---|
| **Wahrnehmbar** | Inhalte müssen mit mindestens einem Sinn erfassbar sein | Alternativtexte für Bilder, ausreichender Kontrast |
| **Bedienbar** | alles muss auch ohne Maus erreichbar sein | vollständige Tastaturbedienung, sichtbarer Fokus |
| **Verständlich** | Sprache und Verhalten müssen nachvollziehbar sein | Fehlermeldungen im Klartext, kein unerwarteter Kontextwechsel |
| **Robust** | auch Hilfsmittel müssen den Inhalt auswerten können | gültiges HTML, sinnvolle Semantik statt bedeutungsloser Verschachtelung |

Für Anwendungsentwickler ist das die Änderung mit den unmittelbarsten Folgen für den eigenen Code. Alternativtexte, Beschriftungen von Formularfeldern, Fokusreihenfolge und Kontrastwerte entscheidet niemand in der Rechtsabteilung — die entstehen beim Schreiben der Oberfläche.

[^1]: <https://de.wikipedia.org/wiki/HTTP-Statuscode>
[^2]: <https://de.wikipedia.org/wiki/Hypertext_Transfer_Protocol>
[^3]: <https://de.wikipedia.org/wiki/Hypertext_Markup_Language>
[^4]: <https://de.wikipedia.org/wiki/Document_Object_Model>
[^6]: <https://de.wikipedia.org/wiki/Abstraktion_(Informatik)>
[^7]: <https://quality.arc42.org/standards/iso-25010>
[^8]: <https://de.wikipedia.org/wiki/V-Modell>
[^9]: <https://de.wikipedia.org/wiki/Lasttest_(Computer)>
[^10]: <https://de.wikipedia.org/wiki/Testgetriebene_Entwicklung>
[^11]: <https://de.wikipedia.org/wiki/Architekturmuster>
[^12]: <https://de.wikipedia.org/wiki/Entwurfsmuster>
[^13]: <https://www.gesetze-im-internet.de/ddg/__5.html>
[^14]: <https://www.gesetze-im-internet.de/ttdsg/__25.html>
[^15]: <https://www.gesetze-im-internet.de/bfsg/>
[^16]: <https://www.w3.org/TR/WCAG21/>
