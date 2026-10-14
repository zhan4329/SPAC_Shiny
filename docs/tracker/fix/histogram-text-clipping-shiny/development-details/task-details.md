# Task Details

## Development

Execution order: Task 2 first; Task 1 is independent. Task IDs are retained
from the original plan.

### Task 1. Wrap Histogram Template Titles
Location: `SCSAWorkflow/src/spac/templates/histogram_template.py`,
`SCSAWorkflow/tests/templates/test_histogram_template.py`
Date: 2026-09-16
Status: Planned

Remarks:
Title wording belongs to the template; export completeness belongs to Task 2.
Preserve all title context and existing ownership of multi-axis panel titles.

Action items:
- [ ] Reproduce the custom-table + Group By + Plot Together title and put
  `grouped by ...` on a second line, allowing space for both lines.
- [ ] Update existing title tests and visually inspect the saved result;
  check that ordinary and multi-panel titles retain their context.
- [ ] Run focused template tests and required package checks, review the
  diff, and commit the correction for a separate SCSAWorkflow PR to `dev`.

### Task 2. Preserve Complete Histogram PNG Output
Location: `SPAC_Shiny/utils/plot_utils.py`, `SPAC_Shiny/tests/test_utils/`
Date: 2026-09-16
Replanned: 2026-10-14 (absorbs former Task 3)
Status: In Progress

Remarks:
Follow the [export policy](./implementation-notes.md#export-policy).
Automatic layout of arbitrary amounts of text is outside this clipping fix.

Action items:
- [x] Reproduce one clipped grouped Histogram with the current
  `fig_to_png_bytes()` and retain a before image.
- [ ] Implement export of the union of the original canvas and padded
  rendered-content bounds; update the helper's boundary documentation.
- [ ] Add focused helper regressions for overflowing title/legend text,
  unchanged output dimensions when padded content fits, and preserved
  figure geometry and DPI. Parameterize legend overflow directions and
  retain wrapper support and figure-cleanup checks.
- [ ] Inspect the corrected grouped Histogram and one multi-panel export,
  and smoke-check ordinary and grouped Features display. Retain a matching
  after image and reproducible verification commands.
- [ ] Run relevant Shiny checks, review the diff, and commit the correction
  for a separate SPAC Shiny PR to `dev`.

Acceptance:
Complete title and legend text, preserved plot appearance, and unchanged
ordinary output. Expand verification if changed code or observed regressions
implicate other paths; dataframe downloads and broad UI testing are not
separate requirements for a serializer-only change.

Evidence (2026-10-14): User-provided [PNG](../pr-details/images/before_image.png)
and [screenshot](../pr-details/images/before_screenshot.png) visually confirm
clipped title and legend text in the export; workflow not rerun.

### Task 3. Expand Canonical PNG Export in SPAC Shiny
Date: 2026-09-16
Status: Dropped as a separate task (2026-10-14)

Consolidated into [Task 2](#task-2-preserve-complete-histogram-png-output).
Its implementation and verification remain planned there; no implementation
is recorded as complete.
