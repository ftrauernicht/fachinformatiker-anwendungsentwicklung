# Use case diagram

## Table of contents

- [Keywords](#keywords)
- [Elements](#elements)
  - [System Context](#system-context)
  - [Actor](#actor)
  - [Use Case](#use-case)
  - [Relationships](#relationships)
    - [Association/Communication](#associationcommunication)
    - [Multiplicity](#multiplicity)
    - [Generalization of Use Cases](#generalization-of-use-cases)
    - [Generalization of Actors](#generalization-of-actors)
    - [Include Relationship](#include-relationship)
    - [Extend Relationship](#extend-relationship)
    - [Extend Relationship with Extension Point](#extend-relationship-with-extension-point)
    - [Use case with an extension point](#use-case-with-an-extension-point)

### Keywords

- **Objective**: To show as simply as possible what one wants to do with the software system to be built, i.e., which application cases exist.
- **Actors**: Represented as "stick figures," which can represent both people like customers or administrators and a system.
- **Use Cases**: Represented in ellipses. They must be described (e.g., in a comment or a separate file).
- **Associations**: Between actors and use cases must be marked by lines.
- **System Boundaries**: Marked by rectangles.
- **Include Relationship**: From the calling use case to the included use case, represented by a dashed arrow with the stereotype `<<include>>`.
- **Extend Relationship**: From the extending use case to the calling use case, represented by a dashed arrow with the stereotype `<<extend>>`. The extending use case can, but does not have to, be activated.

### Elements

#### System Context

<img src="../../assets/img/uml-use-case/system-context.svg" alt="System boundary drawn as a rectangle around two use cases" width="200px">

The system context is marked by system boundaries in the form of rectangles.

#### Actor

<img src="../../assets/img/uml-use-case/actor.svg" alt="Actor drawn as a stick figure" width="120px">

Actors are represented as "stick figures," which can represent both people like customers or administrators and a system.

#### Use Case

<img src="../../assets/img/uml-use-case/use-case.svg" alt="Use case drawn as a labelled ellipse" width="200px">

Use cases are represented in ellipses. They must be described (e.g., in a comment or a separate file).

#### Relationships

##### Association/Communication

<img src="../../assets/img/uml-use-case/association.svg" alt="Line connecting an actor and a use case" width="300px">

Association/Communication between actor and use case.

##### Multiplicity

<img src="../../assets/img/uml-use-case/multiplicity.svg" alt="Association annotated with multiplicities at both ends" width="300">

Multiplicity between actor and use case, where the default of the actor is 1.

##### Generalization of Use Cases

<img src="../../assets/img/uml-use-case/generalisation.svg" alt="Generalisation arrow between two use cases" width="300">

##### Generalization of Actors

<img src="../../assets/img/uml-use-case/generalisation-actor.svg" alt="Generalisation arrow between two actors" width="300">

##### Include Relationship

<img src="../../assets/img/uml-use-case/include.svg" alt="Dashed arrow stereotyped include, pointing from use case A to B" width="300">

Include relationships in the use-case diagram, where use case A includes use case B.

##### Extend Relationship

<img src="../../assets/img/uml-use-case/extend.svg" alt="Dashed arrow stereotyped extend, pointing from use case A to B" width="300">

Extend relationships in the use-case diagram, where use case A extends use case B.

##### Extend Relationship with Extension Point

<img src="../../assets/img/uml-use-case/extend-condition.svg" alt="Extend relationship with a condition at the extension point" width="300">

Extend relationship with extension point, where use case A extends use case B under the specified condition.

##### Use case with an extension point

<img src="../../assets/img/uml-use-case/use-case-detail.svg" alt="Use case with an extension point listed inside" width="150">

Use case with extension point.
