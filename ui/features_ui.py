from shiny import ui
from utils.accessibility import accessible_slider


def features_ui():
    # 3. FEATURES PANEL (Histogram) --------------------------
    return ui.nav_panel(
        "Features",
        ui.card(
            {"style": "width:100%;"},
            ui.row(
                ui.column(3, _controls_panel()),
                ui.column(9, _plot_panel())
            )
        )
    )


def _controls_panel():
    return ui.div(
        {"class": "controls-panel"},

        # === SECTION 1: Core Parameters (always visible) ===
        ui.h4("Core Parameters"),
        ui.input_select(
            "h1_feat",
            "Select a Feature",
            choices=[]
        ),
        ui.input_select(
            "h1_layer",
            "Select a Table",
            choices=[],
            selected=["Original"]
        ),

        ui.hr(),

        # === SECTION 2: Plot Configuration (collapsible) ===
        _collapsible_section(
            checkbox_id="h1_show_plot_config",
            label="Show Plot Configuration",
            content=[
                ui.input_checkbox(
                    "h1_group_by_check",
                    "Group By",
                    value=False
                ),
                ui.panel_conditional(
                    "input.h1_group_by_check",
                    ui.input_select(
                        "h1_anno",
                        "Select an Annotation",
                        choices=[]
                    ),
                    ui.input_checkbox(
                        "h1_together_check",
                        "Plot Together",
                        value=True
                    ),
                    ui.panel_conditional(
                        "input.h1_together_check",
                        ui.input_select(
                            "h1_together_drop",
                            "Select Stack Type",
                            choices=["stack", "layer", "dodge", "fill"],
                            selected="stack"
                        )
                    )
                ),
                ui.input_checkbox(
                    "h1_log_x",
                    "Log X-axis",
                    value=False
                ),
                ui.input_checkbox(
                    "h1_log_y",
                    "Log Y-axis",
                    value=False
                )
            ]
        ),

        ui.hr(),

        # === SECTION 3: Figure Configuration (collapsible) ===
        _collapsible_section(
            checkbox_id="h1_show_figure_config",
            label="Show Figure Configuration",
            content=[
                accessible_slider(
                    "feat_slider",
                    "Rotate X-axis Labels (degrees)",
                    min_val=0,
                    max_val=90,
                    value=0,
                    step=1
                )
            ]
        ),

        ui.br(),

        # === Generate Button ===
        ui.input_action_button(
            "go_h1",
            "Render Plot",
            class_="btn-success w-100"
        ),
        ui.div(
            {"style": "padding-top: 20px;"},
            ui.output_ui("download_histogram1_button_ui")
        )
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
    return ui.div(
        {"style": "padding-bottom: 100px;"},
        ui.output_image(
            "spac_Histogram_1",
            width="100%",
            height="60vh"
        )
    )
