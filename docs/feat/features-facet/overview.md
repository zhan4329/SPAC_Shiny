# Features Facet Development Overview

## Problem Statement

Expose the updated SPAC histogram facet feature in the SPAC Shiny Features tab. This work depends on the template adapter because facet behavior should be driven by the SPAC template rather than reimplemented in Shiny.

## Project Context

- Repository: `SPAC_Shiny`
- Feature branch: `feat/features-facet`
- Target branch: `dev`
- Prerequisite: `ref/features-template-adapter`
- Primary reference: [SPAC template integration guide](https://github.com/FNLCR-DMAP/SPAC_Shiny/issues/73)
- Related prior work: [Mousumi's draft PR #81](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/81)

## Immediate Next Step

Review and implement the facet concerns below after the template-adapter work is merged.

## Progress

### Ongoing Tasks

None currently.

### Remaining Tasks

None currently.

### Postponed Tasks

None currently.

### Issues (Open)

The following candidate work remains undecided:

1. Start facet exposure only after the template-adapter PR is complete.
2. Define the facet PR boundary as Shiny UI/server wiring, with facet behavior remaining in the SPAC template.
3. Decide the intended interaction between facet and Together/grouped plotting controls.
4. Decide the focused verification needed for facet-enabled and ordinary histogram paths.

## Analysis Summary

The Shiny layer should expose the facet input and pass it through the adapter. The SPAC template should remain responsible for facet validation, plotting, figure construction, and returned data.

## Development Details

See [implementation-notes.md](./development-details/implementation-notes.md) for the branch, cherry-pick, and attribution approach.

## Future Work

See [future-work.md](../../plans/future-work.md) for controls and UI work intentionally deferred from this development.
