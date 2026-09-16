# Decisions

The dependency baseline decision is maintained in the prerequisite
[compatibility PR decision log](../../../chore/pin-spac-to-pr-433/development-details/decisions.md).

### D21. Record PR #86 Merge
Date: 2026-09-16

Decision:
PR #86 merged into `dev`; this development is complete.

### D20. Close the Adapter PR and Reassign Follow-Up Work
Date: 2026-09-03

Decision:
Treat the [Features facet plan](../../../plans/pr-plans/1-features-facet-pr-plan.md) and
[development roadmap](../../../plans/development-roadmap.md) as the
authoritative future sequence. Close the current development after PR #86
review and merge. Reassign Task 3 to Agent PR C, Task 8 to the plan's PR 3,
and Task 9 to its PR 4 without changing their unexecuted action items.

Rationale:
The template-delegation implementation is complete and committed. Keeping its
review boundary closed makes PR #86 easier to evaluate, while the canonical
plans give facet, agent, and layout work distinct future owners without
duplicating their details in this overview.

### D19. Deliver the Canonical PNG Directly
Date: 2026-09-02

Decision:
Use `render.image(delete_file=True)` with the matching image output for the
Features histogram. Write the canonical PNG bytes to a uniquely named
temporary file, let Shiny remove successfully delivered files, and keep the
rare pre-return cleanup edge case out of the server's ordinary path.

Rationale:
Direct image delivery avoids reconstructing a Matplotlib wrapper that can
mutate the canonical layout. Shiny owns successful-file cleanup, while the
simpler server flow remains understandable to the project's active
data-science developers. Responsive sizing remains independent Task 9 work.

### D18. Resolve the Renderer Boundary Before Layout Work
Date: 2026-09-02

Decision:
Promote the `render.plot` versus `render.image` question to active Task 10 and
resolve it in the current SPAC Shiny PR before Tasks 8 and 9.

Rationale:
The PNG renderer is a newly introduced transport and lifecycle concern, not a
template- or browser-layout concern. Resolving it first prevents later layout
work from being built around a temporary wrapper and gives responsive sizing
a stable renderer boundary.

### D17. Split Canonical Clipping From Responsive Delivery
Date: 2026-09-02

Decision:
Assign template-generated title and legend containment to Task 8 in
SCSAWorkflow. Assign proportional full-width preview delivery and the
`render.image` decision to Task 9 in SPAC Shiny.

Rationale:
Clipping loses information while the canonical image is created, whereas
responsive delivery controls how an already-created image occupies the
browser. Either can fail independently, so they need separate implementation
and verification boundaries even though both affect the visible layout.

### D16. Separate Unimplemented Layout Work From Task 6
Date: 2026-09-01

Decision:
Keep Task 6 limited to its completed experiments and implemented canonical-PNG
adapter. Combine template-owned text containment and proportional full-width
Shiny presentation in Task 8 because together they define whether the user can
see the complete histogram. Keep their package and Shiny commits separate.

Rationale:
The canonical image must contain all information before the UI can present it,
and the UI must then preserve its aspect ratio while deriving height from the
available width. These are different implementation layers but one observable
layout outcome. They have not yet been implemented, so moving them out keeps
Task 6 concise without revising its checked execution history.

### D15. Freeze Template Geometry Before Shiny Rendering
Date: 2026-09-01

Decision:
Complete the rendering correction in Task 6 and the current template-refactor
PR. Keep the Histogram template's 300-DPI default and `render.plot`, but
serialize the completed figure without tight cropping and display a
non-mutating wrapper around those PNG bytes.

Rationale:
Shiny 0.10.2 uses Matplotlib DPI while fitting a returned figure to its CSS
plot area, so directly returning the 300-DPI template figure changes the
relative text scale and can clip content. An 80-DPI adapter override improves
the preview but lowers the canonical artifact resolution and conflicts with
future user-controlled figure settings. The PNG-byte boundary preserves the
template layout, aligns with PR #76's cache representation and the restored
PNG-download work, and leaves those broader features outside this PR.

### D14. Defer Log X Feedback to UI Exposure
Date: 2026-09-01

