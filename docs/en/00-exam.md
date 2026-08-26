# The final examination at a glance

What gets examined is fixed in two places. The framework — which examination areas exist, how long they take, how much they count — is laid down in the German training regulation for IT specialists and is therefore binding law. The subject matter is defined in the examination catalogues issued by the chambers of commerce; those are revised regularly, most recently for the examinations from 2025 onwards.

This page records both, and names the state this collection is written against.

## Table of contents

- [Two parts, one grade](#two-parts-one-grade)
- [When the examination is passed](#when-the-examination-is-passed)
- [What gets examined: the examination catalogues](#what-gets-examined-the-examination-catalogues)
  - [Where the statements about the catalogue come from](#where-the-statements-about-the-catalogue-come-from)
  - [What that walkthrough reports as changed](#what-that-walkthrough-reports-as-changed)
- [What this collection covers](#what-this-collection-covers)
- [The state of this collection](#the-state-of-this-collection)

## Two parts, one grade

The apprenticeship ends with a *split* final examination. Part 1 is written after roughly half of the training period and already counts towards the final grade — there is no separate interim examination.[^1]

| Examination area | Part | Form | Duration | Weight |
|---|---|---|---|---|
| Setting up an IT-supported workplace | 1 | written | 90 minutes | 20 % |
| Planning and implementing a software project | 2 | project work with documentation, plus presentation and technical discussion | at most 80 hours, plus at most 30 minutes | 50 % |
| Planning a software product | 2 | written | 90 minutes | 10 % |
| Developing and implementing algorithms | 2 | written | 90 minutes | 10 % |
| Economics and social studies | 2 | written | 60 minutes | 10 % |

Within the project area, the written half — carrying out the project and documenting it — and the oral half of presentation and technical discussion count equally. The presentation may take at most 15 of the 30 minutes.[^2]

The arithmetic adds up: 20 + 50 + 10 + 10 + 10 = 100. Anyone wondering where study time pays off best has the answer in the right-hand column. The three written areas of Part 2 together make up 30 per cent, the project alone 50.

## When the examination is passed

Four conditions must hold at the same time:[^3]

1. The combined result of Part 1 and Part 2 is at least "sufficient".
2. The result of Part 2 on its own is at least "sufficient".
3. At least three of the five examination areas in Part 2 are at least "sufficient".
4. No examination area in Part 2 is graded "insufficient".

Two consequences that are regularly overlooked: an excellent Part 1 cannot rescue a failed Part 2, because Part 2 has to pass on its own. And a single failing grade in one of the 10-per-cent areas sinks the whole examination, however good the rest is.

## What gets examined: the examination catalogues

The regulation describes the examination areas in a few sentences only. Which subject matter sits behind them is set by the examination catalogues of the chambers of commerce. They are identical across all German chambers, contain no sample tasks themselves, and are sold through U-Form Verlag.[^4]

**The authoritative version is the 2nd revised edition.** It is the basis for Part 1 in spring 2025 and Part 2 in summer 2025 for the first time. The chamber gives two reasons: feedback from the examination dates since the first edition of 2021, and technical developments. It also separates Part 1 and Part 2 more sharply — SQL and RAID are now examined exclusively in Part 2.[^5]

### Where the statements about the catalogue come from

The following section is the only one in this collection that says anything about the **contents** of the examination catalogue. What it rests on is therefore stated openly here.

| | |
|---|---|
| Evidenced by the chamber | that a 2nd edition exists, from when it applies, and that SQL and RAID now appear in Part 2 only[^5] |
| Evidenced by the training regulation | examination areas, weighting, durations, pass rule[^1] [^2] [^3] |
| **Not** from the catalogue itself | the list of individual topics below. It comes from a public walkthrough of the catalogue on the IT-Berufe podcast[^6] |

The catalogue is protected material of the chambers' examination bodies; it is neither quoted nor reproduced here, only named by topic. Anyone who has to rely on it should obtain it from U-Form Verlag — it costs around seven euros — or ask their own chamber of commerce. **This collection has not been reconciled against the original.**

### What that walkthrough reports as changed

Reportedly added for the application development specialisation, among others: load and performance testing, test-driven development, software quality characteristics, architectural patterns, monitoring, Kerberos, ODBC, cyber-physical systems, the elementary sorting algorithms, and man-in-the-middle attacks, SQL injection and DDoS by name.[^6]

Reportedly removed: **flowcharts and Nassi-Shneiderman diagrams**; control structures are said to be asked for in pseudocode or as an activity diagram instead.[^6]

That is the most consequential statement in this collection, because it shapes what someone practises. It rests on two episodes of the same podcast and fits the chamber's announcement that room was made for the transition to newer methods such as UML[^5] — which does not make it proven.

The regulation itself still requires in § 14 that algorithms be "transferred into program logic and represented graphically".[^7] What would have changed is therefore not the requirement but the notation expected for it. Both notations stay in this collection — as groundwork and for vocational school — but carry a note.

## What this collection covers

It covers the two written subject areas of Part 2, plus economics and social studies in outline:

| Examination area | Chapter here |
|---|---|
| Planning a software product | [Software development](04-software-development.md), [Databases](03-databases.md), [Diagrams](diagrams/index.md) |
| Developing and implementing algorithms | [Algorithms](10-algorithms.md), [Databases](03-databases.md), [Diagrams](diagrams/index.md) |
| Economics and social studies | [Politics and economy](08-politics-and-economy.md), [Project management](07-project-management.md) |

Not covered is the project work — the area carrying 50 per cent. How a project proposal is worded, what belongs in the documentation and how a presentation should be built depends too much on the responsible chamber and on the training company to describe usefully in general terms. Ask there for the requirements and for examples from earlier cohorts.

Part 1 is not covered either. The collection is cut for Part 2; the network technology chapter does overlap with it to a large extent, though.

## The state of this collection

| | State |
|---|---|
| Examination catalogue | 2nd edition, valid from Part 1 spring 2025 and Part 2 summer 2025 |
| Legal state | August 2026 |

Both go out of date, and they do so without warning. Once a year a workflow in this repository opens an issue asking for both lines to be checked — which is no substitute for asking your own chamber of commerce when in doubt.

Which legal changes have been worked in since the 2023 version is stated in the respective chapters with a date and a source: the German Accessibility Strengthening Act and the electronic invoicing obligation, the replacement of the Telemedia Act by the Digital Services Act, the NIS 2 implementation act, the EU AI Act and the modernisation of partnership law.

[^1]: <https://www.gesetze-im-internet.de/fiausbv/__7.html>
[^2]: <https://www.gesetze-im-internet.de/fiausbv/__12.html>
[^3]: <https://www.gesetze-im-internet.de/fiausbv/__16.html>
[^4]: <https://www.u-form-shop.de/ihk-pruefungen/pruefungskataloge-abschlusspruefung/fachinformatiker-fachinformatikerin-anwendungsentwicklung-pruefungskatalog-fuer-die-ihk-abschlusspruefung-1>
[^5]: <https://www.ihk.de/hannover/hauptnavigation/ausbildung-und-weiterbildung/ausbildung/ausbildung-a-z/neuordnungen/pruefungskataloge-it-berufe-6438900>
[^6]: <https://it-berufe-podcast.de/neuer-pruefungskatalog-fuer-die-ap2-als-fachinformatiker-anwendungsentwicklung-ab-2025-it-berufe-podcast-191/>
[^7]: <https://www.gesetze-im-internet.de/fiausbv/__14.html>
