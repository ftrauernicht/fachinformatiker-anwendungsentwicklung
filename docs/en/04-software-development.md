# Software development

## Table of contents

- [Web Development](#web-development)
  - [Markup Languages](#markup-languages)
    - [HTML - Hypertext Markup Language](#html---hypertext-markup-language)
      - [DOM - Document Object Model](#dom---document-object-model)
  - [Protocols](#protocols)
    - [HTTP/S](#https)
      - [HTTP-400](#http-400)
      - [HTTP-500](#http-500)
- [Object Orientation](#object-orientation)
  - [Interfaces](#interfaces)
    - [Declaration](#declaration)
    - [Example](#example)
    - [Naming Conventions](#naming-conventions)
  - [Abstraction](#abstraction)
    - [Programming Languages](#programming-languages)
    - [Abstraction in Object-Oriented Programming](#abstraction-in-object-oriented-programming)
- [Software quality](#software-quality)
- [Testing](#testing)
  - [Test levels](#test-levels)
  - [Black-box and white-box testing](#black-box-and-white-box-testing)
  - [Load and performance testing](#load-and-performance-testing)
  - [Test-driven development](#test-driven-development)
- [Architectural and design patterns](#architectural-and-design-patterns)
  - [Architectural patterns](#architectural-patterns)
  - [Design patterns](#design-patterns)
  - [Telling the two apart](#telling-the-two-apart)
- [Legal obligations for web applications](#legal-obligations-for-web-applications)
  - [Site notice under the Digital Services Act](#site-notice-under-the-digital-services-act)
  - [Accessibility under the Barrierefreiheitsstärkungsgesetz](#accessibility-under-the-barrierefreiheitsstärkungsgesetz)

## Web Development

### Markup Languages

#### HTML - Hypertext Markup Language

[^3]
HTML is a text-based markup language for structuring electronic documents such as texts with hyperlinks, images, and other content. HTML documents are the foundation of the World Wide Web (WWW) and are displayed by web browsers.

Contrary to some people's claims, HTML is **NOT** a programming language.
HTML cannot exhibit characteristics of a programming language like **variables** and **control structures**.

##### DOM - Document Object Model

[^4]
Document Object Model

- mainly HTML
- but can also be XML or XHTML
- The DOM represents a tree structure in which each element of the document is represented as a node in the tree.

### Protocols

#### HTTP/S

[^1] [^2]

- Hyper Text Transport Protocol
- Secure Hyper Text Transport Protocol

##### HTTP-400

HTTP Response Code 400 refers to client errors.

###### Types of HTTP-400

- 400 Bad Request
  - The server cannot or will not process the request due to an apparent client error (incorrect request, syntax incorrect, content too large, etc.).
- 403 Forbidden
  - The request contained data that was understood by the server but not processed (entry duplicate).
- 404 Not Found
  - The requested resource could not be found.

##### HTTP-500

HTTP Response Code 500 refers to server errors.

###### Types of HTTP-500

- 500 Internal Server Error
  - A generic error message given when an unexpected condition was encountered.
- 502 Bad Gateway
  - The server acted as a gateway or proxy and received an invalid response.
- 503 Service Unavailable
  - The server cannot handle the request (too many requests, down for maintenance).

## Object Orientation

### Interfaces

An interface in object-oriented programming defines which methods exist or must exist in different classes or similar.  
An interface specifies which methods exist or must exist.  
Interfaces provide a guarantee about the methods present in a class. They indicate that all objects possessing these interfaces can be treated equally.

In programming languages that do not support multiple inheritance like Java, interfaces can be used to define compatibilities between classes that do not inherit from each other.

#### Declaration

Other programming languages that support multiple inheritance, such as C++, know the concept of interfaces but treat them like ordinary classes. This is also called abstract classes. Sometimes, a separate language (a so-called Interface Description Language, IDL) is used to declare the interface - this is often the case with middleware systems like CORBA or DCOM. Object-based languages without strict typing usually do not have interfaces.

#### Example

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
            points[i] = new PointF((float)(cosine * (point.X - x) - sine * (point.Y - y) + x), (float)(sine * (point.X - x) + cosine * (point.Y - y) + y));
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

#### Naming Conventions

In some programming languages, it is customary to make interfaces recognizable by special prefixes or suffixes. For example, an "I" or "IF" is often appended.
In the example above, this would be an "I" for "IFace", which is typically applied in C#.

### Abstraction

[^6]
The term abstraction is frequently used in computer science and describes the separation between **concept** and **implementation**.

#### Programming Languages

Different programming languages offer different ways of abstraction, such as:

- In object-oriented languages like C++, Object Pascal, or Java, the concept of abstraction has been implemented in the form of a separate declarative statement. After such a declaration, it is the programmer's task to implement a class to create an instance of an object from it.

#### Abstraction in Object-Oriented Programming

- Needs elaboration

## Software quality

In an examination, quality is not a feeling but a list. The reference is the product quality model of the ISO/IEC 25010 series, which names eight characteristics and breaks each of them down into sub-characteristics.[^7]

| Characteristic | The question behind it | Example of a violation |
|---|---|---|
| **Functional suitability** | Does the software do what it is supposed to — completely and correctly? | The invoice total is rounded incorrectly |
| **Performance efficiency** | How much time and how many resources does it need for that? | The search answers only after twelve seconds |
| **Compatibility** | Does it work alongside other systems without disturbing them? | The export writes a file no other application can read |
| **Usability** | Can the intended users cope with it? | The cancel button saves |
| **Reliability** | Does it stay stable over time and recover from faults? | After three days without a restart the service stalls |
| **Security** | Are data and functions protected against unauthorised access? | Someone else's customer number in the address bar shows their data |
| **Maintainability** | How expensive is a change? | A new tax class needs edits in nineteen places |
| **Portability** | Can it be moved to a different environment? | The application only runs against this exact database version |

The 2023 revision reworked the model: usability is now interaction capability, portability is now flexibility, and safety has been added as a ninth characteristic — the question of whether the system can endanger people, property or the environment.[^7] Textbooks and examination tasks still mostly use the eight-characteristic model.

Two terms that German merges into one word and that are regularly confused: **security** protects the system from its environment, **safety** protects the environment from the system.

## Testing

### Test levels

The test levels build on each other, and each belongs to a level of the specification. That is the core of the V-model: specification on the left, the matching test on the right.[^8]

| Level | Object under test | Basis | Who tests |
|---|---|---|---|
| **Component test** (unit test) | a single class or method, in isolation | detailed technical design | development |
| **Integration test** | the interplay of several components, including database and interfaces | architecture, high-level design | development |
| **System test** | the complete system in a production-like environment | functional specification | test or quality assurance |
| **Acceptance test** | whether the system meets the client's requirements | requirement specification, contract | client |

The later a defect surfaces, the more expensive it is to remove — roughly by a factor of ten per level. That, and not the number in the coverage report, is the real argument for automated component tests.

### Black-box and white-box testing

**Black box** means testing against the specification without knowing the source code. Feed input in, compare the output. The usual techniques are equivalence partitioning and boundary value analysis.

**White box** means the source code is known and the test goes against its structure. The measure is coverage — statement, branch or path coverage.

Boundary value analysis is the standard technique for this: for a permitted quantity of 1 to 100, the values checked are 0, 1, 100 and 101, not 50. Defects sit at the edges, because that is where the comparison operators are.

### Load and performance testing

These tests do not measure *whether* something works but *how well* it works under load.[^9]

| Kind of test | The question behind it |
|---|---|
| **Load test** | Does the system cope with the expected load, say 500 concurrent users? |
| **Stress test** | Where is the limit, and what happens when it is exceeded? |
| **Soak test** | Does it still run after 48 hours, or does memory use keep growing? |
| **Scalability test** | Does twice the hardware also deliver twice the throughput? |

What is measured is response time, throughput and error rate. A load test without target values agreed beforehand produces numbers but no result.

### Test-driven development

In test-driven development the test is written before the code. The cycle is called red-green-refactor:[^10]

1. **Red** — write a test for the wanted behaviour. It fails, because the function does not exist yet.
2. **Green** — write just enough code to make the test pass. No more.
3. **Refactor** — tidy the code without changing its behaviour. The test just written keeps that safe.

The benefit lies less in coverage than in design: writing the call first makes an awkward interface obvious immediately.

## Architectural and design patterns

Both are reusable solutions to recurring problems. They differ in altitude: an architectural pattern organises the system as a whole, a design pattern solves a problem within a handful of classes.

### Architectural patterns

Architectural patterns determine which building blocks a system consists of and how they talk to each other.[^11]

| Pattern | Idea | Typical use |
|---|---|---|
| **Layered architecture** | presentation, business logic and data storage separated; each layer knows only the one below | the default for business applications |
| **Model view controller** | data model, presentation and control separated | user interfaces, especially on the web |
| **Client-server** | one service, many requesters | almost every networked application |
| **Microservices** | services cut along business capabilities, deployable independently | large systems with many teams |
| **Event-driven architecture** | components react to events instead of calling each other directly | processing chains, loose coupling |

### Design patterns

The classic categorisation comes from the book by the so-called Gang of Four and knows three groups:[^12]

| Group | Purpose | Examples |
|---|---|---|
| **Creational patterns** | how objects come into being | singleton, factory method, builder |
| **Structural patterns** | how objects are composed | adapter, decorator, facade, composite |
| **Behavioural patterns** | how objects cooperate | observer, strategy, command, iterator |

Three of them turn up in tasks particularly often:

- **Singleton** guarantees that a class has exactly one instance — a configuration, for example. The private constructor is the giveaway.
- **Observer** notifies registered objects about a change of state without knowing them individually. The basis of every event mechanism.
- **Strategy** wraps interchangeable algorithms behind a common interface, for example several ways of calculating shipping costs.

### Telling the two apart

A pattern is neither a library nor finished code but a description. Name, purpose and an example are therefore enough to place one; the full class diagram is only needed when implementing it.

## Legal obligations for web applications

Three obligations apply to practically every publicly reachable application, and all three have changed since 2023.

### Site notice under the Digital Services Act

The German Telemedia Act no longer exists. Since 14 May 2024 the obligation to publish a site notice sits in § 5 of the Digitale-Dienste-Gesetz; nothing changed in substance, only the term "telemedia" was replaced by "digital services".[^13] An application that still prints "§ 5 TMG" cites a repealed provision.

The same legislative package renamed the TTDSG to TDDDG. Consent for cookies and comparable access to a terminal device is still governed by its § 25.[^14]

### Accessibility under the Barrierefreiheitsstärkungsgesetz

The German Accessibility Strengthening Act has applied since 28 June 2025. Among others, it obliges providers of services in electronic commerce — online shops, booking flows, apps — to make their offering accessible, provided it addresses consumers.[^15]

Micro-enterprises with fewer than ten employees and at most two million euros of annual turnover are exempt, but only for services, not for products.

The technical yardstick is the European standard EN 301 549, which for web content refers to WCAG 2.1 at level AA. Its four principles:[^16]

| Principle | Meaning | Example of a measure |
|---|---|---|
| **Perceivable** | content must be graspable through at least one sense | alternative texts for images, sufficient contrast |
| **Operable** | everything must be reachable without a mouse as well | full keyboard operation, visible focus |
| **Understandable** | language and behaviour must be comprehensible | error messages in plain words, no unexpected change of context |
| **Robust** | assistive technology must be able to interpret the content | valid HTML, meaningful semantics instead of meaningless nesting |

For application developers this is the change with the most immediate consequences for their own code. Alternative texts, form field labels, focus order and contrast values are not decided in a legal department — they come into being while the interface is written.

[^1]: <https://de.wikipedia.org/wiki/HTTP-Statuscode>
[^2]: <https://de.wikipedia.org/wiki/Hypertext_Transfer_Protocol>
[^3]: <https://de.wikipedia.org/wiki/Hypertext_Markup_Language>
[^4]: <https://de.wikipedia.org/wiki/Document_Object_Model>
[^6]: <https://de.wikipedia.org/wiki/Abstraktion_(Informatik)>
[^7]: <https://quality.arc42.org/standards/iso-25010>
[^8]: <https://en.wikipedia.org/wiki/V-model_(software_development)>
[^9]: <https://en.wikipedia.org/wiki/Load_testing>
[^10]: <https://en.wikipedia.org/wiki/Test-driven_development>
[^11]: <https://en.wikipedia.org/wiki/Architectural_pattern>
[^12]: <https://en.wikipedia.org/wiki/Software_design_pattern>
[^13]: <https://www.gesetze-im-internet.de/ddg/__5.html>
[^14]: <https://www.gesetze-im-internet.de/ttdsg/__25.html>
[^15]: <https://www.gesetze-im-internet.de/bfsg/>
[^16]: <https://www.w3.org/TR/WCAG21/>
