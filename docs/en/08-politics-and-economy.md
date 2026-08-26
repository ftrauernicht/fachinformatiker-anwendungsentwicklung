# Politics and economy

## Table of contents

- [Work and Business Processes](#work-and-business-processes)
  - [Company Goals/Interests](#company-goalsinterests)
  - [Contracts](#contracts)
- [Amortization](#amortization)
  - [How are Development Costs Composed?](#how-are-development-costs-composed)
- [Legal forms of a company](#legal-forms-of-a-company)
  - [What changed in 2024](#what-changed-in-2024)
- [Market structures](#market-structures)
- [Electronic invoicing](#electronic-invoicing)

## Work and Business Processes

### Company Goals/Interests

- Ecological Goal
- Economic Goal
- Mission/Vision
- Social Goal

### Contracts

- Work Contract
- Service Contract
- Purchase Contract
- Lease Contract
- Loan Contract

## Amortization

### How are Development Costs Composed?

- Development costs consist of salaries, etc., of the employees and overhead costs.
- Overhead costs include everything a employee needs to work and more. These include:
  - Work materials
    - Computer
    - Chair
    - Desk
    - etc.
  - Electricity costs
  - Heating/Cooling costs
  - Coffee
  - Food
  - etc.

## Legal forms of a company

The choice of legal form decides three things: who is liable for debts, how much capital has to be contributed, and which formalities apply to founding and bookkeeping. The forms below are the German ones asked about in the examination.[^1]

| Legal form | Members | Liability | Minimum capital | Register |
|---|---|---|---|---|
| **Sole proprietorship** | 1 | unlimited, including private assets | none | commercial register A, if a merchant |
| **GbR** (civil law partnership) | from 2 | unlimited and joint and several | none | voluntary, in the partnership register |
| **OHG** (general partnership) | from 2 | unlimited and joint and several | none | commercial register A |
| **KG** (limited partnership) | from 2 | general partner unlimited, limited partner only up to their contribution | none | commercial register A |
| **GmbH** (limited company) | from 1 | limited to the company's assets | €25,000, at least €12,500 paid in | commercial register B |
| **UG** (entrepreneurial company) | from 1 | limited to the company's assets | from €1 | commercial register B |
| **AG** (stock corporation) | from 1 | limited to the company's assets | €50,000 | commercial register B |

The fundamental distinction runs between **partnerships** and **corporations**. In partnerships — GbR, OHG, KG — the members are personally liable and run the business themselves; in exchange, founding one is informal and cheap. Corporations — GmbH, UG, AG — are legal persons in their own right; liability ends at the company's assets, but capital, a notary and proper bookkeeping are required.

The UG is not a legal form of its own but a GmbH with a smaller starting capital. It has to retain a quarter of its annual profit as a reserve until it reaches the share capital of a GmbH.

### What changed in 2024

On 1 January 2024 the act modernising German partnership law came into force — without a transition period and for existing partnerships as well.[^2]

Two points from it matter in practice:

- The **legal capacity of the GbR** is now written into the law. It can enter into contracts, hold property and sue in its own name; until then this followed only from case law.
- There is a **partnership register**. A GbR that registers carries the suffix **eGbR**. Registration is voluntary in principle but becomes a practical necessity as soon as the partnership wants to acquire land or shares — without it, nothing changes in the land register.

## Market structures

Which market structure applies follows from the number of suppliers and the number of buyers.[^3]

| Buyers ↓ / Suppliers → | one | few | many |
|---|---|---|---|
| **one** | bilateral monopoly | limited monopsony | monopsony |
| **few** | limited monopoly | bilateral oligopoly | oligopsony |
| **many** | monopoly | oligopoly | polypoly |

The three cases usually asked about:

- **Monopoly** — one supplier, many buyers. The supplier sets the price; without regulation there is no ceiling other than willingness to pay.
- **Oligopoly** — few suppliers, many buyers. Each supplier has to factor in the reaction of the others, which leads either to rigid prices or to price wars.
- **Polypoly** — many on both sides. The individual supplier has no influence on the price and can only accept it.

## Electronic invoicing

Since 1 January 2025 electronic invoicing has been mandatory in Germany for business between domestic companies.[^4]

An electronic invoice in the sense of the law is **not** just any digital document. It has to be issued in a structured electronic format, be processable automatically, and comply with the European standard EN 16931. A PDF attached to an email does not meet that — since 2025 it counts as an "other invoice".

| Format | Structure |
|---|---|
| **XRechnung** | plain XML, known from public procurement |
| **ZUGFeRD from 2.x** | hybrid: a PDF with the XML data embedded — readable by people and processable by machines |

The deadlines are staggered:[^5]

| From | What applies |
|---|---|
| 1 January 2025 | **Every** company has to be able to receive and process electronic invoices. An email address suffices legally. |
| 1 January 2027 | duty to issue for companies with more than €800,000 turnover in the previous year |
| 1 January 2028 | duty to issue for everyone else |

For application developers this is not an administrative matter: anyone maintaining an ERP system or a shop has to switch its output to a structured format and store the invoices in an audit-proof way.

[^1]: <https://de.wikipedia.org/wiki/Rechtsform>
[^2]: <https://www.ihk-muenchen.de/de/Service/Recht-und-Steuern/Gesellschaftsrecht/GbR-gruenden-so-funktioniert-die-Gruendung-IHK/modernisierung-der-gbr-mopeg/>
[^3]: <https://en.wikipedia.org/wiki/Market_structure>
[^4]: <https://www.gesetze-im-internet.de/ustg_1980/__14.html>
[^5]: <https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html>
