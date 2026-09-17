# Canonical Histogram Text Overview

Preserve complete Histogram titles and legend labels in the canonical PNG.
Coordinate package-side title wrapping with Shiny-side export-boundary
expansion; the PNG may extend beyond the configured figure canvas.

## Project Context

- Repositories: `SCSAWorkflow` (title wrapping) and `SPAC_Shiny` (PNG export).
- Package branch: `fix/canonical-histogram-text-spac`.
- Shiny branch: `fix/canonical-histogram-text-shiny`.
- Target branch: `dev` in each repository.
- Governing plan: [PR 4](../../plans/pr-plans/1-features-facet-pr-plan.md#pr-4-contain-canonical-histogram-text).
- Inherited work: [Features template delegation Task 8](../../ref/features-server-template/development-details/task-details.md#task-8-contain-histogram-template-text-within-its-canvas)
- Consumer follow-up: pin the merged package commit in a separate SPAC Shiny
  dependency update; that update is outside this development.

## Immediate Next Step

Begin Task 2: test the proposed expanded PNG boundary with the existing
Shiny serializer and representative template figures. Use the results to
guide Task 3's export fix. Task 1's package title wrapping is a separate
implementation.

## Progress

**In Progress**
- None currently.

**Planned**
- Task 1: Wrap Histogram Template Titles.
- Task 2: Test Expanded PNG Export Boundaries.
- Task 3: Expand Canonical PNG Export in SPAC Shiny.

**Complete**
- Development tracker created.

**Postponed**
- None currently.

**Dropped**
- None currently.

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
- [Features facet PR plan](../../plans/pr-plans/1-features-facet-pr-plan.md)
