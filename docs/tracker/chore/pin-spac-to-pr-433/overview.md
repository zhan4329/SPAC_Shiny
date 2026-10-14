# Pin SPAC to PR #433 Compatibility Overview

Update SPAC Shiny to the official SPAC commit containing PR #433's
histogram-facet follow-up, then keep existing template callers compatible
before downstream Features adapter work begins.

## Project Context

- Repository: `SPAC_Shiny`
- Feature branch: `chore/pin-spac-to-pr-433`
- Target branch: `dev`
- SPAC commit: `f9886bcde643ebf14e58a31d5ac397e28b6ea510`
- Environment: Docker image based on `python:3.9.19-slim-bookworm`

## Immediate Next Step

After this prerequisite is merged, start the Features template-adapter
development.

## Progress

**In Progress**
- None currently.

**Complete**
- Task 1: Update the SPAC Dependency Pin.
- Task 2: Verify the Current SPAC Dev Contract.
- Task 3: Fix SPAC Template Caller Compatibility.

**Postponed tasks**
- Facet UI exposure.

**Dropped tasks**
- None.

**Issues (open)**
- None.

## Scope Boundary

Keep this development limited to dependency pinning, existing SPAC contract
verification, and compatibility fixes required by the pinned SPAC contract.
Defer facet UI, Annotation, UMAP, and broad cleanup to the downstream
developments. The Features server template refactor is the next development
after this prerequisite.

## Development Details

- [Task details](./development-details/task-details.md)
- [PR summary](./pr-summary.md)
- [Decisions](./development-details/decisions.md)
- [Implementation log](./development-details/implementation-log.md)
- [Implementation notes](./development-details/implementation-notes.md)
