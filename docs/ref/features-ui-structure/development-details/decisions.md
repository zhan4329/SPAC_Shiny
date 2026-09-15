# Decisions

### D5. Adopt Shared-First Visualization Styling
Date: 2026-09-15

Decision:
Promote the CSS issue to Task 5. Load application-wide and reusable
visualization styles once at the app root, keep Data Input-specific rules with
that page, and make Features the first visualization consumer. Defer migration
of Nearest Neighbor, Feature vs Annotation, and Ripley L until the shared
contract has been validated through Features.

Rationale:
The existing `utils/styling.py` provides a natural shared home, but its broad
styles currently reach the application indirectly through Data Input. Making
ownership explicit avoids that hidden dependency and gives later tab
migrations a reusable contract without duplicating their current inline CSS.

### D4. Replace Dynamic Group By UI in the Current Refactor
Date: 2026-09-15

Decision:
Promote the dynamic-control ownership issue to Task 4. Declare Annotation,
Plot Together, and Stack Type statically in `features_ui.py`, use nested
`panel_conditional()` visibility, update Annotation choices through the
central effect updater, and remove the corresponding Features server
insertion/removal lifecycle. Leave the later Group By/Together/Facet
interaction contract outside this task.

This supersedes D3's preservation of `insert_ui()` / `remove_ui()` and the
earlier one-file boundary only for the focused Task 4 cleanup.

Rationale:
PR #66 provides an accepted SPAC Shiny precedent for moving stable dependent
controls from server insertion into conditional UI. The feature-template
branches instead retained the dynamic lifecycle and duplicated insertion
targets, so they are not suitable implementation references. Static control
ownership removes unnecessary reactive state and DOM mutation without
requiring Facet behavior in this refactor.

### D3. Implement the UI Refactor as Three Sequential Tasks
Date: 2026-09-15

Decision:
Divide the development into composition extraction, control-section
organization, and focused verification. Preserve the existing server-side
`insert_ui()` and `remove_ui()` mechanism throughout these tasks. Track a
possible move to static UI-owned `panel_conditional()` controls as an open
issue for a later decision rather than expanding the active refactor.

Rationale:
The first two tasks are independently reviewable one-file presentation
changes, while the third provides a clear regression boundary. Replacing the
dynamic controls would also change `features_server.py`, reactive behavior,
and the current scope, so it requires a separate design decision after the
agreed UI structure has been verified.

### D2. Base the UI Refactor on Dev and Keep Its Helper Local
Date: 2026-09-15

Decision:
Create `ref/features-ui-structure` from `dev` and target `dev` directly. Keep
the current `output_plot` renderer in this PR; when PR #86 is rebased after
the UI change merges, apply its `output_image` change inside the extracted
plot-panel builder. Keep the disclosure helper local to `features_ui.py`
until a second tab demonstrates a shared contract.

This supersedes D1 only where D1 named `ref/features-server-template` as the
base and the canonical image output as the preserved baseline. D1's UI-only
scope, component structure, and preserved functional identifiers remain in
effect.

Rationale:
The UI composition is logically independent of the template adapter. Basing
it on `dev` gives the PR an independent review and merge path; the two branches
overlap only at the plot-output call. The guide's `utils/ui_components.py`
examples are intended for controls reused across visualizations, while the
current disclosure helper has only one module consumer. Keeping it local
avoids expanding the one-file PR with speculative shared API.

### D1. Separate UI Structure From Facet Behavior
Date: 2026-09-15

Decision:
Create a focused `ref/features-ui-structure` development from
`ref/features-server-template`. Change only `ui/features_ui.py` and adopt the
Issue #73 composition pattern: a small public UI function, separate control
and plot builders, always-visible core parameters, collapsible plot and figure
sections, and a reusable local disclosure helper. Preserve existing IDs,
defaults, insertion targets, server behavior, and canonical image output.

Rationale:
The current flat UI can be reorganized independently of facet semantics. A
small presentation-only PR is feasible within the available development
window, gives reviewers one coherent change, and establishes the intended
location for later facet controls without exposing incomplete functionality or
mixing UI organization with server-state changes.
