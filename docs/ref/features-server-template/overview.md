# Features Server Template Refactor Development Overview

## Problem Statement

Refactor the SPAC Shiny Features tab to use the standard SPAC template workflow while preserving its current behavior. This provides the foundation needed for later facet support and agent-driven UI updates.

## Project Context

- Repository: `SPAC_Shiny`
- Feature branch: `ref/features-server-template`
- Target branch: `dev`
- Dependency prerequisite: `chore/pin-spac-to-pr-433`
- Primary reference: [SPAC template integration guide](https://github.com/FNLCR-DMAP/SPAC_Shiny/issues/73), or [issue-73.md](../../issues/issue-73.md)
- Related examples: [PR #75](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/75) and [PR #80](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/80)
- Related prior work: [Mousumi's draft PR #81](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/81)

## Immediate Next Step

With `chore/pin-spac-to-pr-433` complete, start Task 1 and implement the
Features adapter tasks below, including the current-dev Histogram template
contract checks assigned to Tasks 4, 5, and 7.

## Progress

### Ongoing Tasks

None currently.

### Remaining Tasks

1. Use the canonical shared AnnData object in the Features server.
2. Extract the Features input snapshot.
3. Add the parameter registry for agent-to-UI updates.
4. Build the current-dev SPAC template parameter dictionary.
5. Delegate histogram execution to the current-dev SPAC template.
6. Preserve and verify the existing reactive UI behavior.
7. Add focused adapter tests for the current-dev contract.

### Postponed Tasks

None currently.

### Issues (Open)

None currently. The former overview issues are reclassified in [D6](./development-details/decisions.md#d6-reclassify-former-overview-issues); Task 1 owns the canonical-source implementation.

## Scope

The adapter should establish the same Shiny-to-template boundary described in
Issue #73 and used by the existing refactored tabs. The canonical AnnData
source and projected UI-choice values must remain distinct. The dependency
baseline is tracked separately in `docs/chore/pin-spac-to-pr-433/`. Facet
support is planned separately in `docs/feat/features-facet/`.

## Development Details

See [task-details.md](./development-details/task-details.md) for the numbered
commit-sized development tasks.

See [implementation-notes.md](./development-details/implementation-notes.md) for the branch, cherry-pick, and attribution approach.

See [architecture.md](./development-details/architecture.md) for the planned
Features server and template-adapter structure.

## Decision Log

See [decisions.md](./development-details/decisions.md) for recorded decisions.

## Future Work

See [future-work.md](../../plans/future-work.md) for controls and UI work intentionally deferred from this development.
