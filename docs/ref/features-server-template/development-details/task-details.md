# Task Details

## Development

### Task 10. Resolve the Canonical PNG Renderer Boundary
Location: `SPAC_Shiny/server/features_server.py`,
`SPAC_Shiny/ui/features_ui.py`, and `SPAC_Shiny/utils/plot_utils.py`
Date: 2026-09-02
Status: Complete

Implementation decision:
- Resolve the newly introduced PNG delivery boundary in the current SPAC
  Shiny PR before changing responsive layout. Compare the existing
  `render.plot` wrapper with direct `render.image` delivery without treating
  browser sizing as part of this task.
- Select direct `render.image(delete_file=True)` delivery. Write the canonical
  PNG bytes to a closed, uniquely named temporary file for Shiny to read, and
  let the renderer delete successfully delivered files. Keep rare pre-return
  filesystem-failure cleanup out of the server path to preserve readability.

Action items:
- [x] Confirm the `render.image` and `output_image` contract under the pinned
  Shiny 0.10.2 runtime.
- [x] Replace the PNG-to-Matplotlib wrapper with direct canonical-PNG delivery
  if it preserves the artifact without layout mutation.
- [x] Use explicit temporary-file cleanup, including reactive rerenders and
  failure paths.
- [x] Simplify the implemented cleanup after review by relying on
  `render.image(delete_file=True)` for successful delivery and accepting the
  narrow pre-return failure-path tradeoff.
- [x] Remove `png_bytes_to_figure()` and its imports if direct image delivery
  makes them unused.
- [x] Preserve button-gated rendering, dataframe publication, memory-registry
  cleanup, and the current display-size behavior.
- [x] User-verify ordinary and grouped-together histograms and repeat plot
  generation within one session.
- [x] Run focused static checks and review the renderer diff.
- [x] Commit the renderer correction separately.

Verification finding (2026-09-02):
- The user reported that direct image delivery looks good in the Shiny app.
  Focused review found no blocking code issue; the accepted residual risk is
  a temporary file left behind only if execution fails after file creation
  but before the renderer receives the returned image path.

Evidence:
- Implemented, user-verified, reviewed, committed, and pushed in `da242c6`
  (`refactor(features): deliver canonical PNG directly`).

Commit boundary:
Deliver canonical histogram PNG bytes through the selected Shiny renderer
without changing responsive sizing, caching, or downloads.

### Task 9. Make the Histogram Preview Responsive
Location: `SPAC_Shiny/server/features_server.py`,
`SPAC_Shiny/ui/features_ui.py`, and rendering utilities
Date: 2026-09-01
Status: Reassigned

