# Features UI Structure Refactor Overview

Reorganize the existing SPAC Shiny Features UI using the modular,
section-based pattern from the template integration guide while preserving
the current controls and behavior. This creates a focused UI foundation for
the later facet development.

## Project Context

- Repository: `SPAC_Shiny`
- Feature branch: `ref/features-ui-structure`
- Pull request: [#87](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/87), open
  and rebased onto `dev` after PR #86 as of 2026-09-16
- Development base: `dev` at `5a3cf25` (includes merged PR #86)
- PR target: `dev`
- Primary reference: [SPAC template integration guide](../../../issues/issue-73.md)
- Follow-up development: [Features facet UI](../../feat/features-facet/overview.md)

## Immediate Next Step

Address review feedback and merge PR #87 after approval.

## Progress

**In Progress**
- None currently.

**Complete**
- Development tracker created and UI structure agreed.
- Task 1: Extract the Features UI Composition.
- Task 2: Organize the Features Controls Into Sections.
- Task 4: Replace Dynamic Group By UI With Static Conditions.
- Task 3: Verify the UI Refactor and Prepare It for Review.
- Rebased and pushed the reviewed branch onto `dev` at `efc514b`.

**Remaining**
- None currently.

**Postponed**
- Task 5: Establish Shared Visualization Styling for Features. Moved to the
  cross-tab work in the [development roadmap](../../plans/development-roadmap.md#step-7-extend-template-adoption-across-spac-shiny).

**Dropped**
- None currently.

**Issues (open)**
- None currently.

## Scope Boundary

Center the refactor in `ui/features_ui.py`. Task 4 permits focused changes to
`features_server.py` and `effect_update_server.py` for static Group By
controls.

Preserve all functional input and output IDs, defaults, analytical server
behavior, and the merged adapter's `output_image` renderer contract. Do not
add facet controls, template parameters, responsive preview work, renderer
changes, dependencies, unrelated cross-tab migrations, or unrelated visual
polish.

## Development Details

- [Task details](./development-details/task-details.md)
- [Architecture](./development-details/architecture.md)
- [Decisions](./development-details/decisions.md)
- [Implementation log](./development-details/implementation-log.md)
- [Implementation notes](./development-details/implementation-notes.md)
- [PR summary](./pr-summary.md)
- [Features facet plan](../../plans/pr-plans/1-features-facet-pr-plan.md)
- [Development roadmap](../../plans/development-roadmap.md)
