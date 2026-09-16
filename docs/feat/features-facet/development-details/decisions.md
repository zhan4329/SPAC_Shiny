### D3. Inherit the Independent Features UI Structure
Date: 2026-09-15

Decision:
Treat `ref/features-ui-structure` and PR #86 as two prerequisites for the facet
development. Reassign the general Issue #73 module composition, parameter
sections, 3/9 layout, and local disclosure helper to the UI-structure tracker.
Keep only the facet-specific grouping lifecycle, controls, semantic mapping,
and verification in this development. Create the facet branch from a base
containing both prerequisites; normally this will be PR #86 after it has been
rebased onto the accepted UI structure.

This supersedes D2's instruction to base the facet branch on the original
unrebased `ref/features-server-template` branch. D2's stacked-development and
merge-order rationale still applies once both prerequisite boundaries are in
the base.

Rationale:
The UI module structure is independent of the template adapter and now has a
focused development owner. Repeating it in the facet PR would duplicate scope
and obscure the feature-specific review. The facet implementation still needs
the accepted UI structure as its presentation boundary and PR #86 as its
semantic and execution boundary.

### D2. Begin Facet Development as a Stacked Branch
Date: 2026-09-15

Decision:
Create `feat/features-facet` from the unmerged
`ref/features-server-template` branch and keep it stacked on that branch while
PR #86 is under review. If a draft PR is opened before PR #86 merges, target
the prerequisite branch so review shows only the feature commits. After PR #86
merges, rebase the feature-only commits onto the updated `dev`, retarget the PR
to `dev`, and preserve the rule that the facet PR cannot merge first.

Rationale:
The facet work depends on PR #86's semantic-input, template-adapter, and
canonical-rendering boundaries. Stacking permits development to start without
duplicating or cherry-picking that work, while retaining the intended merge
order and a focused review diff.

### D1. Reclassify Preliminary Facet Issues
Date: 2026-09-09

Decision:
Treat the merged template adapter as a prerequisite rather than an open
issue, and retain the Shiny-to-template ownership boundary as established
scope. Move focused ordinary and facet verification into the development's
verification boundary. Keep broad input naming outside PR 2 under the roadmap's
later shared naming work. Retain the exact Together-versus-Facet interaction
and the `Facet_Ncol` automatic-versus-explicit control design as open product
decisions.

Rationale:
The current Features code already provides the semantic-input and template
adapter boundaries, while the pinned Histogram template requires `Group_by`
for facet mode and rejects `Together=True` with `Facet=True`. The plan and
roadmap therefore settle ownership and sequencing, but they intentionally do
not choose how the visible UI should enforce the incompatible-state rule or
represent the template's automatic facet-column value.
