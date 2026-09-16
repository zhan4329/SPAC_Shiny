# Features Facet UI Overview

Expose facet histograms through a structured SPAC Shiny Features UI while
preserving the accepted template-adapter and canonical-rendering boundaries.

## Project Context

- Repository: `SPAC_Shiny`
- Proposed feature branch: `feat/features-facet`
- Target branch: `dev`
- Development prerequisites: merged PR #86, `ref/features-server-template`, and PR #87,
  [Features UI structure refactor](../../ref/features-ui-structure/overview.md)
- Development base: a branch containing both accepted prerequisites
- Merge prerequisite: both prerequisite PRs must merge before this development
  merges to `dev`
- Primary reference: [SPAC template integration guide](../../../issues/issue-73.md)
- Governing plan: [Features facet PR plan](../../plans/pr-plans/1-features-facet-pr-plan.md#pr-3-expose-facet-through-the-structured-features-ui)
- Related prior work: [Mousumi's draft PR #81](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/81)

## Immediate Next Step

Resolve the facet-specific interaction and verification issues below. Create
`feat/features-facet` once its base contains both prerequisites, following the
integration sequence in
[implementation notes](./development-details/implementation-notes.md#branch-and-pr-sequence).

## Progress

**In Progress**
- None currently.

**Complete**
- Development tracker created.

**Postponed**
- None currently.

**Dropped**
- None currently.

## Issues (Open)

1. Choose the Together-versus-Facet interaction. Proposal: one Group By
   presentation mode with Combined, Separate, and Facet Grid choices, mapped to
   the three valid `Together`/`Facet` states so the invalid combination cannot
   be selected.
2. Choose the `Facet_Ncol` control. Proposal: Automatic submits `"auto"`;
   Custom reveals a positive-integer input. Exact controls and reset behavior
   remain undecided.
3. Define facet-specific state normalization over PR #87's static controls.
   Specify what happens to retained Annotation, Together, Stack Type, and
   facet-column selections when Group By or a mode is disabled or changed;
   inactive values must not affect the template payload. Dynamic insertion
   cleanup is already owned by #87 and is not facet work.
4. Confirm verification. Proposal: focused normalization and parameter-mapping
   tests for ordinary, separate, Combined, and both facet-column modes, plus
   direct Shiny checks of transitions, repeated rendering, and dataframe
   download.
5. Check representative facets in the current fixed-height preview. Keep
   responsive behavior separate unless the facet result is unusable, in which
   case reconsider the boundary instead of adding an undocumented workaround.

## Issues (Reassigned)

- UI composition and static Group By control ownership belong to
  [PR #87's tracker](../../ref/features-ui-structure/overview.md).

## Scope Boundary

Build on the accepted Features UI structure and change only the grouping and
facet content needed to expose `Facet`, `Facet_Ncol`, and their directly
coupled behavior. Define a clear Together-versus-Facet interaction, preserve
current non-facet behavior, and keep validation and plot construction in the
Histogram template.

Do not include responsive preview behavior, canonical text containment,
general Features UI composition or layout work, remaining Histogram
parameters, broad cross-tab input renaming, caching, downloads, cancellation,
or agent integration.

## Development Details

- [Task details](./development-details/task-details.md)
- [Architecture](./development-details/architecture.md)
- [Decisions](./development-details/decisions.md)
- [Implementation log](./development-details/implementation-log.md)
- [Implementation notes](./development-details/implementation-notes.md)
- [Features UI structure refactor](../../ref/features-ui-structure/overview.md)
- [Features facet PR plan](../../plans/pr-plans/1-features-facet-pr-plan.md)
- [Development roadmap](../../plans/development-roadmap.md)
- [Future work](../../plans/future-work.md)
