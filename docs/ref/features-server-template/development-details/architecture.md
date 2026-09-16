# Features Server Architecture

This document describes the partial architecture delivered by the current
Features template-adapter refactor. The refactor preserves the existing
Features interaction model while replacing its direct core Histogram call
with the standard SPAC template workflow. It also establishes the semantic
input and template-adapter boundaries needed for later agent integration,
without implementing an agent, an agent-to-UI registry, or a new UI state
model in this development.

## Current Branch Baseline

- `app.py` owns the session-local shared reactive values, including the
  canonical AnnData object in `shared["adata_main"]` and the Features result
  dataframe in `shared["df_histogram1"]`.
- `data_input_server.adata_filter()`,
  `effect_update_server.subset_stratification()`, and
  `effect_update_server.restore_to_master()` replace
  `shared["adata_main"]`.
- `data_input_server.update_parts()` derives component projections and UI
  metadata from `adata_main`; `effect_update_server` uses that metadata to
  update the available Features choices.
- The Features branch already reads canonical AnnData through `get_adata()`
  and reads the current controls through `get_features_inputs()`.
- The renderer remains gated by the human `go_h1` action button and delegates
  execution to the Histogram template. Task 6 freezes the returned figure as
  canonical PNG bytes; completed Task 10 delivers those bytes directly
  through `render.image` as committed in `da242c6`.
- `utils/template_wrapper.py` provides the process-local memory registry used
  to pass in-memory AnnData objects to SPAC templates.

## Partial Architecture Goal

The current development changes only the Features data-to-execution boundary:

```text
Current:
  Features UI → semantic input snapshot → core histogram function

Target for this development:
  Features UI → semantic input snapshot → template payload
              → Histogram template → core histogram function
              → canonical PNG → temporary file → Shiny image output
```

The existing UI remains the input source of truth. Parameter changes do not
render automatically; a human click on `go_h1` captures the current data and
control values for one render. The template payload and memory-registry path
are transient execution values and are not application state.

This boundary prepares for a future agent to inspect and update stable
semantic Features parameters through the visible UI. The agent-to-UI registry
and agent render requests remain deferred until the Features UI names and
exposure are stable.

## Shared Data Ownership

```text
AnnData writers:
  data_input_server.adata_filter()               → shared["adata_main"]
  effect_update_server.subset_stratification()   → shared["adata_main"]
  effect_update_server.restore_to_master()       → shared["adata_main"]

Projection and choice metadata writer:
  data_input_server.update_parts()               → component reactives
                                                   and choice metadata

Features result writer:
  spac_Histogram_1() after successful execution  → shared["df_histogram1"]
```

`shared["adata_main"]` is the Features data source. `X_data`, `obs_data`,
`var_data`, and `layers_data` remain derived compatibility projections for
existing consumers and UI metadata; they are not alternate AnnData state.
The exact object returned by `get_adata()` is registered for template
execution without reconstruction or copying.

The known projection-clearing limitations remain broader data-input concerns
outside this Features adapter development.

## Component Structure

Features-specific helpers remain nested in `features_server()` to preserve
the repository's current server organization and avoid exposing a
single-caller template mapping as a module-level interface:

```text
features_server()
├── get_adata()                  reactive canonical-data reader
├── get_features_inputs()        reactive semantic input snapshot
├── build_template_params()      normal semantic-to-template conversion
├── spac_Histogram_1()           go_h1-gated template renderer
├── download_histogram1_df()     dataframe download
├── download_histogram1_button_ui()
├── histogram_reactivity()       existing Group By UI behavior
└── update_stack_type_dropdown() existing Together UI behavior
```

`build_template_params()` is a normal function because it reads no reactive
state. It receives explicit semantic values and a virtual path, then returns
the corresponding template payload. It is called during each render, but it
is not itself a reactive calculation or persistent state.

No additional `run_features_histogram()` abstraction is introduced in this
development. `spac_Histogram_1()` remains the single Features execution owner.

## State and Reactive Boundaries

The partial architecture distinguishes editable control state from a render
request and its result:

| State or event | Owner | Effect |
| --- | --- | --- |
| Canonical AnnData | `shared["adata_main"]` | Supplies data for the next render |
| Available choices | Derived shared reactives | Updates valid Features controls |
| Visible control values | Shiny inputs | Supplies parameters for the next render |
| Semantic Features values | `get_features_inputs()` | Normalizes current control values |
| Human render request | `input.go_h1` | Starts one render using current values |
| Memory-registry entry | Template adapter | Exists only during template execution |
| Canonical figure artifact | Task 6 display adapter | Preserves completed template geometry as PNG bytes |
| Figure result | Shiny image output | Displays the canonical PNG without reconstructing a figure |
| Dataframe result | `shared["df_histogram1"]` | Supports the download output |

