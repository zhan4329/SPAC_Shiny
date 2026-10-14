# Implementation Notes

## Branch and PR Sequence

Create `feat/features-facet` from a base containing both #86 and #87, following
the [prerequisite integration notes](../../../ref/features-server-template/development-details/implementation-notes.md#branch-and-pr-sequence).
After one prerequisite merges and the other is rebased, facet may be stacked
on the remaining PR branch while it is reviewed. Do not duplicate or
cherry-pick partial prerequisites. Facet cannot merge to `dev` before both.

## Reusing Mousumi's Work

Mousumi's facet work is included in:

```text
5c511e9 facet plot is exposed on the Features Tab
```

Use `git cherry-pick -n 5c511e9` rather than cherry-picking it wholesale
because the commit also changes dependency files and `ripleyL_server.py`.
Retain only applicable Features UI and server changes, update them to the
accepted template contract, and preserve accurate author or co-author
metadata. Mention reused work in the PR description.

## Facet Boundary

Pass `Facet` and `Facet_Ncol` through the existing semantic-input and template
adapter boundaries. Keep facet validation, plotting, titles, layout, and
returned data in the SPAC Histogram template. The template requires
`Group_by` in facet mode and rejects `Together=True` with `Facet=True`.

The visible UI behavior for the incompatible Together-versus-Facet state and
the control representation for automatic versus explicit facet columns remain
open product decisions in the overview.

## Structured UI Boundary

Extend PR #87's static conditional content within Plot Configuration. The
[overview](../overview.md#issues-open) owns the unresolved mode and hidden-state
behavior; its scope boundary lists excluded work.

## Verification

Verify ordinary, grouped-separate, grouped-Together, and facet Histogram
paths. Cover automatic and explicit facet-column values, transitions among
supported modes, understandable handling of the incompatible
Together-versus-Facet combination, repeated rendering, and preservation of
the existing dataframe download behavior.

Do not mark implementation tasks complete until their changes are reviewed,
verified to the agreed boundary, and committed.
