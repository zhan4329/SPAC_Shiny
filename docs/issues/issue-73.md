# SPAC Template Integration Guide for Shiny

> A guide for integrating `spac.templates` into Shiny for Python visualizations.

## Why Use SPAC Templates?

SPAC templates (`spac.templates.*`) provide **production-ready** visualization functions with:

- **Complete feature coverage** — All parameters (plot types, colors, fonts, faceting) are exposed
- **Consistent output** — Returns both figures and dataframes for download
- **Validated parameters** — Built-in input validation and error handling
- **Galaxy/NIDAP compatibility** — Same code works across platforms

**The Goal:** Instead of reimplementing visualization logic in Shiny, we leverage templates via `run_from_json()` to get full functionality with minimal code.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        SHINY APPLICATION                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   ui/feature_ui.py              server/feature_server.py            │
│   ┌─────────────────┐           ┌─────────────────────────────┐     │
│   │ Core Parameters │           │ 1. Get adata from shared    │     │
│   │ Plot Options    │──input───▶│ 2. Register in memory       │     │
│   │ Figure Settings │           │ 3. Build params dict        │     │
│   └─────────────────┘           │ 4. Call run_from_json()     │     │
│                                 │ 5. Cleanup & return fig     │     │
│                                 └─────────────────────────────┘     │
│                                            │                         │
│                                            ▼                         │
│                        utils/template_wrapper.py                     │
│                        ┌─────────────────────────┐                   │
│                        │ Memory Registry         │                   │
│                        │ • register_memory_object│                   │
│                        │ • unregister (cleanup)  │                   │
│                        └─────────────────────────┘                   │
│                                            │                         │
│                                            ▼                         │
│                        spac.templates.your_template                  │
│                        ┌─────────────────────────┐                   │
│                        │ run_from_json(params)   │                   │
│                        │ → (figure, dataframe)   │                   │
│                        └─────────────────────────┘                   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Example for Step-by-Step Implementation

### Step 1: Create the UI Module (`ui/feature_ui.py`)

Organize parameters into **collapsible sections**:

```python
"""
Feature visualization UI module.
"""
from shiny import ui


def feature_ui():
    """Create the feature visualization UI."""
    return ui.nav_panel(
        "Feature Name",
        ui.card(
            ui.row(
                # Left panel: Controls (3 columns)
                ui.column(3, _controls_panel()),
                # Right panel: Plot output (9 columns)
                ui.column(9, _plot_panel())
            )
        )
    )


def _controls_panel():
    """Build the controls panel with organized sections."""
    return ui.div(
        {"class": "controls-panel"},
        
        # === SECTION 1: Core Parameters (always visible) ===
        ui.h4("Core Parameters"),
        ui.input_select("feat_source", "Source Label", choices=[]),
        ui.input_selectize("feat_targets", "Target Labels",
                          choices=[], multiple=True),
        
        ui.hr(),
        
        # === SECTION 2: Plot Configuration (collapsible) ===
        _collapsible_section(
            checkbox_id="feat_show_plot_config",
            label="Show Plot Configuration",
            content=[
                ui.input_select("feat_plot_type", "Plot Type",
                               choices=["boxen", "violin", "box"]),
                ui.input_checkbox("feat_log_scale", "Log Scale", value=False),
                ui.input_checkbox("feat_facet", "Facet Plot", value=False),
            ]
        ),
        
        ui.hr(),
        
        # === SECTION 3: Figure Configuration (collapsible) ===
        _collapsible_section(
            checkbox_id="feat_show_figure_config",
            label="Show Figure Configuration",
            content=[
                ui.row(
                    ui.column(6, ui.input_numeric("feat_width", "Width", 
                                                  value=10, min=4, max=20)),
                    ui.column(6, ui.input_numeric("feat_height", "Height",
                                                  value=6, min=3, max=15)),
                ),
                ui.row(
                    ui.column(6, ui.input_numeric("feat_font_size", "Font Size",
                                                  value=11, min=8, max=20)),
                    ui.column(6, ui.input_numeric("feat_dpi", "DPI",
                                                  value=150, min=72, max=600)),
                ),
            ]
        ),
        
        ui.br(),
        
        # === Generate Button ===
        ui.input_action_button("go_feat", "Generate Visualization",
                              class_="btn-success w-100"),
        ui.div({"style": "padding-top: 15px;"},
               ui.output_ui("download_button_ui_feat"))
    )


def _collapsible_section(checkbox_id, label, content):
    """Create a collapsible section with checkbox toggle."""
    return ui.div(
        ui.input_checkbox(checkbox_id, label, value=False),
        ui.panel_conditional(
            f"input.{checkbox_id}",
            *content
        )
    )


def _plot_panel():
    """Build the plot output panel."""
    return ui.div(
        {"class": "plot-container"},
        ui.output_plot("feat_plot", width="100%", height="700px")
    )
```

