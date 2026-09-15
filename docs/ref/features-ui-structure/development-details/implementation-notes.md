# Implementation Notes

## Branch and PR Sequence

Create `ref/features-ui-structure` from `dev` and open its PR against `dev`.
This UI composition does not depend on PR #86. Whichever development merges
second must rebase because both touch `features_ui.py`; after this UI PR
merges, PR #86 should apply its renderer change inside `_plot_panel()`. The
later `feat/features-facet` development should build on both accepted changes.

## File and Behavior Boundary

Change only `ui/features_ui.py`. Preserve every existing functional input and
output ID, its default, and the ordering required by the current interaction.
Keep `main-h1_dropdown`, `main-h1_check`, and `main-h1_together_drop` inside
the Plot Configuration content so the current `insert_ui()` and `remove_ui()`
selectors continue to work.

Do not edit `features_server.py`, add facet controls, expose further Histogram
parameters, change the template adapter, or alter the current plot renderer.
Do not add shared components or stylesheet work for a one-tab refactor.

## Intended UI Organization

- Keep Feature and Table in an always-visible Core Parameters section.
- Put Group By, its insertion targets, and the X/Y log controls in a
  collapsible Plot Configuration section.
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
parameters. No code from Mousumi's facet commit is required for this
presentation-only development.

## Verification

Run a focused syntax/import check and `git diff --check`. In Shiny, verify the
initial disclosure state, opening and closing both sections, Group By dynamic
insertion and removal, Together and Stack Type behavior, ordinary and grouped
renders, repeated rendering, plot display, and dataframe download.

Do not record implementation in `implementation-log.md` or populate
`task-details.md` until implementation work actually begins and its concrete
tasks are agreed.
