# Features UI Structure Architecture

This document defines the UI-only organization for `ui/features_ui.py`. It
adapts the section-based module pattern in the SPAC template integration guide
to the controls that the Features tab currently exposes. It does not change
the Features server, plot execution, or renderer.

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
| Annotation insertion target | `main-h1_dropdown` |
| Together insertion target | `main-h1_check` |
| Stack-type insertion target | `main-h1_together_drop` |
| X log | `h1_log_x` |
| Y log | `h1_log_y` |
| X-label rotation | `feat_slider` |
| Render action | `go_h1` |
| Download UI | `download_histogram1_button_ui` |
| Plot output | `spac_Histogram_1` |

These identifiers and their current defaults remain unchanged.

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

The collapsible plot section contains `h1_group_by_check`, the three existing
dynamic insertion targets, `h1_log_x`, and `h1_log_y`. The targets remain in
the rendered DOM so the existing server selectors can insert and remove the
Annotation, Plot Together, and Stack Type controls without modification.

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
    ├── existing analytical input IDs ───────────────┐
    ├── existing dynamic insertion targets ──────┐   │
    └── existing action and output IDs ────────┐  │   │
                                               ▼  ▼   ▼
                                     unchanged features_server.py
                                               │
                                               ▼
                                          current plot result
```

The refactor changes presentation structure only. It does not change the
current server input reads, dynamic insertion effects, button-gated plotting,
dataframe publication, download behavior, or returned Matplotlib figure.

## Verification Boundary

Verification should establish that the module imports and constructs its UI,
that all established identifiers occur once, and that the disclosure sections
show the intended controls. Direct Shiny verification should confirm Group By
insertion and removal, Together and Stack Type behavior, ordinary and grouped
rendering, repeated rendering, plot presentation, and dataframe download.

Facet behavior, responsive plot geometry, canonical title or legend
containment, renderer changes, and server-side parameter tests are outside
this UI-only architecture. When the template-server PR is later rebased, its
`output_plot`-to-`output_image` change should be applied inside
`_plot_panel()` without changing this composition.
