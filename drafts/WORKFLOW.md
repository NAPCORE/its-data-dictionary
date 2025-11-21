# 🛠️ Definition Processing Workflow

A structured workflow for capturing, enriching, reviewing, validating, and publishing ITS data definitions.

---

## 🔁 Status Labels & Transition Logic

| Status         | Description                                  | 
|----------------|----------------------------------------------|
| ![proposed](https://img.shields.io/badge/proposed-ffc107)     | Initial definition captured for enrichment, initial development is here   |
| ![ready for review](https://img.shields.io/badge/ready_for_review-673ab7) | staging status, after initial enrichment of the draft definition         |
| ![under review](https://img.shields.io/badge/under_review-2196f3) | Being peer-reviewed or expert-evaluated      |
| ![approved](https://img.shields.io/badge/approved-4caf50)     | Finalised concept definition 				|
| ![for thorough review](https://img.shields.io/badge/for_thorough_review-ff9800)    | No consensus reached, needs further developments               | 
| ![archived](https://img.shields.io/badge/archived-bdbdbd)     | Deprecated or replaced concept               | 


## Drafting the definition

### 📥 1. Initial Capture

- Source definitions from trusted materials.
- Assign status → ![proposed](https://img.shields.io/badge/proposed-ffc107).
- Create metadata fields:  
  `source`, `category`, `subcategory`, `id`, `definition`, `status`.

### 🔍 2. Refinement Tasks

- Reword for precision and clarity.
- Normalize terminology to domain standards.

### 📝 3. Explanatory Additions

- Provide background context.
- Include example usage and edge cases.
- Clarify assumptions or constraints.
- Add visual aids or code samples when helpful.

- Change status to → ![ready for review](https://img.shields.io/badge/ready_for_review-673ab7).

## 👥 3. Peer Review Workflow

- Change status to → ![under review](https://img.shields.io/badge/under_review-2196f3).
- Reviewers may suggest edits or approve.
- Resulting status becomes:
  - ![approved](https://img.shields.io/badge/approved-4caf50) if approved after all proposed changes
  - ![for thorough review](https://img.shields.io/badge/for_thorough_review-ff9800) if no consensus was reached in the review process and dictionary item needs further elaboration
  - ![archived](https://img.shields.io/badge/archived-bdbdbd) if the item is deprecated, by e.g. new definitions in updated laws

Track revisions via commit history or comments in issues.

## 🌍 4. Publishing & Discovery

- Release finalized definitions → `release/DR_*.md`
- Generate semantic vocab → `vocab/<DR>/<item>.ttl`
- Publish via GitHub Actions as versioned artifacts.

## 🔄 5. Change Management

- Any update starts from status → ![proposed](https://img.shields.io/badge/proposed-ffc107).
- From [for thorough review](https://img.shields.io/badge/for_thorough_review-ff9800), after further elaboration dictionary items go to ![ready for review].
- Retired concepts receive status → ![archived](https://img.shields.io/badge/archived-bdbdbd).
- Maintain changelog entries per definition.
- Track rollback versions via git history.

## 🌐 Visual Workflow

```mermaid
graph TD
  A[Proposed] --> B[Ready for Review]
  B --> C[Under the Review]
  C --> E[Approved]
  E --> F[Published]
  F --> G[Archived]
  C --> D[For Thorough Review]  
  D --> B
```
