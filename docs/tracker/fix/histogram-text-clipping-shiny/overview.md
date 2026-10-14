# Histogram Text Clipping Overview

Keep Histogram titles and legends readable and complete in the generated
PNG. Fix export clipping in Shiny and improve the identified long title in
the package; the PNG may expand beyond the original canvas.

## Project Context

- Repositories: `SCSAWorkflow` (title wrapping) and `SPAC_Shiny` (PNG export).
- Package branch: `fix/histogram-text-clipping-spac`.
- Shiny branch: `fix/histogram-text-clipping-shiny`.
- Target branch: `dev` in each repository.
- Governing plan: [PR 4](../../../plans/pr-plans/1-features-facet-pr-plan.md#pr-4-fix-histogram-text-clipping).
- Inherited work: [Features template delegation Task 8](../../ref/features-server-template/development-details/task-details.md#task-8-contain-histogram-template-text-within-its-canvas)
- Consumer follow-up: pin the merged package commit in a separate SPAC Shiny
  dependency update; that update is outside this development and is required
  to deliver the package title improvement to Shiny users.

## Immediate Next Step

Continue Task 2. Preserve Complete Histogram PNG Output.

## Progress

**In Progress**
- Task 2. Preserve Complete Histogram PNG Output.

**Planned**
- Task 1. Wrap Histogram Template Titles.

**Complete**
- Development tracker created.

**Postponed**
- None currently.

**Dropped**
- Task 3. Expand Canonical PNG Export in SPAC Shiny.

## Scope Boundary

This development covers title wording in the package and complete PNG export
in Shiny. UI parameter controls and responsive preview work remain separate.
The linked task details and implementation notes own the actions and rules.

## Development Details

- [Task details](./development-details/task-details.md)
- [Architecture](./development-details/architecture.md)
- [Decisions](./development-details/decisions.md)
- [Implementation log](./development-details/implementation-log.md)
- [Implementation notes](./development-details/implementation-notes.md)
- [Features facet PR plan](../../../plans/pr-plans/1-features-facet-pr-plan.md)
