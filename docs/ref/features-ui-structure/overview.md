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

Create `ref/features-ui-structure` from `dev`,
implement the UI-only organization recorded in
[Architecture](./development-details/architecture.md), verify preservation of
the existing Features interactions, and open a focused PR against `dev`.

## Progress

**In Progress**
- None currently.

**Complete**
- Development tracker created and UI structure agreed.

**Postponed**
- None currently.

**Dropped**
- None currently.

## Scope Boundary

Change only `ui/features_ui.py`. Compose the Features panel from focused
control and plot helpers; organize the existing inputs into always-visible
core parameters, collapsible plot configuration, collapsible figure
configuration, and actions; and use the guide's clearer control-versus-plot
layout.

Preserve all functional input and output IDs, defaults, dynamic insertion
targets, the current `output_plot`, and current server behavior. Do not add
facet controls, template parameters, server changes, responsive preview work,
renderer changes, shared UI utilities, dependencies, or unrelated visual
polish.

## Development Details

- [Task details](./development-details/task-details.md)
- [Architecture](./development-details/architecture.md)
- [Decisions](./development-details/decisions.md)
- [Implementation log](./development-details/implementation-log.md)
- [Implementation notes](./development-details/implementation-notes.md)
- [Features facet plan](../../plans/features-facet-pr-plan.md)
- [Development roadmap](../../plans/development-roadmap.md)
