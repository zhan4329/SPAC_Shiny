# Implementation Notes

## Branch and PR Sequence

Use the existing `ref/features-ui-structure` branch based on `dev` and open
its PR against `dev`. This UI composition does not depend on PR #86. Whichever
development merges second must rebase because both touch `features_ui.py`;
after this UI PR merges, PR #86 should apply its renderer change inside
`_plot_panel()`. The later `feat/features-facet` development should build on
both accepted changes.

## File and Behavior Boundary

Center changes in `ui/features_ui.py`. Task 4 may edit
`features_server.py` only to remove the Group By insertion lifecycle and
`effect_update_server.py` only to update the static Annotation choices.
Preserve every functional input and output ID, its default, and the ordering
required by the current interaction.

Do not add facet controls, expose further Histogram parameters, change the
template adapter, or alter the current plot renderer. Task 5 may edit
`app.py`, `utils/styling.py`, `ui/data_input_ui.py`, and `ui/features_ui.py`
only to establish shared style loading and adopt reusable visualization
classes in Features. Do not migrate other visualization tabs in this task.

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

## Shared Style Ownership

- Load application-wide and reusable component styles once at the app root.
- Keep Data Input-specific rules owned by `data_input_ui.py` without using that
  page as the delivery path for global styles.
- Keep reusable visualization selectors semantically scoped and make Features
  their first consumer.
- Leave fixed heights, overflow behavior, plot dimensions, and tab-specific
  tooltip rules local rather than treating them as shared defaults.
- Migrate Nearest Neighbor, Feature vs Annotation, and Ripley L separately
  after the shared contract is reviewed through Features.

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
download. Also verify that shared styles load once, Data Input remains styled,
Features uses the reusable visualization classes, and other tabs remain
unchanged.

Do not record work in `implementation-log.md` until implementation or runtime
state actually changes. The agreed task definitions are maintained in
`task-details.md`.