```python
@reactive.calc
def get_adata():
    return shared["adata_main"].get()


@reactive.calc
def get_features_inputs():
    ...


def build_template_params(input_values, virtual_path):
    ...


@render.image(delete_file=True)
@reactive.event(input.go_h1, ignore_none=True)
def spac_Histogram_1():
    ...
```

Changes to AnnData or Features controls invalidate their derived reactive
state but do not render a new histogram. The displayed figure and dataframe
continue to represent the last successful render until `go_h1` is clicked
again. The renderer must treat the dictionary returned by
`get_features_inputs()` as read-only and must not mutate the cached reactive
value with operations such as `pop()`.

## Parameter Layers

### Semantic Features Input Contract

`get_features_inputs()` returns current application-level meaning rather than
template-specific names:

```python
{
    "feature": ...,
    "layer": ...,
    "x_log_scale": ...,
    "y_log_scale": ...,
    "group_by": ...,
    "together": ...,
    "multiple": ...,
    "x_axis_label_rotation": ...,
}
```

It normalizes disabled controls to the current behavior: `group_by=None`,
`together=False`, and `multiple="stack"` when grouping or Together is not
active. `layer=None` represents the UI's `"Original"` selection.

This semantic contract is the baseline a future agent-facing registry can
inspect and update through Shiny controls. It does not contain template keys,
file paths, or memory-registry identifiers.

### Histogram Template Payload

`build_template_params()` translates one semantic snapshot into the exact
current Histogram template contract:

```python
{
    "Upstream_Analysis": virtual_path,
    "Feature": input_values["feature"] or "None",
    "Table_": input_values["layer"] or "Original",
    "Group_by": input_values["group_by"] or "None",
    "Together": input_values["together"],
    "Take_X_Log": input_values["x_log_scale"],
    "Take_Y_log": input_values["y_log_scale"],
    "Multiple": input_values["multiple"],
    "X_Axis_Label_Rotation": input_values["x_axis_label_rotation"],
    "Plot_By": "Feature",
    "Facet": False,
}
```

The adapter owns this explicit Shiny-to-template mapping. The payload is
created after the AnnData virtual path exists, used once, and discarded after
execution. It includes current UI-controlled values and the explicit feature
mode and non-facet invariants. The Histogram template owns defaults for
controls that the current Features UI does not expose, including its current
300-DPI figure default.

## Render and Template Data Flow

```text
AnnData load/subset/restore
    ▼
shared["adata_main"] and derived choice metadata
    ▼
Features choices and visible Shiny input state
    │
    │ parameter changes alone do not render
    ▼
human clicks go_h1
    ▼
spac_Histogram_1()
    ├── get_adata()
    │     └── None → return without template execution
    └── get_features_inputs()
          └── capture current semantic values
    ▼
register_memory_object(canonical_adata)
    ▼
temporary memory:// virtual path
    ▼
build_template_params(semantic_values, virtual_path)
    ▼
histogram_template.run_from_json(
    json_path=params,
    save_to_disk=False,
    show_plot=False,
)
    ▼
(figure, dataframe)
    ▼
unregister_memory_object(virtual_path) in finally
    ▼
    ├── figure → canonical PNG without tight cropping
    │          → temporary PNG file → Shiny image output
    └── dataframe → shared["df_histogram1"] → download output
```

The final execution dependency is:

```text
SPAC Shiny Features server
    → SPAC Histogram template
        → SPAC core histogram visualization function
```

SPAC Shiny no longer performs template-owned validation or direct core
Histogram execution after this refactor. Its only figure processing is the
Task 6 presentation conversion that freezes the completed template layout
before Shiny can resize a mutable Matplotlib figure.

## Reactive and Resource Lifecycle

`get_adata()` and `get_features_inputs()` remain reactive calculations that
cache derived state until their dependencies invalidate. Because
`spac_Histogram_1()` is gated by `input.go_h1`, changes to those dependencies
do not render immediately; the next button click consumes their current
values. `build_template_params()` remains a normal function because it reads
only explicit arguments and owns no reactive state.

