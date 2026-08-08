# Features Server Architecture

This document describes the target architecture after the Features template
adapter refactor. The current implementation and the intended transition are
summarized below.

## Current Implementation

- `app.py` stores the canonical AnnData object in
  `shared["adata_main"]` and also maintains projected reactive values
  for UI choices.
- `features_server.py` currently reconstructs AnnData from
  `X_data`, `obs_data`, `var_data`, and
  `layers_data`, then calls the direct
  `spac.visualization.histogram()` API.
- The Features UI already has button-gated rendering, dataframe downloads,
  and dynamically inserted Group By/Together controls.
- `utils/template_wrapper.py` already provides the process-local memory
  registry used by the other template-based servers.

The refactor changes only the Features data and template boundary. The
projected reactive values remain available for UI choice updates.

## Component Structure

```text
features_server()
├── get_adata()                  reactive calculation
├── get_features_inputs()        reactive input snapshot
├── spac_Histogram_1()           button-gated template render
├── download_histogram1_df()     dataframe download
├── download_histogram1_button_ui()
├── histogram_reactivity()       dynamic Group By UI
└── update_stack_type_dropdown() dynamic Together UI
```

## Data Flow

```text
Shiny inputs ──► get_features_inputs() ── input values ──┐
                                                        ▼
get_adata() ──► register_memory_object() ── virtual path ──►
                                                        │
                                                        ▼
                                      build_template_params(...)
                                                        │
                                                        ▼
                                                 run_from_json()
                                                        │
                                      ┌─────────────────┴─────────────────┐
                                      ▼                                   ▼
                                figure → plot output        dataframe → shared["df_histogram1"]
```

## Reactive Boundaries

```python
@reactive.calc
def get_adata():
    return shared["adata_main"].get()


@reactive.calc
def get_features_inputs():
    ...


@render.plot
@reactive.event(input.go_h1, ignore_none=True)
def spac_Histogram_1():
    ...
```

- `get_adata()` reads the shared main `AnnData` object.
- `get_features_inputs()` reads the current visible Features inputs.
- `spac_Histogram_1()` renders only when `go_h1` is clicked.
- Dynamic UI effects remain separate from template execution.
- Download handlers read the dataframe stored in shared reactive state.

## Parameter Layers

### Agent-to-UI Registry

```python
FEATURE_INPUT_REGISTRY = {
    "feature": {"input_id": "h1_feat", "update_type": "select"},
    "table": {"input_id": "h1_layer", "update_type": "select"},
    "log_x": {"input_id": "h1_log_x", "update_type": "checkbox"},
    "log_y": {"input_id": "h1_log_y", "update_type": "checkbox"},
    "x_axis_rotation": {
        "input_id": "feat_slider",
        "update_type": "slider",
    },
    "group_by_enabled": {
        "input_id": "h1_group_by_check",
        "update_type": "checkbox",
    },
    "annotation": {"input_id": "h1_anno", "update_type": "select"},
    "together": {
        "input_id": "h1_together_check",
        "update_type": "checkbox",
    },
    "multiple": {
        "input_id": "h1_together_drop",
        "update_type": "select",
    },
}
```

The registry maps stable semantic names to visible Shiny controls. Agent
updates use the corresponding `ui.update_*()` functions. Shiny inputs remain
the source of truth. The dynamically inserted controls are read and updated
only when Group By has initialized them.

### Template Payload

```python
def build_template_params(input_values, virtual_path):
    return {
        "Upstream_Analysis": virtual_path,
        "Feature": input_values["feature"],
        "Table_": input_values["table"] or "None",
        "Take_X_Log": input_values["log_x"],
        "Take_Y_Log": input_values["log_y"],
        "Group_by": input_values["group_by"] or "None",
        "Together": input_values["together"],
        "Multiple": input_values["multiple"],
        "X_Axis_Label_Rotation": input_values["x_axis_rotation"],
        "Max_Groups": 20,
        "Plot_By": "Feature",
        "Annotation": "None",
        "Bins": "auto",
        "Stat": "count",
        "Facet": False,
        "Facet_Ncol": "auto",
        "Figure_Width": 8,
        "Figure_Height": 6,
        "Font_Size": 12,
        "Figure_DPI": 300,
    }
```

The template payload is created for each render and is not persistent state.

## Template Execution

```text
get_adata()
    ▼
register_memory_object(adata)
    ▼
build_template_params(...)
    ▼
run_from_json(..., save_to_disk=False, show_plot=False)
    ▼
store dataframe and return figure
    ▼
unregister_memory_object(...) in finally
```

The registered object is the exact canonical AnnData object; it is not copied
or reconstructed for the template call. Registration must be cleaned up on
both successful and failed execution.

The SPAC dependency baseline and compatibility checks are tracked in the
prerequisite [compatibility PR](../../../chore/pin-spac-to-pr-433/).

## Boundaries

```text
Included:    adapter, current inputs, template payload, memory registry,
             dataframe return, agent-to-UI registry

Excluded:    facet UI, new histogram controls, persistent state model,
             JSON/CLI endpoint, broad UI cleanup
```
