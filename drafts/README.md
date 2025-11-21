# 📄 Draft Dictionary Items
This folder contains draft entries for semantic dictionary concepts aka **data types**, written in Markdown format with metadata in front matter. Each file includes:

- YAML frontmatter for metadata (e.g. label, definition, language, status)
- Rich content like text, code, and image references

**List of working data types definitions** in sin preview folder in [INDEX](./INDEX.md)

## 🧱 File Structure

Each file must:
- Use .md extension
- Start with a YAML metadata block (between --- lines)
- Include a human-readable definition and optional commentary, diagrams, or citations

### 🧾 Metadata Fields

| Field | Description | 
| - | - | 
| id | Unique lowercase identifier for the concept (also used as filename) | 
| label | Human-friendly title | 
| definition | Concise explanation of the concept's meaning | 
| category | Domain or grouping the concept belongs to | 
| language | Language code of the definition (e.g. en) | 
| status | Approval state (draft, review, approved, etc.) | 
| source | Citable source or reference (standard, report, etc.) | 
| subcategory | **list of** sub grouping the concept belongs to |


### 🧾 Workflow

Drafts are manually edited and commented upon via GitHub issues.

**Workflow including statuses is in detail described in** [WORKFLOW](WORKFLOW.md).

Previews are auto-generated in each commit by `generate_preview.py` in the [PREVIEW](./preview/README.md) folder

Releases are auto-generated when committing a version tag by `generate_releease.py`. in the [RELEASE](../release/README.md)

## 🧠 Examples

Here’s an example draft file named: `road-classification.md`

```markdown
---
id: road-classification
label: road classification
definition: the minimum information required for distinguishing the links of a road network encompassing form of way, functional, or other concerns.
category: Types of data on infrastructure
language: en
status: accepted
source: DR_EU_2022-670
---

>According to ETSI TS 102 894-2 (DE=RoadType), road types are distinguished based on two parameters: (a) urban versus non-urban roads and (b) roads with versus without structural separation to opposite lanes.

>An extended **classification** is provided by the INSPIRE data specification on transport networks (based on EuroRoads and GDF specifications). This classification is based on: (a) ‘form of way’ that considers the physical properties of each road link (including accessible mobility modes) and (b) ‘functional class’ indicating the importance of each road link within the road network. It is important to note that the ‘form of way’ and ‘functional class’ elements may vary in meaning across different European countries due to the lack of harmonization.

![Figure](../..images/road-classification.png)

>NOTE: The classification of road links is an important aspect to be considered by navigation systems. For example, in certain contexts, main or first-class roads may preferably be used for long-distance traffic (e.g., international traffic), while the lower classes in this hierarchy may preferably be used for regional and local traffic.

>Reference/additional info: https://www.etsi.org/deliver/etsi_ts/102800_102899/10289402/01.03.01_60/ts_10289402v010301p.pdf; https://inspire.ec.europa.eu/id/document/tg/tn
```

Here’s an example draft file named: `road-network--physical-attributes_road-width.md`

```markdown
---
id: road-network--physical-attributes_road-width
label: road width
definition: the minimum information required for indicating the width of a road network’s links.
category: Types of data on infrastructure
language: en
status: accepted
source: DR_EU_2022-670
subcategory:
  - Road network links and their physical attributes
---

>This information is addressed as encompassing in a discretized and systematic manner the width of various (maintained) components of the road surface, including driving lanes, hard shoulders, medians, parking space, and the roadside.

> NOTE: Driving lanes, according to ETSI TS 102 894-2, are counted from the inside border of the road excluding the hard shoulder.

> Reference/additional info: https://www.etsi.org/deliver/etsi_ts/102800_102899/10289402/01.03.01_60/ts_10289402v010301p.pdf 

> Despite the fact that traffic capacity is the main concern of various RTTI-related use cases, lateral clearance constitutes a contextual factor for determining free-flow speed and, in turn, traffic capacity.
```

This structure allows automated parsing of metadata while retaining rich, readable content for users and editors alike.
