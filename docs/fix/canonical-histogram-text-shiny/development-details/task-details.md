# Task Details

## Development

### Task 1. Wrap Histogram Template Titles
Location: `SCSAWorkflow/src/spac/templates/histogram_template.py`,
`SCSAWorkflow/tests/templates/test_histogram_template.py`
Date: 2026-09-16
Status: Planned

Implementation decision:
- Keep title wording and line breaks in the Histogram template. Put the
  `grouped by ...` clause on a second line for the custom-table + Group By +
  Plot Together case, preserving all title information and existing title
  ownership. PNG export clipping is owned by Tasks 2 and 3.

Action items:
- [ ] Reproduce the custom-table + Group By + Plot Together title case
  independently of Shiny.
- [ ] Add the semantic line break and allow layout to reserve its vertical
  space without truncating feature, table, grouping, or filtering context.
- [ ] Update focused title tests; preserve ordinary titles and core-owned
  multi-axis panel titles, and check separate/facet output for regressions.
- [ ] Inspect the saved result from an 8-by-6-inch, 300-DPI figure; preserve
  the figure settings without requiring the PNG to have that exact boundary.
- [ ] Run the focused template tests and relevant package checks, review the
  diff, and commit the correction as one SCSAWorkflow PR.

Commit boundary:
Wrap template-generated Histogram titles in one SCSAWorkflow PR without
changing legend placement, Shiny behavior, or package pinning.

### Task 2. Test Expanded PNG Export Boundaries
Location: `SPAC_Shiny/utils/plot_utils.py`, `SPAC_Shiny/tests/test_utils/`,
representative figures from `SCSAWorkflow/src/spac/templates/histogram_template.py`
Date: 2026-09-16
Status: Planned

Testing proposal:
- Validate the complete export required by the
  [export policy](./implementation-notes.md#export-policy).
  Prior exploratory experiments motivate this task but do not complete its
  reproducible verification or constitute an implemented fix.

Action items:
- [ ] Reproduce missing text with the current `fig_to_png_bytes()` using
  synthetic data, distinguishing export clipping from a crowded plot.
- [ ] Compare the existing boundary, `bbox_inches="tight"`, and the proposed
  union of the original canvas and padded content bounds. Confirm that the
  proposed boundary never crops the original canvas.
- [ ] Cover an in-canvas legend and legends extending left, right, above, and
  below the canvas, plus an overflowing title. Include the actual grouped
  Histogram template case and representative ordinary, separate, and facet
  figures.
- [ ] Verify full title/legend bounds fit in the final export, and inspect
  saved PNGs to confirm text is present. A figure whose padded content fits
  inside the original canvas must retain its pixel dimensions.
- [ ] Verify underlying figure dimensions, DPI, font size, legend placement,
  and plot geometry are preserved. Exercise representative non-default
  dimensions/DPI/font sizes through existing APIs, without new UI controls.
- [ ] Include a crowded case such as 20 long labels: export must retain the
  full legend, while readability and overlap are not acceptance requirements
  for this clipping fix.
- [ ] Check the existing `.fig` wrapper support and figure-closing contract;
  use the real helper to verify PNG bytes, not only an isolated formula.
- [ ] Record reproducible commands, environment, image evidence, and findings
  before accepting the approach for Task 3. Retain focused regression cases
  with the Shiny implementation PR.

Acceptance boundary:
Establish that boundary expansion preserves complete exported text without
changing the figure layout. Export completeness is required; automatic
layout of arbitrary amounts of text is outside this task.

### Task 3. Expand Canonical PNG Export in SPAC Shiny
Location: `SPAC_Shiny/utils/plot_utils.py`, `SPAC_Shiny/tests/test_utils/`;
integration check through `SPAC_Shiny/server/features_server.py`
Date: 2026-09-16
Status: Planned

Implementation decision:
- After Task 2 validates the approach, update `fig_to_png_bytes()` to export
  the union of the original canvas and padded rendered-content bounds.
  Preserve figure settings and direct `render.image` delivery.

Action items:
- [ ] Implement the verified expansion at PNG serialization and update the
  helper's documented boundary contract.
- [ ] Add the focused regressions selected in Task 2 and run relevant Shiny
  checks, including unchanged figure cleanup and wrapper support.
- [ ] Verify ordinary and grouped Features rendering, a complete outside
  legend, repeated renders, and unchanged dataframe download in Shiny.
  Exercise facet export directly; facet UI remains outside this task.
- [ ] Verify Shiny receives the complete generated PNG bytes without another
  plotting conversion, and retain evidence of the formerly clipped case.
- [ ] Review and commit the fix as a separate SPAC Shiny PR targeting `dev`.

Commit boundary:
Fix PNG export completeness in SPAC Shiny without combining package title
changes, dependency pinning, responsive sizing, or new parameter controls.
