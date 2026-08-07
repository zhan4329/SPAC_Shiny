# Pin SPAC to PR #433 Compatibility Overview

Update the SPAC dependency to the official commit containing PR #433's
histogram-facet follow-up, then keep existing template callers compatible.
This PR is a prerequisite for the Features adapter refactor.

## Project Context

- Repository: `SPAC_Shiny`
- Feature branch: `chore/pin-spac-to-pr-433`
- Target branch: `dev`
- Downstream branch: `ref/features-template-adapter`
- SPAC commit: `f9886bcde643ebf14e58a31d5ac397e28b6ea510`

## Immediate Next Step

Complete Task 1, then Task 2.

## Scope

Update the dependency pin, verify the current template contract, and apply
compatibility fixes required by the new pin. Features refactoring, facet UI,
Annotation, UMAP, and broad cleanup are out of scope.

## Remaining Tasks

1. Update the SPAC dependency pin.
2. Verify the SPAC contract and existing template callers.

## Development Details

- [Task details](./development-details/task-details.md)
- [Implementation notes](./development-details/implementation-notes.md)
- [Decision log](./development-details/decisions.md)