Decision:
Move Task 6 finding F6.1 to the coordinated Features UI-exposure work in
[Future work](../../../plans/future-work.md#deferred-ui-work).

Rationale:
The existing adapter passes the requested value correctly, while explaining
or disabling an unavailable control is a broader UI-state concern.

### D13. Defer Group By Control Placement to UI Exposure
Date: 2026-09-01

Decision:
Move Task 6 finding F6.2 to the coordinated Features UI-exposure work in
[Future work](../../../plans/future-work.md#deferred-ui-work).

Rationale:
Control placement is a UI-organization concern and does not affect the
template-adapter contract being reviewed in this development.

### D12. Use a Narrow Reactive Template-Adapter Lifecycle
Date: 2026-09-01

Decision:
Adopt the reactive and resource lifecycle recorded in
[Architecture](./architecture.md#reactive-and-resource-lifecycle).

Rationale:
It preserves the established reactive organization while separating resource
cleanup from exception policy without adding another abstraction.

### D11. Let the Histogram Template Own Unexposed Defaults
Date: 2026-09-01

Decision:
Send current Features UI values and the explicit feature-mode and non-facet
invariants in the adapter payload. Omit values that only duplicate defaults
already supplied by `histogram_template.run_from_json()`.

Rationale:
The Shiny adapter should express current user state and intentional product
constraints. Leaving unexposed defaults with the template avoids duplicate
sources of truth and lets later UI developments add each value when its
control is introduced.

### D10. Defer Comprehensive Adapter Tests to SWE Verification
Date: 2026-09-01

Decision:
Use direct Shiny app verification for the current Features adapter development
and postpone Task 7 automated adapter tests to the specialized SWE stage.
Continue to add focused tests when stable reusable utility behavior warrants
them.

Rationale:
The input-to-template mapping is still evolving, while SPAC Shiny does not
currently treat unit tests as a strict review blocker. Runtime verification
lets development continue against the actual reactive application without
committing brittle mapping-name tests that the SWE stage would replace.

### D9. Postpone the Agent-to-UI Parameter Registry
Date: 2026-08-22

Decision:
Postpone Task 3 until the template parameter contract is established and the
later UI-exposure naming is stable.

Rationale:
The registry would otherwise duplicate the current input-to-parameter mapping
and encode UI IDs before the template boundary is finalized. Deferring it
allows the registry to expose one stable agent-facing contract and avoids
rework when UI names or template mappings change.

### D8. Validate the Existing Features Data Boundary
Date: 2026-08-08

Finding:
Compare the current reconstructed Features object with the canonical object
using `dev_example.pickle` (4,825 × 33). `X`, `obs`, `var`, and `layers` match
in values, indexes, and dtypes. The reconstruction omits `obsm`, `uns`, and
`obsp`.

Decision:
Treat the current reconstruction as field-equivalent for the existing
Histogram inputs, not as a complete AnnData equivalent. Add the missing-data
guard before switching the renderer, then pause before changing its source.

Rationale:
The current Histogram path uses only the fields that matched, but the guard
currently runs after AnnData construction and cannot protect missing or stale
projection values.

### D7. Treat Component Reactives as Derived Compatibility State
Date: 2026-08-08

Decision:
- Treat `shared["adata_main"]` as the AnnData state written by data loading,
  subsetting, and restore operations.
- Treat `X_data`, `obs_data`, `var_data`, and `layers_data` as read-only
  projections maintained by `update_parts()` for existing consumers.
- Use `adata_main` for the new Features template boundary without removing or
  independently rewriting the projections in this development.

Evidence:
- `data_input_server.adata_filter()` writes loaded data to `adata_main`.
- `effect_update_server.subset_stratification()` and
  `restore_to_master()` replace `adata_main`.
- `data_input_server.update_parts()` derives the component projections.
- No other current server writes those component reactives independently.

Rationale:
The projections are an active compatibility interface, not deprecated state,
but they are not a second source of truth. Keeping this distinction allows
the Features adapter to use the complete AnnData object while preserving the
existing server consumers.

### D6. Reclassify Former Overview Issues
Date: 2026-08-07

Decision:
- The question of setting `shared["X_data"]` to `None` when `adata` is
  missing is outside the Features template boundary. Leave it out of the
  active adapter tasks and revisit it with broader data-input changes.
- The Features renderer will use `shared["adata_main"]` as its AnnData source;
  projected component values remain available for existing consumers and
  UI-choice updates.
  Task 1 owns implementation and missing-data verification of this boundary.

Rationale:
The first question does not affect the new renderer once it stops
reconstructing AnnData. The second is the source-of-truth decision for this
refactor and must remain explicit while implementation is still pending.

### D5. Own the Histogram Template Contract in the Adapter
Date: 2026-08-07

Decision:
Track Histogram template import, parameter/default, and in-memory return
contract checks in adapter Tasks 4, 5, and 7.

Rationale:
These checks validate the boundary that this development is introducing when
the Features server delegates from `spac.visualization.histogram()` to the
current-dev Histogram template. They are not required for the prerequisite
dependency pin or the existing Ripley/Nearest Neighbor callers.

### D4. Track the refactor as seven commit-sized tasks
Date: 2026-08-05

Decision:
Replace the open issue checklist with seven numbered development tasks in
`task-details.md`. The former issues are covered by those tasks.

### D3. Verify the AnnData source before changing it
Date: 2026-08-05

Decision:
Compare the current reconstructed AnnData with `shared["adata_main"]` before
refactoring. Use the shared object if equivalent; document any discrepancy
before choosing another source.

### D2. Use a thin parameter registry for agent-driven UI updates
Date: 2026-08-05

Decision:
Add a small parameter registry that maps stable semantic parameter names to
Shiny input IDs and their corresponding update functions. Keep the visible
Shiny inputs as the source of truth instead of introducing a separate full
application-state dictionary at this stage.

Details:
- Let the agent submit validated parameter updates through the registry.
- Apply updates with the appropriate `ui.update_*()` function.
- Allow the updated values to return through Shiny's normal reactive cycle
  before rendering the plot.
- Keep the registry small enough to expand later for JSON or CLI integration.

Rationale:
This keeps agent updates visible and user-friendly while avoiding duplicated
state during the current template-adapter refactor. A larger session-state
model can be introduced later if CLI updates, saved configurations, or
undo/redo become requirements.

### D1. Use Mousumi's contribution as a reference
Date: 2026-08-05

Decision:
Use Mousumi's `ref/features-template` contribution as a reference for the
template-adapter design rather than cherry-picking the full branch or using
`git cherry-pick -n ffa8644` as the default workflow.

Details:
- Start from the current `ref/features-server-template` branch.
- Implement the adapter cleanly for the current SPAC version and the
  [Issue #73 workflow](../../../../issues/issue-73.md).
- Mention `ffa8644` in the PR description.
- Add Mousumi as a co-author if her design or code is materially reused.

Rationale:
The branch combines the adapter prototype with later histogram-control UI,
facet exposure, dependency changes, and unrelated updates. Using it as a
reference preserves the useful design while keeping the adapter refactor
focused.
