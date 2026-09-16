# Features Facet Near-Future PR Plan

## Goal

Expose facet histograms through the SPAC Histogram template and leave the
Features tab with a structured UI, responsive preview, and useful template
controls. This is the first program step in the
[SPAC development roadmap](./development-roadmap.md).

This file defines PR-sized developments only. Each PR will receive its own
task details, acceptance criteria, implementation log, and verification plan
when development begins. PRs 1-3 provide the prerequisites for the
interview-target agentic Features workflow; PRs 4-6 normally resume afterward.
These numbers identify plan entries, not GitHub PR numbers.

## Ordered PR Developments

### PR 1. Complete Features Template Delegation

Repository: SPAC Shiny

Current development: [PR #86](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/86), `ref/features-server-template`

Tracker: [Features template delegation](../ref/features-server-template/overview.md)

Complete mentor review and merge the existing delegation work without adding
facet controls, responsive behavior, template layout fixes, caching, or
downloads. This PR establishes the adapter and canonical-rendering boundary
used by every later PR in this sequence.

### PR 2. Establish Features UI Structure and Static Controls

Repository: SPAC Shiny

Current development: [PR #87](https://github.com/FNLCR-DMAP/SPAC_Shiny/pull/87), `ref/features-ui-structure`

Tracker: [Features UI structure](../ref/features-ui-structure/overview.md)

Complete review of the independent UI organization and static Group By
control refactor. Detailed scope belongs to its tracker. Shared styling
remains in roadmap Step 7.

### PR 3. Expose Facet Through the Structured Features UI

Repository: SPAC Shiny

Planned development: `feat/features-facet`

Tracker: [Features facet UI](../feat/features-facet/overview.md)

Expose `Facet`, `Facet_Ncol`, and their coupled grouping behavior through the
existing template adapter and structured UI. Preserve non-facet behavior;
inherit the UI refactor rather than repeating it. Interaction decisions and
verification belong to the facet tracker. Agent PR C will use the resulting
input contract.

### PR 4. Contain Canonical Histogram Text

Repository: SCSAWorkflow  
Inherited from PR 1: Task 8

Fix long-title and long-legend-label containment inside the Histogram
template. Verify ordinary, grouped, external-legend, and facet output at the
canonical dimensions and DPI. Keep Shiny browser sizing out of this package
PR.

This PR owns the PR 1 finding that long template-generated titles or legend
labels can be clipped at the canonical PNG boundary.

This PR may be developed while a SPAC Shiny PR is waiting for mentor review,
but it should be accepted before download behavior is finalized.

### PR 5. Make the Histogram Preview Responsive

Repository: SPAC Shiny

Inherited from PR 1: Task 9

Present the canonical image at the available width while preserving its aspect
ratio. Derive height from the image and permit vertical page flow or an
intentional scroll region for tall facet figures. Do not mutate the canonical
artifact or introduce download and cache behavior.

This PR owns the PR 1 finding that proportional preview fitting can leave
available browser width unused.

### PR 6. Expose Remaining Histogram Parameters

Repository: SPAC Shiny

Expose the remaining justified Histogram template parameters in clearly
separated analytical and presentation sections. Analytical controls may
include bins, statistic, element, and transparency. Presentation controls may
include legend placement, axis-label rotation, font size, figure dimensions,
and DPI after canonical containment and responsive presentation are stable.
Keep template defaults when the UI does not need to override them, and ensure
one parameter snapshot creates the same canonical appearance for preview and
future download.

The exact parameter set will be selected when this PR begins, after reviewing
the then-current Histogram template contract. Split this PR only if its final
scope cannot be implemented and verified within roughly two or three working
sessions.

After this PR stabilizes the final planned Histogram parameter contract,
reconsider former PR 1 Task 7 through the
[deferred adapter verification](./future-work.md#deferred-verification)
development rather than adding it to an earlier unstable PR.

## Ordering Rules

- PRs 1 and 2 independently target `dev`; either may merge first. Follow the
  [adapter integration notes](../ref/features-server-template/development-details/implementation-notes.md#branch-and-pr-sequence).
- PR 3 requires both prerequisites before merging. Its
  [branch sequence](../feat/features-facet/development-details/implementation-notes.md#branch-and-pr-sequence)
  also permits stacked development after their integration.
- PR 4 is independent of PR 3 but precedes final download development.
  Reconsider its timing if facet verification shows blocking text clipping.
- PR 5 follows PR 3 because responsive behavior must be tested against real
  adaptive facet geometry.
- Within PR 6, implement analytical controls before presentation controls
  because presentation behavior depends more heavily on final layout.
- Do not add naming, caching, downloads, cancellation, other tabs, or full
  chatbot integration to this sequence merely because they touch plotting.

## Target Milestones

- Mid-September 2026: complete review and integration of PRs 1-2, settle the
  facet interaction, and implement PR 3 from the combined prerequisite base.
- After PR 3 through mid-to-late October: pause this sequence for the
  end-to-end agentic Features milestone defined in the broader roadmap.
- Late October and November: aim to complete PRs 4-5.
- December: continue PR 6 as capacity and mentor review permit.

The dates are direction rather than promises. With only a few hours per week,
a reviewed PR that establishes a reusable pattern is more valuable than
several simultaneous drafts.