The registry entry exists only during template execution. Readiness checks and
input collection occur before registration. After registration succeeds,
parameter construction and template execution run inside the immediately
following `try/finally`; cleanup occurs in `finally`, and successful results
are processed afterward. The canonical PNG is then written to a closed
temporary file for `render.image`, which deletes it after successful delivery.

The wrapper must currently be imported before the Histogram template because
the template imports `load_input` by name. This import-order constraint and
the global memory registry are compatibility properties of the current
path-based template interface, not intended Shiny application state.

Missing AnnData returns before registration. Unexpected template exceptions
propagate after cleanup. After successful cleanup, Task 6 serializes the
completed figure without changing its plot content; Task 10 publishes the
dataframe and returns the temporary PNG path through `render.image`. Existing
dataframe download and button-gated behavior remain unchanged.

## Verification Boundaries

Developer-run Shiny verification covers:

- semantic input normalization for ordinary and grouped non-facet paths;
- preservation of `go_h1`-gated rendering, current plotting controls, and
  dataframe download behavior;
- proportional display of the template's 300-DPI artifact at normal browser
  zoom on the supported desktop displays.

Static review checks the exact Histogram template parameter mapping,
`run_from_json(..., save_to_disk=False, show_plot=False)`, returned figure and
dataframe handling, and guaranteed memory-registry cleanup. Comprehensive
automated adapter verification is postponed to the specialized SWE stage;
stable reusable utilities should still receive focused tests when appropriate.

## Development Boundaries

```text
Included:
  canonical AnnData access
  current semantic Features input snapshot
  semantic-to-template payload conversion
  memory-registry execution
  Histogram template delegation
  canonical-PNG display adaptation and dataframe return
  existing human button-gated behavior
  focused adapter and compatibility verification

Deferred:
  static conditional-panel replacement for current dynamic controls
  agent-to-UI parameter registry
  agent inspection and update commands
  agent render requests
  current-versus-last-rendered provenance state
  facet UI and additional histogram controls
  plot caching and PNG download delivery
  persistent state, JSON/CLI endpoints, and broad UI cleanup
```

## Final Aimed Features Architecture

The future architecture extends this adapter baseline with static controls,
conditional visibility, a stable semantic registry, and two peer interaction
paths. Parameter updates remain separate from explicit render requests;
human and agent render requests converge on the same Features renderer.

```text
                         ┌─────────────────────────┐
                         │ Canonical AnnData       │
                         │ + available choices     │
                         └────────────┬────────────┘
                                      │ constrains
                                      ▼
┌──────────────┐       ┌──────────────────────────────────┐       ┌──────────────┐
│ Human user   │◄─────►│ Static Features UI / Shiny state│◄─────►│ AI agent     │
│              │       │                                  │       │              │
│ edits inputs │       │ all controls always exist;       │       │ inspects and │
│ reviews plot │       │ conditional panels hide/show     │       │ validates    │
└──────┬───────┘       └────────────────┬─────────────────┘       │ semantic     │
       │                                │                         │ updates      │
       │ clicks Render                  │ normalized by           └──────┬───────┘
       │                                ▼                                │
       │                    ┌─────────────────────────┐                   │
       │                    │ get_features_inputs()   │                   │
       │                    │ semantic effective state│                   │
       │                    └────────────┬────────────┘                   │
       │                                 │                                │
       │                                 │                 explicit agent │
       │                                 │                 render request │
       └──────────────────────┐          │          ┌─────────────────────┘
                              ▼          ▼          ▼
                         ┌─────────────────────────┐
                         │ Shared render request   │
                         │ origin: human | agent   │
                         └────────────┬────────────┘
                                      ▼
                         ┌─────────────────────────┐
                         │ Immutable render snapshot│
                         │ semantic state + data    │
                         └────────────┬────────────┘
                                      ▼
                         ┌─────────────────────────┐
                         │ build_template_params() │
                         └────────────┬────────────┘
                                      ▼
                         ┌─────────────────────────┐
                         │ Memory registry         │
                         │ memory:// canonical data│
                         └────────────┬────────────┘
                                      ▼
                         ┌─────────────────────────┐
                         │ Histogram template      │
                         │ → core histogram        │
                         └────────────┬────────────┘
                                      ▼
                         ┌─────────────────────────┐
                         │ Figure + dataframe      │
                         │ + render provenance     │
                         └───────┬─────────┬───────┘
                                 │         │
                                 ▼         ▼
                         Features plot/   Agent result
                         download state   context/status
```