Implementation decision:
- Reassigned on 2026-09-03 to the responsive-preview development, now PR 5
  after the 2026-09-15 UI extraction, in the
  [Features facet plan](../../../plans/pr-plans/1-features-facet-pr-plan.md#pr-5-make-the-histogram-preview-responsive).
  No implementation belongs to the current template-delegation PR.
- Treat proportional preview delivery as a Shiny concern independent of
  both canonical text containment and the selected Shiny renderer. Fit the
  preview to the available width, preserve its aspect ratio, derive its height,
  and allow vertical page flow or scrolling where necessary.

Action items:
- [ ] Define a renderer-neutral responsive sizing contract for the plot output
  and its containing column.
- [ ] Verify proportional full-width display and adaptive facet ratios at
  representative desktop widths. Allow vertical page flow or an intentional
  scroll region when the derived height is large.
- [ ] Verify that responsive sizing does not change the canonical image or its
  download representation.

Commit boundary:
Present the canonical histogram at the available Shiny width without changing
its aspect ratio or implementing caching and downloads.

### Task 8. Contain Histogram Template Text Within Its Canvas
Location: `SCSAWorkflow/src/spac/templates/histogram_template.py`
Date: 2026-09-01
Status: Reassigned

Implementation decision:
- Reassigned on 2026-09-03 to the canonical-text development, now PR 4
  after the 2026-09-15 UI extraction, in the
  [Features facet plan](../../../plans/pr-plans/1-features-facet-pr-plan.md#pr-4-contain-canonical-histogram-text).
  Detailed work is now owned by the
  [Canonical Histogram Text tracker](../../../fix/canonical-histogram-text/overview.md).
  No implementation belongs to the current template-delegation PR.
- The successor tracker owns the revised scope; this reassignment remains
  historical.

Action items:
- Detailed unexecuted action items belong to the
  [Canonical Histogram Text tasks](../../../fix/canonical-histogram-text/development-details/task-details.md).

Commit boundary:
Commit boundaries belong to the successor tracker.

### Task 7. Add Focused Adapter Tests
Location: `server/features_server.py`, `tests/`
Date: 2026-08-05
Status: Postponed

Implementation decision:
- Defer comprehensive automated adapter verification to the specialized SWE
  stage. Use direct Shiny app verification during the current unstable
  development, while retaining tests for stable reusable utilities when
  appropriate.

Action items:
- [ ] Add tests for `get_features_inputs()` and
  `build_template_params()`.
- [ ] Mock `run_from_json()` and assert the current-dev template payload and
  returned figure/dataframe handling.
- [ ] Cover the current-dev Histogram template import, parameter defaults,
  `save_to_disk=False`, `show_plot=False`, and the in-memory return contract.
- [ ] Assert memory-registry cleanup after successful and failed execution.
- [ ] Cover ordinary and grouped non-facet parameter paths.
- [ ] Run the focused adapter test module.

Commit boundary:
Add focused tests for the Features template-adapter contract.

### Task 6. Preserve and Verify Reactive UI Behavior
Location: `server/features_server.py`, `utils/plot_utils.py`
Date: 2026-08-05
Status: Complete

Implementation decision:
- Keep dynamic UI effects separate from AnnData access and template execution.
- Keep this compatibility correction in the template-refactor PR as a
  separate commit. Preserve the template's 300-DPI default, freeze its
  completed figure as canonical PNG bytes, and retain `render.plot` through a
  display-only wrapper figure.

Action items:
- [x] Implement the focused final-save safeguard with
  `@render.plot(bbox_inches="tight", pad_inches=0.1)` without adding fixed
  dimensions or new UI controls.
- [x] User-verify the full figure at normal browser zoom and representative
  window sizes while rechecking the current non-facet controls.
- [x] If verification passes, commit the fix and complete Task 6; otherwise,
  investigate the Histogram template's in-memory sizing before considering
  fixed dimensions or manual figure controls.
- [x] Add or adapt focused figure-to-PNG and PNG-to-display-figure helpers
  from the PR #76 pattern without introducing its cache.
- [x] Serialize the template-returned figure at its own DPI with
  `bbox_inches=None`, preserve its intrinsic geometry, and close the original
  figure after serialization.
- [x] Return the display-only wrapper through the existing `@render.plot`
  boundary; do not switch to `render.image` in this task.
- [x] Keep `Figure_DPI` out of the current adapter payload so the template
  supplies its 300-DPI default; do not add DPI or other figure controls.
- [x] Preserve dataframe publication, memory-registry cleanup, button-gated
  rendering, and current non-facet controls.
- [x] Run focused static checks, review the resulting diff, and commit the
  rendering correction separately before completing Task 6.

Verification findings (2026-09-01):
- F6.1 — Deferred: the core Histogram function disables
  `x_log_scale` when the selected data contains negative values and reports
  this only through console output, so the Shiny control appears ineffective
  to the user. Address the feedback and unavailable-control behavior in
  [Future work](../../../plans/future-work.md#deferred-ui-work).
- F6.2 — Deferred: reposition the dynamically inserted Group By controls in
  the later Features UI-exposure work; see
  [Future work](../../../plans/future-work.md#deferred-ui-work).
- F6.3 — Addressed: direct `render.plot` presentation of the template's 300-DPI
  Matplotlib figure makes text too large relative to the browser plot area and
  can clip titles, labels, or legends. A temporary 80-DPI override rendered
  acceptably on the tested MacBook Air and Dell display, but it conflates
  screen layout with artifact resolution and is not the selected final fix.
- Rejected experiments: `bbox_inches="tight"`, an additional tight layout
  engine, and fixed 8-by-6 sizing at the Shiny boundary did not solve the
  scaling problem without distortion or other regressions.
- Selected remediation: retain the template's 300-DPI figure as the canonical
  artifact, flatten it before Shiny can recalculate its internal layout, and
  display it through the existing `render.plot` interface. This matches the
  PNG-byte boundary needed by future caching and download work without
  implementing those features here. The remediation was implemented and
  user-verified within the Task 6 boundary.
- Runtime outcome: the user confirmed that the adapter preserves an acceptable
  plot appearance. The newly observed canonical text clipping and unused-width
  behavior are unimplemented work assigned to Tasks 8 and 9 respectively,
  rather than additional Task 6 findings.

Evidence:
- Implemented, reviewed, and committed in `54320cc`; see the
  [Implementation log](./implementation-log.md) for verification and
  attribution details.

Commit boundary:
Preserve the template's completed figure geometry through a canonical-PNG
display adapter while keeping existing Features reactivity and `render.plot`.

### Task 5. Delegate Histogram Execution to the Template
Location: `server/features_server.py`
Date: 2026-08-05
Status: Complete

Implementation decision:
- Register the canonical AnnData object returned by `get_adata()`
  through the existing memory registry.

Action items:
- [x] Import the histogram template and memory-registry helpers.
- [x] Register the object returned by `get_adata()` before template
  execution.
- [x] Call `run_from_json(..., save_to_disk=False, show_plot=False)`
  with the built parameter dictionary.
- [x] Store the returned dataframe in `shared["df_histogram1"]` and
  return the returned figure.
- [x] Unregister the memory object in a `finally` block.
- [x] Remove the direct `spac.visualization.histogram()` call from
  the Features renderer.

Evidence:
- Implemented and reviewed in `2b7382b`; related docstrings committed in
  `4ec93f0`.
- The template-backed plot reached the Shiny output during user verification.
  See [Architecture](./architecture.md) for the execution lifecycle; broader
  UI verification remains Task 6.

Commit boundary:
Move the Features histogram execution from the bare SPAC visualization API
to the SPAC histogram template.

### Task 4. Build the SPAC Template Parameter Dictionary
Location: `server/features_server.py`
Date: 2026-08-05
Status: Complete

Implementation decision:
- Keep semantic Features inputs separate from the template’s parameter names.

Action items:
- [x] Define pure `build_template_params(input_values, virtual_path)`
  conversion.
- [x] Map the current inputs to the template keys
  `Upstream_Analysis`, `Feature`, `Table_`,
  `Take_X_Log`, `Take_Y_log`, `Group_by`,
  `Together`, `Multiple`, and `X_Axis_Label_Rotation`.
- [x] Set explicit adapter invariants for feature mode and non-facet behavior
  without exposing new controls in this task.
- [x] Let the Histogram template supply defaults for controls not exposed by
  the current Features UI.
- [x] Pass `"None"` or the template’s documented default tokens where
  the template requires them.

Evidence:
- Implemented and reviewed against pinned SPAC commit `f9886bc` in
  `2b7382b`; see [Architecture](./architecture.md) for the payload contract.

Commit boundary:
Create the pure semantic-state-to-template-payload conversion.

### Task 3. Add the Agent-to-UI Parameter Registry
Location: `server/features_server.py`
Date: 2026-08-05
Status: Reassigned

Implementation decision:
- Store metadata for existing visible Shiny inputs without adding a second
  application-state source.
- Reassigned on 2026-09-03 to Agent PR C after structured facet exposure; see
  the [development roadmap](../../../plans/development-roadmap.md#agent-pr-c-features-ui-update-and-render).
  Keep it outside the current template-delegation PR.

Action items:
- [ ] Define `FEATURE_INPUT_REGISTRY` in `features_server.py`.
- [ ] Add entries for feature, table, log controls, rotation, Group By,
  annotation, Together, and Multiple.
- [ ] Record each input ID, update function/type, and validation metadata.
- [ ] Match registry names to the semantic keys returned by
  `get_features_inputs()`.

Commit boundary:
Add registry metadata for future agent-driven `ui.update_*()` calls without
changing plotting behavior.

### Task 2. Extract the Features Input Snapshot
Location: `server/features_server.py`, `tests/`
Date: 2026-08-05
Status: Complete

Implementation decision:
- Read the existing Features controls and assemble the current core histogram
  parameters before any template-specific conversion.
- Use the existing Features input IDs as the current UI contract. Do not rename
  the `h1`-prefixed inputs in this adapter refactor; UI naming standardization
  belongs to the later Features UI exposure development.
- Build the current core histogram parameters in the input calculation so the
  renderer does not reconstruct them separately. Task 4 owns the translation
  to exact template keys such as `Table_`, `Take_X_Log`, `Take_Y_Log`, and
  `Group_by`.

Input calculation contract:
- The returned flat dictionary contains the current core keywords `feature`,
  `layer`, `x_log_scale`, `y_log_scale`, `group_by`, `together`, and
  `multiple`.
- `group_by` is `None`, `multiple` is `"stack"`, and `together` is `False`
  when their controls are disabled. The backend ignores `multiple` unless
  Together is enabled.
- The `layer` value is normalized to `None` when `h1_layer()` is
  `"Original"`.
- `x_axis_label_rotation` contains the display-only value from `feat_slider`
  and is removed before the remaining parameters are passed to the core
  histogram function.

Action items:
- [x] Define `get_features_inputs()` as a reactive calculation.
- [x] Read `h1_feat`, `h1_layer`, `h1_log_x`,
  `h1_log_y`, `feat_slider`, and
  `h1_group_by_check`.
- [x] Read `h1_anno`, `h1_together_check`, and
  `h1_together_drop` when the dynamic controls are available.
- [x] Assemble the current core histogram parameters in the input calculation
  without changing the plotting backend.

Evidence:
- `get_features_inputs()` reads the current `h1`-prefixed UI inputs and
  returns one flat parameter dictionary containing the current core histogram
  parameters plus display metadata.
- `spac_Histogram_1()` passes those parameters directly to the existing core
  histogram call and applies the display-only rotation afterward.
- UI input names and template keyword conversion remain unchanged for the
  later UI-exposure and template-adapter tasks.

Commit boundary:
Extract current Features input processing without changing the plotting
backend.

### Task 1. Use the Canonical AnnData Source
Location: `server/features_server.py`
Date: 2026-08-06
Status: Complete

Implementation decision:
- Use `shared["adata_main"].get()` as the Features AnnData source.
- Keep the projected reactive values as read-only compatibility projections
  for existing consumers and UI choices.

Action items:
- [x] Define `get_adata()` to return `shared["adata_main"].get()`.
- [x] Compare the current reconstructed Features inputs with the
  corresponding `adata_main` fields and document any discrepancy before
  switching the renderer.
- [x] Change the Features renderer to obtain AnnData through `get_adata()`.
- [x] Preserve the current write contract: loading, subsetting, and restore
  replace `adata_main`, while `update_parts()` derives the projections.
- [x] Add a missing-data guard before reading Features inputs or rendering.

Evidence:
- On `dev_example.pickle` (4,825 × 33), the reconstruction matches
  `adata_main` for `X`, `obs`, `var`, and `layers` values, indexes, and dtypes.
- The reconstruction omits `obsm`, `uns`, and `obsp`, so it is equivalent only
  for the current Histogram field contract, not as a complete AnnData object.
- At branch commit `b9f63d2` (PR #85), `features_server.py` still constructs
  AnnData from the projected values and calls
  `spac.visualization.histogram()` directly; the missing-data guard remains
  after construction. The canonical AnnData source switch is complete; the
  direct core call is intentionally retained until the later template-adapter
  tasks.
- Commit `d68a0de` now reads `shared["adata_main"]` through
  `get_adata()` and returns early before reading histogram inputs when the
  canonical object is missing.

Commit boundary:
Use the canonical AnnData source for Features without changing the current UI
or plotting behavior.
