"""
Feature histogram visualization module for SPAC Shiny application.

This module handles the server-side logic for generating feature histograms
through the standard SPAC Histogram template workflow.
"""

import tempfile

from shiny import ui, render, reactive

# Import plot display utilities.
from utils.plot_utils import fig_to_png_bytes
# Import template wrapper utilities.
from utils.template_wrapper import (
    register_memory_object,
    unregister_memory_object,
)
# Import the specific template
from spac.templates.histogram_template import run_from_json


def features_server(input, output, session, shared):
    """
    Server logic for the feature histogram visualization.

    Parameters
    ----------
    input : shiny.session.Inputs
        Shiny input object
    output : shiny.session.Outputs
        Shiny output object
    session : shiny.session.Session
        Shiny session object
    shared : dict
        Shared reactive values across server modules
    """

    @reactive.calc
    def get_adata():
        """Get the main AnnData object from shared state."""
        return shared['adata_main'].get()

    @reactive.calc
    def get_features_inputs():
        """Return normalized semantic state from the Features controls."""

        group_by_enabled = input.h1_group_by_check()
        group_by = input.h1_anno() if group_by_enabled else None
        together = input.h1_together_check() if group_by_enabled else False
        multiple = input.h1_together_drop() if together else "stack"

        return {
            "feature": input.h1_feat(),
            "layer": (
                input.h1_layer() if input.h1_layer() != "Original" else None
            ),
            "x_log_scale": input.h1_log_x(),
            "y_log_scale": input.h1_log_y(),
            "group_by": group_by,
            "together": together,
            "multiple": multiple,
            "x_axis_label_rotation": input.feat_slider(),
        }

    def build_template_params(input_values, virtual_path):
        """Convert normalized semantic values to template parameters.

        The template supplies defaults for controls not exposed by the UI.
        """

        return {
            "Upstream_Analysis": virtual_path,
            "Feature": input_values["feature"] or "None",
            "Table_": input_values["layer"] or "Original",
            "Group_by": input_values["group_by"] or "None",
            "Together": input_values["together"],
            "Take_X_Log": input_values["x_log_scale"],
            "Take_Y_log": input_values["y_log_scale"],
            "Multiple": input_values["multiple"],
            "X_Axis_Label_Rotation": input_values["x_axis_label_rotation"],
            "Plot_By": "Feature",  # Features tab invariant
            "Facet": False,  # Facet UI deferred
        }

    @output
    @render.image(delete_file=True)
    @reactive.event(input.go_h1, ignore_none=True)
    def spac_Histogram_1():
        """Generate a feature histogram through the SPAC template."""

        adata = get_adata()
        if adata is None:
            return None
        features_inputs = get_features_inputs()

        virtual_path = register_memory_object(adata)
        try:
            params = build_template_params(features_inputs, virtual_path)
            fig, df = run_from_json(
                json_path=params,
                save_to_disk=False,
                show_plot=False,
            )
        finally:
            unregister_memory_object(virtual_path)

        png_bytes = fig_to_png_bytes(fig)
        with tempfile.NamedTemporaryFile(
            prefix="spac_feature_histogram_",
            suffix=".png",
            delete=False,
        ) as temp_file:
            temp_file.write(png_bytes)
            temp_path = temp_file.name

        shared['df_histogram1'].set(df)
        return {
            "src": temp_path,
            "width": "100%",
            "height": "100%",
            "style": "object-fit: contain;",
            "alt": "Feature histogram",
        }

    histogram_ui_initialized = reactive.Value(False)


    @render.download(filename="features_histogram_data.csv")
    def download_histogram1_df():
        df = shared['df_histogram1'].get()
        if df is not None:
            csv_string = df.to_csv(index=False)
            csv_bytes = csv_string.encode("utf-8")
            return csv_bytes, "text/csv"
        return None


    @render.ui
    @reactive.event(input.go_h1, ignore_none=True)
    def download_histogram1_button_ui():
        if shared['df_histogram1'].get() is not None:
            return ui.download_button(
                "download_histogram1_df", 
                "Download Data", 
                class_="btn-warning"
            )
        return None


    @reactive.effect
    def histogram_reactivity():
        btn = input.h1_group_by_check()
        ui_initialized = histogram_ui_initialized.get()

        if btn and not ui_initialized:
            dropdown = ui.input_select(
                "h1_anno", 
                "Select an Annotation", 
                choices=shared['obs_names'].get()
            )
            ui.insert_ui(
                ui.div({"id": "inserted-dropdown"}, dropdown),
                selector="#main-h1_dropdown",
                where="beforeEnd",
            )

            together_check = ui.input_checkbox(
                "h1_together_check", 
                "Plot Together", 
                value=True
            )
            ui.insert_ui(
                ui.div({"id": "inserted-check"}, together_check),
                selector="#main-h1_check",
                where="beforeEnd",
            )

            histogram_ui_initialized.set(True)

        elif not btn and ui_initialized:
            ui.remove_ui("#inserted-dropdown")
            ui.remove_ui("#inserted-check")
            ui.remove_ui("#inserted-dropdown_together")
            histogram_ui_initialized.set(False)


    @reactive.effect
    @reactive.event(input.h1_together_check)
    def update_stack_type_dropdown():
        if input.h1_together_check():
            dropdown_together = ui.input_select(
                "h1_together_drop", 
                "Select Stack Type", 
                choices=['stack', 'layer', 'dodge', 'fill'], 
                selected='stack'
            )
            ui.insert_ui(
                ui.div(
                    {"id": "inserted-dropdown_together"}, 
                    dropdown_together
                ),
                selector="#main-h1_together_drop",
                where="beforeEnd",)      
        else:
            ui.remove_ui("#inserted-dropdown_together")