### Step 2: Create the Server Module (`server/feature_server.py`)

Follow this **exact pattern** for template integration:

```python
"""
Feature visualization server module.
"""
from shiny import ui, render, reactive, req

# Import template wrapper utilities
from utils.template_wrapper import (
    register_memory_object,
    unregister_memory_object,
)
# Import the specific template
from spac.templates.your_template import run_from_json


def feature_server(input, output, session, shared):
    """
    Server logic for feature visualization.

    Parameters
    ----------
    input, output, session : shiny bindings
        Standard Shiny server arguments.
    shared : dict
        Shared reactive values (expects 'adata_main', 'df_feature').
    """

    # === Reactive Calculations for Input Processing ===
    
    @reactive.calc
    def get_adata():
        """Get the main AnnData object from shared state."""
        return shared['adata_main'].get()

    @reactive.calc
    def get_targets():
        """Process target selection (None means 'All')."""
        targets = input.feat_targets()
        return list(targets) if targets else None

    # === Main Plot Rendering ===
    
    @output
    @render.plot
    @reactive.event(input.go_feat, ignore_none=True)
    def feat_plot():
        """Generate the visualization plot."""
        adata = get_adata()
        if adata is None:
            return None

        # Validate required inputs
        source = input.feat_source()
        if not source:
            return None

        # === KEY PATTERN: Memory Registry + run_from_json ===
        virtual_path = None
        try:
            # 1. Register adata in memory registry
            virtual_path = register_memory_object(adata)

            # 2. Build parameter dictionary matching template signature
            params = {
                "Upstream_Analysis": virtual_path,
                "Source_Label": source,
                "Target_Labels": ",".join(get_targets()) if get_targets() else "All",
                "Plot_Type": input.feat_plot_type(),
                "Log_Scale": input.feat_log_scale(),
                "Facet_Plot": input.feat_facet(),
                "Figure_Width": input.feat_width(),
                "Figure_Height": input.feat_height(),
                "Figure_DPI": input.feat_dpi(),
                "Font_Size": input.feat_font_size(),
            }

            # 3. Call template - returns (figure, dataframe)
            figs, df_data = run_from_json(
                json_path=params,
                save_results=False,  # Don't save to disk
                show_plot=False       # Don't display inline
            )

            # 4. Store dataframe for download
            shared['df_feature'].set(df_data)

            # 5. Handle single figure or list of figures
            if isinstance(figs, list):
                return figs[0] if figs else None
            return figs

        except Exception:
            import traceback
            traceback.print_exc()
            return None

        finally:
            # 6. ALWAYS cleanup memory registry
            if virtual_path:
                unregister_memory_object(virtual_path)

    # === Download Functionality ===
    
    @render.download(filename="feature_data.csv")
    def download_df_feat():
        """Download the data as CSV."""
        df = shared['df_feature'].get()
        if df is not None:
            return df.to_csv(index=False).encode("utf-8"), "text/csv"
        return None

    @render.ui
    @reactive.event(input.go_feat, ignore_none=True)
    def download_button_ui_feat():
        """Show download button when data is available."""
        if shared['df_feature'].get() is not None:
            return ui.download_button(
                "download_df_feat", "Download Data", class_="btn-warning"
            )
        return None
```

---

## The Memory Registry Pattern

The `template_wrapper.py` solves a key challenge: **templates expect file paths, but Shiny has in-memory data.**

```python
# How it works:
from utils.template_wrapper import register_memory_object, unregister_memory_object

# 1. Register your adata object
virtual_path = register_memory_object(adata)  # Returns "memory://abc123..."

# 2. Pass virtual_path as "Upstream_Analysis" parameter
params = {"Upstream_Analysis": virtual_path, ...}

# 3. Template's load_input() is patched to recognize "memory://" paths
#    and return the in-memory object instead of reading from disk

# 4. ALWAYS cleanup after use
unregister_memory_object(virtual_path)
```

**Why use `try/finally`?** To ensure cleanup happens even if an error occurs.

---

## Reusable UI Components

### Create Shared Components in `utils/`

For parameters used across multiple visualizations:

