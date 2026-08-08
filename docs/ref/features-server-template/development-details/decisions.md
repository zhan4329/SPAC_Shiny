# Decisions

The dependency baseline decision is maintained in the prerequisite
[compatibility PR decision log](../../../chore/pin-spac-to-pr-433/development-details/decisions.md).

### D6. Reclassify Former Overview Issues
Date: 2026-08-07

Decision:
- The question of setting `shared["X_data"]` to `None` when `adata` is
  missing is outside the Features template boundary. Leave it out of the
  active adapter tasks and revisit it with broader data-input changes.
- The Features renderer will use `shared["adata_main"]` as its AnnData source;
  projected component values remain available only for UI-choice updates.
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
- Implement the adapter cleanly for the current SPAC version and Issue #73
  workflow.
- Mention `ffa8644` in the PR description.
- Add Mousumi as a co-author if her design or code is materially reused.

Rationale:
The branch combines the adapter prototype with later histogram-control UI,
facet exposure, dependency changes, and unrelated updates. Using it as a
reference preserves the useful design while keeping the adapter refactor
focused.
