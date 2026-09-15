# Features UI Structure Refactor Overview

Reorganize the existing SPAC Shiny Features UI using the modular,
section-based pattern from the template integration guide while preserving
the current controls and behavior. This creates a focused UI foundation for
the later facet development.

## Project Context

- Repository: `SPAC_Shiny`
- Feature branch: `ref/features-ui-structure`
- Development base: `dev`
- PR target: `dev`
- Primary reference: [SPAC template integration guide](../../../issues/issue-73.md)
- Follow-up development: [Features facet UI](../../feat/features-facet/overview.md)

## Immediate Next Step

Begin Task 4 by replacing the server-inserted Group By controls with static
conditional UI. Then complete the shared-first styling work in Task 5 before
the final Task 3 verification.

## Progress

**In Progress**
- None currently.

**Complete**
- Development tracker created and UI structure agreed.
- Task 1: Extract the Features UI Composition.
- Task 2: Organize the Features Controls Into Sections.

**Remaining**
- Task 4: Replace Dynamic Group By UI With Static Conditions.
- Task 5: Establish Shared Visualization Styling for Features.
- Task 3: Verify the UI Refactor and Prepare It for Review.

**Postponed**
- None currently.

**Dropped**
- None currently.

**Issues (open)**
- None currently.

## Scope Boundary

Center the refactor in `ui/features_ui.py`. Task 4 permits focused changes to
`features_server.py` and `effect_update_server.py` for static Group By
controls. Task 5 permits focused changes to `app.py`, `utils/styling.py`, and
`ui/data_input_ui.py` to establish shared style ownership and make Features
its first visualization consumer.

Preserve all functional input and output IDs, defaults, the current
`output_plot`, and analytical server behavior. Do not add facet controls,
template parameters, responsive preview work, renderer changes, dependencies,
unrelated cross-tab migrations, or unrelated visual polish.

## Development Details

- [Task details](./development-details/task-details.md)
- [Architecture](./development-details/architecture.md)
- [Decisions](./development-details/decisions.md)
- [Implementation log](./development-details/implementation-log.md)
- [Implementation notes](./development-details/implementation-notes.md)
- [Features facet plan](../../plans/features-facet-pr-plan.md)
- [Development roadmap](../../plans/development-roadmap.md)
