# Task Details

## Development

### Task 5. Establish Shared Visualization Styling for Features
Location: `app.py`, `utils/styling.py`, `ui/data_input_ui.py`,
`ui/features_ui.py`
Date: 2026-09-15
Status: Remaining

Implementation decision:
- Adopt a shared-first CSS structure: load application-wide styles once at
  the app root, retain Data Input-specific rules with that page, and make
  Features the first consumer of reusable visualization styles.

Action items:
- [ ] Separate application-wide style loading from Data Input page ownership
  and load the shared styles once from the application root.
- [ ] Keep Data Input-specific styles available without reinjecting global or
  shared component styles through `data_input_ui()`.
- [ ] Add reusable, semantically scoped visualization control and result-panel
  styles to `utils/styling.py`.
- [ ] Apply those shared classes to the Features controls and plot panels.
- [ ] Align stable Features presentation rules with the established
  visualization style, including panel surfaces, borders, radii, padding, and
  control spacing.
- [ ] Keep fixed tab geometry, overflow rules, plot dimensions, and
  tab-specific tooltip behavior outside the shared style contract.
- [ ] Verify that Data Input remains styled, Features receives the shared
  styles, styles are injected only once, and other visualization tabs are
  unaffected.
- [ ] Run focused syntax/import checks and `git diff --check`, then review the
  four-file diff.

Commit boundary:
Establish shared style ownership and adopt it in Features without migrating
Nearest Neighbor, Feature vs Annotation, or Ripley L in this task.

### Task 4. Replace Dynamic Group By UI With Static Conditions
Location: `ui/features_ui.py`, `server/features_server.py`,
`server/effect_update_server.py`
Date: 2026-09-15
Status: Remaining

Implementation decision:
- Follow the accepted Feature vs Annotation pattern from PR #66: declare
  stable controls in the UI, use conditional visibility for dependent
  controls, and keep dataset-driven choice updates in the central effect
  updater.

Action items:
- [ ] Declare `h1_anno` and `h1_together_check` inside the Group By
  `panel_conditional()` with their current labels and defaults.
- [ ] Declare `h1_together_drop` inside a nested condition tied to
  `h1_together_check`, preserving its choices and `"stack"` default.
- [ ] Remove `main-h1_dropdown`, `main-h1_check`, and
  `main-h1_together_drop` from `features_ui.py`.
- [ ] Add `h1_anno` to the existing annotation-choice update effect in
  `effect_update_server.py`.
- [ ] Remove `histogram_ui_initialized` and the Group By and Stack Type
  insertion/removal effects from `features_server.py`.
- [ ] Preserve the current renderer gating and input IDs without adding Facet
  controls or defining the later Group By/Together/Facet interaction contract.
- [ ] Verify module syntax, unique rendered IDs, annotation-choice updates,
  conditional visibility, and ordinary and grouped render paths.
- [ ] Run `git diff --check` and review the focused three-file diff.

Commit boundary:
Replace the dynamic Group By control lifecycle with static conditional UI and
central choice updates without changing histogram parameters or adding Facet
behavior.

### Task 3. Verify the UI Refactor and Prepare It for Review
Location: Features UI/server files, shared styling files, SPAC Shiny runtime
Date: 2026-09-15
Status: Remaining

Implementation decision:
- Verify the completed UI structure, control-ownership cleanup, and shared
  styling through focused static checks and direct Shiny interaction before
  review.

Action items:
- [ ] Confirm `ui/features_ui.py` imports and constructs successfully.
- [ ] Confirm every preserved functional input and output ID occurs exactly
  once and retains its established default.
- [ ] Run the focused syntax/import check and `git diff --check`.
- [ ] Verify the initial disclosure state and opening and closing the Plot
  Configuration and Figure Configuration sections.
- [ ] Verify Group By conditional visibility, Plot Together behavior, Stack
  Type conditional visibility, and annotation-choice updates.
- [ ] Verify ordinary and grouped rendering, repeated rendering, plot display,
  and dataframe download.
- [ ] Verify shared styles load once, Data Input remains styled, and Features
  uses the intended reusable visualization classes.
- [ ] Review the final diff against the focused scope and correct only
  regressions introduced by this refactor.
- [ ] Commit the reviewed UI refactor and record the verification evidence.

Commit boundary:
Complete and verify the focused refactor without adding facet behavior,
renderer changes, responsive sizing, cross-tab style migration, or unrelated
polish.

### Task 2. Organize the Features Controls Into Sections
Location: `ui/features_ui.py`
Date: 2026-09-15
Status: Complete

Implementation decision:
- Organize the existing controls into the agreed always-visible and
  collapsible sections using a local disclosure helper while preserving the
  current server-owned dynamic Group By behavior.

Action items:
- [x] Add a private local `_collapsible_section()` helper.
- [x] Keep Feature and Table in an always-visible Core Parameters section.
- [x] Put Group By, its three existing insertion targets, and the X/Y log
  controls in a collapsible Plot Configuration section.
- [x] Put X-axis label rotation in a collapsible Figure Configuration section.
- [x] Add only the two presentation-only disclosure input IDs; keep them
  independent of analytical state and server logic.
- [x] Keep Render Plot and the download UI below the parameter sections.
- [x] Apply the agreed full-width styling to the Render Plot action.
- [x] Preserve every existing functional identifier, default, and dynamic
  insertion target.

Evidence:
- Reviewed and committed as `7251e2f`. Focused checks passed; see
  `implementation-log.md`.

Commit boundary:
Add the agreed section and disclosure organization without moving dynamic
control creation out of `features_server.py` or changing analytical behavior.

### Task 1. Extract the Features UI Composition
Location: `ui/features_ui.py`
Date: 2026-09-15
Status: Complete

Implementation decision:
- Establish the helper-based control-versus-result composition before adding
  collapsible section behavior.

Action items:
- [x] Reduce `features_ui()` to the outer Features navigation, card, and row
  composition.
- [x] Add a private `_controls_panel()` builder containing the current controls
  and actions without changing their behavior.
- [x] Add a private `_plot_panel()` builder containing the current
  `ui.output_plot()` call and plot-container spacing.
- [x] Change the control/result layout from 2/10 columns to the agreed 3/9
  columns.
- [x] Preserve the current control order, IDs, defaults, insertion targets,
  action/output IDs, and plot dimensions during the extraction.
- [x] Confirm the module imports and the composed UI can be constructed before
  beginning Task 2.

Evidence:
- Reviewed and committed as `14e215d`
  (`refactor(features): extract UI composition`). Focused checks passed; see
  `implementation-log.md`.

Commit boundary:
Extract the local composition boundaries and adopt the 3/9 layout without
adding disclosure behavior or changing the server contract.
