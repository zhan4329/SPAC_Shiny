# Implementation Notes

## Branch and PR Sequence

Create `chore/pin-spac-to-pr-433` from `dev`. After it is merged,
create `ref/features-template-adapter` from the updated `dev`.
Create `feat/features-facet` only after the adapter PR is merged.

## Compatibility Boundary

Keep this PR limited to the dependency pin and compatibility changes required
by the installed SPAC contract. Do not add Features refactoring, facet UI,
Annotation changes, UMAP changes, or broad cleanup.

## Prior-Branch Evidence

Mousumi's `ref/features-template` branch updated the dependency pin and
changed `server/ripleyL_server.py` to import
`visualize_ripley_l_template`. It left other template callers using the
older execution argument, so use the branch as evidence for compatibility
scope rather than cherry-picking it wholesale.

## Verification

Run focused checks for the Histogram, Nearest Neighbor, and Ripley template
paths after installing the selected SPAC commit. Record implementation
evidence in the implementation log when work begins.