```python
# utils/ui_components.py
"""Reusable UI components for visualization modules."""
from shiny import ui


def figure_config_inputs(prefix: str):
    """
    Create standard figure configuration inputs.
    
    Parameters
    ----------
    prefix : str
        Unique prefix for input IDs (e.g., 'nn', 'rl', 'box')
    
    Returns
    -------
    list
        List of UI elements for figure configuration
    """
    return [
        ui.row(
            ui.column(6, ui.input_numeric(
                f"{prefix}_width", "Width", value=10, min=4, max=20)),
            ui.column(6, ui.input_numeric(
                f"{prefix}_height", "Height", value=6, min=3, max=15)),
        ),
        ui.row(
            ui.column(6, ui.input_numeric(
                f"{prefix}_font_size", "Font Size", value=11, min=8, max=20)),
            ui.column(6, ui.input_numeric(
                f"{prefix}_dpi", "DPI", value=150, min=72, max=600)),
        ),
    ]


def tooltip(text: str):
    """Create an accessible info tooltip."""
    return ui.tags.span(
        "\u24D8",  # ⓘ Unicode
        title=text,
        tabindex="0",
        class_="accessible-tooltip",
        style="margin-left:5px; cursor:help; color:#007bff;"
    )


def generate_button(button_id: str, label: str = "Generate Visualization"):
    """Create a standardized generate button."""
    return ui.input_action_button(
        button_id, label, class_="btn-success w-100"
    )
```

### Usage in UI Modules

```python
from utils.ui_components import figure_config_inputs, tooltip, generate_button

# In your UI:
ui.input_select(
    "nn_source",
    ui.tags.span("Source Label", tooltip("Select the anchor cell phenotype")),
    choices=[]
),
*figure_config_inputs("nn"),  # Unpacks the list
generate_button("go_nn")
```

---

## Checklist for New Visualizations

- [ ] **Find the template:** Check `spac/templates/` for `visualize_*_template.py`
- [ ] **Study parameters:** Look at `run_from_json()` signature and docstring
- [ ] **Create UI module:** `ui/feature_ui.py` with three collapsible sections
- [ ] **Create server module:** `server/feature_server.py` using memory registry pattern
- [ ] **Add shared state:** In `app.py`, add `shared['df_feature'] = reactive.Value(None)`
- [ ] **Wire up in app.py:** Import and call both `feature_ui()` and `feature_server()`
- [ ] **Test download:** Ensure CSV download works correctly
- [ ] **Reuse components:** Check `utils/` before creating new styling/inputs

---

## Quick Reference: Parameter Mapping

| UI Input Type | Template Parameter Format | Example |
|---------------|--------------------------|---------|
| `input_select` (single) | String directly | `input.feat_plot_type()` |
| `input_selectize` (multiple) | Comma-separated or list | `",".join(input.targets())` |
| `input_checkbox` | Boolean | `input.feat_log_scale()` |
| `input_numeric` | Integer/Float | `input.feat_width()` |
| Empty/None | `"None"` string or `None` | `image_id or "None"` |

---

## Example: `nearest_neighbor_server.py` Breakdown

```python
# Key sections annotated:

# 1. IMPORTS - template wrapper + specific template
from utils.template_wrapper import register_memory_object, unregister_memory_object
from spac.templates.visualize_nearest_neighbor_template import run_from_json

# 2. REACTIVE CALCS - process inputs before use
@reactive.calc
def process_target_labels():
    targets = input.nn_target_label()
    return list(targets) if targets else None

# 3. MAIN PLOT - triggered by button, uses try/finally
@output
@render.plot
@reactive.event(input.go_nn_viz, ignore_none=True)
def nn_visualization_plot():
    # ... validation ...
    
    virtual_path = register_memory_object(adata)
    try:
        params = { ... }  # Map all UI inputs to template params
        figs, df_data = run_from_json(json_path=params, save_results=False, show_plot=False)
        shared['df_nn'].set(df_data)
        return figs[0] if isinstance(figs, list) else figs
    finally:
        unregister_memory_object(virtual_path)

# 4. DOWNLOAD - standard pattern
@render.download(filename="nearest_neighbor_data.csv")
def download_df_nn():
    df = shared['df_nn'].get()
    if df is not None:
        return df.to_csv(index=False).encode("utf-8"), "text/csv"
```

---

## Common Pitfalls

| Issue | Solution |
|-------|----------|
| Plot not updating | Ensure `@reactive.event(input.button_id)` is set |
| Memory leak | Always use `try/finally` with `unregister_memory_object()` |
| "None" vs `None` | Templates expect string `"None"`, not Python `None` |
| Missing parameters | Check template docstring for required vs optional params |
| Download not working | Verify `shared['df_*'].set()` is called before render |

---

## Further Reading

- [`docs/REACTIVE_ARCHITECTURE.md`](./REACTIVE_ARCHITECTURE.md) — Reactive patterns in detail
- [`utils/template_wrapper.py`](../utils/template_wrapper.py) — Memory registry implementation
- [`server/nearest_neighbor_server.py`](../server/nearest_neighbor_server.py) — Complete example
- [`server/ripleyL_server.py`](../server/ripleyL_server.py) — Simpler example
