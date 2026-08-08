# Task Details

## Development

### Task 7. Add Focused Adapter Tests
Location: `server/features_server.py`, `tests/`
Date: 2026-08-05
Status: Planned

Implementation decision:
- Test the adapter boundaries against the current SPAC dev contract without
  introducing full end-to-end Shiny tests.

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
Location: `server/features_server.py`
Date: 2026-08-05
Status: Planned

Implementation decision:
- Keep dynamic UI effects separate from AnnData access and template execution.

Action items:
- [ ] Run one focused Features UI verification covering Group By and Together
  insertion/removal, `input.go_h1`-gated rendering, plotting options, and
  dataframe download.

Commit boundary:
Keep the existing Features reactive behavior isolated from template
execution and verify the non-facet user flow.

### Task 5. Delegate Histogram Execution to the Template
Location: `server/features_server.py`
Date: 2026-08-05
Status: Planned

Implementation decision:
- Register the canonical AnnData object returned by `get_adata()`
  through the existing memory registry.

Action items:
- [ ] Import the histogram template and memory-registry helpers.
- [ ] Register the object returned by `get_adata()` before template
  execution.
- [ ] Call `run_from_json(..., save_to_disk=False, show_plot=False)`
  with the built parameter dictionary.
- [ ] Store the returned dataframe in `shared["df_histogram1"]` and
  return the returned figure.
- [ ] Unregister the memory object in a `finally` block.
- [ ] Remove the direct `spac.visualization.histogram()` call from
  the Features renderer.

Commit boundary:
Move the Features histogram execution from the bare SPAC visualization API
to the SPAC histogram template.

### Task 4. Build the SPAC Template Parameter Dictionary
Location: `server/features_server.py`, `tests/`
Date: 2026-08-05
Status: Planned

Implementation decision:
- Keep semantic Features inputs separate from the template’s parameter names.

Action items:
- [ ] Define pure `build_template_params(inputs, virtual_path)`
  conversion.
- [ ] Map the current inputs to the template keys
  `Upstream_Analysis`, `Feature`, `Table_`,
  `Take_X_Log`, `Take_Y_Log`, `Group_by`,
  `Together`, `Multiple`, and `X_Axis_Label_Rotation`.
- [ ] Add current-dev defaults for `Plot_By`, `Annotation`,
  `Bins`, `Stat`, `Element`, `Max_Groups`,
  `Facet`, `Facet_Ncol`, and figure settings not exposed by
  the current UI.
- [ ] Set `Facet` to its non-facet default without exposing facet
  controls in this task.
- [ ] Pass `"None"` or the template’s documented default tokens where
  the template requires them.

Commit boundary:
Create and test the pure semantic-state-to-template-payload conversion.

### Task 3. Add the Agent-to-UI Parameter Registry
Location: `server/features_server.py`
Date: 2026-08-05
Status: Planned

Implementation decision:
- Store metadata for existing visible Shiny inputs without adding a second
  application-state source.

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
Status: Planned

Implementation decision:
- Read the existing Features controls and return stable semantic names before
  any template-specific conversion.

Action items:
- [ ] Define `get_features_inputs()` as a reactive calculation.
- [ ] Read `h1_feat`, `h1_layer`, `h1_log_x`,
  `h1_log_y`, `feat_slider`, and
  `h1_group_by_check`.
- [ ] Read `h1_anno`, `h1_together_check`, and
  `h1_together_drop` when the dynamic controls are available.
- [ ] Return explicit defaults for grouping, Together, and Multiple when
  Group By is disabled.
- [ ] Return semantic keys independent of SPAC template parameter names.

Commit boundary:
Extract current Features input processing without changing the plotting
backend.

### Task 1. Use the Canonical AnnData Source
Location: `server/features_server.py`
Date: 2026-08-06
Status: Planned

Implementation decision:
- Use `shared["adata_main"].get()` as the Features AnnData source.
- Keep the projected reactive values for UI choices unchanged.

Action items:
- [ ] Define `get_adata()` to return `shared["adata_main"].get()`.
- [ ] Change the Features renderer to obtain AnnData through `get_adata()`.
- [ ] Confirm the reconstructed component values remain projected UI-choice
  state rather than the renderer's AnnData source.
- [ ] Add a missing-data guard before reading Features inputs or rendering.

Commit boundary:
Use the canonical AnnData source for Features without changing the current UI
or plotting behavior.
