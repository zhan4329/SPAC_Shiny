# Decisions

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
