# Implementation Notes

## Branch and PR Sequence

PR #87 independently targets `dev`. Follow the
[adapter integration notes](../../../ref/features-server-template/development-details/implementation-notes.md#branch-and-pr-sequence)
when combining it with PR #86.

## File and Behavior Boundary

Center changes in `ui/features_ui.py`. Task 4 may edit
`features_server.py` only to remove the Group By insertion lifecycle and
`effect_update_server.py` only to update the static Annotation choices.
Preserve every functional input and output ID, its default, and the ordering
required by the current interaction.

Do not add facet controls, expose further Histogram parameters, change the
template adapter, alter the current plot renderer, or change styling and CSS
loading in this PR.

## Intended UI Organization

- Keep Feature and Table in an always-visible Core Parameters section.
- Put Group By, its static conditionally visible dependent controls, and the
  X/Y log controls in a collapsible Plot Configuration section.
- Put the existing X-axis label rotation control in a collapsible Figure
  Configuration section.
- Add only the two disclosure input IDs needed by those collapsible sections;
  they are presentation state and are not read by the server.
- Keep Render Plot and the download output below the sections, using the
  guide's full-width action-button style.
- Use a 3-column controls area and 9-column result area as in the guide.
- Keep `ui.output_plot("spac_Histogram_1", width="100%", height="60vh")`
  unchanged inside the extracted plot-panel builder.

Prefer private module-level builders such as `_controls_panel()`,
`_collapsible_section()`, and `_plot_panel()`. Keep the disclosure helper local
to this module until another tab has a demonstrated need for the same
abstraction. Do not create `utils/ui_components.py` speculatively; promote a
helper later when at least one additional visualization adopts the same stable
contract.

## Reference and Reuse

Use the organization in the
[SPAC template integration guide](../../../../issues/issue-73.md) as the
primary reference. Adapt the pattern to the current Features controls rather
than copying the example's unrelated controls or exposing its example figure
parameters. Follow PR #66's accepted static conditional-control pattern rather
than copying the incomplete target duplication from Mousumi's facet commit.

## Verification

Run a focused syntax/import check and `git diff --check`. In Shiny, verify the
initial disclosure state, opening and closing both sections, Group By
conditional visibility, Together and Stack Type conditional behavior,
ordinary and grouped renders, repeated rendering, plot display, and dataframe
download.

Do not record work in `implementation-log.md` until implementation or runtime
state actually changes. The agreed task definitions are maintained in
`task-details.md`.
