# Features Server Template Refactor Overview

Refactor the SPAC Shiny Features tab to use the standard SPAC template
workflow while preserving its current behavior. This provides the foundation
for later facet support and agent-driven UI updates.

## Project Context

- Repository: `SPAC_Shiny`
- Feature branch: `ref/features-server-template`
- Target branch: `dev`
- Dependency prerequisite: `chore/pin-spac-to-pr-433` (merged into `dev` via PR #85 at `b9f63d2`)
- Primary reference: [SPAC template integration guide](../../../../issues/issue-73.md)
- Related examples: [PR #75](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/75), [PR #80](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/80), and [Mousumi's draft PR #81](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/81)

## Immediate Next Step

Mark draft PR #86 ready for mentor review, request review, and address only
feedback within the established template-delegation boundary. Merge the PR
after approval, close this development tracker, and begin PR 2 from the
[Features facet plan](../../plans/features-facet-pr-plan.md) as a separate
development.

## Progress

**In Progress**
- None currently.

**Complete**
- Task 10: Resolve the Canonical PNG Renderer Boundary.
- Task 6: Preserve and Verify Reactive UI Behavior.
- Task 5: Delegate Histogram Execution to the Template.
- Task 4: Build the SPAC Template Parameter Dictionary.
- Task 2: Extract the Features Input Snapshot.
- Task 1: Use the Canonical AnnData Source.

**Reassigned tasks**
- Task 3: Add the Agent-to-UI Parameter Registry. This is now part of Agent
  PR C after facet exposure; see the
  [development roadmap](../../plans/development-roadmap.md#agent-pr-c-features-ui-update-and-render).
- Task 8: Contain Histogram Template Text Within Its Canvas. This is now PR 3
  in the [Features facet plan](../../plans/features-facet-pr-plan.md#pr-3-contain-canonical-histogram-text).
- Task 9: Make the Histogram Preview Responsive. This is now PR 4 in the
  [Features facet plan](../../plans/features-facet-pr-plan.md#pr-4-make-the-histogram-preview-responsive).

**Postponed tasks**
- Task 7: Add Focused Adapter Tests. Defer comprehensive automated adapter
  verification to the specialized SWE stage.

**Dropped tasks**
- None currently.

**Issues (open)**
1. Long template-generated titles or legend labels can be clipped by the
   canonical PNG. The separate SCSAWorkflow PR 3 owns this issue; see the
   [Features facet plan](../../plans/features-facet-pr-plan.md#pr-3-contain-canonical-histogram-text).
2. Proportional preview fitting can leave available width unused. Task 9 owns
   this renderer-neutral browser-layout issue through separate SPAC Shiny
   PR 4; see the
   [Features facet plan](../../plans/features-facet-pr-plan.md#pr-4-make-the-histogram-preview-responsive).

**Issues (addressed)**
- Task 10 selected direct canonical-PNG delivery through `render.image` and
  was completed in `da242c6`.

## Scope Boundary

Keep the adapter boundary focused on canonical AnnData access, current
Features inputs, template payload construction, memory-registry execution,
canonical figure presentation, and dataframe return. Do not add facet UI,
new histogram controls, responsive layout, caching, downloads, cancellation,
or agent integration while PR #86 is under review. The canonical order and
ownership of that later work are defined by the Features facet plan and the
broader development roadmap.

## Development Details

- [Task details](./development-details/task-details.md)
- [Architecture](./development-details/architecture.md)
- [Decisions](./development-details/decisions.md)
- [Implementation log](./development-details/implementation-log.md)
- [Implementation notes](./development-details/implementation-notes.md)
- [Features facet PR plan](../../plans/features-facet-pr-plan.md)
- [Development roadmap](../../plans/development-roadmap.md)
- [Future work](../../plans/future-work.md)
