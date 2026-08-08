# Features Server Template Refactor Overview

Refactor the SPAC Shiny Features tab to use the standard SPAC template
workflow while preserving its current behavior. This provides the foundation
for later facet support and agent-driven UI updates.

## Project Context

- Repository: `SPAC_Shiny`
- Feature branch: `ref/features-server-template`
- Target branch: `dev`
- Dependency prerequisite: `chore/pin-spac-to-pr-433`
- Primary reference: [SPAC template integration guide](https://github.com/FNLCR-DMAP/SPAC_Shiny/issues/73)
- Related examples: [PR #75](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/75), [PR #80](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/80), and [Mousumi's draft PR #81](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/81)

## Immediate Next Step

After the prerequisite is merged, start Task 1.

## Progress

**In Progress**
- None currently.

**Remaining tasks**
- Task 1: Use the Canonical AnnData Source.
- Task 2: Extract the Features Input Snapshot.
- Task 3: Add the Agent-to-UI Parameter Registry.
- Task 4: Build the SPAC Template Parameter Dictionary.
- Task 5: Delegate Histogram Execution to the Template.
- Task 6: Preserve and Verify Reactive UI Behavior.
- Task 7: Add Focused Adapter Tests.

**Complete**
- None currently.

**Postponed tasks**
- None currently.

**Dropped tasks**
- None currently.

**Issues (open)**
- None currently.

## Scope Boundary

Keep the adapter boundary focused on canonical AnnData access, current
Features inputs, template payload construction, memory-registry execution,
dataframe return, and the agent-to-UI registry. Keep facet UI, new histogram
controls, persistent state, JSON/CLI endpoints, and broad UI cleanup in later
developments.

## Development Details

- [Task details](./development-details/task-details.md)
- [Architecture](./development-details/architecture.md)
- [Decisions](./development-details/decisions.md)
- [Implementation notes](./development-details/implementation-notes.md)
- [Future work](../../plans/future-work.md)
