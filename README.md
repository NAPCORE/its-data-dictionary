# NAPCORE ITS Data Dictionary 📚

![Version](https://img.shields.io/github/v/tag/NAPCORE/its-data-dictionary?label=version&style=flat-square)
![License](https://img.shields.io/github/license/NAPCORE/its-data-dictionary?style=flat-square)
![Last Commit](https://img.shields.io/github/last-commit/NAPCORE/its-data-dictionary?style=flat-square)
![Issues](https://img.shields.io/github/issues/NAPCORE/its-data-dictionary?style=flat-square)
![Build](https://github.com/NAPCORE/its-data-dictionary/actions/workflows/release.yml/badge.svg)
![Build](https://github.com/NAPCORE/its-data-dictionary/actions/workflows/preview.yml/badge.svg)

A structured dictionary of **transport-related concepts** defined in delegated regulations of the [ITS Directive](https://eur-lex.europa.eu/eli/dir/2010/40/oj/eng), managed in Markdown. Includes human-readable previews, releases and machine-readable RDF.
This repository serves for development and publishing of the data dictionary. 

## 🧭 Data Dictionary Index

Data Dictionary items are grouped by delegated regulation they appear in to the separate file. Available as stable **release** [here](./release/README.md) or draft development version [here](./release/preview/README.md)

| Abbreviation | Full Title & Regulation No.                          | 📂 Link                     |
|--------------|------------------------------------------------------|-----------------------------|
| 🛑 **SRTI**  | Safety-Related Traffic Information *(DR 886/2013)*   | [View Vocabulary →](./release/DR_EU_886-2013.md) |
| 🧭 **MMTIS** | Multimodal Travel Information Services *(DR 2024/490)* | [View Vocabulary →](./release/DR_EU_2024-490.md) |
| 🚙 **RTTI**  | Real-Time Traffic Information *(DR 2015/962)*        | [View Vocabulary →](./release/DR_EU_2015-962.md) |
| 🚙 **RTTI**  | Real-Time Traffic Information *(DR 2022/670)*        | [View Vocabulary →](./release/DR_EU_2022-670.md) |
| 🏁 **SSTP**  | Safe and Secure Truck Parking *(DR 885/2013)*       | [View Vocabulary →](./release/DR_EU_885-2013.md) |

NOTE: release could be also accessed as a downloadable artefact in releases GitHub functionality.

## 🛠 Content Creation

The work on **transport-related concepts** aka **data types** is done in the `drafts/` folder in the subfolder per delegated regulation. Each data type is a separate markdown document (fragment), with predefined attributes and "free" content. 

- [`drafts/README.md`](drafts/README.md) for the detailed instructions on drafting and content of data dictionary definitions. 
- [`drafts/INDEX.md`](drafts/INDEX.md) to view the statuses of all data dictionary items.
- [`drafts/WORKFLOW.md`](drafts/WORKFLOW.md) to view the process of updating the terms.
- [`drafts/preview/README.md`](drafts/preview/README.md) – review file of data types definitions, one per delegated regulation

## 🌍 Published Outputs

- 📦 Release Dictionaries:  [`release/README.md`](release/README.md)
- 🐢 RDF Vocabularies: [`vocab/`](vocab/)

## 📁 Repository Structure

- `drafts/`: Individual Markdown entries grouped by delegated regulation including Auto-generated index file and browsable pre-view files (one per DR)
- `release/`: Final published dictionary for each tagged version
- `vocab/`: RDF files (Turtle format) for each concept
- `scripts/`: Python automation for preview and release generation
- `images/`, `code/`: Optional media and supporting examples

## 🚀 Workflow Automation 

### 🔄 Preview auto-generation

Triggered automatically on each push to:

- `drafts/**`
- `code/**`
- `scripts/generate_preview.py`

Generates:

- [`drafts/INDEX.md`](drafts/INDEX.md) – an index file with links to individual data type file fragments with their statuses.
- `drafts/preview/DR_*.md` – review file of data types definitions, one per delegated regulation
- Commits updated previews back to the repository
- Uploads preview files as GitHub Actions artifact

### 🏁 Release auto-generation

Triggered automatically when a version tag is pushed (e.g. `v1.0.0`):

```bash
git tag v1.0.0
git push origin v1.0.0
```

Generates:

- `release/DR_*.md` – versioned release file of data types definitions, one per delegated regulation
- `vocab/<DR>/<item>.ttl` – SKOS-formatted RDF files from data types strict-definitions
- Uploads files as a downloadable GitHub Actions artifact


## 💬 License & Contributions

Open-source under the MIT License. Contributions are welcome—just submit a PR or open an issue.
