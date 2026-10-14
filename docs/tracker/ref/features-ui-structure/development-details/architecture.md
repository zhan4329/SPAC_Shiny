# Features UI Structure Architecture

This document defines the Features UI organization and focused control-
ownership cleanup. It adapts the section-based module pattern in the SPAC
template integration guide while replacing server-inserted Group By controls
with static conditional UI. It does not change styling, plot execution, or the
renderer.

## Baseline

The `dev` branch renders the entire Features panel from one `features_ui()`
function. That function owns the control column, the dynamic Group By
insertion targets, the render and download actions, and the plot output in one
nested expression.

The existing server depends on these UI identifiers:

| Role | Existing identifier |
| --- | --- |
| Feature | `h1_feat` |
| Table | `h1_layer` |
| Grouping enabled | `h1_group_by_check` |
| Annotation | `h1_anno` |
| Together | `h1_together_check` |
| Stack type | `h1_together_drop` |
| X log | `h1_log_x` |
| Y log | `h1_log_y` |
| X-label rotation | `feat_slider` |
| Render action | `go_h1` |
| Download UI | `download_histogram1_button_ui` |
| Plot output | `spac_Histogram_1` |

These functional identifiers and their current defaults remain unchanged. The
three baseline insertion-target IDs are removed with the dynamic lifecycle.

## Target Composition

The public function becomes a small composition boundary, with private
module-level builders separating the controls from the plot output:

```text
features_ui()
└── Features nav panel and card
    └── row
        ├── 3-column control area → _controls_panel()
        │   ├── Core Parameters (always visible)
        │   ├── Plot Configuration (collapsible)
        │   ├── Figure Configuration (collapsible)
        │   └── Render and download actions
        └── 9-column result area → _plot_panel()

_collapsible_section()
└── disclosure checkbox + panel_conditional content
```

`features_ui()` owns only the outer Features navigation, card, and 3/9-column
composition. `_controls_panel()` owns the ordered controls and action area.
`_plot_panel()` owns the existing plot output. The local
`_collapsible_section()` helper implements the repeated disclosure pattern
without creating a shared cross-tab abstraction.

## Section Ownership

### Core Parameters

The always-visible section contains `h1_feat` and `h1_layer`. These identify
the data to visualize and should remain immediately available.

### Plot Configuration

The collapsible plot section contains `h1_group_by_check`, `h1_log_x`, and
`h1_log_y`. A condition tied to Group By contains the static `h1_anno` and
`h1_together_check` controls; a nested condition tied to Together contains
`h1_together_drop`. Annotation choices remain dataset-driven through the
central effect updater.

The disclosure control changes only visibility. It does not normalize,
clear, or update any analytical input value. The existing Shiny inputs remain
the application state consumed by `features_server.py`.

### Figure Configuration

The collapsible figure section contains the existing `feat_slider` X-axis
label rotation control. Width, height, DPI, font size, and other unexposed
Histogram parameters are not added merely to fill this section; later
developments will add them when their product and template contracts are
accepted.

### Actions and Result

The existing `go_h1` action remains after the parameter sections and adopts
the guide's full-width action styling. The download UI stays directly below
it. `_plot_panel()` continues to return `ui.output_plot()` for
`spac_Histogram_1` with `width="100%"` and `height="60vh"`; responsive sizing
and renderer changes are separate developments.

## UI and Server Boundary

```text
Features UI composition
    ├── stable analytical input IDs ────────────────┐
    ├── conditional visibility ─────────────────┐   │
    └── existing action and output IDs ──────┐   │   │
                                            ▼   ▼   ▼
                                  current render behavior
                                            │
                                            ▼
                                      current plot result
```

The refactor changes presentation structure and removes the dynamic insertion
effects. It does not change button-gated plotting, dataframe publication,
download behavior, or the returned Matplotlib figure.

## Verification Boundary

Verification should establish that the module imports and constructs its UI,
that all established functional identifiers occur once, and that the
disclosure sections show the intended controls. Direct Shiny verification
should confirm Group By and Together conditional visibility, annotation-choice
updates, ordinary and grouped rendering, repeated rendering, plot
presentation, and dataframe download.

Facet behavior, responsive plot geometry, canonical title or legend
containment, renderer changes, and server-side parameter tests are outside
this architecture. When the template-server PR is later rebased, its
`output_plot`-to-`output_image` change should be applied inside
`_plot_panel()` without changing this composition.
