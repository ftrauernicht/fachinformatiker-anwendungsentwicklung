# Anwendungsfalldiagramm (Use Case)

## Inhaltsverzeichnis

- [Use-Case Diagramm](#use-case-diagramm)
  - [Keywords](#keywords)
  - [Elemente](#elemente)
    - [Systemkontext](#systemkontext)
    - [Akteur](#akteur)
    - [Anwendungsfall](#anwendungsfall)
    - [Beziehungen](#beziehungen)
      - [Assoziation/Kommunikation](#assoziationkommunikation)
      - [Multiplizität](#multiplizität)
      - [Generalisierung von Anwendungsfällen](#generalisierung-von-anwendungsfällen)
      - [Generalisierung von Akteuren](#generalisierung-von-akteuren)
      - [Include-Beziehung](#include-beziehung)
      - [Extend-Beziehung](#extend-beziehung)
      - [Extend-Beziehung mit extension point](#extend-beziehung-mit-extension-point)
      - [Anwendungsfall mit extension point](#anwendungsfall-mit-extension-point)

## Use-Case Diagramm

[^1]

Das Use-Case Diagramm wird auch Anwendungsfalldiagramm bezeichnet und ist eine der Diagrammarten der Unified Modelling Language (UML). Es stellt Anwendungsfälle und Akteure mit ihren jeweiligen Abhängigkeiten und Beziehungen dar.

### Keywords

- **Ziel** ist es, möglichst einfach zu zeigen, was man mit dem zu bauenden Softwaresystem machen will, welche Fälle der Anwendung es also gibt.
- **Akteure** werden als "Strichmännchen" dargestellt, welche sowohl Personen wie Kunden oder Administratoren als auch ein System darstellen können.
- **Anwendungsfälle** werden in Ellipsen dargestellt. Sie müssen beschrieben werden (z.B. in einem Kommentar oder einer eigenen Datei).
- **Assoziationen** zwischen Akteuren und Anwendungsfällen müssen durch Linien gekennzeichnet werden.
- **Systemgrenzen** werden durch Rechtecke gekennzeichnet.
- **include-Beziehung** vom aufrufenden Anwendungsfall zum inkludierten Anwendungsfall werden als gestrichelter Pfeil mit dem Stereotyp ``<<include>>`` dargestellt.
- **extend-Beziehung** vom erweiternden Anwendungsfall zum aufrufenden Anwendungsfall werden als gestrichelter Pfeil mit dem Stereotyp ``<<extend>>`` dargestellt. Der erweiternde Anwendungsfall kann, muss aber nicht aktiviert werden.

### Elemente

#### Systemkontext

<img src="../../assets/img/uml-use-case/system-context.svg" alt="Systemgrenze als Rechteck um zwei Anwendungsfälle" width="200px">

Der Systemkontext wurde durch Systemgrenzen in Form von Rechtecken gekennzeichnet.

#### Akteur

<img src="../../assets/img/uml-use-case/actor.svg" alt="Akteur als Strichmännchen" width="120px">

Akteure werden als "Strichmännchen" dargestellt, welche sowohl Personen wie Kunden oder Administratoren als auch ein System darstellen können.

#### Anwendungsfall

<img src="../../assets/img/uml-use-case/use-case.svg" alt="Anwendungsfall als beschriftete Ellipse" width="200px">

Anwendungsfälle werden in Ellipsen dargestellt. Sie müssen (z.B. in einem Kommentar oder einer eigenen Datei) beschrieben werden.

#### Beziehungen

##### Assoziation/Kommunikation

<img src="../../assets/img/uml-use-case/association.svg" alt="Linie zwischen Akteur und Anwendungsfall" width="300px">

Assoziation / Kommunikation von Akteur und Anwendungsfall

##### Multiplizität

<img src="../../assets/img/uml-use-case/multiplicity.svg" alt="Assoziation mit Multiplizitätsangaben an beiden Enden" width="300">

Multiplizität von Akteur und Anwendungsfall, wobei die Voreinstellung des Akteurs 1 ist.

##### Generalisierung von Anwendungsfällen

<img src="../../assets/img/uml-use-case/generalisation.svg" alt="Generalisierungspfeil zwischen zwei Anwendungsfällen" width="300">

##### Generalisierung von Akteuren

<img src="../../assets/img/uml-use-case/generalisation-actor.svg" alt="Generalisierungspfeil zwischen zwei Akteuren" width="300">

##### Include-Beziehung

<img src="../../assets/img/uml-use-case/include.svg" alt="Gestrichelter Pfeil mit Stereotyp include von Anwendungsfall A nach B" width="300">

Include-Beziehungen im Anwendungsfalldiagramm, wobei Anwendungsfall A den Anwendungsfall B beinhaltet

##### Extend-Beziehung

<img src="../../assets/img/uml-use-case/extend.svg" alt="Gestrichelter Pfeil mit Stereotyp extend von Anwendungsfall A nach B" width="300">

Extend-Beziehung im Anwendungsfalldiagramm, wobei Anwendungsfall A den Anwendungsfall B erweitert.

##### Extend-Beziehung mit extension point

<img src="../../assets/img/uml-use-case/extend-condition.svg" alt="Extend-Beziehung mit Bedingung am extension point" width="300">

Extend-Beziehung mit extension point, wobei Anwendungsfall A den Anwendungsfall B unter der angegebenen Bedingung erweitert.

##### Anwendungsfall mit extension point

<img src="../../assets/img/uml-use-case/use-case-detail.svg" alt="Anwendungsfall mit eingetragenem extension point" width="150">

Anwendungsfall mit extension point.

[^1]: <https://de.wikipedia.org/wiki/Anwendungsfalldiagramm>
